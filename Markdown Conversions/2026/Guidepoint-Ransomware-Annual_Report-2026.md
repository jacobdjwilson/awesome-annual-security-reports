# 2026 Ransomware and Cyber Threat Report

## Table of Contents
- [A Note From GRIT](#a-note-from-grit)
- [Methodology](#methodology)
- [Annual Ransomware Summary](#annual-ransomware-summary)
- [Annual Ransomware Trends](#annual-ransomware-trends)
- [Annual Taxonomy Trends](#annual-taxonomy-trends)
- [Threat Actor Spotlight: Qilin](#threat-actor-spotlight-qilin)
- [Industry Spotlight: Legal](#industry-spotlight-legal)
- [Annual Vulnerability Analysis](#annual-vulnerability-analysis)
- [Other Reporting and Analysis](#other-reporting-and-analysis)
  - [Innovation in Ransomware in 2025](#innovation-in-ransomware-in-2025)
  - [Law Enforcement Operations in 2025](#law-enforcement-operations-in-2025)
  - [Ransomware Payment Rate Analysis](#ransomware-payment-rate-analysis)
- [2025 Signpost Analysis](#2025-signpost-analysis)
- [Annual Wrap Up](#annual-wrap-up)

# 2026 Ransomware and Cyber Threat Report

A GRIT® Report

2026 Annual

## A Note From GRIT

Welcome to GRIT’s 2026 Ransomware and Cyber Threat Insights report, our flagship annual review of the trends, tactics, and context that GuidePoint’s Research and Intelligence Team (GRIT) have observed over the past year.

This report is an annual labor of love, an opportunity for our analysts to look backward and forward to inform our friends, colleagues, and professional peers.

Artificial Intelligence / Large Language Models (AI/LLM) present as an inescapable force in this year’s report, no matter how sick we all are of hearing the term in this industry. Threat actors continue to evolve in their tactics, techniques, and procedures (TTP), with AI/LLM enabling more rapid adaptation and continuing to reduce barriers to entry for less-skilled and unskilled actors.

The news is not all bad here – trickle-down benefits of innovation introduced by skilled actors takes time, and Defenders have also benefited from this technology. We hope that by the end of this report, you will better understand the reality of this threat, free of unnecessary fear, uncertainty, or doubt.

Our report concludes with our annual signpost analysis and opportunity for our team to foot-stomp what we assess to be the most impactful and substantial elements that will impact the ransomware and cybercrime landscape in the near and mid-term. We encourage our colleagues to consider these factors in their intelligence programs and organizational threat modeling.

Finally, for our readers – thank you for joining us for this year’s report. As an analytic organization as well as a services team, we believe that improvement is continuous. If you believe we have erred in our assessments, failed to consider key information, or just want to share your hot take from this year’s report, we would love to hear from you. While we can’t guarantee a response to everything, you can contact us at GRITBlog@guidepointsecurity.com

Happy Hunting.

- GRIT

## Methodology

*   Data collected for this report was obtained from publicly available resources, including the sites and blogs of threat groups themselves. It has not been validated by alleged victims. As a result of these sources, as well as unknowable outcomes and figures of victims which have not been publicly disclosed, the number of observed attacks in this report and the total number of attacks conducted will not be equal.
*   Collected data has been reviewed by GRIT for potential duplications or inaccuracies and adjusted accordingly to best reflect the true impacts of ransomware and cybercrime. We note that ransomware and cybercrime groups are likely to employ denial and deception to complicate research efforts and retain or build credibility among peers. To this end, we have reviewed each group and validated that its claims are at least as likely as not to be genuine before including them in our data set. While our process does effectively rule out clear fabricators, we cannot completely rule out groups in which the number or qualities of victims may have been exaggerated or inflated. As a result of these differences in our approach, our numbers may periodically differ from other public reporting, particularly if this reporting does not scrutinize group claims and history.
*   We note that throughout this report’s analysis of ransomware, we include data and analysis of several groups that may be better described as "extortion" groups rather than "ransomware" groups. These groups may eschew encryption and instead focus only on data exfiltration and extortion. Or they may not perform intrusion operations of any kind, instead extorting or re-extorting organizations based on historically compromised data. While these groups do not deploy ransomware, we are including them in our ransomware reporting due to their relationships with other ransomware groups and their impact on the extortion-based cybercrime environment.
*   Finally, we make efforts to exclude from our data those groups which self-identify as “hacktivists”, compromised data brokers and markets, or non-financially motivated data thieves and leakers which may employ similar TTPs as ransomware and other cybercriminal groups. While these actors and venues doubtlessly have impacts, we distinguish them from financially-motivated cybercrime and data extortion, which is the primary focus of this report.
*   Despite the above caveats, we have always and continue to assess that our reporting and our data is useful in aggregate while acknowledging that the underlying data sources have variability. We strongly believe that this report provides a consistent and accurate representation of the threat landscape over a given period, and that our observations of the underlying trends remain valuable for Defenders.
*   In cases where we leverage datasets that were not uniquely collected by us, we endeavor to cite the source appropriately.

## Annual Ransomware Summary

As we publish our fourth annual report analyzing ransomware, we close the chapter on another year of observing, fighting, and defending against contemporary crime. This one places a heavy emphasis on ransomware across the public and private sectors. What initially started as a somewhat “average” year in terms of growth surprised us by the end of December, shattering all records and resulting in a 58% Year-over-Year (YoY) increase in the number of observed ransomware victims, claimed by a record-breaking 124 distinct named groups.

2025 demonstrated the staying power and adaptability of contemporary ransomware operations. While we note and appreciate the efficacy of 2024’s broad law enforcement disruption efforts, former mid-tier groups, such as Qilin and Akira, have stepped in to fill the spots formerly filled by LockBit and Alphv, likely absorbing affiliates in the process. Still other groups, such as RansomHub, have obtained short-term successes only to be undone by internal deceit and infighting – with the associated affiliates similarly reorganizing under other groups.

We continued to observe indications of threat actor adoption of AI/LLMs in their operations, though we have found concerns of super-affiliates deploying fully autonomous ransom-bots to be overstated. AI/LLM usage remains rudimentary among less mature threat actors, though the more sophisticated and experienced operators have prioritized finding new means and manners of incorporating AI. Their successes will almost certainly trickle down over time in the same way that vulnerability exploitation has for years.

In this year’s report, we have had the opportunity and interest to focus on threat actor innovation efforts, on the profitability of the most prolific ransomware groups, and on what we believe to be the most impactful variables that will drive or hinder ransomware activity across the near- and mid-term. To do so, we have leveraged new tools to provide new perspectives, while continuing to apply the insight and analysis gleaned from the hundreds of ransomware and cybercrime incident response cases that GuidePoint supports every year.

As always, with a litany of causes for concern come opportunities for optimism, as we continue to see growing international law enforcement collaboration and disruption efforts targeting not just ransomware, but cybercrime’s underlying support infrastructure as well. As we enter 2026, we continue to view the age-old dynamic of criminals vs. defenders and law enforcement. Neither intend to slow down. More than ever, 2025 has highlighted the dense concentration of expertise and competence within an otherwise sprawling ecosystem.

Total Publicly Posted Ransomware Victims
7,515

Number of Tracked Ransomware Groups
124

Average Daily Victims
20.6

## Annual Ransomware Trends

![Graph showing ransomware victim posts per week and distinct groups posting per week in 2025.](placeholder_for_image_1)

2025 proved to be another record-setting year for ransomware activity. The number of ransomware victims we observed, as posted by ransomware groups, peaked fairly early in the year (in February), driven by activity from the data extortion group, Clop. We note this principally because the group’s preceding mass exploitation campaign took place in 2024; however, victims were not posted en masse until 2025. We then observed what would appear to be a Q2 and Q3 decline, which we initially hoped could represent a “flattening of the curve.” Regrettably, ransomware activity resurged throughout most of Q4 with record-breaking numbers closing out a record-breaking year.

As we have come to expect, the number of distinct named ransomware groups continues to rise YoY, with 124 distinct named groups observed over the course of 2025, a 46% YoY increase from 2024’s 88. However, we note that no more than 28 distinct groups posted victims in any given week, reflecting the highly ephemeral nature of many new groups. Nonetheless, we observed numerous “newcomers” operating at a higher tempo suggestive of experienced operators, including “The Gentlemen” and “Coinbase Cartel.”

Each quarter of 2025 outpaced the same quarter of the preceding year by observed victim volume; Q1 provides the most vivid example, where 2025 (2,063 observed victims) more than doubled Q1 of 2024 (1023 observed victims).

The dramatic YoY increase was less pronounced over the remainder of 2025, but small differences added up. We observed similar “summer slowdowns” to those observed in 2024 and 2022, a trend we have hypothesized as attributable to summer vacations and warmer weather.

![Graph showing victim posting rates per quarter from 2021-2025.](placeholder_for_image_2)

### 2025 Most Impacted Industries

*   The Manufacturing industry claimed the most ransomware victim organizations in terms of volume, accounting for 1060 (or 14%) of all observed ransomware victims. Manufacturing remains a constant "most impacted" presence. Its increases have been both in real (+454 victims) and relative (+1.3%) YoY.
*   The four most impacted industries in terms of victim volume – Manufacturing, Technology, Retail & Wholesale, and Healthcare – remained consistent in 2025 and 2024. While this can potentially be explained, in part, by the prevalence of the industries in the US economy, it also may speak to vulnerabilities or threats which uniquely impact organizations in these industries. We note that these industries are more likely to experience financial or operational losses from ransomware’s impacts on networks, and to hold high-value or particularly sensitive data, such as PII and PHI.
*   Akira claimed responsibility for the highest number of observed victims against four of five top industries, excluding only the Healthcare industry, which was disproportionately impacted by Qilin. Our observations show disparities in healthcare impacts by different groups in recent years, with some Ransomware as a Service (RaaS) groups prohibiting or discouraging attacks (or at least encryption) against healthcare organizations. While we do not know whether Akira employs such rules, we do expect to see a disparity in the healthcare industry in terms of “top offenders” relative to other industries.

![Bar chart showing the most impacted industries in 2025, with top ransomware groups listed for each.](placeholder_for_image_3)

### Geographic Breakdown of Ransomware Victims, 2025

![World map showing the geographic distribution of ransomware victims in 2025.](placeholder_for_image_4)

Top 10:
1.  United States: 4161 (55.37%)
2.  Canada: 337 (4.48%)
3.  Germany: 308 (4.10%)
4.  United Kingdom: 258 (3.43%)
5.  France: 192 (2.55%)
6.  Italy: 162 (2.16%)
7.  Spain: 150 (2.00%)
8.  Brazil: 134 (1.78%)
9.  Australia: 120 (1.60%)
10. India: 116 (1.54%)

### 2025 Ransomware Impacts by Country

*   Continuing a long-established trend, the United States remains the country most impacted by ransomware. The US accounted for over 55% of observed victims and outpaced all other countries combined. This disparity can be driven by a myriad of factors, including the absence of bans on ransom payments, low reporting requirements, and economic viability of US victims to “afford” ransom payments. In other words, US victims remain attractive targets because they are more likely to pay.
*   The remaining “top 10” countries by victim volume stay largely consistent with 2024, comprised primarily of western European developed economies (Germany, United Kingdom, France, Italy, Spain) and other “Western” nations (Canada, Australia). Brazil and India, as developing economies, are outliers but likely present a growing target-rich environment for attackers.

![Pie chart showing the percentage breakdown of ransomware victims by country in 2025.](placeholder_for_image_5)

### 2025 Most Impactful Ransomware Groups

![Line graph showing daily victim posts by the top ransomware groups in 2025.](placeholder_for_image_6)

*   **Qilin**: Qilin, which first appeared in 2024, rose to much greater prominence in 2025 by publicly claiming the most victims. While Qilin's open recruitment model for affiliates likely allows the group’s affiliates to attack in greater numbers, the rate of payment vs. non-payment is lower than other groups, which we explore later in this report. Ultimately, this means that while Qilin is the most prolific in terms of victims, they are far from the most “profitable.”
*   **Akira**: Akira, one of the longest-operating RaaS groups (it emerged in 2023), remains prolific. It was responsible for the second-highest number of observed victims in 2025. In recent years, Akira has shown a propensity for exploiting “zero-day” and “n-day” vulnerabilities on perimeter devices. In 2025, Akira’s mass exploitation of the SonicWall SSL VPNs led to a surge of attacks in Q3 and Q4. Notably, Akira operates on a seemingly closed recruitment model, suggesting a greater emphasis on experienced affiliates and/or operational security.
*   **Clop**: Clop, a data extortion group that has eschewed ransomware deployment in favor of mass vulnerability exploitation campaigns, was responsible for two such campaigns between late 2024 and 2025. Clop’s surge in February 2025 is a result of 2024 attacks against the Cleo managed file transfer platform. It’s November surge was the result of a campaign targeting Oracle’s eBusiness Suite (EBS). Cumulatively, these two campaigns accounted for 461 victims, though payment rates were extremely low relative to double-extortion ransomware groups.

### Q4 2025 Daily Victim Posts and Active Groups by Week

![Line graph showing daily victim posts and active groups by week in Q4 2025.](placeholder_for_image_7)

*   Q4 shattered records for the highest number of observed ransomware victims in a single quarter since GRIT began tracking ransomware data in 2022. At 2,287 observed victims, Q4 accounted nearly a third of the year’s total, and a 45% YoY increase over 2024’s Q4 victim count of 1,576.
*   LockBit has resurged in an apparent fifth iteration during Q4, despite numerous setbacks stemming from their 2024 disruption at the hands of international law enforcement and being relegated to near irrelevance by the imposition of international sanctions. In 2024, sanctions were imposed by the United States, United Kingdom, and Australia which proscribed payments to LockBit or its affiliates. “LockBit 5.0,” whether under historical or new leadership, returned to prominence with 106 claimed victims in December 2025 alone.
*   Sinobi, a relative newcomer, also increased operational activity in Q4. First observed in mid-2025, Sinobi claimed 149 victims in Q4, reflecting an operational tempo more closely associated with Established threat groups than Emerging or Developing ransomware groups. In addition, the group’s data leak site is nearly identical to that of Lynx ransomware, and Sinobi’s ransomware includes whitelisting for Lynx files. While not conclusive, these connections suggest that Sinobi boasts at least some experienced affiliates within its ranks.

## Annual Taxonomy Trends

![Bar chart showing 2025 activity by GRIT Taxonomy Classification, broken down by month.](placeholder_for_image_8)

### 2025 Activity by GRIT Taxonomy Classification

*   Established ransomware groups, or those we consider to be the most organized, prolific, and long-running, continued to account for the majority of observed victims in 2025. Established groups often benefit from more experienced affiliates, economies of scale, and visible data leak sites which support greater volumes of attacks.
*   GRIT identified a swell of Emerging or newer groups that have not been ruled out as short-term Ephemeral groups in May and October. This increase impacted “market share” of victims relative to the longer-running Established and Developing groups.
*   Manufacturing, Technology, and Healthcare remained the most impacted industries by all group types, reflecting their value and interest across groups of varying sizes and sophistication. Ephemeral groups were more likely to impact Banking and Finance victims, though we note that this observation does not provide insight into the breadth and depth of those attacks relative to more mature groups.
*   The United States, Canada, and the United Kingdom, were among the most impacted countries across all group types except for Emerging and Ephemeral groups. Interestingly, these less mature groups were more likely to impact a wider swath, including Spanish and Indian victims.

## Threat Actor Spotlight: Qilin

![Image of a Qilin logo from a Data Leak Site.](placeholder_for_image_9)

Qilin emerged within the RaaS landscape in June 2024. It first gained wide recognition for its 2024 attack on Synnovis, a UK-based medical laboratory company. The attack reportedly resulted in over 40 million USD in loss to the company and a major disruption in operations. Although it had already made a name for itself through that attack, Qilin appears to have increased its number of affiliates and operational tempo substantially in 2025. The group went from 154 victims posted in 2024 to 1,044 by the end of 2025. This makes Qilin — by-far — the most prolific ransomware group GRIT observed in 2025.

Qilin’s affiliates are believed to operate primarily from eastern Europe, though limited reporting indicates that North Korean actors may have successfully deployed Qilin ransomware as part of revenue-generating operations. While Qilin emerged under its current name in 2024, the Qilin “brand” is assessed to be a rebrand of “Agenda” ransomware, a group that dates back to September 2022. Qilin primarily employs double-extortion ransomware tactics. These tactics rely on both encryption and data extortion to coerce compliance from victims.

We assess that Qilin’s growth in 2025 was likely fueled in part by affiliates who migrated to Qilin after the April shutdown of former major RaaS player, RansomHub. Following RansomHub’s shutdown, the group increased its victim volume by 280%, rising from 188 victims at the end of April 2025 to nearly 800 by late October of the same year.

As a RaaS operator, Qilin uses an affiliate system that openly recruits potential affiliates on Dark Web forums. It licenses its ransomware to affiliates who conduct attacks, with the core group keeping a percentage of the ransom in exchange for maintaining the software and providing access to Qilin’s data leak site and chat infrastructure. Qilin's affiliate program is competitive, with affiliates allegedly earning 80% on payments of $3 million USD or lower, and 85% for payments above $3 million USD.

Throughout 2025, Qilin added several features to its panel to increase its attractiveness to affiliates, including spam campaigns and automated ransom negotiation tools. The group introduced a "Call Lawyer" feature for affiliates in June 2025 that claims to provide legal counsel to increase pressure on victims during negotiations. It also offers “in-house journalists” to assist with writing blog posts for Qilin’s data leak site. Our own experience in communications suggests the both tools are very likely simple AI/LLM tools designed to parse and summarize exfiltrated data.

![Qilin post on RAMP forum advertising new features.](placeholder_for_image_10)

Qilin ransomware samples have been observed in the wild, written in both Golang and Rust. They are capable of targeting both Windows and Linux operating systems. Affiliates can configure settings, including file exclusion lists, process and service termination settings, partial or full encryption modes, and encrypted file extensions. In October 2024, cybersecurity company Halcyon reported on an enhanced version of Qilin’s ransomware, dubbed "Qilin.B." which supports AES-256-CTR in addition to Chacha20 encryption. It also includes RSA-4096 with OAEP padding to further protect against decryption without purchasing the attacker's private key.

Like most RaaS groups, Qilin affiliate targeting appears to be opportunistic and at the discretion of individual affiliates. As such, while the group’s observed attacks have heavily impacted victims in the manufacturing, healthcare, technology, and legal industries, there is no indication that this is a result of deliberate targeting by the group. At least some subset of the group’s affiliates has been observed exploiting Fortinet vulnerabilities (CVE-2024-21762, CVE-2024-55591) in automated attacks targeting FortiOS/FortiProxy SSL-VPN devices, as well as pre-disclosure vulnerabilities in SAP NetWeaver Visual Composer (CVE-2025-31324).

![A logo and graphics from Qilin’s data leak site.](placeholder_for_image_11)

Ultimately, Qilin remains among the most prolific ransomware groups but likely enjoys and suffers from the benefits and limitations inherent in any open or semi-open RaaS operation. The group’s affiliates range in sophistication and competence. They often employ widely different tactics in their attacks. As we will explore later in this report, Qilin’s high operational tempo should not be mistaken for profitability, as a substantial portion of Qilin’s victims do not comply with the group’s ransom demands. Anecdotally, we can attribute this at least in part to a rigid communications approach and inflexibility in negotiations.

We assess that Qilin’s operations will almost certainly continue into 2026, though their efficacy may increase or decrease based on a variety of factors. A body of reporting reflecting internal complaints and disagreements suggests there may be opportunities for infighting and reputational risks to the group among ransomware operators, particularly in the event of exit-scams or suspected law enforcement infiltration. Finally, Qilin’s high victim count coupled with its open or semi-open affiliate structure strongly increases the likelihood of actual law enforcement infiltration and intelligence collection, making the group a prime target for law enforcement disruption efforts over the next year.

## Industry Spotlight: Legal

While ransomware victim counts continue to increase in general, GRIT has observed a notable surge in law firm and attorneys’ offices becoming public victims on ransomware data leak sites. The numbers tell a stark story where legal industry ransomware victims more than doubled YoY from 196 in 2024 to 455 in 2025. This represents a 132% YoY increase. Of the 455 legal sector victims in 2025, 335 (74%) were located in the United States. As one may imagine, legal entities face significant risk in the digital space due to the sensitivity of the data they handle and store. Ransomware incidents affecting law firms rarely stop at the firm itself. Legal industry victims often preside over a veritable treasure trove of sensitive data, including client PII, client PHI, and sensitive information pertaining to planned or ongoing litigation, or protected under attorney-client privilege.

As a result, when attackers compromise a legal practice and remove data, threats and risks quickly spreads to clients, counterparties, courts, regulators, and insurers. For ransomware actors, access to legal data offers influence over outcomes that matter to multiple parties, not just a singular firm experiencing the intrusion.

Based on our experience and that of our partners, data exfiltration in legal industry cases is often extensive, supported by record retention rules, and structured data organization in legal environments. This increases the depth and breadth of impacted data in cases of data extortion. It also arguably increases the ransomware actor's coercive leverage.

Anecdotally, organizations in the legal sector may be more likely to carry cybersecurity insurance, a fact which may be exploited by ransomware affiliates to justify high ransom demands and reject counter-offers during negotiations. This risk increases substantially in cases where copies of the insurance policy are maintained on-network, allowing the attacker to reference coverage and deductible details in their demands.

Finally, except for the largest firms, many legal organizations do not maintain robust in-house security capabilities. Instead, they depend on out-sourced support, Managed Detection and Response (MDR) and Managed Security Service Providers (MSSPs) for basic security. While this approach is cost-effective, it often prevents deep understanding of impacted data, the deployment of more advanced security solutions, such as Data Loss Prevention (DLP), and the testing or validation of backup systems. This can result in “scrambling” to understand the full scope and recoverability of a breach during early hours and days of incident response efforts.

Organizations within the legal industry do benefit, however, from robust resources and guidance on preparing for and defending against ransomware. The American Bar Association provides cybersecurity handbooks, guides, and resources, and federal government resources from CISA and the FBI remain viable starting points for developing and validating internal cybersecurity practices.

For legal organizations focused on the threat of ransomware, the greatest variable remains the data to which they are entrusted. Legal organizations should emphasize measures that complicate or prevent data theft, such as network segmentation, least-privilege or zero-trust architectures, and attack surface reduction. Secondarily, emplacement and validation of immutable backup solutions segmented from the main IT network can provide legal organizations with the ability to recover without paying for decryption keys, increasing their business resilience and continuity of operations.

## Annual Vulnerability Analysis

2025 witnessed a critical evolution in the RaaS landscape, characterized by simultaneous fragmentation of threat groups and highly strategic, large-scale exploitation campaigns led by longstanding established groups such as Qilin, Akira, Clop and PLAY. While key players within the ecosystem fragmented, with a recorded 117 groups observed throughout 2025, the most significant financial and operational damage stemmed from vulnerability exploitation campaigns leveraging zero-day and critical Common Vulnerabilities and Exposures (CVEs) in internet-facing enterprise applications and network perimeter devices.

This analysis is scoped specifically to CVEs disclosed in 2025 or Q4 2024 and exploited as part of Ransomware campaigns throughout 2025.

GRIT has identified the overarching trends of consistent critical business infrastructure, enterprise software suites, and VPN appliance exploitation throughout the year. These trends are exemplified by not only the deployment of complex zero-days for mass data extortion, such as Clop’s exploitation of Oracle E-Business Suite (EBS) flaws (CVE-2025-61882 and CVE-2025-61884), but also the consistent high-volume monetization of critical, unpatched Known Exploited Vulnerabilities (KEVs) in VPN infrastructure, such as through Akira’s ongoing targeting of SonicWall systems (CVE-2024-40766).

### The 2025 Ransomware Ecosystem and Vulnerability Focus

There was significant instability in the structure of 2025's ransomware market. While the traditional RaaS model remained the most prevalent form of ransomware, the ecosystem experienced both structural fragmentation and collaboration between disparate groups during 2025. Fragmentation and disruption of major RaaS brands, including RansomHub, BianLian, and 8Base, drove a proliferation of smaller, more agile actors. This resulted in a record 117 groups monitored by GRIT. Nonetheless, a handful of high-impact groups, specifically Clop, Qilin, Akira, and RansomHub, remained the most prolific key players, filling the vacuum left by earlier disruptions like LockBit and ALPHV/BlackCat from 2024. The reappearance of LockBit and the emergence of ShinyLapsusHunters, however, suggest a potential countertrend in which criminal brands retain their weight.

Ransomware operators consistently attack sectors where operational disruption creates heavy pressure to pay the ransom. GRIT’s tracking victims and threat groups highlighted a concentration of activity against Manufacturing organizations, accounting for 22% of all attacks, followed closely by victims in the Technology industry at 14%.

### Analysis of 2025 Known Exploited Vulnerabilities

Our analysis of the Known Exploited Vulnerabilities (KEV) catalog reveals critical trends in attacker impacts throughout 2025. The first half of the year saw a dramatic increase in exploitation activity. Specifically, Q1 2025 recorded a massive 82.5% YoY increase in the number of new vulnerabilities added to the KEV, and a 32.7% month-over-month (MoM) increase when comparing Q1 2025 to Q4 2024. This surge signals a significantly higher baseline of observed zero-day and n-day exploitation early in 2025. Interestingly, the number of vulnerabilities actively exploited in the second half of 2025 sharply declined quarter-over-quarter (QoQ), potentially indicating a shift from vulnerabilities in favor of other access vectors in 2H 2025.

KEV vulnerabilities disproportionately impacted Microsoft products in 2025. Their share of new KEVs doubled from 7 occurrences in Q1 2024 to 16 occurrences in Q1 2025. This concentrated targeting underpins the prevalence of Windows-based exploitations observed in groups like PLAY (CVE-2025-29824) and compared to overall market share being predominantly Microsoft around the world. Furthermore, attackers demonstrated a clear shift toward infrastructure-based vulnerabilities, with Fortinet and Cisco maintaining top 5 most-targeted vendors in 2025, replacing earlier targets like Google from last year.

![Bar chart showing KEV Vendors Year at a Glance for 2025.](placeholder_for_image_12)

Despite this surge in volume, the number of KEV entries used specifically by ransomware groups saw a reported decline throughout 2025. It dropped YoY from 42.5% of new KEV entries in Q1 2024 to just 13.7% of new KEV entries in Q1 2025. While this data reflects a reduction in novel vulnerabilities employed by ransomware actors, we note a typical delay from vulnerability publication to exploitation “in the wild” with many sub-critical vulnerabilities. High-severity but historical vulnerabilities continue to be widely leveraged by Initial Access Brokers (IABs) and RaaS affiliates. We see a large attribution of KEVs related to ransomware campaigns typically in the first and last quarters of each year. This is supported by the relatively stable numbers in Q2 and Q3 in both 2024 and 2025 compared with Q1 and Q4 numbers of the same year. This does not indicate a lull in exploitation, but rather a general trend of delay between vulnerability identification and exploitation.

| Quarter  | Known Ransomware KEVs | YoY Change | QoQ Change |
| :------- | :-------------------- | :--------- | :--------- |
| Q1 2024  | 17                    | N/A        | N/A        |
| Q2 2024  | 7                     | N/A        | -58.80%    |
| Q3 2024  | 5                     | N/A        | -28.60%    |
| Q4 2024  | 9                     | N/A        | 80%        |
| Q1 2025  | 10                    | -41.20%    | 11.10%     |
| Q2 2025  | 5                     | -28.60%    | -50%       |
| Q3 2025  | 5                     | 0.00%      | 0%         |
| Q4 2025  | 2                     | -77.80%    | -60%       |

### Annual Vulnerability Analysis: Qilin Case Studies

Qilin, a RaaS group, has cemented its position as one of the most prolific and impactful ransomware threat groups of 2025. Known for operating a double-extortion model, the group and its affiliates not only encrypt data but also exfiltrate and threaten to leak sensitive information, significantly increasing the pressure on victims.

The group's known victims reflect an outsized impact against organizations where downtime and data exposure carry severe consequences. The group distinguished itself in 2025 by demonstrating early access to, and systematic exploitation of several high-severity vulnerabilities. In doing so, Qilin’s affiliates have showcased a level of capability and sophistication that GRIT associates with highly experienced and established threat groups.

*   Security researchers have observed Qilin regularly leveraging multiple vulnerabilities in their pursuit of initial access to victim infrastructure. CVE-2025-31324 is a critical (CVSS 9.8) Unrestricted File Upload vulnerability in the SAP NetWeaver Visual Composer Metadata Uploader. This vulnerability allowed Qilin to achieve unauthenticated Remote Code Execution (RCE). Various sources have reportedly observed Qilin exploiting this vulnerability as early as March 2025, at least three weeks before its public disclosure and official patching in April 2025, confirming its use as a “zero-day” exploit. Successful exploitation of the vulnerability ultimately allows attackers to upload malicious files, such as JSP-based webshells, to victim environments in order to maintain persistent access.
*   Additionally, Qilin was observed exploiting CVE-2025-32756, a stack-based buffer overflow flaw (CVSS 9.8) in multiple Fortinet products (including FortiVoice, FortiMail, and FortiNDR) that allows a remote unauthenticated attacker to execute arbitrary code. This vulnerability was added to the CISA KEV catalog in May 2025, while Qilin was observed leveraging this RCE to deploy ransomware.
*   Researchers also observed Qilin’s use in 2025 of several FortiGate vulnerabilities initially disclosed in 2024. These vulnerabilities included CVE-2024-21762, (CVSS 9.8) an out-of-bounds write vulnerability impacting Fortinet FortiOS and FortiProxy that allows an attacker to execute unauthorized code or commands; and CVE-2024-55591, (CVSS 9.8), an authentication bypass vulnerability also affecting FortiOS and FortiProxy which allows a remote attacker to gain “super-admin" privileges. These vulnerabilities were patched in 2024 and early 2025, respectively, and were used to gain initial access in a mid-summer 2025 campaign. At the time of exploitation, Bleeping Computer reported that the ShadowServer Foundation had identified over 150,000 devices still vulnerable to CVE-2024-21762 attacks.

### Annual Vulnerability Analysis: Akira Case Study

Akira, a similarly prolific RaaS group, maintained a persistent focus throughout 2025 on vulnerabilities and weak security controls impacting remote access solutions to establish initial access. GRIT previously reported on Akira’s active targeting of SonicWall VPN products, emphasizing the group’s focus on perimeter network infrastructure as an initial access vector. Specifically, Akira affiliates frequently leveraged CVE-2024-40766 (CVSS 9.8), an Improper Access Control vulnerability in SonicWall SonicOS. This vulnerability was added to the CISA KEV catalog in September 2024 due to active exploitation, though Akira’s subsequent exploitation began in July 2025 and continued through at least November 2025. As previously referenced, RaaS groups, including Akira, will continue to exploit historical vulnerabilities so long as they remain effective against a body of vulnerable systems.

The group