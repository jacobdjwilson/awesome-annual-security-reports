# 2025 Trustwave Risk Radar Report: Energy & Utilities Sector

## Table of Contents
- [Energy and Utilities’ Unique Threat Landscape](#energy-and-utilities-unique-threat-landscape)
- [Notable & Prominent Trends in Energy & Utilities Sector](#notable--prominent-trends-in-energy--utilities-sector)
- [Ransomware Trends](#ransomware-trends)
- [Ransomware Threat Groups](#ransomware-threat-groups)
- [IT/OT Convergence](#itot-convergence)
- [Evolving Regulatory Pressures](#evolving-regulatory-pressures)
- [Threat Actor Techniques by Attack Stage](#threat-actor-techniques-by-attack-stage)
- [Conclusion & Key Takeaways](#conclusion--key-takeaways)

---

For the past two years, Trustwave SpiderLabs has released research analyzing industry-specific attack flows, offering insights into threat actors, actionable intelligence, and recommended mitigations for each attack stage. In this report, we delve into the unique cybersecurity challenges facing the energy and utilities sector, which is increasingly targeted due to its critical role in supporting national and global infrastructures.

The Trustwave SpiderLabs team highlights significant trends shaping the industry, including the rise of ransomware, the convergence of operational technology (OT) and information technology (IT), and evolving regulatory pressures. We also address the growing sophistication of threat actors and provide a comprehensive overview of the tactics, techniques, and procedures (TTPs) they employ, categorized by attack stage. This intelligence empowers energy sector organizations to better prepare, detect, and mitigate potential attacks.

Additionally, Trustwave SpiderLabs has produced two in-depth analyses focusing on critical areas of concern: notable trends in ransomware attacks and detailed profiles of the most active and dangerous ransomware groups. These reports offer extensive research and actionable strategies for mitigating risk. For example, ransomware attacks targeting the energy and utilities sector have increased by 80% year over year, underscoring the growing urgency of addressing this threat.

In this research, we’ve categorized energy and utilities to include the production, distribution, and storage of oil and gas, renewable energy, and nuclear energy, as well as the generation and distribution of electricity, gas, and water. This broad scope reflects the sector’s complexity and the interconnectedness of its diverse systems, each presenting its own unique security challenges.

### Key Report Findings for the Energy & Utilities Sector
- **80%**: Increase in ransomware activity YoY.
- **47%**: Of ransomware attacks in the United States.
- **19%**: Of ransomware attacks were conducted by Hunters International in H2 2024.
- **84%**: Of attacks originated from phishing.
- **96%**: Of attackers relied on remote services to move laterally.
- **67%**: Of credential access techniques were brute force.

---

## Energy and Utilities’ Unique Threat Landscape

### IT/OT Convergence
The energy and utilities sector heavily relies on the integration of physical infrastructure/OT (power plants, pipelines, etc.) with cyber systems/IT (SCADA, IoT devices). The integration of these two domains has created a more efficient and responsive energy ecosystem, but it has also introduced a complex and expanded attack surface for cybercriminals. Traditionally, OT systems were isolated or “air-gapped” from the Internet to prevent remote cyberattacks. However, the need for real-time data exchange, remote monitoring, and automation has led to the increased connection of OT systems to IT networks. This convergence allows for greater operational efficiencies and enables cybercriminals to exploit vulnerabilities in previously isolated systems.

A successful cyberattack on an OT system can result in not just data breaches, but physical damage to infrastructure, disruptions in service, or even safety incidents that put human lives at risk. As IT/OT boundaries continue to blur, organizations must adopt a holistic cybersecurity approach that addresses both domains simultaneously.

### Critical Infrastructure
Energy and utility systems form the backbone of modern society, making them a prime target for cyberattacks with potentially devastating consequences. A cyberattack targeting a critical energy infrastructure—such as a power grid, oil pipeline, or water supply system—can cause widespread disruptions that ripple across multiple sectors.

For instance, a breach that takes down the electrical grid can disable communication systems, halt manufacturing processes, and disrupt transportation networks. In more severe cases, such an attack can compromise healthcare services by incapacitating hospitals that rely on electricity for medical equipment and patient care. Furthermore, because the energy sector is also interconnected with other essential services like telecommunications and finance, an attack on one industry can have cascading effects, jeopardizing public safety and national security.

The convergence of physical and digital systems in energy operations means even localized disruptions can have far-reaching consequences, making cybersecurity in this sector a matter of national interest. Governments and regulators recognize the importance of securing these systems, and attacks on critical infrastructure are often treated as matters of national security.

### Regulatory Compliance
The energy and utilities sector is subject to rigorous and evolving cybersecurity regulations designed to protect national and economic security. Regulatory frameworks like NERC CIP (North American Electric Reliability Corporation Critical Infrastructure Protection) in the US and NIS2 (Network and Information Security Directive 2) in the EU establish mandatory cybersecurity requirements for critical infrastructure operators.

These regulations include guidelines for securing networks, monitoring vulnerabilities, and ensuring data integrity in both IT and OT environments. Compliance is not just about adhering to best practices; it also includes requirements for reporting cyber incidents in a timely manner, often with strict deadlines. Non-compliance can lead to significant financial penalties, litigation, and reputational damage.

> **American Water, Largest Water Utility Company in the U.S. Targeted in Cyberattack**
> *October 2024, CNBC*

### Aging Infrastructure and Legacy Systems
A significant challenge facing the energy and utilities sector is the widespread reliance on aging infrastructure and legacy systems. The average age of electrical infrastructure in the US is 40 years—with 25% of the grid being 50-plus years old—and many systems still use decades-old IT systems. Many critical systems, particularly in the OT domain, were designed decades ago and were not built with modern cybersecurity threats in mind. These legacy systems often lack the necessary patches, updates, and support to address evolving vulnerabilities.

### OT Complexity
OT systems are often more complex and specialized than traditional IT systems, requiring a unique approach to cybersecurity. These systems are responsible for controlling and monitoring industrial operations—everything from power generation and distribution to water treatment and gas pipeline management. Unlike IT systems, which are built around general-purpose software and hardware, OT systems often rely on proprietary software, specialized control systems (like SCADA—Supervisory Control and Data Acquisition), and customized hardware.

### Geopolitical Significance
The energy sector holds immense geopolitical significance, and as such, is a frequent target for nation-state actors. Energy infrastructure is often viewed as critical not only for economic stability but also for national security. Disrupting or sabotaging energy systems can destabilize a country’s economy, hinder military operations, and disrupt the functioning of key sectors like healthcare, transportation, and communications.

---

## Notable & Prominent Trends in Energy & Utilities Sector

## Ransomware Trends
The number of ransomware attacks, which is based on claims published on group’s extortion websites for the energy and utilities sector, was significantly higher in H2 2023 and H1 2024.

![Chart showing ransomware attacks in Energy and Utilities from 2022H2 to 2024H2]

### Mitigations to Reduce Risk
- **Implement Robust Network Segmentation**: Separate OT from IT networks to prevent lateral movement of attackers within systems.
- **Invest in Threat Detection and Response Tools**: Deploy advanced intrusion detection systems (IDS) and intrusion prevention systems (IPS) tailored for OT environments.
- **Regularly Update and Patch Systems**: Ensure timely updates and patches for all software, firmware, and operating systems.
- **Conduct Regular Security Assessments**: Perform penetration testing to identify weaknesses in IT and OT networks.
- **Enhance Employee Awareness and Training**: Provide regular cybersecurity training tailored to energy and utilities sector-specific threats.

---

## Ransomware Threat Groups
While groups such as Conti, LockBit, Cl0p, and others dominate the headlines, our researchers wanted to shift the focus to lesser-known but active ransomware groups from the past year—specifically Play, 8Base, Hunters International, and Qilin.

- **Play**: Active since June 2022. They target a wide range of businesses and critical infrastructure across North America, South America, and Europe.
- **Hunters International**: Financially motivated group that emerged in early October 2023. They deny direct affiliation with Hive but claim to have acquired Hive’s source code.
- **8Base**: Financially motivated RaaS affiliate program active since at least March 2022. They focus on stealing sensitive information for extortion purposes without deploying ransomware.
- **Qilin**: Active since early 2023. Known for sophisticated attack methods and a focus on high-value targets.

> **Schneider Electric Reports Cyberattack, its Third Incident in 18 Months**
> *November 2024, CyberScoop*

---

## IT/OT Convergence
The convergence of IT and OT systems has created new opportunities for efficiency, automation, and innovation. However, this convergence has also introduced significant cybersecurity risks. IT systems are often designed with flexibility and remote access in mind, while OT systems are generally more rigid and have been historically isolated.

### What Trustwave Is Seeing
- **Increased Attack Surface**: Proliferation of IoT devices and network complexity.
- **Vulnerabilities in OT Systems**: Legacy systems with outdated security protocols and a lack of security focus.
- **Potential Consequences**: Physical damage, operational disruptions, data breaches, financial loss, and reputational damage.

> **Volt Typhoon Hits Multiple Electric Utilities, Expands Cyber Activity**
> *February 2024, Dark Reading*

---

## Evolving Regulatory Pressures
As the energy, utilities, and oil and gas sectors continue to digitize, regulatory bodies have placed increasing emphasis on cybersecurity to protect critical infrastructure.

### Key Regulations
- **US: NERC CIP**: Cybersecurity standards designed to secure the North American bulk power system.
- **US: CMMC**: Cybersecurity Maturity Model Certification for contractors working with the DoD.
- **EU and UK: NIS Directive**: Requires energy providers to implement robust cybersecurity measures and report significant incidents.
- **Australia: SOCI Act**: Legislation aimed at securing critical infrastructure across several sectors.

> **Key Electricity Distributor in Romania Warns of ‘Cyber Attack in Progress’**
> *December 2024, The Record*

---

## Threat Actor Techniques by Attack Stage

### Initial Access Techniques
- **Phishing (T1566)**: 84%
- **Exploit Public-Facing Application (T1190)**: 16%

### Execution Techniques
- **User Execution (T1204)**: 48%
- **Command and Scripting Interpreter (T1059)**: 45%

### Credential Access Techniques
- **Brute Force (T1110)**: 67%
- **Steal or Forge Kerberos Tickets (T1558)**: 27%

### Lateral Movement Techniques
- **Remote Services (T1021)**: 96%

### Persistence Techniques
- **External Remote Services (T1133)**: 49%
- **Create Account (T1136)**: 27%

> **Costa Rica State Energy Company Calls in US Experts to Help with Ransomware Attack**
> *December 2024, The Record*

---

## Conclusion & Key Takeaways
The energy and utilities sector faces a unique set of cybersecurity challenges, largely due to its critical role in powering national economies and global infrastructure. As the lines between OT and IT continue to blur, the sector finds itself increasingly vulnerable to sophisticated cyberattacks.

### Key Takeaways
- **Ransomware Threats**: Attacks targeting energy and utility providers have surged.
- **IT/OT Convergence**: A unified cybersecurity approach across both domains is now more important than ever.
- **Regulatory Compliance**: Staying compliant is essential for reducing vulnerabilities and safeguarding critical infrastructure.
- **Aging Infrastructure**: Companies must invest in upgrading systems and enhance collaboration between IT and OT teams.
- **Geopolitical Significance**: Providers must be ready to defend against highly sophisticated threats that are as much about national security as they are about financial gain.