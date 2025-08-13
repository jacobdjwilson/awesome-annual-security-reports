# 2025 Threat Hunting Report

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
    - [Defining GenAI](#defining-genai)
    - [How Threat Actors Leverage GenAI to Augment Operations](#how-threat-actors-leverage-genai-to-augment-operations)
    - [FAMOUS CHOLLIMA Leads in GenAI-Supported Operations](#famous-chollima-leads-in-genai-supported-operations)
    - [Countering FAMOUS CHOLLIMA](#countering-famous-chollima)
    - [Threat Actors Targeting AI Tools](#threat-actors-targeting-ai-tools)
    - [Outlook](#outlook-genai)
    - [How CrowdStrike OverWatch Applies AI to Threat Hunting](#how-crowdstrike-overwatch-applies-ai-to-threat-hunting)
  - [Hunting Cross-Domain Adversaries](#hunting-cross-domain-adversaries)
    - [Hunting in a Shifting Ransomware Landscape](#hunting-in-a-shifting-ransomware-landscape)
    - [Case Study: Disrupting BLOCKADE SPIDER](#case-study-disrupting-blockade-spider)
    - [Case Study: Hunting OPERATOR PANDA](#case-study-hunting-operator-panda)
    - [Outlook](#outlook-cross-domain)
  - [Identity Hunting](#identity-hunting)
    - [Adversary Spotlight: SCATTERED SPIDER](#adversary-spotlight-scattered-spider)
    - [Countering SCATTERED SPIDER](#countering-scattered-spider)
    - [Outlook](#outlook-identity)
  - [Cloud Hunting](#cloud-hunting)
    - [Case Study: Hunting GENESIS PANDA Across the Cloud Control Plane](#case-study-hunting-genesis-panda-across-the-cloud-control-plane)
    - [Case Study: MURKY PANDA’s Abuse of Trusted Relationships](#case-study-murky-pandas-abuse-of-trusted-relationships)
    - [Outlook](#outlook-cloud)
  - [Endpoint Hunting](#endpoint-hunting)
    - [Case Study: Hunting GLACIAL PANDA Living off the Land](#case-study-hunting-glacial-panda-living-off-the-land)
    - [ShieldSlide: Credential Harvesting and Backdoor Access via Trojanized OpenSSH Binaries](#shieldslide-credential-harvesting-and-backdoor-access-via-trojanized-openssh-binaries)
  - [Vulnerability Hunting](#vulnerability-hunting)
    - [Case Study: Hunting GRACEFUL SPIDER’s Zero-Day](#case-study-hunting-graceful-spiders-zero-day)
    - [Patch Circumvention Enables Zero-Day Enterprise](#patch-circumvention-enables-zero-day-enterprise)
    - [Hunting for GRACEFUL SPIDER’s Zero-Day Campaign Artifacts](#hunting-for-graceful-spiders-zero-day-campaign-artifacts)
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

> »IN THE FIRST HALF OF 2025,
> CROWDSTRIKE OVERWATCH
> IDENTIFIED A 136% INCREASE
> IN CLOUD INTRUSIONS COMPARED
> TO ALL OF 2024.

In the first half of 2025, CrowdStrike OverWatch identified a 136% increase in cloud intrusions compared to all of 2024, highlighting the fact that more threat actors are becoming versed in exploiting cloud environments. China-nexus adversaries in particular have quickly gained proficiency in cloud exploitation techniques; GENESIS PANDA and MURKY PANDA, for example, have become adept at navigating cloud environments. Over the past 12 months, CrowdStrike OverWatch observed a 40% increase in cloud intrusions attributed to China-nexus adversaries. CrowdStrike OverWatch keeps pace by developing innovative hunting techniques for cloud services, workloads, and control planes as well as leveraging advances in identity protection.

> »IN THE CROWDSTRIKE 2025 GLOBAL
> THREAT REPORT, CROWDSTRIKE
> REPORTED THAT VOICE PHISHING
> (VISHING) ATTACKS INCREASED
> BY 442% FROM THE FIRST TO THE
> SECOND HALF OF 2024, MARKING
> A SIGNIFICANT AND EFFECTIVE
> EVOLUTION IN eCRIME TACTICS.
> THIS TREND HAS NOT SLOWED
> DOWN IN THE FIRST HALF OF 2025,
> WHERE VISHING ATTACKS HAVE
> ALREADY SURPASSED THE TOTAL
> NUMBER SEEN IN 2024.

In the CrowdStrike 2025 Global Threat Report, CrowdStrike reported that voice phishing (vishing) attacks increased by 442% from the first to the second half of 2024, marking a significant and effective evolution in eCrime tactics. This trend has not slowed down in the first half of 2025, where vishing attacks have already surpassed the total number seen in 2024. These attacks are successful because they exploit human vulnerabilities and leverage compromised credentials and social engineering to bypass traditional security measures, gain initial access, and move laterally within organizations at speed. One of the earliest adopters of this tactic is SCATTERED SPIDER, an eCrime adversary well known for their sophisticated social engineering and credential theft techniques. In 2025, this adversary exploded back into the eCrime landscape, and though they showcased some new techniques, help desk attacks have remained a prominent tool in SCATTERED SPIDER’s arsenal.

Also noted in the CrowdStrike 2025 Global Threat Report, 52% of vulnerabilities observed by CrowdStrike in 2024 were related to initial access. Adversaries continue to exploit internet-exposed applications for initial access. When adversaries like GRACEFUL SPIDER develop zero-day exploits, CrowdStrike OverWatch's ability to identify and hunt for post-exploitation malicious behaviors becomes a critical fail-safe, ensuring rapid and effective coverage against widespread exploitation.

The CrowdStrike 2025 Threat Hunting Report highlights key trends and shifts the CrowdStrike OverWatch team observed over the past 12 months and details how CrowdStrike Falcon® Adversary OverWatch™ leverages innovation and proactive, intelligence-informed threat hunting to track, detect, and disrupt the adversary. This year’s report presents trends the team identified from July 1, 2024, to June 30, 2025. In this time frame, CrowdStrike OverWatch observed the following:

- **81%** of interactive intrusions were malware-free.
- Interactive (hands-on-keyboard) intrusions increased **27%** year-over-year, highlighting that adversaries are innovating their operations to bypass legacy detection methods.
- eCrime activity represented **73%** of total interactive intrusions.
- Cloud intrusions increased **136%** in the first half of 2025 compared to all of 2024.
- CrowdStrike OverWatch observed a **40%** year-over-year increase in intrusions by suspected cloud-conscious China-nexus actors.
- In the first half of 2025, vishing attacks already surpassed the total number seen in 2024.
- The government sector was affected by a **71%** year-over-year increase in overall interactive intrusions and a **185%** year-over-year increase in targeted intrusion activity.
- FAMOUS CHOLLIMA insiders infiltrated over **320** companies in the last 12 months — a **220%** year-over-year increase — by leveraging GenAI at every stage of the hiring and employment process.
- SCATTERED SPIDER accelerated their operations — in one incident, the adversary moved from account takeover to ransomware deployment in just **24 hours**, **32%** faster than they were able to accomplish this in 2024.

This report showcases the Counter Adversary Operations team’s relentless pursuit to disrupt the adversary. In CrowdStrike customer environments, adversaries face a unified security solution that empowers every CrowdStrike threat hunter with extensive security telemetry — spanning endpoint, identity, cloud, and next-gen SIEM, along with integrated intelligence — to detect and disrupt threats quickly and effectively.

## Naming Conventions

![Image of CrowdStrike Adversary Naming Conventions table](images/naming_conventions.png)

## Front-Line Snapshot

The statistics provided in this report specifically focus on interactive intrusions — attacks where adversaries establish an active presence within a target network, often engaging in hands-on-keyboard activities to achieve their objectives. Unlike automated attacks, interactive intrusions involve human operators who interact with systems in real time, adapting their tactics as needed. They are typically more sophisticated and difficult to detect than automated attacks, and they require advanced threat hunting and incident response capabilities to identify and mitigate.

**ANATOMY OF AN INTERACTIVE INTRUSION**

- **MANUAL INTERVENTION**: ATTACKERS MANUALLY NAVIGATE THE NETWORK, LEVERAGING THEIR SKILLS AND KNOWLEDGE TO BYPASS SECURITY CONTROLS.
- **PERSISTENCE**: ATTACKERS ESTABLISH AND MAINTAIN LONG-TERM ACCESS TO THE NETWORK, OFTEN USING ADVANCED TECHNIQUES TO EVADE DETECTION.
- **LATERAL MOVEMENT**: AFTER GAINING INITIAL ACCESS, ATTACKERS MOVE LATERALLY ACROSS THE NETWORK TO IDENTIFY AND COMPROMISE ADDITIONAL SYSTEMS.
- **DATA EXFILTRATION**: THE PRIMARY GOAL IS OFTEN TO STEAL SENSITIVE DATA, INTELLECTUAL PROPERTY, OR CREDENTIALS.
- **CUSTOMIZATION**: ATTACKERS TAILOR THEIR TECHNIQUES TO THE SPECIFIC ENVIRONMENT AND DEFENSES OF THE TARGET ORGANIZATION.

![Image of Figure 1. Description of a typical interactive intrusion observed by CrowdStrike OverWatch](images/figure1.png)

Over the past 12 months, CrowdStrike OverWatch observed interactive intrusions continue to climb, increasing 27% year-over-year. The overall distribution of interactive intrusion activity by threat type saw a noted increase in eCrime: 73% of the total 2025 reporting period volume was associated with eCrime activity, highlighting the persistent and pervasive threat of adversaries seeking financial gain.

![Image of Figure 2. Interactive intrusion breakdown](images/figure2.png)

## Sector Targeting

The technology sector remained at the top of the list for the reporting period, making technology the most frequently targeted industry for the eighth consecutive year. This sector encompasses a broad range of organizations that develop computer software and hardware or provide IT services or technology. Due to its relationship to many other sectors, the technology sector is a high-value target for both nation-state and eCrime adversaries.

![Image of Figure 3. Targeted sectors by intrusion frequency](images/figure3.png)

The government and telecommunications sectors saw a significant increase in interactive intrusions during the reporting period, namely by nation-state adversaries. Russia-nexus activity accounted for most of the government targeting, while China-nexus activity accounted for most of the telecommunications targeting.

## Sector Spotlights

### Government

CrowdStrike observed a 71% increase in overall interactive intrusions and a 185% increase in nation-state activity within the government sector over the past 12 months. Though the government sector is consistently a high-value target for a variety of nation-state adversaries, this significant increase is attributed to activity conducted by Russia-nexus adversaries such as PRIMITIVE BEAR and VENOMOUS BEAR, who conduct suspected espionage operations against Ukraine government entities in direct support of the conflict in Ukraine.

> »185%↑
> CROWDSTRIKE OBSERVED A 71%
> INCREASE IN OVERALL INTERACTIVE
> INTRUSIONS AND A 185% INCREASE
> IN NATION-STATE ACTIVITY WITHIN
> THE GOVERNMENT SECTOR OVER THE
> PAST 12 MONTHS.

### Telecommunications

CrowdStrike observed a 53% increase in overall interactive intrusions and a 130% increase in nation-state activity within the telecommunications sector over the past 12 months. This activity has primarily focused on entities in countries across Asia and North America. It is directly related to a surge in China-nexus adversaries’ operations against the telecommunications industry, which have become the most significant and consistent targeted intrusion threat to this sector over the past year. The telecommunications sector is a high-value target for nation-state adversaries, providing access to subscriber and organizational data that supports their intelligence collection and counterintelligence efforts. Telecommunication network access can also enable intrusion vectors and traffic collection against downstream customer organizations that obtain connectivity from the provider.

### Manufacturing and Retail

CrowdStrike observed notable increases in eCrime interactive intrusions targeting the manufacturing (55%) and retail (41%) sectors over the past 12 months. CURLY SPIDER emerged as a prominent threat actor conducting intrusions against North America-based retail and manufacturing entities at an increased rate. CURLY SPIDER is an eCrime group that has conducted ransomware intrusions (which predominantly involve vishing) targeting North America- and Western Europe-based entities across various sectors. Manufacturing and retail entities remain high-value targets for eCrime intrusions because these entities’ operating nature incentivizes them to pay ransoms quickly. Manufacturers cannot afford production delays, and retailers risk losing customer data and sales, especially during busy shopping seasons. These industries typically have larger budgets and complex computer systems that can be outdated, which also makes them attractive targets.

## MITRE ATT&CK Observations

CrowdStrike OverWatch tracks interactive intrusion activity against the MITRE ATT&CK® Enterprise Matrix, a framework that categorizes and tracks adversary behavior.[^1]

![Image of Figure 4. MITRE ATT&CK heat map highlighting the top techniques CrowdStrike OverWatch observed adversaries employ in each tactic area, July 2024-June 2025](images/figure4.png)

[^1]: To learn more about the MITRE ATT&CK Enterprise Matrix, visit [https://attack.mitre.org/matrices/enterprise/](https://attack.mitre.org/matrices/enterprise/)

Though CrowdStrike OverWatch observed the most total activity within the Defense Evasion tactic, five of the top 10 most commonly used MITRE ATT&CK techniques in the past 12 months were Discovery techniques. This highlights that adversaries are both spending their time orienting themselves within a network and ensuring their activities are not detected by security measures whenever possible. eCrime access brokers rely on these techniques — including Account Discovery, System Network Configuration Discovery, and Remote System Discovery — to evaluate targets as part of the threat actors’ efforts to monetize operations.

Defense Evasion techniques such as Masquerading and Disable or Modify Tools — as well as Ingress Tool Transfer, a Command and Control technique — were also in the top 10 most leveraged techniques. These techniques allow adversaries to blend their activity into expected network activity while enabling follow-on activities in various other tactic areas, such as Privilege Escalation and Credential Access.

## Intrusion Trends by Adversary

CrowdStrike’s insight into adversaries is unmatched. With detailed information about more than 265 attributed eCrime, nation-state, and hacktivist adversaries — and more than 150 active clusters of malicious activity that have not yet met CrowdStrike’s standards for adversary graduation — CrowdStrike OverWatch threat hunters are well positioned to quickly and accurately disrupt the adversary. Figure 5 highlights the most prevalent adversary operations identified over the past 12 months.

![Image of Figure 5. Interactive adversary disruptions across the world, July 2024-June 2025](images/figure5.png)

## Observations from the Front Lines

### Countering the Adversary: Generative Artificial Intelligence

Enterprising threat actors have capitalized on the surge of recently developed GenAI models to conduct social engineering, technical operations, and information operations (IO). GenAI tools have likely contributed to increased speed, access to expertise, and scalability in threat actor operations. At the same time, organizations’ integration of AI into business operations has created a new attack surface for threat actors to target. Despite these observable advantages for attackers, AI-enhanced cyber operations face similar constraints to traditional cyber operations, including resource availability and authorities.

#### Defining GenAI

GenAI is a subset of AI designed to create new data based on existing data. It is powered primarily by advanced machine learning models such as large language models (LLMs), which use natural language processing to generate text, and diffusion models, which create images, audio, and video content.[^2]

[^2]: Generative AI in Cybersecurity || What Is the Difference Between a Diffusion Model and LLM in Simple Terms || Explained: Generative AI

#### How Threat Actors Leverage GenAI to Augment Operations

Throughout 2024 and 2025, threat actors have increasingly integrated GenAI across their operations, using it to enhance their methods rather than replace existing tactics, techniques, and procedures (TTPs).

Nation-state adversaries — such as those attributed to Iran and North Korea — are increasingly adopting GenAI technology to make their cyber operations faster, more efficient, and harder to detect. They are using publicly available models to aid their reconnaissance, vulnerability research, and phishing campaign content and payload development. Threat actors with fewer resources, including eCrime and hacktivist actors, have employed GenAI to automate tasks and improve their tools, including script generation, technical problem-solving, malware development, and