# Zscaler ThreatLabz 2025 Ransomware Report

©2025 Zscaler, Inc. All rights reserved.

## Table of Contents
- [Executive Summary](#executive-summary)
- [Key Findings](#key-findings)
- [Ransomware Landscape: Top Trends and Targets](#ransomware-landscape-top-trends-and-targets)
- [Ransomware attacks hit new highs](#ransomware-attacks-hit-new-highs)
- [Data exfiltration trends up 92.7%](#data-exfiltration-trends-up-927)
- [Shifting to data extortion only](#shifting-to-data-extortion-only)
- [Industries facing the most attacks](#industries-facing-the-most-attacks)
- [Global and regional hotspots](#global-and-regional-hotspots)
- [Most active ransomware groups in 2024–2025](#most-active-ransomware-groups-in-20242025)
- [New ransomware groups on the scene](#new-ransomware-groups-on-the-scene)
- [Major vulnerabilities exploited in ransomware campaigns](#major-vulnerabilities-exploited-in-ransomware-campaigns)
- [Ransomware Roundup: What’s Making Headlines](#ransomware-roundup-whats-making-headlines)
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
- [How Zscaler Stops Ransomware with Zero Trust + AI](#how-zscaler-stops-ransomware-with-zero-trust--ai)
- [Ransomware Prevention Checklist](#ransomware-prevention-checklist)
- [Research Methodology](#research-methodology)
- [About ThreatLabz](#about-threatlabz)
- [About Zscaler](#about-zscaler)

---

## Executive Summary

Ransomware has long been a constant in the threat landscape—but how it operates is constantly changing. Today’s campaigns are more targeted, automated, and efficient, driven in part by the growing use of generative AI enhancing and accelerating everything from phishing lures to malware development. This evolution has translated into a significant surge in ransomware activity and impact.

From April 2024 to April 2025, the Zscaler cloud blocked more ransomware attempts than in any previous year—more than 10.8 million hits—marking a 145.9% year-over-year increase and the highest volume recorded since tracking began. At the same time, the number of organizations listed on ransomware leak sites rose 70.1%, underscoring a broader shift to extortion-driven attacks. Today’s campaigns are high-frequency and high-impact, designed to extract maximum leverage, often without the need for encryption. A growing number of ransomware operators are abandoning encryption altogether in favor of pure data extortion—an evolution mirrored by a 92.7% rise in data exfiltration volumes over the past year.

Even amid high-profile takedown initiatives like Operation Endgame, ransomware groups show no signs of slowing down. If anything, disruption may be driving reinvention. Thirty-four new ransomware families emerged during the analysis period for this report. Meanwhile, established groups such as DragonForce, Akira, and Clop climbed to the top of the activity charts, demonstrating the resilience of mature ransomware operations.

The Zscaler ThreatLabz 2025 Ransomware Report dives deeper into these developments and findings, covering top targeted sectors and regions, ransomware families to watch, evolving attack methodologies, and actionable guidance for defenders. Beyond threat tracking, learn how ThreatLabz plays an active role in protecting enterprises worldwide—from building custom tools for ransomware attack recovery to contributing to global efforts that expose and disrupt large-scale malware and ransomware ecosystems.

---

## Key Findings

- **Ransomware attempts blocked by the Zscaler cloud increased by 145.9% year-over-year** (April 2024–April 2025), marking the most significant spike we’ve seen in three years.
- **Data exfiltration volumes for 10 major ransomware families increased 92.7% year-over-year to 238.5 terabytes (TB) stolen**, signaling the broader shift toward data theft as a primary extortion tactic.
- **Public extortion cases jumped by 70.1%** based on data leak site analysis, proving the threat of reputational damage or regulatory consequences is often more compelling than encryption alone.
- **Manufacturing, Technology, and Healthcare were the top targeted industries**, and the Oil & Gas sector experienced a 935.3% increase in attacks.
- **The United States remains the #1 global target for ransomware threat actors**, experiencing 50.8% of overall attacks, followed by Canada, the United Kingdom, Germany, and India.
- **Generative AI is becoming a force multiplier**, helping to rapidly create phishing lures, write malicious code, automate data extraction, and more.
- **RansomHub (833), Akira (520), and Clop (488) emerged as the most active ransomware families**, collectively responsible for the largest share of attacks.
- **Vishing (voice-based phishing) is increasingly integrated into ransomware attacks** as voice scams become more convincing and more effective at gaining initial access.
- **ThreatLabz identified 34 newly active ransomware families** during the analysis period, bringing the total number tracked to 425 since our research began.
- **Despite rising ransomware activity, coordinated law enforcement efforts**—supported by industry experts like Zscaler ThreatLabz—have made meaningful strides in disrupting major ransomware infrastructure, as demonstrated by Operation Endgame.

---

## Ransomware Landscape: Top Trends and Targets

While headline-making breaches illustrate the global scale of ransomware, the most valuable insights come from analyzing targeting patterns and operational behaviors threat actors use across campaigns. This section goes beyond headlines to examine where ransomware is having the most significant impact (by industry and region), identify which ransomware families are leading the charge, and spotlight the emergence of new groups over the past year.

### Ransomware attacks hit new highs

Steady growth in ransomware activity is no longer surprising, but the latest data shows a dramatic surge in attack volume: attempted ransomware attacks in the Zscaler cloud have jumped 145.9% year-over-year—and sixfold since 2021. This figure reflects the volume of ransomware-related indicators and events the platform blocked. The uptick reveals more than just higher volume; it signals a shift toward faster, more deliberate campaigns targeting high-impact environments.

For security teams, ransomware tactics may be largely familiar, but the rising pervasiveness, precision, and operational efficiency of recent campaigns point to an evolution—one fueled in part by GenAI accelerating ransomware’s development into a more sophisticated and scalable cybercriminal business model.

![Figure 1: Ransomware attack indicators (events) blocked by Zscaler annually]

### Data exfiltration trends up 92.7%

Over the last year, ransomware groups have turned data theft from a supporting act into the main event. Increasingly, encryption alone—if at all—isn’t the endgame. Threat actors are exfiltrating massive amounts of data to amplify pressure and raise the stakes for victims.

A recent uptick in data exfiltration reflects this trend. ThreatLabz analysis reveals that the total volume of data stolen increased year-over-year across 10 major ransomware groups. The total volume of exfiltrated data by these groups rose 92.7%, from 123.8 TB (April 2023–March 2024) to 238.5 TB (April 2024–March 2025).

![Figure 2: Data exfiltration by key ransomware groups]

*Note: This excludes a single breach in the 2023–2024 period involving 100 TB of exfiltrated data—the largest exfiltration observed across the entire dataset—which heavily skews the annual total. Removing that outlier provided a more accurate view of broader trends in data theft activity.*

- **Hunters International** significantly increased its total data stolen year-over-year, up 224.3% from 37.7 TB to 122.1 TB. The median data loss per victim also rose from approximately 300 GB to 359 GB year-over-year, a 19.6% increase per victim.
- **DragonForce** made the highest percentage jump in total exfiltration volume, up 382.6% from 4.2 TB to 20.3 TB.
- **Dark Angels** had the highest median impact per victim: a 132.6% increase from 2.15 TB to 5 TB.
- **RansomHub** exfiltrated 86.2% more data year-over-year, with 22.4 TB total from April 2024 to March 2025.
- **RansomHouse** increased its total stolen volume by 83.1% year-over-year, from 17.2 TB to 31.6 TB.

### Shifting to data extortion only

The Zscaler ThreatLabz 2024 Ransomware Report examined how the Hive ransomware group rebranded as Hunters International in October 2023. Since the emergence of Hunters International, the group has been very active and heavily focused on data theft over encryption. In fact, from the group’s inception, they have stolen nearly 160 TB of data.

In May 2025, a new group surfaced under the brand **World Leaks**, launching attacks without deploying ransomware—choosing instead to focus exclusively on data extortion. The World Leaks site is visually and programmatically similar to Hunters International (see figure 4), indicating that the same group is likely behind both.

Incidentally, on July 3, 2025, Hunters International announced its shutdown via a message on its leak site, claiming the group was closing operations and providing free decryption tools (see figure 5).

![Figure 3: GB of data stolen per month by Hunters International]
![Figure 4: World Leaks ransomware group website]
![Figure 5: Hunters International shutdown notice]

### Industries facing the most attacks

Attackers continued to prioritize industries where the pressure to pay is highest—whether due to potential for operational disruption, the sensitivity of stolen data and the related potential for reputation damage, or regulatory exposure.

Manufacturing, Technology, and Healthcare remained the most frequently targeted sectors, representing high-stakes environments ripe for extortion and leverage.

![Figure 6: Ransomware attacks by industry based on data leak sites (top 20 industries)]

### Global and regional hotspots

Leak site data reveals a clear geographic concentration, with a dominant share of attacks targeting organizations in the United States (50.8%), far ahead of countries like Canada (5.2%) and the United Kingdom (4.6%).

![Figure 8: Top 15 countries based on share of ransomware attacks]

### Most active ransomware groups in 2024–2025

Several highly active groups continued to dominate the ransomware ecosystem, with RansomHub leading the pack, claiming the highest number of publicly named victims at 833. Interestingly, the group decided to cease operations and disappeared in April 2025.

![Figure 12: Ransomware attacks reported on data leak websites]

### New ransomware groups on the scene

The ransomware landscape is constantly shifting, with some legacy groups disappearing and new groups surfacing. The timeline in figure 13 showcases ransomware groups that became active and started publishing data on leak sites between April 2024 and April 2025.

![Figure 13: New ransomware groups with data leak sites]

### Major vulnerabilities exploited in ransomware campaigns

Ransomware groups are increasingly leveraging vulnerabilities in critical enterprise technologies to execute impactful attacks. Nearly all of these vulnerabilities are easily exploited because they are internet-facing applications that can be discovered through basic scanning techniques. Key targets include VPNs, backup systems, hypervisors, remote access tools, and file transfer applications.

#### Shoring up vulnerable systems
To combat the ransomware campaigns driven by these vulnerabilities, defenders must adopt a layered approach to security:
1. **Patching as priority**: Expedite fixes for edge-facing services—firewalls, VPNs, and backup systems.
2. **Segmentation and zero trust**: Block lateral movement by enforcing user-app segmentation, device posture management, strict access controls, and monitoring privileged accounts.
3. **Advanced threat protection with zero day coverage**: Leverage inline sandboxing and isolation technologies to prevent zero day exploitation. Perform TLS inspection to block malicious payloads and apply data loss prevention (DLP) controls to stop data exfiltration.

### Ransomware Roundup: What’s Making Headlines

#### Black Basta Leverages ChatGPT for Criminal Activities
In February 2025, a treasure trove of messages from the Black Basta ransomware group’s internal Matrix chat server were leaked online. Our findings reveal that the ransomware group employs ChatGPT in several ways:
- **Code rewriting**: The chat logs explicitly mention using ChatGPT to rewrite scripts in Python.
- **AI reliance**: The group refers to relying partly on ChatGPT alongside internet resources.
- **Interest in unrestricted AI models**: Discussion about WormGPT reflects an interest in exploring uncensored AI tools.

### Hello? It’s Ransomware Calling: Inside the Multi-Stage Attack Playbook

There has been a shift away from initial access brokers using large-scale spam campaigns as the initial infection vector. Instead, more targeted attacks have been used effectively over the last two years. Threat actors first perform reconnaissance using sites like ZoomInfo and LinkedIn to purchase contact information about employees, especially those in IT, HR, payroll, and finance.

The attack kicks off with “spam bombing” to flood a victim's inbox, followed by a phone call (vishing) where the attacker impersonates an IT employee to request remote access through an RMM tool.

![Figure 14: Multi-stage ransomware attack methodology]
![Figure 15: A ransomware initial access broker’s fake “Filters update” website]

### Leaky LockBit: RaaS Mechanisms Exposed in Dark Web Breach

In May 2025, LockBit’s affiliate and admin panels were defaced with a link to download the group’s database. The leaked MySQL database provides researchers a detailed view of LockBit’s internal operations following Operation Cronos in February 2024. The information exposes 75 affiliate monikers, 4,423 ransom chat messages, and around 60,000 bitcoin wallet addresses.

![Figure 18: Defaced LockBit admin panel]
![Figure 19: Number of LockBit affiliates by “trust level”]

### Healthcare Under Siege: The Era of Massive Data Theft

Ransomware’s playbook in the healthcare sector has evolved with a new prescription: exfiltrate first, disrupt second. Because patient trust is critical in healthcare, a public breach can be as damaging as downtime. In 2024, the US Department of Health and Human Services Office for Civil Rights (OCR) reported 725 breaches involving 500 or more individuals, with around 275 million healthcare records exposed.[^5]

[^5]: The HIPAA Journal, 2024 Healthcare Data Breach Report, January 30, 2025.

### Turning the Ransomware Tide: From the Front Lines

Collaboration between global law enforcement and private industry researchers has proven effective in dismantling some key elements of ransomware operations.

For example, in early 2025, ThreatLabz discovered a vulnerability in RansomHub that made file decryption possible without having to pay a ransom. Building on this discovery, the ThreatLabz team developed **DecryptHub**, a specialized portal designed to help organizations impacted by RansomHub’s ransomware attacks.

![Figure 22: The DecryptHub victim portal]

---

## Top 5 Ransomware Families to Watch in 2025-2026

### #1 Dark Angels
The Dark Angels ransomware group, active since April 2022, is one of the most successful ransomware families to date. The group has gained notoriety for their highly lucrative attacks, with a record-breaking $75 million ransom payment that ThreatLabz disclosed in 2024. Unlike other threat groups, Dark Angels does not outsource attacks to third-party affiliates. The number of attacks launched by Dark Angels is limited and focused on large organizations.

### #2 Clop/Cl0p
Clop, also known as ClOp, is a ransomware group that has been active since 2019. Clop has largely shifted away from file encryption, instead focusing on data extortion via supply chain attacks that exploit zero-day vulnerabilities, especially in popular web-based secure file transfer application platforms.

### #3 DragonForce
DragonForce is a ransomware group that has climbed to the top of the activity charts, demonstrating the resilience of mature ransomware operations.

### #4 Akira
Akira, associated with 520 victims, has steadily expanded its reach through numerous affiliates and initial access brokers.

### #5 Interlock
Interlock is a ransomware gang that has been linked to attacks on several major healthcare organizations.

---

is
impacting more than 2,500 organizations and leading to the loss available here.
of personal information for millions of people. Clop announced
Figure 25: Clop’s announcement of the CVE-2023-34362
this attack on their data leak site, as shown in figure 25. MOVEit vulnerability exploit The breadth of Clop’s attacks is significant, with
some victims subjected to multiple breaches by
the group. In fact, ThreatLabz identified a victim
from Clop’s MOVEit attack, who previously paid
$1 million in ransom, later falling victim to the
group’s Cleo attack.
Zscaler ThreatLabz 2025 Ransomware Report ©2025 Zscaler, Inc. All rights reserved. 25

#3 DragonForce #4 Akira
DragonForce emerged as a RaaS group in Since emerging in April 2023, Akira has
December 2023. Early versions of DragonForce’s established itself as one of the most active
ransomware used the leaked LockBit builder, ransomware groups. The initial versions of
and the group later created its own ransomware Akira were based on the leaked Conti source
based on the leaked Conti source code. In early code. The group later developed a Rust-based
2025, DragonForce announced a new “cartel” ransomware named Megazord. However, the
business model on a cybercrime forum and its group abandoned Megazord in favor of the C/
news website, as shown in figure 26. C++ based variant, which is now compiled
for ESXi versions 6 and 7 as well as Windows
This new model enables ransomware affiliates to x86 and x64. The latest variant uses the GNU
use the group’s infrastructure, tools, and services Multiple Precision Arithmetic Library (GMP) for
for their own attacks with an 80/20 percent RSA encryption instead of the native Windows
profit-share scheme. The group’s affiliates have APIs found in earlier versions. It’s interesting to
stolen more than 30 TB of data, with each victim point out that Black Basta previously used the
losing approximately 156 GB on average, with a same GMP library for asymmetric encryption
Figure 26: DragonForce “cartel” announcement
median of 72 GB. in their ransomware (before migrating to the
Crypto++ library).
DragonForce received relatively modest attention
until April 2025, when the group announced Akira affiliates continue to focus primarily on file
that they were “merging” with RansomHub, encryption rather than stealing large amounts of
one of the largest and most active ransomware data. The volumes of data exfiltration by Akira
groups at the time. RansomHub denied the affiliates are typically lower on average than many
claim and accused members of DragonForce of other ransomware groups that steal terabytes of
disrupting their infrastructure and defacing their data or more from individual victims. In fact, on
website. Whether the claim was accurate or by Akira’s data leak site (see figure 27), the average
coincidence, RansomHub shut down operations and median data theft volumes were 44.87 GB
and many of the group’s affiliates migrated to and 14.33 GB, respectively. The largest data
DragonForce. These affiliates include Scattered theft was about 370 GB, far smaller than many
Spider (aka “The Com”), which has conducted top ransomware families. However, despite not
significant attacks on large organizations using emphasizing data theft, Akira has significant
various social engineering techniques targeting IT numbers of victims and is responsible for more
departments to bypass multifactor authentication than 13 TB of data loss in total.
(MFA). Scattered Spider is believed to be behind
the DragonForce attacks targeting multiple UK
retailers in April and May 2025.
Figure 27: Akira group’s data leak site
Zscaler ThreatLabz 2025 Ransomware Report ©2025 Zscaler, Inc. All rights reserved. 26

#5 Interlock
Interlock is a newer ransomware group that has been conducting
attacks since at least September 2024, compromising around 50 victim
organizations. Interlock's attacks span various sectors, including healthcare,
education, finance, government, and manufacturing. The former two sectors
have been particularly hard-hit by Interlock. This targeting is likely due to the
group’s keen awareness of compliance frameworks such as GDPR, HIPAA,
CCPA, NYDFS, and GLBA. Interlock attempts to leverage these regulations to
pressure these victims into paying a ransom. In fact, Interlock’s ransom notes
specifically call out the financial penalties for such violations.
The group has developed ransomware variants for Windows, Linux,
and FreeBSD. The ransomware isn’t noteworthy other than it is relatively
uncommon to create specific builds for the latter. However, since many
large organizations use FreeBSD to run critical server infrastructure, it is not
surprising and will remain a target.
Similar to Dark Angels, Interlock steals significant volumes of data from
organizations. In one instance, Interlock stole more than 11 TB of data from a
single victim. Another victim in the healthcare industry lost more than 5 TB
of data and paid over $2.5 million in ransom. Overall, the group has stolen
more than 73.5 TB of data in the last nine months alone. On average, each
victim lost 1.6 TB of data, with the median loss around 700 GB.
The About section on Interlock’s data leak site, shown in figure 28,
highlights the group’s stance toward victims. Interlock blames victims for
“recklessness” and “negligence” as the root causes that lead to the group’s
ransomware attacks.
Figure 28: Interlock group’s “About Us” page
Zscaler ThreatLabz 2025 Ransomware Report ©2025 Zscaler, Inc. All rights reserved. 27

ThreatLabz
Ransomware_Notes
Archive
Zscaler ThreatLabz maintains a public GitHub repository that, as of this
writing, added another 73 new ransomware notes over the past year,
bringing the total to 1,018. This archive can be valuable for tracking
ransomware groups over time, including their data leak websites and
negotiation tactics, as well as for using stylometric analysis to link
ransomware groups that rebrand.
Zscaler ThreatLabz 2025 Ransomware Report ©2025 Zscaler, Inc. All rights reserved. 28

2026_
Predictions
3. Voice-based attacks will rise as
1. Ransomware groups will weaponize
ransomware operators refine social
GenAI for scalable, multi-phase
engineering tactics.
extortion campaigns.
Generative AI will increasingly become core infrastructure for Ransomware groups will continue to leverage voice-based attack
ransomware operations. Leaked communications from the Black Basta vectors through voice phishing or “vishing” and AI-generated audio to
group reveal how ransomware threat actors are already using tools like gain access to victim organizations. These tactics exploit human trust
ChatGPT to generate phishing lures and fake documents, debug and and urgency, often impersonating executives or IT staff to manipulate
rewrite malware, and craft deepfake content. Looking ahead, expect employees into disclosing credentials or granting access to internal
ransomware operations to expand this model—with vast possibilities, systems. As generative AI tools become more accessible, ransomware
including using LLMs to analyze and summarize sensitive data that threat actors will essentially put vishing on autopilot—leveraging
is stolen. In addition, as companies increase the amount of data they tactics like multilingual voice cloning and adaptive call scripts to deceive
collect for AI training purposes, this data will make lucrative targets for enterprise employees and open the door to encryption and extortion.
ransomware gangs.
4. Data extortion will remain a key
2. Ransomware groups will continue
driver for ransom payments, with
to employ multi-stage social
increased volumes of theft.
engineering attacks.
Data theft is becoming the primary lever in ransomware campaigns,
Ransomware operators will double down on targeted attacks and ditch and this trend will accelerate. Groups like Clop, BianLian, and Hunters
mass spam campaigns for highly precise social engineering. Using International have led the shift toward pure extortion operations,
platforms like LinkedIn and ZoomInfo, they’ll pinpoint employees with abandoning encryption entirely. ThreatLabz observed that several of
privileged access, overwhelm inboxes with spam, then impersonate IT these groups now steal hundreds of gigabytes per victim on average.
staff via phone calls to gain entry. As organizations improve their backup and recovery capabilities,
threat actors will increasingly weaponize stolen data to pressure victim
organizations into paying.
Zscaler ThreatLabz 2025 Ransomware Report ©2025 Zscaler, Inc. All rights reserved. 29

5. Ransomware source code and builder
leaks will power the next generation
of attacks.
As ransomware builder tools and source code continue to leak
(intentionally or otherwise), a new wave of low-effort, high-impact
attacks will emerge. Leaks from major ransomware groups have already
fueled spin-off operations, rebranded variants, and copycat campaigns.
Emerging groups will build on leaked codebases, modifying payloads
and delivery techniques while evading existing detection signatures.
6. Law enforcement will expand focus to
target ransomware enablers.
International law enforcement operations are growing bolder and
more targeted, taking down not just ransomware groups, but also the
infrastructure and services that enable their attacks. Operation Endgame
demonstrated that malware distribution platforms can be dismantled
at scale.
7. Ransomware affiliates will continue
to move between groups.
The ransomware-as-a-service (RaaS) model gives affiliates flexibility—
and creates volatility in the threat landscape. Affiliates frequently shift
between groups based on takedown pressures, payout terms, tooling,
or reputation. This constant movement leads to recycled infrastructure,
overlapping tactics, and rapid rebrands when operations are disrupted.
As long as affiliate models remain profitable with low risk, this pattern
will continue.
ZZssccaalleerr TThhrreeaattLLaabbzz 22002255 RRaannssoommwwaarree RReeppoorrtt ©2025 Zscaler, Inc. All rights reserved. 30

How Zscaler Stops
Ransomware_with
ZSCALER STOPS RANSOMWARE AT EVERY STAGE OF THE ATTACK
Zero Trust + AI
LIFE CYCLE:
• Minimize the attack surface: Effectively eliminate exposed
infrastructure that ransomware can target by hiding users, applications,
Ransomware thrives in environments where security is fragmented, visibility and devices behind a cloud proxy, where they are not visible or
is limited, and trust is implicit. Yet many organizations still rely on traditional discoverable from the internet, creating a far smaller attack surface.
security tools—next-generation firewalls, VPNs, and point products like There are no public IPs and no direct network access—ransomware
anti-malware—that weren’t designed to handle modern threats. threat actors cannot find or reach internal resources. Breach prediction
technology leverages AI to simulate attack scenarios and pinpoint likely
These legacy architectures create more risk than they mitigate. They leave paths threat actors could exploit, allowing security teams to remediate
critical gaps in ransomware protection, from blind spots in encrypted traffic before an attack occurs.
to siloed threat visibility and complex, inconsistent policy management.
Worse, these architectures rely on broad, overly permissive access • Prevent initial compromise: Protect users from accessing malicious
models that expose internal resources. Once attackers gain a foothold, content and detect unknown threats before they reach your network
they can move laterally across systems—making it easier for ransomware through full TLS/SSL inspection and inline sandboxing and isolation.
threat actors to spread, escalate privileges, and reach sensitive data These capabilities stop ransomware before it can execute, minimizing
without detection. the risk of a compromise occurring in the first place.
The Zscaler Zero Trust Exchange™ eliminates these risks by replacing • Eliminate lateral movement: Connect users directly to applications
outdated, network-centric models with a cloud native, AI-powered zero (and apps to other apps), not the network itself, eliminating the risk
trust architecture. It delivers a unified, scalable platform that minimizes of lateral movement. AI-powered segmentation adapts access based
risk and simplifies ransomware protection across users, devices, and on user behavior, device posture, and app context. Ransomware threat
applications—no matter where they reside. actors can’t spread from one system to another, even if an endpoint
is compromised. AI and identity threat detection and response (ITDR)
help surface anomalous access patterns while deception technology
and decoys lure ransomware threat actors into monitored traps.
• Block data exfiltration: Extortion-first ransomware campaigns rely
on stealing sensitive data. Inline data loss protection (DLP), CASB, and
traffic inspection capabilities block unauthorized transfers to sanctioned
cloud apps, shadow IT, and command-and-control (C2) infrastructure.
Zscaler ThreatLabz 2025 Ransomware Report ©2025 Zscaler, Inc. All rights reserved. 31

KEY AI-POWERED RANSOMWARE PROTECTIONS FROM ZSCALER
INCLUDE:
• Breach prediction preempts potential breach scenarios using
generative AI and multidimensional predictive models.
• Phishing and C2 detection uses inline AI-based detection from the
Zscaler Secure Web Gateway to identify and block never-before-seen
phishing sites and C2 infrastructure.
• Inline sandboxing offers comprehensive malware and zero-day threat
prevention by using advanced AI models to analyze suspicious files in a
controlled environment.
AS RANSOMWARE TACTICS EVOLVE,
• Zero Trust Browser leverages AI to identify and isolate malicious web
SO MUST DEFENSES. THE ZSCALER
content, preventing data leaks and malware delivery.
ZERO TRUST EXCHANGE IS INTEGRAL
TO HELPING ORGANIZATIONS SHRINK
• Segmentation uses machine learning to auto-generate
THEIR ATTACK SURFACE, STOP NOVEL
recommendations for app segments and policies, ultimately minimizing
AND EVASIVE RANSOMWARE THREATS,
the attack surface and preventing lateral movement.
PREVENT LATERAL MOVEMENT (EVEN
POST-COMPROMISE), AND DISRUPT
• Dynamic, risk-based policy continuously evaluates the risk posture of
EXTORTION ATTEMPTS BEFORE DATA IS
users, devices, and applications using AI-driven behavioral analysis to
EXFILTRATED.
enforce dynamic security and access policies.
• Data discovery and classification instantly scans and classifies sensitive
data across endpoint, inline traffic, and cloud apps, making it more
difficult for ransomware to target and encrypt sensitive data.
• Data loss prevention (DLP) controls block unauthorized data transfers,
backed by AI-based content inspection and policy enforcement,
preventing ransomware operators from stealing sensitive data
for extortion.
ZZssccaalleerr TThhrreeaattLLaabbzz 22002255 RRaannssoommwwaarree RReeppoorrtt ©2025 Zscaler, Inc. All rights reserved. 32

Ransomware Prevention_
Checklist
Zero trust is a must-have when it comes to stopping ransomware, but effective ransomware defense doesn’t stop there. It also depends on broader operational
layers, including employee training, secure backups, and a well-prepared response plan.
Based on insights from ThreatLabz experts, this checklist brings together the most effective steps you can take right now to reduce your ransomware risk and
build lasting resilience.
Back up data regularly Enforce multifactor authentication (MFA) Harden application security
• Maintain routine, encrypted backups, both • Require MFA across all user accounts, • Remove applications from public exposure
online and offline. especially for privileged access. to prevent ransomware actors from
• Test recovery procedures frequently and • Integrate with identity protection to detect exploiting vulnerabilities.
adapt backup strategies as ransomware and block account takeovers effectively. • Implement a zero trust architecture
tactics evolve. for internal apps to safeguard them
against ransomware.
Keep software and systems up to date Standardize corporate security policies Apply least-privileged access controls
• Apply the latest security patches promptly • Ensure all users follow consistent security • Implement least-privileged policies to
to close known vulnerabilities. procedures, including MFA, software limit users’ access strictly to the data and
• Use AI-driven threat intelligence to prioritize updates, and access controls. systems required for their roles.
patching based on real-world risk. • Adopt a security service edge (SSE) • Employ AI-powered solutions to
architecture to protect users, whether on- dynamically analyze behavior and adjust
premises or remote. privileges accordingly.
Zscaler ThreatLabz 2025 Ransomware Report ©2025 Zscaler, Inc. All rights reserved. 33

Strengthen identity protection Use AI-driven browser isolation Leverage deception technology Provide ongoing employee training
• Use ITDR tools to monitor for identity • Safely isolate user sessions from the web to • Set traps (e.g., honeypots, fake credentials) • Regularly educate users on ransomware
misconfigurations, remediate vulnerabilities prevent drive-by downloads, phishing, and to detect, misdirect, and delay attackers techniques, including phishing, social
in Active Directory that adversaries exploit credential theft. early in the kill chain. engineering, and fake software updates.
to escalate privileges and move laterally, • Let users access suspicious sites in a • Use alerts from deception systems to • Simulate real-world attack scenarios to
and detect stealthy identity threats. contained, read-only environment. speed up incident response. enhance employee preparedness.
Inspect all traffic—especially encrypted Deploy AI-powered sandboxing Control SaaS access with a CASB Create a tested ransomware response plan
• 87% of threats hide in encrypted • Detect and block evasive, never-before- • Monitor and manage cloud app usage to • Include procedures for data
channels—inspect all traffic, encrypted seen malware using AI/ML-behavior- block malicious activities like file downloads recovery, incident response, and
or not, to uncover hidden threats and based analysis. and data exfiltration. communication protocols.
prevent compromise. • Quarantine suspicious files before they • Enforce policies around data sharing and • Run regular tabletop exercises to evaluate
reach endpoints. downloads. readiness and close gaps.
Implement zero trust network access (ZTNA) Implement inline data loss prevention (DLP)
• Replace broad network access with precise, • Prevent data exfiltration and sensitive file
identity-based segmentation (user-to-app transfers by deploying inline DLP measures.
and app-to-app). • Apply policies across web, cloud, and email
• Broker access via least-privileged access channels.
controls to prevent lateral movement and
reduce attack surface.
Zscaler ThreatLabz 2025 Ransomware Report ©2025 Zscaler, Inc. All rights reserved. 34

Research_
About ThreatLabz
Follow Zscaler ThreatLabz for regular
Methodology
insights on the latest ransomware
threats and developments, including
ThreatLabz is the security research arm of Zscaler. published indicators of compromise
This world–class team is responsible for hunting (IOCs) and MITRE ATT&CK mappings.
The research methodology for this report is a comprehensive process that new threats and ensuring that the thousands of This information can be used to
uses multiple data sources to identify and track ransomware trends. The organizations using the global Zscaler platform are train your team, improve your
ThreatLabz team collected data between April 2024 and April 2025 from always protected. In addition to malware research and security posture, and help prevent
sources including: behavioral analysis, team members are involved in the ransomware attacks.
research and development of new prototype modules
• The Zscaler global security cloud. Zscaler’s cloud processes more for advanced threat protection on the Zscaler platform, ThreatLabz also maintains GitHub
than 500 trillion daily signals, blocks more than 9 billion total threats and regularly conduct internal security audits to ensure repositories with IOCs, tools
and policy violations per day, and delivers 250,000+ daily security that Zscaler products and infrastructure meet security (including proof-of-concept
updates to Zscaler customers. We analyzed this data, which includes compliance standards. ThreatLabz regularly publishes ransomware decryption tools), and an
information about source IP addresses, destination IP addresses, in-depth analyses of new and emerging threats on its archive of ransomware notes from all
and file types associated with ransomware attacks, to identify portal, research.zscaler.com. major ransomware groups.
ransomware activity.
X @ThreatLabz
• The ThreatLabz team’s own analysis of ransomware samples and
ThreatLabz security research blog
attack data. ThreatLabz tracks ransomware families and threat actors
along with corresponding attack telemetry. The team performs
deep-dive reverse engineering to understand the tools used by initial
access brokers as well as the ransomware itself, including the file
encryption algorithms. In a number of cases, the team has discovered
cryptographic flaws that can be exploited to decrypt files without
paying a ransom, and created decryption tools. The team provides
these tools to international law enforcement agencies to offer to
About Zscaler
victims free of charge. ThreatLabz also has built a proprietary malware
automation platform that can automatically detect and stop threats in
Zscaler’s cloud.
Zscaler (NASDAQ: ZS) accelerates digital transformation so that customers can be more agile, efficient,
• External intelligence sources. We also compiled and compared our resilient, and secure. The Zscaler Zero Trust Exchange™ protects thousands of customers from
own data with open source research where applicable. cyberattacks and data loss by securely connecting users, devices, and applications in any location.
Distributed across more than 160 data centers globally, the SASE–based Zero Trust Exchange is the
world’s largest inline cloud security platform. To learn more, visit www.zscaler.com.
Zscaler ThreatLabz 2025 Ransomware Report ©©22002255 ZZssccaalleerr,, IInncc.. AAllll rriigghhttss rreesseerrvveedd.. 3355

Zero Trust Everywhere
About Zscaler
Zscaler (NASDAQ: ZS) accelerates digital transformation so customers can be more agile, efficient, resilient, and
secure. The Zscaler Zero Trust Exchange™ platform protects thousands of customers from cyberattacks and data
loss by securely connecting users, devices, and applications in any location. Distributed across more than 160 data
centers globally, the SSE-based Zero Trust Exchange™ is the world’s largest in-line cloud security platform. Learn
more at zscaler.com or follow us on Twitter @zscaler.
© 2025 Zscaler, Inc. All rights reserved. Zscaler™ and other trademarks listed at zscaler.com/legal/trademarks are either (i) registered
trademarks or service marks or (ii) trademarks or service marks of Zscaler, Inc. in the United States and/or other countries. Any other
trademarks are the properties of their respective owners.
+1 408.533.0288 Zscaler, Inc. (HQ) • 120 Holger Way • San Jose, CA 95134 zscaler.com