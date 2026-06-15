# 2025 Trustwave Risk Radar Report: Healthcare Sector

## Table of Contents
- [Healthcare’s Unique Threat Landscape](#healthcares-unique-threat-landscape)
- [Notable and Prominent Trends in Healthcare](#notable-and-prominent-trends-in-healthcare)
- [Ransomware Groups Continue to Target Healthcare](#ransomware-groups-continue-to-target-healthcare)
- [Unmasking Security Gaps in Healthcare](#unmasking-security-gaps-in-healthcare)
- [Medical Supply Chain Complexities](#medical-supply-chain-complexities)
- [Complex Web of Compliance](#complex-web-of-compliance)
- [Threat Actor Techniques by Attack Stage](#threat-actor-techniques-by-attack-stage)
- [Conclusion & Key Takeaways](#conclusion--key-takeaways)

---

The healthcare landscape is undergoing rapid digital transformation, bringing unprecedented advancements in patient care. Yet, this evolution has also ushered in a new era of cybersecurity challenges. Building upon our previous Healthcare Threat Intelligence Briefing, which dissected the attack flows specific to this vital sector, our 2025 report delves deeper into the emergent threats confronting healthcare organizations.

The Trustwave SpiderLabs team has conducted in-depth analysis of emerging cyber adversary tactics, identifying the key trends reshaping the industry’s risk profile. We’ve structured these findings into a comprehensive breakdown of attack stages, providing healthcare organizations with actionable intelligence to strengthen their defensive posture.

### Key Report Findings for the Healthcare Sector
- **45%** of attacks originated from exploiting public-facing applications.
- **56%** of public-facing applications exploited were against Log4j.
- **9%** of ransomware attacks were conducted by Ransomhub.
- **21%** of ransomware attacks targeted public health and government healthcare.
- **51%** of ransomware attacks targeted the US.

The complexities of modern healthcare, with its intricate network of interconnected medical devices, electronic health records (EHRs), and legacy systems, create a fertile ground for cyberattacks. The expanding adoption of telehealth, Internet of Medical Things (IoMT), and cloud-based solutions has broadened the attack surface. Beyond the staggering financial implications, with average data breach costs exceeding $9.7 million—which is double the cross-industry average of $4.8 million—the true cost lies in the potential for compromised patient safety.

## Healthcare’s Unique Threat Landscape

### Patient Safety and Data Integrity
At the heart of healthcare cybersecurity lies the absolute necessity to safeguard patient safety and data integrity. A breach at a healthcare facility can have immediate, life-threatening consequences. Medical devices, from infusion pumps to ventilators, are now interconnected, creating potential for vulnerabilities that, if exploited, could directly harm patients.

### Complex Compliance and Regulation
Healthcare operates within a highly regulated environment, with stringent compliance requirements that vary by jurisdiction. In addition to data privacy laws, healthcare organizations must adhere to industry-specific standards and regulations related to medical device security, data interoperability, and patient consent.

### Legacy Systems and Cutting-Edge Technology
Healthcare grapples with the challenge of integrating legacy systems with modern technologies. Hospitals often rely on outdated EHR systems and medical devices that lack robust security features. A typical US hospital has between 10 and 15 medical devices per bed, which means a 1,000-bed hospital could have around 15,000 medical devices.

### The Human Element
Healthcare is inherently a people-centric industry, making it particularly susceptible to social engineering attacks. Phishing, ransomware, and other forms of cybercrime often target healthcare employees, exploiting their empathy and urgency to gain access to sensitive data or systems.

## Notable and Prominent Trends in Healthcare

## Ransomware Groups Continue to Target Healthcare

Ransomware has emerged as one of the most disruptive and dangerous cyber threats targeting healthcare facilities. Unlike other industries, hospitals and healthcare providers cannot afford prolonged downtime, making them more likely to pay ransom demands to restore operations quickly.

![Threat actor on the Dark Web seeking various types of access to healthcare facilities]

### Top Ransomware Groups Targeting Healthcare
Trustwave SpiderLabs identified Ransomhub and LockBit 3.0 as the predominant groups operating in this space. 
- **Ransomhub**: 9%
- **LockBit 3.0**: 8%
- **Black Basta**: 8%
- **Rhysida**: 6%

From a global perspective, ransomware groups exhibit a clear focus on certain regions, with the United States bearing the brunt of attacks (51% of incidents).

## Unmasking Security Gaps in Healthcare

A United States-based health system hired Trustwave SpiderLabs to perform a Red Team assessment. The assessment identified several issues related to the company’s Virtual Desktop Infrastructure (VDI) instance, which allowed arbitrary code execution and the means to establish a foothold within the company’s network.

### Summary of Key Findings
- **Credential Mismanagement**: Weak password policies and credential reuse.
- **Vulnerability in Sensitive Systems**: Critical systems, including medical devices and shared drives, were improperly secured.
- **Privilege Escalation**: Demonstrated ability to reach Domain Admin levels.
- **Misconfiguration in Network Segmentation**: Vulnerabilities in the segmentation of sensitive areas, such as patient rooms and camera systems.

## Medical Supply Chain Complexities

Healthcare institutions rely on specialized software solutions for patient management, medical imaging, billing systems, and electronic health records. Cybercriminals have identified these software providers as high-value targets, knowing that compromising a single vendor could grant them access to multiple hospitals and healthcare facilities at once.

![Threat actor claims to hack into the healthcare supply chain]

## Complex Web of Compliance

### International Healthcare Cybersecurity Standards
- **ISO 27001**: Provides a framework for establishing, implementing, maintaining, and continually improving an information security management system (ISMS).
- **IEC 62443**: Addresses security for operational technology in automation and control systems.
- **EU’s NIS2 Directive**: Aims to enhance cybersecurity across critical infrastructure sectors, including healthcare.

### HIPAA 2.0
In January 2025, the US Department of Health and Human Services (HHS) proposed significant updates to the HIPAA Security Rule, often referred to as “HIPAA 2.0,” to address the evolving cybersecurity landscape and enhance protections for electronic protected health information (ePHI).

## Threat Actor Techniques by Attack Stage

### Initial Access Techniques
- **Phishing (T1566)**: 45%
- **Valid Account (T1078)**: 45%
- **Exploit Public-Facing Application (T1190)**: 10%

![Public-facing applications exploited in the healthcare sector]

## Conclusion & Key Takeaways

Cybersecurity in healthcare is not just about protecting data—it’s about safeguarding lives. It’s a fundamental obligation to ensure that the technologies designed to heal do not become instruments of harm. Healthcare organizations must prioritize:
1. **Enhanced Cybersecurity Hygiene**: Regular patching and vulnerability management.
2. **Robust Backup and Recovery**: Stored offline or in isolated environments.
3. **Multi-Factor Authentication (MFA)**: Across all systems, especially remote access.
4. **Incident Response Planning**: Regular testing through tabletop exercises.
5. **Vendor Security Agreements**: Clear cybersecurity responsibilities for third-party suppliers.

---

50% Command Injection (CVE-2023-1389) – accounting for 11%
Figure 10: Initial access techniques used by attackers of healthcare
and 10% of the cases respectively.
entities
Execution Techniques
Initial access vectors used in healthcare attacks were split
between phishing (45%) and exploit attempts against web
|                     |               |                      |                     |                  | User Execution T1204   |                 |         | 50%     |     |
| ------------------- | ------------- | -------------------- | ------------------- | ---------------- | ---------------------- | --------------- | ------- | ------- | --- |
| applications        | (45%).  Most  | of  the              | phishing  attempts  | were             | Comm a n d  a n d  S   | c r ip ti ng    |         |         |     |
|                     |               |                      |                     |                  | I n t er p re t        | e r  T 10 5 9   |         | 47%     |     |
| generic  and        | leveraged     | social  engineering  |                     | with  links  to  | W in d o w s  M a n    | a g em e n t 3% |         |         |     |
|                     |               |                      |                     |                  | Ins tr u m e n ta t io | n  T 10 4 7     |         |         |     |
| external websites.  |               |                      |                     |                  |                        | 0% 10%          | 20% 30% | 40% 50% | 60% |
Figure 12: Execution techniques used by attackers of healthcare entities
Execution techniques observed in the healthcare security
incidents mostly involved user execution of malicious files
and links (50%), followed by malicious uses of PowerShell
scripts and commands (47%). Some commands were found
to be a result of Mimikatz hacktool execution.
31

| Persistence Techniques          |     |     |     |     |     |     | Defense Evasion Techniques |          |     |     |     |     |
| ------------------------------- | --- | --- | --- | --- | --- | --- | -------------------------- | -------- | --- | --- | --- | --- |
| Account Manipulation T1098      |     |     |     |     |     | 89% | Masquerading T1036         |          |     |     |     | 48% |
|                                 |     |     |     |     |     |     | System Binary Proxy Exec   | u t io n |     |     |     |     |
| Event Triggered Execution T1546 |     | 4%  |     |     |     |     |                            |          |     | 17% |     |     |
T 1 2 18
|                                | Create Account T1136 | 4%                  |     |     |     |      | Access Token Manipulation T1134 |          |     | 14%     |     |     |
| ------------------------------ | -------------------- | ------------------- | --- | --- | --- | ---- | ------------------------------- | -------- | --- | ------- | --- | --- |
|                                | Boot or  L o g o n   |   A u t o s ta r t  |     |     |     |      | Obfuscated Files or Inform      | a ti o n |     |         |     |     |
|                                | E x e c u t          | i o n  T 1 5 4 7 2% |     |     |     |      |                                 | T 10 2 7 |     | 13%     |     |     |
| External Remote Services T1133 |                      | 1%                  |     |     |     |      | Process Injection T1055         |          | 6%  |         |     |     |
|                                |                      | 0% 20%              | 40% | 60% | 80% | 100% | Impair Defenses T1562           |          | 2%  |         |     |     |
|                                |                      |                     |     |     |     |      |                                 | 0%       | 10% | 20% 30% | 40% | 50% |
Figure 13: Persistence techniques used by attackers of healthcare
entities Figure 14: Defense evasion techniques used by attackers of healthcare
entities
| The  | persistence  | techniques  | observed  | relied  | mostly  | on  |     |     |     |     |     |     |
| ---- | ------------ | ----------- | --------- | ------- | ------- | --- | --- | --- | --- | --- | --- | --- |
Defense evasion techniques observed in healthcare security
account manipulation (89%), but also other techniques such
incidents mostly utilized masquerading (48%), using process
as account creation, (4%) and event-triggered execution (4%).
names such as explorer.exe, srvany.exe, taskmgr.exe and
Account manipulation involves modifying existing accounts  chrome.exe,  and  system  binary  proxy  execution  using
to either maintain access or escalate privileges. For example,  rundll32  and  curl.exe  to  download  and  execute  external
| an attacker might change account permissions or add their  |     |     |     |     |     |     | payloads. |     |     |     |     |     |
| ---------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --------- | --- | --- | --- | --- | --- |
credentials to an existing user account to retain access.
Account creation refers to the creation of new user accounts
| by  attackers.  |     | Threat  groups  | use  these  | new  | accounts  | to  |     |     |     |     |     |     |
| --------------- | --- | --------------- | ----------- | ---- | --------- | --- | --- | --- | --- | --- | --- | --- |
maintain access or to disguise their activities as legitimate
users.
2025 Trustwave Risk Radar Report: Healthcare Sector

| Credential Access Techniques |            |     |     | Lateral Movement Techniques |             |         |          |
| ---------------------------- | ---------- | --- | --- | --------------------------- | ----------- | ------- | -------- |
| Brute Force T1110            |            |     | 92% | Remote Services T1021       |             |         | 99%      |
|                              |            |     |     | Use Alternate  Au t h e n t | i ca ti o n |         |          |
| OS Credential Dumping T1003  | 5%         |     |     | M a t e ri a l              | T 15 5 0 1% |         |          |
| Forced Authentication T1178  | 2%         |     |     |                             |             |         |          |
|                              |            |     |     |                             | 0% 20%      | 40% 60% | 80% 100% |
| Steal or Forge Kerberos T    | ic k e t s |     |     |                             |             |         |          |
T 1 5 5 8 1%
|     | 0% 20% | 40% 60% | 80% 100% |     |     |     |     |
| --- | ------ | ------- | -------- | --- | --- | --- | --- |
Figure 15: Credential access techniques used by attackers of healthcare  Figure 16: Lateral movement techniques used by attackers of healthcare
| entities |     |     |     | entities |     |     |     |
| -------- | --- | --- | --- | -------- | --- | --- | --- |
Credential access techniques observed in the attacks relied  To move laterally within healthcare organizations, attackers
mostly  on  brute-force  attempts  and  generic  brute-force  relied  almost  exclusively  on  Remote  Services  (99%),
attacks  (92%).  We  also  observed  OS  credential  dumping  specifically Remote Desktop Protocol (RDP).
| attempts  (5%)  | using  ComSvcs  | and  Mimikatz  | and  forced  |     |     |     |     |
| --------------- | --------------- | -------------- | ------------ | --- | --- | --- | --- |
authentication attempts (2%).
33

Conclusion &
Key Takeaways
2025 Trustwave Risk Radar Report: Healthcare Sector

Conclusion
The healthcare sector is facing an evolving and alarming landscape of cyber threats, underscoring the importance of robust
cybersecurity practices to safeguard not just data, but human lives. With the rapid expansion of digital tools such as telehealth,
IoMT devices, and cloud-based systems, healthcare organizations are increasingly vulnerable to a variety of cyberattacks,
including ransomware, data breaches, and supply chain compromises. These threats have the potential to cause disruptions
that can delay critical treatments, compromise patient records, and even jeopardize patient safety.
Despite these risks, many healthcare organizations are still grappling with outdated security practices, inadequate
authentication measures, and insufficient staff training. To address these challenges, the healthcare sector must prioritize
proactive cybersecurity strategies that integrate strengthened access controls, device security, vendor management, and
employee training. A robust cybersecurity posture will not only help mitigate financial losses but also ensure the resilience of
healthcare systems and the protection of patient safety in this digital age.
Ultimately, cybersecurity in healthcare is no longer just a technical issue—it is a critical component of patient care. By investing
in comprehensive security measures and fostering a culture of vigilance, healthcare organizations can better safeguard their
networks, protect sensitive data, and ensure that technological advancements enhance rather than endanger the well-being
of patients.
35

Key Takeaways:
1.  Emerging Cyber Threats:  The healthcare sector faces  4. Vendor  and  Supply  Chain  Risks:  C  ybercriminals
growing cyber threats, including ransomware attacks, data  increasingly  target  third-party  vendors  and  suppliers.
breaches, and supply chain compromises. These attacks  Healthcare organizations must strengthen their security
can disrupt medical services and put patient safety at risk. frameworks to protect data shared with external partners.
2. Impact  on  Patient  Care:   Cyberattacks  in  healthcare  5. Comprehensive  Security  Approach:   A  robust
can  directly  harm  patients  by  delaying  treatments,  cybersecurity strategy should include endpoint protection,
compromising  medical  devices,  and  disrupting  critical  IoMT device security, staff training, dark web monitoring,
healthcare operations, which can lead to life-threatening  and a well-defined incident response and recovery plan.
consequences.
6. Patient Safety as a Priority:  Cybersecurity is not just an
3. Need  for  Stronger  Cybersecurity  Measures:  M  any  IT concern but a patient safety imperative. Healthcare
healthcare  organizations  are  vulnerable  due  to  organizations must treat securing their networks and data
outdated cybersecurity practices, weak authentication,  as a top priority to safeguard patient lives and preserve
| and  insufficient        | staff        | training.   | Implementing  | multi-        | trust in the healthcare system. |            |                 |          |             |
| ------------------------ | ------------ | ----------- | ------------- | ------------- | ------------------------------- | ---------- | --------------- | -------- | ----------- |
| factor  authentication,  |              | zero-trust  | models,       | and  regular  |                                 |            |                 |          |             |
|                          |              |             |               |               | By  taking                      | proactive  | and  strategic  | action,  | healthcare  |
| cybersecurity            | audits  are  | essential   | steps         | to  enhance   |                                 |            |                 |          |             |
organizations can significantly reduce their risk exposure
security.
|     |     |     |     |     | and  build  | a  more  | resilient,  secure  | environment  | for  both  |
| --- | --- | --- | --- | --- | ----------- | -------- | ------------------- | ------------ | ---------- |
healthcare professionals and patients.
2025 Trustwave Risk Radar Report: Healthcare Sector