# 2025 THREAT DETECTION REPORT
Techniques, trends, & takeways

Explore
our new
Field Guide

## Table of Contents
- [Introduction](#introduction)
- [Methodology](#methodology)
- [Trends](#trends)
  - [Ransomware](#ransomware)
  - [Initial access tradecraft](#initial-access-tradecraft)
  - [Identity attacks](#identity-attacks)
  - [Vulnerabilities](#vulnerabilities)
  - [Stealers](#stealers)
  - [Insider threats](#insider-threats)
  - [VPN abuse](#vpn-abuse)
  - [Cloud attacks](#cloud-attacks)
  - [Mac malware](#mac-malware)
- [Top threats](#top-threats)
  - [Featured threat: Scarlet Goldfinch](#featured-threat-scarlet-goldfinch)
  - [Featured threat: Amber Albatross](#featured-threat-amber-albatross)
  - [Featured threat: LummaC2](#featured-threat-lummac2)
  - [Featured threat: NetSupport Manager](#featured-threat-netsupport-manager)
  - [Featured threat: HijackLoader](#featured-threat-hijackloader)
- [Field Guide to Color Bird Threats](#field-guide-to-color-bird-threats)
  - [Tangerine Turkey](#tangerine-turkey)
  - [Amber Albatross](#amber-albatross)
  - [Saffron Starling](#saffron-starling)
  - [Scarlet Goldfinch](#scarlet-goldfinch)
  - [Lilac Lyrebird](#lilac-lyrebird)
  - [Charcoal Stork](#charcoal-stork)
  - [Raspberry Robin](#raspberry-robin)
  - [Mango Parakeet](#mango-parakeet)
  - [Yellow Cockatoo](#yellow-cockatoo)
  - [Silver Toucan](#silver-toucan)
  - [Coral Crane](#coral-crane)
  - [Silver Sparrow](#silver-sparrow)
  - [Blue Mockingbird](#blue-mockingbird)
- [Top techniques](#top-techniques)
  - [Featured technique: Email Hiding Rules](#featured-technique-email-hiding-rules)
  - [Featured technique: Mshta](#featured-technique-mshta)
  - [Featured technique: Cloud Service Hijacking](#featured-technique-cloud-service-hijacking)
- [Acknowledgements](#acknowledgements)

## Introduction

We are pleased to present Red Canary’s 2025 Threat Detection Report. Our seventh annual retrospective is based on in-depth analysis of nearly 93,000 threats detected across our customers’ over 4 million identities, endpoints, and cloud resources over the past year. This report provides you with a comprehensive view of this threat landscape, including new twists on existing adversary techniques, and the trends that our team has observed as adversaries continue to organize, commoditize, and ratchet up their cybercrime operations.

As the technology that we rely on to conduct business continues to evolve, so do the threats that we face. Here are some of our key findings:

*   **More data**: Red Canary detected nearly 93,000 threats in 2024, increasing last year’s total by more than a third. This is the result of not only more customers, but also our expanded visibility into cloud and identity infrastructure.
*   **Expanded attack surface**: Three of the top 5 MITRE ATT&CK® techniques we detected this year were cloud-native and enabled by identity, including our number one, Cloud Accounts.
*   **On the rise**: Along with 4x times as many identity attacks as last year, we observed notable increases in infostealers, macOS threats, and business email compromise.
*   **Trickier browser lures**: The use of fake CAPTCHA lures, a technique known as “paste and run,” likely explains how LummaC2, NetSupport Manager, and HijackLoader made their way into our top 10 threats, as well as Mshta’s return to the top 10 technique list after a four-year absence.
*   **Proxies are a common thread**: VPN abuse is both rampant and hard to detect, and we observed these popular products leveraged in incidents ranging from ransomware to insider threats.

USE THIS REPORT TO:

*   Explore the most prevalent and impactful threats, techniques, and trends that we’ve observed.
*   Note how adversaries are evolving their tradecraft as organizations continue their shift to cloud-based identity, infrastructure, and applications.
*   Learn how to emulate, mitigate, and detect specific threats and techniques.
*   Shape and inform your readiness, detection, and response to critical threats.

After reading this report, we encourage you to explore the new and improved Threat Detection Report website, featuring a new threat index and field guide to Red Canary-named threats.

## Methodology

Behind the data

The Threat Detection Report sets itself apart from other annual reports with its unique data and insights derived from a combination of expansive detection coverage, diverse technological partnerships, and expert-led investigation and confirmation of threats. The data that powers Red Canary and this report are not mere software signals—this data set is the result of hundreds of thousands of investigations across millions of protected systems and identities.

Each of the nearly 93,000 threats that we responded to have one thing in common: They weren’t prevented by our customers’ expansive security controls. This research is the result of a breadth and depth of analytics and analysis that we use to detect the threats that would otherwise go undetected.

BY THE NUMBERS

Red Canary ingested 308 petabytes of security telemetry from our 1,400 customers’ endpoints, identities, clouds, and SaaS applications in 2024. Our detection engine generated 30 million investigative leads that our platform pared down to nearly 93,000 confirmed threats, 25,000 of which were high-severity threats that might’ve represented a significant risk to our customers if we hadn’t detected them. Every one of these was scrutinized and enriched by professional detection engineers, intelligence analysts, researchers, threat hunters, and an ever-expanding suite of bespoke generative artificial intelligence (GenAI) tools.

More than a quarter of the threats Red Canary detected in 2024 were high severity.

The Threat Detection Report synthesizes the critical information we communicate to customers whenever we detect a threat, the research and detection engineering that underlies those detections, the intelligence we glean from analyzing them, and the expertise we deploy to help our customers respond to and mitigate the threats we detect.

What counts

We map our custom detection analytics and the other security signals we use to detect threats to corresponding MITRE ATT&CK® techniques whenever possible. If the analytic or alert uncovers a realized or confirmed threat, we construct a timeline that includes detailed information about the activity we observed, including extensive information about techniques an adversary leveraged. We track this data over time to determine technique prevalence, correlation, and much more.

DETECTIONS BY YEAR

![DETECTIONS BY YEAR]

This report also examines the threats that leverage these techniques and other tradecraft intending to harm organizations. While Red Canary broadly defines a threat as any suspicious or malicious activity that represents a risk to you or your organization, we also track specific threats by programmatically or manually associating malicious and suspicious actions with clusters of activity, specific malware variants, legitimate tools being abused, and known threat actors. We track and analyze these threats continually throughout the year, publishing Intelligence Insights, bulletins, and profiles, considering not just prevalence of a given threat, but also aspects such as velocity, impact, or the relative difficulty of mitigating or defending against. The Threats section of this report highlights our analysis of common or impactful threats, which we rank by the number of customers they affect.

Consistent with past years, we exclude unwanted software and confirmed testing from the data we use to compile this report.

Limitations

Red Canary optimizes heavily for detecting and responding rapidly to early-stage adversary activity. As a result, the techniques that rank skew heavily between the initial access stage of an intrusion and any rapid execution, privilege escalation, lateral movement, and defense evasion. This will be in contrast to incident response providers, for example, whose visibility tends towards the middle and later stages of an intrusion, or a full-on breach. We often detect and action threats early, shielding organizations from the wide array of risks associated with breaches and incidents. As such, one of the great benefits of this report is that it acts as a playbook that organizations can follow to develop the ability to detect threats early and often, before adversaries are able to accomplish their objectives and cause harm.

Knowing the limitations of any methodology is important as you determine what threats your team should focus on. While we hope our list of top threats and detection opportunities helps you and your team prioritize, we recommend building your own threat model by comparing the top threats we share in our report with what other teams publish and what you observe in your own environment.

## TRENDS

Red Canary performed an analysis of emerging and significant trends that we’ve encountered in confirmed threats, intelligence reporting, and elsewhere over the past year. We’ve compiled the most prominent trends of 2024 in this report to show major themes that may continue into 2025.

The Technique and Threat sections of this report are focused on prevalent ATT&CK techniques and threat associations from the more than 93,000 confirmed threats we detected in 2024. The Trends section takes us one step beyond that data and allows us to narrate events that might not be prevalent in our detection dataset but may be emergent or otherwise deserve your attention.

What’s included in this section

We’ve written an extensive analysis of nine trends we tracked throughout 2024. This PDF includes an abridged version of our analysis, describing the trend and explaining why it matters. You can view the full analysis—including mitigation, detection, and testing guidance—in the web version of this report.

How to use our analysis

The Trends section provides valuable insight and actionable recommendations for security leaders to make informed decisions. We offer advice to help defenders prepare, prevent, detect, and mitigate activity associated with these trends where relevant. The guidance we provide differs, since each trend requires a different approach. You might also use our analysis to help anticipate and plan for key trends that may continue into 2025, just as we saw with 2023 trends extending into 2024.

*   Ransomware
*   Initial access tradecraft
*   Identity attacks
*   Vulnerabilities
*   Stealers
*   Insider threats
*   VPN abuse
*   Cloud attacks
*   Mac malware

### Ransomware

Ransomware continues to surge year-over-year, and payout demands are only getting higher.

Ransomware is holding strong as a lucrative business model for criminals. Despite early wins from law enforcement actions, this past year saw increasingly sophisticated and agile operations, with adversaries asking for higher payouts.

As with last year, Red Canary’s visibility into the ransomware landscape focused on the early stages of the ransomware intrusion chain—the initial access, reconnaissance, lateral movement, and command and control (C2) occurring before exfiltration or encryption, which we refer to as “ransomware precursors.” Focusing on detecting these precursors continued to be a solid approach to stopping ransomware in 2024, so we’ll focus on sharing what has worked for us.

We saw few intrusions making it to the final stages, and this meant that no ransomware group made it into our top 10 threats for any month or the year overall. This past year we observed activity related to the following ransomware variants:

*   Akira
*   Play
*   FOG
*   LockBit
*   RansomHub
*   Black Basta

Since our visibility centers on ransomware precursors, we also recommend checking out ransomware reporting from other researchers for a full perspective across the intrusion chain.

Common ransomware precursors in 2024

As in previous years, multiple threats in our top 10 play a role in ransomware intrusions as common precursors:

*   Impacket
*   Mimikatz
*   SocGholish
*   Gootloader
*   HijackLoader
*   NetSupport Manager

Check out each of those pages for ideas on how to take action to detect these threats.

We’ve previously shared the simplified ransomware intrusion chain below as a way to think about detection across the entire intrusion, and it continues to hold up as a high-level approach to breaking down ransomware.

![Ransomware intrusion chain diagram: Pre-ransomware (Initial access, Recon, Lateral movement, Command and control) -> Ransomware (Exfiltration, Encryption)]

Here are some of the common techniques, tools, and procedures we observe across “pre-ransomware” intrusion stages.

Initial access

Ransomware affiliates continue to rely on the same broad categories of exploitation of vulnerabilities, phishing, brute force, and valid credentials for initial access. This year we observed affiliates exploiting vulnerabilities in ScreenConnect and Fortinet software.

We also observed a plethora of phishing varieties, most notably with Black Basta affiliates who conducted extensive social engineering campaigns that began with email bombing to flood a victim’s inbox with spam. Next, the adversary—posing as an IT admin offering to help with the email problem—contacted the user via phone or a link to join a Microsoft Teams call. Once in contact, the adversary guided the user into running a remote monitoring and management (RMM) tool like Microsoft Quick Assist, AnyDesk, or TeamViewer.

Watch our video on the Black Basta email bombing campaign.

In August 2024, we observed ransomware incidents that leveraged virtual private networks (VPN), particularly Cisco ASA, as an initial access vector and to facilitate further access within organizations. To exploit VPN appliances, adversaries typically conduct password spray attacks targeting login accounts with weak passwords and without MFA. Reporting indicates that both Akira and FOG ransomware affiliates have targeted VPN software for initial access.

Finally, as noted in the Stealers section of this report, we continued to see increasing use of info-stealing malware for obtaining valid credentials, which adversaries use or sell to ransomware affiliates to gain access.

Lateral movement

Adversaries are fast and furious when it comes to lateral movement, with some intrusions progressing in a matter of hours. A continuing trend is adversaries quickly moving to unmonitored parts of the network; this past year, adversaries often favored moving to VMware ESXi hypervisors, which are rarely well-monitored. In these attacks, adversaries deploy encryptors developed for Linux to stop all virtual machines running on a victim’s hypervisor before encrypting individual VMDK files.

Hypervisors are a particularly valuable target because organizations often use them to host business-critical services, and they are unable to host endpoint sensors. Although most ransomware reporting focuses on Windows varieties, many of the more prolific ransomware families—like RansomHub, Play, Black Basta, and Akira—include a Linux variant that they can deploy against hypervisors.

Prior to moving to ESXi environments, adversaries commonly obtain credentials through tools like Mimikatz and move laterally using detectable tools like PsExec or Impacket. We also observed adversaries downloading and using RMM tools to facilitate lateral movement as well as persist in the environment and act as their command and control.

Reconnaissance

As adversaries land on new systems, we regularly observe them conducting reconnaissance with the usual built-in commands:

*   `ipconfig`
*   `whoami`
*   `net`
*   `nltest`

We have also observed adversaries using free open source tools like AdFind, Angry IP Scanner, BloodHound, Nmap, PCHunter, SoftPerfect NetScan, and others to map out victim environments and scan the system for hosts.

Command and control

This past year, we saw adversaries continue to abuse RMM tools. (Adversaries use these tools to facilitate lateral movement, persistence, and command and control; we classify RMM usage under command and control consistent with MITRE ATT&CK.) RMM tools are an attractive option for adversaries because they offer robust sets of remote administration features with the veneer of legitimacy, as they are used for regular business functions.

This past year, we most commonly saw the following RMM tools:

*   NetSupport Manager
*   AnyDesk Standalone
*   TightVNC
*   ConnectWise
*   TeamViewer Standalone
*   AdvancedRun
*   RUSTDESK
*   Ammyy Admin

Notable ransomware trends in 2024

It’s hard to believe that only a couple years ago, it would have been relatively unheard of for a ransomware actor to call their victim on the phone. However, what used to be SCATTERED SPIDER’s signature technique has proliferated across ransomware actors. Aggressive social engineering tactics that include calling the victim have spread across the ransomware ecosystem. At Red Canary, we observed an increase in email bombing followed by voice phishing, consistent with Black Basta precursor behavior.

Another technique that has spread across the ransomware ecosystem is the use of RMM tools for command and control and lateral movement. For example, this year we saw NetSupport Manager break into our top 10, demonstrating the popularity of the use of RMM tools.

New ransomware groups

The past year saw an emergence of new ransomware variants, with newer groups quickly rising to the tops of charts for number of victims compromised (based on data from their own data leak sites). Prolific groups like FOG, RansomHub, and FunkSec all first appeared on the scene in 2024. Groups that began operations in 2024 represented a large percentage of ransomware attacks, with some researchers estimating that new groups made up over 50 percent of the compromises in November and December 2024.

Record-high costs of a ransomware event

Ransomware continues to be a lucrative business for criminals, with victims in 2024 reportedly making record-high ransom payments, with one as high as $75 million. Despite these individually large ransom payments, there was a drop in the total amount of ransom earnings in 2024, combined with a decreasing percentage of victims that pay the ransom. Whether victims choose to pay or not, the costs of being ransomed far exceed the requested ransom amount.

Businesses often face regulatory fines, litigation, and reputational damage from ransomware events, which can impact future earnings. Since the SEC’s requirement to disclose material cyber events in late 2023, there has been a boon to class action lawsuits following data leaks. The increased media reporting of ransomware incidents, made possible through adversary leak sites, has also likely contributed to this boon. Attorneys monitoring for any data breaches reported to the SEC or on data leak sites will initiate these so-called “event-driven litigations” almost immediately upon disclosure. In some cases, multiple attorney groups will initiate lawsuits, driving up the cost to the victim.

A silver lining: Law enforcement takedowns

2024 started off with a big win against ransomware operator LockBit with Operation Cronos, a multi-national effort led by the UK National Crime Agency (NCA). The trans-national disruption operation involved law enforcement agencies from nine countries, who collectively took down 34 servers, seized more than 200 cryptocurrency wallets, seized the LockBit data leak site, and arrested two alleged LockBit members. The LockBit disruption was quite different than previous takedown efforts in that it aimed not only at dismantling the infrastructure but also sowing distrust in the ransomware marketplace, releasing affiliate names and stating that developer LockBitSupp was working with authorities.

Despite this effort, LockBitSupp announced within five days that operations had resumed. Although LockBit continued to post victims throughout 2024, some researchers assessed that the majority of the posted victims listed were from older intrusions, calling into question the accuracy of LockBit’s claims.

Life-saving detection and response: Learn how Red Canary stopped a ransomware attack at a major hospital.

Read the blog

Take action

Visit the Ransomware trend page for detection opportunities and relevant atomic tests to validate your coverage.

The good news for defenders is that even though new techniques and tools have emerged, many ransomware techniques have remained the same for the past several years. Continuing to focus on detection across the entire ransomware intrusion chain—particularly ransomware precursors—remains an effective strategy to ensure ransomware incidents have minimal impact.

The tried-and-true guidance of patching known vulnerabilities remains a solid approach to preventing initial access, as many ransomware intrusions start this way. If an organization can’t keep up with patching all vulnerabilities, we recommend prioritizing based on vulnerabilities in internet-facing devices listed in CISA’s Known Exploited Vulnerabilities catalog.

Prevention

*   Educate employees on the latest ransomware actor TTPs, such as the email flooding techniques employed by Black Basta affiliates.
*   To prevent unauthorized access to Microsoft Teams chats or phones, disallow external access and allowlist partner domains as needed. This involves setting the External Access portion of Teams to either:
    *   Allow only specific external domains
    *   Block all external domains
*   Enhance endpoint visibility by deploying detection and response sensors across systems. Unmonitored endpoints can create an attacker playground; defenders’ visibility limits adversaries’ freedom.
*   Maintain an approved tools list and monitor or deny unauthorized RMM tools. Legitimate tools can be exploited—know what is in your environment and how the tools are utilized. Adversaries will often change the filename, download and run it from a non-standard directory, or make suspicious network connections.

### Initial access tradecraft

Sketchy CAPTCHAs, fake updates, social engineering, and more; adversaries continued their masquerading, tricking users throughout 2024.

In 2024, adversaries used a wide range of methods to access and mislead unsuspecting victims. Users had to contend with malicious links and phishes presented in a multitude of ways, including via email, search engines, Microsoft Teams messages, and phone calls. “Paste and run,” a technique used to fool users into running malicious code, grew in popularity in the second half of the year. Adversaries used this method to obtain legitimate credentials and leveraged them to great effect, particularly for virtual private network (VPN) access.

Paste and run away

One of the most successful new initial access techniques we observed this year was paste and run, also known as “ClickFix” and “fakeCAPTCHA.” The last half of the year made clear that this was an effective method of luring victims into executing malicious PowerShell code. Red Canary first observed the technique in August 2024, although other researchers reported seeing it in use as early as March 2024. Proofpoint coined the commonly used moniker ClickFix to initially describe the ClearFake cluster and TA571’s use of this technique. They subsequently expanded the term as they observed it being used by additional actors. At Red Canary we chose to refer to the technique in general as “paste and run,” since not all of the lures involve a “fix” of some kind.

Different styles of lures have been reported, including a phishing lure, where the victim has to copy-paste-run the code to “fix” their access to something, like a document or a video meeting:

![Image courtesy of Proofpoint]

Adversaries have also employed this technique via compromised websites with browser injects, posing either as fake CAPTCHAs to access the site or as a page loading error requiring a “fix” to display the page:

![Image