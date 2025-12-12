# Global Incident Response Report 2025

## Table of Contents
- [Executive Summary](#executive-summary)
- [1. Introduction](#1-introduction)
- [2. Emerging Threats and Trends](#2-emerging-threats-and-trends)
  - [Trend 1. Disrupting Business Operations: The Third Wave of Extortion Attacks](#trend-1-disrupting-business-operations-the-third-wave-of-extortion-attacks)
  - [Trend 2. Increasing Impact in Software Supply Chain and Cloud Attacks](#trend-2-increasing-impact-in-software-supply-chain-and-cloud-attacks)
  - [Trend 3. Speed: Attacks are Getting Faster, Giving Defenders Less Time to Respond](#trend-3-speed-attacks-are-getting-faster-giving-defenders-less-time-to-respond)
  - [Trend 4. The Rise of Insider Threats: North Korea’s Insider Threat Spree](#trend-4-the-rise-of-insider-threats-north-koreas-insider-threat-spree)
  - [Trend 5. The Emergence of AI-assisted Attacks](#trend-5-the-emergence-of-ai-assisted-attacks)
- [3. How Threat Actors Succeed: Common Effective Tactics, Techniques and Procedures](#3-how-threat-actors-succeed-common-effective-tactics-techniques-and-procedures)
  - [3.1. Intrusion: Growing Social Engineering, Both Widespread and Targeted](#31-intrusion-growing-social-engineering-both-widespread-and-targeted)
  - [3.2. Attack Technique Insights From Unit 42 Case Data](#32-attack-technique-insights-from-unit-42-case-data)
- [4. Recommendations for Defenders](#4-recommendations-for-defenders)
  - [4.1. Common Contributing Factors](#41-common-contributing-factors)
  - [4.2. Recommendations for Defenders](#42-recommendations-for-defenders)
- [5. Appendix: MITRE ATT&CK® Techniques by Tactic, Investigation Types and Other Case Data](#5-appendix-mitre-attack-techniques-by-tactic-investigation-types-and-other-case-data)
  - [5.1 Overview of Observed MITRE Techniques by Tactic](#51-overview-of-observed-mitre-techniques-by-tactic)
  - [5.2. Data by Region and Industry](#52-data-by-region-and-industry)
- [6. Data and Methodology](#6-data-and-methodology)
- [Contributors](#contributors)
- [About Palo Alto Networks](#about-palo-alto-networks)
- [About Unit 42](#about-unit-42)

---

# Global Incident Response Report 2025

## Executive Summary

We see five major emerging trends reshaping the threat landscape.

*   First, threat actors are augmenting traditional ransomware and extortion with attacks designed to intentionally disrupt operations. In 2024, 86% of incidents that Unit 42 responded to involved business disruption — spanning operational downtime, reputational damage or both.
*   Second, software supply chain and cloud attacks are growing in both frequency and sophistication. In the cloud, threat actors often embed within misconfigured environments to scan vast networks for valuable data. In one campaign, attackers scanned more than 230 million unique targets for sensitive information.
*   Third, the increasing speed of intrusions — amplified by automation and streamlined hacker toolkits — gives defenders minimal time to detect and respond. In nearly one in five cases, data exfiltration took place within the first hour of compromise.
*   Fourth, organizations face an elevated risk of insider threats, as nation-states like North Korea target organizations to steal information and fund national initiatives. Insider threat cases tied to North Korea tripled in 2024.
*   Fifth, early observations of AI-assisted attacks show how AI can amplify the scale and speed of intrusions.

Amid these trends, we’re also seeing a multi-pronged approach in attacks, as threat actors target multiple areas of the attack surface. In fact, 70% of the incidents Unit 42 responded to happened on three or more fronts, underscoring the need to protect endpoints, networks, cloud environments and the human factor in tandem. And on the human element — nearly half of the security incidents (44%) we investigated involved a web browser, including phishing attacks, malicious redirects and malware downloads.

Drawing from thousands of incident responses over years of experience, we’ve identified three core enablers that allow adversaries to succeed: complexity, gaps in visibility and excessive trust. Fragmented security architectures, unmanaged assets and overly permissive accounts all give attackers the space they need to succeed.

To confront these challenges, security leaders must accelerate their journey to Zero Trust, reducing implicit trust across the ecosystem. Equally crucial is securing applications and cloud environments from development to runtime, ensuring that misconfigurations and vulnerabilities are swiftly addressed. Finally, it’s essential to empower security operations to see more and respond faster — with consolidated visibility across on-premises, cloud and endpoint logs, as well as automation-driven threat detection and remediation.

## 1. Introduction

Over my two-decade career as an incident responder, I’ve witnessed countless shifts in the threat landscape and attacker tactics.

When ransomware first appeared, file encryption became the tactic of choice for cybercriminals. Locking up files, getting paid for an encryption key, and moving on. Backups got better, and double extortion became more popular. Cybercriminals leveraged harassment (and still do) to tell companies “pay, or we will leak sensitive data.” But even that is losing its luster.

Almost every month, I receive notice of a data breach. Occasionally, I open and read these letters; admittedly other times, they go directly into the trash. Like many people, I’ve invested in identity theft protection software and adhere to best practices in cyber hygiene. With the onslaught of these notifications, it’s hard not to imagine the everyday person thinking: My data has been leaked again, so what? This desensitized mindset is unsettling. And yet, despite this public apathy, a data breach can still cause substantial damage to a company.

The past year has marked yet another shift in attacker focus to intentional operational disruption. This new phase in financially motivated extortion prioritizes sabotage — where attackers are intentionally destroying systems, locking customers out of their environments, and forcing prolonged downtime — so threat actors can maintain their ability to have maximum impact with their attacks and command payment from organizations.

In 2024, Unit 42 responded to over 500 major cyberattacks. These incidents involved large organizations grappling with extortion, network intrusions, data theft, advanced persistent threats and more. The targets of these attacks spanned all major industry verticals and 38 countries.

We’ve responded to breaches occurring at unprecedented speed, causing severe operational disruption and cascading impacts — from downtime and service outages to costs reaching billions of dollars. In every case, the situation had escalated to the point where the security operations center (SOC) called for backup.

When Unit 42 is called, our Incident Response team works swiftly to contain threats, investigate incidents, and restore operations. After the crisis, we partner with clients to strengthen their security posture against future attacks.

The Unit 42 mission is clear: protecting the digital world from cyberthreats. Operating 24/7 across the globe, our team is united by the purpose of stopping threat actors, hunting evolving threats and helping organizations prepare for and recover from even the most sophisticated attacks.

This report is organized to guide you through our key findings and actionable insights:

*   Emerging Threats and Trends: A look at what’s coming, including the rise of disruption-driven extortion, AI-assisted attacks, cloud and software supply chain-based attacks, nation-state insider threats, and speed.
*   How Threat Actors Succeed: Analysis of the most common effective tactics, techniques and procedures, from initial access to impact.
*   Recommendations for Defenders: Practical guidance for executives, CISOs and security teams to fortify their defenses, build resilience and stay ahead of the threat.

As you read, consider not just what’s happening, but what’s next and how your organization can prepare to meet the challenges of an increasingly complex threat environment.

Sam Rubin
SVP of Consulting and Threat Intelligence
Unit 42

## 2. Emerging Threats and Trends

In 2025, organizations face a complex mix of threats from financially driven cybercriminals, well-resourced nation-states, insider schemes and ideologically motivated hacktivists. While extortion attacks remain dominant among criminal groups, sophisticated nation-state adversaries target critical infrastructure, supply chains and key industries. Insider risks intensify as contractors and employees with privileged access can bypass external defenses, and hacktivists exploit social media networks to coordinate large-scale disruptions.

Against this backdrop, Unit 42 has identified five key trends where we see the most significant and immediate impact on organizations: intentionally disruptive extortion attacks, software supply chain and cloud exploitation, the increasing speed of attacks, North Korean insider threats and AI-assisted threats.

### Trend 1. Disrupting Business Operations: The Third Wave of Extortion Attacks

As defenses improve, backups become more common and successful as cyber hygiene matures. Attackers have been forced to innovate their approaches to ensure they can command consistent — and higher — payments.

Extortion attacks evolved over the past decade: from encryption, to exfiltration and multi-extortion techniques, to intentional disruption. Though ransomware remains a headline threat, attackers have shifted from solely encrypting data to more disruptive tactics like harassing stakeholders and threatening critical operations resulting in long periods of downtime.

In 2024, 86% of incidents that Unit 42 responded to had some sort of impact-related loss. This includes:

*   Outright business disruption
*   Asset and fraud-related losses
*   Brand and market damage as a result of publicized attacks
*   Increased operating costs, legal and regulatory costs, and more

We can define the evolution of extortion attacks in terms of three waves.

#### Wave 1: In the Beginning, There Was Encryption

The rise of cryptocurrency enabled larger-scale crime with smaller-scale risk to the criminal. Threat actors quickly adopted ransomware as a profitable attack method, locking up critical files, holding them for ransom and demanding a cryptocurrency payment to unlock them. Cryptocurrency has since become a critical enabler of ransomware attacks:

*   Reducing the attacker’s risk of being identified
*   Lowering the barrier to entry for cybercriminals
*   Helping the attacker evade law enforcement and international sanctions

In those early ransomware cases, the playbook was simple. Get in, encrypt the files and get out. Unit 42 investigations from this period rarely uncovered signs of data exfiltration.

Attackers are now more sophisticated, often combining encryption with data theft and double extortion threats, but encryption itself is still a go-to tactic. In fact, Unit 42’s latest incident response data shows that encryption remains the most common tactic used in extortion cases, holding relatively steady over the past 4 years.

Over time, as organizations have improved their data backup practices, encryption as the sole extortion tactic has become less effective. Backups have helped more organizations recover faster — nearly half (49.5%) of impacted victims were able to restore from backup in 2024. As seen in Figure 1, this is about five times as many as in 2022, when only 11% of victims were able to restore from backup.

![Figure 1. The percentage of victims who successfully restored encrypted files from backup rose 360% between 2022-2024.](Image description: A bar chart showing the percentage of victims who successfully restored encrypted files from backup. The percentage increased significantly from 2022 to 2024.)

However, these defensive measures do little to counter the risk of attackers publishing or selling stolen data.

#### Wave 2: Upping the Ante With Data Exfiltration

As focusing solely on encryption became less effective, attackers pivoted to a new extortion tactic: data exfiltration and subsequent harassment. In addition to using exfiltrated data to pressure victims through blackmail and harassment, financially motivated actors gained additional revenue streams, such as auctioning data on dark-web marketplaces.

Attackers threatened to leak sensitive information publicly, often hosting leak sites touting their alleged victims. Some bombarded employees and customers with malicious messages.

However, while data theft remains a popular tactic, its effectiveness has started to decline for several reasons. Data breach fatigue has made dark web leaks less impactful in pressuring victims to pay.

According to the Identity Theft Resource Center’s 2023 Data Breach Report, 353 million victims had their data leaked in 2023 alone. Additionally, while attackers do keep their promises more often than not, organizations are increasingly concerned about the times when they don’t.

In fact, in fewer than two thirds of cases with data theft in 2024 did attackers provide any proof of data deletion (only 58%). In some cases, Unit 42 became aware that despite providing such alleged “proof,” the threat actor had retained at least some of the data. While two thirds of the time is still most of the time, that’s far from the level of certainty most would expect when paying an (often exorbitant) fee for something.

Public leak site data supports this trend. After a 50% increase in leak site victims from 2022-2023, the number rose by only 2% in 2024. This may indicate that threat actors are finding leak site extortion less effective in compelling payments.

Extortion tactics rely on instilling fear and keeping the victim’s full attention. To achieve this, threat actors will continue to evolve their methods to remain at the forefront of disruption.

This doesn’t mean that attackers are abandoning exfiltration. As seen in Table 1, threat actors continue to steal data more than half the time, and their use of harassment is steadily rising. However, threat actors are piling on additional tactics to ensure they get their payouts.

| Extortion Tactic | 2021 | 2022 | 2023 | 2024 |
| :--------------- | :--- | :--- | :--- | :--- |
| Encryption       | 96%  | 90%  | 89%  | 92%  |
| Data Theft       | 53%  | 59%  | 53%  | 60%  |
| Harassment       | 5%   | 9%   | 8%   | 13%  |

Table 1. Prevalence of extortion tactics in extortion-related cases.

Deliberate disruption is the next phase in the evolution of financially motivated attacks as threat actors continue to turn up the volume to get their victims’ attention.

#### Wave 3: Intentional Operational Disruption

Attackers are increasing the pressure by focusing on a third tactic: intentional disruption. In 2024, 86% of incidents that Unit 42 responded to involved some sort of loss that disrupted the business either operationally, reputationally or otherwise.

Unit 42 observed attackers combining encryption techniques with data theft and then going even further with other tactics to visibly disrupt organizations. They damaged victims’ brand reputation or harassed their customers and partners. Attackers also deleted virtual machines and destroyed data (section 5.1 offers a full breakdown of MITRE techniques attackers used for this type of impact).

We have seen attackers disrupt victims who have deep partner networks that they rely on to conduct business. When an organization has to lock down parts of its network to contain the threat actor and remediate the attack before resuming operations, their partners are forced to disconnect. Once back online, the recertification process creates further disruption as partners reconnect to the network.

Sophisticated attackers have targeted enterprises leveraging these tactics — including in healthcare, hospitality, manufacturing and critical infrastructure — with the goal of causing widespread disruption not only to the business but their partners and customers as well.

As businesses grapple with extended downtime, strain on partner and customer relationships and bottom-line impacts, threat actors are taking advantage and demanding increased payments. Businesses looking to get their systems back online and minimize the financial impact (which can stretch to the millions and sometimes even billions) are being extorted for higher payments. The median initial extortion demand increased nearly 80% to $1.25 million in 2024 from $695,000 in 2023.

We also examined demands in terms of how much a threat actor perceives an organization can pay. (We based this on what the threat actor would find by searching for public sources of information about an organization.) The median initial demand in 2024 is 2% of the victim organization’s perceived annual revenue. Half of the initial demands fell between half a percent (0.5%) and 5% of the victim’s perceived annual revenue. On the high end, we have seen attackers attempt to extort amounts that are more than a victim organization’s perceived annual revenue.

However, whereas demands have increased, Unit 42 continues to find success when negotiating the ultimate payment (for clients who pay). As a result, the median ransom payment has risen only $30,000 to $267,500 in 2024. When organizations pay, the median amount is less than 1% of their perceived revenue (0.6%). The median percent reduction negotiated by Unit 42 is therefore more than a 50% decrease from the initial demand.

### Countermeasures: Remaining Resilient in the Face of Increasing Disruption

An important factor to consider when facing disruption-minded threat actors is operational resilience: Can you continue to function if critical systems go down or sensitive data is locked out of reach? Which business operations are essential to maintain? What are your disaster recovery and backup strategies? Are critical partners prepared to shift to new systems in the face of an attack?

The best way to find out is through regular testing and incident simulations, which validate your technical controls, train your response teams, and gauge your capacity to maintain essential services. By focusing on resilience, you not only mitigate the immediate financial impact of an attack, but also protect your long-term reputation and stakeholder trust — key assets in an increasingly volatile cyber landscape.

Extortion attacks and all that comes with them — encryption, data theft, harassment and intentional disruption — are no passing trend. Cybersecurity strategies must continuously evolve to counter the shifting technical tactics of attackers — while also recognizing that threat actors will continuously adapt to overcome stronger defenses.

### Trend 2. Increasing Impact in Software Supply Chain and Cloud Attacks

As organizations increasingly rely on cloud resources for both operations and the storage of valuable data, incidents related to the cloud or SaaS applications are some of the most impactful we see.

A little less than one third of cases (29%) in 2024 were cloud-related. This means that our investigation involved collecting logs and images from a cloud environment or touched on externally hosted assets such as SaaS applications.

Those cases don’t necessarily represent the situations in which threat actors are doing damage to cloud assets. We see this in about one in five cases in 2024 (21%), where threat actors adversely impacted cloud environments or assets.

#### Identity and Access Management as Contributing Factor

Issues with identity and access management (IAM) continue to be contributing factors in a significant number of cases. Cybercriminals such as Bling Libra (distributors of ShinyHunters ransomware) and Muddled Libra gain access to cloud environments by exploiting misconfigurations and finding exposed credentials.

While lack of multi-factor authentication (MFA) is still the most prevalent contributing factor of this type, we are seeing that issue less frequently. We saw it about one fourth of the time in 2024, compared to about a third of the time in 2023.

Other identity and access management issues are trending in the wrong direction. Excessive policy access, excessive permissions and password issues all became more prevalent in 2024, as shown in Figure 2.

![Figure 2. Trends in identity and access management issues from 2023 to 2024.](Image description: A bar chart showing the trends in identity and access management issues from 2023 to 2024. It highlights an increase in excessive policy access, excessive permissions, and password issues.)

IAM misconfigurations were the initial access vector in about 4% of cases, but this figure should be considered alongside the scale and impact of cloud attacks. Incidents of this type can affect an organization on a wide scale, and can also affect other organizations if threat actors are able to commandeer cloud resources.

One extortion campaign’s cloud operation took advantage of exposed environment variables, the use of long-lived credentials and the absence of least-privilege architecture. Once the threat actors succeeded in embedding attack infrastructure within multiple organizations’ cloud environments, they used this as a jumping off point to attack other organizations on a large scale. This included scanning more than 230 million unique targets for additional exposed API endpoints. As a result, the threat actor was able to target exposed files from at least 110,000 domains, collecting more than 90,000 unique leaked variables. Of these variables, 7,000 were associated with cloud services and 1,500 with social media accounts, often including account names in addition to information needed for authentication.

On multiple occasions, Unit 42 has observed threat actors using leaked API/access keys for initial access. This often gives threat actors leverage for further compromise. The use of valid cloud accounts (T1078.004) appears repeatedly in our case data in relation to the following tactics:

*   Initial Access (13% of cases where we observed this tactic)
*   Privilege Escalation (8%)
*   Persistence (7%)
*   Defense Evasion (7%)

#### Exfiltration and Cloud Storage

We responded to multiple cases of threat actors accessing, exfiltrating and then deleting organizations’ cloud storage. The speed of exfiltration (often less than a day), combined with data destruction can put extreme pressure on organizations to comply with extortion demands.

In some cases, attackers have also exfiltrated cloud snapshots, which are point-in-time copies of the contents of a cloud storage volume. This activity can expose critical data and can also be difficult to detect amid legitimate uses of snapshots for backup purposes.

The use of cloud resources for exfiltration is very common, even though cloud dataplane compromises represent a small percentage of overall cases (less than 5%). In 45% of cases where we observed exfiltration, attackers sent the data to cloud storage (T1567.002 - Exfiltration Over Web Service: Exfiltration to Cloud Storage), a technique that can also mask the attackers’ activity within legitimate organizational traffic.

#### Poor Visibility and Control of SaaS and Cloud-Based Systems

A common issue for SaaS and cloud-based systems is lack of visibility into or attention to issues on those systems.

In one investigation, the organization successfully mitigated an attack, only to be compromised again a short time later.

Our investigators discovered that threat actors had automated exploitation of a vulnerability within a service used within the organization’s cloud-based products. By combining this with using anti-forensic techniques to hide activity, the threat actor was able to regain access to the organization and its clients even after internal teams appeared to have successfully removed them.

#### Web Scraping and API Abuse

Though data scraping is not always malicious, its weaponization emerged as a significant threat in 2024. In one case, a threat actor executed billions of daily unauthorized scraping requests. This was an operation that would have cost more than $6 million annually in compute resources had we not identified the activity and aided with its mitigation.

Our incident response teams responded to attacks leveraging advanced techniques to bypass security controls, while cybercrime groups integrated scraping into their attack lifecycle to fuel fraud operations. In another case, attackers’ systematic, unauthorized scraping of documents forced an organization to completely re-architect their API infrastructure.

With privacy laws evolving to address automated collection, organizations face pressure to implement unauthorized scraping detection measures. Yet many struggle to differentiate between legitimate access and malicious scraping, often discovering data harvesting only after significant exposure has occurred.

#### Cloud-Enabled Attacks

Attackers frequently use compromised cloud resources to attempt to exploit or brute force other unrelated targets.

Another emerging trend is adversaries manipulating environment configurations (beyond a single host) to further enable or conceal their activity.

In cloud environments, threat actors can perform the following activities, for example:

*   Abuse admin-level access (or the equivalent user account permission misconfigurations, T1098 - Account Manipulation)
*   Hijack cloud resources (T1578 - Modify Cloud Compute Infrastructure, T1496.004 - Resource Hijacking: Cloud Service Hijacking)
*   Infect critical centrally managed configuration settings (T1484 - Domain or Tenant Policy Modification).

#### Software Supply Chain Attacks and Third-Party Software

In 2024, we responded to a number of incidents related to the software supply chain.

A critical vulnerability in the data compression library XZ Utils was identified before it could do large-scale damage. However, it remains a lesson in the potential impact of supply chain compromises. According to Red Hat at the time of the disclosure, the XZ tools and libraries contained “malicious code that appears to be intended to allow unauthorized access.” Since XZ Utils is included in a variety of major Linux distributions – which are used in turn by countless organizations around the world – successful deployment of this malicious code could have exposed thousands of organizations around the world. The result of a “multi-year effort,” the issue in XZ Utils underscores the need for all organizations to implement best practices around the open source software incorporated into their systems.

Several vulnerabilities in VPN appliances also raised concerns about the integrity of third-party software. We saw these vulnerabilities used as initial access vectors by both nation-state threat actors and cybercriminals.

Threat actors do not always need to use vulnerabilities to attack organizations through third-party software. In June 2024, the cloud-based data platform Snowflake warned that threat actors were targeting some of its customers’ accounts. The company said its research indicated that attackers were using previously compromised credentials (T1078 - Valid Accounts) and cited “ongoing industry-wide, identity-based attacks with the intent to obtain customer data.”

In a different matter worked by Unit 42, threat actors spent months brute-forcing a VPN (T1110 - Brute Force). Their eventual success allowed them to gain access to and maintain persistence in the organization’s environment.

The complexity of infrastructure and resulting lack of visibility can make it challenging to fully remediate attacks, particularly when incorporating third-party software.

### Countermeasures: Defending Against Software Supply Chain and Cloud Attacks

To reduce risk from supply chain and cloud-based attacks, focus on a few key tactics:

*   Limit credential abuse: Enforce strict IAM controls, granting only the privileges necessary for each role. Use short-lived credentials and multi-factor authentication wherever possible.
*   Centralize logging and auditing of production cloud resources: Forward logs off the originating host to prevent tampering, and aggregate them for correlation across services. Track anomalies such as unusual API calls or large data transfers.
*   Monitor usage patterns: Use log analytics to establish baselines for normal resource consumption and trigger alerts for deviations. Attackers frequently spike CPU or bandwidth usage during data exfiltration or cryptomining.
*   Patch promptly: Treat third-party libraries, container images and open-source components as part of your operational infrastructure. Develop a process to regularly review and quickly deploy security updates.
*   Secure APIs and supply chain integrations: Apply rate limiting to thwart excessive scraping or brute-force attempts, and use robust scanning tools to assess new dependencies before integrating them into production.

By applying these measures consistently, security teams can identify attacks early, limit their impact and maintain confidence that cloud resources and software pipelines remain under control.

### Trend 3. Speed: Attacks are Getting Faster, Giving Defenders Less Time to Respond

Unit 42 has observed a notable acceleration in cyberattacks as threat actors increasingly adopt automation, ransomware-as-a-service (RaaS) models and generative AI (GenAI) to streamline their campaigns. These tools allow attackers to rapidly identify vulnerabilities, craft convincing social engineering lures and ultimately execute attacks at scale, faster.

The speed of attacks forces global organizations to reassess their response capabilities and prioritize early detection. In many cases, just a few hours can determine whether an attacker succeeds in completing their mission, including data theft, encryption or operational disruption. As attackers continue to refine their methods and accelerate their timelines, the need for proactive security measures and rapid incident response is critical.

One of the ways Unit 42 gauges attack speed is by measuring time to exfiltration — how quickly an attacker exfiltrates stolen data following initial compromise.

In 2024, the median time to exfiltration in attacks that Unit 42 responded to was about two days. This time frame is notable because organizations often take several days to detect and remediate a compromise.

Examining the subset of cases where exfiltration happened most quickly, the speed of exfiltration is even more concerning.

*   In a quarter of cases, the time from compromise to exfiltration was less than five hours. This is three times faster than in 2021, when for the first quartile of cases, exfiltration took place in less than 15 hours.

For a large proportion of incidents, attackers are even faster.

*   In one in five cases (19%), the time from compromise to exfiltration was less than one hour.

In three recent cases that Unit 42 responded to, we observed attacker speed in action:

*   RansomHub (tracked by Unit 42 as Spoiled Scorpius) accessed a municipal government’s network through a VPN that lacked multi-factor authentication (MFA). Within seven hours of gaining a foothold, the threat actor exfiltrated 500 GB of data from the network.
*   A threat actor brute-forced a VPN account to gain access to a university. After identifying a system without XDR protection, they deployed ransomware and exfiltrated data within 18 hours.
*   Muddled Libra (also known as Scattered Spider) successfully social-engineered a service provider’s helpdesk to gain access to a privileged access manager (PAM) account. Using this access, they retrieved stored credentials and compromised a domain-privileged account — all within just 40 minutes. With domain access secured, the threat actor breached a password management vault and added a compromised account to the client’s cloud environment, escalating permissions to enable data exfiltration.

Defenders have less time than ever to identify, respond to and contain an attack. In some cases, they have less than an hour to respond.

However, we are making progress in reducing dwell time, which is measured as the number of days an attacker is present in a victim environment before an organization discovers or detects the attacker. Dwell time in 2024 decreased 46% to 7 days from 13 days in 2023. This continues a trend of decreasing dwell time that we have observed since 2021, when dwell time was 26.5 days.

### Countermeasures: Defending Against Faster Attacks

To improve your defense against ever faster attacks, consider the following tactics:

*   Measure detection and response times: Tracking and driving continuous improvement in mean time to detect (MTTD) and mean time to respond (MTTR) means your SOC is getting faster.
*   Leverage AI-driven analytics: Centralize data sources and identify anomalies in real time, surfacing critical alerts faster than manual methods.
*   Use automated playbooks: Predefine containment actions to isolate compromised endpoints or lock down user accounts within minutes.
*   Test continuously: Conduct regular tabletop and red-team exercises to ensure your SecOps team can pivot seamlessly from detection to response.
*   Prioritize high-risk assets: Focus swift-response capabilities on your most critical systems, where downtime or data loss would be most damaging.

By integrating real-time visibility, AI insights and automated workflows, you can outpace even the fastest-moving adversaries.

### Trend 4. The Rise of Insider Threats: North Korea’s Insider Threat Spree

Insider threats pose some of the most elusive risks for any organization, as they exploit the privileged access and trusted relationships that businesses depend on to operate. The ability to sidestep many external defenses makes these threats exceptionally challenging to detect.

North Korean nation-state threat groups have recently engaged in even more disruptive insider threat attacks by placing operatives in technical positions in international organizations. The campaign we track as Wagemole (also known as “IT Workers”) has transformed engineering roles themselves into another attack surface. This generates hundreds of millions of USD and other hard currencies for the North Korean regime in the process.

North Korean threat actors exploit traditional hiring processes with stolen or synthetic identities backed by detailed technical portfolios. These portfolios can include legitimate references obtained through identity manipulation and previous real work histories that pass basic verification.

About 5% of our incident response cases in 2024 related to insider threats, and the number of those tied to North Korea tripled compared to the previous year. While greater awareness of the threat may have led to more clients looking for it, it is significant that these threat actors continue to operate.

No sector is immune from this threat. In 2024, these actors expanded their reach to include financial services, media, retail, logistics, entertainment, telecommunications, IT services and government defense contractors. Large technology companies remained primary targets.

#### Contract Workforce

These campaigns typically target organizations utilizing contract-based technical roles. Staffing firms become unwitting facilitators for North Korean IT worker schemes due to:

*   Abbreviated verification processes to meet rapid staffing demands
*   Limited identity verification mechanisms
*   Poor visibility into subcontracted workforce providers
*   Pressure to quickly fill positions in a competitive market

While North Korean operatives have successfully obtained full-time positions, the contract workforce remains their most utilized vector of infiltration.

#### Evolving Tactics

The technical sophistication of these operatives has evolved. Where they once relied heavily on commercial remote management tools, they’ve recently shifted toward more subtle approaches.

Most concerning is the increasing use of hardware-based KVM-over-IP solutions — small devices that connect directly to target systems’ video and USB ports, providing remote control capabilities that can bypass most endpoint monitoring tools. These devices are attached to the computers that the target organization themselves provided to further the threat actors’ aims.

Visual Studio Code tunneling features, originally designed for legitimate remote development, now serve as covert channels for maintaining access.

The nature of these operations presents detection challenges because many operatives possess genuine technical skills. Their access appears legitimate because it is. They perform their assigned work while simultaneously serving their true objectives.

#### Threats Posed by Fake IT Workers

Once embedded within a company, in addition to illegally collecting salaries that help support the regime, these insiders engage in a range of malicious activities:

*   Data exfiltration: Systematic exfiltration of sensitive business data and internal documentation — using security policies, vulnerability reports and interviewing guides to better evade detection while targeting client data, source code and intellectual property.
*   Unauthorized tool deployment: Introducing remote management and other unauthorized tools to maintain access or prepare for further exploitation.
*   Altering source code: With access to a source code repository, the threat actor may insert backdoor code, potentially enabling unauthorized system access across broader organizations or tampering with financial transactions.
*   Extortion: In some cases, operatives leverage stolen data to demand ransoms, threatening to leak proprietary information. In some cases, they followed through on these threats.
*   Fake referrals: Threat actors may refer their associates to the organization, leading to the hiring of additional fake IT workers. In some cases, the referred hires are merely clones of the original referrer, using different fake identities to pose as multiple individuals.

### Countermeasures: Defending Against Fake IT Workers

The North Korean IT worker scheme has shifted from simply collecting revenue to a more evasive insider threat strategy, targeting a wide range of organizations globally. The regime’s strategic investment in these operations is a long-term commitment to this approach.

Defending against this threat requires a shift in how organizations approach both workforce management and security.

Addressing insider threats requires more than just technical controls. It demands a culture of security awareness and active monitoring of user activities, particularly among individuals with elevated privileges.

Measures such as implementing least privilege policies and acting on the results of thorough background checks can help minimize the potential for abuse. Additionally, organizations should pay close attention to behavioral indicators, such as unusual data transfers or last-minute system access by employees nearing their departure date. As part of this, it’s important to have the ability to put together indicators from various data sources. A behavior may seem innocuous on its own but, in combination with other signals, may indicate the need for an investigation.

Ultimately, trust must be balanced with verification. A single insider incident can undermine years of organizational progress, threaten intellectual property and inflict reputational harm. By fortifying internal processes, monitoring privileged access and emphasizing security at every level, businesses can significantly reduce the likelihood of a damaging insider event.

### Trend 5. The Emergence of AI-assisted Attacks

Although still in early stages, malicious use of GenAI is already transforming the cyberthreat landscape. Attackers use AI-driven methods to enable more convincing phishing campaigns, automate malware development and accelerate progression through the attack chain, making cyberattacks both harder to detect and faster to execute. While adversarial GenAI use is more evolutionary than revolutionary at this point, make no mistake: GenAI is already transforming offensive attack capabilities.

#### Enhancing Attack Capabilities with GenAI

GenAI tools, particularly LLMs, are being harnessed by both nation-state APTs and financially motivated cybercriminals to streamline and amplify attacks. These technologies automate complex tasks that previously required significant manual effort, accelerating the entire attack lifecycle.

For example, LLMs can craft highly convincing phishing emails that mimic legitimate corporate communications with unprecedented accuracy, increasing the success rate of phishing campaigns and making them harder to detect with