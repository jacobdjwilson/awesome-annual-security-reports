# 2025 Health Sector Cyber Threat Landscape

## Table of Contents
- [Introduction](#introduction)
- [Annual Member Survey Insights](#annual-member-survey-insights)
- [Key Insights](#key-insights)
- [Part I: Recent Attacks Against Healthcare](#part-i-recent-attacks-against-healthcare)
- [Part II: The Current Threat Landscape](#part-ii-the-current-threat-landscape)
- [Part III: Tactics, Techniques and Procedures](#part-iii-tactics-techniques-and-procedures)
- [Part IV: Future Cybersecurity Outlook](#part-iv-future-cybersecurity-outlook)
- [A Call to Action](#a-call-to-action)

---

# Introduction

2024 was a challenging year in cybersecurity for health sector systems around the world. The Health-ISAC 2025 Health Sector Cyber Threat Landscape highlights a continued escalation of cyberattacks. Key findings include a surge in ransomware attacks, with increasingly sophisticated techniques employed by threat actors. The report also emphasizes the growing threat of nation-state actors and cyber-espionage, targeting sensitive patient data and intellectual property. Furthermore, the rise of Internet of Medical Things (IoMT) devices has introduced new vulnerabilities, while the evolving threat landscape necessitates continuous adaptation of security measures for health sector organizations globally.

# Annual Member Survey Insights

### Survey Background
In Health-ISAC’s November 2024 survey, nearly 200 executives and cybersecurity professionals across the health sector completed a survey and ranked their top five “greatest cybersecurity concerns” facing their organizations for both 2024 and 2025. The survey included cyber (e.g., CISO) and non-cyber executives (e.g., CFO), multiple health subsectors (e.g., Providers, Pharma, Payers, Medical Device Manufacturers, Health IT) as well as healthcare organizations of varying size and IT/IS budget.

Survey responses were received from members of:
- Health-ISAC
- Association for the Advancement of Medical Instrumentation (AAMI)
- American College of Clinical Engineering (ACCE)

### Survey Findings
Health sector security professionals reported the Top Five Cyber Threats facing their organizations in 2024 as follows:
1. Ransomware
2. Phishing
3. Compromised Credentials
4. Third-Party Credentials
5. Data Breaches

Health sector security professionals reported the Top Five Cyber Threats facing their organizations looking ahead in 2025 are:
1. Ransomware Deployments
2. Third-Party Breaches
3. Data Breaches
4. Supply Chain Attacks
5. Zero-Day Exploits

Medical Device Manufacturers reported the top three challenges in developing secure medical devices as:
1. Integrating security into the design and development process.
2. Providing regular and secure updating and patching for medical devices.
3. Designing for the ongoing security of medical devices over their long operational lifespan.

Conversely, the top three impacts on Healthcare Delivery Organizations were reported as:
1. Disruption in the normal operation of medical technology, including such things as loss of diagnostic technology or loss of access to electronic medical records which may cause delay and disruption to patient care, such as diversion of patients and ambulances, canceled surgeries, or the need to revert to manual procedures.
2. Unauthorized access, theft, or exposure of patients’ personal health information (PHI), resulting in privacy violations and legal consequences.
3. Disruption of overall hospital operations, including administrative processes, scheduling, and communication.

# Key Insights
- The top three impacts on Healthcare Delivery Organizations remained the same from 2024 to 2025.
- Organizations with cybersecurity budgets in both the highest and lowest brackets listed AI-enabled attacks as their primary concern going into 2025 despite the collective consensus across the membership being ransomware deployments as the greatest threat going into 2025.
- The concerns going into 2025 reflect a highlighted concern about third-party breaches using zero-day exploits. Three of the top five concerns relate to this scenario, similar to the exploitation of MoveIT Managed File Transfer in 2023.

# Part I: Recent Attacks Against the Health Sector

### Patient Extortion
After a cyber-attack on the Integris Health System, in December 2023, patients of numerous hospitals, specialty care clinics, and other institutions began to receive emails from a threat actor attempting to blackmail them with data stolen in the cyber-attack. These emails alleged the threat actor had information from a stolen database that included the details of medical visits, social security numbers, and other sensitive Protected Health Information (PHI) belonging to patients. Victims were presented with three options. First, victims could pay $50 to delete their entry in the stolen dataset of approximately 500,000 records. Second, they could pay $3 to view what data was compromised in the attack. Finally, they could opt not to pay and be a part of the dataset that was going to be sold on the dark web.[^1]

Unfortunately, this is not an isolated incident. The previous year, patients from cancer centers were extorted using stolen mammogram pictures, and patients at plastic surgery clinics were extorted with stolen sensitive pre-operation photos. This worrying trend may begin to gain traction in 2025 as cybercriminal actors target healthcare even more.[^2]

> This worrying trend may begin to gain traction in 2025 as cybercriminal actors target healthcare even more.

### High-Impact Ransomware Attacks
**Payment Portal Outage**
Change Healthcare is a massive healthcare payment processing conglomerate that is widely adopted across American healthcare delivery organizations. According to some estimates, Change Healthcare processes about one in three healthcare transactions in the US.[^3] The ransomware attack that befell this organization in February 2024 created an outage that disrupted patient care in such a way that millions of patients could no longer pay for treatment or medication.

> Due to the payment portal outage, “millions of patients could no longer pay for treatment or medication.”

Affiliates of the ransomware as a service (RaaS) group, BlackCat/ALPHV, claimed responsibility for the attack. However, the administrators of the RaaS platform kept the money made from the hack, swindling the affiliates who carried out the attack on Change Healthcare. After this, the group decided to disband, announcing on social media that the RaaS operation had ended.[^4]

**Ascension Healthcare**
On May 8, 2024, Ascension Healthcare discovered a ransomware incident in their network. To remediate the situation, Ascension Health took many systems offline to reduce the impact of the incident. As a result, several functions of the large healthcare network were unavailable, resulting in massive disruptions to patient care across the 40 senior care facilities and 140 hospitals across 19 states. This incident caused lapses in access to electronic health records, making it much harder to treat patients. As a result, ambulances were diverted away from hospitals in the Ascension Healthcare network, and appointments were postponed. To respond to this incident, Health-ISAC worked with Ascension and shared Indicators of Compromise (IOCs) with the wider membership.[^5] The group responsible for the attack was Black Basta, a prolific ransomware gang.

Black Basta emerged in early 2022 and has continuously targeted healthcare organizations. Black Basta has used double extortion tactics to encrypt data and threaten to leak sensitive information, allegedly extorting over $100 million. Their malware targets Windows and Linux systems, employing sophisticated techniques to prevent detection and hinder file recovery. The threat actor used spearphishing attacks and was seen buying compromised credentials through Initial Access Brokers (IABs) to obtain means of initial access.

### Physical Security
Physical threats to the healthcare sector persisted through 2024. Some of the major threats observed this year were seasonal outbreaks of diseases, continued threats of workplace violence, protests concerning working conditions, and controversy surrounding the legal status of various medical procedures and medications.

Throughout 2024 there have been increased outbreaks of seasonal diseases including dengue fever, pertussis (whooping cough), and COVID-19 strains. There has also been increased attention on Avian Flu due to the increased infection rates from fowl and cattle populations. However, the most significant outbreak of the year has been a new strain of Mpox clade 1b that has spread rampantly across African nations. The World Health Organization (WHO) declared a global public health emergency in August 2024.[^6]

Workplace violence has also been a consistent issue in 2024, with increased reports of acts of violence toward healthcare staff reported all over the globe.[^7] Notably, protests broke out in August 2024 in India after a medical student was found murdered, spurring protests against workplace violence facing healthcare staff and women.[^8]

# Part II: The Current Threat Landscape

### Supply Chain Attacks
In the early months of 2024, threat actors identified and exploited several vulnerabilities in various Ivanti tools. On January 10, 2024, Ivanti released a security update to address two zero-day vulnerabilities (CVE-2023-46805 and 2024-21887) in Ivanti Connect Secure. These vulnerabilities were also seen being used to deploy Mirai botnet attacks in May 2024.[^9]

### Cybercriminal Activity
**XZ Utils Vulnerability Impacts Linux Systems**
In February 2024, it was discovered that the latest versions of the XZ Utils software contained obfuscated malicious code in its liblzma library that created a backdoor into Linux systems. The disclosure of CVE-2024-3049 highlights the fragility of supply chain security.[^10]

**Brute Ratel**
Brute Ratel is a commercial command and control framework similar to Cobalt Strike. It is being abused by threat actors to conduct malicious command and control (C2) operations. Despite the group disbanding in March 2024, Health-ISAC has continued to observe Brute Ratel being used against healthcare organizations.[^11]

### Significant Takedowns
- **Operation Cronos**: International law enforcement took down LockBit infrastructure, seizing 34 servers and freezing 200 cryptocurrency accounts.[^12]
- **Operation Endgame**: Neutralized four malware groups (IcedID, SmokeLoader, Pikabot, and Bumblebee) that infected millions of computers.[^13]
- **Operation Morpheus**: Successfully disabled 593 Cobalt Strike servers used by cybercriminals.[^14]
- **Operation Magnus**: International action against the Meta and Redline infostealer malware distribution networks.[^15]

### Most Active Ransomware Gangs Attacks
In 2024, Health-ISAC tracked 458 ransomware events in the health sector.
1. **LockBit 3.0**: 52 attacks.
2. **INC Ransomware**: 39 attacks.
3. **RansomHub**: 36 attacks.
4. **BianLian**: 31 attacks.
5. **QiLin**: 23 attacks.

### Nation-State Activity
- **APT29 WINELOADER Campaign**: Russian nation-state threat actor conducting cyber espionage using custom backdoor malware named WINELOADER.[^16]
- **UTA0178**: Chinese nation-state actors leveraging Ivanti vulnerabilities to conduct data exfiltration.[^17]
- **North Korean Remote IT Workers**: Operatives masquerading as remote workers to gain entry into health sector organizations to steal intellectual property or money.[^18]

### Geopolitical Activity
- **Russia/Ukraine War Escalation**: Potential for increased offensive cyber campaigns against NATO critical infrastructure.[^19]
- **Threats to EU Energy Infrastructure**: NATO officials are on high alert for hybrid activity against offshore energy infrastructure.[^20]
- **Middle East Escalation**: Potential for Iranian-sponsored threat actors to attack NATO critical infrastructure.[^21]

### Medical Device Security
In 2024, CISA issued 11 advisories concerning medical devices. Health-ISAC conducted a review of all ICSMAs issued by CISA since 2016, mapping CVEs to the CISA Known Exploited Vulnerabilities (KEV) list. Additionally, the Censys report identified 5,100 publicly exposed DICOM servers, highlighting the need for better network isolation.[^22]

# Part III: Tactics, Techniques and Procedures

### Social Engineering
- **Help Desk Targeting**: Adversaries are targeting help desk teams by impersonating leadership.
- **TOAD Campaigns**: Telephone-Oriented Attack Delivery campaigns continue to be used.
- **Spam Bomb Social Engineering**: Threat actors add target email addresses to spam sites, then reach out pretending to offer tech support to gain remote access.

### Most Shared Malware Observables by Family
1. **Agent Tesla**: 515 IOCs.
2. **Remcos RAT**: 471 IOCs.
3. **AsyncRAT**: 222 IOCs.
4. **DarkGate**: 160 IOCs.
5. **XWorm**: 139 IOCs.

### Notable Vulnerabilities and Exposures
- **RDP Exposures**: 105 targeted alerts.
- **Ivanti Connect Secure**: 57 targeted alerts.
- **FortiOS**: 56 targeted alerts.
- **MOVEit Transfer**: 46 targeted alerts.
- **Check Point**: 27 targeted alerts.

# Part IV: Future Cybersecurity Outlook

### Business Resilience
- **Ransomware Attacks on Blood Suppliers**: The attacks on Synnovis, Octapharma, and OneBlood highlight the need to incorporate mission-critical suppliers into enterprise risk management plans.[^23]
- **CrowdStrike Outage**: The July 2024 outage showcased the volatility of large digital infrastructure, emphasizing the need for scenario-based risk planning.[^24]

### Emerging Cybercriminal Threats
- **AI Adoption**: Europol observed malicious large language models (LLMs) being used in cybercrime, including LLM-supported social engineering and LLM-informed reconnaissance.[^25]
- **Post-Quantum Cryptography**: NIST released the first post-quantum cryptography (PQC) standards in August 2024, marking a significant milestone in the future of data security.

# A Call to Action
[Content omitted in source]

---

[^1]: https://www.bleepingcomputer.com/news/security/integris-health-patients-get-extortion-emails-after-cyberattack/
[^2]: https://www.lehighvalleynews.com/health-news/2023-03-07/hackers-posted-photos-of-lvhn-cancer-patients-receiving-treatment-hospital-says
[^3]: https://www.webmd.com/health-insurance/news/20240325/change-healthcare-cyberattack-what-consumers-should-know
[^4]: https://www.bleepingcomputer.com/news/security/blackcat-ransomware-turns-off-servers-amid-claim-they-stole22-million-ransom/
[^5]: https://apnews.com/article/cyberattack-hospital-system-ambulances-diverted-ascension-728ab2a0e5afaf7c344e46a5ce5ca42c
[^6]: https://www.who.int/news/item/14-08-2024-who-director-general-declares-mpox-outbreak-a-public-health-emergency-of-international-concern
[^7]: https://www.facs.org/for-medical-professionals/news-publications/news-and-articles/bulletin/2024/october-2024-volume-109-issue-9/violence-escalates-against-surgeons-and-other-healthcare-workers/
[^8]: https://www.newindianexpress.com/nation/2024/Aug/17/one-of-indias-largest-medical-service-shutdowns-says-ima-chief-as-doctors-24-hour-strike-takes-effect
[^9]: https://thehackernews.com/2024/05/mirai-botnet-exploits-ivanti-connect.html
[^10]: https://arstechnica.com/security/2024/04/what-we-know-about-the-xz-utils-backdoor-that-almost-infected-the-world/
[^11]: https://blackpointcyber.com/resources/blog/brute-ratel-advanced-ip-scanner-netsupport-rat-blackpoint-soc-apg
[^12]: https://www.europol.europa.eu/media-press/newsroom/news/law-enforcement-disrupt-worlds-biggest-ransomware-operation
[^13]: https://www.europol.europa.eu/media-press/newsroom/news/largest-ever-operation-against-botnets-hits-dropper-malware-ecosystem
[^14]: https://www.europol.europa.eu/media-press/newsroom/news/europol-coordinates-global-action-against-criminal-abuse-of-cobalt-strike
[^15]: https://www.irs.gov/compliance/criminal-investigation/us-joins-international-action-against-redline-and-meta-infostealers
[^16]: https://cloud.google.com/blog/topics/threat-intelligence/apt29-wineloader-german-political-parties
[^17]: https://www.volexity.com/blog/2024/01/10/active-exploitation-of-two-zero-day-vulnerabilities-in-ivanti-connect-secure-vpn/
[^18]: https://www.securityweek.com/fake-it-workers-funneled-millions-to-north-korea-doj-says/
[^19]: https://www.bbc.com/news/articles/cwypg2z780go
[^20]: https://apnews.com/article/finland-germany-data-communications-cable-9b231aa47501545690a26a442fe106a5
[^21]: https://media.defense.gov/2024/Oct/16/2003565317/-1/-1/0/CSA-IRAN-CYBER-BRUTE-FORCE-CRITICAL-INFRASTRUCTURE-ORGS.PDF
[^22]: https://censys.com/state-of-internet-of-healthcare-things/
[^23]: https://www.aha.org/advisory/2024-08-01-american-hospital-association-and-health-isac-joint-threat-bulletin-tlp-white
[^24]: https://www.bleepingcomputer.com/news/security/crowdstrike-update-crashes-windows-systems-causes-outages-worldwide/
[^25]: https://www.europol.europa.eu/publications-events/publications/internet-organised-crime-threat-assessment-iocta-2024

---

ield of cryptography. These algorithms were almost certainly created to
proactively prepare for attacks posed by cryptographically relevant quantum computers (CRQCs). CRQCs
are any quantum computer that is used to decrypt information. These CRQCs could theoretically break the
encryption algorithms that secure national security secrets today. Corporate secrets also use some of the
same algorithms, meaning that business confidential secrets could also be stolen in encrypted form and
decrypted with a CRQC later. Post-quantum cryptographic standards should be considered as the threat of a
CRQC becomes realized.46

44  https://www.europol.europa.eu/publications-events/main-reports/iocta-report
45  https://openai.com/index/disrupting-malicious-uses-of-ai-by-state-affiliated-threat-actors/
46  https://csrc.nist.gov/projects/post-quantum-cryptography/post-quantum-cryptography-standardization

23

health-isac.org

2025 Health Sector Cyber Threat Landscape

A Call to Action

Protect your patients, elevate your defenses, and empower your team

In today’s interconnected health ecosystem, no organization is alone in facing cyber threats. Information
sharing and collaboration through Health-ISAC is the key to building a unified front against cybercrime,
protecting sensitive patient data, and ensuring the well-being of those we serve.

By joining and actively participating in your Health-ISAC community, you gain:

•

•

•

 Foresight: Early warnings about emerging threats and proven mitigation strategies from your peers.

 Expertise: Crowdsourced knowledge from industry veterans to strengthen your defenses and elevate
your team’s skills.

 Resilience: Collaborative trust to navigate evolving threats with confidence and maintain a secure,
reliable network.

•

 Innovation: Shared insights that fuel cutting-edge cybersecurity solutions for a safer future of healthcare.

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

Together, we can build a stronger, more resilient healthcare ecosystem where patient
safety is always the top priority. Don’t wait for the next attack. Be part of the solution.
Share, collaborate, and secure the future of healthcare.

If you have any comments

or questions about this

report, please reachc out

to Health-ISAC at

contact@h-isac.org

24

health-isac.org

Health-ISAC, Inc.
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