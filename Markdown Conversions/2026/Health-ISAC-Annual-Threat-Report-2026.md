# 2026 Global Health Sector Threat Landscape

**Organization:** Health  
**Report Title:** ISAC-Annual-Threat-Report  
**Year:** 2026  
**Date:** January 2026  
**TLP:** WHITE (This report may be shared without restriction.)

## Table of Contents
- [Introduction](#introduction)
- [Annual Member Survey Insights](#annual-member-survey-insights)
  - [Survey Background](#survey-background)
  - [Survey Findings](#survey-findings)
  - [Key Insights](#key-insights)
- [Part I: The Current Threat Landscape](#part-i-the-current-threat-landscape)
  - [Physical Security](#physical-security)
  - [Physical Security / Violence Legislation – U.S. and Global](#physical-security--violence-legislation--us-and-global)
  - [Man-Made and Natural Threats to Security](#man-made-and-natural-threats-to-security)
  - [Cybercriminal Activity](#cybercriminal-activity)
  - [Hacktivist Attacks Against the Health Sector](#hacktivist-attacks-against-the-health-sector)
  - [Data Breaches — Episource](#data-breaches--episource)
  - [Significant Takedowns](#significant-takedowns)
  - [Ransomware Gangs Attacking Health Sector](#ransomware-gangs-attacking-health-sector)
  - [Ransomware Trends in the Health Sector](#ransomware-trends-in-the-health-sector)
  - [Nation-State Activity](#nation-state-activity)
  - [Geopolitical Activity](#geopolitical-activity)
  - [Medical Device Cybersecurity](#medical-device-cybersecurity)
- [Part II: Tactics, Techniques, and Procedures](#part-ii-tactics-techniques-and-procedures)
  - [Social Engineering](#social-engineering)
  - [QR Code Phishing](#qr-code-phishing)
  - [Cleo Compromise Victim Bundling](#cleo-compromise-victim-bundling)
  - [Malicious Activity Observed by Members](#malicious-activity-observed-by-members)
  - [Breakdown of 2025 MITRE ATT&CK Data](#breakdown-of-2025-mitre-attck-data)
  - [Notable Vulnerabilities](#notable-vulnerabilities)
  - [Popular Targeted Alerts](#popular-targeted-alerts)
- [Part III: Future Cybersecurity Outlook](#part-iii-future-cybersecurity-outlook)
  - [Business Resilience](#business-resilience)
  - [Business Resiliency Looking into 2026](#business-resiliency-looking-into-2026)
- [Conclusion](#conclusion)

---

## Introduction

2025 was defined by a critical escalation in the volume, complexity, and systemic risk facing the global health ecosystem. As the digital transformation of the health sector—from advanced medical devices to telehealth platforms—continued to accelerate, it expanded the attack surface, confirming that the health industry remains a primary, high-value target for cybercriminals and nation-state actors alike.

The primary threat facing the health sector remains ransomware, with prolific groups like Qilin, INC Ransom, and the rapidly growing SAFEPAY dominating the threat landscape. However, the most concerning trend is the continued pivot and acceleration by threat actors to supply chain exploitation. Major security incidents throughout the year repeatedly demonstrated that a provider’s security is only as strong as its weakest vendor link, leading to widespread compromises that impacted millions of patient records and forced a significant industry-wide reevaluation of third-party risk management.

Attack methodologies also evolved, requiring more advanced defenses. The proliferation of sophisticated social engineering techniques used in malware, such as ClickFix and FileFix, along with the emergence of QR code phishing (quishing), showcased an increasing reliance on methods that bypass traditional perimeter defenses by exploiting human trust. The evolving attack methodologies were often successfully countered, as demonstrated by the intervention of illegitimate Cobalt Strike usage and the successful takedown of the RaccoonO365 phishing-as-a-service infrastructure.

Compounding these cyber challenges is the unique duality of the health sector: the urgent need to secure life-critical operational technology and the exposure to geopolitical events. The security risks posed by legacy medical devices, particularly those approaching end-of-life, demanded immediate compensating controls to protect patient safety. Furthermore, 2025 saw the continued impact of nation-state cyber activity, from widespread remote IT worker fraud campaigns to hybrid warfare tactics that leveraged cybercriminal elements against geopolitical adversaries.

As we look toward 2026, the focus must shift from incident response to sustained Business Resilience. The lessons learned from massive disruptive events—such as the widespread impact from the faulty CrowdStrike update in July 2024—underscore the necessity for robust planning that goes beyond traditional cybersecurity and addresses operational continuity in the face of widespread third-party failure.

This report is structured to provide an in-depth analysis of these dynamics, offering clear insight into:

- **Part I: The Current Threat Landscape**: A deep dive into the most active cybercriminal groups, significant law enforcement takedowns, nation-state activity, and critical issues in medical device security.
- **Part II: Notable Tactics, Techniques, and Procedures (TTPs)**: A breakdown of the most effective initial access and evasion techniques used by adversaries.
- **Part III: Future Cybersecurity Outlook**: Strategic guidance on enhancing business resilience and preparing for the emerging risks of 2026.

By sharing intelligence and adopting a collaborative defense strategy, the health sector can build the collective resilience necessary to protect patients, staff, and critical services in the years ahead.

---

## Annual Member Survey Insights

### Survey Background

In November 2025, Health-ISAC conducted a survey of nearly 250 executives and cybersecurity professionals across the health sector. The survey included cyber (e.g., CISO) and non-cyber (e.g., CFO) executives across multiple health subsectors (e.g., providers, pharmaceutical companies, payers, medical device manufacturers, health IT) as well as healthcare organizations of varying sizes and IT/IS budgets.

Survey responses were received from members of:
- Health-ISAC
- The Association for the Advancement of Medical Instrumentation® (AAMI)
- Health Sector Coordinating Council Cybersecurity Working Group (HSCC CWG)

Health Security Professionals were asked to rank the five greatest cybersecurity concerns facing their organizations for 2025 and 2026 and Medical Device Manufacturers were also asked the top three challenges in developing secure medical devices for 2025 and 2026.

![Link to detailed survey results in the Health-ISAC Threat Intelligence Portal (HTIP)]

### Survey Findings

Health Sector Security Professionals ranked the top five cyber threats facing their organizations in 2025 as follows:
1. Ransomware Deployments
2. Phishing Attacks
3. Third Party/Partner Breaches
4. Data Breaches
5. Zero-Day Exploits

Health Sector Security Professionals ranked the top five cyber threats facing their organizations, looking ahead toward 2026, as follows:
1. AI-Enabled Attacks
2. Ransomware Deployments
3. Third Party Breaches
4. Zero-Day Exploits
5. Phishing/Spear Phishing

Medical Device Manufacturers reported the top three challenges in developing secure medical devices such as:
1. Integrating security into the design and development process
2. Providing regular and secure updating and patching for medical devices
3. Designing for the ongoing security of medical devices over their long operational lifespan

Conversely, the top three impacts on Healthcare Delivery Organizations were reported as:
1. Disruption in the normal operation of medical technology
2. Unauthorized access, theft, or exposure of patients' personal health information (PHI)
3. Disruption of overall hospital operations, including administrative processes, scheduling, and communication

### Key Insights

- The most significant consequences of cyberattacks on patient care were found to be the same in 2025 as those reported in 2024.
- Executives and cybersecurity practitioners reported the same concerns going into 2026, indicating a level of synergy across all levels of health sector cybersecurity.
- Member organizations with smaller cybersecurity budgets were more concerned by phishing in 2025, while those with larger budgets were more concerned by ransomware deployments.

---

## Part I: The Current Threat Landscape

### Physical Security

Throughout 2025, the health sector has maintained an increased focus on workplace violence and the safety of staff. Most recent reporting by the Bureau of Labor Statistics in 2023 states that healthcare was the industry where staff had the highest likelihood of experiencing violence in the workplace.[^1] This, combined with the assassination of a health insurance executive at the end of 2024, has caused an increased focus on physical security and executive protection measures, driving increased budget allocations to the safety of all employees.

### Physical Security / Violence Legislation – U.S. and Global

From a regulatory perspective in the United States, the Save Healthcare Workers Act (H.R. 3178/S.1600) was reintroduced to Congress for a third time on May 5, 2025. The legislation aims to make assault on a healthcare worker a felony offense. Another regulation aimed at increasing healthcare worker safety was The Workplace Violence Prevention for Health Care and Social Service Workers Act (H.R. 2531/S.1232), which was introduced to Congress for the fourth time on April 01, 2025. This act, if passed, would establish a federal standard for preventing workplace violence in healthcare environments. Working outside of the legislative process, health sector organizations have been implementing their own policies and using recommendations from the Occupational Safety and Health Administration to reduce workplace violence.[^2]

### Man-Made and Natural Threats to Security

The 2025 wildfire season in North America was marked by multiple major fires. It was the second-worst fire season on record in Canada in terms of total area burned.[^3]

The Atlantic hurricane season saw minimal activity, with fewer storms making landfall compared to recent years. The Pacific typhoon season also saw fewer overall storms, although Super Typhoon Fung-Wong caused severe damage in the Philippines in mid-November.[^4]

There were multiple significant viral outbreaks throughout the year, the largest of which was the resurgence of Chikungunya. According to the World Health Organization, there were potentially 445,271 cases and 155 deaths globally across 40 countries.[^5]

The 2025 outbreak of measles in the United States was the largest since 2000. It started in west Texas and quickly spread, with multiple cases appearing around the country.[^6]

Avian Influenza has remained a global concern through 2025, as concerns of viral adaptation that makes the disease become human-to-human transmissible continue. The Centers for Disease Control and Prevention reported 70 cases in the United States, with one death. The World Health Organization reported 18 cases with eight deaths across the Western Pacific Region.[^7]

The "50501" movement (short for "50 protests, 50 states, 1 movement") has been responsible for national protests on 10 different days across the United States, each growing in attendance and participation. The movement was founded with the intent of resisting perceived anti-democratic politics.[^8] The protests have had a large footprint and drawn in many participants. As they grow, there is an increased potential for disruptions to emergency medical services and business travel. The protests can also disrupt day-to-day operations in the healthcare industry, as they can pull staff and patients away who wish to participate. International activity related to the 50501 movement has manifested as coordinated solidarity demonstrations outside the US, primarily concentrated in Western Europe and key Asian capitals. These protests create localized physical security risks by restricting the freedom of movement around US government facilities, potentially delaying secure logistics and complicating emergency response protocols of personnel in the area.

Many nations have moved to categorize healthcare staff as a "protected class" or have increased penalties specifically for crimes committed against them. Here are several examples Health-ISAC is tracking around the world:

1. **United Kingdom — Assaults on Emergency Workers (Offences) Act 2018**: This is perhaps the most direct parallel to the U.S. legislation. This Act doubled the maximum sentence for common assault against "emergency workers" (including NHS staff, paramedics, and police) from six months to 12 months in prison (later increased to two years via the Police, Crime, Sentencing and Courts Act 2022).
2. **India — Epidemic Diseases (Amendment) Act 2020**: Following a surge in violence against doctors during the COVID-19 pandemic, India enacted significant federal protections. The amendment makes any act of violence against healthcare personnel a cognizable and non-bailable offense.
3. **Australia — State-Level "Health Worker" Protections**: New South Wales introduced new laws in 2022 making it a specific crime to assault a healthcare worker. Penalties range from 12 months to 14 years in prison.
4. **France — Loi n° 2021-502**: France has implemented specific criminal provisions to protect medical personnel, particularly those in emergency services.
5. **Armenia — 2025 Criminal Code Proposals**: As of mid-2025, Armenia is debating a draft law very similar to the current U.S. bill.

### Cybercriminal Activity

#### Hacktivist Attacks Against the Health Sector

Hacktivism involves using hacking techniques to promote a political or social cause. Hacktivist groups often leverage Distributed Denial of Service (DDoS) attacks to achieve their goals. Attackers are increasingly targeting business associates and third-party vendors that provide critical services to healthcare providers.

In June 2025, a Hacktivist group operating on Telegram within a channel dubbed *ServerKillers* orchestrated a temporary disruption of websites associated with Medical Centers in Israel in response to Israel’s strikes on Iran. The ServerKillers team is described as part of the larger *Killnet Collective*. The pro-Iran hacktivist group *Cyber Islamic Resistance* also attacked Israeli health sector entities in July 2025, including mental health hospitals, emergency rooms, and children’s hospitals.[^9][^10]

#### Data Breaches — Episource

Data breaches were identified as the fourth most severe concern for global health sector cybersecurity professionals in 2025. A ransomware-driven intrusion between January and February 2025 exposed data from over 5.4 million individuals. The data breach originated from a single vendor, Episource, a provider of risk adjustment services, software, and solutions for health plans and provider groups.[^11]

![Whitepaper: A New Era of Digital Warfare: Understanding and Mitigating Modern DDoS and RDoS Attacks]

### Significant Takedowns

#### Cybercriminal Cobalt Strike Usage Down 80%
Cobalt Strike is a legitimate penetration testing framework. In the first quarter of 2025, Fortra announced that abuse by threat actors had dropped by 80%, thanks largely to the joint Cobalt Strike disruption effort started in 2023.[^12]

#### RaccoonO365 Disruption
RaccoonO365 is a phishing-as-a-service kit used to steal user credentials and one-time login tokens. While used across industries, its phishing kits targeted more than 25 health sector organizations.[^13] In September 2025, a court order allowed Microsoft to seize 338 websites associated with RaccoonO365, disrupting the operation’s technical infrastructure.

### Ransomware Gangs Attacking Health Sector

Health-ISAC tracked 455 ransomware events across the health sector in 2025.

| Ransomware Gang | Number of Health Sector Entities Attacked |
| :--- | :--- |
| Qilin | 77 |
| INC Ransom | 50 |
| SAFEPAY | 23 |
| Sinobi | 21 |
| World Leaks | 18 |

- **Qilin**: A Russian-speaking RaaS group. Activity against the health sector soared in 2025, with nearly triple the victims compared to 2024.
- **INC Ransomware**: An RaaS operator active since 2023.
- **SAFEPAY**: A single sophisticated cybercriminal outfit. Attacks grew from 3 victims in 2024 to 21 in 2025.
- **Sinobi**: First observed in summer 2025, aggressively targeting the health sector.
- **WorldLeaks**: Suspected rebrand of Hunters International, prioritizing data theft over encryption.

### Ransomware Trends in the Health Sector

SAFEPAY, Qilin, and INC Ransomware have the highest percentage increase in victim count year-over-year. Conversely, Everest, BianLian, and Lockbit have reduced their health sector victim count.

**Health Sector Victimology (2025):**
- Hospitals and Health Care: 49.6%
- Medical Practice: 25.7%
- Medical Devices: 9.3%
- Biotechnology Research: 6.5%
- Mental Health Care: 4.6%
- Dentists: 4.3%

### Nation-State Activity

#### DPRK Remote IT Worker Campaigns
North Korea has continued its operation to secure remote IT jobs to generate revenue for weapons programs. Research from Okta suggests this campaign is expanding outside the US and increasing in scope.[^19]

### Geopolitical Activity

#### Israel-Iran War
On June 13, 2025, Israel launched Operation Rising Lion. During the 12-day war, various hacktivist groups targeted the health sector in Israel, including the use of "one-way ransomware" designed to destroy data rather than encrypt it for ransom.[^20]

#### Hybrid Warfare
In September 2025, Health-ISAC and CI-ISAC released a joint publication, *Melding of State and Criminal Threat Actor Motivation: The Nebulous Normal*, which examined the collaboration between nation-state intelligence agencies and cybercriminal elements.[^21]

### Medical Device Cybersecurity

#### Contec CMS 8000 Patient Monitor
On January 30, 2025, CISA issued advisory ICSMA-25-030-01 regarding severe vulnerabilities in Contec CMS8000 patient monitors, including hard-coded backdoor access. Cylera linked the hard-coded IP address to Tsinghua University in Beijing, China.[^22][^23]

#### Legacy Devices
On April 1, 2025, the U.S. House Energy & Commerce Oversight & Investigations Subcommittee held a hearing on the cybersecurity vulnerabilities of legacy medical devices. Since Windows 10 reached end-of-life on October 14, 2025, many devices require support through compensating controls.[^24]

#### DICOM/PACS Exposure
Of the 45 Health-ISAC medical device advisories issued in 2025, 19 specifically addressed DICOM/PACS vulnerabilities.[^26]

---

## Part II: Tactics, Techniques, and Procedures

### Social Engineering

#### ClickFix and FileFix
ClickFix uses phishing emails to redirect users to fake error pages, tricking them into copying and pasting malicious code. FileFix, emerging in 2025, exploits a browser's legitimate file upload feature to trick users into executing commands via the File Explorer's address bar.[^28]

### QR Code Phishing
"Quishing" exploits the assumed trust of QR codes. These attacks are particularly impactful because they often occur on personal mobile devices, which lack the robust endpoint security of enterprise-managed devices.

### Cleo Compromise Victim Bundling
The Cl0p ransomware group exploited vulnerabilities in the Cleo Managed File Transfer (MFT) software in late 2024 and early 2025, bundling hundreds of victims into one mass extortion campaign.

### Malicious Activity Observed by Members
1. **XWorm**: Remote access trojan (RAT) sold as commodity malware.
2. **NetSupportRAT**: Packaged to look like the legitimate NetSupport Manager tool.
3. **njRAT**: Long-standing malware capable of webcam control and credential theft.
4. **SocGholish**: Malware loader served through drive-by compromise.
5. **AsyncRAT**: Targets Windows systems to broker connections with C2 servers.

### Breakdown of 2025 MITRE ATT&CK Data
- **T1059.001**: Command and Scripting Interpreter: PowerShell
- **T1189**: Drive-by Compromise
- **T1204.004**: User Execution — Malicious Copy & Paste
- **T1566.002**: Spearphishing Link
- **T1219**: Remote Access Tools

### Notable Vulnerabilities
- **Microsoft SharePoint ToolShell (CVE-2025-53770)**: A critical RCE vulnerability (CVSS 9.8) exploited as a zero-day by groups linked to the Chinese government.
- **Cisco ASA 5500-X Series**: Critical vulnerabilities in perimeter firewalls/VPN gateways under active exploitation.

### Popular Targeted Alerts
Health-ISAC distributed over 1,200 Targeted Alerts in 2025.
1. **Dangling DNS**: 407 alerts.
2. **Citrix NetScaler**: 98 alerts.
3. **BeyondTrust**: 77 alerts.
4. **CEO Doxxing**: 54 alerts.
5. **RDP**: 41 alerts.

---

## Part III: Future Cybersecurity Outlook

### Business Resilience

The CrowdStrike Faulty Update in July 2024 caused measurable disruptions in 750 US hospitals. A 2025 Health-ISAC survey found that 69% of respondents were affected, with 80% of those reporting issues with electronic health records. 73% of organizations have since reassessed their business resiliency strategy.

### Business Resiliency Looking into 2026

Threats for 2026 include supply chain challenges, financial pressures, and the governance risks of AI. Health sector leaders are encouraged to utilize the *Health Industry Cybersecurity – Sector Mapping and Risk Toolkit (SMART)* published by the Health Sector Coordinating Council.[^40]

---

## Conclusion

In today's interconnected health sector, no organization is alone in facing cyber threats. Information sharing and collaboration through Health-ISAC is the key to building a unified front against cybercrime, protecting sensitive patient data, and ensuring the well-being of those we serve.

---

[^1]: https://www.bls.gov/iif/factsheets/workplace-violence-2021-2022.htm
[^2]: https://www.bls.gov/iif/factsheets/workplace-violence-2021-2022.htm
[^3]: https://www.cbc.ca/news/climate/wildfire-season-2025-1.7606371
[^4]: https://www.cbsnews.com/news/super-typhoon-fung-wong-philippines/
[^5]: https://www.sciencealert.com/outbreak-of-chikungunya-virus-poses-global-risk-warns-who
[^6]: https://www.who.int/emergencies/disease-outbreak-news/item/2025-DON561
[^7]: https://www.cdc.gov/bird-flu/h5-monitoring/index.html
[^8]: https://www.newsweek.com/50-states-anti-trump-protest-nationwide-50501-explainer-2026115
[^9]: https://twitter.com/FalconFeedsio/status/1947009260543791524
[^10]: https://twitter.com/FalconFeedsio/status/1946905848795546105
[^11]: https://www.hipaajournal.com/episource-data-breach/
[^12]: https://www.cobaltstrike.com/blog/update-stopping-cybercriminsignificantls-from-abusing-cobalt-strike
[^13]: https://www.microsoft.com/en-us/security/blog/2025/04/03/threat-actors-leverage-tax-season-to-deploy-tax-themed-phishing-campaigns/
[^19]: https://www.okta.com/newsroom/articles/north-korea-s-it-worke,rs-expand-beyond-us-big-tech/
[^20]: https://dailydarkweb.net/aptiran-allegedly-hits-israeli-critical-infrastructure-with-ransomware/
[^21]: https://health-isac.org/melding-of-state-and-criminal-threat-actor-motivation-the-nebulous-normal-whitepaper/
[^22]: https://claroty.com/team82/research/are-contec-cms8000-patient-monitors-infected-with-a-chinese-backdoor-the-reality-is-more-complicated
[^23]: https://cylera.com/blog/contec-patient-vital-signs-monitor-chinehat that se-backdoor-bad-design/
[^24]: https://www.congress.gov/event/119th-congress/house-event/118077
[^25]: https://health-isac.org/exploring-the-cybersecurity-roles-of-manufacturers-and-healthcare-organizations-during-the-medical-device-lifecycle/
[^26]: https://www.dreamsoft4u.com/blog/what-is-the-difference-between-dicom-and-pacs
[^27]: https://www.linkedin.com/posts/phil-englert-2642724_health-isac-protecting-pacs-tip-sheet-activity-7385033795650928640-gLIx
[^28]: https://blog.checkpoint.com/research/filefix-the-new-social-engineering-attack-building-on-clickfix-tested-in-the-wild/
[^29]: https://any.run/malware-trends/xworm/
[^30]: https://any.run/malware-trends/netsupport/
[^31]: https://any.run/malware-trends/njrat/
[^32]: https://attack.mitre.org/software/S1124/
[^33]: https://www.checkpoint.com/cyber-hub/threat-prevention/what-is-malware/asyncrat-malware-explained/
[^34]: https://health-isac.cyware.com/webapp/user/myfeeds/671361ad
[^35]: https://www.paloaltonetworks.com/cyberpedia/what-is-a-dangling-dns
[^36]: https://www.beyondtrust.com/trust-center/security-advisories/bt24-11
[^37]: https://www.securitymagazine.com/articles/101670-luigi-was-right-a-look-at-the-website-sharing-data-on-more-than-1-000-executives
[^38]: https://cybersecuritynews.com/microsoft-remote-desktop-protocol-services/
[^39]: https://health-isac.cyware.com/webapp/user/myfeeds/f2235d14
[^40]: https://healthsectorcouncil.org/smart-toolkit/

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