# 2023 Mid-Year Threat Report: Navigating the Threat Landscape

## Table of Contents
- [Introduction](#introduction)
- [Ransomware Trends](#ransomware-trends)
- [Ransomware Descriptions by Family and Activity Overview](#ransomware-descriptions-by-family-and-activity-overview)
- [Top Stealers and RATs Overview](#top-stealers-and-rats-overview)
- [Top Takeaways](#top-takeaways)
- [Our Predictions for 2024](#our-predictions-for-2024)

---

## Introduction

Welcome to Deep Instinct’s interim threat report, which details the most important cyber threats of the year along with overall trends to be aware of as 2024 draws nearer. We have seen several major developments throughout the year, with the proliferation of Ransomware-as-a-Service (RaaS) being one of the most concerning. From the launch of LockBit’s affiliate program to new languages featured within BlackCat’s latest family, the impact and scale RaaS can offer ransomware gangs has proven irresistible.

State-sponsored cyber attacks have evolved as the war between Russia and Ukraine continues. Cybercriminal gangs fragmented and regrouped for a variety of reasons, with the various Conti splinter groups being particularly high profile following their inception. Adaptation by criminal gangs has not been limited to their organizational structures. As vendors have made changes to their software suites to increase their resistance to malware, gangs have also evolved their leading malware.

Examples of this evolution include nearly all stealers and Remote Access Trojans (RATs) who changed to maintain their effectiveness in overcoming traditional defenses by varying their delivery mechanisms, adopting LNK, HTML, JS and inflated archives as part of their malware strategy.

This report represents Deep Instinct’s current view of the threat landscape and trends seen between January - August 2023, and where possible, provides concrete data to verify the credibility of these developments. The information was sourced from our repositories, which are routinely analyzed as we protect our customers from incessant and ever-evolving attacks. This report provides a timely perspective of today’s threat landscape and how it is likely to evolve in 2024 and beyond.

---

## Ransomware Trends

Total number of ransomware victims in 2023 compared to 2022 is significantly higher. In fact, the number of victims in the first half of 2023 already exceeds all victims in 2022. As you can see in Figure 1, there are several spikes during 2023 caused by vulnerabilities that are often used for large-scale campaigns affecting a significant number of victims at once – such as the Zimbra and MOVEit vulnerability.

![Figure 1: Ransomware victims during 2022 and 2023, showing monthly spikes for various ransomware families including Malas, Cl0p, 8base, ALPHV, Vice Society, Hive, LockBit2, Royal, Cuba, and LockBit3.]

### 2023 H1 vs 2022 H1 and H2

Large-scale ransomware campaigns were mentioned as a prediction in our last interim report. As you can see in Figure 1 and 2, no matter how you compare it with previous timeframes, ransomware operators are working harder and breaking records for victims.

![Figure 2: Bar chart comparing the number of ransomware victims: 1547 in 2022 H1, 1472 in 2022 H2, 2835 for 2022 Full Year, and 2987 in 2023 H1.]

![Figure 3: Bar chart showing ransomware victims by threat group during 2023 H1, led by Lockbit3, ALPHV, and Cl0p.]

---

## Ransomware Descriptions by Family and Activity Overview

### 01 LOCKBIT
In January 2020, LockBit posted an announcement that they had opened an affiliate program, becoming a RaaS. They noted that the development of the locker started in September 2019. LockBit 3.0, also known as “LockBit Black,” was reported in July 2022.

### 02 ALPHV
BlackCat (aka AlphaVM or AlphaV) is a ransomware family created in the Rust programming language and operated under a RaaS model. It targets both Windows and Linux, as well as VMware ESXi environments.

### 03 CLOP
Mainly known as Cl0p, this ransomware targets various industries and organizations. Associated with the Russian threat group TA505, it utilizes zero-day exploits such as the MOVEit Transfer exploitation.

![Figure 4: Clop ransomware member tweet.]
![Figure 5: Clop using torrents to leak data.]

### 04 BIANLIAN
BianLian is a ransomware developer, deployer, and data-extortion group that has targeted critical infrastructure since June 2022. They shifted from a double-extortion model to primarily exfiltration-based extortion in January 2023.

### 05 MALAS
Also known as MalasLocker, this group was first observed in March 2023. They demand donations to charities rather than traditional ransoms. They are known for exploiting vulnerable Zimbra servers.

### 06 8BASE
Emerging in April 2022, 8Base targets small to medium-sized businesses. There are rumors of links to RansomHouse and the leaked Babuk builder.

### 07 PLAY
Also known as PlayCrypt, this group neutralizes anti-malware systems before execution. They have been identified exploiting Microsoft Exchange vulnerabilities.

### 08 ROYAL
Royal operates privately, comprising former members of the Conti group. They use a unique partial encryption tactic to evade detection and target critical infrastructure, particularly healthcare.

![Figure 6: Top threat groups in 2022 H2.]

### 09 EVEREST
Emerging in December 2020, Everest often functions as an "Initial Access Broker," selling entry points into organizations.

### 10 LORENZ
Similar to ThunderCrypt, Lorenz pressures victims by making data available for sale to competitors before releasing password-protected RAR archives.

### 11 MIDAS
Also known as Midas Touch, this is a Thanos ransomware variant written in C# and obfuscated using SmartAssembly.

### Additional Known Threats
- **12 SNATCH**: Reboots PCs into Safe Mode to evade security.
- **13 LV**: Targets manufacturing and retail; similar to REvil.
- **14 STORMOUS**: Pro-Russian group composed of ex-Conti members.
- **15 MINDWARE**: Likely a rebrand of SFile ransomware.
- **16 DARKLEAKMARKET**: Known for attacking India’s largest private bank.
- **17 CHEERS**: Targets Linux ESXi.
- **17 ONYX**: .NET-based ransomware that switched to wiper mode.

---

## Top Stealers and RATs Overview

![Figure 7: Pie chart showing the distribution of Banking Trojans/Stealers/Spyware, including Emotet, Agent Tesla, NanoCore, Redline Stealer, Remcos, Qbot, IcedID, LokiBot, Njrat, Vidar, Ursnif, Racoon, and Bumblebee.]

### 01 EMOTET
Originally a banking trojan (2014), it evolved into a Dropper. Despite infrastructure seizures in 2021, it remains active, adopting LNK files and OneNote as vectors.

### 02 AGENT TESLA
A .NET-based RAT and data stealer often used in the Malware-as-a-Service (MaaS) model.

### 03 NANOCORE
A customizable RAT developed using the .NET framework, managed by the APT33 threat group.

### 04 REDLINE STEALER
Designed to extract browser data, passwords, and cryptocurrency. Available on illicit forums via subscription.

### 05 REMCOS
A RAT providing remote control and surveillance capabilities, often abused by cybercriminals despite being marketed as a legitimate administration tool.

### 06 QBOT
Also known as Qakbot, it has been active since 2009. It uses worm features to spread and monitors browsers to steal banking credentials.

### 07 ICEDID
Also referred to as BokBot, it uses man-in-the-browser techniques to hijack bank accounts. It has recently been used to drop Nokoyawa ransomware.

### 08 LOKIBOT
Steals usernames, passwords, and cryptocurrency wallet details.

---

## Top Takeaways

### Macros Left in the Past
Threat actors have moved away from Office macros toward LNK files, JavaScript, and artificial inflation to bypass security.

![Figure 8: Chart showing the shift from PowerShell to JS and LNK files.]

### Artificial Inflation
Threat actors are padding malicious files to evade EPP and Sandbox detection, causing files to grow exponentially after extraction.

![Figure 9: Artificial inflated files in zip trends.]

### Underground Forums
Despite the closure of forums like RaidForums, Genesis Market, and Breached Forums, new alternative markets and mirroring techniques are emerging.

### Popular Systems Being Exploited
Vulnerabilities remain the primary component of large-scale attacks. The MOVEit vulnerability is a prime example of rapid exploitation following publication.

![Figure 10: Vulnerabilities exploited in the wild.]

### LLMs and Malware
The rise of LLMs like WormGPT has enabled threat actors to build malware and abuse non-existent code libraries.

![Figure 11: WormGPT pricing and advertisement.]

---

## Our Predictions for 2024

- **Threats become more sophisticated with AI**: LLMs will soon perform standalone vulnerability research and custom malware building.
- **Large-scale compromise attacks**: These will continue to cause damage; prevention-first deep learning is required to combat them.
- **AV service disruption**: Disruption of security services remains a critical focus for threat actors.
- **State-motivated cyber attacks**: These will continue to leverage AI, particularly as the Russia-Ukraine cyber war continues.
- **Macros become obsolete**: LNKs, JS, and inflated zip files will remain the dominant initial vectors.

---

**Report Authors:**
Shaul Vilkomir-Preisman, Bar Block, Simon Kenin, Mark Vaitzman

© Deep Instinct Ltd.
[deepinstinct.com](https://deepinstinct.com)