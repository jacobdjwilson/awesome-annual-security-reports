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

The healthcare landscape is undergoing rapid digital transformation, bringing unprecedented advancements in patient care. Yet, this evolution has also ushered in a new era of cybersecurity challenges. Building upon our previous Healthcare Threat Briefing, which dissected the attack flows specific to this vital sector, our 2025 report delves deeper into the emergent threats confronting healthcare organizations.

The Trustwave SpiderLabs team has conducted in-depth analysis of emerging cyber adversary tactics, identifying the key trends reshaping the industry’s risk profile. We’ve structured these findings into a comprehensive breakdown of attack stages, providing healthcare organizations with actionable intelligence to strengthen their defensive posture. In addition, Trustwave SpiderLabs has produced two detailed analyses focusing on pressing areas of concern: the rapid rise of ransomware and an examination of common security gaps discovered through a healthcare red team.

The complexities of modern healthcare, with its intricate network of interconnected medical devices, electronic health records (EHRs), and legacy systems, create a fertile ground for cyberattacks. The expanding adoption of telehealth, Internet of Medical Things (IoMT), and cloud-based solutions has broadened the attack surface, introducing new vulnerabilities that threat actors are adept at exploiting. Beyond the staggering financial implications, with average data breach costs exceeding $9.7 million – which is double the cross-industry average of $4.8 million – the true cost lies in the potential for compromised patient safety.

A cyberattack in healthcare can directly impact human lives. A compromised infusion pump, ventilator, or patient monitoring system can lead to incorrect dosages, system malfunctions, and potentially fatal outcomes. Moreover, the stringent compliance requirements of HIPAA and other regulations underscore the imperative of robust cybersecurity.

Our findings emphasize that cybersecurity in healthcare is not just about protecting data—it’s about safeguarding lives. It’s a fundamental obligation to ensure that the technologies designed to heal do not become instruments of harm. We aim to equip healthcare professionals with the knowledge and strategies necessary to navigate this complex terrain, ensuring that patient safety, data integrity, and regulatory compliance remain paramount in the face of evolving cyber threats.

### Key Report Findings for the Healthcare Sector
- **45%** of attacks originated from exploiting public-facing applications
- **9%** of ransomware attacks were conducted by Ransomhub
- **51%** of ransomware attacks targeted the US
- **56%** of public-facing applications exploited were against Log4j
- **21%** of ransomware attacks targeted public health and government healthcare

---

## Healthcare’s Unique Threat Landscape

### Patient Safety and Data Integrity
- At the heart of healthcare cybersecurity lies the absolute necessity to safeguard patient safety and data integrity. A breach at a healthcare facility can have immediate, life-threatening consequences. Medical devices, from infusion pumps to ventilators, are now interconnected, creating potential for vulnerabilities that, if exploited, could directly harm patients. Adding to the urgency, healthcare data is exceptionally valuable to threat actors, often fetching high prices on the dark web due to its comprehensive nature.
- The sensitivity of Protected Health Information (PHI) adds another layer of complexity. Breaches not only violate patient trust but also incur severe regulatory penalties under frameworks like HIPAA in the United States, GDPR in Europe, and similar legislation worldwide. The global healthcare community, while diverse in its delivery models, shares this fundamental commitment to patient safety and data protection, making robust cybersecurity a universal imperative.

### Complex Compliance and Regulation
- Healthcare operates within a highly regulated environment, with stringent compliance requirements that vary by jurisdiction. In addition to data privacy laws, healthcare organizations must adhere to industry-specific standards and regulations related to medical device security, data interoperability, and patient consent. For example, the GDPR in Europe requires organizations to report data breaches within 72 hours, with potential fines of up to 4% of annual global turnover. This regulatory landscape is constantly evolving, requiring organizations to maintain agility and vigilance.
- Additionally, the global nature of healthcare, with cross-border collaborations and remote patient monitoring, necessitates a harmonized approach to cybersecurity, balancing national regulations with international best practices. The sheer volume and sensitivity of healthcare regulations places a significant burden on organizations to ensure compliance while maintaining operational efficiency.

### Legacy Systems and Cutting-Edge Technology
- Healthcare grapples with the challenge of integrating legacy systems with modern technologies. Hospitals often rely on outdated EHR systems and medical devices that lack robust security features. However, the rapid adoption of telehealth, IoMT, and cloud-based solutions has expanded the attack surface, creating new vulnerabilities. A typical US hospital has between 10 and 15 medical devices per bed, which means a 1,000-bed hospital could have around 15,000 medical devices.
- The convergence of these disparate systems necessitates a holistic cybersecurity approach that addresses both legacy vulnerabilities and emerging threats. This challenge is compounded by the fact that many healthcare organizations lack the resources and expertise to modernize their infrastructure while maintaining operational continuity.

### The Human Element
- Healthcare is inherently a people-centric industry, making it particularly susceptible to social engineering attacks. Phishing, ransomware, and other forms of cybercrime often target healthcare employees, exploiting their empathy and urgency to gain access to sensitive data or systems.
- The human element is a critical vulnerability that requires ongoing training and awareness programs. Healthcare must prioritize the security awareness of its workforce to mitigate the risk of social engineering attacks.

### Global Interconnectedness and Supply Chain Risks
- The global supply chain for medical devices and pharmaceuticals introduces another layer of complexity. Vulnerabilities in third-party systems or devices can have cascading effects, impacting healthcare organizations worldwide. This interconnectedness necessitates a collaborative approach to cybersecurity, with information sharing and coordinated responses across national borders.
- The global nature of medical research and development also creates a target-rich environment for intellectual property theft and espionage.

![Change Healthcare Breach Impact Doubles to 190M People - January 2025, Dark Reading]
![Ransomware Attack Forces 100 Romanian Hospitals to Go Offline - February 2024, Bleeping Computer]

With more than 250 cybersecurity experts across the globe, the Trustwave SpiderLabs team puts its resources to task researching the top threats in today’s landscape. We are uniquely positioned to do so, as we perform over 200,000 hours of penetration tests and uncover tens of thousands of vulnerabilities annually. We also have a dedicated email security team analyzing millions of phishing URLs validated daily, including 10k per day that are uniquely identified by Trustwave SpiderLabs. Our diverse coverage of infosec disciplines, including Advanced Continuous Threat Hunting, Digital Forensics and Incident Response, Malware Reversal, and Database Security, give us insight into identifying how these breaches occur, as well as mitigations and controls that your organization can put in place to prevent these compromises.

---

## Notable and Prominent Trends in Healthcare

## Ransomware Groups Continue to Target Healthcare

### The Threat
Ransomware has emerged as one of the most disruptive and dangerous cyber threats targeting healthcare facilities, with attacks against hospitals, research institutions, medical suppliers, and healthcare educational facilities increasing at an alarming rate.

Cybercriminals infiltrate healthcare networks, encrypt critical systems, and demand ransom payments, often leaving organizations unable to access patient records, process medical procedures, or operate essential equipment. Given the life-critical nature of healthcare services, these attacks not only pose financial risks but can also result in patient endangerment, delayed treatments, and loss of critical medical data.

Unlike other industries, hospitals and healthcare providers cannot afford prolonged downtime, making them more likely to pay ransom demands to restore operations quickly. This reality has made healthcare a prime target for ransomware gangs, who see it as a high-pressure, high-payoff sector.

The healthcare industry has become a lucrative target for cybercriminals, with network access to hospitals, clinics, and medical institutions being actively sold on the Dark Web.

![11 Big Pharma Firms Affected in Cencora Cyber Attack - May 2024, Cyber Daily]

Cybercriminal marketplaces and forums offer access to compromised remote desktop (RDP) credentials, VPN logins, and administrator accounts, providing attackers with a direct gateway into hospital networks. These illicit sales fuel a growing underground economy, where ransomware groups, data brokers, and all types of actors compete to exploit healthcare vulnerabilities for financial gain, intelligence gathering, or even disrupting critical medical operations.

![Figure 1: Threat actor on the Dark Web seeking various types of access to healthcare facilities]

### What Trustwave Is Seeing
Trustwave SpiderLabs analyzed ransomware incidents targeting the healthcare sector and identified Ransomhub and LockBit 3.0 as the predominant groups operating in this space. The data reveals that Ransomhub had the greatest number of reported incidents with 62 victims, followed closely by LockBit 3.0 and Dispossessor, each claiming 55 attacks.

![Figure 2: Top ransomware groups targeting healthcare]

From a global perspective, ransomware groups exhibit a clear focus on certain regions, with the United States bearing the brunt of attacks. 51% of the incidents in the dataset target US-based companies.

![Figure 3: Healthcare organizations affected by ransomware by country]
![Figure 4: Ransomware attacks by healthcare type]

![23andMe Settles Data Breach Lawsuit for $30 Million - September 2024, Reuters]

### Mitigations to Reduce Risk
- **Enhance Cybersecurity Hygiene and Patch Management**: Many ransomware attacks exploit known vulnerabilities, especially in legacy systems.
- **Implement Robust Backup and Recovery Plans**: Maintaining regular, encrypted backups of critical systems and data is essential.
- **Employee Training and Awareness**: Educating employees on recognizing phishing attempts and practicing good password hygiene.
- **Multi-Factor Authentication (MFA) and Strong Credential Management**: Implementing MFA across all systems, especially for remote access.
- **Incident Response Planning**: A comprehensive incident response plan is essential to minimizing the impact of a ransomware attack.
- **Collaboration with Law Enforcement**: In the event of an attack, healthcare organizations should report the incident to relevant law enforcement agencies.

---

## Unmasking Security Gaps in Healthcare

### The Threat
A United States-based health system hired Trustwave SpiderLabs to perform a Red Team on its environments, focusing specifically on achieving privilege escalation or abusing user privileges to attempt further exploitation of the environment.

### What Trustwave Is Seeing
Trustwave SpiderLabs identified several issues related to the company’s Virtual Desktop Infrastructure (VDI) instance, which allowed arbitrary code execution and the means to establish a foothold within the company’s network.

### Summary of Key Findings
- **Credential Mismanagement**: Weak password policies, credential reuse, and exposed accounts.
- **Vulnerability in Sensitive Systems**: Critical systems, including medical devices, shared drives, and web applications, were found to be improperly secured.
- **Privilege Escalation**: The ability to escalate privileges, both within the network and to Domain Admin levels.
- **Misconfiguration in Network Segmentation**: Vulnerabilities in the segmentation of sensitive areas, such as patient rooms and camera systems.

### Mitigations to Reduce Risk
- **Regular Vulnerability Scanning and Patch Management**
- **Review and Mitigate Misconfigured Shared Drives**
- **User Permissions Audits**
- **Credential Hardening**
- **Network Segmentation**
- **EDR and Security Monitoring**

---

## Medical Supply Chain Complexities

### The Threat
The medical supply chain is a critical component of healthcare operations. A successful attack on a single supplier can create a ripple effect across multiple healthcare facilities.

### What Trustwave Is Seeing
Healthcare institutions rely on specialized software solutions for patient management, medical imaging, billing systems, and electronic health records. Cybercriminals have identified these software providers as high-value targets.

![Figure 5: Threat actor claims to hack into the healthcare supply chain attack by targeting healthcare software provider]
![Figure 6: The same actor advertises data claimed to be obtained from the healthcare facility using a supply chain attack against a healthcare software supplier]

![Figure 7: Threat actor sells access to a medical equipment supplier in US]
![Figure 8: Threat actor shares databases and credentials from a compromised global healthcare materials and science solutions supplier]

![Ransomware Attack Forces UMC Health System to Divert Some Patients - October 2024, Bleeping Computer]
![Figure 9: The post shares a database of healthcare products and nutritional supplements developer]

### Mitigations to Reduce Risk
- **Vendor Security Agreements**
- **Secure API Integrations**
- **Monitor Vendor Access**
- **Continuous Monitoring of Third-Party Systems**
- **Patch and Update Software Regularly**
- **Use Secure Software Development Practices**
- **Adopt Zero-Trust Architecture**

---

## Complex Web of Compliance

### International Healthcare Cybersecurity Standards
- **ISO 27001**: Provides a framework for establishing, implementing, maintaining, and continually improving an information security management system (ISMS).
- **IEC 62443**: Addresses security for operational technology in automation and control systems.
- **EU’s NIS2 Directive**: Aims to enhance cybersecurity across critical infrastructure sectors, including healthcare.

![Cyberattack at French Hospital Exposes Health Data of 750,000 Patients - November 2024, Bleeping Computer]

### HIPAA 2.0: Strengthening Cybersecurity in US Healthcare
In January 2025, the US Department of Health and Human Services (HHS) proposed significant updates to the HIPAA Security Rule, often referred to as “HIPAA 2.0.”

**Key Changes in HIPAA 2.0:**
- Removing the distinction between “required” and “addressable” implementation specifications.
- Enhancing risk analysis requirements.
- Strengthening incident response and contingency planning.
- Mandating new security controls (encryption, MFA, network segmentation).
- Increasing accountability for business associates.

---

## Threat Actor Techniques by Attack Stage

### Initial Access Techniques
Initial access vectors used in healthcare attacks were split between phishing (45%) and exploit attempts against web applications (45%).

![Figure 10: Initial access techniques used by attackers of healthcare entities]
![Figure 11: Public-facing applications exploited in the healthcare sector]

### Execution Techniques
Execution techniques observed mostly involved user execution of malicious files and links (50%), followed by malicious uses of PowerShell scripts and commands (47%).

![Figure 12: Execution techniques used by attackers of healthcare entities]

### Persistence Techniques
The persistence techniques observed relied mostly on account manipulation (89%).

![Figure 13: Persistence techniques used by attackers of healthcare entities]

### Defense Evasion Techniques
Defense evasion techniques observed mostly utilized masquerading (48%).

![Figure 14: Defense evasion techniques used by attackers of healthcare entities]

### Credential Access Techniques
Credential access techniques observed relied mostly on brute-force attempts (92%).

![Figure 15: Credential access techniques used by attackers of healthcare entities]

### Lateral Movement Techniques
To move laterally within healthcare organizations, attackers relied almost exclusively on Remote Services (99%), specifically Remote Desktop Protocol (RDP).

![Figure 16: Lateral movement techniques used by attackers of healthcare entities]

---

## Conclusion & Key Takeaways

### Conclusion
The healthcare sector is facing an evolving and alarming landscape of cyber threats, underscoring the importance of robust cybersecurity practices to safeguard not just data, but human lives. By taking proactive and strategic action, healthcare organizations can significantly reduce their risk exposure and build a more resilient, secure environment for both healthcare professionals and patients.

### Key Takeaways:
1. **Emerging Cyber Threats**: The healthcare sector faces growing cyber threats, including ransomware attacks, data breaches, and supply chain compromises.
2. **Impact on Patient Care**: Cyberattacks in healthcare can directly harm patients by delaying treatments, compromising medical devices, and disrupting critical healthcare operations.
3. **Need for Stronger Cybersecurity Measures**: Many healthcare organizations are vulnerable due to outdated cybersecurity practices, weak authentication, and insufficient staff training.
4. **Vendor and Supply Chain Risks**: Cybercriminals increasingly target third-party vendors and suppliers.
5. **Comprehensive Security Approach**: A robust cybersecurity strategy should include endpoint protection, IoMT device security, staff training, dark web monitoring, and a well-defined incident response and recovery plan.
6. **Patient Safety as a Priority**: Cybersecurity is not just an IT concern but a patient safety imperative.