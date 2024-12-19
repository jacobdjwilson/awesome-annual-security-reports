# ThreatLabz 2024 Ransomware Report

©2024 Zscaler, Inc. All rights reserved.

## Table of Contents
[Executive Summary](#executive-summary)
[Key Findings](#key-findings)
[Ransomware Landscape: Top Trends and Targets](#ransomware-landscape-top-trends-and-targets)
[Overall rise in ransomware attacks](#overall-rise-in-ransomware-attacks)
[Industry verticals most impacted by ransomware](#industry-verticals-most-impacted-by-ransomware)
[Geographical distribution of victim organizations](#geographical-distribution-of-victim-organizations)
[Most active ransomware groups in 2023-2024](#most-active-ransomware-groups-in-2023-2024)
[Major vulnerabilities used in ransomware attacks](#major-vulnerabilities-used-in-ransomware-attacks)
[Ransomware Roundup: What’s Making Headlines](#ransomware-roundup-whats-making-headlines)
[The ransomware plague in healthcare](#the-ransomware-plague-in-healthcare)
[The impact of the SEC’s cybersecurity ruling](#the-impact-of-the-secs-cybersecurity-ruling)
[Impact of law enforcement actions](#impact-of-law-enforcement-actions)
[Top 5 Ransomware Families to Watch in 2024-2025](#top-5-ransomware-families-to-watch-in-2024-2025)
[#1 Dark Angels](#1-dark-angels)
[#2 LockBit](#2-lockbit)
[#3 BlackCat](#3-blackcat)
[#4 Akira](#4-akira)
[#5 Black Basta](#5-black-basta)
[ThreatLabz Ransomware Notes Archive](#threatlabz-ransomware-notes-archive)
[2025 Predictions](#2025-predictions)
[How Zscaler Simplifies Ransomware Protection](#how-zscaler-simplifies-ransomware-protection)
[Holistic prevention at each stage of the attack chain](#holistic-prevention-at-each-stage-of-the-attack-chain)
[Related Zscaler products](#related-zscaler-products)
[Ransomware Prevention Guidance](#ransomware-prevention-guidance)
[Report Methodology](#report-methodology)
[About ThreatLabz](#about-threatlabz)
[About Zscaler](#about-zscaler)

2

©2024 Zscaler, Inc. All rights reserved.

ThreatLabz 2024 Ransomware Report

Ransomware attacks have reached new heights of ambition and audacity over the past year, marked by a notable surge in extortion attacks. Adding to the increase in ransomware attacks, ThreatLabz research uncovered an unprecedented ransom payout of US$75 million—the largest ever paid by one company. This amount is nearly double the highest publicly known ransom payment. <sup>1</sup> In 2023 alone, ransomware payments exceeded $1 billion, highlighting the escalating financial impact of these cybercrimes.

Ransomware threat actors’ tactics have become increasingly sophisticated and bold. Notably, they have surpassed the traditional boundaries of the corporations they attack, even going so far as to target the children of executives to provoke faster and higher ransoms.<sup>2</sup> From critical infrastructure<sup>3</sup> and major corporations<sup>4</sup> to small and medium-sized enterprises, no organization is immune to finding themselves in the crosshairs of the next campaign or evolution of attacks.

Despite law enforcement takedowns of multiple initial access brokers under special ops “Operation Endgame” and “Operation Duck Hunt,” many of the largest active ransomware families continue to rapidly regroup and launch new attacks while barely skipping a beat. Unfortunately, many ransomware actors are beyond the reach of law enforcement, making them virtually immune to criminal prosecution. As detailed in this report, law enforcement agencies have augmented their pressure tactics through reward money, sanctions, trolling, and exposing the individuals behind ransomware using various forms of psychological tactics.

As ransomware actors continuously evolve their tactics, it is crucial to stay up to date on how the threat landscape is changing.

The Zscaler ThreatLabz 2024 Ransomware Report offers an overview of the ransomware threat landscape from April 2023 through April 2024, detailing the latest trends, targets, ransomware families, and effective defense strategies.

ThreatLabz found that ransomware attacks increased by 17.8% year-over-year based on blocked attempts in the Zscaler cloud, while ransomware attacks identified through data leak site analysis surged by 57.8%. The most common targets were businesses in the manufacturing, healthcare, and technology sectors, putting critical operations and infrastructure squarely in the line of attack.

The findings presented in this report underscore the need for organizations to prioritize protection against the relentless tide of ransomware. The insights and strategies in the report serve as a crucial guide for improving your ransomware defenses. By understanding the latest trends and vulnerabilities, and implementing recommended best practices, you can significantly reduce the risk of becoming a ransomware victim and better protect your organization’s critical assets and data.

## Executive Summary

<sup>1</sup> Bloomberg, CNA Financial Paid $40 Million in Ransom After March Cyberattack, May 20, 2021.
<sup>2</sup> Business Insider, Hackers are now targeting the children of corporate executives in ransomware attacks, May 12, 2024.
<sup>3</sup> Dark Reading, Ascension Healthcare Suffers Major Cyberattack, May 10, 2024.
<sup>4</sup> CyberScoop, Boeing confirms attempted $200 million ransomware extortion attempt, May 8, 2024.

3

©2024 Zscaler, Inc. All rights reserved.

ThreatLabz 2024 Ransomware Report

Zscaler ThreatLabz research uncovered a record-breaking ransom payment of US$75 million—the largest ransomware payment by a company in history—nearly double the highest publicly known payout.

The manufacturing, healthcare, and technology sectors were the top targets of ransomware attacks, while the energy sector experienced a 500% year-over-year spike as critical infrastructure and susceptibility to operational disruptions make it particularly attractive to cybercriminals.

Ransomware attacks blocked by the Zscaler cloud increased by 17.8%, and the number of extorted companies on data leak sites grew by 57.8% in the same period year-over-year despite numerous law enforcement operations, including the seizure of infrastructure along with arrests, criminal indictments, and sanctions.

The United States remains the top target of ransomware, experiencing 49.95% of overall attacks, followed by the United Kingdom, Germany, Canada, and France.

## Key Findings

ThreatLabz identified 19 new ransomware families during the analysis period, bringing the total number to 391 since our tracking started.

The most active ransomware families were LockBit (22.1%), BlackCat (a.k.a. ALPHV) (9.2%), and 8Base (7.9%).

Vulnerabilities remain an all-too-common ransomware attack vector, emphasizing the importance of timely patching and unified vulnerability management, underpinned by a zero trust architecture to provide protection even when patches are not available.

Voice-based social engineering attacks are increasingly being used to gain access to corporate networks—a technique used by Scattered Spider and the Qakbot threat group.

4

©2024 Zscaler, Inc. All rights reserved.

ThreatLabz 2024 Ransomware Report

The dynamic nature of ransomware has placed it at the forefront of security concerns in recent years. Threat actors are constantly evolving their methods of attack and extortion, leveraging advances in artificial intelligence (AI) technology, leaked source code, and advanced encryption to maximize their impact and profitability.

This report examines the following ransomware attack trends from April 2023 through April 2024:
* Overall rise in ransomware attacks
* Industry verticals most impacted by ransomware
* Geographical distribution of victim organizations
* Increased law enforcement action against ransomware groups and initial access brokers
* Top ransomware threats and record-breaking ransom payments

## Ransomware Landscape: Top Trends and Targets

5

©2024 Zscaler, Inc. All rights reserved.

ThreatLabz 2024 Ransomware Report

## Overall rise in ransomware attacks

The latest ThreatLabz analysis reveals a concerning trend, with a 17.84% year-over-year increase in ransomware attacks based on blocked attempts observed across the Zscaler cloud. The rise in ransomware activity translates to significant disruptions and financial impacts to victim organizations of all sizes. These attacks often disrupt business operations, causing extended downtime, substantial data loss, and high recovery costs. The financial burden is considerable; not only is there a ransom demand at play, but system restoration and damage control can come at a hefty price. In light of these escalating threats, the need for robust ransomware defense measures has never been greater.

**NUMBER OF ATTEMPTS BLOCKED IN ZSCALER CLOUD**

*   **2021:** 1,502,175
*   **2022:** 2,727,114
*   **APR 2022 - APR 2023:** 3,756,858
*   **APR 2023 - APR 2024:** 4,426,966
*   **Year-over-year increase:** +17.84%

*Image description: A bar graph showing the number of ransomware attempts blocked in the Zscaler cloud from 2021 to April 2024. The bars increase in height from left to right, with the final bar representing the period from April 2023 to April 2024, and showing a 17.84% increase.*

ThreatLabz 2024 Ransomware Report

6

©2024 Zscaler, Inc. All rights reserved.

## Industry verticals most impacted by ransomware

Ransomware attacks pose significant risks to businesses of all sizes and industries. These attacks can compromise sensitive data, lead to heavy financial losses, disrupt business continuity, and damage reputations. Different industries face unique ransomware challenges based on how they operate, the data they handle, and their technological infrastructure.

Despite the variables, ransomware extortion attacks have consistently surged, with the number of victim companies listed on data leak sites increasing by 57.81% since last year’s ThreatLabz report on ransomware trends. The manufacturing industry was by far the most targeted industry, accounting for 653 attacks—more than two times as many as any other industry.

*Image description: A bar graph showing the number of ransomware attacks by industry based on data leak sites. The top 20 industries are shown, with Manufacturing having the highest number of attacks (653) and Consulting having the lowest (44).*

**Figure 1: Ransomware attacks by industry based on data leak sites (top 20 industries only).**

*   Manufacturing: 653
*   Healthcare: 312
*   Technology: 265
*   Education: 217
*   Financial Services: 159
*   Retail & Wholesale: 156
*   Legal: 154
*   Other: 152
*   Construction: 144
*   Transportation Services: 144
*   Services: 108
*   Government: 95
*   Real Estate: 79
*   Industrial Machinery & Equipment: 69
*   IT Services: 69
*   Energy: 69
*   Insurance: 50
*   Recreation: 48
*   Hospitality: 47
*   Consulting: 44

ThreatLabz 2024 Ransomware Report

©2024 Zscaler, Inc. All rights reserved.

7

### Year-over-year trends

The energy sector experienced a 527.27% year-over-year increase in ransomware attacks, likely due to its critical nature and the high ransom potential it offers to attackers.

Similarly, the restaurants, bars, and food services industry saw a 333.33% rise in such attacks. This may be attributed to the sector’s rapid digitization, driven by the adoption of advanced point-of-sales systems and online ordering platforms. While these technologies may streamline operations and improve customer experiences, they can also introduce potential vulnerabilities.

While this rise highlights the prevalence of ransomware attacks, it may not capture the full extent of ransomware incidents. Many attacks go unreported or are resolved privately through ransom payments without public disclosure. Thus, these figures should be seen as indicative of broader ransomware trends rather than a comprehensive representation of the entire threat landscape.

*Image description: A bar graph showing the year-over-year percentage change in ransomware extortion attacks by industry. The graph shows a wide range of increases and decreases, with Energy having the highest increase (527.27%) and Consumer Services having the largest decrease (-94.12%).*

**Figure 2: Year-over-year percentage change in ransomware extortion attacks by industry. Note that some sectors had a relatively low baseline of attacks in last year’s report, making their growth appear more substantial.**

*   Energy: 527.27%
*   Restaurants, Bars & Food Services: 333.33%
*   Religious Organizations: 250.00%
*   Technology: 173.20%
*   Healthcare: 126.09%
*   Legal: 102.63%
*   Manufacturing: 93.77%
*   Real Estate: 75.56%
*   Arts, Entertainment & Recreation: 75.00%
*   Agriculture & Forestry: 72.22%
*   Financial Services: 55.88%
*   Government: 48.44%
*   Pharmaceuticals: 40.00%
*   Transportation Services: 35.85%
*   Media: 31.82%
*   Education: 25.43%
*   Retail & Wholesale: 15.56%
*   Insurance: 11.11%
*   Construction: 10.77%
*   Telecommunications: 0.00%
*   Other: -8.98%
*   Aerospace & Defense: -12.50%
*   Utilities: -47.06%
*   Oil & Gas: -54.05%
*   Food, Beverage & Tobacco: -56.67%
*   Services: -59.09%
*   Mining: -60.00%
*   Household & Personal Products: -69.23%
*   Nonprofit Institutions: -70.00%
*   Basic Materials and Chemicals: -86.27%
*   Consumer Services: -94.12%

ThreatLabz 2024 Ransomware Report

©2024 Zscaler, Inc. All rights reserved.

8

## Geographical distribution of victim organizations

The United States faced a markedly higher volume of ransomware attacks than any other country, accounting for about 50% of all incidents globally. In comparison, the United Kingdom was the second-most targeted nation, experiencing nearly 6% of ransomware attacks, followed by Germany (4.09%), Canada (3.51%), and France (3.26%). Figure 3 shows a heatmap illustrating countries impacted by ransom extortions between April 2023 and April 2024.

*Image description: A world map showing the geographical distribution of ransomware victims. The United States is highlighted in the darkest color, indicating the highest number of attacks, followed by the United Kingdom, Germany, Canada, and France.*

**Figure 3: Breakdown of ransomware victims by country.**

*   United States: 49.95%
*   United Kingdom: 5.92%
*   Germany: 4.09%
*   Canada: 3.51%
*   France: 3.26%
*   Italy: 3.24%
*   Australia: 2.00%
*   Spain: 1.70%
*   India: 1.65%
*   Mexico: 1.56%
*   Brazil: 1.56%
*   Netherlands: 1.37%
*   Switzerland: 1.18%
*   Japan: 1.15%
*   Sweden: 0.99%

9

©2024 Zscaler, Inc. All rights reserved.

ThreatLabz 2024 Ransomware Report

Understanding the distribution of ransomware attacks is essential for risk assessment, resource allocation, policy development, international cooperation, and public awareness efforts in combating ransomware threats.

### Risk assessment

Analyzing heavily targeted regions helps organizations in those areas to assess their own risk levels and implement stronger cybersecurity. In ThreatLabz research, the US accounts for 50% of global ransomware attacks, calling for organizations within its borders to prioritize stringent security protocols.

### Policy development

Governments can use insights from regional ransomware attacks to inform legislation, improve security standards, promote international cooperation, and facilitate public-private sector information sharing. As a recent notable example, the SEC’s new cybersecurity rules mark a major step in enhancing transparency and accountability amid growing threats.

### Resource allocation

Targeted data enables governments and organizations to strategically allocate resources, enhancing their security posture by prioritizing support, funding, and expertise in areas with the highest threat levels.

### International cooperation

Identifying the most targeted countries allows coordinated efforts between law enforcement, organizations, and governments to combat ransomware at the national and international levels. Operation Duck Hunt and Operation Endgame exemplify how international cooperation can disrupt cybercriminal activities.

### Public awareness

Highlighting frequently targeted countries may urge individuals, organizations, and governments to take more proactive measures when it comes to cybersecurity training, incident response planning, and investment in defensive technologies.

10

©2024 Zscaler, Inc. All rights reserved.

ThreatLabz 2024 Ransomware Report

### Year-over-year trends

ThreatLabz compared ransomware attacks from this year's report with the ThreatLabz 2023 Ransomware Report to assess rates of change. Among the top 15 most targeted countries, the US experienced a notable year-over-year increase of 101.88%, and Sweden saw a staggering 350% rise, although it accounted for a significantly smaller share of the total attacks.

While analyzing ransomware trends at a global level is invaluable, it is also important to examine the specific developments in different regions of the world. Studying regional breakdowns helps organizations create tailored security plans and aid governments in developing more effective cybersecurity policies.

*Image description: Three tables showing year-over-year comparisons of ransomware attacks by country. The first table shows the top 15 targeted countries, the second shows the EMEA region, and the third shows the APAC region.*

**Figure 5: Year-over-year comparison of ransomware attacks by country.**

| Country                | Ransomware attacks by country (2023) | Ransomware attacks by country (2024) | Percentage change |
|------------------------|-------------------------------------|-------------------------------------|-------------------|
| United States of America | 902                                 | 1,821                                 | 101.88%           |
| United Kingdom         | 144                                 | 216                                 | 50.00%            |
| Germany                | 110                                 | 149                                 | 35.45%            |
| Canada                 | 151                                 | 128                                 | -15.23%           |
| France                 | 87                                  | 119                                 | 36.78%            |
| Italy                  | 63                                  | 118                                 | 87.30%            |
| Australia              | 69                                  | 73                                  | 5.80%             |
| Brazil                 | 38                                  | 57                                  | 50.00%            |
| Spain                  | 36                                  | 62                                  | 72.22%            |
| Mexico                 | 31                                  | 57                                  | 83.87%            |
| Netherlands            | 17                                  | 50                                  | 194.12%           |
| India                  | 62                                  | 60                                  | -3.23%            |
| Switzerland            | 32                                  | 43                                  | 34.38%            |
| Japan                  | 44                                  | 42                                  | -4.55%            |
| Sweden                 | 8                                   | 36                                  | 350.00%           |

**Figure 6: Year-over-year comparison of ransomware attacks by country in the EMEA region.**

| Country               | Companies impacted by ransomware attacks (2023) | Companies impacted by ransomware attacks (2024) | Percentage change |
|-----------------------|----------------------------------------------|----------------------------------------------|-------------------|
| United Kingdom        | 144                                          | 216                                          | 50.00%            |
| Germany               | 110                                          | 149                                          | 35.45%            |
| France                | 87                                           | 119                                          | 36.78%            |
| Italy                 | 63                                           | 118                                          | 87.30%            |
| Spain                 | 36                                           | 62                                           | 72.22%            |
| Netherlands           | 17                                           | 50                                           | 194.12%           |
| Switzerland           | 32                                           | 43                                           | 34.38%            |
| Sweden                | 8                                            | 36                                           | 350.00%           |
| Belgium               | 16                                           | 34                                           | 112.50%           |
| South Africa          | 13                                           | 24                                           | 84.62%            |
| Austria               | 15                                           | 24                                           | 60.00%            |
| United Arab Emirates  | 12                                           | 21                                           | 75.00%            |

**Figure 7: Year-over-year comparison of ransomware attacks by country in the APAC region.**

| Country     | Companies impacted by ransomware attacks (2023) | Companies impacted by ransomware attacks (2024) | Percentage change |
|-------------|----------------------------------------------|----------------------------------------------|-------------------|
| Australia   | 69                                           | 73                                           | 5.80%             |
| India       | 62                                           | 60                                           | -3.23%            |
| Japan       | 44                                           | 42                                           | -4.55%            |
| Thailand    | 13                                           | 25                                           | 92.31%            |
| Indonesia   | 15                                           | 23                                           | 53.33%            |
| Malaysia    | 14                                           | 20                                           | 42.86%            |
| Taiwan      | 23                                           | 17                                           | -26.09%           |
| Philippines | 7                                            | 16                                           | 128.57%           |
| Singapore   | 8                                            | 16                                           | 100.00%           |
| China       | 21                                           | 15                                           | -28.57%           |
| South Korea | 12                                           | 10                                           | -16.67%           |
| Vietnam     | 10                                           | 10                                           | 0.00%             |

ThreatLabz 2024 Ransomware Report

©2024 Zscaler, Inc. All rights reserved.

11

## Most active ransomware groups in 2023-2024

LockBit (22.1%), BlackCat (9.2%), and 8Base (7.9%) were the most active ransomware extortion groups over the past year, each responsible for a significant number of attacks. Figure 8 shows the number of data leak victims per ransomware family during this period.

*Image description: A bar graph showing the number of data leak victims per ransomware family. LockBit has the highest number of victims (988), followed by BlackCat (410) and 8Base (352).*

**Figure 8: Ransomware attacks revealed on maliciously operated data leak websites.**

*   LockBit: 988
*   BlackCat: 410
*   8Base: 352
*   Play: 345
*   Clop: 291
*   BianLian: 268
*   Akira: 224
*   Black Basta: 202
*   Medusa: 169
*   NoEscape: 126
*   Hunters: 97
*   Stormous: 92
*   Rhysida: 90
*   Qilin/AgendaCrypt: 84

### Newest ransomware groups on the scene

Figure 9 showcases a timeline of new ransomware groups that began publishing data on leak sites as part of their extortion strategy.

*Image description: A timeline showing the emergence of new ransomware groups with data leak sites from April 2023 to March 2024. The timeline shows the order in which new groups appeared.*

**Figure 9: New ransomware groups with data leak sites.**

*   APR 2023: CiphBit
*   MAY 2023: Money Message
*   JUN 2023: Dark Angels
*   JUL 2023: RAworld
*   SEP 2023: Abyss
*   OCT 2023: Akira, BlackSuit, Rhysida
*   JAN 2024: Knight (rebrand of Cyclops)
*   FEB 2024: NoEscape, INC, Underground, 3AM, Killsec
*   MAR 2024: Hunters International (rebrand of Hive), Slug, RansomHub, Cloak

ThreatLabz 2024 Ransomware Report

©2024 Zscaler, Inc. All rights reserved.

12

## Major vulnerabilities used in ransomware attacks

Vulnerabilities in software, systems, and the overall digital infrastructure can serve as critical entry points for ransomware attacks. Organizations must be aware of these vulnerabilities and take proactive measures to address them.

The Cybersecurity & Infrastructure Security Agency (CISA) maintains a comprehensive list of vulnerabilities,<sup>5</sup> including those actively exploited by ransomware groups. It is highly recommended that organizations closely monitor this list and prioritize the mitigation of vulnerabilities mentioned therein. Proactive vulnerability management is essential for strengthening the overall cybersecurity posture of an organization.

In many cases, the vulnerabilities exploited by ransomware groups impact internet-connected assets in organizations’ external attack surface, such as gateways, VPNs, and other remote connectivity technologies. Because they are internet-facing, these vulnerabilities are significantly easier for threat actors to scan for and exploit. CISA’s latest guidance<sup>6</sup> further emphasizes vulnerabilities in VPNs and remote connectivity solutions as critical points of concern, advising the adoption of the most current approaches, such as zero trust architecture, SSE, and SASE, which are based on granular access control policies.

Over the past year, prominent ransomware families have targeted and exploited the vulnerabilities shown in figure 10, significantly impacting a wide range of systems.

Available patches for these vulnerabilities should be applied as soon as possible, along with the following mitigation measures:
* Disable remote access to servers
* Use strong passwords and multifactor authentication
* Monitor servers for suspicious activity

<sup>5</sup> Cybersecurity & Infrastructure Security Agency, Known Exploited Vulnerabilities Catalog, accessed June 25, 2024.
<sup>6</sup> Cybersecurity & Infrastructure Security Agency, Modern Approaches to Network Access Security, June 18, 2024.

*Image description: A table describing prevalent vulnerabilities from April 2023-April 2024. Each row describes a vulnerability, the affected software, and the ransomware families that have exploited it.*

**Figure 10: Prevalent vulnerabilities from April 2023-April 2024.**

| Vulnerability                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             