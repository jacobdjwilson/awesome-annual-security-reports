# 2026 Cyber Threat Report

## Table of Contents
- [Inside the Business of Cybercrime](#inside-S1)
- [2025 Threat Landscape](#section-2025-threat-landscape)
- [Attack Breakdown By Industry](#section-attack-breakdown-by-industry)
- [Ransomware](#section-ransomware)
- [Attacker Tools and Techniques](#section-attacker-tools-and-techniques)

---

# Inside the Business of Cybercrime

As adversaries heavily abused legitimate tools, processes, and software at scale, and locked in on stealth and speed in 2025, the lines between normal activity and unauthorized intrusions blurred.

Attackers have realized they don't need to break in anymore when they can just log in as you. As a result, identity-based attacks surged as attackers relied on multi-factor authentication (MFA) fatigue, token theft, OAuth abuse, and misconfigured SaaS applications to infiltrate and persist in target environments.

Legitimate tools and processes quietly morphed into dangerous attack vectors. Bad actors continued to abuse trusted infrastructure, like remote monitoring and management (RMM) tools, and living off the land binaries (LOLBins), to avoid detection before launching payloads.

Social engineering sharpened its deceptive edge. ClickFix and fake CAPTCHA schemes were abundant, tricking users into installing infostealers, ransomware, or remote access trojans (RATs).

Right now, the good guys are losing way too often. Malicious hackers are the real competition you have in your business. We don’t say that to scare you, but to wake you up. Let’s get to work. It’s time to wreck hackers together.

Your traditional business competitors aren’t the only ones you have to worry about, because cybercriminals are actively trying to steal your livelihood. They’re organized, efficient, and relentlessly profit-driven, running operations that rival legitimate corporations in scale and strategy. They silently scope out your digital footprint and online identities while targeting your people.

All too often, the biggest vulnerability isn’t a zero-day exploit: it’s humans. We get tired, we get distracted, and we click things we shouldn't. These seemingly innocent mishaps turn a normal Tuesday into an unwanted interruption at 3am.

One thing is crystal clear—you can’t hire or innovate fast enough to fight these threats alone. Security isn’t just an IT ticket anymore: it’s a finance issue, an HR issue, a leadership issue, and a business survival issue.

The Huntress 2026 Cyber Threat Report looks back at 2025 to show you where threat actors moved the needle and what that means for your business to safely scale today and beyond. The report draws on analysis gleaned from over 4.6 million endpoints and 9.4 million identities protected by the Huntress Security Platform and backed by a 24/7 AI-assisted Security Operations Center (SOC).

---

<div id="section-2025-threat-landscape"></div>

# 2025 Threat Landscape

## 2025 Threat Landscape at a Glance

Throughout 2025, cybercriminals leveled up their attack playbooks, prioritizing stealthy access and persistence in targeted environments. They did it by abusing legitimate tools, launching sophisticated identity attacks, and executing clever social engineering scams.

We successfully shut down attackers using these exact methods every day in 2025. And in 2026, it's crucial to understand the most common threats competing with your business…

### RMM Abuse
Businesses use RMMs to work smarter, but attackers abuse these trusted tools to gain persistence, execute commands, and deploy malware while evading detection, leading to a 277% year-over-year increase in RMM abuse. By abusing the inherent legitimacy of these platforms, threat actors blend in with normal admin activity, significantly complicating defense efforts.

### ClickFix and Fake CAPTCHA Variants
ClickFix accounted for 53.2% of all malware loader activity, showing that abuse of end-user trust rather than traditional vulnerabilities is an effective tactic. Threat actors also invested in new ClickFix techniques and post-attack patterns. Fake CAPTCHA lures showed up across different types of campaigns, blurring the lines between normal and malicious activity. This reflects a broader shift towards scaling stealthier operations, away from more easily detected exploit-driven campaigns focused on CVEs.

### Ransomware
This ruthless threat accounted for 5% of all incidents in 2025, contributing to a year-over-year volume increase. The average time-to-ransom (TTR) went up from 17 to 20 hours, as ransomware attackers focused on stealth, data theft, and extortion. We saw four major groups—Akira, Medusa, Qilin, and Ransomhub—dominate over half of all ransomware incidents. Intense competition drove these actors toward a standardized playbook, tapping into tactics like Active Directory mapping, disabling security tools, and deploying encrypted tunnels.

### Identity-Based Attacks
These ghostlike threats have evolved from isolated incidents into structured intrusion chains, making the unsuspecting user the main attack vector. Attackers now bypass traditional perimeter defenses by logging in with valid credentials, using tactics like adversary-in-the-middle (AiTM) schemes and shadow workflows to launch more damaging attacks like business email compromise (BEC). In 2025, this shift solidified identity as the new endpoint, with access policy and trust boundary violations (37.2%), mailbox manipulation and persistence (19.0%), and AiTM dominating identity-based threat activity.

### Frequency of Threats Overall (2024 vs. 2025)

![Frequency of threats overall bar chart comparing 2024 and 2025 percentages across threat categories including RMM Abuse, Malware, Malicious Script, Stealers, RATs, Ransomware, Lateral Movement, and Hacking Tools.](Figure 1: Most common threat categories in 2024 vs. 2025)

---

<div id="section-attack-breakdown-by-industry"></div>

# Attack Breakdown By Industry

## Industries Under Fire

Throughout 2024, attackers targeted a wide range of industries, with a focus on education and healthcare. This trend continued in 2025, with these two industries accounting for 37% of all observed incidents. Notably, healthcare overtook education as the most targeted industry, representing 21% of all attacks. This shift reflects attackers’ focus on the high resale value of sensitive patient data and the critical nature of medical services, which they exploit to demand higher ransom payments.

At the same time, the manufacturing industry became a new focus for attackers, accounting for 17% of observed incidents in 2025. Manufacturing’s "zero-downtime" requirements make it especially vulnerable to extortion. Brief production interruptions can result in millions of dollars in losses, as seen when a breach at Jaguar Land Rover forced a complete shutdown of global manufacturing.

Beyond these industries, the technology and government sectors also saw major cyber incidents.

![Industries targeted by percentage in 2024 vs 2025 showing Healthcare, Manufacturing, Education, Technology, Government, and Other sectors.](Figure 2: Industries targeted by percentage in 2024 vs. 2025)

### Threats by Industry (2024 vs. 2025)

![Threat frequency by industry comparing Healthcare, Technology, Education, Government, and Manufacturing across various threat types.](Figure 3: Threat frequency by industry in 2024 vs. 2025)

In 2025, we noticed a shift toward more operationally efficient and stealth-focused attacker behavior across all major industries. Attackers were forced to adapt or risk getting left in the dust, with many malware and ransomware groups either pivoting to new tactics or losing ground.

- **Healthcare RMM Abuse**: +111% (2024 to 2025)
- **Technology RMM Abuse**: +107% (2024 to 2025)

> Healthcare and technology experienced the largest increases in attacks leveraging RMM abuse, letting attackers stay undetected for longer periods, giving them more time to operate in targeted environments. This extended dwell time makes it easier to steal credentials, access additional systems, and move laterally before detection occurs.

Government environments, on the other hand, continue to be targeted by infostealers and malicious scripts. This suggests that specific controls focusing on RMM attack vectors work, but attacks using traditional tradecraft are still slipping through the cracks.

Attackers heavily targeted the manufacturing sector with traditional malware loaders and RMMs to gain access. We saw a drop in hacking tools and malicious scripts, meaning attackers are moving toward abusing trusted services and platforms versus heavy payload intrusions. Why? Because security tools often catch them when they use malicious scripts to download other components or deliver payloads.

> Cybercrime isn't underground anymore; it's the world's third-largest economy. There are pricing models, support, and even refunds. It’s organized crime operating like a business.
> 
> — **Kyle Hanslovan**, CEO and Cofounder of Huntress

Ransomware persists, but threat actors are targeting more selectively. They often look for large payouts or environments they can easily manipulate. Similar to what we saw in 2023, this could open the door for smaller ransomware groups to claim their stake in the threat landscape as others shift their focus to extortion-only operations and specific targeting patterns, like specific industries or companies. Successful takedowns caused a few of these groups to shut down, but many moved on to bigger targets.

Malicious scripts are still popular, but many operators have replaced them with RMM installers or RAT components. Additionally, endpoint detection and response (EDR) solutions are getting better at spotting these scripts. This often disrupts attacks earlier in the attack path, killing longer chains of script executions or similar payloads.

Finally, attackers seem to be standardizing playbooks tested against technology and MSP-adjacent environments and reusing them on other industries. 2025 data indicates that risk will be defined by low-noise abuse of legitimate access mechanisms, combined with faster credential theft to pivot to other resources, rather than typical malware families.

Looking ahead, RMM abuse will continue to outpace traditional RAT deployments across all industries. This is especially true where distributed or outsourced IT operations are part of the security stack. Attackers have caught on that exploiting these trusted relationships gives them access to multiple victims simultaneously.

### Out (Traditional & Noisy) vs. In (Stealth & Trusted)
- Malicious Scripts ➔ RMM Installers
- EDR’s Managed AV Shut Down ➔ Cobalt Strike
- Generic RATs ➔ Legitimate RMM Components
- Mass Phishing ➔ Credential Theft

![Example of a malicious intrusion at a European manufacturer showing SIEM detected RDP, Lateral Movement, and EDR actions.](Figure 4: Example of a malicious intrusion at a European manufacturer)

---

<div id="section-ransomware"></div>

# Ransomware

## The State of Ransomware

Despite a year of aggressive law enforcement takedowns and high-profile disruptions, ransomware activity was steady, accounting for 5% of all observed incidents in 2025. While ransomware made up a smaller share of total incidents, the overall volume increased year-over-year.

This increased volume was paired with a noticeable drop in the variety of tactics, techniques, and procedures (TTPs) used across ransomware groups. Power became concentrated among four major players: Akira, Medusa, Qilin, and Ransomhub, who collectively accounted for over half of all ransomware incidents. Driven by intense competition to outdo each other, these groups and their rivals standardized their operations to create a "common playbook," defined by:

- External payload retrieval through PowerShell-based downloaders
- Active Directory enumeration for internal mapping and target identification
- Use of Bring Your Own Vulnerable Driver (BYOVD) techniques to systematically disable EDR solutions
- Standardized commands to remove shadow copies and modify Windows Defender settings
- Strategic implementation of RMMs to blend in with legitimate IT tooling and aid in specific parts of the attack chain
- Mass adoption of encrypted tunnels such as `cloudflared`, `ngrok`, `FRP`, and `Chisel` to conduct staging and steal files, especially in more professional groups
- Increased evidence of data theft happening before ransomware delivery for extortion or additional sources of financial gain, or might even have been the primary goal in some circumstances

### Average Time-to-Ransom in 2024 and 2025
- **2024**: 17 Hours
- **2025**: 20 Hours

What also stands data-wise is that the time-to-ransom (TTR) in 2025 went up from 17 to 20 hours. Here’s why this likely happened:
- Increased focus on extortion and data theft
- A strategic shift to stealth over speed
- Extended time between initial access and follow-up activity

With fewer server-side vulnerabilities, most ransomware activity in 2025 shifted away from exploit-driven attacks. While the number of ransomware campaigns fluctuated in part due to spikes attributed to known ransomware families, most groups pivoted to alternative methods: using stolen or brute-forced credentials, remote access tools (VPN/RMM), and data bought from infostealers.

Specific surges were occasionally tied to exploits, like Akira’s August campaign targeting SonicWall SSLVPN devices, but these became the exception and not the norm. Groups specializing in exploitation—like Cl0p and Akira—doubled down on their niche expertise for “exploit once, compromise many” strategies that effectively balance hands-on intrusion efforts with exploit development, a luxury that most ransomware groups can’t afford.

![Windows Defender Alerts for Akira ransomware and a correlation rule triggered by multiple AV alerts leading to an AI-assisted, human-led investigation.](Figure 5: Example of Akira ransomware detection)

### Monthly Distribution of Global Ransomware Campaigns

![Monthly distribution of global ransomware campaigns throughout 2025.](Figure 6: Monthly distribution of global ransomware campaigns)

## Ransomware Groups

Ransomware is increasingly concentrated in the hands of a few groups (Akira, Medusa, Qilin, and RansomHub) that run organized and efficient operations with streamlined playbooks.

- **Akira**: 22.2%
- **RansomHub**: 11.2%
- **Qilin**: 9.8%
- **Medusa**: 8.0%
- **LockBit**: 4.2%
- **Play**: 2.7%
- **INC/LYNX**: 2.1%
- **Safepay**: 1.2%
- **Other**: 38.3%

![Most prevalent ransomware groups in 2025 pie chart.](Figure 7: Most prevalent ransomware groups in 2025)

Ransomware activity in 2025 looked surprisingly similar across sectors, as attackers streamlined their playbooks. Major cybercrime partnerships ramped things up through coordinated efforts, as we saw with the merger of Shiny Hunters, Scattered Spider, and Lapsus$ to develop "ShinySp1d3r." Similarly, DragonForce (formed by ex-members of RansomHub) attempted to build a "ransomware cartel" alongside Qilin and LockBit, which resurfaced with LockBit 5.0 despite repeated law enforcement disruptions.

While newer families like Shinobi and Play popped up, a few key groups controlled most of the market. Akira solidified its position as the year's top operator, accounting for nearly a quarter of all observed incidents. Their dominance persisted even as other giants faltered: Black Basta was rocked by a massive leak of over 200,000 internal chat messages that exposed its infrastructure and operations, while BlackSuit (formerly Royal) was dismantled in July following a successful global law enforcement takedown.

> Ransomware groups have largely abandoned novel methods, instead favoring a 'common playbook' of proven attack chains.

Longtime groups had a clear preference for proven attack chains, not novel techniques. In 2025, most relied on the existing and available ransomware ecosystem: initial access brokers for infostealers or credential-theft tools, remote-management abuse, commodity malware loaders, and hands-on-keyboard actions prior to deployment. While brand-new variants like Cephalus, Obscura, and Kawalocker showed up, most incidents were driven by Akira, Medusa, Qilin, and Ransomhub, who accounted for 51% of all ransomware incidents we observed.

### Incidents of Ransomware Groups (2024 vs. 2025)

![Ransomware groups incident frequency comparison between 2024 and 2025.](Figure 8: Ransomware groups incident frequency from 2024 to 2025)

### Ransomware Groups Gains and Losses

| Ransomware Family | 2024 Frequency | 2025 Frequency | Gains and Losses |
| :--- | :--- | :--- | :--- |
| Qilin | 0.00% | 9.82% | +9.82% |
| Akira | 15.80% | 22.25% | +6.45% |
| LockBit | 1.40% | 4.19% | +2.79% |
| Safepay | 0.00% | 1.18% | +1.18% |
| Phobos | 0.00% | 0.28% | +0.28% |
| BianLian | 0.40% | 0.00% | -0.40% |
| Cl0p | 1.20% | 0.00% | -1.20% |
| Medusa | 11.80% | 7.98% | -3.82% |
| BlackSuit | 5.70% | 0.00% | -5.70% |
| Play | 9.10% | 2.75% | -6.35% |
| Black Basta | 7.60% | 0.00% | -7.60% |
| RansomHub | 21.40% | 11.26% | -10.14% |
| INC / LYNX | 16.80% | 2.09% | -14.71% |

Figure 9: Table of ransomware gains and losses 2024 vs. 2025

---

## Common Ransomware Tradecraft in 2025

### NTDS.dit Access via Shadow Copy and Symlink Abuse

For those unfamiliar with NTDS.dit, it’s the main database file for Microsoft Active Directory Domain Services (AD DS). It stores all domain information, including user accounts, group memberships, and hashed passwords. In other words, a playground for ransomware operators.

We consistently saw operators take Active Directory credential material from NTDS.dit without interacting with the live directory database. Attackers routinely accessed offline copies of NTDS.dit through Volume Shadow Copies, avoiding service disruption and reducing the likelihood of detection tied to domain controller instability.

Ransomware campaigns across different families used the same core techniques to move through the attack path, from initial access to domain-wide control. To make this happen, operators frequently abused legitimate Windows utilities that copied files from snapshot contexts, bypassing file locks that normally protect NTDS.dit during runtime. To do this, attackers modified Windows symlink evaluation behavior to weaken default filesystem trust boundaries. These changes allowed paths associated with shadow copy devices to be resolved in contexts normally restricted by Windows security controls and file-system limitation.

### The 2025 Pre-Encryption Workflow
1. **Shadow Copy & Symlink Abuse**
2. **Offline Credential Extraction**
3. **SYSTEM-Level Persistence & Tampering**
4. **Encrypted Tunneling & Staging**
5. **Data Exfiltration & Payload Deployment**

Once symlink protections were relaxed, attackers mapped internal shadow copy device paths into attacker-accessible locations. This exposed protected system files to post-exploitation tooling without needing direct access to the live NTDS database. The technique bridges privilege boundaries between system-level resources and userland tooling, enabling credential material to be copied, parsed, and exfiltrated with minimal operational noise.

After acquisition, NTDS.dit was used as the foundation for credential-driven expansion. It’s a known strategy, but this year, we saw it used by several small ransomware groups who had been using `ntsdutil`, `impacket`, `reg save`, or similar easily detected methods to carry out these attacks.

Operators extracted domain password hashes offline, performed Kerberoasting against service accounts, and reused credentials via pass-the-hash and pass-the-ticket techniques. These credentials were then used to escalate privileges and move laterally across the environment. In practice, this workflow cuts down the time needed to achieve domain-wide access and eliminated many traditional detection opportunities tied to interactive credential dumping.

### Security Control Tampering as a Preparatory Phase

Defense evasion activity observed in 2025 was deliberate, not incidental. Ransomware operators like Akira, Medusa, and DragonForce routinely used installed security products early in the intrusion to inform follow-on actions. This reconnaissance guided attackers’ targeted tampering efforts to reduce visibility and response effectiveness.

Operators frequently changed security configurations, introduced process or path exclusions, suppressed logging, and cleared event data to limit forensic traceability. In more advanced cases, we saw attackers abuse or deploy kernel drivers to bypass user-mode protections entirely. These actions weren’t used to immediately disable security tooling, but to degrade detection long enough to allow staging, credential harvesting, and encryption preparation to proceed uninterrupted.

### Expanded Use of Encrypted Tunnels

In 2025, ransomware operators used more mature tradecraft by favoring resilient, legitimate tunneling and exfiltration tools over custom malware. `Cloudflared` emerged as the main tunneling mechanism, seeing big spikes in July and August that aligned with surges in "hands-on-keyboard" activity. For data theft, `Rclone` was still the most consistent and scalable exfiltration utility, especially during late summer and fall as campaigns shifted toward bulk data theft and extortion.

While SSH remains a staple with attackers, tools like `FRP` and `Chisel` appeared selectively, suggesting specialized use by specific threat actors. At the same time, brief upticks in WinSCP and Mega Cloud Sync suggest opportunistic, operator-driven file theft once privileged access was established. All together, these trends highlight a growing use of encrypted tunnels among ransomware groups, most notably Akira, Medusa, and LockBit, to blend into legitimate network traffic, maximize throughput, and quietly exfiltrate data at scale before extortion.

> Ransomware crews stepped up their game by leaning on legit, resilient tools for tunneling and data theft. Groups like Akira, Medusa, and LockBit increasingly hid inside encrypted, normal-looking traffic to quietly steal data before making their demands.

![Monthly breakdown of tunneling and exfiltration methods linked to ransomware activity.](Figure 10: Monthly breakdown of tunneling and exfiltration methods linked to ransomware activity)

---

## Time-to-Ransom (TTR) Measurement

Last year, we introduced TTR, a specialized metric for the average time it takes ransomware operators to move from initial access to ransomware deployment. By investigating incidents where ransomware is deployed and analyzing activity logs, we determine the initial access time and attribute it to specific groups based on the attempted delivery of a ransomware note. This calculation is influenced by several critical variables, including where and how a ransomware operator gains initial access, level of network isolation in the environment, value of victim data and need for exfiltration, and more.

TTR helps shape our knowledge of operator maturity, intrusion complexity, and the operational workload required for successful attacks. For businesses, this metric also helps build knowledge for the average time to spot and mitigate ransomware threats based on real-world trends.

In 2024, our findings revealed an average TTR of approximately 17 hours, with "smash-and-grab" groups like Play, RansomHub, and Akira often deploying ransomware in less than seven hours.

By contrast, this year’s data shows the average TTR increased to approximately 20 hours. We believe this trend is driven by several critical shifts and factors in attacker behavior:

- **Prioritizing Extortion and Data Theft**: Attackers are shifting toward extortion operations, with more time spent on spotting and exfiltrating data. We often see exfiltration as the final step, happening within the last six hours of a ransomware incident. The three most common exfiltration methods are Archive tools (Zip/Rar), Encrypted Tunnel Relays (`Cloudflared`, `SSH`, `Ngrok`, and `FRP`), and FTP/Secure FTP (`Filezilla`, `FTP.exe`, `WinSCP`).
- **Operational Handoffs and Workloads**: We’re seeing longer "pauses" in activity that likely signal slower handoffs from initial access brokers and affiliates to ransomware operators. As groups take on larger workloads, the time between initial access and follow-up activity is longer.
- **Stealth Over Speed**: Attackers prioritize "low and slow" methods over the high-velocity "smash-and-grab" tactics of previous years. Manual, multi-step techniques—like the NTDS.dit exploit—show how operators do more prep work to stay under the radar.

![Average time-to-ransom (TTR) by ransomware group in 2024 vs. 2025.](Figure 11: Average time-to-ransom (TTR) by ransomware group in 2024 vs. 2025)

Notably, telemetry from our Identity Threat Detection and Response (ITDR) solution flagged a critical "pre-access" window, where precursor activity like account verification via stolen credentials from VPNs or data centers happens days or weeks before ransomware. Around 17% of ransomware incidents showed ITDR-related precursor activity at least seven days prior to deployment, a figure that climbed to nearly 21% when expanded to a 14-day window. This pattern suggests that infostealer operators or initial access brokers validate credentials so they don’t go inactive/cold before high-velocity ransomware events go down.

The increase in average TTR reflects a strategic tactical move in how ransomware operators manage their intrusion timelines that suggests many groups are now prioritizing thorough data exfiltration and stealthy, manual techniques over the sheer velocity of "smash-and-grab" attacks. While the window for detection has widened, it’s defined by "low and slow" activity and deliberate operational pauses.

For defenders, these findings highlight how important it is to spot late-stage indicators like encrypted tunnels or archive tools before the final deployment.

---

## Mapping Ransomware Attack Paths With Initial Access Data

To understand these timelines, it is important to distinguish between two metrics:
- **Time-to-ransom (TTR)** measures the duration from initial access to the final deployment (or attempted deployment) of the ransomware payload.
- **Time to ransomware activity** tracks the window from initial access to the first sign of malicious behavior, like lateral movement or credential harvesting.

By focusing on the time to first activity versus just the final deployment, we can more accurately convey the true agility of these operators, and the narrow intervention window before an attack reaches its destructive final stage.

One of the biggest variables impacting TTR is initial access. This vector largely sets the stage for how efficiently ransomware operators execute attacks. Depending on how an operator compromises a system, they’ll have a shorter TTR in the targeted environment, significantly decreasing detection time for defenders.

To illustrate how these timelines vary, we analyzed three common initial access methods: RATs, RMM tools, and ClickFix scams. We then measured the time from the initial compromise to ransomware activity, or attempted activity, within a 48-hour window.

![Encrypted file sample from Obscura ransomware.](Figure 12: Encrypted file sample from Obscura ransomware)

### RATs

#### RAT Detection as a "Late-Stage" Warning
Because most ransomware activity starts within 12 hours of a RAT install, these detections are emergency signals that an environment is already compromised and prepared for impact.

#### Variant-Specific Urgency
Certain families—specifically RevengeRAT, STRRAT, and XWorm—are precursors to imminent ransomware activity and require the same immediate response as the ransomware itself.

#### Strategic Redundancy & Exfiltration
Attackers often deploy RATs late in an operation so they have a persistent backup if ransomware deployment is interrupted, or for final data exfiltration before "going loud."

The time between RAT installation and ransomware activity follows a highly compressed timeline. In cases where a RAT was the initial access vector, 25% escalated to ransomware activity within the same hour, and more than 50% did so within 12 hours. AsyncRAT is the most prominent catalyst for these handoffs, with one-third of ransomware activity happening within minutes of installation, a clear sign of immediate monetization.

Depending on the family, these tools signal different behaviors: Jupyter RAT often indicates methodical "hands-on-keyboard" activity, while Remcos is typically deployed after gaining privileged privileges near the end of an operation. These deployments frequently serve as a final hand-off point, a redundant communication channel, or a tool for data exfiltration, particularly for groups without other specialized exfiltration methods. Regardless of the variant, a RAT suggests an attacker has already completed extensive environmental prep, leaving a narrow window for defensive intervention.

![Time to ransomware activity within 48 hours of RAT install.](Figure 13: Time to ransomware activity within 48 hours of RAT install)

---

### RMM Execution

Unlike the highly compressed and uniform timelines we saw with RATs, the transition from RMM execution to ransomware activity is notably varied. We identified three distinct operator workflows categorized by their timing and tool choice, and these strategies suggest that choosing an RMM for initial access is rarely random. It’s a tactical reflection of the attacker’s immediate goals, ranging from immediate execution to methodical multi-stage operations.

- **0–8 Hours (Near-Immediate Conversions)**: Ransomware activity that occurs within eight hours of RMM execution tends to be attackers who already have credentials, reconnaissance intelligence, and pre-staged executions planned. RMMs like RustDesk and various VNC iterations show the highest urgency, with 50% of ransomware activity happening within the first hour of RustDesk abuse. Atera follows a similar high-velocity pattern, with 75% of ransomware activity in under two hours, with a secondary peak of activity (~10%) between the six and eight hour marks. In these scenarios, the RMM is likely used as a safety net to ensure encryption delivery or as a specialized channel for late-stage data exfiltration.
- **8–12 Hours (Mid-Window Execution)**: This group aligns with human-operated cadences, where the RMM is used for "hands-on-keyboard" lateral movement or near-endgame staging. This timing is consistent with fast-operating ransomware groups, who migrate to their ransomware toolkits only after confirming they’ve landed on high-value targets. Tools like MeshCentral and PDQConnect typically see ransomware deployment between eight and twelve hours post-installation, suggesting the RMM is being used mid-operation to broaden environmental control and perform final defense evasions before "going loud."
- **12+ Hours (Initial Access & Reseller Gaps)**: The longest lead times are associated with larger, traditional RMM platforms, suggesting a multi-stage operation or a change in ownership. ScreenConnect and SimpleHelp have the longest dwell times, ranging from 18 to 32 hours, with SimpleHelp showing unique activity spikes at the 24-hour mark. AnyDesk displays a bifurcated strategy, where activity happens either immediately or after a distinct 48-hour delay. These extended gaps are hallmarks of Initial Access Broker (IAB) activity, where the ransomware group is the purchaser or the secondary phase of the operation. Furthermore, immediate deployments following these specific RMMs can be an indicator of successful bribing or insider threats, where the attacker bypasses the reconnaissance phase due to pre-existing knowledge or access.

![Time to ransomware activity within 48 hours of RMM execution.](Figure 14: Time to ransomware activity within 48 hours of RMM execution)

---

### ClickFix Scams

ClickFix scams have become an initial access vector of choice for threat actors looking to exploit the human psyche, evade defenses, and target multiple platforms. These attacks trick users into unknowingly executing arbitrary commands, like PowerShell scripts or terminal instructions, under the guise of a legit authentication or troubleshooting process. The fake CAPTCHA lure, which makes users go through manual steps to "verify" they’re human, has emerged as a common variation of this technique. Notably, our analysis found that fake CAPTCHA lures exhibit a markedly different time to ransomware activity compared to general ClickFix attacks, revealing two distinct operational strategies:

- **ClickFix (Rapid Deployment)**: Timing data shows ClickFix campaigns are built for speed, with ransomware activity kicking off almost immediately after infection. Smaller spikes 16–20 hours later suggest some access is handed off or sold to specialized ransomware operators rather than used right away.
- **Fake CAPTCHA (Broker Model)**: Shows a more distributed timeline with only 7% of ransomware activity starting within the first hour. The majority of handoffs happen between 6 and 16 hours, consistent with a model where system information is harvested and validated before being resold on the dark web.

While both methods had limited direct involvement in ransomware activities, with only 4% of ClickFix events and 6% of fake CAPTCHA events leading to ransomware, the sheer volume of these attacks makes them a serious threat. Even if ransomware isn't the immediate goal, if left unchecked, these threats can lead to the installation of infostealers, credential theft, or other malicious activity. Both should be treated with fast responses and threat hunting teams should look for signs of credential theft, secondary payloads, and lateral movement that typically happen with these attacks.

![Example of a ClickFix human verification lure.](Figure 15: Example of a ClickFix human verification lure)

![Time to ransomware activity within 48 hours of ClickFix and fake CAPTCHA events.](Figure 16: Time to ransomware activity within 48 hours of ClickFix and fake CAPTCHA events)

---

<div id="section-attacker-tools-and-techniques"></div>

# Attacker Tools and Techniques

## Hacking Tools

When attackers compromise systems at scale, speed and automation are key. Threat actors use hacking tools to carry out fast, complex actions within a short window of intrusion opportunity. These tools bundle advanced capabilities like credential harvesting, memory dumping, password cracking, network discovery, lateral movement, persistence, installation, and remote C2 into streamlined workflows without a lot of effort.

Modern attackers often combine purpose-built offensive tooling with legitimate administrative and diagnostic software, abusing trusted binaries to blend into normal system activity. Common examples include the Sysinternals Suite, network scanners, and PowerShell-based frameworks.

A noticeable trend in 2025 is the growing replacement of traditional hacking frameworks with abused RMM tools for command-and-control, persistence, and lateral movement. With detection of traditional hacking tools improving, RMM abuse is becoming popular for maintaining access and control in post-compromise environments, since these platforms are already trusted.

### Hacking Tools Usage
- **Mimikatz**: 28.0%
- **Atomic Red Team**: 21.7%
- **Sysinternals**: 11.9%
- **Hack Tool, Other**: 7.1%
- **Metasploit**: 7.1%
- **Cobalt Strike**: 6.7%
- **PowerSploit**: 6.6%
- **Advanced IP Scanner**: 3.9%
- **BloodHound/SharpHound**: 3.4%
- **Impacket**: 1.5%
- **Rubeus**: 0.8%

![Distribution of hacking tools used in 2025.](Figure 17: Distribution of hacking tools used in 2025)

In 2025, Mimikatz, a well-known, open-source post-exploitation tool used to extract credentials from Windows systems, was the most frequently observed hacking tool by event volume, accounting for 28% of all hacking-tool detections. Originally created as a proof-of-concept to show weak spots in Windows authentication, Mimikatz has become a popular dual-use tool that can pull plaintext passwords, hashes, Kerberos tickets, and other sensitive credentials from system memory.

Despite being more than a decade old, Mimikatz remains central to credential-theft operations. It’s commonly executed via direct payloads, through PowerShell scripts, or embedded within larger malware frameworks. The continued prevalence of Mimikatz highlights the lasting value of credential access in post-compromise activity and its deep integration into modern intrusion and ransomware campaigns from groups like Akira and Play.

### Mimikatz Attack Techniques
- **Pass the Hash**: Attackers steal NTLM hashes to authenticate to systems without needing plaintext passwords, gaining access even if credentials are encrypted.
- **Pass the Ticket**: This technique uses captured Kerberos tickets to impersonate legitimate users and authenticate to other systems across the network.
- **Kerberos Golden Ticket**: One of the most critical attacks where an operator forges a Ticket Granting Ticket (TGT) for a Domain Admin, granting unrestricted and persistent control over the entire network.
- **Overpass the Hash**: An advanced method that converts stolen NTLM hashes into Kerberos tickets, allowing attackers to bypass standard authentication mechanisms.
- **DC Sync Attack**: A stealthy method where Mimikatz mimics a Domain Controller to trick the environment into replicating sensitive data, including admin password hashes.

Atomic Red Team, an open-source framework that does small, focused tests to emulate adversary behavior, accounted for 21.7% of hacking-tool detections in 2025. Repeated test executions drove this volume and automated emulation workflows. Although Atomic Red Team is most commonly used for defensive testing and purple-team activities, its activity is indistinguishable from real adversary behavior at the telemetry level. Because of this, its frequent appearance in detection data reinforces how important context and analyst validation is when interpreting its presence in an environment.

Sysinternals tools, a collection of free monitoring and troubleshooting utilities from Microsoft, accounted for 11.9% of detections, underscoring continued abuse of legitimate administrative tools for malicious purposes. We saw threat actors using tools like ProcDump, PsExec, and related binaries for credential dumping, remote execution, and reconnaissance, letting attackers operate under the guise of normal system administration.

Cobalt Strike, while still an important tool in adversary tradecraft, represented a smaller share of total events in 2025 (6.7%) compared to previous years. It appears Cobalt Strike users shifted toward tools like Atomic Red Team, PowerSploit, BloodHound, or, in some cases, legitimate RMM tools. Despite this decline in event volume, Cobalt Strike is still one of the most operationally significant frameworks, widely used by both cybercriminals and advanced threat groups because of its mature command-and-control (C2) capabilities and flexibility. Known APT groups, including Ocean Lotus, APT31, Cinnamon Tempest, and Wizard Spider, use Cobalt Strike to blend malicious activity with legitimate red-team behavior for plausible deniability.

Other notable tools observed in 2025 include Metasploit (7.1%), PowerSploit (6.6%), Advanced IP Scanner (3.9%), and BloodHound / SharpHound (3.4%), each playing specific roles in exploitation, credential access, and Active Directory reconnaissance. Frameworks like Empire, Impacket, Rubeus, and CrackMapExec appeared less frequently by volume, but are still impactful due to their targeted use in lateral movement and domain compromise operations.

![Distribution of hacking tools used in 2024 vs. 2025.](Figure 18: Distribution of hacking tools used in 2024 vs. 2025)

---

## Malware Loader Activity

### Top Malware Loader Families
- **ClickFix**: 53.2%
- **SocGholish**: 24.1%
- **TrickBot**: 5.8%
- **Emotet**: 5.6%
- **Gootloader**: 3.0%
- **Bumblebee**: 2.9%
- **QakBot**: 2.8%
- **IcedID**: 0.9%
- **DarkGate**: 0.9%
- **HijackLoader**: 0.8%

![Distribution of malware loader families.](Figure 19: Distribution of malware loader families)

Thanks to international law enforcement, the malware ecosystem took a few solid hits this year. Operation Endgame targeted major loader families like Qakbot, Bumblebee, and Trickbot. But malware loaders didn’t disappear in 2025.

Malware loaders are usually small components—often PowerShell, JavaScript, or other natively supported scripting languages—that send back environmental information to the attacker, set a specific flag or key, and then download additional malware components onto the victim's computer. While all malware loaders are designed to gain initial access and drop secondary payloads, our telemetry shows that some are also used as a stealthy way to launch additional tooling at later stages throughout the attack path, often going unnoticed by victims. In some cases, threat actors remove loaders once they’ve done their job to minimize their attack footprint in the targeted environment.

Loaders can be diverse in terms of operational functionality. Some are rented or purchased by one group to give access to another group. We’ve also seen loaders get delivered pre-infected by another group's malware, and then hijack existing infections with their own malware later in the compromise phase.

### ClickFix: The ‘Human-Operated’ Attack Chain
- **Exploit User Trust** ➔ Instruction-Based Social Engineering Abuses (rely on exploiting user trust rather than vulnerabilities)
- **Manual User Execution** ➔ Users Copy/Paste Commands (Abuses LOLbins like PowerShell and MSHTA, looking like normal admin or user activity)
- **Staged Payload Delivery** ➔ Fast-Moving Secondary Payloads (Infostealers, RATs, and Ransomware precursors)

In 2025, malware authors doubled down on adding more innovative defense evasion, stealth techniques, and obfuscation into their malware variants, like Gootloader using custom WOFF2 fonts with glyph substitution for filenames.

Most malicious loader activity centers around user interaction abuse, deceptive execution chains, and staged payload delivery. This reflects a continued shift by threat actors toward techniques that reduce reliance on exploits and instead leverage trust, familiarity, and built-in operating system capabilities.

ClickFix emerged as the main malware loader delivery mechanism, representing over half (53.2%) of all observed loader executions. ClickFix campaigns are characterized by highly repeatable social-engineering workflows that instruct users to manually copy and execute commands, most often through PowerShell, MSHTA, or LOLBins. These campaigns are particularly effective because they rely on exploiting user trust (rather than vulnerabilities) and look like normal administrative or user activity.

Like we saw in 2024, SocGholish, a malware framework that uses social engineering to trick users into downloading infected updates, is a major initial access vector. This year, it accounted for 24.1% of all malware loader and initial access behavior. It’s typically associated with fake update themes and drive-by delivery mechanisms, often executed through JavaScript or browser-assisted execution chains. Its persistence highlights the ongoing effectiveness of compromised web infrastructure and malicious advertising as a scalable infection vector, particularly against environments with permissive browser execution policies.

QakBot (2.8%), Emotet (5.6%), and Gootloader (3%) might be lower in volume this year, but they’re clear red flags for fast moving secondary malware payloads, including RATs, credential stealers, and ransomware precursors. Compared to SocGholish, for example, these loader families are a clear sign of a more deliberate attack path following initial access: staged execution, discovery, and lateral movement.

> Think of loaders as a prime opportunity to interrupt an attack. By proactively identifying and neutralizing them, defenders can stop an intrusion in its tracks. It’s a vital step for securing your environment.

![Top malware loader percentage by month showing trends for Bumblebee, Clickfix, DarkGate, Emotet, Gootloader, HijackLoader, IcedID, QakBot, SOCGholish, and TrickBot.](Figure 20: Top malware loader percentage by month)

---

10 2025-11 2025-12
Figure 20: Monthly distribution of malware loader families in 2025
22002266 CCyybbeerr
TThhrreeaatt RReeppoorrtt Attacker Tools and Techniques 36

Remote Access
Common RATs in 2025
Trojans (RATs) 0% 10% 20% 30% 40% 50% 60%
AsyncRAT
58.08
BitRAT
17.2
GhostRAT
6.35
RATs disguise themselves as legitimate or harmless files or applications to trick
Jupyter RAT
5.46
a user into installing and downloading them, giving the attacker control over
the infected device. RAT activity in our 2025 telemetry data reflects a post-
initial access phase of compromise, where attackers transition from delivery Adwind / jRAT 5.17
and staging into persistent control, reconnaissance, credential access, and
lateral movement. Unlike malware loaders, RATs represent an explicit intent to
Remcos
3.1
maintain interactive access to endpoints, and often serve as the operational
backbone for longer-lived intrusions.
STRRAT
1.11
NanoCore 0.96
50%
With over of RAT activity, AsyncRAT led
XWorm
0.96
the pack in 2025. It frequently sets the stage for
ransomware and has become a staple in enterprise
NjRAT
0.81
intrusion playbooks.
QuasarRAT
0.37
RevengeRAT
0.22
PlugX
0.22
Figure 21: Distribution of RATs
2026 Cyber
Threat Report Attacker Tools and Techniques 37

|     | RAT(s) | Primary Role | Key Activity |     |     |
| --- | ------ | ------------ | ------------ | --- | --- |
Most prevalent RAT family of 2025, thanks to its
accessibility, extensibility, and wide adoption. It’s
typically executed as managed .NET binaries staged
from user-writable directories and used to establish a
|     |     | Foundational  | persistent foothold, execute interactive commands,  |     |     |
| --- | --- | ------------- | --------------------------------------------------- | --- | --- |
AsyncRAT
|     |     | Access Enabler | transfer files for payload staging, and conduct initial  |     |     |
| --- | --- | -------------- | -------------------------------------------------------- | --- | --- |
credential harvesting and reconnaissance. It frequently
precedes ransomware activity in structured intrusion
playbooks and has become a foundational access tool
In 2025, cybercriminals relied on less than 10 malware families for most RAT
in enterprise ransomware operations.
deployments, with execution patterns strongly aligned to loader activity
observed elsewhere in the telemetry. In many cases, RAT execution
Used less than AsyncRAT but is operationally significant
happens shortly after initial access loaders like ClickFix, SocGholish, or
due to its focus on stealth and persistence. Technical
similar delivery mechanisms, reinforcing the modular attack life cycle we
activity is characterized by obfuscated execution
saw throughout 2025.

|     |     | Stealth and  | parameters, non-standard parent/child process  |     |     |
| --- | --- | ------------ | ---------------------------------------------- | --- | --- |
BitRAT & GhostRAT
|     |     | Persistence | relationships, and deliberate attempts to blend into  |     |     |
| --- | --- | ----------- | ----------------------------------------------------- | --- | --- |
legitimate application execution paths. Their presence
RAT execution is rarely isolated. Instead, it’s most often observed:
typically indicates a more deliberate intrusion phase
rather than mass commodity activity.
Following loader execution, sometimes within minutes or hours
This year, a variant of Jupyter was notable for using
Python runtimes or embedded interpreters to move
across networks where Python exists. This can evade
|     |     | Evasive Scripting  | detection due to their script-based nature and quickly  |     |     |
| --- | --- | ------------------ | ------------------------------------------------------- | --- | --- |
As part of a multi-stage execution chain
|     | Jupyter & Python- | Framework    | introduce functionality and modular capabilities. Activity  |     |     |
| --- | ----------------- | ------------ | ----------------------------------------------------------- | --- | --- |
|     | Based RATs        | Targeting    | often overlaps with generic RAT and infostealer             |     |     |
|     |                   | Browser Info | heuristics, as they target browser credentials and          |     |     |
cryptowallets.  This particular variant was frequently
On systems that subsequently exhibit discovery, credential access, or  deployed in environments where scripting execution is
privilege escalation behavior common to reduce the operational footprint.
Used in targeted or semi-targeted campaigns, these
This attack sequencing shows that RATs aren’t the entry point—they’re the
families are typically used in affiliate-driven
ransomware ecosystems where operators prioritize
control mechanism used after initial access is secured.
rapid deployment and broad compatibility. Remcos
occupies a niche between commodity RATs and
|     | Remcos, STRRAT, &  | Ransomware  |     |     |     |
| --- | ------------------ | ----------- | --- | --- | --- |
advanced frameworks, used to establish persistence,
|     | NjRAT | Affiliate Workflow |     |     |     |
| --- | ----- | ------------------ | --- | --- | --- |
conduct reconnaissance, and stage payloads before
moving to ransomware execution. Activity is followed
by delivery/staging and impact-oriented behavior,
aligning with ransomware workflows rather than
espionage.
Figure 22: Breakdown of most common RAT activity observed in 2025
2026 Cyber
| Threat Report |     |     |     | Attacker Tools and Techniques | 38  |
| ------------- | --- | --- | --- | ----------------------------- | --- |

Types of Malicious Activity % by RAT Family
Collection Credential Access Defense Evasion Delivery / Staging Discovery / Recon Exfiltration Impact / Disruption
Interactive Control & Scripting Lateral Movement & C2 Persistence Privilege Escalation RAT Session Management Ransomware
0% 10% 20% 30% 40% 50% 60% 70% 80% 90% 100%
Adwind / jRAT
AsyncRAT
BitRAT
Generic RAT
GhostRAT
Jupyter RAT
NanoCore
NjRAT
QuasarRAT
Remcos
RevengeRAT
STRRAT
XWorm
Figure 23: Distribution of malicious activity following RAT installation

2026 Cyber
Threat Report Attacker Tools and Techniques 39

RMM Abuse
2026 Cyber
Threat Report

RMMs are Hackers'
New Favorite Weapon
RMM solutions have emerged as hackers' new
+277% favorite weapon, offering stealth, persistence, and
operational efficiency. Because they’re legitimate
tools, their activity can look completely normal,
making malicious use harder to spot. As a result, Instead of running their own
we've seen a surge in RMM abuse over the past
malware to conduct C2
year, with the threat now accounting for 24% of all
functions, attackers have
incidents observed at Huntress.
moved to using legitimate
2025
RMM abuse has evolved beyond opportunistic
RMM solutions that offer an
usage into a deliberate, standardized intrusion
interactive console, HOK
strategy. As cybercriminals built entire playbooks
around these tools to drop malware, steal access, and all the features
2024 credentials, and execute commands, the use of
and functionality they could
traditional hacking tools plummeted by 53%, while
RATs and malicious scripts dropped by 20% and want.
Attackers are ditching traditional 11.7%, respectively.
hacking tools and abusing trusted
This shift reflects a broader pivot in the threat
software that blends into normal landscape, where attackers are increasingly “living Robert Knapp
off the land” and weaponizing the same Director, Security Operations Center
business workflows—RMM abuse
applications, tools, and solutions businesses use for
alone is up 277% year over year.
day-to-day operations.
2026 Cyber
Threat Report Defense Evasion 41

RMM Techniques
and Tool Analysis
In 2025, RMM tools transitioned from simple initial access points to dominant post-
access channels. Our analysis throughout the year consistently showed that once Consolidated C2
an RMM agent is established, the use of traditional malware becomes notably
Once deployed, RMM tooling often became the only interactive access method, with outbound network
rare. This highlights a deliberate shift in which adversaries swap short-lived
noise decreasing, as operators used RMMs to issue commands, transfer tooling, and orchestrate follow-
implants for legitimate management tooling to sustain access and reduce their
on actions.
footprint.
Rather than deploying custom backdoors, attackers now leverage RMMs as a
unified control hub for the following:
Execution via LOLBins
There is a high correlation between RMM sessions and the execution of native Windows utilities (e.g.,
PowerShell, msiexec, rundll32, certutil). This indicates hackers mainly used RMMs to "live off
the land" and execute native tooling rather than introduce new binaries.
Attack Path Redundancy
Attackers often installed two or more RMM agents during a single intrusion. This gave them a "fail-safe"
persistence method, ensuring that if one tool was detected and removed, persistent access was
maintained through the second.
2026 Cyber
Threat Report Defense Evasion 42

Throughout the year, malicious tradecraft consistently followed suspicious
RMM executions, with each major RMM platform highlighting a unique
Adjacent Malicious Activity by RMM Tool
blend of attacker behaviors. Attackers strategically chose specific RMM
(24 Hours Post-Compromise)
platforms based on their operational objectives and the stage of their
intrusion. A detailed analysis of non-RMM activity within a 24-hour window
of suspicious RMM execution revealed distinct behavioral patterns from
Exfiltration Defense Evasion Lateral Movement Ransomware
each major tool.

Delivery / Staging Discovery / Recon Credential access Other malicious activity
These findings highlight how hackers strategically weaponize specific
RMM tools during certain phases of the attack lifecycle:

0% 10% 20% 30% 40% 50% 60% 70% 80% 90% 100%
ScreenConnect sets up orchestration and credential harvesting

ScreenConnect
NetSupport speeds up staging

AnyDesk and Atera align with ransomware execution

Splashtop supports credential-driven lateral expansion

NetSupport
PDQConnect is an initial delivery bridge

AnyDesk
When correlated with 24 hour post-infection tradecraft, RMM telemetry
shows a high-confidence signal of where an intrusion is headed in the
attack path, not just the one in progress.
Atera
SplashTop
50%
Over of activity following suspicious
PDQConnect
Atera instances ties to ransomware, highlighting
its role in late-stage abuse. It usually shows up
Figure 24: Adjacent malicious activity by RMM tool within 24 hours of RMM execution
during active ransomware and extortion efforts.
2026 Cyber
Threat Report RMM Abuse in 2025 43

Primary Operational
Tool Key Activity
Role During Attack
Most often used to stabilize access, contain defenses, harvest credentials, and
General Purpose
ScreenConnect coordinate movement before or alongside impact versus trigger encryption right
Post-Access
away.
Mainly used for delivery and staging, far exceeding any other RMM observed in this
Early category. Frequently abused during the early operationalization phase, where
NetSupport
Operationalization attackers move from initial access into active execution and tool deployment. Rarely
the final control mechanism during impact.
AnyDesk and smaller
DWAgent, Chrome Stabilization & Commonly introduced during stabilization and pre-encryption phases, where attackers
Remote, and Pre-Encryption reinforce access, validate credentials, and prep the environment for extortion.
ZohoAssist
More than half of activity following a suspicious Atera execution is ransomware-
related, with the RMM exhibiting the clearest late-stage abuse profile. Rarely used
Atera Late-Stage Impact
for initial access or staging and instead appears once attackers are actively
executing ransomware and extortion operations.
Lateral Often used to harvest credentials and pivot internally, rather than to directly
Splashtop
Expansion facilitate encryption events.
Majority of activity is tied to delivery and staging. Frequently used as a transitional
Initial Delivery
PDQConnect mechanism to introduce other RMM tooling before attackers pivot to RMM platforms
Bridge
better suited for sustained control and impact.
Figure 25: Breakdown of adjacent malicious activity within 24 hours of RMM activity by tool
2026 Cyber
Threat Report RMM Abuse in 2025 44

While RMM abuse patterns vary by tool, we observed three core techniques
that remain consistent across all platforms. These methods exploit the
Suspicious RMM Tool
inherent trust granted to administrative tools, letting attackers execute
Installation
commands and move files under the guise of authorized maintenance. By
focusing on these shared behaviors, rather than specific tool techniques,
defenders can more accurately distinguish malicious activity from routine
system management.
Direct File Drop and Execution
RMM sessions were used to transfer and execute payloads directly on endpoints, often via built-in file
transfer mechanisms or native Windows utilities. Payloads included secondary tools, scripts, and
persistence components.
Remote PowerShell Sessions
PowerShell execution over RMM channels was common, enabling script-based discovery, defense
evasion, and follow-on tooling deployment. These sessions frequently leveraged encoded or
obfuscated commands to blend with legitimate administrative activity.
Lateral Movement Through Internal RMM Consoles
In environments where RMM platforms were already deployed internally, adversaries abused existing
consoles to pivot laterally. This included using trusted RMM infrastructure to access additional hosts
without introducing new external connections, significantly reducing detection opportunities.
Figure 26: An attacker gained persistence with RMM installation
2026 Cyber
Threat Report RMM Abuse in 2025 45

Redefining Defense in
the Era of RMM Abuse
The evolution of RMM abuse in 2025 highlights a critical challenge for defenders: Organizations can stay ahead of this threat by:
adversaries are increasingly aligning their operations with legitimate
administrative behavior. By mimicking routine IT workflows, leveraging trusted
management tools, and minimizing the use of distinct malware artifacts, attackers
Treating unexpected RMM installations as Applying the latest security patches to
are blurring the lines between malicious and authorized activity. Defenders should high-confidence signs of compromise close the gap on vulnerabilities
expect this pattern to continue.
As long as RMMs are easy to deploy and tough to differentiate from authorized
Using security awareness training to
activity, they will be an attractive vector for both initial access brokers and Reviewing logs regularly to detect
teach employees to quickly spot and
suspicious or unauthorized RMM activity
financially motivated threat groups. Attackers are also tailoring their use of
report shady lures
specific RMM platforms to align with distinct operational goals. This deliberate
selection of RMM tools based on their unique capabilities and the stage of an
intrusion highlights the sophistication of modern attacker tradecraft.

Restricting external connections from
Enforcing MFA on all RMM platforms
atypical geographies or infrastructure.
and accounts
Detection strategies that rely solely on malware signatures or traditional Enforce IP allow lists where supported.
indicators of compromise are no longer sufficient. Effective defense requires a shift
toward behavioral detection, focusing on anomalous RMM usage, execution
patterns, and deviations from established administrative baselines. Organizations Routinely auditing and monitoring remote Locking down new RMM agent
access tools to maintain an up-to-date enrollment with approval workflows
must treat RMM telemetry as a high-confidence signal of potential compromise,
inventory of approved RMM solutions and device validation
especially when correlated with adjacent suspicious activity.
2026 Cyber
Threat Report Defense Evasion 46

Exploit-Driven
Campaigns
2026 Cyber
Threat Report

SonicWall
SonicWall Exploitation in 2025
Exploitation
0% 10% 20% 30% 40% 50%
Jan 0.53
(CVE-2024-40766)
Feb
1.07
March 2.67
A huge wave of exploit-driven incidents we saw this year was threat
April 0.53
actors targeting an improper access control flaw (CVE-2024-40766) in
SonicWall SSLVPN devices. SonicWall noted this 2024 vulnerability
May 5.88
stemmed from firewall migrations from sixth to seventh generation,
where local user passwords were carried over without being reset. In
the activity that spiked between July and August, attackers exploited
June 3.74
flaws in SonicWall to gain administrative access, move laterally, steal
credentials, disable security defenses, and deploy Akira ransomware.
July 4.81
With no evidence of password spraying or invalid login tactics,
attackers had authentication bypass, stolen credentials, or previously
undetected systems access.
August 19.79
Our analysis of SonicWall post-exploitation activity since August shows
attackers create interactive access, not fully automated follow up Sept 21.92
payload deployment. About 51% of behavior we looked at immediately
following compromise consisted of profile and interactive user
Oct 18.18
initialization artifacts. Beyond these actions, roughly 20% of follow-up
events pointed to clear hands-on-keyboard activity, including manual
command execution, system domain discovery, privilege elevation, and Nov 13.37
direct inspection of logs, security settings, and file contents.
Dec 7.49
Figure 27: Monthly breakdown of SonicWall Exploitation
2026 Cyber
Threat Report Exploit-Driven Campaigns In 2025 48

We saw secondary exploitation, lateral movement, and persistence Types of SonicWall Post-Exploitation Activity
characterized by NTDS extraction, SMB share mapping and migration,
firewall and service manipulation, and defense tool tampering. These
actions align with vetted playbooks used by professional ransomware
0% 20% 40% 60% 80% 100%
groups like Akira and other sophisticated attackers deploying mass
Profile / User Initialization 50.92
domain compromises.
Overall, SonicWall exploitation in 2025 was a key entry point for Other (Residual) 16.12
deliberate operator-led intrusions. Attackers showed restraint and
skillful intent, validating access with careful selection, swift lateral Command Execution 6.59
movement, and highly effective privilege elevation actions.
Lateral Movement / Staging 4.76
Privilege & Access Validation 4.76
Recon / Environment Discovery 4.4
Network Scanning / Validation 2.93
Security Control Verification 2.56
Defense Tampering 2.2
Credential Access 1.83
RDP Access / Enablement 1.47
File System Prep / Staging 1.47
Interactive Operator Activity 1.83
LOLBIN Payload Execution 1.83
File System Manipulation 1.83
Figure 28: Distribution of SonicWall post-exploitation activity
2026 Cyber
Threat Report Exploit-Driven Campaigns In 2025 49

 Top Binary Executables Used in
SonicWall Post-Exploitation
20%
16%
10.99
|     | 12% |     |     |     |     |     | 8.79 |     |     | 8.79 |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ---- | --- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
8.43
8.06
|     |     |     |     |     |     |     |     |     |     |     |     |     |     |     | 7.69 |     |     | 7.69 |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- | --- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
8%
3.66
3.30
4%
2.20
|     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     | 1.83 |     | 1.83 |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- | --- | ---- | --- | --- |
0%
|     |     |     | e   |     |     | e   |     |     | e   |     |     | e   |     | e    | e t |     |     | e   |     |      | e   |     | e   |     |     | e   |     |     | e   |     | e   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     | x   |     |     | x   |     |     | x   |     |     | x   |     | x    |     |     |     | x   |     |      | x   |     | x   |     |     | x   |     |     | x   |     | x   |     |     |
|     |     |     | e   |     |     | e   |     |     | e   |     |     | e   |     | e    | n   |     |     | e   |     |      | e   |     | e   |     |     | e   |     |     | e   |     | e   |     |     |
|     |     |     | t.  |     |     | 2.  |     |     | 2.  |     |     | y.  |     | t.   |     |     |     | e.  |     | ell. |     |     | d.  |     | d.  |     |     | p.  |     |     | c.  |     |     |
|     |     | ni  |     |     | 3   |     |     | p   |     |     | a   |     |     | ui r |     |     | c   |     |     |      |     | m   |     |     | a   |     |     | t   |     |     | s   |     |     |
|     |     | ui  |     |     | dll |     |     | m   |     |     | r   |     |     |      |     |     | n   |     |     | h    |     |     |     |     | p   |     |     | s   |     | c   |     |     |     |
|     |     |     |     |     |     |     |     |     |     |     | s t |     | q   |      |     |     | o   |     |     | s    |     | c   |     |     |     |     |     | m   |     |     |     |     |     |
|     |     | 4   |     |     |     |     |     | g   |     |     | y   |     |     |      |     |     |     |     |     | r    |     |     |     |     | e   |     |     |     |     |     |     |     |     |
|     | e   |     |     |     | n   |     | e   |     |     |     |     |     | s   |      |     |     | n   |     | e   |      |     |     |     |     | t   |     |     | r   |     |     |     |     |     |
|     |     |     |     | u   |     |     |     |     |     |     | s   |     | f   |      |     | u   |     |     | w   |      |     |     |     | o   |     |     |     | h   |     |     |     |     |     |
|     | i   |     |     | r   |     |     | r   |     |     | h   |     |     |     |      |     | r   |     |     |     |      |     |     |     | n   |     |     | c   |     |     |     |     |     |     |
|     |     |     |     |     |     |     | n   |     |     | t   |     |     |     |      |     |     |     |     | o   |      |     |     |     |     |     |     |     |     |     |     |     |     |     |
|     |     |     |     |     |     |     | u   |     |     | al  |     |     |     |      |     |     |     |     | p   |      |     |     |     |     |     |     |     |     |     |     |     |     |     |
e
h
y
t
ri
u
c
e
s
Figure 29: Most common binary executables used in SonicWall post-exploitation activities
2026 Cyber
| Threat Report |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     | Exploit-Driven Campaigns In 2025 | 50  |
| ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | -------------------------------- | --- |

CrushFTP
Exploitation
(CVE-2025-31161)
In April, we saw in-the-wild exploitation of an authentication bypass
flaw (CVE-2025-31161) in CrushFTP software. This vulnerability impacted
how the file transfer application handles user authentication and gave
attackers access to the application’s administrator user account, which
led to new backdoor accounts, unauthorized file access (upload and
download), malicious code execution, and full control of the vulnerable
server. Across several incidents, we saw threat actors exploit the flaw
to deploy MeshAgent, install malicious AnyDesk RMM instances, and
more.
Figure 30: AnyDesk process spawning from CrushFTPService.exe
2026 Cyber
Threat Report Exploit-Driven Campaigns In 2025 51

Gladinet
Exploitation
(CVE-2025-30406, CVE-2025-11371, CVE-2025-14611)
Gladinet had a spicy security year. We responded to multiple exploited
vulnerabilities, including a critical severity flaw, in Gladinet’s CentreStack and
Triofox products, its enterprise file access, sharing, and content management
Figure 31: Screenshot of CISA’s Notification of CVE-2025-30406
solutions.
It started with a Rapid Response in April for CVE-2025-30406, a critical severity
vulnerability stemming from a hard coded machine key, which would allow a threat
actor to achieve remote code execution via a ViewState deserialization flaw.
In October, we spotted adjacent Gladinet in-the-wild exploitation, with an
unauthenticated CentreStack and Triofox Local File Inclusion flaw (CVE-2025-11371).
After a deep dive, we found this flaw impacted several customers and allowed
threat actors to retrieve the machine key from the Web.config file to perform remote
code execution via the same ViewState deserialization vulnerability in
CVE-2025-30406.

In December, the security community uncovered another round of Gladinet
exploitation. This time, it was linked to Cl0p ransomware gang and tracked under
CVE-2025-14611. Because the AES implementation in Gladinet’s CentreStack and
Triofox products has hardcoded cryptographic keys, threat actors could potentially
abuse this to access the web.config file, opening the door for deserialization and
remote code execution.

Figure 32: Detection timeline for observed exploitation of CVE-2025-30406
2026 Cyber
Threat Report Exploit-Driven Campaigns In 2025 52

React2Shell
Feature Primary Role Key Activity
Exploitation
Starts a SOCKS5 proxy to move laterally
SPivoting socket_quick_start
through the network.
Timestomping — Modifies timestamps (defaults
Stealth change_file_time
to 2016-01-15) to evade forensic detection.
(CVE-2025-55182)
Spawns a reverse PTY bash shell and
Execution interactive_shell
immediately wipes the command history.
In December, a threat advisory was released for another deserialization
Reads, hex-encodes, and exfiltrates
flaw with five words nobody wants to hear: critical unauthenticated Exfiltration explorer_download
files to the attacker's C2.
remote code vulnerability. This exploit, dubbed React2Shell, abused
React Server Components’ processing of the React Flight protocol.
Threat actors broadly targeted CVE-2025-55182 due to its widespread Figure 33: Post-exploitation stage of React2Shell attack path
nature (the components are used in React.js, Next.js, and more) and the
ease of exploitation. CVE-2025-55182 is caused by insecure
deserialization of React Server Components’ payload logic, and can be
exploited with an unauthenticated attacker and one HTTP request.
During these incidents, we saw attackers move fast from initial access to
post-exploitation payloads, including cryptominers, a Linux backdoor
called ‘PeerBlight’, a reverse-proxy tunneling tool nicknamed
CowTunnel, and a Go-based implant dubbed ZinFoq. We also watched
a Kaiji botnet variant get dropped.
Figure 34: Example of React2Shell exploitation
2026 Cyber
Threat Report Exploit-Driven Campaigns In 2025 53

Veeam Backup
Exploitation
(CVE-2025-48983)
Exploitation of Veeam backup servers didn’t skip a beat in 2025, with
attacks on the Mount Service (CVE-2025-48983), the SVC_VEEAM
service account, and the Veeam database components that interface
with backup systems. This malicious activity happened after attackers
gained access to internal networks, suggesting that patching and
hardening of these systems is still a tricky issue.
Attackers targeted the Mount Service for elevated privileges to disable
defenses, get access to backup jobs, access mounted backup content,
and extract files for credential access. Attackers also targeted the
SVC_VEEAM account, taking advantage of the account’s elevated Figure 35: PowerShell script exploiting Veeam Backup and Replication Service
privileges, or creating accounts disguised as this account to blend in
with normal service operations. They would then give this account RDP
access to move laterally under the guise of the legitimate backup
system.

Most of this activity happened after attackers exploited the local
VeeamBackup SQL database, which stores service credentials. The
most common command execution was via the sqlcmd or similar SQL
database clients.
Figure 36: Suspicious parent process of Veeam.Backup.MountService.exe
2026 Cyber
Threat Report Exploit-Driven Campaigns In 2025 54

Defense
Evasion
2026 Cyber
Threat Report

Driver Abuse
and EDR
Obfuscation of payload
to evade analysis and
detection
Tampering
in 2025
Attackers began acting earlier in the attack chain and deliberately
targeting endpoint visibility. They increasingly sought kernel-level control
to improve their chances of success, particularly in ransomware and multi-
stage campaigns. Instead of relying only on user-mode evasion or short-
lived process termination, adversaries invested in techniques for
persistent, system-wide control over security tools.
Figure 37: Wordlist-encoded BYOVD payload
2026 Cyber
Threat Report Defense Evasion 56

Bring Your
Own Vulnerable
Driver
Most Commonly Abused Drivers
(BYOVD)
CopCom.sys / CapRoot 5.7%
23.8% Throttlestop/RWDriver
TrueSught.sys 2.9% (mgdsrv/rwdrv.sys)
In 2025, BYOVD techniques were a reliable and repeatable method for
attackers to gain privileged Ring 0 execution without exploiting zero day RTCore64.sys 4.8%
kernel vulnerabilities. Instead of chasing novel kernel exploits, malware
operators favored a stable inventory of well-documented, signed but gdrv.sys 4.8%
vulnerable drivers that provide predictable input/output control (IOCTL)
WinRing0 /
abuse paths.

WinRing0x64/sys 8.6%
Drivers like Throttlestop, SSPort, Dell’s DBUtilDrv2, RTCore64, Asus
13.3% SSPort.sys
Asus AsIO / AsIO2.sys /
AsIO series, and WinRing0 appeared across unrelated incidents,
AsIO3.sys 9.5%
reinforcing that attackers keep curated “driver toolkits” to reuse across
campaigns. The presence of ransomware-linked vulnerable driver
telemetry, especially inpoutx64.sys and gdrv.sys, further shows that
these drivers are commonly used during pre-encryption staging workflows, inpoutx64.sys 12.4% 14.3% Dell DButilDrv2.sys
not just for post-exploitation persistence.

Over time, the execution flow became consistent:

Establish execution via initial access or lateral movement
 Figure 38: Most commonly abused drivers in 2025
Load or map a vulnerable driver using a kernel loader

Leverage kernel primitives to squash defenses or stabilize access
2026 Cyber
Threat Report Defense Evasion 57

Kernel Loader
Types of Driver Abuse Methods for
Tooling and
Privilege Escalation vs. Defense Tampering
|     |     | Defense Tampering |     |     | Privilege Elevation |     |     |     |     |
| --- | --- | ----------------- | --- | --- | ------------------- | --- | --- | --- | --- |
Signature
|     |     | 0%  | 8%  | 16% | 24% | 32% | 40% |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Enforcement
|     | Kernel Driver Mapper |     |     | 18  |     |     | 14  |     |     |
| --- | -------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
Bypass
|     | KDU and similar Tools |     | 2   |     |     |     | 4   |     |     |
| --- | --------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
BCEDIT Integrity modification
|     |     |     | 2   |     |     |     | 4   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Kernel loader utilities like driver mappers were popular in attacker toolkits.
These tools let attackers load unsigned or modified drivers without directly
|     | Kernel Service Creation |     | 8   |     |     |     | 28  |     |     |
| --- | ----------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
exploiting kernel vulnerabilities, often by temporarily weakening code
integrity through boot configuration changes.

The recurring combo of kernel loader usage, explicit kernel service
creation, and code integrity enforcement modification means attackers
|     | Filter Driver Modifications |     |     |     | 18  |     | 7   |     |     |
| --- | --------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
are designing workflows that assume driver loading may initially fail, and
include fallback paths to ensure kernel code execution regardless of
system posture. This layered approach mirrors the redundancy seen in
lateral movement tooling and shows a mature understanding of modern
Windows protections. Figure 39: Distribution of driver abuse methods used for
privilege escalation vs. defense tampering
2026 Cyber
| Threat Report |     |     |     |     |     |     |     | Defense Evasion | 58  |
| ------------- | --- | --- | --- | --- | --- | --- | --- | --------------- | --- |

Driver-Enabled
Credential and Privilege
Consolidation
Driver-assisted credential and privilege access was a persistent attacker strategy This technique popped up right before:
throughout 2025. The continued appearance of Mimikatz’s mimidrv.sys highlights
a reliance on kernel components to bypass user-mode protections around 22% 31%
39%
credentials and protected processes. This approach acts as a force multiplier,
letting attackers extract credentials shielded by the OS, access memory protected
Lateral Payload
by Protected Process Light (PPL), and expand privileges before disabling security Ransomware
controls.
 movement bursts staging
execution windows
Attackers applied these techniques in different ways. Some tried to load kernel
components early to keep full control over the environment, while others delayed
Its use means attackers know that disabling configuration settings alone isn’t
kernel access until later stages of an intrusion. In several cases, attackers were
enough in environments with layered monitoring. Filter driver tampering offers a
convinced that failure to gain kernel access would often lead to their discovery,
more durable suppression mechanism and reflects growing attacker confidence
and decided to only try it as a last resort.

operating in kernel space.
Another notable trend was more use of filter driver manipulation to suppress
security visibility at the kernel level. Unloading monitoring filter drivers represents a
decisive escalation beyond user-mode tampering, as it removes telemetry at the
source, rather than racing against agent self-defense logic.

2026 Cyber
Threat Report Defense Evasion 59

Escalation to
Service and
Code to kill and impair
EDR visibility
Process
Termination
When configuration-level tampering wasn’t enough or was blocked,
attackers escalated to direct service and process termination. This pattern
underscores attacker adaptability and highlights that EDR resistance is
treated as an obstacle to be iteratively overcome and not a single control
to bypass.
Kernel-level suppression consistently represented the final and most
effective stage of this progression.
Figure 40: Example of KillProc implementation
2026 Cyber
Threat Report Defense Evasion 60

Microsoft
Most Common Types of PowerShell
Defender
Manipulation to Disable Defender
0% 5% 10% 15% 20% 25% 30%
Degradation as
ExclusionPath
27.54
a Repeatable
ExclusionProcess 26.61
ExclusionExtension 16.62
Workflow
DisableRealTimeMonitoring 16.34
PUAProtection
16.34
Attackers didn’t just shut down Defender last year—they quietly weakened DisableIOAVProtection 2.15
it. By tweaking settings, they lowered detection rates while keeping the
service running. This keeps the lights on but the alarms off, so
cybercriminals can lurk in your system unnoticed.
 DisableIntrusionPreventionSystem 1.21
Based on activity we saw, Defender tampering wasn’t a single action, but
a multi-stage process repeated across hosts within the same intrusion.

DisableBehaviorMonitoring 1.12
Figure 41: Most common types of PowerShell manipulation attackers
used to tamper with or disable Microsoft Defender

2026 Cyber
Threat Report Defense Evasion 61

PowerShell-
Defender compromise via
Based
encoded PowerShell
Manipulation
PowerShell-based manipulation of Defender accounted for ~81% of all
Defender-related tampering activity, making it the number-one defense
evasion technique in 2025.

Attackers consistently used Defender’s native management interface,
enabling protection changes without exploiting vulnerabilities and often
without triggering tamper-protection safeguards. This reflects a
preference for legitimate administrative tooling over noisy or brittle
bypass techniques.
Figure 42: Security Information and Event Management (SIEM)
detection events for compromised host
2026 Cyber
Threat Report Defense Evasion 62

Real-Time
Protection
Tampering
Attackers usually tampered with Defender by explicitly disabling real-time This included use of Defender’s native CLI, purpose-built disabling scripts or tools
protections, accounting for roughly 9% of all Defender tampering. This action was designed to repeatedly enforce suppression, and explicit stopping or disabling of
treated as a high-risk situational step and not a default move, happening after Defender-related services.
exclusions were already configured and before high-risk activity like payload
deployment, encryption, or mass credential access, or once stealth was no longer
a priority, signaling a shift from evasion to execution.

Registry-based policy tampering was rampant, representing about 14% of
Defender tampering activity. Adversaries modified core policy and service
enforcement keys to weaken real-time monitoring, behavioral protections, and
IOAV scanning. In a smaller but notable subset of cases, several threat actors fully
disabled cloud reporting and sample submission, suggesting deliberate attempts
to reduce telemetry and detection feedback rather than fully dismantle local
protections.

A smaller but operationally significant portion of Defender tampering activity
involved direct command-line utilities, third-party suppression tools, and service-
level control, collectively accounting for ~4.5% of all Defender degradation
observed.
Figure 43: Commands modifying Defender security settings
2026 Cyber
Threat Report Defense Evasion 63

Breaking Down
Hacker Activity
2026 Cyber
Threat Report

Hands-On-
Keyboard
HOK Activity by Month
(HOK) and
2025-01
Evasive Activity
20%
2025-12 2025-02
16%
12%
2025-11 2025-03
8%
4%
2025-10 0% 2025-04
Let’s unpack attacker behaviors that highlight direct human interaction
during different stages of the attack path. We’re talking about things like
network reconnaissance commands, manual command execution, or
2025-09 2025-05
lateral movement, not fully automated tools or scripts. Tracking hands-on-
keyboard (HOK) activity shapes defenses by revealing operational
timeframes and default attacker behaviors and strategies across attack
2025-08 2025-06
phases. It also gives us an inside perspective on how threat actors respond
2025-07
to roadblocks, whether that’s failed execution events or unexpected
security defenses.

AVG
Our findings reinforce that most intrusions move beyond automation into
active human control. This drives actionable insights for detection timing,
response prioritization, and dwell time reduction.
Figure 44: HOK activity by month
2026 Cyber
Threat Report Breaking Down Hacker Activity 65

Operational
Mapping HOK activity by hour within a 24-hour period shows clear activity clusters
within late-day and early-evening UTC windows, with peak activity between 15:00
and 19:00 UTC. These windows align with reduced security staffing in many regions,
Timeframes while still overlapping with standard business hours in North America. These also
correlate to heightened obfuscation activity, when attackers alter scripts or commands
to hide malware or their HOK activities from detection.

Compared to automated execution, interactive activity demonstrates tighter hourly
clustering and longer session durations. Manual reconnaissance, obfuscated command
attempts, and defense tampering disproportionately happen within these windows,
indicating active operator oversight rather than scheduled or scripted execution.

HOK vs. Obfuscated Activity % by Hour (UTC)
|     |     |     |     |     |     |     |     | HOK Activity (%) |     |     | Obfuscated Activity (%) |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------------- | --- | --- | ----------------------- | --- | --- | --- | --- | --- |
20%
16%
12%
10.3
9.7
9.2
8.7
8.5
7.8
|     | 8%  |     |     |     |     |     |     |     |     |     |     | 7.6 | 7.7 |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
7.0 6.8
6.6 6.4
6.1
5.9 6.1
5.0
4.9 5.0
|     |     |     |     |     |     |     |     |     |     | 4.1 |         |     | 4.2 | 4.4 |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------- | --- | --- | --- | --- | --- |
|     | 4%  |     |     |     |     | 3.6 |     |     | 3.5 | 3.5 | 3.5 3.5 |     |     |     | 3.7 |     |
3.4
|     | 2.8 |     |     |     | 3.0 |     |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
2.6
2.1
|     | 1.91.8 | 2.0 |     |     |     |     |     |     |     |     |     |     |     | 1.9 | 1.9 |     |
| --- | ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |        |     | 1.7 |     |     | 1.6 |     | 1.5 |     |     |     |     |     |     |     |     |
|     |        | 1.2 |     | 1.3 |     |     | 1.4 |     |     |     | 1.4 |     |     |     |     |     |
1.1
|     |     |     |     |     | 0.7 |     |     |     | 0.6 | 0.8 |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
0%
0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
Hour (UTC)
Figure 45: Percentages of HOK vs. obfuscated activity by hour (UTC)

2026 Cyber
| Threat Report |     |     |     |     |     |     |     |     |     |     |     |     |     | Breaking Down Hacker Activity |     | 66  |
| ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----------------------------- | --- | --- |

HOK Activity
Breakdown
HOK Activity in 2025
0.8% EDR Tampering
Reconnaissance (26.1%), lateral movement (23.8%), and manual tool
9.9% Data Exfiltration
execution (19.8%) topped the list of HOK activity in 2025.
Lateral Movement 23.8%
Over the last year, we spotted multiple manual reconnaissance sequences 7.6% Custom Persistence
Installation
where attackers executed three or more distinct actions in a short
timeframe. These sequences can include identity validation, domain
enumeration, network discovery, and privilege assessment. Threat actors
extensively used low-frequency, environment-specific commands, with 12% Active User
direct references to local domains, user contexts, network paths, and Credential Dumping
service names that reflected situational awareness of the target
environment.
Reconnaissance 26.1%
19.8% Manual Tool Execution
Figure 46: Type of HOK activity
2026 Cyber
Threat Report Breaking Down Hacker Activity 67

Interaction Type Breakdown by Month
|     |         |      |       |       |     | HOK AVG (%) |     | Automated Avg (%) |     |     |     |     |       |      |     |
| --- | ------- | ---- | ----- | ----- | --- | ----------- | --- | ----------------- | --- | --- | --- | --- | ----- | ---- | --- |
|     |         | 0%   |       | 10%   | 20% | 30%         | 40% | 50%               | 60% | 70% | 80% | 90% |       | 100% |     |
|     | 2025-01 |      | 10.68 |       |     |             |     |                   |     |     |     |     | 89.32 |      |     |
|     | 2025-02 |      |       | 14.61 |     |             |     |                   |     |     |     |     | 85.39 |      |     |
|     | 2025-03 |      | 10.33 |       |     |             |     |                   |     |     |     |     | 89.67 |      |     |
|     | 2025-04 |      | 10.77 |       |     |             |     |                   |     |     |     |     | 89.23 |      |     |
|     | 2025-05 |      | 6.87  |       |     |             |     |                   |     |     |     |     | 93.13 |      |     |
|     | 2025-06 |      | 9.94  |       |     |             |     |                   |     |     |     |     | 90.07 |      |     |
|     | 2025-07 |      |       | 12.06 |     |             |     |                   |     |     |     |     | 87.95 |      |     |
|     | 2025-08 |      | 10.21 |       |     |             |     |                   |     |     |     |     |       | 89.8 |     |
|     | 2025-09 |      | 7.96  |       |     |             |     |                   |     |     |     |     | 92.05 |      |     |
|     | 2025-10 | 5.68 |       |       |     |             |     |                   |     |     |     |     | 94.32 |      |     |
|     | 2025-11 |      | 6.68  |       |     |             |     |                   |     |     |     |     | 93.33 |      |     |
|     | 2025-12 |      | 8.86  |       |     |             |     |                   |     |     |     |     | 91.14 |      |     |
Figure 47: HOK vs. automated activity in 2025
2026 Cyber
| Threat Report |     |     |     |     |     |     |     |     |     |     |     |     | Breaking Down Hacker Activity |     | 68  |
| ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----------------------------- | --- | --- |

HOK Activity by Malware Family
User-driven execution surged this year, especially ClickFix, leading us to (Two Hours Post-Intrusion)
dig into the associated HOK data. Following the success of ClickFix
attacks, we noticed a measurable rate of follow-on HOK activity shortly
after successful fake CAPTCHA scams. In these cases, initial user execution
0% 2% 4% 6% 8% 10% 12%
was followed by interactive command execution, obfuscation attempts, or
reconnaissance. Analyzing HOK activity post-infection, we saw that
SocGholish 10.51
roughly 7% of ClickFix attacks leads to HOK activity within two hours.
Gootloader 7.39
ClickFix 7.39
QakBot 6.37
TrickBot 4.46
ChromeLoader 4.13
LummaStealer 2.86
Figure 48: Percentages of follow-on HOK activity by malware
family two hours post-intrusion
2026 Cyber
Threat Report Breaking Down Hacker Activity 69

HOK
|     |     |     |     |     |     |     |     |     | Threat actors use obfuscation to hide their      |     |     |     |     |     |     |     |     |     |     |     | strategies during interactive sessions. If an     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------------------------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------------------------------------------- | --- | --- | --- | --- | --- |
|     |     |     |     |     |     |     |     |     | tracks and confuse detection analysis. They      |     |     |     |     |     |     |     |     |     |     |     | execution fails, they refine their approach with  |     |     |     |     |     |
|     |     |     |     |     |     |     |     |     | often use techniques like the Invoke-Expression  |     |     |     |     |     |     |     |     |     |     |     | trickier, indirect commands.
                     |     |     |     |     |     |
Obfuscation
cmdlet or string concatenation to sneak past
|     |     |     |     |     |     |     |     |     | defenses, and if their initial attempts get  |     |     |     |     |     |     |     |     |     |     |     | Finally, watch for PowerShell activity with  |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | -------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | -------------------------------------------- | --- | --- | --- | --- | --- |
|     |     |     |     |     |     |     |     |     | blocked, these human operators react. They   |     |     |     |     |     |     |     |     |     |     |     | nested scriptblocks. These multi-layered     |     |     |     |     |     |
executions vary wildly between incidents,
switch to complex methods like split keywords
|     |     |     |     |     |     |     |     |     | or delayed string resolution to evade  |     |     |     |     |     |     |     |     |     |     |     | which confirms you’re dealing with a human  |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | -------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------------------------------------- | --- | --- | --- | --- | --- |
Techniques
operator manually tweaking the payload
detection.

rather than a standard malware tool.
We also see them use adaptive decoding
chains. Instead of a set pattern, they shift
Obfuscation Activity %
40%
34.97
32%
26.09
24%
3.83
16%
8%
|     |     |     |     |     | 3.83 |     | 3.53 |     |      |      |     |      |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | ---- | --- | ---- | --- | ---- | ---- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     |     |     |      |     |      |     | 2.81 | 2.33 |     | 2.31 |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
2.16
|     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     | 0.46 |     | 0.28 |     | 0.26 | 0.13 |     | 0.02 |     | 0.02 |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- | --- | ---- | --- | ---- | ---- | --- | ---- | --- | ---- | --- |
0%
|     |     | C   |     |     |     |     | R   |     |     |     |     |     |     |     |     | X   |     |     |     | X   |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     | X   |     | R   |     | X   |     |     |     | X   | 4   |     | X   |     | R   |     |     |     | Z   |     |     | X   |     | X   |     | X   |     |
|     | E   | N   | A   |     | E   |     | E   |     | E   | 6   |     | E   |     | A   |     | E   |     | G   |     | E   | E   |     | E   |     | E   |     |
|     | I   |     |     |     | I   |     | H   |     | I   | B   |     | H   |     | H   |     | I   |     | 4   |     | I   | H   |     | I   |     | I   |     |
|     |     | E   | H   |     | 4   |     |     |     | R   |     |     |     |     |     |     | R   |     |     |     | R   |     |     | Z   |     | C   |     |
|     |     |     | C   | 6   |     |     | T   |     | A   |     |     | R   |     | C   |     | A   | 6   |     |     | A   |     |     | G   |     |     |     |
|     |     |     |     | B   |     | O   |     |     |     |     |     | A   |     |     |     |     | B   |     |     |     |     |     |     |     | N   |     |
|     |     |     |     |     |     |     |     | H   |     |     |     |     |     | 4   | H   |     |     |     | H   |     |     |     | 4   | E   |     |     |
|     |     |     |     |     |     |     |     | C   |     |     | H   |     | 6   |     | C   |     |     |     | C   |     |     | 6   |     |     |     |     |
|     |     |     |     |     |     |     |     |     |     |     | C   |     | B   |     |     |     |     |     |     |     |     | B   |     |     |     |     |
|     |     |     |     |     |     |     |     |     |     |     |     |     |     |     | Z   |     |     |     | 4   |     |     |     |     |     |     |     |
|     |     |     |     |     |     |     |     |     |     |     |     |     |     |     | G   |     |     |     | 6   |     |     |     |     |     |     |     |
B
Figure 49: Types of obfuscation methods in 2025
2026 Cyber
| Threat Report |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     | Breaking Down Hacker Activity |     | 70  |
| ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----------------------------- | --- | --- |

Identity-Based
Attacks
2026 Cyber
Threat Report

Legit Credentials.
Malicious Users.
Identity-based threat activity in 2025 reflected a continued shift away from
Deceptive, Intrusive, Stealthy
isolated authentication abuse toward structured, goal-driven intrusion chains.
Attackers treated identity as the primary attack vector, using access anomalies,
phishing-as-a-service platforms, session hijacking, OAuth abuse, and mailbox
manipulation as interconnected steps, rather than independent tactics.

This past year, we also saw threat actors respond more confidently to security
Rogue Business Email
measures like MFA, by launching AiTM attacks or abusing legitimate
Infostealers
Applications Compromise
authentication workflows.
While identity alert volume fluctuated throughout the year, the underlying
Identity threats were everywhere in 2025. While organizations have spent years tradecraft showed consistency, suggesting a smaller number of mature campaigns
hardening devices and securing network perimeters, attackers have shifted their rather than broad, opportunistic abuse.

focus to the path of least resistance: the user. Threat actors don’t just get
unauthorized access to victims’ accounts anymore—they’re using infostealers, We saw a sharp increase in identity threat activity in February, with daily event
rogue apps, and shadow workflows (malicious rules attackers use to hide activity volume rising noticeably in the middle of the month. This surge coincided with the
by auto-forwarding or deleting messages) to expand their reach into your public disclosure of CVE-2025-0108 on February 12, an authentication bypass in
business. the management web interface of Palo Alto Networks PAN-OS software. The
timing aligns with increased malicious OAuth abuse, anomalous session behavior,
Compromising an identity lets threat actors bypass traditional defenses by logging and post-authentication activity spotted across multiple organizations, peaking
in with valid user credentials. Attackers weaponize these identities to quietly work on February 14th. These give strong evidence that threat actors focused on
in your environment, turning a single compromised user into a launchpad for major campaign deployment, accelerated access, and prioritized exploitation activity
operations like ransomware and BEC attacks. during that week.
2026 Cyber
Threat Report Identity-Based Attacks In 2025 72

Average ITDR Events % vs. CVE-2025-0108 Disclosure (February 2025)
ITDR Events % CVE-2025-0108 Disclosure
20%
16%
12%
8%
4%
0%
2025-02-01 2025-02-04 2025-02-07 2025-02-10 2025-02-13 2025-02-16 2025-02-19 2025-02-22 2025-02-25 2025-02-28
Figure 50: Average ITDR events in February 2025 compared to spike related to CVE-2025-0108 disclosure date

2026 Cyber
Threat Report Identity-Based Attacks In 2025 73

Shady
Logins
Victim's username,
password, and session
token in plain sight
Threat actors continued to exploit Microsoft 365 environments, but in 2025,
we saw attackers get better at breaking in quietly and staying there.

Access policy and trust boundary violations (37.2%) emerged as a top
attack category for ITDR. This means attackers are trying to log in from
suspicious places—like unauthorized countries or known bad networks—
often using stolen credentials bought from the dark web. In fact, these
types of shady login attempts made up over a third of all detections this
year.

This can also be a signal that attackers hide behind legitimate VPN
services. Throughout 2025, we saw cybercriminals use VPNs and proxies
to mask their malicious activities and behaviors. A small group of consumer
VPN services—specifically NordVPN, ExpressVPN, TunnelBear, SurfEasy,
and ProtonVPN—accounted for most of this activity, while a long tail of
providers supported short-term, opportunistic access attempts.
Figure 51: An example of an AiTM attack with Evilginx
2026 Cyber
Threat Report Identity-Based Attacks In 2025 74

VPN Abuse Frequency % by Month
NORD VPN EXPRESS VPN TUNNELBEAR VPN SURF EASY VPN PROTON VPN SURFSHARK VPN PIA VPN HIDE MY ASS VPN TOUCH VPN WHITELABEL VPN OTHER VPNs
0% 10% 20% 30% 40% 50% 60% 70% 80% 90% 100%
2025-02
2025-03
2025-04
2025-05
2025-06
2025-07
2025-08
2025-09
2025-10
2025-11
2025-12
Figure 52: VPN abuse in 2025
2026 Cyber
Threat Report Identity-Based Attacks In 2025 75

NordVPN was the most consistently abused provider, accounting for
18–24% of tunnel-related activity in any given month, and averaging just
over 21% across the year. Its steady use in 2025 suggests repeated reuse
rather than opportunistic testing, especially during months that also
showed higher post-authentication behavior. ExpressVPN followed a
similar pattern, averaging roughly 12% of monthly activity, with noticeable
increases during several campaign windows, including late Q2 and early
Q4.

Other providers showed more fleeting behavior. TunnelBear and SurfEasy
each showed sharp, short-lived spikes, often exceeding 10% of monthly
tunnel usage during specific periods, followed by fast decline. These bursts
aligned closely with access-stage activity and didn’t always come before
mailbox manipulation or OAuth persistence, indicating likely use during
Compromised
credential validation or access brokerage rather than sustained intrusion
identity disabled,
operations. ProtonVPN had moderate but recurring usage, ranging
between five to nine percent and suggesting a hybrid role spanning both threat contained,
exploratory and follow-on activity.

and SOC report
within 25 minutes
In our month-over-month analysis of malicious VPN activity, we spotted
these operational patterns:

Initial access phases: Attackers deliberately rotated providers across
multiple VPN services to minimize detection

Persistence or BEC: Attackers returned to the same VPN providers
across multiple weeks or months, signaling operational success
against tenant-specific controls
Figure 53: ITDR telemetry revealing adversary abuse of
legitimate hosting environments
2026 Cyber
Threat Report Identity-Based Attacks In 2025 76

Malicious Identity Activity by Month
Mailbox Manipulation & Persistence Malicious OAuth & Application Abuse Post-Compromise Identity Abuse Session & Token Hijacking VPN / Proxy Abuse
Access Policy & Trust Boundary Violations Adversary-in-the-Middle (AiTM) Credential Compromise & Abuse Defense Tampering Identity Reconnaissance
0% 10% 20% 30% 40% 50% 60% 70% 80% 90% 100%
2025-01
2025-02
2025-03
2025-04
2025-05
2025-06
2025-07
2025-08
2025-09
2025-10
2025-11
2025-12
Figure 54: Malicious identity activity breakdown by month in 2025
2026 Cyber
Threat Report Identity-Based Attacks In 2025 77

Other key identity threat
trends in 2025 include:
ITDR Incident Frequency
Mailbox Manipulation Anomalous behavior
and Persistence
 after valid logins

Attackers love to hide their tracks. In about While the initial login might look
19% of cases, they set up automated rules legitimate, the subsequent session
to hide or forward sensitive emails. This activity will have unusual
helps them stay undetected during BEC characteristics.
attacks or quietly steal data.
Access Policy & Trust
 18.9% Adversary-in-the-Middle (AiTM)
Boundary Violations 37.2%
4.1% Credential
AiTM Attacks
 Quality Over Quantity

Compromise & Abuse
Session & Token Hijacking 4.3%
Nearly 19% of attacks involved AiTM Attackers moved away from volume-based
1.2% Identity Reconnaissance
tools like Evilproxy or Evilginx. These attacks to stealthier tactics like valid
Post-Compromise
tools help criminals steal credentials and authentication abuse, session persistence, and
Identity Abuse 0.7%
bypass 2FA and MFA. post-authentication manipulation.
4.6% Datacenter, CDN
and ASN Abuse
Malicious OAuth &
Application Abuse 10.1% 19% Mailbox Manipulation & Persistence
Attackers are becoming more efficient. They’re turning unauthorized
access into reliable footholds within your network, often validating stolen
data quickly (looking over large sets of stolen data to see if there’s
valuable data in it) to sell it to other cybercriminals. They’re running a
Figurer 55: Identity Threat Detection and Response (ITDR) incidents in 2025
profitable business, and this scaling of the identity theft ecosystem means
organizations need to be more vigilant about monitoring post-login
activity, not just the initial break-in.
2026 Cyber
Threat Report Identity-Based Attacks In 2025 78

Mailbox
Manipulation
Step PowerShell Command Purpose
1 Connect-ExchangeOnline Establish authenticated session
Mailbox manipulation (19.0%) and persistence followed access policy and
trust boundary violations, as the second most common identity threat flagged
by ITDR. Cybercriminals know that obvious moves like forwarding emails
immediately set off alarms, especially as precursors to BEC attacks. So, they
Get-Mailbox -ResultSize
favor subtle concealment tactics, like:
 2 Retrieve all mailboxes
Unlimited
Marking messages as read

Deleting inbound mail

Redirecting emails to obscure folders

Get-InboxRule -Mailbox
Surface all rules including
3 user@company.com -
hidden ones
We typically see external forwarding and outbound spam only after the IncludeHidden
attacker establishes a foothold. It’s a deliberate choice: they stage their
attacks carefully, because they know that immediate exploitation will get
them busted.

Export-Csv -Path
Old inbox rules and hidden artifacts make it tough to spot these intruders once 4 Document findings for analysis
"InboxRules.csv"
they take control. These techniques keep you in the dark and allow attackers
to maintain access, particularly if you don’t perform routine mailbox audits.

Figurer 56: How to manually uncover hidden inbox rules with PowerShell
2026 Cyber
Threat Report
Identity-Based Attacks In 2025 79

Adversary-
in-the-Middle
(AiTM)
AiTM (18.9%) attacks were the third most frequent identity threat in 2025. Whether AiTM activity didn't grow in a straight line this year. Instead, we saw clear ups and
ITDR flagged sketchy session reuse or token mismatches from suspicious networks, downs, which tells us that these events are specific campaign indicators rather
the goal was the same for attackers: bypass MFA to access a vulnerable network. than general risk signals.

While an AiTM attack might not look like a full-blown breach, it’s often just the In many cases, the lack of follow-up activity shows that defensive controls at the
beginning. It’s the open door for criminals to steal authentication tokens and abuse access stage are working. But don't let your guard down, because instances
OAuth, paving the way for more severe incidents. where attackers did succeed prove that phishing attacks designed to bypass MFA
are highly effective, especially when cybercriminals strike fast.
Rather than a steady stream of background noise, these attacks hit in short, intense
bursts. Think of it like a series of coordinated raids. We saw recurring technical clues
—like specific login patterns and reused tools—that tell us organized groups are
managing these campaigns centrally.

Our data explicitly identified multiple AiTM platforms, with EvilProxy appearing
most frequently, followed by Sneaky 2FA and FlowerStorm. These platforms often
used malicious subdomains and spoofed login panels, though we also saw fake
document signing requests and deceptive error messages designed to trick users
into giving their credentials.
Figurer 57: AiTM detection alert
2026 Cyber
Threat Report
Identity-Based Attacks In 2025 80

OAuth Abuse
and Malicious
Application
Activity
While not an ITDR frontrunner in 2025, OAuth abuse and malicious
application (10.1%) activity are high impact tradecraft, up from 4.8% in
2024. Attackers use malicious web apps and sneaky consent requests to
get permanent access to your accounts, all without ever changing your
password.

This shift in our data shows that criminals now prefer to hide within the
application layer itself. It lets them quietly raid mailboxes and data for
months without setting off security alarms.

This stealthy approach is perfect for BEC attacks and corporate espionage.
Even as other attack methods dropped off throughout the year, OAuth abuse
was steady. It proves that if your defenses aren't configured tightly, this is a
low-risk, high-reward way for attackers to slip past your controls.

Figure 58: Attackers exploit OAuth permissions for access and persistence
2026 Cyber
Threat Report Identity-Based Attacks In 2025 81

Session and
Token Hijacking
Malicious authentication
attempts
Token theft (4.3%) happened consistently throughout the year, but many
attackers got caught because they failed to match their victims' location,
browser, operating system, and tunnel characteristics.

Think of it like a burglar trying to use a stolen key, but wearing a neon sign
that says "I don't live here!" These victories highlight why we need to
proactively monitor for strange behavior. If successful, these techniques let
adversaries bypass MFA entirely. This reduces their reliance on credentials
and drastically speeds up their activity after gaining access, leading to
further compromises.

In the past, attackers often compromised session tokens and waited a long
time to sell them to the highest bidder to maximize profits. But now, with
ITDR becoming more effective at spotting these intrusions and cutting off
access, the game has changed. Would-be bidders now pay a premium for
quick access to maximize their cybercrime profits before their window
closes.
Figure 59: A Huntress report flags a session hijacking attack
2026 Cyber
Threat Report Identity-Based Attacks In 2025 82

BEC: Trends,
Conversion, and BEC was one of the most dangerous identity
threat trends of 2025. Mailbox manipulation,
external forwarding, outbound spam abuse, or
OAuth-based mailbox persistence was a smaller
proportion of total identity telemetry compared to
Campaign Activity
prior years, but showed higher confidence and
tighter sequencing in 2025 leading to financial
fraud. A notable spike in February aligns with the
previously noted CVE-2025-0108 disclosure.
BEC Frequency % by Month
20%
16%
12%
8%
4%
0%
2025-01 2025-02 2025-03 2025-04 2025-05 2025-06 2025-07 2025-08 2025-09 2025-10 2025-11 2025-12
Figure 60: Frequency of BEC attacks in 2025
2026 Cyber
Threat Report Identity-Based Attacks In 2025 83

In our analysis of ITDR data, a BEC conversion is marked by detection of
inbox rules manipulation to hide emails or suspicious outbound email
activity. We analyzed two types of BEC pre-compromise activity to
establish BEC conversion events:
BEC Precursors
Suspicious activities that set the stage for potential BEC attacks. Sketchy password activity,
Threat actor’s
suspicious sign-in attempts, attempts to manipulate tokens/sessions, suspicious activity
related to mailboxes, or identity reconnaissance methods. IP address
BEC Enabler
Actions that give an attacker control over email or identity workflows, like session hijacking,
OAuth consent abuse, and role or permission escalations.
Not every BEC red flag turns into a full-blown financial fraud email-based
attack. This was evident in November in the chart below, with a spike of
BEC enabler activity characterized by increased AiTM activity followed by
shady credential theft (sessions/tokens/passwords). But instead of moving
to sketchy mailbox activity, the attackers installed malicious apps and Compromised OAuth2
turned to traditional exploitation.
authentication and
shady inbox rules
Figure 61: Example of BEC activity flagged by ITDR
2026 Cyber
Threat Report Identity-Based Attacks In 2025 84

BEC Conversion Trends
BEC Enabler BEC Precursor
20%
16%
12%
8%
4%
0%
Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec
Figure 62: Distribution of BEC enabler vs. BEC precursor activity
In BEC attacks, we see cybercriminals rely on session and token hijacking because
it gives them a quick path from compromising a token to manipulating a mailbox.
BEC attacks don't always involve malware, so attackers
Once inside, attackers stay hidden before they try to cash out. They abuse inbox
use AiTM to steal credentials and bypass MFA for
rules to conceal their presence, setting the stage for external forwarding or spam
persistent access to compromised accounts. Organizations activity. This trend shows that cybercriminals are playing the long game. They
prioritize long-term access and operational flexibility over rapid, high-volume
can improve resilience by setting known login locations.
fraud.
Block or challenge anything outside of the allow lists.
As the year closed out, BEC conversion and activity spiked. This surge happened
because attackers ramped up campaigns focused on mail spamming, reselling
Casey Smith
email accounts, and gaining enterprise access during the holiday season.
Staff Threat Intelligence Analyst
2026 Cyber
Threat Report Identity-Based Attacks In 2025 85

Phishing
Activity
2026 Cyber
Threat Report

Hacking
Top File Extensions %
|     |     |     | 0%  | 10% | 20% | 30% | 40% | 50% | 60% |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Human
.pdf
57.7
.html
10.2
Nature
.docx
5.9
.svg
4.2
|     |     | .htm | 4   |     |     |     |     |     |     |     |
| --- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     | .doc | 3.3 |     |     |     |     |     |     |     |
In 2025, phishing was a major entry point for threat actors to gain initial
access and do reconnaissance work. Despite vendor disruptions to
|     |     | .rpmsg | 2   |     |     |     |     |     |     |     |
| --- | --- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
phishing kits like Raccoon0365 and Lighthouse, these kits kept developing
to give attackers advanced capabilities for scalable credential theft like
|     |     | .ics | 1.9 |     |     |     |     |     |     |     |
| --- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
MFA bypass tactics, unique subdomains for victims, or anti-analysis scripts.

To track phishing trends throughout the year, we gathered potential
|     |     | .xlsx | 1.3 |     |     |     |     |     |     |     |
| --- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
phishing emails reported by Huntress Managed Security Awareness Training
(SAT) learners. These emails were then studied using a vision-based
|     |     | .zip | 1   |     |     |     |     |     |     |     |
| --- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
identification process to catalog, organize, and do in-depth analysis to
categorize the most prevalent threats into unique groups of attacks
|     |     | .txt | 0.7 |     |     |     |     |     |     |     |
| --- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
targeting customers. While these groups don’t represent all potential
attacks, they present clear recurring themes and techniques consistently
| abused.
 |     | .pptx | 0.7 |     |     |     |     |     |     |     |
| -------- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
As seen on the next page, the most common phishing themes revolved
|     |     | .mail | 0.6 |     |     |     |     |     |     |     |
| --- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
around requests for e-signatures, voicemail notifications, invoice payments,
and file shares. Alongside these lures, we most frequently saw file
|     |     | .mp3 | 0.4 |     |     |     |     |     |     |     |
| --- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
attachments that included .pdf, .png, and .html.

|     |     | .xhtml | 0.4 |     |     |     |     |     |     |     |
| --- | --- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
Figure 63:  Most prevalent phishing attachment file extensions in 2025
2026 Cyber
|     | Threat Report |     |     |     |     |     |     |     | Phishing Activity | 87  |
| --- | ------------- | --- | --- | --- | --- | --- | --- | --- | ----------------- | --- |

Top Phishing Lure Themes %
20%
16%
14.2
12%
7.8
|     | 8%  |     |     |     |     |     |     |     |     |     | 7.5 |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
6.8
4%
|     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     | 2.2 |     |     |     | 2.1 |     |     | 2   |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
1.8
1.5
1
0%
|     |     |     | t   |     |     |     | n   |     |     |     | n   |     | e   |     |     |     |     | n   |     |     |     | n   |     |     | e   |     |     |     | n   |     |     |     |     | n   |     |     |     |     | t   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     | s   |     |     |     | o   |     |     |     | o   |     | r   |     |     |     |     | o   |     |     |     | o   |     |     | c   |     |     |     | o   |     |     |     |     | o   |     |     |     |     | s   |     |
|     |     |     | e   |     |     |     |     |     |     |     |     |     | a   |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     | e   |     |
|     |     |     | u   |     |     |     | ti  |     |     |     | ti  |     | h   |     |     |     | ti  |     |     |     |     | ti  |     | n   |     |     |     |     | ti  |     |     |     |     | ti  |     |     |     | u   |     |     |
|     |     |     | q   |     |     |     | a   |     |     |     | a   |     | S   |     |     |     | a   |     |     |     |     | a   |     | a   |     |     |     |     | a   |     |     |     |     | a   |     |     |     | q   |     |     |
|     |     |     |     |     |     |     | c   |     |     |     | c   |     |     |     |     |     | c   |     |     |     |     | r   |     | t   |     |     |     |     | c   |     |     |     | c   |     |     |     |     |     |     |     |
|     |     |     | e   |     |     | fi  |     |     |     |     | fi  |     | e   |     |     |     | fi  |     |     |     | pi  |     |     | t   |     |     |     |     | fi  |     |     |     | fi  |     |     |     |     | e   |     |     |
|     |     |     | R   |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     | mi  |     |     |     |     |     |     |     |     |     |     |     |     |     | R   |     |     |
|     |     | e   |     |     |     | ti  |     |     |     |     | ti  | Fil |     |     |     |     | ti  |     |     |     | x   |     |     |     |     |     |     |     | ri  |     |     |     | ti  |     |     |     | w   |     |     |     |
|     |     |     |     |     |     | o   |     |     |     | o   |     |     |     |     |     | o   |     |     |     |     | E   |     | e   |     |     |     |     | e   |     |     |     |     | o   |     |     |     |     |     |     |     |
|     |     | r   |     |     | N   |     |     |     |     | N   |     |     |     |     |     | N   |     |     |     |     | d   |     | R   |     |     |     |     | V   |     |     |     | N   |     |     |     |     | e   |     |     |     |
u
|     |     | t   |     |     | e   |     |     |     | ail  |     |     |     |     |     |     | t   |     |     |     |     | r   |     |     |     |     |     |     | t   |     |     |     | e   |     |     |     |     | vi  |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     | a   |     |     |     |     |     |     |     |      |     |     |     |     |     | n   |     |     |     |     | o   |     |     |     |     |     |     |     | n   |     |     |     |     |     |     |     |     | e   |     |     |     |
|     | n   |     |     |     | c   |     |     |     |      |     |     |     |     |     | e   |     |     |     |     | w   |     |     |     |     |     |     | u   |     |     |     |     | g   |     |     |     |     |     |     |     |     |
|     | g   |     |     |     | oi  |     |     |     | m    |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     | a   |     |     |     |     | R   |     |     |     |     |
|     |     |     |     |     |     |     |     |     | e    |     |     |     |     |     | m   |     |     |     |     | s   |     |     |     |     |     |     | o   |     |     |     | s   |     |     |     |     | t   |     |     |     |     |
|     | Si  |     |     | v   |     |     |     |     |      |     |     |     |     |     | y   |     |     |     |     | s   |     |     |     |     |     |     | c   |     |     |     | s   |     |     |     |     | n   |     |     |     |     |
|     |     |     |     | n   |     |     |     |     | c    |     |     |     |     |     |     |     |     |     | a   |     |     |     |     |     |     |     | c   |     |     |     | e   |     |     |     |     | e   |     |     |     |     |
| -   |     |     |     | I   |     |     |     | oi  |      |     |     |     |     | a   |     |     |     |     | P   |     |     |     |     |     |     | A   |     |     |     | M   |     |     |     |     |     |     |     |     |     |     |
| E   |     |     |     |     |     |     |     |     |      |     |     |     |     | P   |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     | m   |     |     |     |     |     |
|     |     |     |     |     |     |     |     | V   |      |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     | e   |     |     |     |     | u   |     |     |     |     |     |
|     |     |     |     |     |     |     |     |     |      |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     | r   |     |     |     |     | c   |     |     |     |     |     |
|     |     |     |     |     |     |     |     |     |      |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     | u   |     |     |     |     | o   |     |     |     |     |     |
|     |     |     |     |     |     |     |     |     |      |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     | c   |     |     |     | D   |     |     |     |     |     |     |
e
S
Figure 64: Most common phishing lure themes in 2025
2026 Cyber
|     |     | Threat Report |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     | Phishing Activity | 88  |
| --- | --- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----------------- | --- |

Impersonated
Brands Frequency of Impersonated Brands %
0% 8% 16% 24% 32% 40%
Microsoft 31.6
Other 22.9
Microsoft was still the top impersonated brand, accounting for 31% of
phishing emails we analyzed. Microsoft's widespread adoption and role as DocuSign 17.9
a cornerstone of productivity tools make it an attractive target. Attackers
used phishing lures that mimicked everything from Teams to Microsoft
RingCentral 2.7
Office 365 to compromise these accounts, giving attackers access to
emails, files, internal communications, and more.
Intuit 2.5
While mainstays like Docusign, Intuit, and Google were frequently
impersonated, RingCentral is a notable new addition to our coverage this
year. The cloud communications company was mimicked for voicemail lures Google 2.3
prompting targets to "listen to the voice message" or "view the transcript"
to facilitate AiTM attacks. Callback phishing, where emails use mistaken
Adobe 1.9
invoices or charges and provide a phone number for victims to call to "fix"
a problem, was a popular method in 2025, and PayPal was a top brand
attackers impersonated to carry out these attacks.
ADP 1.9
Attackers also exploited the inherent trust placed in these brands in "Living
off Trusted Sites" (LoTS) attacks. Unlike standard phishing emails that link PayPal 1.9
directly to a malicious page, LoTS attacks guide victims to legitimate
platforms, such as file-sharing and collaboration sites, where attackers
Dropbox 1.4
either host malicious files directly or embed deceptive links within
documents stored on the trusted site. This approach is particularly
effective, as users tend to lower their guard for content on "trusted" sites
and outside the perceived risks of their inbox.
Figure 65: Brands most commonly impersonated in phishing emails in 2025
2026 Cyber
Threat Report Phishing Activity 89

Phishing: Lures
and Defense
Psychological Hooks Frequency %
Evasion
40%
32%
30.6
25.7
24%
It isn’t surprising that threat actors still rely on well-known lures like those
nagging shipping notifications claiming you have incorrect delivery details
or that text message saying you have unpaid toll road charges. After all,
why change a winning formula?
16.3
15.5
16%
These lures are often paired with defense evasion tactics like QR codes
with ASCII characters that won’t be picked up by security tools, or
manipulating legitimate URLs vulnerable to open URL redirects to push
8.1
victims to a malicious site. 8%
These phishing lures continue to work for threat actors because they prey 3.1
on human emotion, manipulating users into opening a link or clicking on an
0.6
attachment by using psychological hooks. Across the phishing lures used in 0%
2
b
0
y
2
a
5
t
,
t a
u
c
rg
k
e
e
n
rs
c
,
y
w
a
it
n
h
d
5
t
6
ru
%
s t
o
w
f a
e
l
r
l
e
p
t
h
h
is
e
h
m
in
o
g
s
e
t
m
co
a
m
ils
m
w
o
e
n p
a
s
n
y
a
c
ly
h
z
o
e
lo
d
g
le
ic
v
a
e
l
r
h
a
o
g
o
in
k
g
s u
th
se
e
d
se U r g
e n c
y
T r u s
t
C
u ri
o si t
y
A
u t h
o ri t
y
F e a
r
n
ci al
G ai
n
H
el p f
ul
emotions. a
n
Fi
Figure 66: Most common psychological hooks used in phishing emails throughout 2025
2026 Cyber
Threat Report Phishing Activity 90

AI Abuse
2026 Cyber
Threat Report

Friend, Foe,
or Both?
AI-generated
PowerShell script,
featuring Russian
While AI-powered cybercrime might seem like a scene from a sci-fi
blockbuster, the reality behind defender lines isn’t film-worthy stuff. AI
abuse in 2024 was mostly about threat actors crafting phishing emails, but
in 2025, experimentation evolved into more sophisticated, tangible
applications.

One of the most alarming advancements is in deepfake technology. A
chilling example involves BlueNoroff, a North Korean APT group, which
used deepfakes of a company’s leadership during a Zoom call to deceive
an employee into downloading malware. Deepfakes have also infiltrated
HR and recruitment processes, with companies unknowingly "interviewing"
candidates who were, in reality, North Korean-linked actors using
deepfake personas. Their goal is to secure employment, infiltrate
organizations, and steal sensitive data.

In December, we saw a particularly novel tactic in an AMOS stealer
campaign where threat actors used the 'shared chat' features of ChatGPT
and Grok. By pre-generating conversations giving malicious Terminal
commands—disguised as helpful instructions for queries like 'Clear disk
Figure 67: An attacker's attempt to use an AI-generated script for credential dumping
space on macOS'—attackers bypassed user suspicion. These shared links
were then promoted via sponsored Google ads to dominate search
results, tricking users into executing malware directly on their systems.
2026 Cyber
Threat Report AI Abuse 92

Cybercrime is, at its core, a business, and like any seasoned operators scale their operations. But
business, cybercriminals are constantly seeking we’re also seeing a shift in AI abuse tactics. Threat
ways to scale. AI has become their ultimate actors will exploit user trust in AI tools, creating
productivity tool, helping them automate and even more convincing social engineering schemes
We’re seeing adversaries
accelerate operations at breakneck pace. But this and using automation to supercharge
rush to scale often comes at a cost: In their haste, reconnaissance efforts.
 use AI much like engineers do:
attackers leave behind telltale signs like scripts
for coding, tool development,
riddled with Russian comments or Cyrillic To prepare for these threats and build stronger
and workflow automation.
characters, malicious browser extensions with defenses against AI abuse, organizations should
emojis buried in the source code, or even scripts take these steps in 2026:
 They’re using it to find
that claim to steal data, but don’t have the
software vulnerabilities, craft
Invest in managed security solutions that
functionality to exfiltrate it.

connect the dots through the entire attack path, more convincing phishing
Malicious groups are adopting AI to speed up from telemetry retention through security
emails, clone voices for
tooling and development. They use AI-assisted awareness training

deepfakes, and optimize
OSINT to pinpoint target details and deploy dark
Use MFA for all VPN, admin interfaces, RMM,
web tools to find high-value data. Attackers also operations across the board.
and backup consoles

rely on AI to generate code, clone phishing
We even caught an attacker
Restrict lateral movement paths by hardening
websites, and modify malware signatures to evade
the network with segmentation and least installing our own EDR agent,
detection. While this technology raises the
privilege deployment, and monitoring WinRM,
baseline skill level for lower-level hackers, its which let us see how they
RDP, and service account usage

biggest advantage is speed. AI cuts down the time
used AI to streamline
needed to stage and launch attacks, forcing Log and alert on suspicious interpreter activity
defenders to identify and react to threats faster with command-line capture and script block workflows and sharpen
than ever.
 logging, and/or deploy appropriate security phishing campaigns.
solutions that facilitate full visibility across the
What does 2026 hold for us as AI-powered network

cybercrime evolves? If 2025 taught us anything, it’s Jamie Levy
Maintain and tune detection for early stage
that AI will keep lowering the barrier to entry for Senior Director, Adversary Tactics
tradecraft behaviours like anomalous
cybercriminals, so even novice threat actors can
enumeration, lateral movement, credential
launch sophisticated attacks while helping
dumping, and privilege escalation
2026 Cyber
Threat Report Phishing Activity 93

Conclusion
2026 Cyber
Threat Report

Resilience
Wins
2025 was defined by shifting tactics and blurred lines across the threat landscape.
Attackers don’t need to break down your digital doors when they can just log in
with stolen credentials or trick an employee into giving them access. By
weaponizing legitimate tools like RMMs and exploiting everyday behaviors
Most teams think resilience comes from seeing
through stealthy tactics like ClickFix and fake CAPTCHAs, cybercriminals have
more. In reality, it comes from knowing what turned identity into the new perimeter. The line between normal activity and an
incident is thinner than ever, proving that traditional defenses alone aren’t enough
matters and acting quickly when it does.
to stop these organized, profit-driven cybercriminal operations.

To stay ahead in 2026, we have to treat security as a business-wide responsibility,
Eric Stride
not just another IT ticket piled up in the queue. This means building a defense
Chief Information Security Officer, Huntress
strategy that prioritizes identity protection, monitors the abuse of trusted
processes, and empowers every employee to spot attacker tradecraft. Trust us—
you can’t hire or innovate fast enough to fight this competition alone. But by
curating a culture where humans are the first line of defense, we can turn our
biggest vulnerability into our greatest strength and lead the threat landscape,
not react to it.
2026 Cyber
Threat Report Conclusion 95

About Huntress
Huntress is a global cybersecurity company on a mission to make enterprise-grade
products accessible to all businesses. Purpose-built from the ground up, Huntress'
technology is specifically designed to continuously address the unique needs of
security and IT teams of all sizes. From Endpoint Detection and Response (EDR) and
Identity Threat Detection and Response (ITDR) to Security Information and Event
Management (SIEM) tools and Security Awareness Training (SAT), the platform
provides targeted protection for endpoints, identities, data, and employees,
delivering trusted outcomes and valuable peace of mind.
﻿

Its 24/7, AI-assisted Security Operations Center (SOC) is powered by a team of
world-renowned engineers, researchers, and security analysts, dedicated to
stopping cyber threats before they can cause harm. Huntress is often the first to
respond to major hacks and incidents, with its expert security team sharing real-
time tradecraft analysis and actionable advisories with the community. Currently
safeguarding over 4.5 million endpoints and 10 million identities, Huntress
empowers security teams, IT departments, and Managed Service Providers (MSPs)
worldwide to protect their businesses with enterprise-grade security accessible to
everyone.

﻿As long as hackers keep hacking, Huntress keeps hunting. Join the hunt at
www.huntress.com and follow us on X, Instagram, Facebook, and LinkedIn.

<!-- CONVERSION_METADATA: {"source": "https://github.com/jacobdjwilson/awesome-annual-security-reports", "date": "2026-10-03", "model": "gemini-3.5-flash-lite"} -->
