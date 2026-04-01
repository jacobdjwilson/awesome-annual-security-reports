# State of ICS/OT Security 2025

## Table of Contents
- [Foreword](#foreword)
- [Key Findings](#key-findings)
- [Survey Author](#survey-author)
- [Expert Corner](#expert-corner)
- [Introduction](#introduction)
- [2025 Trends: Increased Threats and Evolving Regulations](#2025-trends-increased-threats-and-evolving-regulations)
- [ICS/OT-Specific Threats, Intelligence, and Information Sharing](#icsot-specific-threats-intelligence-and-information-sharing)
- [ICS-Specific Security Regulations](#ics-specific-security-regulations)
- [Detecting Today’s Threats and Managing Vulnerabilities](#detecting-todays-threats-and-managing-vulnerabilities)
- [Cloud and Secure Remote Access](#cloud-and-secure-remote-access)
- [Planning for Tomorrow’s Cyber Risks](#planning-for-tomorrows-cyber-risks)
- [ICS/OT Threat Hunting and Red/Purple Exercises](#icsot-threat-hunting-and-redpurple-exercises)
- [By the Levels: Detection and Proactive Capabilities in the Purdue Model](#by-the-levels-detection-and-proactive-capabilities-in-the-purdue-model)
- [Cyber Resilience, Business Continuity, and Disaster Recovery Planning](#cyber-resilience-business-continuity-and-disaster-recovery-planning)
- [Technology Deployments: Past, Present, and Future](#technology-deployments-past-present-and-future)
- [Conclusions and Next Steps for Industry](#conclusions-and-next-steps-for-industry)
- [Appendix 1: Purdue Model Overview](#appendix-1-purdue-model-overview)
- [Appendix 2: ICS Career Progression](#appendix-2-ics-career-progression)

---

## Foreword
For nearly a decade, these surveys have tracked the industry’s progress toward cybersecurity maturity and identified the key drivers behind actions, both taken and not taken, within each sector. In collaboration with industry experts, the SANS team designs the survey to deliver actionable insights for readers. In recent years, Jason Christopher has elevated this report to a new level of excellence.

Over the years, the world has evolved: organizations have deepened their capabilities, adversaries have adapted, and expectations for corporate cybersecurity performance continue to rise. Given this reality, both the survey questions and the analysis of responses must mature to capture the nuances that matter most to leaders shaping and advancing their programs.

In this year’s survey, Jason Christopher delivers a true masterclass for the industry, capturing historical trends, identifying the current state of the field, and forecasting where it’s heading. His work provides the ICS/OT community with valuable context on where peers stand today, why, and where they go next.

> This report is essential reading for anyone in a leadership role across critical infrastructure environments.

I am excited to see how leaders across the industry put these insights into action, and I look forward to watching this survey continue to evolve as a vital tool in the defense of critical infrastructure worldwide!

**Tim Conway**
SANS Fellow

---

## Key Findings
- **Incidents remain high and disruptive.** More than one in five organizations (22%) reported a cybersecurity incident in the past year, with 40% causing operational disruption and nearly 20% taking over a month to remediate.
- **Detection is improving, but recovery lags.** Nearly half of incidents were detected within 24 hours and 60% contained within 48 hours, yet remediation often stretches into days or weeks (and can even take over a year).
- **Regulation drives maturity.** Sites under mandatory compliance had similar incident rates as peers but experienced ~50% fewer financial losses and safety impacts.
- **Threat intelligence pays dividends.** Organizations leveraging ICS-specific threat intelligence were more likely to adjust defensive priorities—improving monitoring, segmentation, and detection.
- **Remote access remains a top risk.** Unauthorized external access accounted for half of all incidents, yet only 13% of organizations have fully implemented advanced controls such as session recording or ICS/OT-aware access.
- **Preparedness is uneven.** Just 14% of respondents felt fully prepared for emerging threats, but those that included frontline technicians in exercises were nearly 1.7 times more likely to report strong readiness.
- **Investment momentum is clear.** Asset visibility, threat detection, and secure remote access dominate both 2025 deployments and 2026–2027 planned investments, showing where organizations see the greatest value.

---

## Survey Author
**Jason Christopher**
SANS Certified Instructor

Over the past 20 years, Jason D. Christopher has worked across multiple industries in unique roles ranging from engineering to incident response and national security. Most notably, Jason was the federal technical lead for the NERC CIPv5 while at the Federal Energy Regulatory Commission, where he was involved in several rulemakings and policy statements. Jason was also the program lead for the US Department of Energy Cybersecurity Capability Maturity Model (C2M2). He has served as a C-level executive, security researcher, and incident responder across his career. He previously held the role of director of Cyber Risk for Dragos, Inc. Today, Jason is the senior vice president of Cybersecurity and Digital Transformation for Research and Innovation at Energy Impact Partners (EIP), a $4 billion global investment firm custom-built to invest in the energy transition. Jason has been invited to speak before the US Congress on several occasions.

---

## Expert Corner
The 2025 SANS State of ICS/OT Security Survey rightfully highlights the increasing frequency of disruptive incidents to OT organizations despite these incidents going underreported in media and traditional sources. Practitioners in this space have long understood that when we look more we start to find more; threats have gone undetected for far too long and we’ve had more “near misses” in the community than we can afford in the future. Leveraging the SANS ICS Five Critical Controls is a great baseline for organizations to follow to enhance their security posture without overspending against the risk. Government leaders and policymakers, board of director members, and OT cybersecurity practitioners are chiefly aware that we have broadly underinvested in the portion of our businesses that generates revenue and where our local and national security interests reside. It is imperative to influence the mindsets outside of these circles and in the traditional enterprise IT security leaders to highlight the rapid and appropriate investments necessary to protect our communities.

**Robert M. Lee**
SANS Faculty Fellow

---

## Introduction
Since 2017, the SANS State of ICS/OT Security Survey has tracked the practices, challenges, and progress of organizations securing critical infrastructure worldwide. Over nearly a decade, these annual benchmarks have documented how the industry has matured—from ad-hoc protection measures to more structured programs shaped by regulation, threat intelligence, and incident response lessons learned.

This year’s survey, based on responses from 330 professionals across diverse industrial sectors, arrives at a pivotal moment. Threat activity against operational environments continues to rise, with ransomware, supply chain compromise, and nation-state alignment shaping the landscape. At the same time, regulatory mandates are expanding in scope and enforcement, requiring organizations to demonstrate not just compliance but resilience.

The report explores the state of ICS/OT security through three lenses: past trends, current practices, and future plans—offering practitioners, executives, and policymakers a clear view of progress, gaps, and the actions needed to build sustainable, resilient operations.

![Figure 1. Demographics]

---

## 2025 Trends: Increased Threats and Evolving Regulations
Historically, ICS/OT cybersecurity programs have responded to two major external factors: threats and regulations. As explored in previous years, the most mature organizations for industrial security leverage ICS-specific threat intelligence and standards. This year’s data supports those findings, as organizations that leverage both continue to demonstrate quicker detection, containment, and remediation during a cybersecurity incident.

### Industrial Cyber Incidents
Similar to previous years, 22% of respondents suffered a cybersecurity incident. Of those, a majority (50%) came from unauthorized external access and/or ransomware (38%).

![Figure 2. ICS/OT Security Incidents by Type]

These incidents have real-world impacts, with 40% of incidents causing a disruption in ICS/OT operations, 13% resulting in financial losses or data compromise, 8% posing a risk to physical safety or reliability, and 6% involving the theft of intellectual property. Interestingly, regulated sites had roughly the same amount of ICS/OT incidents but both financial losses and risks to physical safety impacts were ~50% less than their unregulated peers.

![Figure 3. ICS Cyber Incident Timeline]

As we teach across the SANS ICS curriculum, incident timelines can be broken into three distinct stages:
1. Compromise-to-detection
2. Detection-to-containment
3. Containment-to-remediation

![Figure 4. ICS Cyber Incident Timeline Distributions for 2025]

Two trends have maintained from previous years. First, industry continues to improve in detection times for ICS/OT incidents, with nearly 50% of incidents being detected within the first 24 hours. Second, we are similarly improving on containment, with over 65% of detection-to-containment gaps being addressed in the proceeding 24 hours. That means, on average, ICS/OT incidents are detected and contained within 48 hours.

That, however, is where the good news ends. Remediation, which includes the act of eradicating the threat and recovering operational integrity, still takes days to achieve, on average, with 22% taking two to seven days to recover. The risks here are real, with 19% of incidents in 2025 taking over a month to remediate (and a striking 3% taking over a year).

> Without an ICS/OT-specific incident response plan, most organizations take up to a week just to detect an incident. Annual testing can cut that timeline down to hours.

Preparation is still key to responding and recovering quickly during an industrial cyber incident. 57% of respondents have a dedicated ICS/OT incident response plan, a minor increase from previous years that represents further maturity across the industry. If an organization has both threat intelligence capabilities and is regulated, the coverage for ICS/OT-specific incident response plans jumps to 70%.

Most organizations (39%) test their incident response plan annually. While this decreased from previous years, that is because we saw a sharp increase in the number of organizations that are now testing their incident response plan quarterly (25%).

![Figure 5. ICS/OT Incident Response Testing]

---

## ICS/OT-Specific Threats, Intelligence, and Information Sharing
Starting with threat intelligence, 67% of respondents leverage threat intelligence in some capacity, with an additional 16% planning to use it over the next year. The majority (79%) of threat intelligence programs for ICS/OT environments are built on vendor-provided intelligence feeds, with government and public reporting sources coming in at a close second (77%) along with peers or industry information sharing and analysis centers (ISACs) (72%).

![Figure 6. Observed Value of ICS/OT Information Sharing]

Although threat intelligence and information sharing are separate activities, they both add to how industrial organizations categorize and monitor threats and, as mentioned, adapt their incident response capabilities. Based on these activities, respondents have seen an increase in ransomware targeting OT environments (64%), nation-state-aligned threats (57%) and supply chain compromises (52%) over the past year.

![Figure 7. Threat-Informed Defensive Priorities]

---

## ICS-Specific Security Regulations
Across the SANS ICS curriculum, we have noted the increase in ICS/OT cybersecurity-specific regulations over the past few years.[^1] It therefore came as no surprise that 58% of respondents reported having at least one facility subject to mandatory cybersecurity compliance requirements. Of that group, 26% reported having a possible violation from an audit or self-report.

![Figure 8. Compliance-Driven Investment Priorities]

[^1]: A more in-depth breakdown can be found in our 2023 SANS ICS Summit presentations: www.youtube.com/watch?v=3mhkEJ9QrL4

---

## Detecting Today’s Threats and Managing Vulnerabilities
Detection capabilities were a common theme across the 2025 data. They are the No. 1 prioritized response for threat intelligence (58% of respondents update threat detections based on intel) and compliance programs (72% have increased investment in logging, monitoring, and detection due to regulations).

> Only one in eight organizations report full ICS Kill Chain visibility—but those that achieve it almost always run a SOC with IT and OT sharing detection tools.

![Figure 9. ICS/OT Detection Capabilities]

Organizations that have achieved some level of visibility across the ICS Cyber Kill Chain largely do so through coordinated, but separate, IT and OT teams with shared log aggregation and correlation tools.

![Figure 10. Integration of IT and OT Visibility]

---

## Cloud and Secure Remote Access
As previously explored, 50% of incidents reported in the 2025 survey originated from unauthorized external access. Only 17% of respondents reported no cloud usage in their ICS/OT environments or IT networks, meaning 83% of respondents need to actively integrate cloud visibility to monitor for threats.

![Figure 11. Cloud Monitoring Across IT/OT Networks]
![Figure 12. Cloud Monitoring Capabilities]

Secure remote access continues to be a challenge for ICS/OT environments. Although industry has improved with multifactor authentication (MFA), there are still plenty of coverage gaps and capabilities missing in standard deployments.

![Figure 13. ICS/OT Secure Remote Access Capabilities]

> Half of 2025 incidents began with external access. Yet fewer than 15% of organizations have advanced remote access controls in place. This remains the weakest link.

![Figure 14. ICS/OT Secure Remote Access Blockers]

---

## Planning for Tomorrow’s Cyber Risks
Further examining industrial organizations and threat intelligence, it is apparent that ICS/OT cybersecurity professionals believe, by wide margins (as shown in Figure 15), that industrial systems are more likely to be targeted than in previous years.

![Figure 15. Threat-Focused ICS/OT Targets]
![Figure 16. Cyber Threat Scenarios Used for Planning and Preparedness]
![Figure 17. Perspective on Future Cyber Threats and Preparedness]

### Expert Corner
The data proves what ICS/OT cybersecurity defenders and engineering staff know about protecting our critical infrastructure: Engineering-informed cyber preparedness cannot be siloed. It must extend across the entire plant floor and engineering operations. Involving field technicians, engineers, and operators in ICS/OT tabletop exercises and industrial incident response planning nearly doubles the likelihood that an organization with ICS/OT is ready to face emerging threats that can directly impact safety. That’s no coincidence. Those closest to the control loops, HMIs, and PLCs understand better than anyone how cyber incidents ripple into safety, reliability, and process integrity. By embedding engineering staff and having them lead the way into ICS/OT cybersecurity exercises, ICS/OT organizations and critical infrastructure operations transform preparedness from a compliance checkbox into a true resilience capability. One that protects the operational environment as well as continuity and human safety. After all, in an organization that has ICS/OT, the ICS/OT is the business.

**Dean Parsons**
SANS Principal Instructor

![Figure 18. Stakeholders Involved in ICS/OT Cyber Preparedness Activities]

---

## ICS/OT Threat Hunting and Red/Purple Exercises
ICS/OT threat hunting is a proactive, hypothesis-driven search for stealthy adversary activity or unsafe changes in industrial environments. Analysts pivot through ICS-specific evidence, such as PLC/HMI logs, historian data, engineering-workstation activity, and protocol captures (e.g., Modbus, DNP3), all under strict safety and change control.

> Do you want to boost preparedness? Involve field technicians. Fully prepared organizations were seven times more likely to engage them in exercises than their peers.

![Figure 19. Preparedness Activities Performed or Planned]

---

## By the Levels: Detection and Proactive Capabilities in the Purdue Model
In the 2025 survey, we wanted to further explore how mature certain capabilities were across the Purdue Model.

![Figure 20. ICS/OT Capabilities by Coverage for Each Level of the Purdue Model]

---

## Cyber Resilience, Business Continuity, and Disaster Recovery Planning
Cyber resilience, like other aspects of risk management, must be incorporated into broader enterprise-level efforts to be successful.

![Figure 21. Cybersecurity Integration into BC/DR Planning]
![Figure 22. BC/DR Activities and ICS/OT Cybersecurity]

---

## Technology Deployments: Past, Present, and Future
Cyber preparedness for industrial environments requires a careful alignment across business processes, technology deployment, and workforce skill and culture.

![Figure 23. Technology Deployments Over the Previous 12 Months]

> Organizations that suffered an incident in 2025 invested heavily in response tools—after the fact. Don’t wait for a breach to justify the budget.

![Figure 24. Technology Investments Over the Next 12–24 Months]
![Figure 25. Technology Deployment Drivers]
![Figure 26. Technology Deployment Success and Effectiveness Metrics]
![Figure 27. Culture Divide Between IT, OT, and Leadership]
![Figure 28. ICS/OT Cybersecurity as Part of Day-to-Day Activities]

> Culture follows capability: Organizations with an ICS/OT incident response plan report stronger IT-OT alignment, better leadership engagement, and more resilient day-to-day practices.

---

## Conclusions and Next Steps for Industry
The 2025 State of ICS/OT Cybersecurity Survey paints a mixed picture. On one hand, detection timelines are shrinking, incident response planning is more common, and regulatory pressure is driving long-term maturity. On the other, remediation remains slow, advanced practices such as threat hunting and red/purple team exercises are limited, and remote access continues to expose organizations to disproportionate risk.

Looking ahead, the path forward for industry is actionable:
1. **Improve coverage of ICS/OT security.** Leveraging a risk-based and threat-informed approach to ICS/OT security controls has proven to improve incident response times and decrease reliability, safety, and financial impacts.
2. **Shift from detection to resilience.** Shorter time-to-containment is not enough. Organizations must invest in faster, safer recovery through backups, failover, and cyber-informed engineering.
3. **Broaden participation.** Preparedness cannot be limited to security teams—field technicians, engineers, and executives alike need to play active roles in threat-aware exercises.
4. **Leverage regulation as a springboard.** Compliance requirements should be treated not as ceilings but as baselines for stronger detection, response, and cultural integration.

---

## Appendix 1: Purdue Model Overview
The Purdue Model serves as the backbone for how ICS/OT environments are conceptualized and secured.

![Figure 29. Purdue Model Concept]

---

## Appendix 2: ICS Career Progression
In a world that is seeing increasingly sophisticated and impactful industrial cyber threats, these courses prepare OT security professionals to lead, defend, and protect industrial control systems at the foundational, essential, management, tactical and advanced skill sets.

- **ICS 310**: ICS Cybersecurity Foundations™
- **ICS 410**: ICS/SCADA Security Essentials™
- **ICS 418**: ICS Security Essentials for Leaders™
- **ICS 456**: Essentials for NERC Critical Infrastructure Protection™
- **ICS 515**: ICS Visibility, Detection, and Response™
- **ICS 612**: ICS Cybersecurity In-Depth™
- **ICS 613**: ICS/OT Penetration Testing & Assessments™

---

nce and sector of work.

 sans.org/ics

 ics-community.sans.org/signup

 @SANSICS

 linkedin.com/showcase/sans-ics

 youtube.com/c/SANSICSsecurity

State of ICS/OT Security 2025

26

ICS Security AnalystAcquires and manages resources, supports, and performs key industrial security protection while adhering to safety and engineering goalsICS Security ArchitectEnsures control system network security compliance and best practices for control networks ICS Security Incident ResponderExecutes speciﬁ c industrial incident response for incidents that threaten or impact control system networks and assets, while maintaining the safety and reliability of operationsICS Security LeaderBuilds and maintains business relationships with engineering staff  and C-suite stakeholders by communicating and managing cyber-to-physical risks while reducing security risk to engineering operations and simultaneously prioritizing safetyProcess Control EngineeringTests, programs, troubleshoots, and oversees changes of existing processes or implements new engineering processes through the deployment and operations of engineering systems and automation devicesICS/OT Security Pen TesterDiscovers system vulnerabilities and works with asset owners and operators to mitigate discoveries and prevent exploitation from adversariesSponsor

SANS would like to thank this survey’s sponsor:

State of ICS/OT Security 2025

27

About the SANS Research Program

The SANS Research Program is a key initiative by the SANS Institute and a
premier global provider of cybersecurity research and information. SANS
Research Program is designed to provide cybersecurity practitioners and
leaders with data-driven insights, thought leadership, and solutions that
help them better understand and respond to evolving security challenges.
All content is authored by SANS instructor experts from around the world
who apply their years of experience from hands-on practitioner work in the
field, advisory roles, and the classroom to provide education, guidance, and
actionable insights that help make the cyber world a safer place.

To learn about sponsorship opportunities for research, content, and
in-person or virtual events, email us at Sponsorships@sans.org or
go to www.sans.org/sponsorship.

State of ICS/OT Security 2025

28