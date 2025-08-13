# 2025 Trustwave Risk Radar Report: Energy & Utilities Sector

## Table of Contents
- [Energy and Utilities’ Unique Threat Landscape](#energy-and-utilities-unique-threat-landscape)
- [Notable & Prominent Trends in Energy & Utilities Sector](#notable-prominent-trends-in-energy-utilities-sector)
  - [Ransomware Trends](#ransomware-trends)
  - [Ransomware Threat Groups](#ransomware-threat-groups)
  - [IT/OT Convergence](#itot-convergence)
  - [Evolving Regulatory Pressures](#evolving-regulatory-pressures)
- [Threat Actor Techniques by Attack Stage](#threat-actor-techniques-by-attack-stage)
- [Conclusion & Key Takeaways](#conclusion-key-takeaways)

For the past two years, Trustwave SpiderLabs has released research analyzing industry-specific attack flows, offering insights into threat actors, actionable intelligence, and recommended mitigations for each attack stage. In this report, we delve into the unique cybersecurity challenges facing the energy and utilities sector, which is increasingly targeted due to its critical role in supporting national and global infrastructures.

In this research, we’ve categorized energy and utilities to include the production, distribution, and storage of oil and gas, renewable energy, and nuclear energy, as well as the generation and distribution of electricity, gas, and water. This broad scope reflects the sector’s complexity and the interconnectedness of its diverse systems, each presenting its own unique security challenges.

The Trustwave SpiderLabs team highlights significant trends shaping the industry, including the rise of ransomware, the convergence of operational technology (OT) and information technology (IT), and evolving regulatory pressures. We also address the growing sophistication of threat actors and provide a comprehensive overview of the tactics, techniques, and procedures (TTPs) they employ, categorized by attack stage. This intelligence empowers energy sector organizations to better prepare, detect, and mitigate potential attacks.

Additionally, Trustwave SpiderLabs has produced two in-depth analyses focusing on critical areas of concern: notable trends in ransomware attacks and detailed profiles of the most active and dangerous ransomware groups. These reports offer extensive research and actionable strategies for mitigating risk. For example, ransomware attacks targeting the energy and utilities sector have increased by 80% year over year, underscoring the growing urgency of addressing this threat.

The sector faces several unique challenges which makes it particularly vulnerable to a diverse range of threats, from ransomware targeting critical infrastructure to spear-phishing campaigns aimed at exploiting human vulnerabilities. These challenges include the prevalence of aging infrastructure, reliance on legacy systems, and the complexity of OT systems. Coupled with the sector’s geopolitical significance and the potential for widespread societal impact, these factors make the energy and utilities industry a prime target for malicious actors.

The increasing reliance on digital technologies, remote operations, and cloud-based systems has expanded the attack surface, creating new vulnerabilities that must be addressed through robust cybersecurity measures. For example, earlier this year, the North American Electric Reliability Corporation (NERC) warned that US power grids are becoming increasingly vulnerable to cyberattacks, with “the number of susceptible points in electrical networks increasing by about 60 per day.” This fact highlights the urgency for energy providers to bolster their cybersecurity defenses.

While the average cost of a data breach in the energy sector is $5.29 million, higher than the overall cross-industry average of $4.8 million, the potential consequences extend far beyond financial loss. A cyberattack can lead to operational disruptions, physical damage, and reputational harm. Given the critical role of the energy sector in society, a cyberattack can have significant societal implications, including power outages, supply chain disruptions, and national security risks. As a result, energy and utility providers must prioritize cybersecurity to ensure the reliability and resilience of their operations.

### Key Report Findings for the Energy & Utilities Sector

- **80%** increase in ransomware activity YoY
- **19%** of ransomware attacks were conducted by Hunters International in H2 2024
- **96%** of attackers relied on remote services to move laterally
- **47%** of ransomware attacks in the United States
- **84%** of attacks originated from phishing
- **67%** of credential access techniques were brute force

## Energy and Utilities’ Unique Threat Landscape

### IT/OT Convergence

- The energy and utilities sector heavily relies on the integration of physical infrastructure/OT (power plants, pipelines, etc.) with cyber systems/IT (SCADA, IoT devices). The integration of these two domains has created a more efficient and responsive energy ecosystem, but it has also introduced a complex and expanded attack surface for cybercriminals. Traditionally, OT systems were isolated or “air-gapped” from the Internet to prevent remote cyberattacks. However, the need for real-time data exchange, remote monitoring, and automation has led to the increased connection of OT systems to IT networks. This convergence allows for greater operational efficiencies and enables cybercriminals to exploit vulnerabilities in previously isolated systems.
- A successful cyberattack on an OT system can result in not just data breaches, but physical damage to infrastructure, disruptions in service, or even safety incidents that put human lives at risk. As IT/OT boundaries continue to blur, organizations must adopt a holistic cybersecurity approach that addresses both domains simultaneously.

### Critical Infrastructure

- Energy and utility systems form the backbone of modern society, making them a prime target for cyberattacks with potentially devastating consequences. A cyberattack targeting a critical energy infrastructure—such as a power grid, oil pipeline, or water supply system—can cause widespread disruptions that ripple across multiple sectors.
- For instance, a breach that takes down the electrical grid can disable communication systems, halt manufacturing processes, and disrupt transportation networks. In more severe cases, such an attack can compromise healthcare services by incapacitating hospitals that rely on electricity for medical equipment and patient care. Furthermore, because the energy sector is also interconnected with other essential services like telecommunications and finance, an attack on one industry can have cascading effects, jeopardizing public safety and national security.
- The convergence of physical and digital systems in energy operations means even localized disruptions can have far-reaching consequences, making cybersecurity in this sector a matter of national interest. Governments and regulators recognize the importance of securing these systems, and attacks on critical infrastructure are often treated as matters of national security.

### Regulatory Compliance

- The energy and utilities sector is subject to rigorous and evolving cybersecurity regulations designed to protect national and economic security. Regulatory frameworks like NERC CIP (North American Electric Reliability Corporation Critical Infrastructure Protection) in the US and NIS2 (Network and Information Security Directive 2) in the EU establish mandatory cybersecurity requirements for critical infrastructure operators.
- These regulations include guidelines for securing networks, monitoring vulnerabilities, and ensuring data integrity in both IT and OT environments. Compliance is not just about adhering to best practices; it also includes requirements for reporting cyber incidents in a timely manner, often with strict deadlines. Non-compliance can lead to significant financial penalties, litigation, and reputational damage that could undermine consumer trust and investor confidence. As cybersecurity threats evolve, these regulations continue to become more stringent, pushing organizations to invest in advanced cybersecurity technologies, processes, and employee training to stay ahead of potential risks. Given the high stakes involved, the ability to demonstrate compliance has become a critical component of corporate governance in the energy sector.

### Aging Infrastructure and Legacy Systems

- A significant challenge facing the energy and utilities sector is the widespread reliance on aging infrastructure and legacy systems. The average age of electrical infrastructure in the US is 40 years— with 25% of the grid being 50-plus years old — and many systems still use decades-old IT systems. Many critical systems, particularly in the OT domain, were designed decades ago and were not built with modern cybersecurity threats in mind. These legacy systems often lack the necessary patches, updates, and support to address evolving vulnerabilities. Additionally, they may run on outdated software and hardware that is incompatible with newer security solutions, making it difficult to implement necessary cybersecurity upgrades without disrupting critical operations.
- Many energy companies are also wary of making large investments in overhauling aging infrastructure due to the high costs and potential disruptions to service. As a result, legacy systems remain a significant security risk, particularly when connected to modern networks or IoT devices that may have stronger, but different, security features. Ensuring the protection of legacy systems while transitioning to more secure, modern technologies requires careful planning, increased investment, and collaboration between IT and OT teams to ensure a seamless integration of security measures without compromising operational continuity.

> American Water, Largest Water Utility Company in the U .S . Targeted in Cyberattack
>
> October 2024, CNBC

### OT Complexity

- OT systems are often more complex and specialized than traditional IT systems, requiring a unique approach to cybersecurity. These systems are responsible for controlling and monitoring industrial operations— everything from power generation and distribution to water treatment and gas pipeline management. Unlike IT systems, which are built around general-purpose software and hardware, OT systems often rely on proprietary software, specialized control systems (like SCADA—Supervisory Control and Data Acquisition), and customized hardware.
- Securing OT systems requires professionals to possess specialized knowledge in cybersecurity and the specific industrial processes they support. Cybersecurity teams need to understand the underlying engineering and and operations of OT systems, as vulnerabilities in these systems can have immediate, tangible consequences on physical infrastructure.
- The traditional “patch-and-update” approaches used in IT security are often not feasible in OT environments due to concerns over system downtime and operational disruption. As a result, OT cybersecurity requires a more nuanced strategy that balances the need for security with the need for continuous, uninterrupted operations.

### Geopolitical Significance:

- The energy sector holds immense geopolitical significance, and as such, is a frequent target for nation-state actors. Energy infrastructure is often viewed as critical not only for economic stability but also for national security. Disrupting or sabotaging energy systems can destabilize a country’s economy, hinder military operations, and disrupt the functioning of key sectors like healthcare, transportation, and communications.
- Nation-state actors may target energy infrastructure for various reasons, including espionage (gathering intelligence), cyber-sabotage (disrupting operations), or even as part of hybrid warfare strategies designed to weaken or destabilize a rival nation. For example, state-sponsored cyberattacks can target power grids or pipeline systems with the intent of causing blackouts, fuel shortages, or broader systemic chaos.
- The threat landscape is further complicated by the potential for cyberattacks to be used in conjunction with physical attacks, creating a “blended” threat environment where cyber incidents can amplify the impact of traditional kinetic attacks. As a result, energy organizations must be prepared to defend against highly sophisticated, well-funded adversaries with both cyber and geopolitical motives, making the cybersecurity challenge in this sector one of the most complex and critical facing the global economy today.

![Diagram illustrating Cybersecurity Challenges in Energy and Utilities Sector. A central circle labeled "Cybersecurity Challenges in Energy and Utilities Sector" is connected by spokes to six key areas: IT/OT Convergence, Critical Infrastructure, Regulatory Compliance, Aging Infrastructure and Legacy Systems, OT Complexity, and Geopolitical Significance. Each area has sub-bullets:
- **IT/OT Convergence**: Expanded Attack Surface, Real-time Data Exchange, Holistic Cybersecurity Approach
- **Critical Infrastructure**: Widespread Disruptions, Cascading Effects, National Security
- **Regulatory Compliance**: NERC CIP and NIS2, Incident Reporting, Financial Penalties
- **Aging Infrastructure and Legacy Systems**: Old IT Systems, Incompatible Software, High Overhaul Costs
- **OT Complexity**: Proprietary Software, Specialized Control Systems, Nuanced Security Strategies
- **Geopolitical Significance**: Nation-state Actors, Espionage and Cyber-sabotage, Blended Threat Environment](Image description of Cybersecurity Challenges Diagram)

With more than 250 cybersecurity experts across the globe, the Trustwave SpiderLabs team puts its resources to task researching the top threats in today’s landscape. We are uniquely positioned to do so, as we perform over 200,000 hours of penetration tests and uncover tens of thousands of vulnerabilities annually. We also have a dedicated email security team analyzing millions of phishing URLs daily, including 10k per day that are uniquely identified by Trustwave SpiderLabs. Our diverse coverage of infosec disciplines, including Advanced Continuous Threat Hunting, Digital Forensics and Incident Response, Malware Reversal, and Database Security, give us insight into identifying how these breaches occur, as well as mitigations and controls that your organization can put in place to prevent these compromises.

This report examines the myriads of threats facing the energy and utilities industry. In addition to supplemental reports focused on notable trends in ransomware attacks and detailed profiles of the most active and dangerous ransomware groups, Trustwave SpiderLabs will offer recommendations to help providers mitigate risks and safeguard their operations.

## Notable & Prominent Trends in Energy & Utilities Sector

### Ransomware Trends

#### The Threat

We explore ransomware trends in the energy and utilities sector in depth in our accompanying report. At a high level, here are some key points to consider:

The rising frequency of ransomware attacks against the energy and utilities sector underscores the need for robust cybersecurity resilience strategies, designed to proactively identify, mitigate, and respond to breaches and ransomware attacks. There are a few reasons why this sector is often targeted by attackers:

- It consists of prosperous organizations with considerable revenues, making them lucrative targets
- The interconnected nature of SCADA systems, including IoT devices and remote access points, provides multiple entry points for cyber attackers
- Recovery time is longer compared to other sectors
- Disruption has high operational costs

#### What Trustwave Is Seeing

The number of ransomware attacks, which is based on claims published on group’s extortion websites for the energy and utilities sector, was significantly higher in H2 2023 and H1 2024.

The below data shows more than an 80% increase in ransomware activity in H1 2024 and H2 2023 than the same time period one year prior.

![Figure 1: Bar chart showing the number of ransomware attacks waged against the energy and utilities sector since H2 2022. The counts are: 2022H2: 53, 2023H1: 84, 2023H2: 44, 2024H1: 132, 2024H2: 125.](Image description of Ransomware Attacks in Energy and Utilities chart)

#### Top Ransomware Groups Since H2 2022

![Figure 2: Bar chart showing ransomware groups targeting energy and utilities and the count of attacks since H2 2022. Top groups include: LockBit3.0 (85), AlphV (36), Play (27), CL0P (26), 8BASE (20), BlackBasta (20), Hunters Int. (16), BianLian (15), Akira (13), RansomHub (12), Royal (11), Qilin (10), Medusa (8), No Escape (7), Black Suit (7), Rhysida (7), Quantum (7), CUBA (7), Cactus (7), hellcat (5). Other groups have 4 or fewer attacks.](Image description of Top Ransomware Groups Since H2 2022 chart)

When looking at the trends since H2 2022, LockBit and AlphV are the most active groups, with Play, Cl0P, and 8Base following.

However, in the chart below, in the second half of 2024, Hunters International and Qilin took a lead in launching attacks against the energy and utilities sector compared to other groups. Hunters International accounted for 19% of attacks (8 total), Qilin accounted for 14% (6 total), and Akira accounted for 10% (4 total).

![Figure 3: Bar chart showing ransomware groups targeting the energy and utilities sector and the number of attacks waged by each group in H2 2024. Top groups include: Hunter's Int (8), Qilin (6), Akira (4), RansomHub (3), Play (3), BianLian (2), Medusa (2), BlackSuit (2), lynx (1), meow (1), termite (1), Abyss (1), helldown (1), Dragon Force (1), sarcoma (1), Lockbit 3.0 (1), Monti (1), killsec (1), Cactus (1), hellcat (1).](Image description of Top Ransomware Groups in H2 2024 chart)

In our accompanying report, *Energy and Utilities Deep Dive: Ransomware Threat Groups*, we examine these threat groups in more detail.

The United States is the most often targeted country, accounting for 47% of the attacks followed by the European Union region (11%), Canada (8%), and United Kingdom (7%).

![Figure 4: Pie chart showing countries and regions targeted by ransomware actors in the energy and utilities sector since H2 2022. The percentages are: United States (47%), European Union (11%), Canada (8%), United Kingdom (7%), Indonesia (3%), United Arab Emirates (2%), Brazil (2%), Italy (2%), Columbia (1%), Malaysia (1%), Other (16%).](Image description of Top Countries Targeted by Ransomware chart)

> Russian Hacking Group Claims Responsibility for Cyberattack on Indiana Wastewater Plant
>
> April 2024, StateScoop

#### Mitigations to Reduce Risk

- **Implement Robust Network Segmentation:** Separate OT from IT networks to prevent lateral movement of attackers within systems. Limit access between critical systems and external networks, including the internet.
- **Invest in Threat Detection and Response Tools:** Deploy advanced intrusion detection systems (IDS) and intrusion prevention systems (IPS) tailored for OT environments. Leverage endpoint detection and response (EDR) solutions to monitor malicious activities across devices. Use security information and event management (SIEM) platforms for centralized visibility and real-time threat analysis.
- **Conduct Regular Security Assessments:** Perform penetration testing to identify weaknesses in IT and OT networks. Undertake periodic risk assessments to evaluate and mitigate potential threats. Simulate phishing attacks to test employee awareness and response capabilities.
- **Enhance Employee Awareness and Training:** Provide regular cybersecurity training tailored to energy and utilities sector-specific threats. Educate employees on recognizing phishing attempts, social engineering tactics, and other common attack vectors. Create a culture of cybersecurity responsibility across all levels of the organization.
- **Regularly Update and Patch Systems:** Ensure timely updates and patches for all software, firmware, and operating systems, especially legacy OT systems that are often overlooked. Establish a patch management schedule to systematically address vulnerabilities.

### Ransomware Threat Groups

#### The Threat

We cover ransomware threat groups in more depth in our accompanying report. At a high level, here are some key points to consider:

While groups such as Conti, LockBit, Cl0p, and others dominate the headlines, our researchers wanted to shift the focus to lesser-known but active ransomware groups from the past year—specifically Play, 8Base, Hunters International, and Qilin—providing a comprehensive understanding of the evolving threat landscape.

Over the years, ransomware groups have shown resilience and adaptability, often dismantled by law enforcement only to reemerge under new identities. For example, the Conti group fractured in 2022 after internal leaks tied to differing views on the Russia-Ukraine