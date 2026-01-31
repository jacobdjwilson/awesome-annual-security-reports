# 2024 Education Threat Landscape

The official report URL is: https://levelblue.com/resources/research-reports/2023-hospitality-sector-threat-landscape-trustwave-threat-intelligence-briefing-and-mitigation-strategies

## Table of Contents
- [Executive Summary](#executive-summary)
- [Emerging and Prominent Trends](#emerging-and-prominent-trends)
  - [Shift Towards Online Education](#shift-towards-online-education)
  - [Third-Party Security Risks](#third-party-security-risks)
  - [Ransomware Attacks](#ransomware-attacks)
- [Dissecting the Attack Flow for the Education Sector](#dissecting-the-attack-flow-for-the-education-sector)
  - [Attack Flow Overview](#attack-flow-overview)
  - [Attack Flow Steps](#attack-flow-steps)
    - [Initial Foothold](#initial-foothold)
      - [Phishing, Spam & Scams](#phishing-spam--scams)
      - [Logging in](#logging-in)
      - [Vulnerability Exploitation](#vulnerability-exploitation)
      - [Supply Chain](#supply-chain)
    - [Initial Payload](#initial-payload)
    - [Expansion / Pivoting](#expansion--pivoting)
    - [Malware](#malware)
      - [Loaders, Infostealers and RATs](#loaders-infostealers-and-rats)
      - [Ransomware](#ransomware)
    - [Exfiltration / Post Compromise/ Impact](#exfiltration--post-compromise-impact)
- [Key Takeaways and Recommendations](#key-takeaways-and-recommendations)
- [Appendix/Reference](#appendixreference)
  - [Threat Groups](#threat-groups)

# 2024 Education Threat Landscape

T R U S T W A V E   T H R E A T   I N T E L L I G E N C E
B R I E F I N G   A N D   M I T I G A T I O N   S T R A T E G I E S

## Table of Contents
Contents

Executive Summary ‧ ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧ 1

Emerging and Prominent Trends‧ ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧ ‧ 4

Shift Towards Online Education ‧ ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧ ‧ 5

Third-Party Security Risks‧ ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧ ‧ 6

Ransomware Attacks‧ ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧ ‧ 8

Dissecting the Attack Flow for the Education Sector‧ ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧ ‧ 10

Attack Flow Overview‧ ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧ 11

Attack Flow Steps‧ ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧ 11

Initial Foothold: Phishing, Spam & Scams‧ ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧ ‧ 13

Initial Foothold: Logging in‧ ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧ 20

Initial Foothold: Vulnerability Exploitation‧ ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧ 25

Initial Foothold: Supply Chain ‧ ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧ 33

Initial Payload‧ ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧ 35

Expansion / Pivoting‧ ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧ 38

Malware: Loaders, Infostealers and RATs‧ ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧ ‧ 41

Malware: Ransomware ‧ ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧ 44

Exfiltration / Post Compromise/ Impact ‧ ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧ 47

Key Takeaways and Recommendations‧ ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧ ‧ 51

Appendix/Reference ‧ ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧ 56

Threat Groups‧ ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧ ‧ 57

Akira:‧ ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧ 57

ALPHV aka BlackCat:‧ ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧ 57

Bl00dy Ransomware:‧ ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧ 57

Clop or Cl0p: ‧ ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧ 58

LockBit 3.0: ‧ ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧ 58

Medusa: ‧ ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧ 58

No Escape:‧ ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧ 59

Pirat-Networks:‧ ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧ 59

Rhysida: ‧ ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧ 59

Royal:‧ ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧ 59

Vice Society: ‧ ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧  ‧ 60

FEBRUARY 2024

2024 Education Threat Landscape: Trustwave Threat Intelligence Briefing and Mitigation Strategies

# Executive Summary

“So many of our schools across the nation are, what we call, ‘target rich, cyber poor’ in that they are often a frequent target for ransomware and other cyberattacks due to the extensive data kept on school networks, often without the proper protection,” stated the Cybersecurity and Infrastructure Security Agency (CISA), aptly summarizing the concerning state of cybersecurity in education.

Primary school systems handle sensitive data concerning minors, while higher education institutions must safeguard intellectual property data, making them prime targets for cyberattacks. These attacks not only threaten the safety and security of teachers and administrators, but they put the privacy of students, staff, and other associated entities at risk.

With millions of students now learning through technology in hybrid, remote, or in-class settings, device security is no longer optional. It's crucial to ensure a safe and secure learning environment for everyone. Strong cybersecurity measures not only protect student data but also enable teachers to do their jobs effectively without fear of disruptions or data breaches.

These disruptions directly contradict the sector's core mission of fostering knowledge and development. As a result, educators and administrators are facing heightened concerns about cyber resilience – and recent breaches illustrate the risks.

In May 2022, Illinois’ Lincoln College was forced to permanently shut down due to the impact of a ransomware attack. In March 2021, the Buffalo Public Schools District was hit by a ransomware attack and as a result, spent nearly $10 million on network security, fraud monitoring and other services. In June 2023, The University of Manchester, which has over 10,000 staff and 45,000 students, confirmed it had been successfully attacked, and data belonging to alumni and current students was accessed and removed.

There are a number of factors that make the education industry especially vulnerable to cyberattacks, including:

*   **BYOD Dilemma**: The "Bring Your Own Device" culture poses security challenges by adding unmanaged devices to the network, straining IT resources.
*   **Complex Infrastructure**: Diverse devices, decentralized IT management, and inconsistent security practices create a sprawling attack surface with vulnerabilities.
*   **Data Trove**: Huge volumes of sensitive student data (PII, research, IP) attract attackers seeking data breaches and identity theft, amplified by online collaboration and open internet access.
*   **Exposed Systems & Services**: Publicly accessible network devices like servers, building management systems, access systems, and cameras lack proper security, increasing risk.
*   **Resource Scarcity**: Limited budgets hinder investments in cybersecurity software and staff, leaving critical systems under-protected.
*   **Legacy Risks**: Outdated IT systems remain vulnerable to exploitation due to lack of updates and security patches.

With hundreds of security researchers across the globe, the Trustwave SpiderLabs team puts its resources to task in looking into what leads to these breaches. We are uniquely positioned to do so, as we perform over 200,000 hours of penetration tests and uncover tens of thousands of vulnerabilities annually. We also have a dedicated email security team analyzing millions of phishing URLs validated daily, including 4,000 to 10,000 per day that are uniquely identified by Trustwave SpiderLabs. Our diverse coverage of infosec disciplines, including Continuous Threat Hunting, Forensics and Incident Response, Malware Reversal, and Database Security, gives us insight into identifying how these breaches occur as well as mitigations and controls that your organization can put in place to prevent these compromises.

We will begin by highlighting the significant trends currently affecting the industry: the shift towards online education, third-party security risks, and the rise of ransomware. Subsequently, we will analyze the attack flow specific to the education industry, offering insight on specific threat actors, actionable intelligence, and recommended mitigations for each stage to illustrate how organizations can proactively identify and prevent attacks to avoid lasting impact.

In this report, we will examine many of the most prevalent threat tactics and threat actors operating across education and throughout the attack chain, including:

**THREAT ACTORS**
*   LockBit 3.0
*   Rhysida
*   CLOP or Cl0p
*   Akira
*   Vice Society
*   No Escape
*   Royal
*   Pirat-Networks
*   ALPHV aka BlackCat
*   Bl00dy Ransomware
*   Medusa

**THREAT TACTICS**
*   Phishing and Social Engineering
*   BYOD and IoT Risks
*   Exploitation of Applications
*   Third-Party Supplier Attacks
and Databases
*   Drive-by Compromise
*   Powershell and User
Execution Techniques
*   Abuse of Valid Account
*   RDP, SMB, and DCOM Lateral
Credentials and Password Attacks
Movement Techniques
*   Access Brokers, Auctions,
*   Ransomware and
and WebShells
Cryptocurrency Miners

For additional information about the most prevalent threat actors, please go to the Appendix.

# Emerging and Prominent Trends

## Shift Towards Online Education

**The Threat**
During the COVID-19 pandemic, the push towards online learning exposed educational institutions to a vast network of devices and systems. While this creates incredible opportunities for accessibility, flexibility, and personalized learning, it also presents significant challenges. Concerns range from cybersecurity and the digital divide to privacy, technical issues, and potential social isolation.

Effectively integrating online education requires careful consideration of these risks and benefits. This includes exploring specific technologies, analyzing successful case studies, staying informed about the evolving landscape, and addressing ethical considerations like algorithmic bias and data ownership. Ultimately, navigating this shift responsibly involves understanding its complexities and paving the way for a future where online and offline learning combine seamlessly to reach students everywhere.

**What Trustwave SpiderLabs Is Seeing**
Trustwave SpiderLabs found significant exposure of critical systems and devices such as public file servers, printers, collaboration systems, and systems storing sensitive data.

Shodan analysis and scans revealed over 1.8 million devices related to the education industry being publicly exposed. As highlighted later in this report, this number significantly dwarfs the exposure in other sectors. Trustwave SpiderLabs also found instances of misconfigured and vulnerable devices, such as publicly accessible conferencing systems and collaboration tools, which could lead to unauthorized access and data breaches.

The operational disruptions caused by data breaches in education can be severe. An example is Lincoln College, which had to permanently close its operations due to a cyberattack. The ransomware attack blocked the college from accessing data used in its student recruitment and retention, as well as fundraising efforts.

**Mitigations to Reduce Risk**
*   Implement strict access controls for critical systems, including file servers, printer management software, and collaboration tools. Strengthen access controls to minimum necessary levels for authorized users.
*   Place all servers behind the firewall and practice proper network segmentation for enhanced access control. Disable Internet access for servers that do not require it.
*   Address misconfigurations in network devices and other IoT devices, ensuring firmware is updated and default passwords are changed.
*   Provide ongoing cybersecurity training and awareness programs for staff and students, emphasizing the importance of security best practices.

## Third-Party Security Risks

**The Threat**
The education sector, like many others, relies heavily on third-party vendors such as software-as-a-service, hosting providers, storage, and IT services for various functions, including learning management systems, email, and communication and collaboration tools.

These third parties pose a grave risk to the education sector because of undiscovered or un-remediated gaps in their cybersecurity controls or data breach protection.

Breaches not only impact the directly targeted institution, but can also have a ripple effect across numerous educational entities relying on the same third-party services.

**What Trustwave SpiderLabs Is Seeing**
Notable incidents include the breaches of Illuminate Education and Blackbaud. The Illuminate breach in early 2022 significantly impacted two of the largest US public school systems, compromising the information of approximately 820,000 students in New York City alone.

The MOVEit RCE (CVE-2023-34362) vulnerability in a third-party file transfer service led to breaches at 13 major universities. These breaches had the highest prevalence from June to August 2023, most often facilitated by the ransomware threat actor Clop.

![Figure 1: CVE-2023-34362 attack claims on notable universities (based on ransomware claims)](https://www.trustwave.com/en-us/resources/library/documents/2024-education-threat-landscape-trustwave-threat-intelligence-briefing-and-mitigation-strategies/figure-1-cve-2023-34362-attack-claims-on-notable-universities/)

**Mitigations to Reduce Risk**
*   Know your supply chain. Keep inventory of all critical suppliers and conduct a comprehensive security assessment before any form of engagement is initiated with a third party.
*   Ensure that third-party vendor contracts have strict cybersecurity clauses. This could include mandating the conducting of regular security audits, immediate breach notification, and compliance with pertinent data protection regulations.
*   Encrypt all sensitive data in transit and at rest. Restrict the access of sensitive data to the principle of least privilege. Carry out regular monitoring of the access logs so that activities of unauthorized or suspicious nature may be detected.
*   Follow industry standards and regulations like GDPR, HIPAA, FERPA, etc. for compliance with geographical location and nature of data handled by third-party vendors.
*   Participate actively in cybersecurity forums of the educational sector and other information sharing platforms.

## Ransomware Attacks

**The Threat**
Ransomware attacks have become a dominant source of breaches in education. These attacks can lead to the loss of critical educational and personal data, disrupt educational processes, and cause substantial financial and reputational damage to institutions.

To facilitate their attacks, threat actors deploy a range of malware types, including loaders/downloaders, infostealers, and RATs, to maintain control, steal information, and to facilitate the end-to-end ransomware process. Attacks targeting universities and primary education schools have led to severe operational disruptions including temporary and even permanent closures. Please refer to our later section on Ransomware for additional details.

**What Trustwave SpiderLabs Is Seeing**
Ransomware attacks striking the education industry are prominent and growing. For example, in 2023, Trustwave researchers monitored 352 ransomware claims against educational institutions.

The top ten ransomware groups targeting the industry were LockBit 3.0, Rhysida, CLOP (aka CL0P, Cl0p), Akira, Medusa, ALPHV, Vice Society, NoEscape, Royal, and Pirat-Networks. These groups have targeted a wide range of educational entities across different countries, predominantly in the US, but also in Canada, the UK, Australia, France, Germany. The types of institutions compromised vary from universities and colleges to public school districts, technical schools, and specific training centers.

![Figure 2: Top ten ransomware groups in the education sector](https://www.trustwave.com/en-us/resources/library/documents/2024-education-threat-landscape-trustwave-threat-intelligence-briefing-and-mitigation-strategies/figure-2-top-ten-ransomware-groups-in-the-education-sector/)

**Mitigations to Reduce Risk**
*   Use host-based anti-malware tools that can assist in identifying and quarantining ransomware, but understand they have limitations and are often circumvented by custom malware packages.
*   Enhance email security controls to protect against ransomware distributed via email. Educate users on the risks of malicious email attachments and phishing attempts. Enhance vigilance and implement email filtering and monitoring systems.
*   Establish and regularly practice a formal Incident Response process. Ensure backups are available as a contingency to recover from a worst-case scenario.
*   Enable system logs on critical systems and workstations and implement network logging through flows, Network Monitoring Solutions, or IDS devices on ingress and egress channels.
*   Implement active monitoring. Merely enabling logs is insufficient; if logs are not monitored, they lose their effectiveness. Regular monitoring helps establish a baseline of regular activity, making abnormal behavior or traffic more conspicuous.
*   Perform ongoing underground and Dark Web monitoring for information leakage that may have been missed.

# Dissecting the Attack Flow for the Education Sector

## Attack Flow Overview

While the specifics and details of every breach and compromise may vary, there is typically a specific attack flow that occurs from the initial security bypass to escalation, compromise, followed by persistent home on your network, and exfiltration and/or destruction of valuable data. The following analysis presents an overview of the attack flow specific to the education sector, incorporating insights from the Trustwave SpiderLabs team and offering actionable mitigations for organizations to implement.

At each stage of the attack flow, the recommended mitigations provide proactive guidance to minimize the potential risks of financial, reputational, regulatory, or physical impacts to an education institution. The typical sequence of events unfolds as follows:

Initial Foothold -> Initial Payload -> Expansion / Pivoting -> Malware -> Exfiltration / Post Compromise

## Attack Flow Steps

### Initial Foothold

This is the step where the attacker successfully triggers a security bypass that will give them the ability to expand their access to suit their motives and goals. This initial foothold can take various forms, ranging from successful phishing attacks to vulnerability exploitation or even logging into public-facing systems using previously acquired credentials.

In this section, we will explore the most common methods through which attackers gain this initial foothold into an education organization, like phishing, third party suppliers and exploitable vulnerabilities.

#### Initial Foothold: Phishing, Spam & Scams

**The Threat**
Phishing stands out as the most commonly exploited method for gaining an initial foothold in an organization. Instead of attempting to exploit vulnerabilities in the software or systems on the network, attackers target staff, faculty, or others who have access to systems within the institution that can be exploited, such as finances, databases, etc.

In a typical scenario, the attacker crafts a compelling email, skillfully persuading the recipient to engage in certain actions. This could include opening an attachment, clicking a link, or executing specific instructions. Education-specific social engineering often involves sending fake university communications like offering enticing student job opportunities, which require the victim to perform certain tasks or provide sensitive information.

Typical phishing goals:
*   **Credential Theft**: An example of this would be an email that appears to be from the university's administration, containing a link. When the recipient clicks this link, they are prompted to enter their login details under the pretense of accessing important information or job opportunity details.
*   **Malware Insertion**: This is often executed through embedding PowerShell scripts, JavaScript, or enabling Macros in a document, which is disguised as being related to the university or a student job offer.
*   **Triggering Specific Actions**: This could involve convincing the recipient to provide confidential information or perform other actions under the guise of a necessary step for a student job application or a university-related process.

**Trustwave SpiderLabs Insights**
The Trustwave SpiderLabs team is committed to monitoring various email-based threats, such as opportunistic phishing, spearphishing, spam-based malware, and scams. In the past year, our team has noted interesting developments in the tactics and delivery approaches used in email-based attacks within education. These advancements have played a role in sustaining the continuing significance and effectiveness of these types of attacks.

In the education sector, the most common types of email attachments used for phishing and malware distribution are HTML files, executables, and PDFs, a trend that echoes observations from other industries. Notably, HTML attachments make up 82% of malicious email attachments. These attachments are primarily used in two forms: as standalone HTML pages designed for credential phishing, often featuring sophisticated obfuscation techniques, or as HTML redirectors leading to malicious sites. Additionally, Trustwave original research has also seen a preference of the use of HTML attachments in Phishing Kits.

![Figure 3: Top malicious attachment filetypes for the education sector](https://www.trustwave.com/en-us/resources/library/documents/2024-education-threat-landscape-trustwave-threat-intelligence-briefing-and-mitigation-strategies/figure-3-top-malicious-attachment-filetypes-for-the-education-sector/)

Trustwave researchers have observed that threat actors are frequently misusing specific services for these attacks. Decentralized InterPlanetary File System (IPFS) links, such as 'dweb.link,' are used to distribute phishing content, exploiting its network to avoid detection. Google Services, with domains like 'googleapis.com,' are abused for their trustworthiness to slip past security filters. Compromised WordPress sites, for example, 'howtotender.co.za,' are hijacked to host fake login pages. Cloudflare Services, including 'workers.dev,' are manipulated for their credibility to host phishing material. Additionally, free web and app hosting platforms, such as 'netlify.app,' are favored by phishers for cost-free malicious site creation.

In the education sector, Trustwave researchers have observed several notable phishing campaign themes:

**RFQ-THEMED MALWARE SPAM**
In a recent phishing scheme targeting universities, Trustwave SpiderLabs researchers observed attackers sending emails masquerading as “requests for quotations” from various educational institutions. To enhance their authenticity, these emails featured the spoofed university's logo in the message body and incorporated the institution's name in the 'From' and 'Subject' headers, as well as in the filenames of attachments.

![Figure 4: Sample of malicious “request for quotations” impersonating various universities](https://www.trustwave.com/en-us/resources/library/documents/2024-education-threat-landscape-trustwave-threat-intelligence-briefing-and-mitigation-strategies/figure-4-sample-of-malicious-request-for-quotations-impersonating-various-universities/)

To further increase the authenticity of the attacks, the emails suggested that the quotations should align with the university’s annual budget, with more details purportedly in the attached file. However, these attachments were either malicious executables or archives containing them. The threats most delivered through this phishing theme included the Lokibot Infostealer, Agent Tesla RAT, and Downloader Guloader.

**FAKE UNIVERSITY COMMUNICATIONS**
In another common phishing campaign, university accounts of students, faculty, and staff were targeted with fraudulent emails purporting to be official university communications.

![Figure 5: Sample of malicious email impersonating an official university communication that leads to a credential phishing site](https://www.trustwave.com/en-us/resources/library/documents/2024-education-threat-landscape-trustwave-threat-intelligence-briefing-and-mitigation-strategies/figure-5-sample-of-malicious-email-impersonating-an-official-university-communication-that-leads-to-a-credential-phishing-site/)

These messages impersonated the university's IT department and were crafted to look authentic. They bolster their credibility by integrating the university's branding and language style, often relating to current university events or settings. The emails typically include urgent calls to action, such as requests to verify accounts or update personal information, and direct recipients to fake websites designed to harvest their credentials.

**STUDENT JOB OFFER SCAMS**
Trustwave researchers observed an uptick in scam messages targeting students with counterfeit job offers. These emails come unsolicited and usually present lucrative opportunities that promise high compensation for minimal effort and offer flexible working hours.

Typically, these communications initiate with a request for personal details as part of the job application process. Scammers may also demand an advance payment under the pretext of covering training expenses. In some cases, students receive a fraudulent check with instructions to deposit it and forward a portion of the funds elsewhere, only to find out later that the check is fake, rendering the student