# 2025 Trustwave Risk Radar Report: Manufacturing Sector

## Table of Contents
- [Introduction](#introduction)
- [Key Report Findings for the Manufacturing Sector](#key-report-findings-for-the-manufacturing-sector)
- [Manufacturing’s Unique Threat Landscape](#manufacturings-unique-threat-landscape)
  - [Reliance on Legacy Systems](#reliance-on-legacy-systems)
  - [Increasing Connectivity of Manufacturing Systems](#increasing-connectivity-of-manufacturing-systems)
  - [Potential for Physical Damage and Disruption](#potential-for-physical-damage-and-disruption)
  - [Lack of Visibility and Control](#lack-of-visibility-and-control)
  - [Cultural Mindset Gap](#cultural-mindset-gap)
- [Notable and Prominent Trends in Manufacturing](#notable-and-prominent-trends-in-manufacturing)
  - [Convergence of IT and OT](#convergence-of-it-and-ot)
    - [The Threat](#the-threat)
    - [What Trustwave Is Seeing](#what-trustwave-is-seeing)
    - [Mitigations to Reduce Risk](#mitigations-to-reduce-risk)
  - [Methods Used to Target Manufacturing](#methods-used-to-target-manufacturing)
    - [The Threat](#the-threat-1)
    - [What Trustwave Is Seeing](#what-trustwave-is-seeing-1)
    - [Mitigations to Reduce Risk](#mitigations-to-reduce-risk-1)
  - [Ransomware Groups Continue to Target Manufacturers](#ransomware-groups-continue-to-target-manufacturers)
    - [The Threat](#the-threat-2)
    - [What Trustwave Is Seeing](#what-trustwave-is-seeing-2)
    - [Mitigations to Reduce Risk](#mitigations-to-reduce-risk-2)
- [Threat Actor Techniques by Attack Stage](#threat-actor-techniques-by-attack-stage)
  - [Initial Access Techniques](#initial-access-techniques)
  - [Execution Techniques](#execution-techniques)
  - [Persistence Techniques](#persistence-techniques)
  - [Defense Evasion Techniques](#defense-evasion-techniques)
  - [Credential Access Techniques](#credential-access-techniques)
  - [Lateral Movement Techniques](#lateral-movement-techniques)
- [Conclusion & Key Takeaways](#conclusion--key-takeaways)
  - [Conclusion](#conclusion-1)
  - [Key Takeaways](#key-takeaways)

# 2025 Trustwave Risk Radar Report: Manufacturing Sector

The official report URL is: https://www.levelblue.com/blogs/spiderlabs-blog/2025-trustwave-risk-radar-report-top-cyber-threats-targeting-the-manufacturing-sector/

## Introduction

Last year, Trustwave released its Manufacturing Threat Intelligence Briefing, analyzing attack flows specific to the manufacturing sector. The report provided insight into threat actors, actionable intelligence, and recommended mitigations for each stage of an attack.

Building on that foundation, our 2025 report takes a deeper dive into the evolving challenges and risks facing the manufacturing industry. The Trustwave SpiderLabs team highlights key trends reshaping the sector and offers a comprehensive breakdown of threat actor tactics categorized by attack stage, equipping manufacturers with critical knowledge to strengthen their cybersecurity posture.

In addition, Trustwave SpiderLabs has produced two detailed analyses focusing on pressing areas of concern: the convergence of informational technology (IT) and operational technology (OT) systems and the methods threat actors are using to target manufacturers. These reports provide in-depth research, offering manufacturers a clearer understanding of the current landscape and actionable risk mitigation strategies.

Cybersecurity in manufacturing is especially complex, driven by the increasing integration of IT/OT environments. These environments often span shop floor systems, enterprise networks, and interconnected supply chains, creating numerous attack vectors. Manufacturers are facing a growing array of threats—from ransomware attacks that disrupt production to data breaches exposing sensitive intellectual property. The adoption of Industry 4.0 technologies, including the Industrial Internet of Things (IIoT) and cloud-based platforms, has expanded the attack surface and introduced new vulnerabilities.

The average cost of a data breach in the manufacturing sector is $5.6 million— up from last year’s figure of $4.7 million and higher than the overall industry average of $4.8 million. However, the full impact of a cyberattack can extend far beyond financial losses. Disruptions to production lines can lead to substantial financial losses, while breaches of sensitive design data or customer information can erode trust and damage brand reputation.

Critically, security incidents impacting OT can have severe safety implications. A compromised industrial control system (ICS) could lead to equipment malfunctions, hazardous material releases, or even physical injuries to workers on the production floor.

Therefore, robust cybersecurity measures are essential—not only to protect manufacturing operations and ensure business continuity but also to safeguard worker safety and prevent potentially catastrophic accidents.

## Key Report Findings for the Manufacturing Sector

- **87%** of attacks originated from phishing
- **19%** of ransomware attacks were conducted by Play
- **14%** of ransomware attacks targeted machinery manufacturers
- **86%** of credential access techniques were brute-force attempts
- **54%** of ransomware attacks were in the US

## Manufacturing’s Unique Threat Landscape

### Reliance on Legacy Systems:

- Many manufacturers continue to rely heavily on legacy systems and operational technologies that were designed long before modern cybersecurity challenges emerged. These outdated systems often lack the security features required to defend against today’s advanced cyber threats. Due to their age and complexity, legacy systems can be extremely difficult, if not impossible, to update or patch regularly. As a result, they often contain known vulnerabilities that cybercriminals can easily exploit.
- For instance, brute-force attacks against outdated hardware and software can be a simple yet effective way for attackers to gain unauthorized access. Cybercriminals frequently target specific vulnerabilities in legacy systems, which are often widely documented, making it easier for hackers to conduct targeted, highly effective attacks. The risk is further compounded by the fact that many manufacturers lack the resources or expertise to replace or modernize these legacy technologies in a timely manner, leaving them vulnerable to exploitation.

### Increasing Connectivity of Manufacturing Systems:

- The rise of IIoT and the increasing adoption of cloud-based platforms have dramatically expanded the connectivity of manufacturing systems. While these innovations offer significant benefits in terms of efficiency, automation, and data analysis, they also introduce a broader attack surface for cybercriminals to exploit. Manufacturing environments that were once isolated from external networks are now interconnected, creating new entry points for malicious actors.
- According to the Cybersecurity and Infrastructure Security Agency (CISA), there are over 1,200 known vulnerabilities and security issues associated with OT systems from more than 300 original equipment manufacturers (OEMs) and system providers. These vulnerabilities are often unpatched or poorly managed, increasing the likelihood of successful cyberattacks. The increased reliance on cloud platforms and remote access further complicates matters, as these systems are vulnerable to external breaches that may not be detected until damage has already occurred.

### Potential for Physical Damage and Disruption:

- Cyberattacks on manufacturing operations carry significant risks that go beyond data theft or financial loss. These attacks can result in direct physical damage to critical infrastructure, production lines, and even employee safety. A successful cyberattack can disrupt entire manufacturing processes, leading to downtime, loss of production, or the destruction of expensive equipment. In some cases, such attacks can trigger safety incidents, including machine malfunctions or accidents that endanger workers.
- This combination of physical and operational risks makes cybersecurity a critical concern for manufacturers, as a breach could potentially have life-threatening consequences. For instance, attacks on ICS can cause machinery to operate in unintended ways, resulting in physical damage to products or equipment or even posing a risk to the health and safety of employees working in the affected environment.

![Image description: News clipping about TSMC confirming a data breach after a LockBit cyberattack on a third-party supplier.](Image description: News clipping about TSMC confirming a data breach after a LockBit cyberattack on a third-party supplier.)

![Image description: News clipping about a ransomware attack on a US Navy shipbuilder leaking information of nearly 17,000 people.](Image description: News clipping about a ransomware attack on a US Navy shipbuilder leaking information of nearly 17,000 people.)

### Lack of Visibility and Control:

- Despite increasing awareness of cybersecurity threats, many manufacturers have yet to develop the necessary capabilities to secure their critical operational systems. While a large number of manufacturers have established procedures for detecting cyber events in their IT systems, far fewer have extended this monitoring to their OT environments, where the majority of critical manufacturing operations take place. Without proper visibility into their OT systems, manufacturers are unable to quickly identify and respond to threats, leaving them vulnerable to cyberattacks.
- Alarmingly, data suggests that 73% of OT devices are unmanaged, meaning they are not regularly monitored or updated by IT departments. This lack of visibility significantly increases the risk of undetected cyber incidents, as compromised devices could remain unnoticed until the damage is already done. In many cases, IT departments may not even be aware that a device is malfunctioning or has been compromised until the issue escalates to a point where it disrupts production or causes safety issues.

### Cultural Mindset Gap:

- A major challenge in improving cybersecurity within the manufacturing sector is the cultural mindset gap that exists between traditional office-based enterprise environments and the industrial settings in which manufacturing occurs. Historically, the manufacturing sector has placed a greater emphasis on physical safety—such as ensuring that machines operate correctly and that workers are not exposed to hazardous conditions—while cybersecurity has often been seen as a secondary concern. This disparity can create resistance to implementing necessary cybersecurity measures, as the urgency of protecting digital assets may not be immediately apparent to those focused primarily on physical operations.
- Additionally, the broader manufacturing sector’s risk management approach tends to prioritize short-term production goals over long-term cybersecurity investments, making it difficult to foster a culture of cybersecurity awareness. This cultural divide is reflected in risk assessments, with the manufacturing sector’s cybersecurity risk score being 11.7% lower than the global average across all industries, indicating a systemic underestimation of digital risks and a lack of preparedness to address them.

With more than 250 cybersecurity experts across the globe, the Trustwave SpiderLabs team puts its resources to task researching the top threats in today’s landscape. We are uniquely positioned to do so, as we perform over 200,000 hours of penetration tests and uncover tens of thousands of vulnerabilities annually. We also have a dedicated email security team analyzing millions of phishing URLs validated daily, including 10k per day that are uniquely identified by Trustwave SpiderLabs. Our diverse coverage of infosec disciplines, including Advanced Continuous Threat Hunting, Digital Forensics and Incident Response, Malware Reversal, and Database Security, give us insight into identifying how these breaches occur, as well as mitigations and controls that your organization can put in place to prevent these compromises.

This report examines the myriad of threats facing the manufacturing industry. In addition to supplemental reports focused on IT/OT convergence and how threat actors are attacking manufacturing, Trustwave SpiderLabs will offer recommendations to help manufacturers mitigate risks and keep their operations undisrupted.

## Notable and Prominent Trends in Manufacturing

### Convergence of IT and OT

#### The Threat

The convergence of IT and OT in manufacturing, while offering significant benefits like increased efficiency and automation, dramatically expands the attack surface and introduces complex cybersecurity risks.

Historically separated due to differing priorities (IT focusing on data and security, OT on physical processes and safety), the integration driven by Industry 4.0 and IoT exposes OT systems to a wider range of cyber threats.

OT systems, often legacy and lacking robust security measures, become vulnerable entry points for attackers. Breaches can lead to production downtime, safety incidents, reputational damage, and even pose risks to human life. The challenge lies in balancing the operational advantages of convergence with the critical need to secure these newly interconnected environments.

A key issue is the frequent prioritization of production uptime over cybersecurity concerns within OT environments, leading to vulnerabilities being overlooked until a disruptive incident occurs. The financial impact is substantial, with cybercrime costing manufacturers billions annually.

#### What Trustwave Is Seeing

At Trustwave, our experts help manufacturers tackle IT and OT convergence issues daily. They frequently encounter the following challenges:

- The inherent conflict between production uptime and cybersecurity: OT environments prioritize continuous operation, often at the expense of robust security measures. This conflict creates a vulnerability, as cybersecurity concerns are frequently addressed only after a production or safety incident occurs. This “if it ain’t broke, don’t fix it” mentality leaves systems vulnerable.
- Skills gap in OT cybersecurity: A significant shortage exists in professionals with the specialized knowledge to secure OT environments. This shortage is compounded by the cultural and priority differences between IT and OT teams, making it hard to find individuals who truly understand both worlds.
- Limitations of traditional endpoint security in OT: Many OT devices lack the processing power, memory, and storage required for traditional endpoint security software. This limitation necessitates alternative security approaches, such as passive network monitoring, which becomes a crucial line of defense.
- Challenge of asset inventory in OT environments: There is difficulty in maintaining a comprehensive inventory of OT assets. This lack of visibility makes it harder to identify vulnerabilities, manage patches, and effectively secure the environment. Often, even OT engineers only have deep knowledge of their specific production line, creating information silos.
- Increasing attack surface: While convergence offers benefits, it dramatically expands the attack surface. Previously isolated OT systems are now exposed to a wider range of cyber threats through their connection to IT networks. This interconnectivity creates new pathways for attackers to exploit.
- Critical need for cross-functional collaboration: It’s vital to bridge the gap between IT and OT teams. Their differing priorities and risk perceptions can hinder effective security. Regular communication, joint training, and cross-functional exercises are essential for building a unified security approach.

#### Mitigations to Reduce Risk

- **Comprehensive Asset Inventory:** Developing and maintaining a detailed inventory of all OT assets, including their function and dependencies, is essential. This is crucial for understanding the attack surface and prioritizing security efforts.
- **Network Segmentation and Micro-segmentation:** Implementing robust network segmentation to isolate IT and OT networks and further micro-segmentation within OT to limit the impact of breaches.
- **Vulnerability Management and Patching:** Establishing a structured vulnerability management program, considering the unique constraints of OT environments, including limited downtime and the need for careful testing before patching. Prioritize patching based on risk and implement compensating controls where patching is infeasible.
- **Strong Authentication and Access Control:** Enforcing strong authentication and access control mechanisms, especially for legacy systems that may have inherent vulnerabilities. This work includes addressing weak default credentials and implementing multi-factor authentication where possible.
- **Security Monitoring and Incident Response:** Implementing robust security monitoring of OT networks, focusing on detecting anomalies and malicious activity. Developing and regularly testing OT-specific incident response and recovery plans, considering the critical nature of production environments. Passive monitoring is highlighted as a key technique due to the limitations of endpoint security in OT.
- **Cross-Functional Teams:** Building cross-functional IT/OT teams to foster communication, collaboration, and shared understanding of security risks and responsibilities.

### Methods Used to Target Manufacturing

#### The Threat

The most recent cyberattacks waged against our clients in the manufacturing industry highlight the increasing frequency of web shell deployments, the exploitation of system vulnerabilities, and the rise of social engineering tactics—especially phishing—used by cybercriminals to gain unauthorized access.

As manufacturers continue to digitize and integrate more connected technologies, the risk of sophisticated cyberattacks becomes ever more pronounced. The tactics employed by attackers are evolving, with many choosing to exploit weak spots in existing infrastructure, human vulnerabilities, or the digital supply chain.

![Image description: News clipping about a ransomware attack disrupting Bassett Furniture manufacturing facilities.](Image description: News clipping about a ransomware attack disrupting Bassett Furniture manufacturing facilities.)

#### What Trustwave Is Seeing

We go into different tactics and techniques in the accompanying report, but one to highlight is vulnerability exploitation.

Manufacturing organizations had 4,370 unique vulnerabilities (out of a total of 24,920) publicly exposed on the Internet. 3,843 of these vulnerabilities are critical vulnerabilities, and 3,532 were listed in the Cybersecurity and Infrastructure Security Agency (CISA) Known Exploited Vulnerability (KEV) list, as seen in Table 1.

| CVE ID      | Description