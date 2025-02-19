```markdown
# 2024 Annual Report
By Insikt Group
®
January 28, 2025

The most significant attacks of 2024 demonstrated how SaaS application proliferation amplified the effect of stolen credentials. Lack of MFA and other misconfigurations contributed to threat actors accessing sensitive data. Criminal groups proliferated in the wake of law enforcement action. The number of ransomware attacks remained similar to last year, though the number of families and variants increased. Generative AI helped nation-states scale up influence operations. As voters in over 70 countries went to the polls, adversarial influence operations used generative AI tools to amplify inauthentic content.

CYBER
THREAT
ANALYSIS

Recorded Future® | www.recordedfuture.com
 CTA-2025-0128

## Table of Contents
- [Foreword](#foreword)
- [Executive Summary](#executive-summary)
- [Key Findings](#key-findings)
- [Growing Adoption of SaaS Leads to Identity Exploits](#growing-adoption-of-saas-leads-to-identity-exploits)
    - [SaaS Applications Provide New Opportunities to Exploit Stolen Credentials](#saas-applications-provide-new-opportunities-to-exploit-stolen-credentials)
    - [Infostealer Infections Increasingly Target Personal Devices and Obtain More Credentials per Infection, Increasing the Risk to SaaS Ecosystems](#infostealer-infections-increasingly-target-personal-devices-and-obtain-more-credentials-per-infection-increasing-the-risk-to-saas-ecosystems)
    - [Geographic Dispersion of Workforces Increases Insider Threat Risks](#geographic-dispersion-of-workforces-increases-insider-threat-risks)
    - [Looking Ahead: Taking Steps to Secure Cloud Identities](#looking-ahead-taking-steps-to-secure-cloud-identities)
- [Extortion Groups Proliferate Despite Law Enforcement Action](#extortion-groups-proliferate-despite-law-enforcement-action)
    - [Law Enforcement Actions Disrupt Two Major Affiliates](#law-enforcement-actions-disrupt-two-major-affiliates)
    - [Looking Ahead: Adapting to Variety in the Ransomware Ecosystem](#looking-ahead-adapting-to-variety-in-the-ransomware-ecosystem)
- [Industry Analysis Gives Insight into Threat Actor Priorities](#industry-analysis-gives-insight-into-threat-actor-priorities)
    - [Threat Actors Seek to Amplify Urgency to Increase Extortion Payouts](#threat-actors-seek-to-amplify-urgency-to-increase-extortion-payouts)
    - [Value of Stolen Data Driven by Future Monetization](#value-of-stolen-data-driven-by-future-monetization)
    - [Looking Ahead: Anticipating the Highest “Return on Infection”](#looking-ahead-anticipating-the-highest-return-on-infection)
- [Escalating Global Hostilities Drive Critical Infrastructure Targeting](#escalating-global-hostilities-drive-critical-infrastructure-targeting)
    - [Chinese State-Sponsored Pre-Positioning Demonstrates Capabilities to Disrupt US Critical Infrastructure](#chinese-state-sponsored-pre-positioning-demonstrates-capabilities-to-disrupt-us-critical-infrastructure)
    - [Salt Typhoon’s Massive Telecom Hack and US-China Relations](#salt-typhoons-massive-telecom-hack-and-us-china-relations)
    - [Russian-Linked Sabotage Efforts Indirectly Advance War Aims](#russian-linked-sabotage-efforts-indirectly-advance-war-aims)
    - [Looking Ahead: Geopolitical and Cyber Convergence](#looking-ahead-geopolitical-and-cyber-convergence)
- [Generative AI Accelerates Spread of Inauthentic Content in Historic Election Year](#generative-ai-accelerates-spread-of-inauthentic-content-in-historic-election-year)
    - [State-Sponsored Adversaries Continue Experimenting with Generative AI for Influence Operations](#state-sponsored-adversaries-continue-experimenting-with-generative-ai-for-influence-operations)
    - [State-Sponsored Threat Actors Are Likely Seeking to Expand Use of Large Language Models (LLMs), but Barriers to Automated Attacks Remain](#state-sponsored-threat-actors-are-likely-seeking-to-expand-use-of-large-language-models-llms-but-barriers-to-automated-attacks-remain)
    - [Looking Ahead: The Future of AI Operations](#looking-ahead-the-future-of-ai-operations)
- [Tactics and Techniques Emphasize Defense Evasion](#tactics-and-techniques-emphasize-defense-evasion)
    - [Remote Management Tools Enable Hiding in Plain Sight](#remote-management-tools-enable-hiding-in-plain-sight)
    - [MacOS and Linux Malware Continue to Diversify](#macos-and-linux-malware-continue-to-diversify)
    - [MacOS-Focused Infostealers and Trojans Increase in Number and Sophistication](#macos-focused-infostealers-and-trojans-increase-in-number-and-sophistication)
    - [Linux Systems Targeted Through Poisoned Utilities, Hypervisors, and Cross-Platform Functionality](#linux-systems-targeted-through-poisoned-utilities-hypervisors-and-cross-platform-functionality)
    - [TTPs Involving Defense Evasion Show Greatest Increase](#ttps-involving-defense-evasion-show-greatest-increase)
    - [Looking Ahead: Tracking Adversarial Actions Off the Disk](#looking-ahead-tracking-adversarial-actions-off-the-disk)
- [Reflections on 2023 Predictions](#reflections-on-2023-predictions)
    - [2023 Predictions](#2023-predictions)
    - [2024 Outcome](#2024-outcome)
- [Outlook: 2025 Predictions](#outlook-2025-predictions)

## Foreword
Our annual threat reports provide an in-depth look at threat actors’ key tactics, techniques, and procedures (TTPs) and motivations from the past year. These inform anticipated TTPs for the year ahead. You can use this information to better detect threats and manage cyber risk.

Learn from the adversary’s 2024 playbook to strengthen your security posture.

This report presents the industry’s most comprehensive intelligence analysis from 2024, a year in which enterprise attack surfaces continued to expand, cybercriminal activity carried on despite high-profile law enforcement actions, and state-sponsored threat actors targeted critical infrastructure and elections.

Read on for details related to key threat actors, their targets, and the TTPs they used so you can identify and address security control gaps in your systems. You’ll learn how:

- Threat actors exploited software-as-a-service (SaaS) setups and valid credentials, notably in the ALPHV and RansomHub ransomware attacks on Change Healthcare and the UNC5537 attack on Snowflake.
- Despite law enforcement disruptions of major ransomware-as-a-service (RaaS) groups like LockBit and ALPHV and the fact that ransomware activity remained consistent year over year, the number of new ransomware groups increased.
- As over 2 billion voters went to the polls worldwide, China, Russia, and Iran used AI-generated content in an attempt to mold public opinion as part of malign influence operations. 

Prevent future attacks with a roadmap for 2025 and beyond.

Review our predictions regarding memory-safe coding, cryptocurrency fraud, third-party risk management, and more. Use the information to craft a threat intelligence strategy that can help safeguard your data, brand reputation, and bottom line. Our predictions include: 

- Developers will use AI to accelerate the transition to safer code.
- Cryptocurrency fraud will lead to a market-destabilizing event.
- A major breach will very likely result from the implementation of GenAI into enterprise workflows, or the abuse of AI for effective impersonation. 
- More companies will report Chinese pre-positioning activity, demonstrating China’s capability to conduct disruptive operations across a broader range of critical industries.

On behalf of Recorded Future’s Insikt Group, I hope this report will help you stay one step ahead of the adversary and avoid disruption to your business in 2025.

Levi Gundert
Chief Security & Intelligence Officer

CYBER THREAT ANALYSIS
www.recordedfuture.com | Recorded Future®
 CTA-2025-0128

## Executive Summary
Two parallel trends shaped the cybersecurity landscape in 2024: the resilience of criminal networks in the face of increased law enforcement disruptions and the growing complexity of enterprise attack surfaces. The cybercriminal marketplace has demonstrated resilience, as criminals adapted to withstand persistent law enforcement takedowns through reorganization, while enterprise networks have become almost too complex as more essential business processes shift to third-party, cloud-based applications.

Multiple law enforcement disruption efforts targeted ransomware operations (such as LockBit), denial-of-service operators, and malware-as-a-service (MaaS) providers throughout 2024. While there was a temporary decrease in ransomware victims immediately after law enforcement seizures or action, overall volumes for reported attacks have not decreased significantly. This adaptability demonstrates how the service-based criminal ecosystem enables threat actors to pivot between providers quickly while maintaining operational continuity. Moreover, the fundamental market dynamics driving cybercrime remain strong, motivating criminals to adapt despite setbacks.

On the other hand, the average enterprise now employs 371 distinct software-as-a-service (SaaS) products, creating a larger attack surface that has become increasingly challenging to defend effectively. Credential compromise for SaaS products and environments have led to significant breaches, as evidenced by the incidents affecting Change Healthcare and Snowflake. Critical vulnerabilities in widely deployed enterprise products, such as Ivanti equipment and Confluence, have also resulted in widespread security breaches.

At the same time, state-sponsored threat actors and their hacktivist proxies (which were primarily linked to China and Russia) launched disruptive attacks on critical infrastructure networks such as water treatment facilities to advance their geopolitical objectives. In addition to cyberattacks, China, Russia, and Iran used generative AI to conduct information operations and spread inauthentic political content around the world. These threat actors also took advantage of heightened complexity — both in industrial technology and in the information ecosystem — to obscure evidence of government involvement in these activities.

In response to an entrenched cybercrime industry, an unwieldy number of third-party considerations, and increasingly emboldened state-sponsored threat actors, organizations must move beyond traditional perimeter-based defenses to adopt more robust, scalable, and automated security architectures. These security solutions need to match the complexity of enterprise operating environments and the proliferation of increasingly advanced threat actor toolsets. That said, based on major breaches like Snowflake in 2024, organizations must first prioritize straightforward and effective solutions — like multi-factor authentication (MFA) — over newly complex security tooling.

CYBER THREAT ANALYSIS
Recorded Future® | www.recordedfuture.com
 CTA-2025-0128

## Key Findings
- **The growing adoption of SaaS applications made identity exploits more effective.** The most significant attacks of 2024 demonstrated how SaaS application proliferation in corporate environments amplified the effect of credentials stolen via infostealer malware.
- **Criminal groups proliferated in the wake of law enforcement actions.** Law enforcement successfully disrupted major ransomware-as-a-service operators, including LockBit. However, distinct ransomware families and variants increased sharply in late 2024 as criminals used exposed source code and builders to launch independent operations.
- **Disruption and data made cybercrime pay.** Manufacturing and health care remained the most targeted industries by ransomware and extortion operators in 2024, demonstrating the continued payoff for cybercriminals to threaten real-world disruption. Meanwhile, the number of databases for sale on criminal forums increased by 20% over the last year, with telecommunications, healthcare, and education databases commanding the highest prices.
- **Increasing global hostilities led to critical infrastructure disruption.** State-sponsored threat actors and their hacktivist proxies weaponized critical infrastructure threats to advance geopolitical goals. China-linked threat actors were identified pre-positioning on critical networks, while Russia- and Iran-backed hacktivists targeted water treatment facilities for maximum visibility.
- **Nation-states took advantage of generative AI to level up influence operations.** As voters in over 70 countries went to the polls, influence operations from China, Russia, and Iran used generative AI tools to expand content production and reach. All three nations continue investing in GenAI research.
- **Tactics, techniques, and procedures emphasized defense evasion.** Tactics once limited to sophisticated, state-resourced threat actors are becoming increasingly common in criminal operations. These include using legitimate tools to evade detection and developing malware in Go and Rust coding languages.

CYBER THREAT ANALYSIS
www.recordedfuture.com | Recorded Future®
 CTA-2025-0128

## Growing Adoption of SaaS Leads to Identity Exploits
The increasing adoption of interconnected software-as-a-service (SaaS) applications in 2024 meant that compromised credentials were even more useful to cyber threat actors, who exploited gaps or misconfigurations in single sign-on (SSO) or multifactor authentication (MFA) policies to gain access to corporate ecosystems.

### SaaS Applications Provide New Opportunities to Exploit Stolen Credentials 
The average company uses approximately 371 software-as-a-service (SaaS) applications, which is up 39.4% from 2021 (266) and is expected to grow throughout 2025. Each of these applications typically comes with its own browser-based log-in portals and can be integrated into an enterprise single sign-on (SSO) solution. However, that integration is not always as seamless as intended if users access applications outside of the approved identity access management (IAM) environment. This rapidly growing identity attack surface almost certainly gives threat actors more opportunities to abuse stolen or exposed credentials, which are used in 77% of web application attacks. Criminals took advantage of this combination of increased SaaS reliance and exposed credentials to carry out two of the most notable attacks in 2024, namely the Change Healthcare and Snowflake breaches. 

The ALPHV and RansomHub ransomware attacks affecting Change Healthcare involved the use of valid credentials to access a Citrix application that enabled remote access to desktops before pivoting to other resources. The Citrix Gateway that served as the SSO interface for remote access to Change Healthcare’s network did not have multi-factor authentication enabled, allowing for the worst confluence of factors: a very common identity threat (credential abuse) being able to take advantage of a very common identity and access management measure (SSO). Once access was established, the threat actor moved laterally through the network, collected and exfiltrated patient data, and deployed the ransomware payload. Change Healthcare paid ALPHV an initial $22 million ransom, and there is evidence, but no confirmation, that it later paid a RansomHub affiliate an additional ransom following re-extortion.

The simultaneous breach of multiple Snowflake cloud storage accounts involved stolen credentials for hundreds of organizations. The financially motivated threat actor UNC5537 compromised data from multiple companies’ Snowflake instances using credentials stolen via infostealer infections. UNC5537 gained access to environments not protected by MFA, similar to Change Healthcare’s Citrix portal. Once they obtained access, UNC5537 used simple Structured Query Language (SQL) queries to conduct reconnaissance, identify data of interest, and exfiltrate it from the Snowflake environment. UNC5537 then sent individual extortion messages to affected organizations while selling the data on known underground and dark web forums. By carrying out these attacks simultaneously, UNC5537 created initial confusion around the source of the breach, with early reports suggesting that the Snowflake platform itself had been compromised.

### Infostealer Infections Increasingly Target Personal Devices and Obtain More Credentials per Infection, Increasing the Risk to SaaS Ecosystems
In both the Change and the Snowflake data breaches, the initial valid credentials were obtained through infostealer infections. Recorded Future observed that most infostealer infections affected personal or small-to-medium business-owned devices in 2024. Personal devices are not usually subject to the same monitoring, usage restrictions, or security resources as enterprise devices, which makes it more likely that an infostealer will not be interrupted. In addition, credentials can remain exposed long after the initial infostealer infection, as demonstrated by Mandiant’s finding that some of the credentials used in the Snowflake breach were stolen in 2020.

The number of credentials stolen per device has also steadily increased since 2021, likely due to the growing number of applications users routinely log in to, both in their corporate environments and personal devices. This increases the likelihood that at least one of those credentials provides access to a corporate resource. The growing number of log-ins across devices can be difficult for security teams to manage, especially if users are logging in outside the enterprise’s centralized identity management system. 

![Personal devices are targeted more often than enterprise devices, while the number of credentials stolen per device has increased over the last three years (Source: Recorded Future)]

### Geographic Dispersion of Workforces Increases Insider Threat Risks
The adoption of SaaS and virtualized cloud environments has been in part driven by the need to connect on-premise and remote working environments. However, remote access has also enabled threat actors to take advantage of not just stolen credentials but entire stolen identities to gain access to sensitive company resources. In December 2024, the Federal Bureau of Investigation (FBI) indicted fourteen North Korean nationals for allegedly using stolen identities to pose as remote workers to obtain jobs at United States (US) companies. One cybersecurity company that unknowingly hired one of these workers reported that its new hire used a “valid but stolen US-based identity”, allowing him to pass background checks, four video-based interviews, and other pre-hire vetting.

### Looking Ahead: Taking Steps to Secure Cloud Identities
An estimated 22% of jobs are expected to be fully remote by 2025, meaning identity management from hiring through termination is likely to remain a complex endeavor. As Insikt Group noted last year, hybrid workspaces are increasingly moving more companies to depend on third-party infrastructure and software to support business operations. Last year, Insikt Group observed the threat of mass vulnerability exploits — brought to prominence by the exploitation of the MOVEit file transfer vulnerability (CVE-2023-34362) — while this year featured threat actors taking a different approach to exploit organizational complexity. Multifactor authentication would have almost certainly helped prevent both the Change and Snowflake breaches, but consistent configuration across a complex and often cloud-based infrastructure is easier said than done.

In response to the growing threats to SaaS applications, companies are already increasingly investing in what they hope are more mature or less easily targeted identity management solutions. One study found a 400% increase in passkey adoption in 2024, with over 100 popular apps now offering passkey support. These investments appear to be paying off, as 83% of companies reported that their identity security investments have helped reduce identity-related risk. However, proper configuration and consistent maintenance are essential to ensuring these solutions work effectively, as criminals will continue to look for new ways to exploit gaps in protection.

## Extortion Groups Proliferate Despite Law Enforcement Action
While law enforcement actions in 2024 temporarily disrupted the operations of LockBit and major infostealers, phishing kits, and DDoS services, criminals adapted by reorganizing into smaller groups outside of major RaaS affiliates, demonstrating operational resilience.

### Law Enforcement Actions Disrupt Two Major Affiliates
The ransomware landscape saw two major shifts in 2024 due to the disruption of LockBit and the departure of ALPHV, two major ransomware-as-a-service (RaaS) groups. In February 2024, law enforcement agencies in the US, United Kingdom (UK), and several European countries announced the disruption of LockBit’s operation in a concerted operation dubbed “Cronos”, seizing several of the group’s network resources, arresting two affiliates, and freezing cryptocurrency accounts. Further operations continued in October 2024, when law enforcement revealed additional actions undertaken against LockBit’s operations. These actions included arresting five additional individuals linked to LockBit and seizing nine servers that were part of the group’s infrastructure. Meanwhile, ALPHV (also known as BlackCat) took its affiliate network offline in March 2024, shortly after collecting a $22 million payment from Change Healthcare. Researchers suspect the sudden shutdown was part of an exit scam to avoid paying affiliates amid increasing law enforcement attention.

The disruption of LockBit and ALPHV’s activities was significant. According to Recorded Future data, Lockbit accounted for 23% of all ransomware activity in 2023, making it one of the most active groups in the previous year. ALPHV also appeared among the top five most active ransomware groups last year.

Law enforcement actions did not only focus on RaaS in 2024. Other notable takedowns included “Operation Endgame”, which shut down infrastructure supporting at least four malware groups, including IcedID, Smokeloader, Pikabot, and Bumblebee. US law enforcement also issued indictments for members of the criminal group Scattered Spider and the hacktivist group Anonymous Sudan, the latter of which also sold access to its distributed denial-of-service (DDoS) tool called the Distributed Cloud Attack Tool (DCAT) in addition to conducting attacks directly.

Despite law enforcement actions on the ransomware and malware-as-a-service ecosystem, overall volumes for reported attacks have not decreased significantly. Ransomware groups adapted to the disruptions by reorganizing and rebranding. Recorded Future data shows that ransomware victims posted on LockBit’s extortion website decreased steadily over the last year, dropping from 205 posts in Q1 to just four posts in Q4. However, the LockBit malware strain continued to be used by various emerging groups, likely due to the ongoing use of the LockBit 3.0 ransomware builder, which was leaked in 2022. Examples of groups using LockBit malware include Dragon Force, a hacktivist threat actor turned ransomware group, and CosmicBeetle, a minor cybercriminal threat actor Recorded Future has tracked since 2020. 

![While the velocity of attacks decreased slightly in August 2024, between September and October 2024, attacks resumed the pace set over the last two years (Source: Recorded Future)]

Additionally, the number of new groups and extortion blogs has increased throughout 2024. In 2023, Insikt tracked 32 new ransomware groups for the entire year. Meanwhile, in the summer of 2024 (June to August), there were fourteen new blog sites and 62 new variants, with the most prevalent group (RansomHub) only representing 12% of total extortion posts. In the previous six months, by comparison, LockBit alone represented 35% of all extortion posts. This activity indicates a pivot from consolidated, high-profile ransomware-as-a-service models toward a more fragmented criminal ecosystem where any one group is less likely to attract law enforcement attention. The increased number of observed new ransomware variants is likely facilitated by leaked source code and builders becoming more widely used and shared among threat actors.

![The number of new ransomware families detected each month has significantly increased throughout H2 2024  (Source: Recorded Future)]

Ransomware persists because it remains a lucrative criminal endeavor, with cumulative ransom payments reaching $459.8 million through June 2024, setting 2024 on track to be the highest-grossing year yet for ransomware payments, according to Chainalysis. Chainalysis observed that in 2024, ransomware groups extorted a smaller number of significantly larger ransom payments against high-profile organizations, a practice known as “big game hunting”. The year 2024, for example, saw the largest ransomware payment ever recorded: approximately $75 million extorted by Dark Angels from a Fortune 500 company. The previous record was a $40 million payment from CNA Insurance in 2021.

In addition to remaining profitable, ransomware operators often see few consequences despite Western law enforcement action. Disruptions tend to have a short-term impact on the ransomware economy, with ransomware victim extortion posts on the dark web recovering quickly, as seen in the chart below. Indictments have even less impact if the target lives and works in a country from which they cannot be extradited to the US or Western Europe — such as in one of the countries making up the Commonwealth of Independent States (CIS). While the Russian government does not often punish cybercriminals who target outside their areas of influence, there have been at least two cases this year where arrests were made involving threat actors who had launched attacks against US entities.

![Despite law enforcement actions throughout the year, there has been limited effect on the number of ransomware victims posted on extortion blogs each month (Source: Recorded Future)] 

### Looking Ahead: Adapting to Variety in the Ransomware Ecosystem
As certain groups rebrand or rebuild using leaked source code or by acquiring code from other ransomware groups, they can adapt and expand their arsenal. Inter-group collaborations, rebranded operations, and the rise of smaller, independent threat actors fill the void left by centralized groups, leading to an expanded variant ecosystem. A larger pool of variants presents emerging challenges for defenders as proactive threat hunting and attribution become more difficult. Defenders are less likely to find success with YARA rules that focus on distinct syntax within the code base, as they are more likely to vary between attacks. However, the talent pool for building distinct functionality or attack chains is unlikely to increase as rapidly, meaning heuristic detection of common precursors to ransomware encryptor execution will remain consistent.

## Industry Analysis Gives Insight into Threat Actor Priorities
Despite the changes in cybercriminal operations described above, sector-specific targeting patterns have remained consistent over the last few years for both extortion attacks and stolen databases. Manufacturing, healthcare, and construction were the most targeted industries by ransomware groups based on Recorded Future’s ransomware victimology data, with the manufacturing industry leading for the third year in a row.

### Threat Actors Seek to Amplify Urgency to Increase Extortion Payouts
For manufacturing, a combination of limited IT and security investments, the high cost of operational downtime, and the complexity of IT and operational technology (OT) networks are likely to result in ransomware operators perceiving greater returns for attacks in this industry. Furthermore, the manufacturing industry is one of the largest industries globally, presenting the most targets of interest to threat actors.

- **Inconsistent network segmentation allows disruptions in operational technology:** Manufacturing companies tend to have complex environments using IT and OT systems that are not always protected by similarly dense security measures. For example, a 2022 study of British chemical companies demonstrated that 74% of companies reported that their OT environment was accessible from corporate IT networks. A year later, OT security company Dragos reported that 70% of attacks affecting OT originated in IT systems.
- **Operational disruption leads to high costs of downtime:** The cost of downtime for manufacturers reportedly ranges from $8,662 to $33,333 per minute, with large automotive companies suffering costs on the higher end. The average downtime following a cyberattack varies wildly, from several hours to over four months.

The healthcare industry is also characterized by a low tolerance for downtime due to the potential for adverse effects on patient health and safety. In May 2024, Ascension, a private healthcare provider in the US, suffered a ransomware attack that disrupted operations across many of its 136 hospitals, forcing the diversion of ambulances and closure of pharmacies, with critical IT systems offline for six weeks. In addition to monetary costs, ransomware attacks on hospitals have been shown to increase emergency room wait times — not just at the affected hospital but also at other hospitals in the region. The direct effects on patient care and, potentially, patient lives add further urgency to resolving ransomware incidents at healthcare facilities, putting additional pressure on companies to pay up.

The types of real-world effects of shutting down a factory or hospital floor are not the only factors driving urgency in ransomware payouts. Targeting a key third-party vendor or service provider can result in knock-on service disruption across an industry. In June 2024, CDK Global shut down data centers, phones, and applications following a BlackSuit ransomware intrusion. In turn, these mitigation measures disrupted services for approximately 15,000 car dealerships across North America. It has been widely reported that CDK Global paid a $25 million ransom. US-based economic consultant Anderson Economic Group estimated that CDK Global’s shutdown cost auto dealers over $600 million in just two weeks. According to the Detroit Free Press in August 2024, German manufacturer AEG estimated that car dealers’ total direct losses over the three weeks of the cyberattack reached $1.02 billion, with an over 5% drop in car sales for June 2024 when compared to the previous year. The high costs and widespread disruptions added urgency to the threat actor’s extortion demands, very likely factoring into CDK Global’s decision to pay.

### Value of Stolen Data Driven by Future Monetization
In addition to extorting companies with the threat of data exposure, criminals monetize access to victim networks through selling stolen data or direct access to networks. According to Recorded Future data, the number of posts from initial access brokers (IABs) on dark web criminal forums in 2024 is roughly equal to the number from 2023. However, breaking out posts by type of service offered shows that the number of exposed databases is increasing, while direct access to compromised organizations appears to be on a downward trend from a peak in 2022. The most represented industries in these criminal advertisements were consumer goods, representing 13% of all posts, followed by technology and government/public sector (both at 7% of all posts). 

![Consumer goods/retail organizations are the most represented data for sale on criminal forums  (Source: Recorded Future)]

A closer look at the prices of advertised databases shows that less frequently referenced industries tend to command higher prices. For example, databases from the retail industry were the most common, and their median price was $320 per listing, below the overall median price of $500. (Insikt Group’s use of median pricing is due to outlier numbers in the dataset.) The median price of healthcare databases and telecommunications databases increased significantly between 2023 and 2024 (100% and 163% increases, respectively); telecommunications featured the most expensive industry data with a median price of $1,000 per listing while representing only 3% of total listings. Databases stolen from the education sector saw one of the most significant price increases, jumping from a median price of $298 in 2022 and then $43 in 2023 to $700 in 2024.

![Despite a peak in 2022, initial access offerings represent only slightly more posts than databases on criminal forums (Source: Recorded Future)]

Prices of databases are driven by multiple factors, including the quality of the data, the profile of the victim organization, or the potential to monetize the data further for identity theft and other scams. Broader reports about the identity theft landscape can help contextualize the utility of exposed data. According to the US Federal Trade Commission, credit card fraud was the most common type of identity theft in the first three quarters of 2024. While financial sector data is highly likely to contain useful information for credit card fraud, other sectors, including healthcare, utilities, and educational institutions, collect personal, immutable data such as previous addresses, family members’ names, or Social Security numbers. Telecommunications customer data is also likely useful for carrying out SIM swap fraud, which continues to be a pervasive method for bypassing two-factor authentication (2FA) and committing other types of fraud.

### Looking Ahead: Anticipating the Highest “Return on Infection”
Understanding how criminals monetize access to networks, assets, and data can help inform mitigation strategies. While financially motivated threat actors do not target specific companies in the same way state-sponsored threat actors do, target prioritization is likely to remain focused on industries with the highest “return-on-infection”, which in 2024 meant the manufacturing, healthcare, and financial industries by dollar amount. This is roughly consistent with Recorded Future’s observations, where the most ransomware extortion posts involved companies in the manufacturing, healthcare, industrial equipment, construction, and service industries.

## Escalating Global Hostilities Drive Critical Infrastructure Targeting
Threat actor groups associated with Iran, China, and Russia, as well as their hacktivist proxies, targeted civilian critical infrastructure in disruptive and destructive cyberattacks, taking advantage of deniability to advance their objectives through hybrid conflict.

### Chinese State-Sponsored Pre-Positioning Demonstrates Capabilities to Disrupt US Critical Infrastructure
In February of 2024, senior US cybersecurity officials warned that the Chinese state-sponsored threat actor known as Volt Typhoon was seeking to pre-position itself in US critical infrastructure networks. Per the warnings, “pre-positioning” intends to ensure threat actors have access to critical networks to carry out a strategically timed cyberattack in the event of escalating geopolitical conflict. Reports of Volt Typhoon’s activity date back to 2023, when Microsoft detected activity at a US organization with the likely intent of “pursuing development of capabilities that could disrupt critical communications infrastructure”. The observed Volt Typhoon activity on critical infrastructure networks represents a shift in Chinese cyber threat activity against the US, which has traditionally been characterized by industrial or geopolitical espionage. Other examples of pre-positioning activity likely occurred in the context of the conflict on the China-India border, where Indian power plants continue to be targeted by reconnaissance activity despite a recent de-escalation of tensions.

Successful pre-positioning activity, as well as the continued development of advanced espionage techniques (see “Salt Typhoon” below), are the result of a nearly decade-long effort to “shift to stealth.” The Chinese government has invested substantially in developing stealth techniques, including researching zero-day vulnerabilities and exploiting edge devices, the latter of which was detected in an espionage campaign primarily targeting Taiwanese entities.

The pre-positioning activity throughout 2024 occurred in the context of a years-long trend toward increasingly adversarial relations between the US and China. The US and China continue to clash on China’s territorial expansion in the South China Sea and the Chinese government’s territorial claims over Taiwan, as well as over human rights, technology transfer, trade, and espionage. Further, the Trump administration has nominated several individuals to key national security and diplomatic positions who have been outspoken about countering China’s growing global influence.

### Salt Typhoon’s Massive Telecom Hack and US-China Relations
In October 2024, the Wall Street Journal reported that Chinese hackers had breached US telecommunications companies, gaining access to metadata associated with personal communications and systems used in court-ordered wiretapping operations. Further details about the extent of the breach emerged in briefings to the US Congress, where it was revealed that dozens of telecommunications companies were targeted and the intrusion was still ongoing. The threat actors, dubbed “Salt Typhoon”, reportedly used access to the companies to target the phones of high-profile political figures. This activity aligns with previous Chinese espionage activity targeting telecommunications companies in Asia and the Middle East to reach intelligence targets. Additionally, evidence from the February “i-Soon Leaks” indicated an interest in targeting call data records from telecommunications companies worldwide.

While espionage operations are distinctly intended to not disrupt their target networks, the discovery of such a wide-ranging infiltration of US critical infrastructure networks degraded US-China relations. As of this writing, the reaction from Congress has primarily focused on the security lapses at the telecommunications companies themselves, such as the presence of outdated routers and a lack of monitoring capabilities. Post-incident investigation of the Salt Typhoon breaches has also focused on perceived shortcomings related to federal cyber agencies’ access monitoring and incident response, though the specific details remain classified. Past Congressional outrage over cyberattacks has led to new cyber legislation, such as the passage of the Cyber Incident Reporting for Critical Infrastructure Act following the Solarwinds breach. However, the Biden administration also imposed sanctions to punish Russia for the breach. Sanctions or other punitive measures toward China will also likely emerge from this activity, further straining US-China relations.

### Russian-Linked Sabotage Efforts Indirectly Advance War Aims
Similarly, Russia has sought to advance its war aims in Ukraine by indirectly targeting Ukraine’s allies. In early May 2024, the Cybersecurity and Infrastructure Security Agency (CISA) alerted on hacktivist activity primarily targeting vulnerabilities in the water and wastewater sector. Pro-Russia hacktivists have been observed remotely manipulating human-machine interfaces (HMIs) to cause low-level disruption or damage. CISA reports that many of these incidents were due to vulnerable internet-facing devices or the use of weak or default passwords. The Russian state-sponsored threat group Sandworm has also used hacktivist personas and proxies to conduct hack-and-leak operations and amplify the impact of destructive cyberattacks through influence operations. In December, the hacktivist group Xaknet, linked to Sandworm, claimed responsibility for disrupting Ukraine’s state registers, stealing data, and preventing citizens from accessing digital services. Sandworm’s control of and relationship to its hacktivist proxies likely varies depending on the group, though Mandiant assesses that the closest operational relationship is with RussianCyberArmy_Reborn.

In addition to calling out cyber disruptions, North Atlantic Treaty Organization (NATO) countries have increasingly been calling attention to Russia’s “shadow war”, which deploys destructive sabotage operations against European critical infrastructure. Russia’s sabotage operations almost certainly seek to destabilize NATO allies, degrade NATO’s war-fighting capacity, and disrupt NATO support to Ukraine (such as targeting military assets NATO committed to providing to Ukraine), among other objectives. Insikt Group identified at least three attacks in June that were plausible Russian sabotage efforts: a break-in at a water treatment facility in Finland, an explosion at an arms factory in Poland, and a fire at a railroad terminal in Poland. Insikt Group also identified 21 additional incidents that occurred the same month throughout Europe that could also have been potential