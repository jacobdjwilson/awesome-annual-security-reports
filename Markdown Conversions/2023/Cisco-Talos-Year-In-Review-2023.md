# 2023 YEAR IN REVIEW

## Table of Contents
- [Introduction](#introduction)
- [Telemetry trends](#telemetry-trends)
- [Ransomware and extortion](#ransomware-and-extortion)
- [Network infrastructure](#network-infrastructure)
- [APTs: China](#apts-china)
- [APTs: Russia](#apts-russia)
- [APTs: Middle East](#apts-middle-east)
- [Commodity loaders: Qakbot, Emotet, Trickbot, IcedID, Ursnif](#commodity-loaders-qakbot-emotet-trickbot-icedid-ursnif)

## Introduction
page 2
© 2023 Cisco and/or its affiliates. All rights reserved.  |  talosintelligence.com

2023
YEAR IN REVIEW

Cisco’s global presence and Talos’ world-class expertise provided a massive amount of data to sift through — endpoint detections, incident response engagements, network traffic, email corpus, sandboxes, honeypots and much more. Thankfully, our teammates include subject matter experts from all ends of the cybersecurity space to help us turn this intelligence into actionable information for defenders and users. Leveraging these rich, complex sources of information, we analyzed the major trends that shaped the threat landscape in 2023.

Ransomware continued to threaten enterprises globally in 2023, with LockBit remaining the top threat in this space for the second year in a row. Health care was the top targeted industry this year, as adversaries maintained their focus on entities that have cybersecurity funding constraints and low downtime tolerance. Not all things were the same, though, as we saw actors such as Clop deploy a collection of zero-day exploits, behavior we usually associate with advanced persistent threat (APT) activity. At the same time, leaked ransomware source code allowed low-skilled actors to enter the fray. Further complicating matters, we observed a new trend of ransomware actors turning to pure extortion, skipping encryption altogether while threatening to leak sensitive data.

Commodity loaders are still being used to deliver these ransomware threats, and many of the same families as last year remained prevalent, such as Qakbot and IcedID. This is reflected in our telemetry, as the most commonly spoofed brands were in financial services and shipping, hallmarks of these adversaries. But these loaders are shedding all remnants of their banking trojan past as they position themselves more as sleek payload delivery mechanisms. Developers and operators are adapting to improved defenses, finding new ways to bypass increasing security updates and compromise victims. And although we again observed a takedown of a large botnet, this year being Qakbot, our experience shows that this does not necessarily mean that the threat has been eliminated.

One of the newer cross-regional trends we have observed this year is an increase in the targeting of network devices from APTs and ransomware actors. Both groups rely on exploiting recently disclosed vulnerabilities and weak/default credentials, one of the reasons why the use of valid accounts was consistently a top weakness in Talos IR engagements. Whatever the sophistication and intent of the adversary is, the reason behind the targeting is the same: network devices are extremely high value while possessing many security weaknesses.

Geopolitical instability is manifesting in APT activity. This is reflected in our telemetry, which shows a rise in suspicious traffic during major geopolitical events. For Chinese groups, as relationships with the West and Asia Pacific become further strained, we see an emboldening in operations, such as a greater willingness to cause destruction. We also observe this in their targeting of telecommunications organizations, which possess numerous critical infrastructure assets in strategically important geographies such as Guam and Taiwan. For Russian APTs, Gamaredon and Turla targeted Ukraine at an accelerated pace, but Russian activity in general for 2023 did not reflect the full range of destructive cyber capabilities we have seen it deploy in the past, potentially because of the concerted efforts of defenders.

One bright spot this year was Cisco’s determined efforts to create and deliver inventive security solutions that help strengthen our partners. Talos’ Ukraine Task Force continues to thwart attacks against critical Ukrainian partners. This year, we spear-headed an effort to stabilize Ukraine’s power grid against the effects of global positioning system (GPS) jamming on the battlefield by delivering modified Cisco switches into an active war zone. Cisco also launched the Network Resilience Coalition with leading industry partners, focusing on increasing awareness and providing actionable recommendations for improving network security. Relatedly, Talos’s Vulnerability Discovery and Research Team made investigating small office, home office (SOHO) and industrial routers a major priority, reporting 289 vulnerabilities to vendors to date, published across 141 Talos advisories.

As conflict in the Middle East worsens, we are once again positioned to help protect our customers and partners. Therefore, perhaps the overarching story of 2023 is this: as the daringness, sophistication, and persistence of our adversaries grows, so too does the resolve of defenders to interdict them in any way we can.

Ransomware, commodity loaders and APTs dominated the threat landscape in 2023. As we’ll outline in the second annual Cisco Talos Year in Review, global conflict influenced cybersecurity trends, shifting many threat actors’ tactics and approaches in operations ranging from espionage to cybercrime.

## Table of contents
Telemetry trends.................................................... 3
Strategic findings and trends based on our vast data sets.
Ransomware and extortion.................................... 8
A look at major changes and top players we observed in this dynamic threat space.
Network infrastructure......................................... 13
Threat actor and attack trends related to frequent, high-impact attacks on network devices.
APTs: China........................................................... 18
Analysis on Chinese adversaries, including victimology and increased pace of operations.
APTs: Russia......................................................... 21
Major players, top threats and trends from our Ukraine Task Force and global monitoring efforts.
APTs: Middle East................................................. 28
A preview of the complex and often dire political climate that impacts the cyber threat landscape.
Commodity loaders: Qakbot, Emotet, Trickbot, IcedID, Ursnif ............. 32
Major developments for these common threats, including activity trends and changes in TTPs.

## Telemetry trends
page 3
© 2023 Cisco and/or its affiliates. All rights reserved.  |  talosintelligence.com

Subhead herelyhere
2023
YEAR IN REVIEW

Section highlights
- Suspicious network traffic captured by Cisco Security products revealed sharp increases in activity that often corresponded with major geopolitical events and global cyber attacks.
- The most targeted vulnerabilities were older security flaws in common applications, consistent with the U.S. Cybersecurity and Infrastructure Security Agency’s (CISA) findings in recent years. Most of the top-targeted vulnerabilities we observed received maximum- or high-severity scores by Cisco Kenna and the Common Vulnerability Scoring System (CVSS) and were also included in CISA’s Known Exploited Vulnerabilities catalog. The high frequency of targeting attempts against these CVEs, paired with their significant impact, underscores adversaries’ preference to target unpatched systems that can cause major disruptions.
- Threat actors abused common file extensions and spoofed well-known brands, common techniques that underscore the use of social engineering to enable operations like phishing and business email compromise (BEC). Adversaries are likely responding to Microsoft’s disabling of macros in 2022 by using different file types to hide their malware, such as PDFs, which was the top blocked file extension this year.
- Financial services and shipping companies accounted for the brands we observed being spoofed most often in email telemetry, suggesting longstanding phishing themes for email-based commodity loaders like Emotet, Qakbot and Trickbot are still at play. Relatedly, phishing accounted for a quarter of known initial access vectors in Talos IR engagements this year, highlighting actors’ continued reliance on this technique.
- The use of valid accounts was a top-observed MITRE ATT&CK technique, underscoring adversaries’ reliance on compromised credentials and use of existing accounts for various stages of their attacks. This is consistent with Talos IR data, which showed compromised credentials/valid accounts accounted for nearly a third of known initial access vectors in 2023.

YEAR IN REVIEW
2023

page 4
© 2023 Cisco and/or its affiliates. All rights reserved.  |  talosintelligence.com
2023
YEAR IN REVIEW
Telemetry trends

### Regional trends over time
Suspicious traffic includes a wide variety of categorized information sourced from multiple Cisco Security products, including Umbrella, Secure Endpoint, Email Security Appliance (ESA), Meraki, SSE and Secure Firewall. Examples include malicious domains blocked by Umbrella, records with malicious dispositions from Secure Endpoint, phishing emails from ESA, triggered Snort signatures from Secure Firewall and Meraki, and many others.

In North America, Europe, the Middle East and Africa (EMEA), and Latin America, suspicious network traffic was periodic, following a Monday - Friday workday pattern for much of the year. Starting mid-year, we saw a break from this pattern marked by a dramatic increase in traffic blocked by our security products, often quadrupling the early part of the year’s normal behavior.

In mid-February, these regions experienced various spikes in web spam. While spam volume was up globally, it disproportionally affected the Asia Pacific, Japan and China (APJC) region.

In APJC, suspicious traffic was less periodic and experienced large swings in volume between January and April. These changes leveled out through the spring and early summer.

Various international events and major cyber attacks overlayed on the graph suggest how such activity can affect the threat landscape. While it’s impossible to prove causation, there are obvious correlations between the suspicious global and regional traffic patterns we observed and significant world events.

![Graph showing the Volume of suspicious activity by Month (2023) and region. Regions are North America (NA), Asia Pacific, Japan and China (APJC), Europe, the Middle East and Africa (EMEA), and Latin America (LATAM). Events are marked on the graph including: Chinese President Xi Jinping meets with Russian President Vladimir Putin in Russia, while Japanese Prime Minister visits Ukraine in dueling diplomatic efforts; China brokers Iran-Saudi Arabia mediation; Chinese President Xi Jinping elected to a third five-year term; Clop ransomware actors begin exploiting zero-day vulnerability in the MOVEit file transfer software affecting hundreds of organizations; Ukrainian miliary begins counteroffensive to reclaim Russian-held territory; Anonymous Sudan claims DDoS attacks against Microsoft Outlook; Rebels depose Niger’s Western-allied president, causing global security implications; New Rhysida ransomware group likely responsible for attack that disrupts several U.S. hospitals; U.S., Japan, and South Korea presidents meet at summit aimed at countering threats from China and North Korea; Powerful earthquake kills more than 40,000 people in Turkey and Syria, prompting humanitarian crisis that threat actors commonly exploit for financial gain; U.S. downs suspected Chinese spy balloon, sparking international incident; “ESXiArgs” ransomware attacks infect thousands of servers worldwide.]

page 5
© 2023 Cisco and/or its affiliates. All rights reserved.  |  talosintelligence.com
2023
YEAR IN REVIEW
Telemetry trends

### Top targeted vulnerabilities
In 2023, cyber threat actors exploited older software vulnerabilities in common applications. In many cases, the vulnerabilities were more than 10 years old, consistent with CISA’s finding that adversaries have targeted old security flaws more than newly disclosed ones in recent years. In fact, four of the top five most-targeted vulnerabilities we observed were also cited by CISA as being frequently exploited in prior years, further highlighting this point. This underscores the need for entities to regularly install software updates, as many of these systems were likely unpatched given the age of the targeted vulnerabilities.

The top targeted vulnerabilities are found in common applications, like Microsoft Office. This finding is also substantiated by CISA, which noted that actors in 2022 prioritize CVEs that are more prevalent in their targets’ networks. Adversaries likely prioritize targeting widespread vulnerabilities because the exploits developed for such CVEs can have long-term use and high impact.

Lastly, most of the vulnerabilities on our list would cause substantial impact if exploited, with six receiving a maximum vulnerability risk score of 100 from Cisco Kenna and seven receiving the highest “critical” score from the Common Vulnerability Scoring System (CVSS). Most of the CVEs are also listed in CISA’s Known Exploited Vulnerabilities catalog, which is meant to inform users on the security flaws for which they should prioritize remediation. The high frequency of targeting attempts against these CVEs, paired with their severity, underscores the risk to unpatched systems.

| Ranking | CVE | Vendor | Product | CISA findings | CISA KEV catalog | Kenna/CVSS |
|---|---|---|---|---|---|---|
| 1 | CVE-2017-0199 | Microsoft | Office and WordPad | Routinely exploited in 2022 |  | 100/9.3 |
| 2 | CVE-2017-11882 | Microsoft | Exchange server | Routinely exploited in 2022 |  | 100/9.3+ |
| 3 | CVE-2020-1472 | Microsoft | Netlogon | Routinely exploited in 2022 |  | 100/9.3 |
| 4 | CVE-2012-1461 | Gzip file parser utility | Multiple antivirus products |  |  | 58/4.3 |
| 5 | CVE-2012-0158 | Microsoft | Office | Commonly exploited by state-sponsored actors from China, Iran, North Korea, and Russia (2016-2019) |  | 100/9.3 |
| 6 | CVE-2010-1807 | Apple | Safari |  |  | 84/9.3 |
| 7 | CVE-2021-1675 | Microsoft | Windows (print spooler) |  |  | 100/9.3 |
| 8 | CVE-2015-1701 | Microsoft | Windows (kernel-mode driver) |  |  | 72/7.2 |
| 9 | CVE-2012-0507 | Oracle | Java SE |  |  | 100/10 |
| 10 | CVE-2015-2426 | Microsoft | Windows (font driver) |  |  | 100/9.3 |

Source: Cisco Secure Endpoint
CISA sources: Top Routinely Exploited Vulnerabilities, 2022 and 2016-2019.

page 6
© 2023 Cisco and/or its affiliates. All rights reserved.  |  talosintelligence.com
2023
YEAR IN REVIEW
Telemetry trends

### Email findings
TOP INITIAL ACCESS VECTORS, ACCORDING TO TALOS IR

TOP BRANDS SPOOFED IN SENDER NAMES

Cybercriminals and other malicious actors rely heavily on social engineering tactics to compromise users, which is why they commonly imitate well-known companies in their phishing emails. Commodity loaders like Emotet, Qakbot and Trickbot, for instance, routinely use fake invoices, bank statements, or shipping notifications as phishing themes to feign legitimacy. This is reflected in our list of top spoofed brands, where we see that financial services entities and shipping services were among those that actors most frequently spoofed.

Business email compromise (BEC) operations also leverage spoofed company names to enhance legitimacy. BEC is a scam in which cybercriminals send emails to targets that appear to come from a known source making a legitimate request. The goal is to prompt the target to make unauthorized money transfers to the threat actor. Actors may impersonate well-known and trusted brands, like those represented in our list, to trick users. BEC has been on the rise in recent years, according to the FBI, and resulting in $2.7 billion in losses in 2022.

Note: Initial access vector is often hard to determine due to a variety of reasons — including insufficient logging or lack of visibility into the affected environment — resulting in “unknown” being highly represented.
Source: Cisco Email Security Appliance

TOP BLOCKED ATTACHMENT FILE EXTENSIONS

Phishing emails are one of the most common ways adversaries compromise victims and this has consistently been a top-ranked threat in Talos IR findings for years. In the last year alone, 25 percent of the initial access vectors identified in Talos IR engagements were comprised of phishing (this refers to chart 3b). This observation is consistent with U.S. government findings, with the FBI noting that phishing was the top incident reported to its Internet Crime Complaint Center (IC3) in 2022.

Threat actors commonly send unsolicited emails requesting users download or open an attachment to deliver malware. While file extension is not necessarily indicative of file type, actors frequently try to hide malware under well-known file extensions to appear less suspicious, so users are more likely to open them. For example, earlier this year, Japan’s Computer Emergency Response Team (JP-CERT) warned that adversaries were embedding malicious Word documents in PDF files to bypass detection, a strategy we have seen threat actors rely on for years.

Threat actors’ file type preference was also likely affected by Microsoft’s 2022 decision to block macros, which adversaries had heavily abused up to that point. With this change, actors have moved away from using Microsoft Office files like Word and Excel as frequently as they once did. In 2023, we saw the commodity loader Ursnif incorporate malicious PDF attachments into their phishing operations for the first time as this actor and other groups looked for ways to avoid relying on macros.

Source: Cisco Email Security Appliance
Note: Common image-related filetypes — like JPG, JPEG, PNG and GIF — were excluded from this list because they appear frequently in an overwhelmingly high volume of benign emails, such as those containing graphics in senders’ signatures or in the email body.

![Pie chart showing top blocked attachment file extensions. 36% PDF, 32% Other, 14% HTML, 8% HTM, 5% DOCX, 5% ZIP]

![Bar chart showing top initial access vectors according to Talos IR. 36% Unknown, 28% Exploit vulnerability in public-facing application, 23% Compromised credentials on valid accounts, 19% Phishing, 6% Drive-by compromise]

![List of top brands spoofed in sender names. DocuSign, FedEx, Banco Bradesco, Walmart, DHL, Aeon, American Airlines, Royal Bank of Canada, Bank of America, Paypal, Capital One, Western Union, Google, American Express, AT&T]

page 7
© 2023 Cisco and/or its affiliates. All rights reserved.  |  talosintelligence.com
2023
YEAR IN REVIEW
Telemetry trends

Hijack execution flow was the most common technique, appearing nearly twice as often as the next highest result. Hijacking execution flow refers to actors co-opting the way an operating system runs programs on a target endpoint. DLL side-loading is a common example of this, whereby actors essentially position their malware alongside the victim application so that when the program searches for its legitimate DLL, it also unwittingly executes the malicious payload. This is an effective way for actors to hide their activities under legitimate and trusted software, a technique we commonly see leveraged by APTs and cybercriminals.

The use of valid accounts was the second-most common technique we observed, underscoring adversaries’ reliance on compromised credentials and use of existing accounts. Actors use this technique to enable various stages of the attack chain. We commonly see commodity loaders deploying information-stealing malware for this very purpose. Relatedly, credentials from password stores ranked in the top five, further highlighting actors’ focus on obtaining user credentials. These findings are consistent with Talos IR data, which showed compromised credentials/valid accounts accounted for nearly a quarter of known initial access vectors in 2023.

Resource hijacking, which ranked in the top 10, is a technique we typically see associated with the deployment of cryptocurrency mining malware, which hijacks an endpoint’s processing power for profitable gains. Cryptocurrency mining threats are highly common, as this is a low-level type of attack typically carried out by unsophisticated actors. We often see this type of malware deployed, especially soon after new vulnerabilities are disclosed, before victims have time to patch and/or in conjunction with other, more complex, malware.

### Top MITRE ATT&CK techniques
Notably, nearly a third of the top 20 most common MITRE ATT&CK techniques fall under the defense evasion tactic, suggesting actors are devoting substantial resources to this phase of the attack chain. Techniques relating to privilege escalation and persistence also ranked high, highlighting their importance in the attack lifecycle.

| Techniques | Tactic |
|---|---|
| T1480, Execution Guardrails | Defense evasion |
| T1564, Hide Artifacts | Defense evasion |
| T1222, File and Directory Permissions Modification | Defense evasion |
| T1558, Steal or Forge Kerberos Tickets | Credential access |
| T1555, Credentials from Password Stores | Credential access |
| T1059, Command and Scripting Interpreter | Execution |
| T1496, Resource Hijacking | Impact |
| T1072, Software Deployment Tools | Persistence |
| T1021, Remote Services | Lateral movement |
| T1068, Exploitation for Privilege Escalation | Privilege escalation |
| T1055, Process Injection | Defense evasion |
| T1135, Network Share Discovery | Discovery |
| T1124, System Time Discovery | Discovery |
| T1057, Process Discovery | Discovery |
| T1102, Web Service | Command and control |
| T1113, Screen Capture | Collection |
| T1056, Input Capture | Collection |
| T1546, Event Triggered Execution | Persistence |
| T1078, Valid Accounts | Initial access |
| T1574, Hijack Execution Flow | Defense evasion |

![Bar chart showing volume of attacks using technique & associated tactics. Techniques are listed on the y-axis, and volume of attacks on the x-axis. Tactics are color coded: Defense evasion, Credential access, Collection, Command and control, Persistence, Privilege escalation, Lateral movement, Initial access, Impact, Execution, Discovery]

## Ransomware and extortion
page 8
© 2023 Cisco and/or its affiliates. All rights reserved.  |  talosintelligence.com

Subhead herelyhere
2023
YEAR IN REVIEW

Section highlights
- Ransomware and pre-ransomware incidents continue to affect customers at a consistent rate — totaling the same 20 percent of Talos IR incidents as last year — with health care being the most targeted vertical.
- For the second year in a row, LockBit was the most prolific ransomware-as-a-service (RaaS) gang, based on our findings, consistent with CISA’s assessment that it is the most deployed ransomware variant. LockBit was one of the most frequently observed ransomware threats in Talos IR this year, and affiliates accounted for more than 25 percent of the total number of victim posts on data leak sites across some 40 ransomware groups we monitor.
- ALPHV, Clop and BianLian also dominated the threat landscape, accounting for another quarter of all ransomware and/or data extortion compromises publicized on dark web actor sites.
- We saw Clop affiliates consistently exploit zero-day vulnerabilities, a highly unusual tactic given the expertise, personnel and access required to develop such exploits, suggesting the group possesses a level of sophistication and/or resources matched only by advanced persistent threats (APTs).
- New ransomware variants are emerging that leverage leaked source code from other RaaS groups, allowing less skilled actors to enter this space. At the same time, we also see highly sophisticated operators like Clop leveraging zero-day vulnerabilities at an unprecedented pace, an interesting dichotomy demonstrating the breadth of actors in this space.
- Actors are turning to data extortion more than ever, with this being the top threat that Talos IR responded to in Q2 2023 (April - June). Data theft extortion looks very similar to pre-ransomware activity, creating challenges for defenders.
- Some actors are abandoning ransomware use altogether, opting for extortion instead, a trend likely influenced by ongoing law enforcement operations, better industry detections and lower operational costs.

YEAR IN REVIEW
2023

page 9
© 2023 Cisco and/or its affiliates. All rights reserved.  |  talosintelligence.com
2023
YEAR IN REVIEW
Ransomware and extortion

### Ransomware attacks persist at steady pace
Ransomware and pre-ransomware made up 20 percent of the total incidents that Talos IR responded to this year, a very slight drop compared to last year. It can be difficult for defenders to determine what constitutes a pre-ransomware attack if a ransomware binary is never executed and encryption does not take place. However, there are some indications analysts use to assess if ransomware is the likely final objective, such as the use of adversary simulation frameworks like Cobalt Strike and/or credential-harvesting tools like Mimikatz, the targeting of certain critical assets such as backups, or enumeration and discovery techniques.

The health care and public health sector was the most targeted vertical in Talos IR ransomware and pre-ransomware engagements this year, compared to the education sector in 2022, as reported in last year’s Year in Review report (see Figure 1). Healthcare organizations are highly vulnerable to cyber attacks given their low downtime tolerance, often underfunded cybersecurity budgets, and possession of protected health information (PHI) that is valuable to threat actors. The COVID-19 pandemic likely exacerbated this situation in recent years, with healthcare providers strained from a resource perspective and downtime being even less tolerable.

### Old foes are top offenders as LockBit remains top threat
For a second year in a row, LockBit was the most active RaaS group, accounting for over 25 percent of the total number of posts made to data leak sites. LockBit, ALPHV, Clop and BianLian accounted for nearly 50 percent of the total posts made to leak sites this year (Figure 2).

The ransomware space remained dynamic in 2023, with groups continuing to rebrand or merge, actors often working for multiple ransomware-as-a-service (RaaS) outfits at a time, and new groups continually emerging. The skill levels varied greatly as well, with experienced actors developing sophisticated exploits for zero-day vulnerabilities, while less-skilled actors relied on repurposed ransomware code to create their own threats. We also saw an emerging trend in this space, as more actors began to abandon the use of ransomware and resort to pure data theft extortion without encrypting files, presenting a new line of challenges for defenders. Despite these changes, one thing remains constant: Ransomware remains a top threat to entities worldwide.

![Bar chart showing Talos IR ransomware and pre-ransomware incidents per sector. Healthcare and public health is the highest, followed by education, manufacturing, government, and other]

![Bar chart showing number of posts made to ransomware data leak sites. LockBit is the highest, followed by ALPHV, Clop, BianLian, and Other]

> “The health care and public health sector was the most targeted vertical in Talos IR ransomware and pre-ransomware engagements this year, compared to the education sector in 2022.”

page 10
© 2023 Cisco and/or its affiliates. All rights reserved.  |  talosintelligence.com
2023
YEAR IN REVIEW
Ransomware and extortion

LockBit continued to conduct prolific ransomware operations in 2023, a finding that aligns with CISA’s assessment that it is the most deployed ransomware variant. LockBit attacks can be very impactful, affecting an organization’s information technology (IT) networks and operational technology (OT), the hardware and machines responsible for physical processes, as we have observed in Talos IR engagements. In October, CISA published guidance for securing OT environments, underscoring how significant the impact can be to these systems. LockBit was also deployed during the exploitation of two vulnerabilities in the PaperCut software, a print management solution widely used across entities in the government and education verticals, among others.

Posts made to the group’s data leak site ebbed and flowed throughout the year, with detections of LockBit activity appearing

### Talos IR responds to LockBit incident affecting IT and OT networks
Talos IR responded to a LockBit ransomware incident affecting a utilities company where ransomware infiltrated the organization’s IT and OT networks, causing significant impact to the victim and downstream disruptions to customers. The ransomware affiliate gained initial access using valid router credentials authenticating over VPN where multi-factor authentication (MFA) was not implemented. The attackers encrypted production servers, including those monitoring the electrical grid, and three of four domain controllers were encrypted, as well.

to spike in March, partially coinciding with LockBit’s deployment against vulnerable instances of the printer management software PaperCut, where it has remained consistently high (Figure 3).

### Ransomware space remains crowded with new and rebranded groups
Ransomware groups’ constant rebranding and/or turnover was a prominent trend this year. Multiple leaks of ransomware source code and builders — components essential to creating and modifying ransomware — have had a significant effect on the ransomware threat landscape. These leaks allow ransomware operators to rebrand or give unsophisticated actors the ability to generate their own ransomware more easily with little effort or knowledge. As more actors enter this space, Talos is seeing an increasing number of ransomware variants emerge leveraging leaked ransomware code, often leading to more frequent attacks and new challenges for cybersecurity professionals and defenders, particularly regarding actor attribution.

The volume of new ransomware variants based on leaked source code also highlights the speed at which actors take advantage of such public disclosures. Most recently, we observed a surge in new ransomware strains emerging from the Yashma ransomware builder. First appearing in May 2022, Yashma is a rebranded version of the Chaos ransomware builder (v5), which was leaked in April 2022. Since early 2023, we have seen several new Yashma strains emerge, including ANXZ and Sirattacker, likely deployed by smaller or groups of affiliates with fewer resources given their lack of widespread adoption and notoriety in the landscape. In April, we discovered a new ransomware actor,

![Line graph showing LockBit activity throughout the year. Activity is measured by number of posts made to data leak sites. Spikes in activity are noted in March and throughout the second half of the year.]

page 11
© 2023 Cisco and/or its affiliates. All rights reserved.  |  talosintelligence.com
2023
YEAR IN REVIEW
Ransomware and extortion

RA Group, deploying their ransomware variant based on the leaked Babuk source code. Since an alleged member of the Babuk group leaked the full source code of its ransomware in September 2021, several new variants based on the leaked code have emerged, with many appearing in 2023, including ESXiArgs, Rorschach and RTM Locker.

While these changes in the threat landscape have largely benefitted affiliates, security researchers and defenders also have an advantage with access to the leaked code. It allows security researchers to analyze the source code and understand the attacker’s TTPs and develop effective detection rules, potentially aid in the creation of decryptors and enhance security products’ capabilities in combating ransomware threats.

### Affiliates turning to data theft extortion over ransomware deployment
Even with the expanding number of RaaS options, some have found success in extorting funds without deploying ransomware. In these extortion instances, an adversary steals the victim’s data but does not encrypt it. The common double extortion tactic is thereby eliminated, with the actor relying solely on the threat of leaking the information rather than also demanding payment to unlock the files. This trend is also reflected in Talos IR engagements, where extortion was the most observed threat in Q2 2023, accounting for almost a third of threats seen, a 25 percent increase from the prior quarter (January-April) (Figure 4).

Several well-known ransomware gangs — including Babuk, BianLian and Clop — have opted for data theft extortion over ransomware, a departure from the groups’ typical ransomware attack chain (Figure 5).

Several factors have likely contributed to some threat actors’ preferences for data theft extortion instead of deploying ransomware. U.S. and international law enforcement have aggressively pursued ransomware actors in recent years, conducting major disruptions against well-known groups. Advancements in endpoint detection and response (EDR) capabilities have likely been a significant obstacle for threat actors seeking to deploy ransomware and encrypt data. Adversaries appear to consider the technique a viable way to receive a payout, demonstrating how ransomware actors are constantly working around advancements in EDR, law enforcement operations and other barriers.

While extortion has proven to be a serious and effective threat, it has not yet outpaced the ransomware threat that has been a challenge for organizations and defenders for the past several years. We are continuing to monitor the long-term effects of this trend.

### Some ransomware groups consistently leverage zero-days, often affecting multiple organizations
While many inexperienced adversaries relied on code reuse this year, we also continued to see highly sophisticated operators exploiting zero-day vulnerabilities at an unprecedented pace, highlighting the broad technical diversity of actors and TTPs in this space. Ransomware actors, well-known for being opportunistic, are quick to exploit flaws when made public. When Clop, a high-profile ransomware

### What is the impact of leaked ransomware source code?
When ransomware source code or builders are leaked, it becomes easier for aspiring cybercriminals who lack the technical expertise to develop their own ransomware variants by making only minor modifications to the original code. Additionally, by using leaked source code, threat actors can confuse or mislead investigators, as security professionals may be more likely to misattribute the activity to the wrong actor.

(From research posted on the Talos blog)

![Bar chart showing data theft extortion was the top threat in Q2 (April - June 2023), according to Talos IR. Data theft extortion is the highest, followed by ransomware, commodity loader, and other.]

![Bar chart showing prominent groups increasingly turn to data theft extortion in recent years. Babuk, BianLian, and Clop are the highest, followed by other]

page 12
© 2023 Cisco and/or its affiliates. All rights reserved.  |  talosintelligence.com
2023
YEAR IN REVIEW
Ransomware and extortion

and data extortion group, claims public responsibility for exploiting a zero-day vulnerability, additional ransomware affiliates quickly follow suit, scanning for affected systems before patches are issued (Figure 6).

In April, shortly after print management software company PaperCut became aware of unpatched servers being exploited in the wild by Clop, other ransomware groups began to exploit the critical remote code execution (RCE) vulnerability (CVE-2023-27350) as part of their attack chain. This highlights the widespread nature of this activity and ransomware operators’ strategy, often based on the disclosure of other groups leveraging high-profile security flaws to increase chances of eliciting payouts from victims.

Clop’s repeated efforts to exploit zero-day vulnerabilities is highly unusual for a ransomware group given the resources required to develop such capabilities. We saw many instances of this in 2023, beginning in January, when the Clop ransomware group launched a campaign leveraging a zero-day vulnerability, (CVE-2023-0669) to target the GoAnywhere MFT platform. In May, Clop claimed responsibility for attacks involving another zero-day flaw (CVE-2023-34362) affecting Progress Software’s file transfer solution, MOVEit Transfer. These attacks also demonstrate Clop’s expanded toolkit, as the operators deployed a previously unseen web shell, dubbed LemurLoot, to exfiltrate victims’ data and extort payments on systems running MOVEit.

The vulnerabilities leveraged by ransomware affiliates/groups highlighted above all received high- or critical-severity CVSS scores, were found to be easily exploitable by Cisco Kenna, and were included in CISA’s Known Exploited Vulnerabilities catalog.

Given the resources required to develop or identify such exploits, it is possible that Clop, and/or certain members, possess a level of sophistication and funding matched only by APTs. There is no known chatter on underground forums about how Clop may have obtained these exploits, though we assess the group may have access to a sophisticated developer that appears to be focusing on identifying vulnerabilities in third-party file management systems and other network peripherals.

### Landscape shifts in the RaaS space due to law enforcement disruptions
Ransomware groups experienced disruptions, forcing them to adapt and/or join other RaaS outfits. In January 2023, the U.S. Justice Department announced it had disrupted the Hive ransomware group. By late January, we saw this reflected in our data, with a general dropoff in posts made to Hive’s data leak site (Figure 7).

When ransomware infrastructure gets disrupted, operators often continue their work with other groups, creating a whack-a-mole scenario for law enforcement and network defenders. For example, when Hive’s infrastructure was disrupted, many former Hive members attempted to join other ransomware groups within days of the disruption, according to our sources. This greater democratization, with an influx of new groups leveraging code from the same ransomware builders, introduces complexities for defenders attributing activity to specific groups as TTPs remain consistent across groups.

![Timeline of ransomware groups leveraging notable vulnerabilities. Clop exploited CVE-2023-0669 in January, PaperCut CVE-2023-27350 in April