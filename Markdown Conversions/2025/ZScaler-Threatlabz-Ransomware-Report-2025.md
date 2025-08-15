# ThreatLabz 2025 Ransomware Report

©2025 Zscaler, Inc. All rights reserved.

## Table of Contents
- [Executive Summary](#executive-summary)
- [Key Findings](#key-findings)
- [Ransomware Landscape: Top Trends and Targets](#ransomware-landscape-top-trends-and-targets)
  - [Ransomware attacks hit new highs](#ransomware-attacks-hit-new-highs)
  - [Data exfiltration trends up 92.7%](#data-exfiltration-trends-up-927)
  - [Shifting to data extortion only](#shifting-to-data-extortion-only)
  - [Industries facing the most attacks](#industries-facing-the-most-attacks)
  - [Year-over-year trends (Industries)](#year-over-year-trends-industries)
  - [Global and regional hotspots](#global-and-regional-hotspots)
  - [Year-over-year trends (Global)](#year-over-year-trends-global)
  - [Most active ransomware groups in 2024–2025](#most-active-ransomware-groups-in-2024–2025)
  - [New ransomware groups on the scene](#new-ransomware-groups-on-the-scene)
  - [Major vulnerabilities exploited in ransomware campaigns](#major-vulnerabilities-exploited-in-ransomware-campaigns)
- [Ransomware Roundup: What’s Making Headlines](#ransomware-roundup-whats-making-headlines)
  - [Black Basta Leverages ChatGPT for Criminal Activities](#black-basta-leverages-chatgpt-for-criminal-activities)
  - [Hello? It’s Ransomware Calling: Inside the Multi-Stage Attack Playbook](#hello-its-ransomware-calling-inside-the-multi-stage-attack-playbook)
  - [Leaky LockBit: RaaS Mechanisms Exposed in Dark Web Breach](#leaky-lockbit-raas-mechanisms-exposed-in-dark-web-breach)
  - [Healthcare Under Siege: The Era of Massive Data Theft](#healthcare-under-siege-the-era-of-massive-data-theft)
- [Turning the Ransomware Tide: From the Front Lines](#turning-the-ransomware-tide-from-the-front-lines)
- [Top 5 Ransomware Families to Watch in 2025-2026](#top-5-ransomware-families-to-watch-in-2025-2026)
  - [#1 Dark Angels](#1-dark-angels)
  - [#2 Clop/Cl0p](#2-clopcl0p)
  - [#3 DragonForce](#3-dragonforce)
  - [#4 Akira](#4-akira)
  - [#5 Interlock](#5-interlock)
- [ThreatLabz Ransomware Notes Archive](#threatlabz-ransomware-notes-archive)
- [2026 Predictions](#2026-predictions)
- [How Zscaler Stops Ransomware with Zero Trust + AI](#how-zscaler-stops-ransomware-with-zero-trust-ai)
- [Ransomware Prevention Checklist](#ransomware-prevention-checklist)
- [Research Methodology](#research-methodology)
- [About ThreatLabz](#about-threatlabz)
- [About Zscaler](#about-zscaler)

## Executive Summary

Ransomware has long been a constant in the threat landscape—but how it operates is constantly changing. Today’s campaigns are more targeted, automated, and efficient, driven in part by the growing use of generative AI enhancing and accelerating everything from phishing lures to malware development. This evolution has translated into a significant surge in ransomware activity and impact.

Even amid high-profile takedown initiatives like Operation Endgame, ransomware groups show no signs of slowing down. If anything, disruption may be driving reinvention. Thirty-four new ransomware families emerged during the analysis period for this report. Meanwhile, established groups such as DragonForce, Akira, and Clop climbed to the top of the activity charts, demonstrating the resilience of mature ransomware operations.

From April 2024 to April 2025, the Zscaler cloud blocked more ransomware attempts than in any previous year—more than 10.8 million hits—marking a 145.9% year-over-year increase and the highest volume recorded since tracking began. At the same time, the number of organizations listed on ransomware leak sites rose 70.1%, underscoring a broader shift to extortion-driven attacks. Today’s campaigns are high-frequency and high-impact, designed to extract maximum leverage, often without the need for encryption. A growing number of ransomware operators are abandoning encryption altogether in favor of pure data extortion—an evolution mirrored by a 92.7% rise in data exfiltration volumes over the past year.

The Zscaler ThreatLabz 2025 Ransomware Report dives deeper into these developments and findings, covering top targeted sectors and regions, ransomware families to watch, evolving attack methodologies, and actionable guidance for defenders. Beyond threat tracking, learn how ThreatLabz plays an active role in protecting enterprises worldwide—from building custom tools for ransomware attack recovery to contributing to global efforts that expose and disrupt large-scale malware and ransomware ecosystems.

## Key Findings

- Ransomware attempts blocked by the Zscaler cloud increased by 145.9% year-over-year (April 2024–April 2025), marking the most significant spike we’ve seen in three years.
- Data exfiltration volumes for 10 major ransomware families increased 92.7% year-over-year to 238.5 terabytes (TB) stolen, signaling the broader shift toward data theft as a primary extortion tactic.
- Public extortion cases jumped by 70.1% based on data leak site analysis, proving the threat of reputational damage or regulatory consequences is often more compelling than encryption alone.
- Manufacturing, Technology, and Healthcare were the top targeted industries, and the Oil & Gas sector experienced a 935.3% increase in attacks.
- The United States remains the #1 global target, experiencing 50.8% of overall attacks, followed by Canada, the United Kingdom, Germany, and India.
- Generative AI is becoming a force multiplier for ransomware threat actors, helping to rapidly create phishing lures, write malicious code, automate data extraction, and more.
- RansomHub (833), Akira (520), and Clop (488) emerged as the most active ransomware families, collectively responsible for the largest share of attacks.
- Vishing (voice-based phishing) is increasingly integrated into ransomware attacks as voice scams become more convincing and more effective at gaining initial access.
- ThreatLabz identified 34 newly active ransomware families during the analysis period, bringing the total number tracked to 425 since our research began.
- Despite rising ransomware activity, coordinated law enforcement efforts—supported by industry experts like Zscaler ThreatLabz—have made meaningful strides in disrupting major ransomware infrastructure, as demonstrated by Operation Endgame.

## Ransomware Landscape: Top Trends and Targets

While headline-making breaches illustrate the global scale of ransomware, the most valuable insights come from analyzing targeting patterns and operational behaviors threat actors use across campaigns.

This section goes beyond headlines to examine where ransomware is having the most significant impact (by industry and region), identify which ransomware families are leading the charge, and spotlight the emergence of new groups over the past year.

### Ransomware attacks hit new highs

Steady growth in ransomware activity is no longer surprising, but the latest data shows a dramatic surge in attack volume: attempted ransomware attacks in the Zscaler cloud have jumped 145.9% year-over-year—and sixfold since 2021. This figure reflects the volume of ransomware-related indicators and events the platform blocked. The uptick reveals more than just higher volume; it signals a shift toward faster, more deliberate campaigns targeting high-impact environments.

For security teams, ransomware tactics may be largely familiar, but the rising pervasiveness, precision, and operational efficiency of recent campaigns point to an evolution—one fueled in part by GenAI accelerating ransomware’s development into a more sophisticated and scalable cybercriminal business model.

![Figure 1: Ransomware attack indicators (events) blocked by Zscaler annually, showing a 145.9% increase from April 2024 - April 2025 compared to April 2023 - April 2024, with total blocked attempts reaching 10,887,030.](image-1-ransomware-attack-indicators-events-blocked-by-zscaler-annually.png)

### Data exfiltration trends up 92.7%

Over the last year, ransomware groups have turned data theft from a supporting act into the main event. Increasingly, encryption alone—if at all—isn’t the endgame. Threat actors are exfiltrating massive amounts of data to amplify pressure and raise the stakes for victims.

A recent uptick in data exfiltration reflects this trend. ThreatLabz analysis reveals that the total volume of data stolen increased year-over-year across 10 major ransomware groups. The total volume of exfiltrated data by these groups rose 92.7%, from 123.8 TB (April 2023–March 2024) to 238.5 TB (April 2024–March 2025). This excludes a single breach in the 2023–2024 period involving 100 TB of exfiltrated data—the largest exfiltration observed across the entire dataset—which heavily skews the annual total. Removing that outlier provided a more accurate view of broader trends in data theft activity.

![Figure 2: Data exfiltration by key ransomware groups over time, showing volume in TB on a logarithmic scale from April 2023 to March 2025 for groups like DragonForce, Underground, Hunters International, RansomHouse, INC Ransom, Qilin, and Dark Angels.](image-2-data-exfiltration-by-key-ransomware-groups.png)

- Hunters International significantly increased its total data stolen year-over-year, up 224.3% from 37.7 TB to 122.1 TB. The median data loss per victim also rose from approximately 300 GB to 359 GB year-over-year, a 19.6% increase per victim. The next section (“Shifting to data extortion only”) explores how the group decided to move entirely away from file encryption.
- DragonForce made the highest percentage jump in total exfiltration volume, up 382.6% from 4.2 TB to 20.3 TB. Although the median remained mostly stable with a slight decline, the increase in overall volume suggests the group has been compromising more victims.
- Dark Angels had the highest median impact per victim: a 132.6% increase from 2.15 TB to 5 TB. This tracks with the group’s continued focus on large, high-value targets despite fewer overall incidents.
- RansomHub exfiltrated 86.2% more data year-over-year, with 22.4 TB total from April 2024 to March 2025. The group’s median data loss per victim more than doubled from 50 GB to 118 GB.
- RansomHouse increased its total stolen volume by 83.1% year-over-year, from 17.2 TB to 31.6 TB. Its median data loss per victim also increased from 425 GB to 500 GB.

### Shifting to data extortion only

The Zscaler ThreatLabz 2024 Ransomware Report examined how the Hive ransomware group rebranded as Hunters International in October 2023, following an FBI-led operation that seized the group’s infrastructure earlier that year. Since the emergence of Hunters International, the group has been very active and heavily focused on data theft over encryption. In fact, from the group’s inception, they have stolen nearly 160 TB of data. Each Hunters International victim lost an average of 698 GB, and the median data loss was 317 GB. Figure 3 shows the volumes of data stolen per month since the group’s formation.

![Figure 3: GB of data stolen per month by Hunters International, showing monthly totals and a trend line from November 2023 to March 2025.](image-3-gb-of-data-stolen-per-month-by-hunters-international.png)

In May 2025, a new group surfaced under the brand World Leaks, launching attacks without deploying ransomware—choosing instead to focus exclusively on data extortion. The World Leaks site is visually and programmatically similar to Hunters International (see figure 4), indicating that the same group is likely behind both.

Since World Leaks started attacks in May 2025, the group has stolen more than 25 TB of data. The data theft statistics are very similar to Hunters International with each victim losing 769 GB on average with a median loss of 452 GB.

Incidentally, on July 3, 2025, Hunters International announced its shutdown via a message on its leak site, claiming the group was closing operations and providing free decryption tools (see figure 5).

This pivot from file encryption to data theft is not unprecedented. Other groups like BianLian and Clop have also shifted away from ransomware in favor of data extortion, a trend we explore in more detail later in this report.

![Figure 4: World Leaks ransomware group website, showing a dark-themed page with a list of victim organizations and a countdown timer.](image-4-world-leaks-ransomware-group-website.png)

![Figure 5: Hunters International shutdown notice, displaying a message on their leak site announcing the closure of operations and offering free decryption tools.](image-5-hunters-international-shutdown-notice.png)

### Industries facing the most attacks

Attackers continued to prioritize industries where the pressure to pay is highest—whether due to potential for operational disruption, the sensitivity of stolen data and the related potential for reputation damage, or regulatory exposure.

Figure 6 shows the number of ransomware incidents per industry based on leak site data, offering a snapshot of confirmed attacks where threat actors exfiltrated data and applied extortion pressure. Manufacturing, Technology, and Healthcare remained the most frequently targeted sectors, representing high-stakes environments ripe for extortion and leverage.

![Figure 6: Ransomware attacks by industry based on data leak sites (top 20 industries), showing Manufacturing, Technology, and Healthcare as the most targeted.](image-6-ransomware-attacks-by-industry-based-on-data-leak-sites.png)

### Year-over-year trends (Industries)

Figure 7 shows year-over-year percentage changes in ransomware attacks by industry.

Ransomware attacks on the Oil & Gas sector have spiked more than 900% year-over-year, likely driven by a combination of increased automation—from drilling rigs to pipelines—inflating the attack surface and outdated security practices. In 2025, the Cybersecurity and Infrastructure Security Agency (CISA) warned[^1] that even “unsophisticated” threat actors are exploiting vulnerabilities in industrial control systems (ICS) and SCADA technology, which are essential for operations in oil and gas.

The Agriculture sector also saw ransomware attacks skyrocket by 677.4%. Farming operations are becoming more and more digitized (think smart tractors and IoT-enabled sensors), yet security defenses haven’t kept pace. Still, there are signs of progress and recognition that farming systems are now prime ransomware targets: John Deere, a major manufacturer of agriculture machinery, hosted a 2025 hackathon where students worked to expose vulnerabilities in its smart tractors.[^2]

Healthcare remains one of the most frequently and consistently targeted, with attacks rising steadily 115.4% year-over-year. According to The HIPAA Journal,[^3] researchers at Michigan State University, Yale University, and Johns Hopkins University have found that ransomware is now one of the leading causes of healthcare data breaches. This risk became painfully real for several major healthcare organizations hit by ransomware attacks attributed to the Interlock ransomware gang (on our ransomware family watch list). Learn more in the section, “Healthcare Under Siege: The Era of Massive Data Theft.”

[^1]: CISA, Unsophisticated Cyber Actor(s) Targeting Operational Technology, May 6, 2025.
[^2]: Axios, John Deere invites students to hack tractors, June 24, 2025.
[^3]: The HIPAA Journal, Study Explores Extent of Hacking and Ransomware Attacks in Healthcare, May 16, 2025.

![Figure 7: Year-over-year percentage change in ransomware extortion attacks by industry, showing Oil & Gas with a 935.3% increase and Agriculture & Forestry with a 677.4% increase.](image-7-year-over-year-percentage-change-in-ransomware-extortion-attacks-by-industry.png)

### Global and regional hotspots

Leak site data reveals a clear geographic concentration, with a dominant share of attacks targeting organizations in the United States (50.8%), far ahead of countries like Canada (5.2%) and the United Kingdom (4.6%). This reflects how threat actors continue to prioritize digitally concentrated, high-value economies. Figure 8 breaks down the top 15 most targeted countries by share of ransomware attacks recorded on data leak sites.

![Figure 8: Top 15 countries based on share of ransomware attacks, with the United States accounting for 50.8% of attacks.](image-8-top-15-countries-based-on-share-of-ransomware-attacks.png)

### Year-over-year trends (Global)

Ransomware’s impact varies widely from region to region. Understanding where attacks are accelerating helps predict where threat actors are likely to strike next and supports more regionally informed defense strategies.

**GLOBAL TOP 15: MASSIVE SPIKES IN THE US**

Ransomware attacks surged worldwide, with the top 15 countries by number of ransomware attacks experiencing double- and triple-digit percentage increases (see figure 9). Attacks in the US more than doubled to 3,671 attacks—exceeding the combined total of the remaining top 15 most-targeted countries. Canada’s 194.5% increase reinforces how threat actors are expanding across North America, with a growing focus on vulnerable sectors. The Canadian Centre for Cyber Security’s National Cyber Threat Assessment 2025-2026 names ransomware the top cybercrime threat to the nation’s critical infrastructure, citing escalating attacks on healthcare, industrial, and public sector organizations.[^4]

[^4]: Canadian Centre for Cyber Security, National Cyber Threat Assessment 2025-2026, accessed July 14, 2025.

![Figure 9: Year-over-year comparison of ransomware attacks by country, showing the United States with a 101.6% increase and Canada with a 194.5% increase.](image-9-year-over-year-comparison-of-ransomware-attacks-by-country.png)

**EMEA: INTENSIFYING ATTACKS IN EUROPE AND BEYOND**

The Europe, Middle East, and Africa (EMEA) region experienced widespread increases in ransomware activity, as shown in figure 10. Notable year-over-year spikes included major economies like Spain (+116.1%) and Germany (+74.5%) as well as smaller markets such as Belgium (+73.5%). Israel saw a 436.4% spike, a sharp relative increase that, while from a smaller baseline of attacks, likely reflects growing geopolitical tensions and a rise in state-linked ransomware operations.

![Figure 10: Year-over-year comparison of ransomware attacks by country in the EMEA region, highlighting significant increases in Israel, Spain, and Germany.](image-10-year-over-year-comparison-of-ransomware-attacks-by-country-in-the-emea-region.png)

**APAC: EXPLOSIVE GROWTH IN EMERGING AND ESTABLISHED MARKETS**

The Asia-Pacific (APAC) region recorded some of the highest year-over-year increases globally. As figure 11 shows, ransomware actors broadened their footprint across a region characterized by fast-paced digital transformation and inconsistent levels of cyber maturity. The impact was felt throughout APAC, spanning regional tech and logistics hubs like Singapore (+237.5%) and Taiwan (+147.1%) to large-scale economies like China (+186.7%) and India (+231.7%).

![Figure 11: Year-over-year comparison of ransomware attacks by country in the APAC region, showing high percentage changes in India, Singapore, and China.](image-11-year-over-year-comparison-of-ransomware-attacks-by-country-in-the-apac-region.png)

### Most active ransomware groups in 2024–2025

Several highly active groups continued to dominate the ransomware ecosystem, with RansomHub leading the pack, claiming the highest number of publicly named victims at 833. This positioned the group as the most prolific ransomware operation based on reported activity over the last year. Interestingly, the group decided to cease operations and disappeared in April 2025.

Akira and Clop have both moved up in the ransomware attack rankings since last year. Akira, associated with 520 victims, has steadily expanded its reach through numerous affiliates and initial access brokers. Clop, known for its focus on supply chain attacks, is close behind with 488 victims, highlighting its strategy of targeting the third-party software applications that many companies use to maximize impact.

Figure 12 shows the ransomware groups with the most victims over the last year.

![Figure 12: Ransomware attacks reported on data leak websites, showing RansomHub with 833 victims, Akira with 520, and Clop with 488.](image-12-ransomware-attacks-reported-on-data-leak-websites.png)

### New ransomware groups on the scene

The ransomware landscape is constantly shifting, with some legacy groups disappearing and new groups surfacing. This can be a strategic rebranding to sidestep sanctions or an effort by a new group to fill a void left by others. Regardless, affiliates from defunct ransomware groups regularly transition between operations, employing their established attack methodologies. The timeline in figure 13 showcases ransomware groups that became active and started publishing data on leak sites between April 2024 and April 2025.

![Figure 13: New ransomware groups with data leak sites, showing a timeline of groups emerging between April 2024 and April 2025, including DarkVault, Apos, SpaceBears, BrainCipher, Embargo, Lynx, Fog, Helldown, Interlock, Nitrogen, Hellcat, Sarcoma, Eldorado, Cicada330, Kairos, Termite, FunkSec, SafePay, Babuk2, Morpheus, KrakenCryptor, Anubis, Trinity, FragVanHelsing, NightSpire, Weyhro, RALordArkana, Devman, and Bert.](image-13-new-ransomware-groups-with-data-leak-sites.png)

### Major vulnerabilities exploited in ransomware campaigns

Ransomware groups are increasingly leveraging vulnerabilities in critical enterprise technologies to execute impactful attacks. Exploiting these vulnerabilities provides attackers direct pathways to move laterally, steal sensitive information, and spread ransomware across network environments. Nearly all of these vulnerabilities are easily exploited because they are internet-facing applications that can be discovered through basic scanning techniques. Key targets include VPNs, backup systems, hypervisors, remote access tools, and file transfer applications—technologies that are pervasive across organizations and essential to operations.

**Virtualization Software**
Hypervis