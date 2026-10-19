# Cisco Talos 2023 Year in Review

## Table of Contents
- [Introduction](#introduction)
  - [Original Report Table of Contents](#original-report-table-of-contents)
- [Telemetry Trends](#telemetry-trends)
  - [Section Highlights](#section-highlights)
  - [Regional Trends Over Time](#regional-trends-over-time)
  - [Top Targeted Vulnerabilities](#top-targeted-vulnerabilities)
  - [Email Findings](#email-findings)
  - [Top MITRE ATT&CK Techniques](#top-mitre-attck-techniques)
- [Ransomware and Extortion](#ransomware-and-extortion)
  - [Section Highlights](#section-highlights-1)
  - [Ransomware Attacks Persist at Steady Pace](#ransomware-attacks-persist-at-steady-pace)
  - [Old Foes Are Top Offenders as LockBit Remains Top Threat](#old-foes-are-top-offenders-as-lockbit-remains-top-threat)
  - [Ransomware Space Remains Crowded with New and Rebranded Groups](#ransomware-space-remains-crowded-with-new-and-rebranded-groups)
  - [Affiliates Turning to Data Theft Extortion over Ransomware Deployment](#affiliates-turning-to-data-theft-extortion-over-ransomware-deployment)
  - [Some Ransomware Groups Consistently Leverage Zero-Days, Often Affecting Multiple Organizations](#some-ransomware-groups-consistently-leverage-zero-days-often-affecting-multiple-organizations)
  - [Landscape Shifts in the RaaS Space Due to Law Enforcement Disruptions](#landscape-shifts-in-the-raas-space-due-to-law-enforcement-disruptions)
- [Network Infrastructure](#network-infrastructure)
  - [Section Highlights](#section-highlights-2)
  - [Weak Security Often Exploited for Initial Access](#weak-security-often-exploited-for-initial-access)
  - [Exploitation of Vulnerabilities Spike After Public Disclosure](#exploitation-of-vulnerabilities-spike-after-public-disclosure)
  - [Top Vulnerabilities Targeted Are Highly Critical, Easily Exploitable and Widespread](#top-vulnerabilities-targeted-are-highly-critical-easily-exploitable-and-widespread)
  - [Malware Sometimes Installed Post-Compromise to Establish Footholds](#malware-sometimes-installed-post-compromise-to-establish-footholds)
  - [Collection of Network Information Essential to High-Stakes Operations](#collection-of-network-information-essential-to-high-stakes-operations)
  - [Numerous Compromised Devices Form Anonymizing Network for Malicious Traffic](#numerous-compromised-devices-form-anonymizing-network-for-malicious-traffic)
  - [How Are We Countering This Growing Threat?](#how-are-we-countering-this-growing-threat)
  - [Ransomware Actors and Initial Access Brokers Abuse Weak Credentials and Monetize Access](#ransomware-actors-and-initial-access-brokers-abuse-weak-credentials-and-monetize-access)
- [Advanced Persistent Threats: China](#advanced-persistent-threats-china)
  - [Section Highlights](#section-highlights-3)
  - [TTPs Largely Centered on Evading Detection and Attribution](#ttps-largely-centered-on-evading-detection-and-attribution)
  - [New Trend of Ransomware Deployment Following Long-Term Espionage Operations](#new-trend-of-ransomware-deployment-following-long-term-espionage-operations)
  - [More Rigorous Pace of Operations Likely Linked to Shifts in Geopolitical Environment](#more-rigorous-pace-of-operations-likely-linked-to-shifts-in-geopolitical-environment)

---

## Introduction

Ransomware, commodity loaders and APTs dominated the threat landscape in 2023. As we’ll outline in the second annual Cisco Talos Year in Review, global conflict influenced cybersecurity trends, shifting many threat actors’ tactics and approaches in operations ranging from espionage to cybercrime.

Cisco’s global presence and Talos’ collection of world-class expertise provided a massive amount of data to sift through — endpoint detections, incident response engagements, network traffic, email corpus, sandboxes, honeypots and much more. Thankfully, our teammates include subject matter experts from all ends of the cybersecurity space to help us turn this intelligence into actionable information for defenders and users. Leveraging these rich, complex sources of information, we analyzed the major trends that shaped the threat landscape in 2023.

Ransomware continued to threaten enterprises globally in 2023, with LockBit remaining the top threat in this space for the second year in a row. Health care was the top targeted industry this year, as adversaries maintained their focus on entities that have cybersecurity funding constraints and low downtime tolerance. Not all things were the same, though, as we saw actors such as Clop deploy a zero-day exploits, behavior we usually associate with advanced persistent threat (APT) activity. At the same time, leaked ransomware source code allowed low-skilled actors to enter the fray. Further complicating matters, we observed a new trend of ransomware actors turning to pure extortion, skipping encryption altogether while threatening to leak sensitive data.

Commodity loaders are still being used to deliver these ransomware threats, and many of the same families as last year remained prevalent, such as Qakbot and IcedID. This is reflected in our telemetry, as the most commonly spoofed brands were in financial services and shipping, hallmarks of these adversaries. But these loaders are shedding all remnants of their banking trojan past as they position themselves more as sleek payload delivery mechanisms. Developers and operators are adapting to improved defenses, finding new ways to bypass increasing security updates and compromise victims. And although we again observed a takedown of a large botnet, this year being Qakbot, our experience shows that this does not necessarily mean that the threat has been eliminated.

One of the newer cross-regional trends we have observed this year is an increase in the targeting of network devices from APTs and ransomware actors. Both groups rely on exploiting recently disclosed vulnerabilities and weak/default credentials, one of the reasons why the use of valid accounts was consistently a top weakness in Talos IR engagements. Whatever the sophistication and intent of the adversary is, the reason behind the targeting is the same: network devices are extremely high value while possessing many security weaknesses.

Geopolitical instability is manifesting in APT activity. This is reflected in our telemetry, which shows a rise in suspicious traffic during major geopolitical events. For Chinese groups, as relationships with the West and Asia Pacific become further strained, we see an emboldening in operations, such as a greater willingness to cause destruction. We also observe this in their targeting of telecommunications organizations, which possess numerous critical infrastructure assets in strategically important geographies such as Guam and Taiwan. For Russian APTs, Gamaredon and Turla targeted Ukraine at an accelerated pace, but Russian activity in general for 2023 did not reflect the full range of destructive cyber capabilities we have seen it deploy in the past, potentially because of the concerted efforts of defenders.

One bright spot this year was Cisco’s determined efforts to create and deliver inventive security solutions that help strengthen our partners. Talos’ Ukraine Task Force continues to thwart attacks against critical Ukrainian partners. This year, we spear-headed an effort to stabilize Ukraine’s power grid against the effects of global positioning system (GPS) jamming on the battlefield by delivering modified Cisco switches into an active war zone. Cisco also launched the Network Resilience Coalition with leading industry partners, focusing on increasing awareness and providing actionable recommendations for improving network security. Relatedly, Talos’s Vulnerability Discovery and Research Team made investigating small office, home office (SOHO) and industrial routers a major priority, reporting 289 vulnerabilities to vendors to date, published across 141 Talos advisories.

As conflict in the Middle East worsens, we are once again positioned to help protect our customers and partners. Therefore, perhaps the overarching story of 2023 is this: as the daringness, sophistication, and persistence of our adversaries grows, so too does the resolve of defenders to interdict them in any way we can.

### Original Report Table of Contents

- **Telemetry trends** .................................................... 3  
  _Strategic findings and trends based on our vast data sets._
- **Ransomware and extortion** .................................... 8  
  _A look at major changes and top players we observed in this dynamic threat space._
- **Network infrastructure** ........................................ 13  
  _Threat actor and attack trends related to frequent, high-impact attacks on network devices._
- **APTs: China** .......................................................... 18  
  _Analysis on Chinese adversaries, including victimology and increased pace of operations._
- **APTs: Russia** ......................................................... 21  
  _Major players, top threats and trends from our Ukraine Task Force and global monitoring efforts._
- **APTs: Middle East** ................................................. 28  
  _A preview of the complex and often dire political climate that impacts the cyber threat landscape._
- **Commodity loaders: Qakbot, Emotet, Trickbot, IcedID, Ursnif** ............ 32  
  _Major developments for these common threats, including activity trends and changes in TTPs._

---

## Telemetry Trends

### Section Highlights

- Suspicious network traffic captured by Cisco Security products revealed sharp increases in activity that often corresponded with major geopolitical events and global cyber attacks.
- The most targeted vulnerabilities were older security flaws in common applications, consistent with the U.S. Cybersecurity and Infrastructure Security Agency’s (CISA) findings in recent years. Most of the top-targeted vulnerabilities we observed received maximum- or high-severity scores by Cisco Kenna and the Common Vulnerability Scoring System (CVSS) and were also included in CISA’s Known Exploited Vulnerabilities catalog. The high frequency of targeting attempts against these CVEs, paired with their significant impact, underscores adversaries’ preference to target unpatched systems that can cause major disruptions.
- Threat actors abused common file extensions and spoofed well-known brands, common techniques that underscore the use of social engineering to enable operations like phishing and business email compromise (BEC). Adversaries are likely responding to Microsoft’s disabling of macros in 2022 by using different file types to hide their malware, such as PDFs, which was the top blocked file extension this year.
- Financial services and shipping companies accounted for the brands we observed being spoofed most often in email telemetry, suggesting longstanding phishing themes for email-based commodity loaders like Emotet, Qakbot and Trickbot are still at play. Relatedly, phishing accounted for a quarter of known initial access vectors in Talos IR engagements this year, highlighting actors’ continued reliance on this technique.
- The use of valid accounts was a top-observed MITRE ATT&CK technique, underscoring adversaries’ reliance on compromised credentials and use of existing accounts for various stages of their attacks. This is consistent with Talos IR data, which showed compromised credentials/valid accounts accounted for nearly a third of known initial access vectors in 2023.

### Regional Trends Over Time

Suspicious traffic includes a wide variety of categorized information sourced from multiple Cisco Security products, including Umbrella, Secure Endpoint, Email Security Appliance (ESA), Meraki, SSE and Secure Firewall. Examples include malicious domains blocked by Umbrella, records with malicious dispositions from Secure Endpoint, phishing emails from ESA, triggered Snort signatures from Secure Firewall and Meraki, and many others.

In North America, Europe, the Middle East and Africa (EMEA), and Latin America, suspicious network traffic was periodic, following a Monday – Friday workday pattern for much of the year. Starting mid-year, we saw a break from this pattern marked by a dramatic increase in traffic blocked by our security products, often quadrupling the early part of the year’s normal behavior.

In mid-February, these regions experienced various spikes in web spam. While spam volume was up globally, it disproportionately affected the Asia Pacific, Japan and China (APJC) region.

In APJC, suspicious traffic was less periodic and experienced large swings in volume between January and April. These changes leveled out through the spring and early summer.

Various international events and major cyber attacks overlaid on the graph suggest how such activity can affect the threat landscape. While it’s impossible to prove causation, there are obvious correlations between the suspicious global and regional traffic patterns we observed and significant world events.

![Timeline graph plotting the volume of suspicious activity from January to September 2023 across North America, APJC, EMEA, and LATAM, annotated with key geopolitical and cyber events: "ESXiArgs" ransomware attacks; U.S. downs suspected Chinese spy balloon; Powerful earthquake in Turkey and Syria; China brokers Iran-Saudi Arabia mediation; Xi Jinping elected to third term; Xi Jinping meets Putin in Russia while Japanese PM visits Ukraine; Anonymous Sudan DDoS attacks on Microsoft Outlook; Ukrainian military counteroffensive; Clop exploits MOVEit zero-day; U.S., Japan, and South Korea trilateral summit; Niger Western-allied president deposed; Rhysida ransomware attacks U.S. hospitals.]

### Top Targeted Vulnerabilities

In 2023, cyber threat actors exploited older software vulnerabilities in common applications. In many cases, the vulnerabilities were more than 10 years old, consistent with CISA’s finding that adversaries have targeted old security flaws more than newly disclosed ones in recent years. In fact, four of the top five most-targeted vulnerabilities we observed were also cited by CISA as being frequently exploited in prior years, further highlighting this point. This underscores the need for entities to regularly install software updates, as many of these systems were likely unpatched given the age of the targeted vulnerabilities.

The top targeted vulnerabilities are found in common applications, like Microsoft Office. This finding is also substantiated by CISA, which noted that actors in 2022 prioritize CVEs that are more prevalent in their targets’ networks. Adversaries likely prioritize targeting widespread vulnerabilities because the exploits developed for such CVEs can have long-term use and high impact.

Lastly, most of the vulnerabilities on our list would cause substantial impact if exploited, with six receiving a maximum vulnerability risk score of 100 from Cisco Kenna and seven receiving the highest “critical” score from the Common Vulnerability Scoring System (CVSS). Most of the CVEs are also listed in CISA’s Known Exploited Vulnerabilities catalog, which is meant to inform users on the security flaws for which they should prioritize remediation. The high frequency of targeting attempts against these CVEs, paired with their severity, underscores the risk to unpatched systems.

| Ranking | CVE | Vendor | Product | CISA findings | CISA KEV catalog | Kenna/CVSS |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **1** | CVE-2017-0199 | Microsoft | Office and WordPad | Routinely exploited in 2022 | Listed | 100/9.3 |
| **2** | CVE-2017-11882 | Microsoft | Exchange server | Routinely exploited in 2022 | Listed | 100/9.3+ |
| **3** | CVE-2020-1472 | Microsoft | Netlogon | Routinely exploited in 2022 | Listed | 100/9.3 |
| **4** | CVE-2012-1461 | Multiple antivirus products | Gzip file parser utility | — | — | 58/4.3 |
| **5** | CVE-2012-0158 | Microsoft | Office | Commonly exploited by state-sponsored actors from China, Iran, North Korea, and Russia (2016-2019) | Listed | 100/9.3 |
| **6** | CVE-2010-1807 | Apple | Safari | — | — | 84/9.3 |
| **7** | CVE-2021-1675 | Microsoft | Windows (print spooler) | — | Listed | 100/9.3 |
| **8** | CVE-2015-1701 | Microsoft | Windows (kernel-mode driver) | — | — | 72/7.2 |
| **9** | CVE-2012-0507 | Oracle | Java SE | — | Listed | 100/10 |
| **10** | CVE-2015-2426 | Microsoft | Windows (font driver) | — | Listed | 100/9.3 |

_Source: Cisco Secure Endpoint_  
_CISA sources: Top Routinely Exploited Vulnerabilities, 2022 and 2016-2019._

### Email Findings

Phishing emails are one of the most common ways adversaries compromise victims and this has consistently been a top-ranked threat in Talos IR findings for years. In the last year alone, 25 percent of the initial access vectors identified in Talos IR engagements were comprised of phishing (this refers to chart 3b). This observation is consistent with U.S. government findings, with the FBI noting that phishing was the top incident reported to its Internet Crime Complaint Center (IC3) in 2022.

Threat actors commonly send unsolicited emails requesting users download or open an attachment to deliver malware. While file extension is not necessarily indicative of file type, actors frequently try to hide malware under well-known file extensions to appear less suspicious, so users are more likely to open them. For example, earlier this year, Japan’s Computer Emergency Response Team (JP-CERT) warned that adversaries were embedding malicious Word documents in PDF files to bypass detection, a strategy we have seen threat actors rely on for years.

Threat actors’ file type preference was also likely affected by Microsoft’s 2022 decision to block macros, which adversaries had heavily abused up to that point. With this change, actors have moved away from using Microsoft Office files like Word and Excel as frequently as they once did. In 2023, we saw the commodity loader Ursnif incorporate malicious PDF attachments into their phishing operations for the first time as this actor and other groups looked for ways to avoid relying on macros.

#### Top Blocked Attachment File Extensions
- **PDF**: 36%
- **Other**: 32%
- **DOCX**: 14%
- **HTML**: 8%
- **ZIP**: 5%
- **HTM**: 5%

_Source: Cisco Email Security Appliance_  
_Note: Common image-related filetypes — like JPG, JPEG, PNG and GIF — were excluded from this list because they appear frequently in an overwhelmingly high volume of benign emails, such as those containing graphics in senders’ signatures or in the email body._

#### Top Initial Access Vectors, According to Talos IR
- **Exploit vulnerability in public-facing application**: 28%
- **Unknown**: 23%
- **Compromised credentials on valid accounts**: 23%
- **Phishing**: 19%
- **Drive-by compromise**: 6%

_Note: Initial access vector is often hard to determine due to a variety of reasons — including insufficient logging or lack of visibility into the affected environment — resulting in “unknown” being highly represented._

#### Top Brands Spoofed in Sender Names
Cybercriminals and other malicious actors rely heavily on social engineering tactics to compromise users, which is why they commonly imitate well-known companies in their phishing emails. Commodity loaders like Emotet, Qakbot and Trickbot, for instance, routinely use fake invoices, bank statements, or shipping notifications as phishing themes to feign legitimacy. This is reflected in our list of top spoofed brands, where we see that financial services entities and shipping services were among those that actors most frequently spoofed.

Business email compromise (BEC) operations also leverage spoofed company names to enhance legitimacy. BEC is a scam in which cybercriminals send emails to targets that appear to come from a known source making a legitimate request. The goal is to prompt the target to make unauthorized money transfers to the threat actor. Actors may impersonate well-known and trusted brands, like those represented in our list, to trick users. BEC has been on the rise in recent years, according to the FBI, and resulting in $2.7 billion in losses in 2022.

![Graphic showing top spoofed brands: Banco Bradesco, Bank of America, Walmart, AT&T, Aeon, Western Union, American Express, Google, Capital One, DHL, Paypal, Royal Bank of Canada, FedEx, American Airlines, DocuSign.]

_Source: Cisco Email Security Appliance_

### Top MITRE ATT&CK Techniques

Notably, nearly a third of the top 20 most common MITRE ATT&CK techniques fall under the defense evasion tactic, suggesting actors are devoting substantial resources to this phase of the attack chain. Techniques relating to privilege escalation and persistence also ranked high, highlighting their importance in the attack lifecycle.

Hijack execution flow was the most common technique, appearing nearly twice as often as the next highest result. Hijacking execution flow refers to actors co-opting the way an operating system runs programs on a target endpoint. DLL side-loading is a common example of this, whereby actors essentially position their malware alongside the victim application so that when the program searches for its legitimate DLL, it also unwittingly executes the malicious payload. This is an effective way for actors to hide their activities under legitimate and trusted software, a technique we commonly see leveraged by APTs and cybercriminals.

The use of valid accounts was the second-most common technique we observed, underscoring adversaries’ reliance on compromised credentials and use of existing accounts. Actors use this technique to enable various stages of the attack chain. We commonly see commodity loaders deploying information-stealing malware for this very purpose. Relatedly, credentials from password stores ranked in the top five, further highlighting actors’ focus on obtaining user credentials. These findings are consistent with Talos IR data, which showed compromised credentials/valid accounts accounted for nearly a quarter of known initial access vectors in 2023.

Resource hijacking, which ranked in the top 10, is a technique we typically see associated with the deployment of cryptocurrency mining malware, which hijacks an endpoint’s processing power for profitable gains. Cryptocurrency mining threats are highly common, as this is a low-level type of attack typically carried out by unsophisticated actors. We often see this type of malware deployed, especially soon after new vulnerabilities are disclosed, before victims have time to patch and/or in conjunction with other, more complex, malware.

#### Top 20 Observed Techniques
1. **T1574, Hijack Execution Flow** (Defense Evasion, Persistence, Privilege Escalation)
2. **T1078, Valid Accounts** (Defense Evasion, Initial Access, Persistence, Privilege Escalation)
3. **T1055, Process Injection** (Defense Evasion, Privilege Escalation)
4. **T1555, Credentials from Password Stores** (Credential Access)
5. **T1068, Exploitation for Privilege Escalation** (Privilege Escalation)
6. **T1222, File and Directory Permissions Modification** (Defense Evasion)
7. **T1056, Input Capture** (Collection, Credential Access)
8. **T1546, Event Triggered Execution** (Persistence, Privilege Escalation)
9. **T1558, Steal or Forge Kerberos Tickets** (Credential Access)
10. **T1496, Resource Hijacking** (Impact)
11. **T1059, Command and Scripting Interpreter** (Execution)
12. **T1564, Hide Artifacts** (Defense Evasion)
13. **T1102, Web Service** (Command and Control, Defense Evasion)
14. **T1480, Execution Guardrails** (Defense Evasion)
15. **T1021, Remote Services** (Lateral Movement)
16. **T1135, Network Share Discovery** (Discovery)
17. **T1124, System Time Discovery** (Discovery)
18. **T1057, Process Discovery** (Discovery)
19. **T1113, Screen Capture** (Collection)
20. **T1072, Software Deployment Tools** (Execution, Lateral Movement)

---

## Ransomware and Extortion

### Section Highlights

- Ransomware and pre-ransomware incidents continue to affect customers at a consistent rate — totaling the same 20 percent of Talos IR incidents as last year — with health care being the most targeted vertical.
- For the second year in a row, LockBit was the most prolific ransomware-as-a-service (RaaS) gang, based on our findings, consistent with CISA’s assessment that it is the most deployed ransomware variant. LockBit was one of the most frequently observed ransomware threats in Talos IR this year, and affiliates accounted for more than 25 percent of the total number of victim posts on data leak sites across some 40 ransomware groups we monitor.
- ALPHV, Clop and BianLian also dominated the threat landscape, accounting for another quarter of all ransomware and/or data extortion compromises publicized on dark web actor sites.
- We saw Clop affiliates consistently exploit zero-day vulnerabilities, a highly unusual tactic given the expertise, personnel and access required to develop such exploits, suggesting the group possesses a level of sophistication and/or resources matched only by advanced persistent threats (APTs).
- New ransomware variants are emerging that leverage leaked source code from other RaaS groups, allowing less skilled actors to enter this space. At the same time, we also see highly sophisticated operators like Clop leveraging zero-day vulnerabilities at an unprecedented pace, an interesting dichotomy demonstrating the breadth of actors in this space.
- Actors are turning to data extortion more than ever, with this being the top threat that Talos IR responded to in Q2 2023 (April - June). Data theft extortion looks very similar to pre-ransomware activity, creating challenges for defenders.
- Some actors are abandoning ransomware use altogether, opting for extortion instead, a trend likely influenced by ongoing law enforcement operations, better industry detections and lower operational costs.

### Ransomware Attacks Persist at Steady Pace

The ransomware space remained dynamic in 2023, with groups continuing to rebrand or merge, actors often working for multiple ransomware-as-a-service (RaaS) outfits at a time, and new groups continually emerging. The skill levels varied greatly as well, with experienced actors developing sophisticated exploits for zero-day vulnerabilities, while less-skilled actors relied on repurposed ransomware code to create their own threats. We also saw an emerging trend in this space, as more actors began to abandon the use of ransomware and resort to pure data theft extortion without encrypting files, presenting a new line of challenges for defenders. Despite these changes, one thing remains constant: Ransomware remains a top threat to entities worldwide.

Ransomware and pre-ransomware made up 20 percent of the total incidents that Talos IR responded to this year, a very slight drop compared to last year. It can be difficult for defenders to determine what constitutes a pre-ransomware attack if a ransomware binary is never executed and encryption does not take place. However, there are some indications analysts use to assess if ransomware is the likely final objective, such as the use of adversary simulation frameworks like Cobalt Strike and/or credential-harvesting tools like Mimikatz, the targeting of certain critical assets such as backups, or enumeration and discovery techniques.

> "The health care and public health sector was the most targeted vertical in Talos IR ransomware and pre-ransomware engagements this year, compared to the education sector in 2022."

The health care and public health sector was the most targeted vertical in Talos IR ransomware and pre-ransomware engagements this year, compared to the education sector in 2022, as reported in last year’s Year in Review report (see Figure 1). Healthcare organizations are highly vulnerable to cyber attacks given their low downtime tolerance, often underfunded cybersecurity budgets, and possession of protected health information (PHI) that is valuable to threat actors. The COVID-19 pandemic likely exacerbated this situation in recent years, with healthcare providers strained from a resource perspective and downtime being even less tolerable.

![Figure 1: Chart depicting Talos IR ransomware and pre-ransomware incidents per sector in 2023, showing Health Care and Public Health as the top targeted vertical.]

### Old Foes Are Top Offenders as LockBit Remains Top Threat

For a second year in a row, LockBit was the most active RaaS group, accounting for over 25 percent of the total number of posts made to data leak sites. LockBit, ALPHV, Clop and BianLian accounted for nearly 50 percent of the total posts made to leak sites this year (Figure 2).

![Figure 2: Chart illustrating the number of victim posts made to ransomware data leak sites in 2023, showing LockBit leading with over 25%, followed by ALPHV, Clop, and BianLian.]

> #### Talos IR Responds to LockBit Incident Affecting IT and OT Networks
> Talos IR responded to a LockBit ransomware incident affecting a utilities company where ransomware infiltrated the organization’s IT and OT networks, causing significant impact to the victim and downstream disruptions to customers. The ransomware affiliate gained initial access using valid router credentials authenticating over VPN where multi-factor authentication (MFA) was not implemented. The attackers encrypted production servers, including those monitoring the electrical grid, and three of four domain controllers were encrypted, as well.

LockBit continued to conduct prolific ransomware operations in 2023, a finding that aligns with CISA’s assessment that it is the most deployed ransomware variant. LockBit attacks can be very impactful, affecting an organization’s information technology (IT) networks and operational technology (OT), the hardware and machines responsible for physical processes, as we have observed in Talos IR engagements. In October, CISA published guidance for securing OT environments, underscoring how significant the impact can be to these systems. LockBit was also deployed during the exploitation of two vulnerabilities in the PaperCut software, a print management solution widely used across entities in the government and education verticals, among others.

Posts made to the group’s data leak site ebbed and flowed throughout the year, with detections of LockBit activity appearing to spike in March, partially coinciding with LockBit’s deployment against vulnerable instances of the printer management software PaperCut, where it has remained consistently high (Figure 3).

![Figure 3: Graph tracking LockBit activity throughout the year 2023, showing spikes in March corresponding with PaperCut exploitation and sustained high activity levels.]

### Ransomware Space Remains Crowded with New and Rebranded Groups

Ransomware groups’ constant rebranding and/or turnover was a prominent trend this year. Multiple leaks of ransomware source code and builders — components essential to creating and modifying ransomware — have had a significant effect on the ransomware threat landscape. These leaks allow ransomware operators to rebrand or give unsophisticated actors the ability to generate their own ransomware more easily with little effort or knowledge. As more actors enter this space, Talos is seeing an increasing number of ransomware variants emerge leveraging leaked ransomware code, often leading to more frequent attacks and new challenges for cybersecurity professionals and defenders, particularly regarding actor attribution.

The volume of new ransomware variants based on leaked source code also highlights the speed at which actors take advantage of such public disclosures. Most recently, we observed a surge in new ransomware strains emerging from the Yashma ransomware builder. First appearing in May 2022, Yashma is a rebranded version of the Chaos ransomware builder (v5), which was leaked in April 2022. Since early 2023, we have seen several new Yashma strains emerge, including ANXZ and Sirattacker, likely deployed by smaller or groups of affiliates with fewer resources given their lack of widespread adoption and notoriety in the landscape.

In April, we discovered a new ransomware actor, RA Group, deploying their ransomware variant based on the leaked Babuk source code. Since an alleged member of the Babuk group leaked the full source code of its ransomware in September 2021, several new variants based on the leaked code have emerged, with many appearing in 2023, including ESXiArgs, Rorschach and RTM Locker.

While these changes in the threat landscape have largely benefitted affiliates, security researchers and defenders also have an advantage with access to the leaked code. It allows security researchers to analyze the source code and understand the attacker’s TTPs and develop effective detection rules, potentially aid in the creation of decryptors and enhance security products’ capabilities in combating ransomware threats.

> #### What is the impact of leaked ransomware source code?
> When ransomware source code or builders are leaked, it becomes easier for aspiring cybercriminals who lack the technical expertise to develop their own ransomware variants by making only minor modifications to the original code. Additionally, by using leaked source code, threat actors can confuse or mislead investigators, as security professionals may be more likely to misattribute the activity to the wrong actor.  
> _(From research posted on the Talos blog)_

### Affiliates Turning to Data Theft Extortion over Ransomware Deployment

Even with the expanding number of RaaS options, some have found success in extorting funds without deploying ransomware. In these extortion instances, an adversary steals the victim’s data but does not encrypt it. The common double extortion tactic is thereby eliminated, with the actor relying solely on the threat of leaking the information rather than also demanding payment to unlock the files. This trend is also reflected in Talos IR engagements, where extortion was the most observed threat in Q2 2023, accounting for almost a third of threats seen, a 25 percent increase from the prior quarter (January–April) (Figure 4).

![Figure 4: Chart showing data theft extortion as the top threat in Q2 (April - June 2023), accounting for nearly a third of all Talos IR engagements.]

Several well-known ransomware gangs — including Babuk, BianLian and Clop — have opted for data theft extortion over ransomware, a departure from the groups’ typical ransomware attack chain (Figure 5).

![Figure 5: Chart illustrating prominent groups increasingly turning to data theft extortion in recent years.]

Several factors have likely contributed to some threat actors’ preferences for data theft extortion instead of deploying ransomware. U.S. and international law enforcement have aggressively pursued ransomware actors in recent years, conducting major disruptions against well-known groups. Advancements in endpoint detection and response (EDR) capabilities have likely been a significant obstacle for threat actors seeking to deploy ransomware and encrypt data. Adversaries appear to consider the technique a viable way to receive a payout, demonstrating how ransomware actors are constantly working around advancements in EDR, law enforcement operations and other barriers.

While extortion has proven to be a serious and effective threat, it has not yet outpaced the ransomware threat that has been a challenge for organizations and defenders for the past several years. We are continuing to monitor the long-term effects of this trend.

### Some Ransomware Groups Consistently Leverage Zero-Days, Often Affecting Multiple Organizations

While many inexperienced adversaries relied on code reuse this year, we also continued to see highly sophisticated operators exploiting zero-day vulnerabilities at an unprecedented pace, highlighting the broad technical diversity of actors and TTPs in this space. Ransomware actors, well-known for being opportunistic, are quick to exploit flaws when made public. When Clop, a high-profile ransomware and data extortion group, claims public responsibility for exploiting a zero-day vulnerability, additional ransomware affiliates quickly follow suit, scanning for affected systems before patches are issued (Figure 6).

![Figure 6: Timeline of ransomware groups leveraging notable vulnerabilities throughout 2023, showcasing campaigns by Clop and other affiliates.]

In April, shortly after print management software company PaperCut became aware of unpatched servers being exploited in the wild by Clop, other ransomware groups began to exploit the critical remote code execution (RCE) vulnerability (CVE-2023-27350) as part of their attack chain. This highlights the widespread nature of this activity and ransomware operators’ strategy, often based on the disclosure of other groups leveraging high-profile security flaws to increase chances of eliciting payouts from victims.

Clop’s repeated efforts to exploit zero-day vulnerabilities is highly unusual for a ransomware group given the resources required to develop such capabilities. We saw many instances of this in 2023, beginning in January, when the Clop ransomware group launched a campaign leveraging a zero-day vulnerability, (CVE-2023-0669) to target the GoAnywhere MFT platform. In May, Clop claimed responsibility for attacks involving another zero-day flaw (CVE-2023-34362) affecting Progress Software’s file transfer solution, MOVEit Transfer. These attacks also demonstrate Clop’s expanded toolkit, as the operators deployed a previously unseen web shell, dubbed LemurLoot, to exfiltrate victims’ data and extort payments on systems running MOVEit.

The vulnerabilities leveraged by ransomware affiliates/groups highlighted above all received high- or critical-severity CVSS scores, were found to be easily exploitable by Cisco Kenna, and were included in CISA’s Known Exploited Vulnerabilities catalog.

Given the resources required to develop or identify such exploits, it is possible that Clop, and/or certain members, possess a level of sophistication and funding matched only by APTs. There is no known chatter on underground forums about how Clop may have obtained these exploits, though we assess the group may have access to a sophisticated developer that appears to be focusing on identifying vulnerabilities in third-party file management systems and other network peripherals.

### Landscape Shifts in the RaaS Space Due to Law Enforcement Disruptions

When ransomware infrastructure gets disrupted, operators often continue their work with other groups, creating a whack-a-mole scenario for law enforcement and network defenders. For example, when Hive’s infrastructure was disrupted, many former Hive members attempted to join other ransomware groups within days of the disruption, according to our sources. This greater democratization, with an influx of new groups leveraging code from the same ransomware builders, introduces complexities for defenders attributing activity to specific groups as TTPs remain consistent across groups.

Ransomware groups experienced disruptions, forcing them to adapt and/or join other RaaS outfits. In January 2023, the U.S. Justice Department announced it had disrupted the Hive ransomware group. By late January, we saw this reflected in our data, with a general dropoff in posts made to Hive’s data leak site (Figure 7).

![Figure 7: Line chart showing the steep dropoff of posts made to Hive's data leak site since late 2022 following the January 2023 law enforcement disruption.]

---

## Network Infrastructure

### Section Highlights

- Advanced actors are attacking networking devices at a concerning rate this year, particularly China and Russia-based groups looking to advance espionage objectives and facilitate stealthy operations against secondary targets.
- Other cybercriminals are starting to follow suit, adopting this technique to sell unauthorized access to these devices on the dark web or pivot into targeted networks and deploy ransomware.
- Actors take advantage of security weaknesses, such as default credentials and unpatched vulnerabilities, to gain initial access to the targeted device.
- Three of the five most targeted device vulnerabilities in this space are critical or severe, and exploitation can, in some instances, lead to full device takeover. This could provide adversaries unfettered access to core components of a target’s network and security perimeter.
- Exploitation attempts against vulnerabilities in this space typically remained consistent throughout 2023 with occasional spikes after the vulnerabilities’ public disclosure. This suggests that targeted organizations are often failing to patch their devices in a timely manner, and actors therefore continue to see value in exploiting CVEs, even as they age.
- To remain hidden post-compromise and establish additional methods of access without raising alarm bells, actors take steps to weaken defenses within the environment and will even introduce new vulnerabilities to exploit.
- Talos is helping to combat this threat by supporting the Network Resilience Coalition, a group of industry leaders from network equipment vendors, network operators, and security companies that focuses on securing critical data networks.

### Weak Security Often Exploited for Initial Access

Talos observed an increase in sophisticated attacks on networking devices this past year, particularly by state-sponsored actors seeking to advance espionage objectives and facilitate stealthy operations. Our investigations have largely involved threat groups affiliated with Russia and the People’s Republic of China (PRC), though it is reasonable to assume any sufficiently capable APT is, or will be, developing the capability to target network infrastructure as the success of these attacks garners increased attention. We have also recently observed targeting activity from other cybercriminals, including initial access brokers and ransomware actors seeking to profit off unauthorized access to targeted devices.

Networking equipment is an attractive target for malicious cyber actors due to the large attack surface it presents and potential access to a victim network it can offer. Though these devices are key components of an organization’s IT infrastructure and often conduits of sensitive network traffic, they are infrequently examined from a security perspective and typically poorly patched. Further, they often do not run on standard operating systems, but rather custom firmware unique to the vendor, meaning they cannot be protected or monitored with standard, one-size-fits-all security solutions. The dichotomy of high value and weak security in these devices makes them a prime target for exploitation. Because of the large presence of Cisco network infrastructure around the world, we are well-positioned to investigate and report on top-tier attackers and their campaigns.

We have seen malicious actors predominately gain initial access to networking devices by exploiting unpatched vulnerabilities, weak or default credentials, or insecure device configurations. While security professionals may not be able to implement standard EDR solutions on networking devices as referenced above, this observation demonstrates that an organization’s defenses against this threat can be greatly improved simply through routine patching, enhanced monitoring, and improved credential management. Once initial access is obtained, threat actors will typically take further advantage of the device’s limited security by destroying evidence of an intrusion, such as wiping or disabling logs.

### Exploitation of Vulnerabilities Spike After Public Disclosure

Over the last year, exploitation activity against vulnerabilities in network devices typically remained consistent, though sometimes spiked following public disclosure, based on our telemetry. A spike in exploitation attempts could be due to several factors, such as a singular and very large campaign conducted by an advanced threat actor, or widespread targeting activity that was suddenly impeded by highly publicized reporting and recommendations to patch. Comparatively, the consistent targeting levels in the months after disclosure suggests affected organizations are failing to patch their devices in a timely manner and actors therefore continue to see value in exploiting these older vulnerabilities even as they age.

For example, detections for Snort IDs (SIDs) 60726 and 60725, which alert on attempts to exploit the aforementioned Fortinet vulnerability (CVE-2022-40684), spiked right after the security flaw was disclosed in mid-October 2022, then significantly lowered to a consistent level in early 2023 (Figure 8). In comparison, attempts against vulnerable Zyxel devices (CVE-2023-28771; SID 6185) began in mid-May 2023, shortly after the CVE was publicized in April, and remained relatively level for months afterward.

![Figure 8: Graph showing exploitation attempts of network device CVEs released in 2022 or 2023, highlighting spikes and consistent baselines for Fortinet (CVE-2022-40684) and Zyxel (CVE-2023-28771).]

### Top Vulnerabilities Targeted Are Highly Critical, Easily Exploitable and Widespread

The vulnerabilities affecting network devices that were most frequently targeted in 2023 have high severity scores, meaning they are easily exploitable and can cause significant operational impact. Of the five most targeted vulnerabilities in this space, three have a CVSS score of 9.8 or 10, scores that are reserved for only a small number of the most serious CVEs. Exploitation of critical and severe security flaws in network devices can, in some instances, lead to full device takeover, allowing adversaries unfettered access to core components of a target’s network and security perimeter.

Furthermore, many of the affected devices are widely used by enterprises and governments globally, further exacerbating the potential impact and scope of successful compromise. Threat actors may uncover thousands of vulnerable devices when conducting mass scanning after flaws are disclosed and can often find publicly available exploits as well.

Finally, the variety of vendors represented in the list below demonstrates how universal this issue is for device providers. This is further supported by Russian intelligence contracting documents, also known as the Vulkan Files, that Talos obtained samples of this past year. These documents showed that any network device brand was vulnerable to targeting, with one scanning component targeting almost 20 different router and switch manufacturers.

Most of the CVEs listed below are also included in CISA’s lists of vulnerabilities that are commonly targeted and/or have known exploitation. Our top two vulnerabilities were also included in a CISA advisory on threats to U.S. critical infrastructure, demonstrating just how impactful exploitation of these vulnerabilities can be.

1. **CVE-2020-5902 (SID 54462)**: A remote code execution vulnerability in F5 BIG-IP’s Traffic Management user interface.
2. **CVE-2019-1653 (SID 48949)**: An information disclosure vulnerability in Cisco RV series routers.
3. **CVE-2022-40684 (SIDs 60725 and 60726)**: An authentication bypass vulnerability in Fortinet FortiOS, FortiProxy and FortiSwitchManager.
4. **CVE-2023-28771 (SID 61865)**: An unauthenticated command injection vulnerability in multiple Zyxel firewalls.
5. **CVE-2020-3452 (SID 54598)**: A directory traversal vulnerability in Cisco Adaptive Security Appliance (ASA) Software and Cisco Firepower Threat Defense (FTD) Software.

_CVE descriptions sourced from the National Institute of Standards and Technology (NIST) website and Snort IDs sourced from the Snort website._

### Malware Sometimes Installed Post-Compromise to Establish Footholds

In some instances, we observed actors, particularly China-affiliated APTs, installing malware onto devices post-compromise to establish footholds in the network and enable follow-on activity. Some of the capabilities enabled by the malware we have seen include:

- Bypassing access control lists (ACLs) so that traffic cannot be properly blocked by the router.
- Allowing for authenticated access to devices outside of normal authentication methods.
- Enabling the ability to corrupt and disable the device.
- Redirecting actor-defined traffic to actor-controlled infrastructure.

In many instances, we see actors using living-off-the-land binaries (LoLBins) either in conjunction with or instead of malware deployment to advance their operations and avoid detection.

In a more recent instance of malware being installed post-compromise, actors began exploiting a previously unknown critical vulnerability (CVE-2023-20198) in September and October 2023 to gain access to certain network devices running Cisco’s IOS XE software. This allowed attackers to gain privilege level 15 access to the device, which they used to exploit a second zero-day vulnerability (CVE-2023-20273) to deploy their malware. Notably, the CVE-2023-20198 vulnerability specifically affects devices that are exposed to the internet and have the HTTP or HTTPS Server feature enabled, features the U.S. government had previously warned about.

This activity underscores Cisco’s recommendations, which are consistent with best practices and guidance the U.S. government has provided in the past on mitigating risk from internet-exposed management interfaces. This is also in line with Cisco’s ongoing work with industry partners as part of the Network Resilience Coalition, covered in more detail below.

### Collection of Network Information Essential to High-Stakes Operations

Russian and Chinese APTs use their visibility into compromised devices to capture sensitive network information, facilitating further access to more valuable data. Actors seek to intercept and abuse data such as legitimate credentials, details of trusted domain relationships, network diagrams, contracts with network customers, and configuration information. This information can provide a roadmap for actors seeking to elevate their privileges and pivot into networks of interest for intelligence collection.

APTs will also take steps to weaken defenses within the environment and carve out additional paths for long-term access. These methods include disabling logging, modifying memory to reintroduce vulnerabilities that had been patched, modifying configurations to enable privileged activity and replacing firmware with older and legitimate firmware that can be modified in memory. This variety of activities demonstrates that adversaries have a very high level of comfort and expertise working within the confines of compromised networking equipment. Additionally, in establishing these footholds within a target environment, actors seek to erode the variable barriers in an organization’s defense-in-depth security architecture. Organizations must update and enhance their system hardening efforts and network monitoring capabilities to defend against these threat groups.

### Numerous Compromised Devices Form Anonymizing Network for Malicious Traffic

While the techniques described thus far are typically highly specialized to target specific victims, actors also conduct widespread and indiscriminate targeting of network devices to facilitate stealthy operations against secondary targets. We have observed China-affiliated APTs compromising numerous networking devices globally, with limited consideration of the device’s owner, to form an anonymizing network that functions similarly to Tor. The actors use this network of compromised devices to route malicious traffic to and from a targeted network, thereby obfuscating the origin of their attack. These APTs can also bypass a target’s security defenses that block traffic from certain geographic regions by having the C2 traffic emanate from internet service providers (ISPs) local to the victim.

We have seen China-affiliated actors conducting widespread campaigns to exploit critical vulnerabilities associated with networking devices within days of public disclosure, meaning the type of infrastructure targeted is often largely opportunistic.

### How Are We Countering This Growing Threat?

Cisco launched the Network Resilience Coalition with leading industry partners in July 2023. This alliance focuses on increasing awareness of this issue, understanding its full scope, and providing actionable recommendations for improving network security that supports global economic and national security.

Talos has led efforts to address this threat, contributing a significant amount of research and technical information that has been published in U.S. government advisories on this topic. We have also increased messaging to customers and network defenders on how to improve network infrastructure resilience. We actively engage in research and information sharing efforts with other vendors as well to bolster overall device security. For example, this past year, our Talos Vulnerability Discovery and Research Team made investigating small office, home office (SOHO) and industrial routers a major priority. As a direct result of this effort, we have reported 289 vulnerabilities to vendors to date, published across 141 Talos advisories. These reports resulted in new Snort network intrusion detection coverage and several security improvements from each vendor. These fixes help customers who deploy Cisco Security solutions and improve the security posture of anyone using these devices once the vulnerabilities are patched.

### Ransomware Actors and Initial Access Brokers Abuse Weak Credentials and Monetize Access

> "Initial access brokers and ransomware affiliates have also become more active in targeting network devices this past year, predominately compromising weak or default credentials..."

Initial access brokers and ransomware affiliates have also become more active in targeting network devices this past year, predominately compromising weak or default credentials, then either selling the unauthorized access on dark web marketplaces or using it to deploy ransomware onto targeted networks.

This year, we responded to a campaign targeting Cisco Adaptive Security Appliance (ASA) devices configured with WebVPN in which cybercriminals likely gained unauthorized access to the devices via brute force and password spraying attacks. In July, we observed a significant spike in activity targeting ASA devices configured with WebVPN, coinciding with much of the public reporting on in-the-wild activity targeting ASA devices (Figure 9). Additionally, a September 2023 spike in WebVPN requests coincides with Cisco’s security advisory on a vulnerability disclosure for CVE-2023-20269. Exploitation of this vulnerability allows a remote attacker to conduct brute-force attacks or an authenticated, remote attacker to establish a clientless SSL VPN session with an unauthorized user. The ability to perform a brute-force attack, combined with widespread use of weak or default credentials, facilitated high impact against a large number of devices. This activity also highlights the frequency in which adversaries will attempt to exploit vulnerabilities soon after they are made public.

![Figure 9: Graph showing spikes in WebVPN-related requests that coincide with activity targeting ASA devices in July and September 2023.]

Akira and LockBit ransomware groups were publicly tied to this activity starting in August 2023, though it is unclear if these actors conducted the credential spraying attacks or if they purchased access from initial access brokers. These two threat groups have also been observed conducting similar activity against other device vendors, such as FortiGuard. Talos believes that third-party brokers may be responsible for initial access in many of the ransomware cases based on volume and timing of the targeting activity and nature of follow-on actions post-compromise. The aforementioned security advisory included mitigation recommendations and indicators of compromise to help defenders protect against this threat, highlighting the importance of implementing proper MFA and limiting the number of consecutive failed login attempts, which would significantly reduce exposure to this threat.

---

## Advanced Persistent Threats: China

_While APTs emanating from many parts of the world remained active, most of our investigations and research this year focused on China, Russia and the Middle East, which are featured in this section of the report._

### Section Highlights

- China-affiliated activity occurred at a rigorous pace this year, likely in response to geopolitical events that strained the country’s relationships with the West and Asia Pacific.
- Based on our analysis of numerous malicious campaigns, it appears Beijing may be directing more aggressive intelligence collection and prepositioning for future attacks against targets in these regions.
- Actors have improved in terms of deeply entrenching themselves in targeted networks and dodging detection or incident response efforts, placing a heavier burden on targeted organizations to keep their networks safe.
- Talos observed several instances of ransomware actors compromising a target closely following a long-term, covert APT intrusion by using similar methods of initial access and deploying ransomware. While the connection, if any, between the APT and ransomware groups is undetermined, the timing of the operations and overlap in TTPs suggests the ransomware operators may at least have prior knowledge of the espionage campaigns.
- Telecommunications organizations were a top target of Chinese cyber operations in 2023, particularly those offering services in areas of strategic interest to China, such as Guam and Taiwan. These entities are particularly attractive targets for these actors, as unauthorized access can enable widespread intelligence collection across several critical sectors.
- The organizational structure of telecommunications organizations and victims’ geographical locations often poses challenges to incident responders, including limited visibility into all affected networks and political sensitivities when investigating or assigning attribution to China.

### TTPs Largely Centered on Evading Detection and Attribution

China-linked APTs operated at a rapid pace this year, conducting sophisticated and stealthy intrusions into the networks of numerous high-value targets. According to our research, the actors responsible for these campaigns often seek long-term access to targeted networks, establishing multiple methods of maintaining persistence while avoiding targets’ detection mechanisms.

China-affiliated APTs appear to considerably reduce their malicious activity on a network if detected or the actor becomes aware of incident response efforts. Operators are likely maintaining undiscovered footholds and waiting until the target is no longer operating at a level of heightened awareness to resume their activity, underscoring the importance of aggressive remediation and eviction efforts, and keeping incident response plans updated. Their success in maintaining this access is evidenced by long dwell times on compromised networks, with one intrusion we investigated this past year having a dwell time of at least seven years. This demonstrates the severe impact these types of campaigns can have on targeted organizations, as complete remediation often requires comprehensive analysis of all network assets, long-term support of advanced incident response teams, and organization-wide action such as password resets and system updates. If targeted entities cannot commit to these measures, their environments are largely unchanged from last year. We also continued to see these APTs conducting operations in which access to the targeted entity can facilitate compromise of many victims, with actors especially employing this methodology against telecommunications organizations.

### New Trend of Ransomware Deployment Following Long-Term Espionage Operations

In a few instances, following a long-term, sophisticated and espionage-oriented APT intrusion, Talos observed a secondary threat group targeting the victim network by using similar methods of gaining initial access, such as exploiting public-facing vulnerabilities, and then deploying ransomware payloads. We have observed this trend in certain industries, such as semiconductors, and regions, such as Guam, that the PRC places a high degree of strategic importance on. Though we have yet to determine a connection, if any, between the two groups of attackers in these instances, several scenarios are possible:

- These groups may also not be affiliated with China at all, though this is probably less likely given the timing of the follow-on ransomware operations and overlap in methods of obtaining initial access.
- Chinese APTs may be contracting out disruptive ransomware operations to third-party cybercriminals seeking financial gain.

Whether it has resulted from strategic collaboration, financial cooperation, or just unaffiliated actors finding their way in due to some other element, such as noisier tradecraft from the original adversaries, these attacks potentially represent a dangerous new destructive element to PRC-affiliated APT attacks that we assess reveals an escalation from previous years.

### More Rigorous Pace of Operations Likely Linked to Shifts in Geopolitical Environment

> "Activity conducted by China-affiliated APTs occurred at a fast tempo this past year, likely due in part to geopolitical factors that Chinese leadership perceived as threats to the Communist Party of China’s (CCP’s) governance."

Activity conducted by China-affiliated APTs occurred at a fast tempo this past year, likely due in part to geopolitical factors that Chinese leadership perceived as threats to the Communist Party of China’s (CCP’s) governance. We quantified this increase in activity based on the number of government partner intelligence shares, collaboration projects with CISA, related infrastructure targeting cases, and high-priority investigations into China-affiliated activity affecting Cisco customers.

This shift in tempo may reflect a difference in intent, a type of signaling we have not observed in years past. Beijing typically directs cyber activity with the intent of collecting i

---

ntelligence to address the economic, political
response efforts, the malicious actors will likely quickly
and quietly resume their activities once they sense the • They could be illustrative of these APTs engaging in and strategic goals of the CCP. Though some of these
target feels the environment is safe. destructive attacks. There are several examples of goals, such as their Five-Year Plans, are routinely set
Chinese APTs incorporating ransomware into their as long-term objectives for growth, other provisional
Other TTPs used by China-linked APTs this past year
operations, such as Bronze Starlight or APT41. needs are determined based upon China’s relationships
include LoLBins to evade detection, exploitation of public
with other nations. For example, if a relationship with a
• They could be comprised of actors affiliated with the
vulnerabilities, targeting of network devices, and use of
nation China relies on for exports deteriorates, Chinese
original attackers, such as opportunistic associates
shared, open-source or commercial tools, all of which
© 2023 Cisco and/or its affiliates. All rights reserved. | talosintelligence.com page 19

2023
YEAR IN REVIEW
Advanced persistent threats: China
actors may seek to exfiltrate proprietary data,  against competition from the West. aggressive in the South China Sea, doubling  pivot into the networks of additional high-value
focused on espionage yet deliberately quiet,  down on their claims to sovereignty over  targets of interest and conduct widespread
U.S. policies and positions regarding China
Threat actor
that can boost their self-reliance in developing  almost all of the disputed area. Their robust  exfiltration of sensitive data.
have not softened this year, with the U.S.
| whatever that export is. If a relationship with  |     | military presence in the region has incurred  |     |
| ------------------------------------------------ | --- | --------------------------------------------- | --- |
highlight:
|                                             | continuing to categorize China as a top security  |                                                  | There are several ways in which use of this  |
| ------------------------------------------- | ------------------------------------------------- | ------------------------------------------------ | -------------------------------------------- |
| a nation becomes increasingly contentious,  |                                                   | standoffs and conflict throughout the past year  |                                              |
|                                             | threat. The Director of National Intelligence     |                                                  | latter technique can challenge remediation   |
Volt Typhoon
| China may seek to establish footholds in the       |                                              | with neighboring countries that have competing  |                                                  |
| -------------------------------------------------- | -------------------------------------------- | ----------------------------------------------- | ------------------------------------------------ |
|                                                    | named China the “most consequential threat”  |                                                 | efforts. A service provider may not immediately  |
| networks of that nation’s critical infrastructure  |                                              | claims for the territory, as well as with the   |                                                  |
|                                                    | to U.S. national security in 2023, and the   |                                                 | realize or have visibility into the extent of    |
| and preposition themselves for future              |                                              | U.S. military that is present there. Finally,   |                                                  |
Volt Typhoon is a China-
|                      | U.S. has steadily expanded sanctions against  |                                                | an intrusion targeting other businesses,  |
| -------------------- | --------------------------------------------- | ---------------------------------------------- | ----------------------------------------- |
| destructive attacks. |                                               | China’s relationship with Japan has also seen  |                                           |
affiliated threat group that made
|     | Chinese companies and organizations because  |     | subscribers or third-party providers, giving  |
| --- | -------------------------------------------- | --- | --------------------------------------------- |
challenges in the past year, with events like
headlines this past year for their
Numerous geopolitical events affected China’s  of such concerns. These security issues were  the actors ample time to burrow themselves
Japan restricting exports of semiconductors
long-term operation targeting
relationships with the West and Asia Pacific  exemplified by an incident in early 2023 when  deeper into compromised networks. The
and Tokyo’s decision to release water from the
U.S. critical infrastructure
this year, potentially leading to CCP directives  a Chinese spy balloon flew over the U.S.,  guidance for notifying customers of a breach
Fukushima Daiichi nuclear power plant, which
organizations and military bases.
for more aggressive targeting activity. Talos  gathered intelligence from military bases, and  also varies by country, potentially delaying
elicited criticism from Beijing.
performed intensive incident response  transmitted the information back to Beijing  incident response based on the geographic
Talos investigated a sustained
operations for strategic targets in both of  before being shot down. The U.S., Japan and  location of the initial victim. Finally, given
Volt Typhoon intrusion targeting
Targeting of the
these regions.  South Korea also bolstered their alliance in  delicate diplomatic relations that may exist
the telecommunications sector
|     | 2023, with the countries’ leaders meeting at  | telecommunications   | between the targeted country and adversary,  |
| --- | --------------------------------------------- | -------------------- | -------------------------------------------- |
in Guam, which is notably the
Deepening divide between  Camp David in August and committing to work  U.S.-based incident response teams may face
site of a U.S. military base
sector expands collection
|     | together to address security challenges from  |     | challenges and political sensitivities when  |
| --- | --------------------------------------------- | --- | -------------------------------------------- |
significant for the defense of
China and the West
|     | China and North Korea. Beijing swiftly criticized  | and prepositions actors for  | assisting in certain regions. Victims in certain  |
| --- | -------------------------------------------------- | ---------------------------- | ------------------------------------------------- |
Taiwan. Our research revealed
|     | this meeting, publicly stating attempts to form  |     | countries may be hesitant to assign attribution  |
| --- | ------------------------------------------------ | --- | ------------------------------------------------ |
the actors maintained persistent
| One major factor that has deepened the  |                                                 | future attacks  |                                                  |
| --------------------------------------- | ----------------------------------------------- | --------------- | ------------------------------------------------ |
|                                         | military blocs in the Asia Pacific will be met  |                 | to a particular threat group, could have strong  |
access to and exfiltrated data
divide between China and the West this year
|     | with “vigilance and opposition.”  |     | organizational ties to China, and/or may be  |
| --- | --------------------------------- | --- | -------------------------------------------- |
from networks of a service
| has been the PRC’s alliance with Russia,  |     | We responded to several intrusions into  |     |
| ----------------------------------------- | --- | ---------------------------------------- | --- |
wary of sharing key details of the compromise
provider and certain high-value
| particularly as other world leaders have  |                           | telecommunications providers by China- |                       |
| ----------------------------------------- | ------------------------- | -------------------------------------- | --------------------- |
|                                           | Growing conflict in the   |                                        | with American teams.  |
customers for at least a year
| vehemently denounced Moscow’s actions in  |     | affiliated APTs this year, particularly in areas  |     |
| ----------------------------------------- | --- | ------------------------------------------------- | --- |
and a half. Talos continues to
| the Russia-Ukraine war. The two countries  | Asia Pacific | that are of strategic interest to Beijing.  |     |
| ------------------------------------------ | ------------ | ------------------------------------------- | --- |
closely collaborate with public
have strengthened their trade relationship,
Telecommunications organizations are
and private partners on hunting
| and China’s rapidly increasing exports to  | Meanwhile, China is already facing conflict  |     |     |
| ------------------------------------------ | -------------------------------------------- | --- | --- |
attractive targets for these groups, as they
this threat group’s activity
| Russia have tempered the impact of numerous  | with neighboring nations in the Asia Pacific.  |     |     |
| -------------------------------------------- | ---------------------------------------------- | --- | --- |
often control numerous critical infrastructure
and investigate the group’s
| Western sanctions that have been levied  | Tensions have been rising between China  |     |     |
| ---------------------------------------- | ---------------------------------------- | --- | --- |
assets in the country, such as national satellite
anonymization infrastructure.
| against the country since its invasion of  | and Taiwan, exacerbated by U.S. support in  |     |     |
| ------------------------------------------ | ------------------------------------------- | --- | --- |
systems, internet services, and telephone
| Ukraine. Russia and China have also united to  | expanding Taiwan’s self-defense capabilities.  |     |     |
| ---------------------------------------------- | ---------------------------------------------- | --- | --- |
networks that are vital to the private and
| expand their presence in the Middle East and  | The People’s Liberation Army (PLA) has upped  |     |     |
| --------------------------------------------- | --------------------------------------------- | --- | --- |
public sectors. China-affiliated APTs can
| developing countries, conducting joint military  | its military pressure on the island, routinely  |     |     |
| ------------------------------------------------ | ----------------------------------------------- | --- | --- |
use their unauthorized access to establish
| exercises in the Gulf of Oman in March 2023,  | sending warplanes, drones and ships past  |     |     |
| --------------------------------------------- | ----------------------------------------- | --- | --- |
footholds to disrupt critical services, such as
| and inviting numerous nations to join BRICS  | the median line of the Taiwan Strait in shows  |     |     |
| -------------------------------------------- | ---------------------------------------------- | --- | --- |
communication infrastructure, in the event of a
| group in August 2023, bolstering the trade bloc  | of force. China has also become increasingly  |     |     |
| ------------------------------------------------ | --------------------------------------------- | --- | --- |
conflict with the targeted nation. They can also
© 2023 Cisco and/or its affiliates. All rights reserved.  |  talosintelligence.com page 20

2023
YEAR IN REVIEW
Subhead herelyhere
YEAR IN REVIEW
© 2023 Cisco and/or its affiliates. All rights reserved. | talosintelligence.com page 21
3202
Section highlights
• Russian state-sponsored APT Gamaredon has remained a major player
in threats against Ukraine and was the top threat that the Cisco Talos
Ukraine Task Unit responded to this year.
• In 2023, Gamaredon primarily targeted entities in North America and
Europe, with a disproportionate number of victims in Western Europe.
Additionally, over half of the entities targeted were in the transportation
and utilities sectors, reflecting Russia’s focus on critical infrastructure.
• Turla, another Russian government-affiliated APT, was largely active
Advanced between September 2022 and February 2023, but their operations
diminished significantly around May 2023, coinciding with the U.S. Justice
Department’s disruption of Turla’s Snake malware.
• The number of affected sectors and volume of victims between these two
persistent
groups vastly differed, contrasting Gamaredon’s broader targeting with
Turla’s more limited activity against highly selective victims.
• Beyond Gamaredon and Turla activity, we also observed a spike in
threats: Russia
SmokeLoader activity — malware used by a variety of different groups
— in late April and early May, aligning with CERT-UA’s reporting of mass
distribution of SmokeLoader targeting Ukrainian entities.
• To stabilize Ukraine’s power grid against the effects of global positioning
system (GPS) jamming on the battlefield, Cisco hardware and software
engineers modified one of our commercial network switches to provide
holdover for Ukraine’s power grid equipment during these outages.

2023
YEAR IN REVIEW
Advanced persistent threats: Russia
T hreats from Russian state-sponsored or state-aligned APTs remain a FIGURE 10
Industry verticals targeted by Gamaredon
mainstay in our threat tracking and research efforts this year. Since the
onset of the Russian invasion of Ukraine, Russian APTs’ engagement in
cyber espionage, cyber influence, and destructive attacks has intensified. In
line with activity reported in last year’s report, Russian APTs continue to adapt
to geopolitical challenges stemming from the war and NATO and allied nations’
military assistance to Ukraine. Additionally, 2023 saw a global law enforcement
effort to dismantle the Snake malware, considered one of the most prolific
and sophisticated cyber espionage tools in the Federal Security Service of
the Russian Federation’s (FSB) arsenal commonly deployed against systems
globally.
Gamaredon and Turla Russian APTs operating in this space. Turla FIGURE 11
also conducts long-term espionage and data
remain top threats, Industry verticals targeted by Turla
exfiltration operations that are in line with Russian
targeting patterns vary intelligence priorities that the U.S. government
attributes to a unit within the FSB. In contrast to
Russia-affiliated APT groups Gamaredon and Turla
Gamaredon, who we observed targeting a range of
continue to persist as top threats in this space,
sectors in 2023 (Figure 10), Turla is known for much
updating aspects of their attacks and toolkits to
more targeted operations against a smaller number
support their TTPs, despite international efforts to
of strategically important entities. Turla, who is
combat the Russian cyber threat.
publicly assessed to operate on behalf of a different
unit than Gamaredon in the FSB, is likely capable of
Cisco Talos closely tracks activities associated with
compromising a much broader spectrum of entities
Gamaredon, an APT broadly suspected to be a team
worldwide but limits their operations to what they
of Russian government-supported actors based
perceive to be high-value targets.
in Crimea. While the group in recent months has
concentrated their efforts on cyberespionage against
The number of sectors and volume of victims that
Ukrainian entities, they also target entities globally,
Gamaredon and Turla targeted vastly differed, based
with a less focused victimology as compared to other
on our telemetry (Figures 10 and 11).
Note: Percentages may not equal 100% due to rounding.
© 2023 Cisco and/or its affiliates. All rights reserved. | talosintelligence.com page 22

2023
YEAR IN REVIEW
Advanced persistent threats: Russia
FIGURE 12
Gamaredon malicious download activity throughout the year
“Beyond highlighting the
sectors that Gamaredon
and Turla targeted this
year, the data is also largely
representative of the
volume of attacks Snort
helped prevent.”
FIGURE 13
Activity across Turla malware variants Gazer, Kazuar, Mosquito and Neptun this year
The largest spread of Gamaredon victims were August 2023 is consistent with the group’s activity Malware deployed by and custom to Turla, including This clustering over time, as seen in Figure 13,
located in North America, followed by Europe levels according to a report by Ukraine’s National various backdoors and implants used for persistent of custom Turla malware continues to convey the
and the Middle East, with a disproportionate Coordination Center for Cybersecurity (NCCC). access, are seen to congregate in a series of events narrative of Turla’s operational tempo, likely highly
number of victims in western Europe. Over half of largely occurring between September 2022 and based on the selectivity of targets. Notably, the
In contrast to the range of industry verticals
Gamaredon’s targeting activity impacted the utilities February 2023. While the reason for the heightened depiction of Turla malware activity in Figure 13
Gamaredon targeted this year, Turla targeted
and transportation industry sectors, consistent with activity during that period is unknown, we asses (while not an exhaustive list) diminishes significantly
fewer victims across a smaller number of sectors
Russia’s targeting of critical infrastructure entities, it is likely to have stemmed from an increased around May 2023, coinciding with the U.S. Justice
and geographies, in line with the group’s precise
likely to cause the most disruption to strategic operational tempo in response to the Russian Department’s disruption of Turla’s Snake malware.
operations. The manufacturing and financial services
entities to stymie Ukraine’s war efforts. invasion on Ukraine. These four malware families — For nearly 20 years, Turla deployed Snake to steal
sectors were equally impacted, with education and
Gazer, Kazuar, Mosquito and Neptun — while not an and exfiltrate data from targeted systems through
In September and December 2022 and September agriculture targeted to a lesser degree (Figure 11).
exhaustive list of Turla malware, are part of Turla’s numerous relay nodes scattered around the world.
2023, we saw three clear spikes in Gamaredon Beyond highlighting the sectors that Gamaredon
large arsenal of bespoke malware and modified While the effects of the Snake disruption on Turla’s
activity (Figure 12), potentially representing clusters and Turla targeted this year, the data is also largely
open-source malware, which are constantly updated current and future operations are still unknown, the
of specific targeted operations. The ramped representative of the volume of attacks Snort
or replaced with more advanced versions. diminished malware activity may represent changes
up Gamaredon activity as seen in Figure 12 in helped prevent.
in Turla’s toolkit as a result of the disruption.
© 2023 Cisco and/or its affiliates. All rights reserved. | talosintelligence.com page 23

2023
YEAR IN REVIEW
Advanced persistent threats: Russia
FIGURE 14 Internal Task Unit continues to
Top threats in Ukraine task force investigations
monitor threats to Ukraine
Talos’ ongoing support for Ukraine continues to be a
large focus of our operational efforts this year. As part
of the Task Unit’s work, we monitor suspicious activity
in endpoint telemetry for nearly three dozen Ukrainian
partners across critical infrastructure sectors, including
government, utilities, financial services, health care and
transportation, among others.
While the threats against these organizations may not
all be designated as APT activity, the volume of threats
and volatile geopolitical climate they are deployed in
poses a significant risk to network defenders protecting
critical assets.
Gamaredon is the most dominant threat to Ukraine
that our task force has responded to (Figure 14). The
group has historically targeted predominantly Ukrainian
entities — particularly those responsible for the
FIGURE 15 country’s defense, diplomacy and internal security.
Top five malicious activities affecting Ukraine partners
Gamaredon, and portions of their attack chain,
consistently appear in top threat hunting alerts from
Cisco Secure Endpoint that notified our Ukrainian
partners (Figure 15). For example, these top five
behaviors demonstrate the consistent use of LoLBins
and the techniques associated with them, such as
Wscript execution — a legitimate Windows process
likely used to masquerade malware deployment under
the guise of expected activity — that continue to be
leveraged to support a variety of threats across an
attack lifecycle. Activity commonly linked to financially
motivated cybercriminals, like the deployment of
cryptocurrency mining and information stealers, also
continue to impact Ukrainian organizations across
numerous industries, speaking to the broad range of
threats facing Ukraine.
© 2023 Cisco and/or its affiliates. All rights reserved. | talosintelligence.com page 24

2023
YEAR IN REVIEW
Advanced persistent threats: Russia
FIGURE 16
SmokeLoader malware activity throughout the year
“The significant cyber
defense resources we
continue to devote to
protecting our Ukrainian
partners has undoubtedly
had a significant impact
on this threat space as
well, thwarting significant
disruptions by mitigating
attacks in the early stages.”
Beyond highlighting the consistent tempo of that the Task Unit has repeatedly responded to While the Task Unit has continuously responded and it is likely the result of combined efforts from
Gamaredon activities above, Figures 14 and 15 this year (Figure 14). Typically delivered via email, to a myriad of cyber threats since the onset of the the cybersecurity industry, U.S. government,
also help to demonstrate the multitude of threats SmokeLoader drops malware on infected machines Russia-Ukraine war, the observed activity in 2023 foreign partners, and Ukraine’s own commitment to
the Task Unit has responded to this year. This and since early May, has been consistently reported was far less sophisticated than what is typically protecting its people. The significant cyber defense
includes activities from malware threats such by Ukraine’s Computer Emergency Response Team associated with the sophisticated adversaries we resources we continue to devote to protecting our
as loaders, information stealers, ransomware, (CERT-UA) further highlighting its persistent use in would expect to see in this space. The activity Ukrainian partners has undoubtedly had a significant
cryptocurrency miners and Raspberry Robin, the threat landscape. was dynamic this year but does not reflect the impact on this threat space as well, thwarting
a prolific malware family covered in last year’s full range of destructive cyber capabilities Russia significant disruptions by mitigating attacks in the
We observed a spike in SmokeLoader activity in
annual report, which remains a consistent threat to has previously demonstrated against Ukraine and/ early stages.
late April and early May, aligning with CERT-UA’s
enterprise environments. For example, SmokeLoader or its NATO allies. The reasons behind this have
reporting of mass distribution of SmokeLoader
is a downloader leveraged by a variety of groups been debated by industry partners and experts,
targeting Ukrainian entities (Figure 16).
© 2023 Cisco and/or its affiliates. All rights reserved. | talosintelligence.com page 25

2023
YEAR IN REVIEW
Advanced persistent threats: Russia
Project PowerUp: Keeping Faced with the complex problem of how to make After months of development and coordination with How is Ukraine’s
Ukraine’s substations resistant to operational failures various partners, the devices were delivered to Ukraine
the lights on in Ukraine power grid
caused by downed GPS signals, Cisco hardware and and installed in substations around the country, no small
affected when
software engineers modified one of our commercial feat during an active war zone. This story will be featured
Leveraging Talos’ unique relationships with industry,
network switches, the Cisco Industrial Ethernet switch, in Cisco’s annual Purpose Report later this year. This
government, and Ukraine, we spearheaded an effort to GPS goes down?
to provide holdover for Ukraine’s power grid equipment example further demonstrates how Cisco’s efforts have
help stabilize Ukraine’s power grid against the effects of
during these outages. helped safeguard Ukraine’s critical infrastructure from
GPS jamming on the battlefield.
Many of Ukraine’s high-voltage
severe Russian cyberattacks in 2023.
electrical substations — which
play a vital role in the country’s
domestic transmission of
power — make extensive use
of the availability of precise
GPS timing information to
help operators anticipate,
react and diagnose a complex
high-voltage electric grid.
When GPS signals are
widely disrupted, substations
cannot synchronize their time
reporting accurately because
they cannot assign accurate
timestamps. Without good
synchronized data, efforts
to manage loads between
different parts of the system
can be affected, and this
management avoids outages
and failure, especially during
peak demand and surge
times. This disruption can be
widespread, causing wide
areas to lose GPS service for
long periods of time.
© 2023 Cisco and/or its affiliates. All rights reserved. | talosintelligence.com page 26

2023
YEAR IN REVIEW
Advanced persistent threats: Russia
FIGURE 17
YoroTrooper threat actor matrix
Some YoroTrooper
members hail from
pro-Russia Kazakhstan
Earlier this year, Cisco Talos disclosed information
on a new threat actor we named “YoroTrooper,”
who we assess with high confidence consists,
at least in part, of individuals from Kazakhstan.
YoroTrooper is a highly motivated threat actor
whose low sophistication is complemented with
aggressive targeting of entities using a multitude of
commodity malware families. Since 2022, the group
has conducted operations aimed at espionage and
data theft against victims in the government or
energy sectors in Azerbaijan, Tajikistan, Kyrgyzstan
and other members of the Commonwealth of
Independent States (CIS).
APT activity from Russian allies Union (EU) health care agency and the World Intellectual access. Recent activities, also tracked by CERT-UA, demonstrate
Property Organization (WIPO). Successful compromises also the group’s exploitation of the WinRAR ZIP parsing vulnerability,
Talos’ research and monitoring efforts of regional threats have
included embassies of European countries including Azerbaijan CVE-2023-38831. The vulnerability allows attackers to hide
expanded to APT activity attributed to countries formerly part of
and Turkmenistan. malicious code in ZIP archives masquerading as popular file
the Soviet Union, whose intelligence goals, TTPs and victimology
formats including JPG or TXT files, which GhostWriter
This year, Talos has also been monitoring GhostWriter operational
often align with the Kremlin. Given the long-standing political
leveraged to deploy Cobalt Strike and the malware
activities, which is a group allegedly linked to the Belarusian
union between these governments, collaboration is plausible.
downloader, PicassoLoader.
government, according to CERT-UA. We have observed several
However, we do not have direct evidence of Russian government
GhostWriter campaigns against government entities, military We cannot rule out Russian contributions to YoroTrooper
involvement.
organizations and civilian users in Ukraine and Poland. We judge or GhostWriter at this time. These operations and targeting
We assess YoroTrooper also targets organizations of strategic
that these operations, often seen promoting anti-NATO narratives patterns, often strongly aligning with Russian strategic interests,
value across European and Turkish governments (Figure 17). For
that aim to undermine regional security cooperation, are very are key for understanding regional threats against the backdrop
example, YoroTrooper has compromised accounts for at least
likely aimed at stealing information and gaining persistent remote of the Russian invasion of Ukraine.
two international organizations, including a critical European
© 2023 Cisco and/or its affiliates. All rights reserved. | talosintelligence.com page 27

2023
YEAR IN REVIEW
Subhead herelyhere
YEAR IN REVIEW
© 2023 Cisco and/or its affiliates. All rights reserved. | talosintelligence.com page 28
3202
Section highlights
• Events in early October 2023 between Hamas and Israel contributed to
several politically motivated hacktivist groups launching uncoordinated
and mostly unsophisticated attacks against both sides, similar to what we
observed at the beginning of the Russia-Ukraine war.
• The Middle East’s complicated geopolitical environment continued to
be dynamic this year, and we will likely see that impact the cyber realm
going forward. As longtime regional adversaries attempt to normalize ties,
and decades-old conflicts spark new violence, major cyber players with
economic and political interests in the Middle East, like China and Iran,
Advanced
may be more motivated to influence outcomes through direct or proxy
operations.
• Middle East-based APT groups targeted telecommunications firms in the
persistent region, following the trend we have seen of sophisticated adversaries
targeting this sector. As part of this activity, we identified a new intrusion
set, ShroudedSnooper, deploying novel implants we dubbed HTTPSnoop
and PipeSnoop against related entities.
threats:
• The Iran state-sponsored MuddyWater APT group relied less on
the commonly used Syncro tool — essential for remote access and
malware deployment — than in previous years, likely in response to the
cybersecurity industry’s action against known MuddyWater TTPs.
Middle East

2023
YEAR IN REVIEW
Advanced persistent threats: Middle East
R egional state-sponsored groups continue to conduct Hamas-Israel conflict brings Significant geopolitical events like this also invite the
participation of much more sophisticated adversaries,
influx of hacktivist groups
pervasive cyber attacks against entities in North America,
including those supported and funded by foreign
Europe, the Middle East and Asia. Telecommunications state governments. We have seen this most recently
Hamas’ surprise attack on Israel in October not only
in Ukraine, where advanced state-sponsored actors
had global implications but also has affected the
companies endured the most of these attacks, a trend that
from Russia like Gamaredon and Turla have been
cyber realm, immediately drawing in actors from both
has transcended multiple APTs, as outlined in other parts of relentless in their targeting of Ukranian entities since
sides of the conflict. Politically motivated hacktivist
the start of the war. Likewise, we expect to see an
groups — including well-known actors like Killnet and
this report. Our work in this space resulted in the discovery of
increase in Iranian cyber activity in the Middle East
Anonymous Sudan as well as lesser-known groups —
a new actor we named ShroudedSnooper that appears intent following Hamas’ attack on Israel. Iran and Israel
launched uncoordinated and mostly unsophisticated
are longstanding adversaries, and their decades-
attacks at the outset, as the threat space was quickly
on targeting major telecommunications entities in the region.
old conflict has major influence on Iran’s cyber
flooded with many different actors. Several hacktivist
The Iran state-sponsored MuddyWater APT actor remains a operations. Iran is also a key backer of several
groups quickly announced support for both sides in
anti-Israel militant and terrorist groups, including
the Israel-Hamas conflict, posted threatening political
key player in this threat space and was the focus of much of
Hamas, Hezbollah, and the Palestinian Islamic Jihad,
messages, called on followers to join in and claimed
our research efforts this year. While the group continues to use which were all involved in this most recent spate
responsibility for DDoS attacks against targets of
of violence against Israel. Iran’s support for these
interest — typical hacktivist TTPs. This is broadly
many of the same techniques to advance their primary goals of
groups and Tehran’s historical hostility with Israel
consistent with what we observed at the start of the
stealing intellectual property and collecting intelligence, industry strongly suggests Iran may use its cyber capabilities
Russia-Ukraine war, when an influx of cyber activity
to influence the outcome of the crisis, much like other
became concentrated on these countries
action has likely influenced the group’s ability to use certain tools,
nations rely on cyber as an essential tool to advance
seemingly overnight.
including the Syncro remote management and monitoring (RMM) foreign policy objectives.
platform that the group was using at the end of 2022.
The Middle East is arguably the most complicated geopolitical
region in the world, and the conflict that ignited between Hamas
“The Iran state-sponsored MuddyWater APT actor remains a key player
and Israel in October 2023 reminds us that events with global
in this threat space and was the focus of much of our research efforts
consequences can unfold quickly and with little notice. The
this year. While the group continues to use many of the same techniques
everchanging geopolitical landscape here will undoubtedly affect
to advance their primary goals of stealing intellectual property and
cyber activity going forward, as established regional players like
collecting intelligence, industry action has likely influenced the group’s
Iran remain intent on achieving certain geopolitical goals and new
ability to use certain tools.”
actors like China seek to expand its influence.
© 2023 Cisco and/or its affiliates. All rights reserved. | talosintelligence.com page 29

2023
YEAR IN REVIEW
Advanced persistent threats: Middle East
Chinese ambitions FIGURE 18 Telecommunications sector telecommunication firms. OfficeTrack is an application
HTTPSnoop URLs masquerading as promoted as a workforce management solution
in the region portend possible remains key target for regional
developed by OfficeCore, a software company
OfficeCore’s LBS System
cyber operations threat actors that helps users manage administrative tasks. In
several instances, we saw URLs ending in “lbs” and
While China has traditionally held a prominent economic role In 2023, we discovered a new intrusion set,
“LbsAdmin,” references to the application’s former
in the Middle East as one of the largest foreign investors, ShroudedSnooper, deploying novel backdoor
name (OfficeCore’s LBS System) before it was
PRC leadership sought to also expand their political implants, HTTPSnoop and PipeSnoop, against
rebranded to OfficeTrack (Figure 18).
presence in the region this past year by engaging in regional telecommunications providers in the Middle East,
Throughout our analysis of the ShroudedSnooper
conflict mediation. In March, Beijing brokered an agreement a continuation of a trend we have been monitoring
implants, the adversary used multiple URLs consisting
between longtime adversaries Iran and Saudi Arabia to in which sophisticated actors frequently target this
of patterns mimicking provisioning services from
reestablish diplomatic ties, and in September, China and Syria sector. There is currently not enough evidence to
telecommunications companies, including an Israeli
announced a strategic partnership, as Syrian President Bashar link ShroudedSnooper activity to a specific country.
telecommunications provider, likely to blend into
Assad begins to reenter the international fold after more than However, the group’s consistent masquerading of
typical network traffic. The DLL-based variants of
a decade of brutal civil war. The China-Syria deal may also software applications used by telecommunication
HTTPSnoop usually rely on DLL hijacking in benign
provide great economic incentives for Beijing, which could firms in the region and impact to several regional
applications and services to get activated on the
become a major financial backer of Syria’s reconstruction providers highly aligns with likely state-sponsored
infected system, which was highlighted as a top
efforts. These strategic moves by China come at a time when actors and sophisticated adversaries around
technique this year in earlier sections of this report.
the U.S. has largely withdrawn from the region following the the world.
post-9/11 period, and Beijing likely sees this as an opportunity
The HTTPSnoop and PipeSnoop implants consist of
to capitalize on waning U.S. involvement and influence there.
novel techniques to listen to incoming requests for
Because of China’s growing political presence in the specific HTTP(S) URLs and execute on an infected
Middle East, we expect to see more Chinese APT activity endpoint. Some of the HTTPSnoop implants use
in the region. We have observed Chinese APTs, among URLs that masquerade as those belonging to
the most active and persistent of state-sponsored threats, OfficeTrack, which is especially marketed toward
supplementing financial endeavors with espionage
operations in regions it is invested in, targeting private sector
Because of China’s growing political
organizations and governments whose intellectual property
presence in the Middle East, we
aligns with economic goals. Future operations would likely
be in-line with well-established Chinese APT TTPs, like
expect to see more Chinese APT
targeting entities and individuals that operate in industries
activity in the region.
essential to China’s strategic plans, establishing long-term
and stealthy access to targeted networks, and stealing
intellectual property and technology.
© 2023 Cisco and/or its affiliates. All rights reserved. | talosintelligence.com page 30

2023
YEAR IN REVIEW
Advanced persistent threats: Middle East
Industry actions likely affected
MuddyWater operations
Syncro leveraged to
In late 2022, it was first reported that Iranian-backed APT group maintain access
MuddyWater was using the Syncro remote management tool to take
over target devices. This activity is consistent with Talos IR data from
In an incident affecting a
Q4 2022 (October - December 2022), where a growing number of
telecommunications company,
adversaries were increasingly relying on Syncro, observed in nearly 30
Talos IR identified company email
percent of engagements.
accounts sending phishing emails
In December 2022, Syncro released a statement addressing concerns with subject lines that translated
about MuddyWater’s deployment of Syncro in spear phishing from Arabic to “Staff Promotion.”
campaigns targeting organizations in the Middle East and Asia. The The emails contained OneDrive
company implemented additional verification measures for new trial and OneHub phishing links with a
account creation to limit the use of Syncro by illegitimate actors, and compressed Microsoft Windows
monitored for irregular account information and usage, terminating Installer (MSI) file that installed
accounts that violate these new policies. Syncro. The adversary used
Syncro to stay connected to
This swift action taken by Syncro most certainly has had an impact
the targeted user’s workstation.
on MuddyWater operations, highlighting the direct effect industry can
During analysis of the MSI
have on thwarting components of advanced adversaries’ operations.
file, multiple Syncro services
While the reason for Syncro’s increased usage in Q4 2022 was
were also installed, including
unknown, its use as a fully featured remote access platform for
SyncroRecovery (SyncroLive) and
managed service providers (MSPs) and its ubiquity across enterprise
SyncroOvermind. The adversary’s
environments likely made it an attractive option.
tactics appeared to focus on
maintaining initial access through
installation of Syncro. The lack
of MFA for email access allowed
“This swift action taken by Syncro most
the adversary to perform phishing
certainly has had an impact on MuddyWater attacks, highlighting the need
to ensure MFA across all critical
operations, highlighting the direct effect
assets.
industry can have on thwarting components
of advanced adversaries’ operations.”
© 2023 Cisco and/or its affiliates. All rights reserved. | talosintelligence.com page 31

2023
YEAR IN REVIEW
Subhead herelyhere
YEAR IN REVIEW
Section highlights
• Commodity loaders such as Qakbot, Ursnif, Emotet, Trickbot and IcedID
represent some of the most impactful and pervasive threats, as actors
routinely rely on them to enable key parts of their operations. Their use
as downloaders for information-stealers, ransomware, and other malware
have made them mainstays in the threat environment, indiscriminately
affecting entities globally.
• All these loaders formerly functioned solely as banking trojans, and
developers have diversified their capabilities in recent years to support
more advanced operations. In 2023, new versions of IcedID, Ursnif, and
Qakbot appeared to be tailored specifically for ransomware actors, based
on their enhanced reconnaissance features, removal of functions that
might trigger antivirus detections, and quick adoption by ransomware
groups and initial access brokers.
• Microsoft’s disabling of macros by default caused commodity loader
actors to invent new ways to use macros undetected or avoid using them
entirely. Qakbot operators used a wide variety of file types, scripting
languages, packers, and exploits to deploy the loader. Emotet, IcedID,
and Ursnif varied their techniques, although less frequently compared to
Qakbot, and also tended to still rely on older TTPs.
• It can be challenging to eradicate the threat of commodity loaders
even after the botnet is dismantled, as developers have been known to
continue operating on behalf of different malware groups or rebuild their
botnets. Furthermore, previously compromised infrastructure could be
leveraged by other threat actors for malicious activity.
© 2023 Cisco and/or its affiliates. All rights reserved. | talosintelligence.com page 32
3202
Commodity
loaders

2023
YEAR IN REVIEW
Commodity loaders
A ctors have consistently relied on FIGURE 19
IcedID activity increased around release of the new variant
commodity loaders for years, and 2023
was no different. Many of these threats
are widely available for purchase on underground
forums, provide a low barrier of entry for
unsophisticated actors, and are highly modular,
allowing threat actors to carry out multiple
phases of an attack. Throughout 2023, Qakbot,
Ursnif, Emotet, Trickbot and IcedID stood out as
the most impactful threats in this space.
Commodity loaders’ updates seem
tailored to support ransomware activity
In late 2023, we observed the latest variants of IcedID and Ursnif,
and a new automated feature in Qakbot, supporting ransomware
deployment, following a trend of commodity loaders playing an
integral part in the ransomware infection chain. These updates
between November 2022 and February 2023— group of sophisticated cyber criminals first active The updates included a list of reconnaissance
were tailored to enhance the malware’s dropper functionalities,
corresponding with the new versions’ release— in September 2022, and suspected by many commands to map out the customer’s
likely signifying a further shift away from their original intended use
suggesting actors were keenly interested in trying security professionals to be a rebrand of the environment upon initial infection. The output of
as banking trojans. Trickbot and Emotet are also known to facilitate
out the threat’s latest capabilities (Figure 19). prolific Russian ransomware group Conti. Royal these commands enumerated data that would
ransomware attacks, however, they did not receive similar upgrades
tightly controls their malware and ransomware be most useful to ransomware groups, including
in 2023. The latest Ursnif variant, which was similarly
operations, unlike many other ransomware domain groups, the domain name, and names
retooled to exclude banking trojan functionality,
In November 2022 and February 2023, IcedID developers released groups that arose in the last two years who of domain controllers. This information could
was also seemingly intended to support
two new versions that were stripped of their banking functionalities chose to operate as a RaaS. Therefore, an assist with lateral movement resulting in Active
ransomware deployment. In 2023, this updated
and designed to solely function as droppers. In 2023, these versions, exclusive partnering of the new Ursnif variant Directory takeover, a tactic commonly used by
version (released in 2022) was adopted by
dubbed “Forked” and “Lite,” were used by initial access brokers, and Royal is likely intentional and could imply an ransomware groups. Qakbot’s new automated
the prolific ransomware group Royal, the first
known for commonly selling network accesses to ransomware groups. affiliation between the developers. reconnaissance capabilities also may have
instance of any ransomware gang incorporating
While the original version was also used by initial access brokers and helped ransomware groups evade detection,
Ursnif into their operations. Since Royal is the Finally, in late 2022, Qakbot deployed several
ransomware groups, the new versions are likely a more attractive because the gathered data could be used to
only group that has been observed leveraging new automated features, including a capability
option because they were stripped of functions that might trigger AV formulate a detailed plan of attack, minimizing the
this new variant, there may be a professional ideally suited to helping ransomware groups
signatures, thereby making them stealthier. IcedID activity increased time between initial infection and encryption.
association between the developers. Royal is a determine valuable targets prior to deployment.
© 2023 Cisco and/or its affiliates. All rights reserved. | talosintelligence.com page 33

2023
YEAR IN REVIEW
Commodity loaders
Commodity loader operators evolved malware automatically when a victim clicks on a malicious
attachment in a phishing email. Now, the user receives a security
TTPs in response to new security
warning if they click on a potentially malicious attachment, Sample reconnaissance
updates blocking macros, continuing reducing the likelihood of downloading malware. Microsoft’s
commands we observed
disabling of macros continued to have an impact throughout
a trend that began in mid-2022
2023, as threat actors invented new ways to use macros deployed by Qakbot
undetected, or to avoid using macros entirely. When Microsoft
In 2023, Microsoft blocked macros by default, a notable change affiliates in 2023
created a new patch to update security features, threat actors
that caused actors to modify their initial access and malware
were able to quickly change their TTPs in a game of cat-and-
delivery techniques. Prior to the change, macros would run
Threat actors conduct reconnaissance to gather
mouse (Figure 20).
automatically when Microsoft Office documents were opened.
information for additional operations. We observed
Macros have been heavily abused by threat actors to execute
Qakbot affiliates abusing common Windows utilities
that allow for command execution in an attempt to
hide among legitimate activity. Below are just a few
FIGURE 20 examples to demonstrate the potential harmful impact
of these commands.
Commodity loaders allow threat actors to quickly change TTPs in response to changing security features
Netstat -nao: Used to obtain a list of open ports that
are particularly vulnerable to malicious attacks and a
list of active connections between the infected host
and other systems, such as a cloud environment, to
determine whether the victim can access data that is
of value to the threat actor.
Net localgroup: Used to identify administrator
accounts (i.e., accounts with elevated privileges that
can access sensitive data and make changes to the
system). This information helps a threat actor know
which accounts to prioritize in their targeting efforts.
Arp -a: Used to display the ARP cache, a record
of each IP address and its corresponding MAC
address that made a connection to the infected
host. With this information, an attacker can position
themselves between the communication of two or
more networked devices to steal additional data or
manipulate transmitted data.
© 2023 Cisco and/or its affiliates. All rights reserved. | talosintelligence.com page 34

2023
YEAR IN REVIEW
Commodity loaders
In a trend that began in 2022 and continued throughout 2023, adversaries using FIGURE 21
commodity loaders repeatedly changed their TTPs in response to new Microsoft security Sample infection chain using OneNote with an embedded macro-enabled file to deliver malware
updates. In November 2022, Microsoft issued two patches to detect and block macros-
enabled content within container files, such as ZIP and LNK, which had been a popular
method for surreptitiously using macros. Just a few weeks later, we observed a surge
in threat actors, including those using Qakbot, Emotet and IcedID using OneNote file
attachments to deploy malware. While using OneNote to deliver malware was not a new
technique, it facilitated delivery of macros-enabled documents without being detected,
which is highly favorable among affiliates wishing to bypass AV detection (Figure 21).
Then in January, Microsoft quietly issued an update, so all macros-enabled documents
embedded within OneNote files would be blocked by default, meaning the user would
receive a security warning when opening a OneNote attachment embedded with macros.
We still saw threat actors using OneNote, but with crafty social engineering techniques
that manipulated victims into ignoring the warnings. In one observed campaign deploying
IcedID, the threat actor used a DocuSign lure to trick the victim into clicking a button with
FIGURE 22
an embedded link. The “Decrypt and View Message” button actually contained a malicious
HTML Application (HTA) file (Figure 22). When opened, the HTA file was dropped into the Sample infection chain attempting to manipulate victims into ignoring a security alert
OneNote directory for execution.
page 35

2023
YEAR IN REVIEW
Commodity loaders
FIGURE 23
Sample infection chains that do not rely on macros
FIGURE 24 Finally, in April 2023, Microsoft issued another update search engine optimization (SEO) to increase visibility. If
Emotet infection chain using binary padding that blocked users from opening files with a potentially the user clicks on the malicious ad, a Google Ad services
dangerous extension embedded in OneNote. To open an URL will be generated, which then generates a secondary
attachment marked as potentially dangerous, OneNote URL that leads the user to the malicious, spoofed domain
users would need to save the file to their device and open with download links that deliver the various threats. Talos
it from there, allowing security applications running on the observed legitimate software products spoofed in these
device to detect any malicious code in the attachment. This campaigns, such as Microsoft Teams and WhatsApp, and
latest update caused many operators to abandon OneNote popular password managers like 1Password. Threat actors’
as a method to hide the use of macros. Instead, we use of Google Ads and Google Search makes their lures
observed actors turning to filetypes that execute malware appear highly legitimate, as users are probably less likely to
without relying on macros, such as JavaScript files which question the authenticity of paid advertisements prioritized
rely on LoLBins for execution (Figure 23). at the top of their search results.
Aside from OneNote, threat actors also experimented with While many affiliates introduced new TTPs in 2023 in
other methods of deploying malware that did not rely on response to evolving security updates, we also observed
macros or could use macros without detection. Since at commodity loaders using older methods. For example,
least December 2022, we have observed threat actors co- Emotet, IcedID, and Ursnif were all observed using macros-
opting the Google Ads platform to deploy malware such enabled Office documents in the initial infection chain.
as Ursnif, IcedID, and Trickbot, a method that completely Furthermore, we observed Emotet being delivered in
avoids using macros. The attack chain in these campaigns phishing emails with old “RedDawn” templates first seen in
begins with a user entering a search term for a software 2020 (Figure 24). While these operators may be capable
or service in the Google search engine. Once Google’s of more sophisticated attacks, it’s possible they have
results page loads, the malicious ads will typically be first in still found success using older TTPs, especially against
the list of results, as the actors have been observed using unpatched, enterprise legacy systems.
© 2023 Cisco and/or its affiliates. All rights reserved. | talosintelligence.com page 36

2023
YEAR IN REVIEW
Commodity loaders
Top five commodity will typically tailor phishing lures for the
targeted geography. For example, in
loaders are similarly
2023, we observed Ursnif predominantly FIGURE 25
deployed against deployed against businesses located World map of regions impacted by commodity, from most to least targeted
in the U.S. and Italy in mass “spray
sectors globally in
and pray” spam campaigns using the
mass opportunistic languages of the targeted countries.
campaigns We have observed loaders primarily
deployed against businesses, as opposed
In 2023, we observed all five commodity
to targeting individuals’ financial data, a
loaders impacting businesses worldwide,
shift that occurred as the malware was
primarily affecting North America and
less frequently used as banking trojans.
Europe (Figure 25). These geographical
This is reflected in the phishing lures we
targets do not necessarily reflect a
observed. For example, in late-March,
coordinated preference among operators
we saw an uptick in Emotet targeting U.S.
because the threats are sold as a
businesses that pay quarterly taxes. The
malware-as-a-service (MaaS). Therefore,
lures used themes related to the Internal
patterns in targeting are aligned with
Revenue Service (IRS) with subject lines
whatever group is executing the campaign
such as “IRS Tax Forms W-9,” which
and can vary.
was also seen last year at the end of
the November 2022 business quarter.
We predominantly observed mass
W-9 forms are typically distributed by
spam campaigns that opportunistically
companies or financial institutions to
attempted to compromise vulnerable
their employees.
targets, likely with the intent to move
laterally towards a more hardened target
after the initial infection. Adversaries
© 2023 Cisco and/or its affiliates. All rights reserved. | talosintelligence.com page 37

2023
YEAR IN REVIEW
Commodity loaders
FIGURE 26
Trickbot activity over time
Threats from commodity  they are still active—albeit delivering different  portions of its infrastructure to help rebuild the  in the charts above by a more dramatic spike or
|     | threats – leaving open the possibility that they  | Emotet botnet. | irregular patterns. |
| --- | ------------------------------------------------- | -------------- | ------------------- |
loaders can persist
rebuilt the Qakbot botnet or rebrand themselves
|                            |                           | Even if threat actors opt to cease cybercriminal     | Meanwhile there are always new commodity           |
| -------------------------- | ------------------------- | ---------------------------------------------------- | -------------------------------------------------- |
| long after their botnets   | under a different name.   |                                                      |                                                    |
|                            |                           | activity, we may still observe zombie activity from  | loaders to replace formerly prolific botnets like  |
are dismantled  We have seen other malware developers  infected Qakbot devices. We have seen this from  Qakbot and Trickbot. For example, IcedID may
|     | also continuing to operate in the cyber threat  | Trickbot, where our telemetry picked up activity  | be a logical choice to fill the void left by Qakbot.  |
| --- | ----------------------------------------------- | ------------------------------------------------- | ----------------------------------------------------- |
In August 2023, the prolific Qakbot commodity  landscape after their botnets were dismantled.  throughout 2023 even though their infrastructure  There is a historical precedence, as IcedID
loader was disrupted in a major global law  For example, even after Trickbot took down its  was dismantled in February 2022. This is  attracted affiliates after Emotet was dismantled
enforcement operation, but dismantling  infrastructure in February 2022, the U.S. and UK  likely due to old infections that have yet to be  in 2021. Furthermore, many Qakbot affiliates
botnet infrastructure does not always mean  still sanctioned the developers in February and  remediated or threat actors leveraging previously  are likely already familiar with IcedID because
cybercriminals cease to operate. Going forward,  September 2023, implying they are still active  compromised infrastructure. Looking at Trickbot  there are numerous instances of the two being
it’s possible Qakbot may reemerge after a  in the cyber threat landscape. The developers  activity over the past year, we can see it hovered  deployed together as part of the same campaign.
several-month hiatus — as we have seen in similar  may have chosen to create other types of  around the same median number, supporting our  Finally, the recent advanced IcedID update shows
scenarios involving other loaders like Emotet —  malware, or work with other groups they have  assessment that the botnet is still active in some  the developers are capable of, and motivated to,
further underscoring the need to monitor and  had longstanding relations with, such as Emotet  capacity, but the developers are not actively  maintain a high-quality product.
| report on this threat. Notably, the threat actors  | and Conti. In 2022, a series of leaks revealed    | engaged in growing the botnet (Figure 26).      |     |
| -------------------------------------------------- | ------------------------------------------------- | ----------------------------------------------- | --- |
| behind Qakbot were not apprehended during the      | close professional relations between developers   | Any new campaigns or infrastructure, such as    |     |
| global takedown, and our latest findings indicate  | of Trickbot and Conti and in 2021, Trickbot lent  | IPs or C2 servers, would likely be represented  |     |
© 2023 Cisco and/or its affiliates. All rights reserved.  |  talosintelligence.com page 38

<!-- CONVERSION_METADATA: {"source": "https://github.com/jacobdjwilson/awesome-annual-security-reports", "date": "2026-10-19", "model": "gemini-3.8-flash"} -->
