# 2024 Threat Detection Report
## Table of Contents
- [Introduction](#introduction)
- [Methodology](#methodology)
- [Trends](#trends)
    - [Ransomware](#ransomware)
    - [Initial access tradecraft](#initial-access-tradecraft)
    - [Identity attacks](#identity-attacks)
    - [Vulnerabilities](#vulnerabilities)
    - [Stealers](#stealers)
    - [Remote monitoring and management tools](#remote-monitoring-and-management-tools)
    - [API abuse in the cloud](#api-abuse-in-the-cloud)
    - [Artificial intelligence (AI)](#artificial-intelligence-ai)
    - [Adversary emulation and testing](#adversary-emulation-and-testing)
    - [Industry and sector analysis](#industry-and-sector-analysis)
- [Threats](#threats)
    - [Charcoal Stork](#charcoal-stork)
    - [Impacket](#impacket)
    - [Mimikatz](#mimikatz)
    - [Yellow Cockatoo](#yellow-cockatoo)
    - [SocGholish](#socgholish)
    - [ChromeLoader](#chromeloader)
    - [Gamarue](#gamarue)
    - [Qbot](#qbot)
    - [Raspberry Robin](#raspberry-robin)
    - [SmashJacker](#smashjacker)
- [Techniques](#techniques)
    - [PowerShell (T1059.001)](#powershell-t1059001)
    - [Windows Command Shell (T1059.003)](#windows-command-shell-t1059003)
    - [Windows Management Instrumentation (T1047)](#windows-management-instrumentation-t1047)
    - [Cloud Accounts (T1078.004)](#cloud-accounts-t1078004)
    - [Obfuscated Files or Information (T1027)](#obfuscated-files-or-information-t1027)
    - [Email Forwarding Rule (T1114.003)](#email-forwarding-rule-t1114003)
    - [OS Credential Dumping (T1003)](#os-credential-dumping-t1003)
    - [Rundll32 (T1218.001)](#rundll32-t1218001)
    - [Ingress Tool Transfer (T1105)](#ingress-tool-transfer-t1105)
    - [Rename System Utilities (T1036.003)](#rename-system-utilities-t1036003)
    - [Featured: Installer Packages (T1546.016)](#featured-installer-packages-t1546016)
    - [Featured: Kernel Modules and Extensions (T1547.006)](#featured-kernel-modules-and-extensions-t1547006)
    - [Featured: Escape to Host (T1611)](#featured-escape-to-host-t1611)
    - [Featured: Reflective Code Loading (T1620)](#featured-reflective-code-loading-t1620)
    - [Featured: AppleScript (T1509.002)](#featured-applescript-t1509002)
- [Acknowledgements](#acknowledgements)

---
2
2024 Threat Detection Report

## Introduction
We are pleased to present Red Canary’s 2024 Threat Detection Report. Our sixth annual retrospective, this report is based on in-depth analysis of nearly 60,000 threats detected across our more than 1,000 customers’ endpoints, networks, cloud infrastructure, identities, and SaaS applications over the past year. This report provides you with a comprehensive view of this threat landscape, including new twists on existing adversary techniques, and the trends that our team has observed as adversaries continue to organize, commoditize, and ratchet up their cybercrime operations. 

As the technology that we rely on to conduct business continues to evolve, so do the threats that we face. Here are some of our key findings:

Everyone is migrating to the cloud, including bad guys: Cloud Accounts was the fourth most prevalent ATT&CK technique we detected this year, increasing 16-fold in detection volume and affecting three times as many customers as last year.

Despite a spate of new CVEs, humans remained the primary vulnerability that adversaries took advantage of in 2023. Adversaries used compromised identities to access cloud service APIs, execute payroll fraud with email forwarding rules, launch ransomware attacks, and more.

While both defenders and cybercriminals have discovered use cases for generative artificial intelligence (GenAI), we see defenders as having the edge.

Container technology is omnipresent, and it’s as important as ever to secure your Linux systems to prevent adversaries from escaping to host systems. 

Mac threats are no myth–this year we saw more stealer activity on macOS environments than ever, along with instances of reflective code loading and AppleScript abuse. 
4
2024 Threat Detection Report

Use this report to:
01
02
03
04
Explore the most prevalent and impactful threats, techniques, and trends that we’ve observed.

Note how adversaries are evolving their tradecraft as organizations continue their shift to cloud-based identity, infrastructure, and applications. 

Learn how to emulate, mitigate, and detect specific threats and techniques.

Shape and inform your readiness, detection, and response to critical threats.

Often dismissed, malvertising threats delivered payloads far more serious than adware, as exemplified by the Red Canary-named Charcoal Stork, our most prevalent threat of the year, and related malware ChromeLoader and SmashJacker.

Our new industry analysis showcases how adversaries reliably leverage the same small set of 10-20 techniques against organizations, regardless of their sector or industry.

We also check back on the timeless threats and techniques that are prevalent year-after-year, explore emerging ones that are worth keeping an eye on, and introduce two new free tools that security teams can start using immediately.
5
2024 Threat Detection Report

## Methodology
Red Canary ingested 216 petabytes of security telemetry from our more than 1,000 customers’ endpoints, identities, clouds, and SaaS applications in 2023. 

Our nearly 4,000 custom detection analytics generated 37 million investigative leads, which our platform helped us pare down to 10 million events. 9.5 million of those events were handled by automation and 500,000 were analyzed by our security operations team. After suppressing or throwing away the remaining noise, we detected more than 58,000 confirmed threats, every one of them scrutinized and enriched by professional detection engineers, intelligence analysts, researchers, threat hunters, and an ever-expanding suite of bespoke generative artificial intelligence (GenAI) tools. 

![Overview of Red Canary's Threat Detection Methodology]

2.5M+ 
endpoints, identities, and cloud resources protected

4,000 
detection analytics applied

10M 
false positives identified by the platform and pared down

500k 
events analyzed by humans

216 
petabytes of security telemetry

37M 
potentially malicious events generated

9.5M 
events resolved by automation

58,000 
threats detected

OVERVIEW
6
2024 Threat Detection Report

The Threat Detection Report synthesizes the critical information we communicate to customers whenever we detect a threat, the research and detection engineering that underlies those detections, the intelligence we glean from analyzing them, and the expertise we deploy to help our customers respond to and mitigate the threats we detect. 

Behind the data 
The Threat Detection Report sets itself apart from other annual reports with its unique data and insights derived from a combination of expansive detection coverage and expert, human-led investigation and confirmation of threats. The data that powers Red Canary and this report are not mere software signals—this data set is the result of hundreds of thousands of expert investigations across millions of protected systems. Each of the nearly 60,000 threats that we responded to have one thing in common: These threats weren’t prevented by our customers’ expansive security controls—they are the product of a breadth and depth of analytics that we use to detect the threats that would otherwise go undetected. 

What counts 
When our detection engineers develop detection analytics, they map them to corresponding MITRE ATT&CK® techniques. If the analytic uncovers a realized or confirmed threat, we construct a timeline that includes detailed information about the activity we observed. Because we know which ATT&CK techniques an analytic aims to detect, and we know which analytics led us to identify a realized threat, we are able to look at this data over time and determine technique prevalence, correlation, and much more.

This report also examines the broader landscape of threats that leverage these techniques and other tradecraft intending to harm organizations. While Red Canary broadly defines a threat as any suspicious or malicious activity that represents a risk to you or your organization, we also track specific threats by programmatically or manually associating malicious and suspicious activity with clusters of activity, specific malware variants, legitimate tools being abused, and known threat actors. Our Intelligence Operations team tracks and analyzes these threats continually throughout the year, publishing Intelligence Insights, bulletins, and profiles, considering not just prevalence of a given threat, but also aspects such as velocity, impact, or the relative difficulty of mitigating or defending. The Threats section of this report highlights our analysis of common or impactful threats, which we rank by the number of customers they affect. Consistent with past years, we exclude unwanted software and customer-confirmed testing from the data we use to compile this report. 
7
2024 Threat Detection Report

![MITRE ATT&CK Framework Stages]

RECONNAISSANCE
INITIAL ACCESS
EXECUTION
PERSISTENCE
DEFENSE EVASION
CREDENTIAL ACCESS
DISCOVERY
LATERAL MOVEMENT
PRIVILEGE 
ESCALATION
RESOURCE 
DEVELOPMENT
COLLECTION
EXFILTRATION
IMPACT
COMMAND  
& CONTROL

Limitations 
Red Canary optimizes heavily for detecting and responding rapidly to early-stage adversary activity. As a result, the techniques that rank skew heavily between the initial access stage of an intrusion and any rapid execution, privilege escalation, and lateral movement attempts. This will be in contrast to incident response providers, whose visibility tends towards the middle and later stages of an intrusion, or a full-on breach.

Knowing the limitations of any methodology is important as you determine what threats your team should focus on. While we hope our list of top threats and detection opportunities helps you and your team prioritize, we recommend building your own threat model by comparing the top threats we share in our report with what other teams publish and what you observe in your own environment.
9
2024 Threat Detection Report

## Trends
Red Canary performed an analysis of emerging and significant trends that we’ve encountered in confirmed threats, intelligence reporting, and elsewhere over the past year. We’ve compiled the most prominent trends of 2023 in this report to show major themes that may continue into 2024.

The Technique and Threat sections of this report are focused on prevalent ATT&CK techniques and threat associations from the more than 58,000 confirmed threats we detected in 2023. The Trends section takes us one step beyond that data and allows us to narrate events that might not be prevalent in our detection dataset but may be emergent or otherwise deserve your attention. 

What’s included in this section? 
We’ve written an extensive analysis of 10 trends we tracked throughout 2023. This PDF includes an abridged version of our analysis, describing the trend and explaining why it matters. You can view the full analysis—including mitigation, detection, and testing guidance—in the web version of this report. 
 
How to use our analysis 
The 2023 Trends section provides valuable insights and actionable recommendations for security leaders to make informed decisions. We offer advice to help defenders prepare, prevent, detect, and mitigate activity associated with these trends where relevant. The guidance we provide differs, since each trend requires a different approach. You might also use our analysis to help anticipate and plan for key trends that may continue into 2024, just as we saw with 2022 trends extending into 2023.

Ransomware
Vulnerabilities
API abuse in the cloud
Initial access tradecraft
Stealers
Artificial intelligence (AI)
Identity attacks
Remote monitoring and management tools
Adversary emulation and testing
Industry and section analysis
10
2024 Threat Detection Report

### Ransomware
Despite some promising disruptions to the ransomware ecosystem in 2023, defenders should stay vigilant in detecting common precursor behavior. 

Even if we as a community are tired of talking about it, 2023 showed us that ransomware isn’t done with us yet. As with 2022, Red Canary’s visibility into the ransomware landscape focused on the early stages of the ransomware intrusion chain—the initial access, reconnaissance, and lateral movement occurring before exfiltration or encryption, which we refer to as “ransomware precursors.” Focusing on detecting these precursors continued to be a solid approach to stopping ransomware in 2023, so we’ll focus on sharing what has worked for us.

We saw so few intrusions making it to the final stages that no ransomware group made it into our top 20 threats. That said, throughout the year, we observed Lockbit, Crysis, Akira, and Snatch, as well as an attempt to deploy Cerber ransomware. Since our visibility centers on ransomware precursors, we also recommend checking out ransomware reporting from others across the community, including Malwarebytes, Emsisoft, and Recorded Future. 

Common ransomware precursors 
As in previous years, multiple threats in our top 10 play a role in ransomware intrusions as common precursors: 
- Impacket
- Mimikatz
- SocGholish
- Qbot
- Raspberry Robin

Check out each of those pages for ideas on how to take action to detect those threats. We’ve previously shared this simplified ransomware intrusion chain as a way to think about detecting across the entire intrusion, and in 2023, this chain continued to hold up as a high-level approach to breaking down ransomware.

TREND
11
2024 Threat Detection Report

Here are some of the common techniques, tools, and procedures we observed across “pre-ransomware” intrusion stages: 
 
Initial access 
Red Canary has observed ransomware intrusions beginning with adversaries exploiting vulnerabilities in internet-facing devices such as Confluence or Veritas. While some vulnerabilities were more recent, in 2023 we also observed adversaries exploiting years-old vulnerabilities as well. These internet-facing devices were often unmonitored, resulting in detection of the intrusion only when adversaries moved off the initial device. We weren’t the only ones to observe adversaries exploiting vulnerabilities to start ransomware intrusions; cyber insurance company Corvus noted that in the first half of 2023, they observed exploitation of external vulnerabilities as the leading method of initial entry for ransomware.

Additionally, we observed intrusions starting with common malware families like SocGholish and Qbot that were followed by reconnaissance commands, suggesting they might have turned into a full-fledged ransomware intrusion had they not been remediated. For more on common initial access techniques, see the Trends page.

Lateral movement
Adversaries moving from unmonitored parts of the network is often the first hint at a ransomware intrusion in progress. For this stage, adversaries commonly use compromised accounts obtained from credential dumping wherever they gained initial access, often using tools like Mimikatz. Once they had credentials, we observed adversaries moving via SMB, RDP, and WMI, often assisted by tools like Impacket.

As adversaries achieved necessary execution during lateral movement, we observed tried-but-true LOLBins like Rundll32. We also observed adversaries downloading and using remote monitoring and management (RMM) tools like AnyDesk, FleetDeck, and others to facilitate lateral movement as well as persist in the environment.
12
2024 Threat Detection Report

Reconnaissance 
As adversaries landed on new systems, we regularly observed them conducting reconnaissance with the usual built-in commands: ipconfig, whoami, net, and nltest. Additionally, we observed adversaries using tools like SoftPerfect Network Scanner (netscan.exe) and ADrecon to assist.

Exfiltration and extortion continue
A trend that continued in 2023 is the shift toward exfiltration and extortion, often without encryption at all. It’s clear that adversaries aren’t just encrypting data anymore, they’re stealing it as well, then demanding payment or threatening to leak the data. As reporting by Recorded Future shows, posting stolen data has become the de facto standard for leading ransomware/extortionware actors. Some defenders track exfiltration and extortion activities under the umbrella of ransomware, which can be helpful since some adversaries exfiltrate and encrypt data. However, we encourage defenders to be clear about which operators commonly achieve which objectives, since these outcomes require different types of responses. 

Affiliates make for increased attribution challenges
The “ransomware-as-a-service” (RaaS) ecosystem continued to present challenges to defenders in 2023. As in previous years, adversaries teamed up during ransomware intrusions, with one actor (often called an “initial access broker”) gaining initial access to a network and then passing off access to other actors. SocGholish, Qbot, and Raspberry Robin are examples of our top 10 threats that are often delivered via initial access brokers that later pass off access to separate ransomware or extortionware operators.

In 2023, we observed multiple brokers using similar patterns and TTPs, which made the already-difficult question of attribution even more difficult. For example, we analyzed an intrusion that spawned from Veritas backup software and compared TTPs to our own observed intrusions as well as community reporting. While some TTPs overlapped with what Mandiant observed from ALPHV, the exploitation of Veritas as well as the use of BITSAdmin were not sufficient evidence to give us confidence in associating the intrusion to ALPHV.

A high-profile incident demonstrating the attribution challenges of the ransomware affiliate model occurred in September 2023 when MGM Resorts experienced a ransomware intrusion. While some reporting
13
2024 Threat Detection Report

attributed the incident to ALPHV/BlackCat actors, other reporting later attributed the incident to the group SCATTERED SPIDER, an affiliate of ALPHV. This incident serves as just one example of the challenges of clustering loosely affiliated adversaries; ransomware/extortionware actors will likely continue to strain the traditional CTI notion of a tracked group under a single name. 
 
Takedowns and disruptions
Ransomware trends were not all doom and gloom in 2023, as law enforcement entities took action to disrupt multiple actors. A prominent example was the FBI’s deployment of a decryption tool to decrypt data from ALPHV/BlackCat intrusions. Another example included the international law enforcement and judicial partnership to arrest actors and take down Ragnar Locker infrastructure.

A notable ransomware-adjacent disruption occurred as Microsoft, Fortra, Health-ISAC, and law enforcement partners took action to disrupt the use of Cobalt Strike by adversaries such as ransomware operators. While we at Red Canary observed Cobalt Strike being used in some intrusions (including those that looked like they might lead to ransomware), notably, we did not observe it as commonly as we did the prior year. Last year, Cobalt Strike was our eighth most prevalent threat, and this year it dropped to #19. While it’s impossible to establish causation with absolute certainty, it’s possible that the community’s collective disruption efforts resulted in this reduction.

TAKE ACTION
Visit the Ransomware trend page for relevant detection opportunities and atomic tests to validate your coverage. 

The good news for defenders is that even though new techniques and tools have emerged, many ransomware techniques have remained the same for the past several years. Continuing to focus on detection across the entire ransomware intrusion chain—particularly ransomware precursors—remains an effective strategy to ensure ransomware incidents have minimal impact. The tried-and-true guidance of patching known vulnerabilities remains a solid approach to preventing initial access, as many ransomware intrusions start this way. If an organization can’t keep up with patching all vulnerabilities, we recommend prioritizing based on vulnerabilities in internet-facing devices that are also in CISA’s Known Exploited Vulnerabilities catalog.
14
2024 Threat Detection Report

### Initial access tradecraft
Adversaries employed tried-and-true initial access methods in 2023, with a few new variations on perennial themes.

In 2023 we saw continued use of perennial favorite techniques. Phishing remains an evergreen issue, and this year adversaries continued to leverage a variety of file types in their phishing emails to deliver malicious payloads. SEO poisoning and malvertising continued to be popular, with new threats taking inspiration from established malware families. We saw a steady stream of new vulnerabilities exploited by adversaries from ransomware operators to state-sponsored threats, emphasizing the need to maintain patch levels both internally and within the supply chain. 

Phishing trends: A variety of file types still in use 
In 2023 adversaries continued to leverage a variety of different file types in attempts to bypass security features like Mark-of-the-Web (MOTW). Compressed archives (ZIP, RAR) and container files (ISO, VHD) are types of files that may not have the MOTW, meaning they won’t be restricted, blocked, or generate warning prompts in the same way as files that do contain the mark. In November 2022, Microsoft released a security update that propagated MOTW identifiers to some ZIP and ISO files, and subsequently adversaries pivoted to new options. 
- One example at the beginning of 2023 was the abuse of OneNote files to deliver payloads like Qbot. In one campaign in February, phishing emails delivered malicious OneNote attachments. User interaction opened and executed an embedded HTML Application file (.hta), a batch script file (.bat), or PowerShell script file (.ps1), which then pulled down the next stage payload. In May 2023, OneNote was updated to block embedded files with commonly abused extensions by default. 
- Beginning in July and continuing through December 2023, Red Canary observed adversaries using MSIX files to deliver malware. MSIX is a Windows application package installation format that IT teams and developers increasingly use to deliver Windows applications within enterprises. The initial access vector appeared to be malicious

TREND
15
2024 Threat Detection Report

advertising or SEO poisoning to trick victims into believing they were downloading legitimate software like Grammarly, Microsoft Teams, Notion, and Zoom. For more technical details, refer to our Installer Packages technique page.

Other security researchers reported adversaries using non-email delivery vehicles for their malicious links in 2023. While it’s not a new technique, adversaries including a QR code in phishing attempts is becoming more common; open-source intelligence suggested an increase in QR code phishing, or “quishing,” activity beginning in September 2023 and continuing through October. Additionally, Microsoft shared details of multiple campaigns using a combination of targeted social engineering and Teams chats to deliver phishing lures in 2023.

SEO poisoning
Search engine optimization (SEO) poisoning continued to be an effective technique for gaining initial access in 2023. Threats already leveraging SEO poisoning—including SocGholish, Yellow Cockatoo, and various stealers—maintained their prevalence using this technique. Several newcomers to the threat landscape, likely noting the success of threats like SocGholish, adopted similar fake browser update lures delivered via SEO poisoning. Adversaries create malicious websites that use SEO techniques like placing strategic search keywords in the body or title of a webpage. They attempt to make their malicious sites more prominent than legitimate sites when search results are returned by Google and other search engines. As an example, Zloader has used keywords like “free software development tools” to encourage victims to navigate to their site and download malicious installers. As another example, Gootloader has used websites claiming to offer information on contracts and other legal or financial documents. 

Malvertising
SEO poisoning is not the only way adversaries use search engines to their advantage. Malicious advertising, also called “malvertising,” persisted in 2023, as seen with our most prevalent threat of the year, Charcoal Stork, and related malware ChromeLoader and SmashJacker. Malvertising is the use of fake ads on search engine pages that masquerade as legitimate websites to download software like Zoom, TeamViewer, or various software updates. 

Vulnerability exploitation
Vulnerability exploitation is nothing new, and 2023 saw its fair share of new CVEs being exploited in the wild. In November 2023 we saw adversaries exploiting a Confluence vulnerability to ultimately deploy
16
2024 Threat Detection Report

ransomware. In addition to ransomware, notable large-scale incidents—like the 3CX compromise in May of 2023 and MOVEit in late May and early April—show how vulnerabilities up the supply chain can have significant downstream consequences for organizations. For more on vulnerability exploitation and what organizations can do to address it, check out the Vulnerabilities trend page.

TAKE ACTION
Visit the Initial access tradecraft trend page for relevant detection opportunities and atomic tests to validate your coverage. 

Preventing container files like ISOs or VHDs from executing can still be an effective way to avert damaging intrusions that attempt to evade MOTW controls. If your users do not have a business need to mount container files, we recommend taking steps to prevent Windows from auto-mounting container files. 
- One way to mitigate the effects of SEO poisoning is to prevent the malicious files from being able to execute. For example, Gootloader uses JScript (.js) files. If your users do not have a need to execute .js files, associating .js files to open with notepad.exe instead of wscript.exe can prevent automatic execution of their malicious content.

Some of the best ways to minimize the risk of vulnerability exploitation in your environment include: 
- patching regularly 
- maintaining an up-to-date asset inventory to let you know if the affected product is present in your environment 
- being aware of your surface area and what is exposed to the internet
17
2024 Threat Detection Report

### Identity attacks
In the era of single-sign-on and cloud-based-everything, there’s no better way for an adversary to sneak into a corporate environment than by compromising identities.

Humans remained the primary vulnerability that adversaries took advantage of when they targeted identities in 2023. This dynamic is not only true of the identity threats we detected but of the ones we researched and read about too. In this section, we will highlight trends we’ve observed in the identity threat landscape—both directly among our customers and across the industry more generally—offering actionable guidance that security teams can leverage to better protect their users and identities.

Note: Given the massive diversity of malicious or suspicious activity an adversary can undertake through a compromised identity, we’ve decided to scope the section narrowly on the process of compromising identities—from stealing credentials, to bypassing MFA, to logging in. For more information on what an adversary can do with a compromised identity, refer to the Cloud Accounts, Email Forwarding Rule, and Cloud API Abuse sections of this report.

Why do identities matter? 
As organizations migrate to the cloud and rely on a growing array of software-as-a-service (SaaS) applications to manage and access sensitive information, identities are the ties that bind all these systems together. Adversaries have quickly learned that these systems house the information they want and that valid and authorized identities are the most expedient and reliable way into those systems. Identity and access management (IAM) technologies, single sign-on (SSO) solutions, and other similar tools have been a boon to the security and IT professionals tasked with managing and securing corporate identities. However, they also present an opportunity for adversaries to potentially gain access to numerous disparate systems by compromising a single, highly privileged identity. 

TREND
18
2024 Threat Detection Report

How do adversaries compromise identities? 
Adversaries can wield relatively unsophisticated and well-known techniques to wrest control of user identities and cause disproportionate harm to organizations. The increasing ubiquity of multi-factor authentication (MFA) has thankfully complicated the matter, but creative MFA bypass techniques are a major commonality among identity compromises. Adversaries are getting better at abusing the difficult-to-monitor mobile devices we frequently use for MFA in order to circumvent imperfect implementations.

Of course, an adversary must have working credentials before they’re able to circumvent MFA. Methods of obtaining credentials aren’t new. While Red Canary doesn’t necessarily have comprehensive visibility into all of the ways that adversaries might steal credentials, we know from inference, experience, and public reporting that credential stuffing or spraying, social engineering, and phishing are common techniques. Adversaries can also obtain credentials through leaked data, via previously compromised systems, by purchasing them on criminal forums, and from countless other sources. 

Working credentials are often just the beginning for adversaries, who must overcome a gauntlet of additional security controls—most notably MFA—before they are able to compromise an identity. 

What we saw and heard in 2023: 
Credential theft 
Credential theft tradecraft is well-worn and discussed elsewhere in this and previous reports. No particular methods of credential theft stood out as new, novel, or emergent in 2023. Adversaries continue to steal credentials through familiar means, like:
- phishing
- malware 
- data leaks
- brute-force attacks
- man-in-the-middle (MitM) attacks
- watering-hole attacks
- previously compromised systems

We’re opting not to spend a great deal of time in this section on credential theft in favor of new or emerging ways that adversaries get around MFA and the specific elements of the login process that we often rely on to differentiate legitimate login attempts from suspicious ones. For more information on how adversaries steal credentials, refer to the following
19
2024 Threat Detection Report

sections from this and past Threat Detection Reports:
- T1003: OS Credential Dumping
- T1003.003: LSASS Memory 
- Initial access tradecraft
- Stealers
- Mimikatz
- Impacket

Exploiting help desk and technical support employees 
Phishing help desk and technical support employees to trick them into registering new MFA devices was probably the most noteworthy identity attack trend—and maybe even overall security trend—of 2023. While Red Canary isn’t well-positioned to observe this directly, we know from incident work and external reporting that adversaries target help desk employees via phone-call based phishing (“vishing”), pretending to be legitimate employees, and request critical changes to identity controls like identity access management (IAM) and MFA in order to take control of identities and gain access to victim infrastructure through SSO and other means. To accomplish their day-to-day tasks, help desk employees often require sensitive permissions like being able to perform password resets, modify IAM role assignments, and register and deregister MFA devices. The increasing prevalence of these attacks against the help desk behooves IT and security teams to place increased scrutiny on securing and properly permissioning help desk accounts, as adversaries are clearly keen on abusing them to reset the passwords and MFA registrations of high-value accounts. 

The way it works is simple: Adversaries call the help desk, posing as an internal employee in order to trick them into unwittingly resetting the victim account’s MFA settings. Next, the adversary will register their own mobile device, thereby gaining unauthorized access to a corporate identity by fundamentally modifying the authentication sequence. Once they gain access, the adversary can perform reconnaissance to profile the 
“Phishing help desk and technical support employees to trick them into registering new MFA devices was probably the most noteworthy identity attack trend—and maybe even overall security trend—of 2023.”

What we saw and heard in 2023: MFA abuse
Red Canary doesn’t have reliable visibility into many varieties of MFA bypass attempts, particularly those that rely extensively on social engineering or take place on unmonitored or difficult-to-monitor mobile devices. However, we’ve performed extensive research into MFA abuse so that we can build detective and preventive controls to stop identity compromise attempts, we’ve received anecdotal reports from customers and partners about the MFA abuse they’ve experienced, and we pay close attention to industry reporting on the matter. The following sections highlight a few techniques that took center stage in 2023.
20
2024 Threat Detection Report

environment for potential infrastructure targets or additional victims with elevated permission levels, such as those with administrative accounts. In some cases adversaries pivot into additional SaaS applications to steal data. In other cases they may move directly into cloud providers, spinning up virtual machines to mine cryptocurrency, accessing databases to steal or otherwise access sensitive information, or simply deleting systems to cause destruction or elicit a ransom. 

This relatively unsophisticated phishing method has proven highly effective, emphasizing the need for enhanced user education and robust security measures to mitigate the risk posed by simple social engineering attacks. See the Take action section below for guidance on combating help desk and tech support social engineering. 

SIM swapping 
Mobile carriers are responsible for another glaring weakness in the identity security ecosystem, and one that corporate security teams can do precious little to mitigate. SIM card swapping has long been a major problem for consumers, particularly in the online banking and cryptocurrency space, where mobile devices play a critical role in backing up account access. However, there’s real concern here for enterprises as well, since SIM swapping can enable adversaries to commandeer mobile phone numbers, hurdling MFA protections and taking over accounts. As such, it’s important to include mobile carriers as an integral component of an enterprise’s comprehensive risk profile because a carrier’s failure to accurately verify their users’ identities can have an impact on enterprises with little or no connection to that carrier.

SIM swapping effectively enables adversaries to take advantage of MFA factors like SMS one-time passcode (OTP). They do this by social engineering mobile service providers into switching their victim’s registered phone number to a new SIM card controlled by the adversary, thus allowing them to receive calls and text messages sent to the victim, including MFA codes sent over SMS or phone calls. A successful SIM swap can be complex because it may require extensive upfront reconnaissance of the victim, although the FBI has reported this can be just as readily accomplished via bribery and insider threats. 

SIM swapping a highly privileged user can potentially offer adversaries untold access to an enterprise environment, where they can then exfiltrate data, surveil the contents of communications, and more. See the Take action section below for guidance on combating SIM swapping. 

Good old-fashion phishing 
Given the phenomena of oversharing on social media, the preponderance of data leaks over the last two decades, and the wide availability of legal data brokers, it’s never been easier to find someone’s
21
2024 Threat Detection Report

contact information openly available on the internet. By extension, it’s trivial to simply contact a target via an email address, social media handle, or a mobile phone number and attempt to phish them directly for their credentials, MFA authentication codes, or both. Depending on the MFA factor the adversary needs to satisfy, they can adjust their communication strategies accordingly. 

Less glamorous than help desk social engineering or SIM swapping, socially engineering users directly remains extremely effective. Victims commonly receive either a text message (smishing) or a phone call instructing them to relay an MFA code in response to a prompt initiated by the adversary. The adversary may ask the victim to enter a number-matching code, send the adversary a newly received SMS code, or have the victim simply accept an MFA push notification. If successful, adversaries are then able to move forward with their objectives, acting with the full rights and privileges of the compromised user identity. 

Another clever phishing mechanism leverages legitimate business chat applications that are configured to allow non-employees to initiate chat sessions with employees. In this scenario, adversaries can masquerade as help desk or IT staff and attempt to phish the employee out of their credentials and/or MFA code by a variety of means. In this and a wide variety of other phishing schemes, the adversary attempts to entice their victim into entering their credentials and their MFA codes into a malicious phishing site that mimics a legitimate service. In this type of man-in-the-middle (MitM) attack, the adversary hopes that the victim will enter their credentials and respond to the corresponding MFA prompt, but instead of logging into the legitimate service, the adversary will siphon off the access token of that session and use it to log into an identity provider. 

What we saw and heard in 2023: 
Suspicious and malicious logins 
As we’ve noted previously, our visibility into credential theft and MFA bypassing is limited, and therefore much of the information above is based on anecdotal or third-party accounts. However, we do have deep visibility into the actual process of a user logging in, which we routinely leverage for detection and response. The overwhelming majority of suspicious login attempts fall into just four categories that will be familiar to nearly anyone who’s ever worked in a security operations center:
- login attempts from unfamiliar locations
- concurrent login attempts from disparate geographic locations
- logins from malicious IP spaces or those associated with suspicious hosting or VPN services
- logins occurring in tandem with high volumes or MFA requests

See the Take action section on the next page for guidance on leveraging identity telemetry and alerts to prevent or detect suspicious login attempts.
22
2024 Threat Detection Report

TAKE ACTION
Visit the Identity attacks trend page for relevant atomic tests to validate your coverage. 

In this section, we’ll offer guidance on how security teams can attempt to mitigate the MFA circumvention, credential