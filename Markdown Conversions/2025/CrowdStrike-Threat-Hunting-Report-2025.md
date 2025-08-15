# 2025 THREAT HUNTING REPORT

## Table of Contents
- [Introduction](#introduction)
- [Naming Conventions](#naming-conventions)
- [Front-Line Snapshot](#front-line-snapshot)
- [Sector Targeting](#sector-targeting)
- [Sector Spotlights](#sector-spotlights)
- [MITRE ATT&CK Observations](#mitre-attck-observations)
- [Intrusion Trends by Adversary](#intrusion-trends-by-adversary)
- [Observations from the Front Lines](#observations-from-the-front-lines)
  - [Countering the Adversary: Generative Artificial Intelligence](#countering-the-adversary-generative-artificial-intelligence)
  - [Hunting Cross-Domain Adversaries](#hunting-cross-domain-adversaries)
  - [Case Study: Disrupting BLOCKADE SPIDER](#case-study-disrupting-blockade-spider)
  - [Case Study: Hunting OPERATOR PANDA](#case-study-hunting-operator-panda)
  - [Identity Hunting](#identity-hunting)
  - [Adversary Spotlight: SCATTERED SPIDER](#adversary-spotlight-scattered-spider)
  - [Cloud Hunting](#cloud-hunting)
  - [Case Study: Hunting GENESIS PANDA Across the Cloud Control Plane](#case-study-hunting-genesis-panda-across-the-cloud-control-plane)
  - [Case Study: MURKY PANDA’s Abuse of Trusted Relationships](#case-study-murky-pandas-abuse-of-trusted-relationships)
  - [Endpoint Hunting](#endpoint-hunting)
  - [Case Study: Hunting GLACIAL PANDA Living off the Land](#case-study-hunting-glacial-panda-living-off-the-land)
  - [Vulnerability Hunting](#vulnerability-hunting)
  - [Case Study: Hunting GRACEFUL SPIDER’s Zero-Day](#case-study-hunting-graceful-spiders-zero-day)
- [Conclusion](#conclusion)
- [Recommendations](#recommendations)
- [CrowdStrike Falcon Platform](#crowdstrike-falcon-platform)
- [CrowdStrike Products](#crowdstrike-products)
- [CrowdStrike Services](#crowdstrike-services)
- [About CrowdStrike](#about-crowdstrike)

---

## Introduction

A new era of cyber threats has emerged with the rise of the “enterprising adversary,” as highlighted in the CrowdStrike 2025 Global Threat Report. This new breed of threat actor distinguishes itself through sophisticated and scalable tactics designed to execute attacks with calculated, business-like efficiency. These adversaries operate with strategic precision to maximize impact and quickly achieve their goals.

Innovation is a critical cornerstone to outmaneuver and disrupt the enterprising adversary. Novel technologies and threat hunting are required to anticipate the adversary's next moves, understand their evolving methodologies, and adapt defenses to stay ahead.

Today's enterprising adversary is adept at bypassing traditional cybersecurity defenses. They understand the limitations of conventional safeguards and seek to exploit security weaknesses and vulnerabilities that established systems and processes often overlook. This includes exploiting human factors through sophisticated social engineering techniques — now often enhanced by AI — and moving to unmanaged devices, which are often significant blind spots in an organization's security posture. By targeting devices outside the direct purview of IT departments, they can establish footholds, exfiltrate data, or launch further attacks without immediate detection.

The CrowdStrike Counter Adversary Operations team brings together industry-leading threat intelligence and best-in-class managed threat hunting with the AI-powered CrowdStrike Falcon® platform to detect, disrupt, and stop enterprising adversaries. Counter Adversary Operations comprises two closely integrated teams. The CrowdStrike Intelligence team provides actionable reporting that identifies new adversaries, monitors their activities, and captures emerging cyber threat developments in real time. The CrowdStrike OverWatch team uses this intelligence to conduct proactive threat hunting across customer telemetry to detect and address malicious activity. Together, these teams protect thousands of customers from the most sophisticated adversaries by providing the intelligence and threat hunting skills and resources that most organizations lack.

Enterprising adversaries are using generative AI (GenAI) to enhance their operations, underscoring the critical need for innovative defensive strategies. The integration of GenAI into insider threat operations by Democratic People’s Republic of Korea (DPRK)-nexus adversary FAMOUS CHOLLIMA rapidly made them the most GenAI-proficient adversary. FAMOUS CHOLLIMA IT workers use GenAI to create attractive résumés for companies, reportedly use real-time deepfake technology to mask their true identities in video interviews, and leverage AI code tools to assist in their job duties, all of which pose a substantial challenge to traditional security defenses.

Adversaries continually seek to stay undetected by moving to unmanaged networks and expanding their reach. Cross-domain threat hunting is critical, as adversaries increasingly operate across multiple domains — such as identity, endpoint, and cloud — in their efforts to evade detection. These cross-domain threats often generate fewer detections in a single domain or product, making the activity difficult to recognize as malicious. To stay ahead of sophisticated cross-domain adversaries such as BLOCKADE SPIDER and OPERATOR PANDA, CrowdStrike OverWatch hunters are expanding their hunting grounds with innovative next-gen security information and event management (SIEM) technology to capture adversaries’ every move.

Though adversaries that prioritize rapid execution have the most visible and immediate impact, those that emphasize stealth, prolonged presence, and the meticulous execution of a “long game” approach present an equally potent threat. These operations often include sustained access, covert data harvesting, and — in some cases — preparing a victim’s environment for future, more impactful operations. China-nexus adversaries such as GLACIAL PANDA have increasingly excelled at this approach. GLACIAL PANDA primarily targets the global telecommunications sector through patient and methodical infiltration, established persistence, and deep, quiet reconnaissance of target networks, systems, and data. The challenge in detecting these stealthy adversaries is amplified by their minimal digital footprint, allowing them to easily blend into legitimate network traffic. CrowdStrike OverWatch successfully disrupts them by conducting customized hunts that uncover trojanized software and malicious code and focusing on repeated attempts to access sensitive data sources.

> »IN THE FIRST HALF OF 2025, CROWDSTRIKE OVERWATCH IDENTIFIED A 136% INCREASE IN CLOUD INTRUSIONS COMPARED TO ALL OF 2024.

> »IN THE CROWDSTRIKE 2025 GLOBAL THREAT REPORT, CROWDSTRIKE REPORTED THAT VOICE PHISHING (VISHING) ATTACKS INCREASED BY 442% FROM THE FIRST TO THE SECOND HALF OF 2024, MARKING A SIGNIFICANT AND EFFECTIVE EVOLUTION IN eCRIME TACTICS. THIS TREND HAS NOT SLOWED DOWN IN THE FIRST HALF OF 2025, WHERE VISHING ATTACKS HAVE ALREADY SURPASSED THE TOTAL NUMBER SEEN IN 2024.

In the first half of 2025, CrowdStrike OverWatch identified a 136% increase in cloud intrusions compared to all of 2024, highlighting the fact that more threat actors are becoming versed in exploiting cloud environments. China-nexus adversaries in particular have quickly gained proficiency in cloud exploitation techniques; GENESIS PANDA and MURKY PANDA, for example, have become adept at navigating cloud environments. Over the past 12 months, CrowdStrike OverWatch observed a 40% increase in cloud intrusions attributed to China-nexus adversaries. CrowdStrike OverWatch keeps pace by developing innovative hunting techniques for cloud services, workloads, and control planes as well as leveraging advances in identity protection.

In the CrowdStrike 2025 Global Threat Report, CrowdStrike reported that voice phishing (vishing) attacks increased by 442% from the first to the second half of 2024, marking a significant and effective evolution in eCrime tactics. This trend has not slowed down in the first half of 2025, where vishing attacks have already surpassed the total number seen in 2024. These attacks are successful because they exploit human vulnerabilities and leverage compromised credentials and social engineering to bypass traditional security measures, gain initial access, and move laterally within organizations at speed. One of the earliest adopters of this tactic is SCATTERED SPIDER, an eCrime adversary well known for their sophisticated social engineering and credential theft techniques. In 2025, this adversary exploded back into the eCrime landscape, and though they showcased some new techniques, help desk attacks have remained a prominent tool in SCATTERED SPIDER’s arsenal.

Also noted in the CrowdStrike 2025 Global Threat Report, 52% of vulnerabilities observed by CrowdStrike in 2024 were related to initial access. Adversaries continue to exploit internet-exposed applications for initial access. When adversaries like GRACEFUL SPIDER develop zero-day