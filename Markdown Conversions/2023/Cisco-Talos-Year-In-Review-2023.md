# Cisco Talos Year In Review

## Table of Contents
- [Introduction](#introduction)
- [Telemetry trends](#telemetry-trends)
- [Ransomware and extortion](#ransomware-and-extortion)
- [Network infrastructure](#network-infrastructure)
- [Advanced persistent threats: China](#advanced-persistent-threats-china)
- [Advanced persistent threats: Russia](#advanced-persistent-threats-russia)
- [Advanced persistent threats: Middle East](#advanced-persistent-threats-middle-east)
- [Commodity loaders](#commodity-loaders)

---

# Introduction

Ransomware, commodity loaders, and APTs dominated the threat landscape in 2023. As outlined in the second annual Cisco Talos Year in Review, global conflict influenced cybersecurity trends, shifting many threat actors’ tactics and approaches in operations ranging from espionage to cybercrime.

Cisco’s global presence and Talos’ world-class expertise provided a massive amount of data to sift through — endpoint detections, incident response engagements, network traffic, email corpus, sandboxes, honeypots, and much more. Thankfully, our teammates include subject matter experts from all ends of the cybersecurity space to help us turn this intelligence into actionable information for defenders and users. Leveraging these rich, complex sources of information, we analyzed the major trends that shaped the threat landscape in 2023.

Ransomware continued to threaten enterprises globally in 2023, with LockBit remaining the top threat in this space for the second year in a row. Health care was the top targeted industry this year, as adversaries maintained their focus on entities that have cybersecurity funding constraints and low downtime tolerance. Not all things were the same, though, as we saw actors such as Clop deploy a collection of zero-day exploits, behavior we usually associate with advanced persistent threat (APT) activity. At the same time, leaked ransomware source code allowed low-skilled actors to enter the fray. Further complicating matters, we observed a new trend of ransomware actors turning to pure extortion, skipping encryption altogether while threatening to leak sensitive data.

Commodity loaders are still being used to deliver these ransomware threats, and many of the same families as last year remained prevalent, such as Qakbot and IcedID. This is reflected in our telemetry, as the most commonly spoofed brands were in financial services and shipping, hallmarks of these adversaries. But these loaders are shedding all remnants of their banking trojan past as they position themselves more as sleek payload delivery mechanisms. Developers and operators are adapting to improved defenses, finding new ways to bypass increasing security updates and compromise victims. And although we again observed a takedown of a large botnet, this year being Qakbot, our experience shows that this does not necessarily mean that the threat has been eliminated.

One of the newer cross-regional trends we have observed this year is an increase in the targeting of network devices from APTs and ransomware actors. Both groups rely on exploiting recently disclosed vulnerabilities and weak/default credentials, one of the reasons why the use of valid accounts was consistently a top weakness in Talos IR engagements. Whatever the sophistication and intent of the adversary is, the reason behind the targeting is the same: network devices are extremely high value while possessing many security weaknesses.

Geopolitical instability is manifesting in APT activity. This is reflected in our telemetry, which shows a rise in suspicious traffic during major geopolitical events. For Chinese groups, as relationships with the West and Asia Pacific become further strained, we see an emboldening in operations, such as a greater willingness to cause destruction. We also observe this in their targeting of telecommunications organizations, which possess numerous critical infrastructure assets in strategically important geographies such as Guam and Taiwan. For Russian APTs, Gamaredon and Turla targeted Ukraine at an accelerated pace, but Russian activity in general for 2023 did not reflect the full range of destructive cyber capabilities we have seen it deploy in the past, potentially because of the concerted efforts of defenders.

One bright spot this year was Cisco’s determined efforts to create and deliver inventive security solutions that help strengthen our partners. Talos’ Ukraine Task Force continues to thwart attacks against critical Ukrainian partners. This year, we spear-headed an effort to stabilize Ukraine’s power grid against the effects of global positioning system (GPS) jamming on the battlefield by delivering modified Cisco switches into an active war zone. Cisco also launched the Network Resilience Coalition with leading industry partners, focusing on increasing awareness and providing actionable recommendations for improving network security. Relatedly, Talos’s Vulnerability Discovery and Research Team made investigating small office, home office (SOHO) and industrial routers a major priority, reporting 289 vulnerabilities to vendors to date, published across 141 Talos advisories.

As conflict in the Middle East worsens, we are once again positioned to help protect our customers and partners. Therefore, perhaps the overarching story of 2023 is this: as the daringness, sophistication, and persistence of our adversaries grows, so too does the resolve of defenders to interdict them in any way we can.

---

## Table of contents

- [Telemetry trends .................................................... 3](#telemetry-trends)
- [Ransomware and extortion .................................... 8](#ransomware-and-extortion)
- [Network infrastructure ........................................ 13](#network-infrastructure)
- [APTs: China .......................................................... 18](#advanced-persistent-threats-china)
- [APTs: Russia ......................................................... 21](#advanced-persistent-threats-russia)
- [APTs: Middle East ................................................. 28](#advanced-persistent-threats-middle-east)
- [Commodity loaders: Qakbot, Emotet, Trickbot, IcedID, Ursnif ............ 32](#commodity-loaders)

---

# Telemetry trends

## Section highlights

*   Suspicious network traffic captured by Cisco Security products revealed sharp increases in activity that often corresponded with major geopolitical events and global cyber attacks.
*   The most targeted vulnerabilities were older security flaws in common applications, consistent with the U.S. Cybersecurity and Infrastructure Security Agency’s (CISA) findings in recent years. Most of the top-targeted vulnerabilities we observed received maximum- or high-severity scores by Cisco Kenna and the Common Vulnerability Scoring System (CVSS) and were also included in CISA’s Known Exploited Vulnerabilities catalog. The high frequency of targeting attempts against these CVEs, paired with their significant impact, underscores adversaries’ preference to target unpatched systems that can cause major disruptions.
*   Threat actors abused common file extensions and spoofed well-known brands, common techniques that underscore the use of social engineering to enable operations like phishing and business email compromise (BEC). Adversaries are likely responding to Microsoft’s disabling of macros in 2022 by using different file types to hide their malware, such as PDFs, which was the top blocked file extension this year.
*   Financial services and shipping companies accounted for the brands we observed being spoofed most often in email telemetry, suggesting longstanding phishing themes for email-based commodity loaders like Emotet, Qakbot and Trickbot are still at play. Relatedly, phishing accounted for a quarter of known initial access vectors in Talos IR engagements this year, highlighting actors’ continued reliance on this technique.
*   The use of valid accounts was a top-observed MITRE ATT&CK technique, underscoring adversaries’ reliance on compromised credentials and use of existing accounts for various stages of their attacks. This is consistent with Talos IR data, which showed compromised credentials/valid accounts accounted for nearly a third of known initial access vectors in 2023.

---

## Regional trends over time

Suspicious traffic includes a wide variety of categorized information sourced from multiple Cisco Security products, including Umbrella, Secure Endpoint, Email Security Appliance (ESA), Meraki, SSE, and Secure Firewall. Examples include malicious domains blocked by Umbrella, records with malicious dispositions from Secure Endpoint, phishing emails from ESA, triggered Snort signatures from Secure Firewall and Meraki, and many others.

In North America, Europe, the Middle East, and Africa (EMEA), and Latin America, suspicious network traffic was periodic, following a Monday - Friday workday pattern for much of the year. Starting mid-year, we saw a break from this pattern marked by a dramatic increase in traffic blocked by our security products, often quadrupling the early part of the year’s normal behavior.

In mid-February, these regions experienced various spikes in web spam. While spam volume was up globally, it disproportionally affected the Asia Pacific, Japan, and China (APJC) region.

In APJC, suspicious traffic was less periodic and experienced large swings in volume between January and April. These changes leveled out through the spring and early summer.

Various international events and major cyber attacks overlayed on the graph suggest how such activity can affect the threat landscape. While it’s impossible to prove causation, there are obvious correlations between the suspicious global and regional traffic patterns we observed and significant world events.

*   **January**: "ESXiArgs" ransomware attacks infect thousands of servers worldwide
*   **February**: Powerful earthquake kills more than 40,000 people in Turkey and Syria, prompting humanitarian crisis that threat actors commonly exploit for financial gain
*   **March**: U.S. downs suspected Chinese spy balloon, sparking international incident; Chinese President Xi Jinping meets with Russian President Vladimir Putin in Russia, while Japanese Prime Minister visits Ukraine in dueling diplomatic efforts
*   **April**: China brokers Iran-Saudi Arabia mediation; Chinese President Xi Jinping elected to a third five-year term; Clop ransomware actors begin exploiting zero-day vulnerability in the MOVEit file transfer software affecting hundreds of organizations
*   **May**: Ukrainian military begins counteroffensive to reclaim Russian-held territory
*   **June**: Anonymous Sudan claims DDoS attacks against Microsoft Outlook
*   **July**: Rebels depose Niger’s Western-allied president, causing global security implications
*   **August**: New Rhysida ransomware group likely responsible for attack that disrupts several U.S. hospitals
*   **September**: U.S., Japan, and South Korea presidents meet at summit aimed at countering threats from China and North Korea

**REGIONAL KEY**
*   North America (NA)
*   Asia Pacific, Japan and China (APJC)
*   Europe, the Middle East and Africa (EMEA)
*   Latin America (LATAM)

---

## Top targeted vulnerabilities

In 2023, cyber threat actors exploited older software vulnerabilities in common applications. In many cases, the vulnerabilities were more than 10 years old, consistent with CISA’s finding that adversaries have targeted old security flaws more than newly disclosed ones in recent years. In fact, four of the top five most-targeted vulnerabilities we observed were also cited by CISA as being frequently exploited in prior years, further highlighting this point. This underscores the need for entities to regularly install software updates, as many of these systems were likely unpatched given the age of the targeted vulnerabilities.

The top targeted vulnerabilities are found in common applications, like Microsoft Office. This finding is also substantiated by CISA, which noted that actors in 2022 prioritize CVEs that are more prevalent in their targets’ networks. Adversaries likely prioritize targeting widespread vulnerabilities because the exploits developed for such CVEs can have long-term use and high impact.

Lastly, most of the vulnerabilities on our list would cause substantial impact if exploited, with six receiving a maximum vulnerability risk score of 100 from Cisco Kenna and seven receiving the highest “critical” score from the Common Vulnerability Scoring System (CVSS). Most of the CVEs are also listed in CISA’s Known Exploited Vulnerabilities catalog, which is meant to inform users on the security flaws for which they should prioritize remediation. The high frequency of targeting attempts against these CVEs, paired with their severity, underscores the risk to unpatched systems.

| Ranking | CVE            | Vendor    | Product                      | CISA findings                                       | CISA KEV catalog | Kenna/CVSS |
| :------ | :------------- | :-------- | :--------------------------- | :-------------------------------------------------- | :--------------- | :--------- |
| 1       | CVE-2017-0199  | Microsoft | Office and WordPad         | Routinely exploited in 2022                         | Yes              | 100/9.3    |
| 2       | CVE-2017-11882 | Microsoft | Exchange server              | Routinely exploited in 2022                         | Yes              | 100/9.3+   |
| 3       | CVE-2020-1472  | Microsoft | Netlogon                     | Routinely exploited in 2022                         | Yes              | 100/9.3    |
| 4       | CVE-2012-1461  | Gzip file parser utility | Multiple antivirus products |                                                     |                  | 58/4.3     |
| 5       | CVE-2012-0158  | Microsoft | Office                       | Commonly exploited by state-sponsored actors from China, Iran, North Korea, and Russia (2016-2019) | Yes              | 100/9.3    |
| 6       | CVE-2010-1807  | Apple     | Safari                       |                                                     | Yes              | 84/9.3     |
| 7       | CVE-2021-1675  | Microsoft | Windows (print spooler)      |                                                     | Yes              | 100/9.3    |
| 8       | CVE-2015-1701  | Microsoft | Windows (kernel-mode driver) |                                                     | Yes              | 72/7.2     |
| 9       | CVE-2012-0507  | Oracle    | Java SE                      |                                                     | Yes              | 100/10     |
| 10      | CVE-2015-2426  | Microsoft | Windows (font driver)        |                                                     | Yes              | 100/9.3    |

---

## Email findings

### TOP BLOCKED ATTACHMENT FILE EXTENSIONS

Phishing emails are one of the most common ways adversaries compromise victims, and this has consistently been a top-ranked threat in Talos IR findings for years. In the last year alone, 25 percent of the initial access vectors identified in Talos IR engagements were comprised of phishing (this refers to chart 3b). This observation is consistent with U.S. government findings, with the FBI noting that phishing was the top incident reported to its Internet Crime Complaint Center (IC3) in 2022.

Threat actors commonly send unsolicited emails requesting users download or open an attachment to deliver malware. While file extension is not necessarily indicative of file type, actors frequently try to hide malware under well-known file extensions to appear less suspicious, so users are more likely to open them. For example, earlier this year, Japan’s Computer Emergency Response Team (JP-CERT) warned that adversaries were embedding malicious Word documents in PDF files to bypass detection, a strategy we have seen threat actors rely on for years.

Threat actors’ file type preference was also likely affected by Microsoft’s 2022 decision to block macros, which adversaries had heavily abused up to that point. With this change, actors have moved away from using Microsoft Office files like Word and Excel as frequently as they once did. In 2023, we saw the commodity loader Ursnif incorporate malicious PDF attachments into their phishing operations for the first time as this actor and other groups looked for ways to avoid relying on macros.

*   PDF: 36%
*   HTML: 14%
*   HTM: 8%
*   ZIP: 5%
*   DOCX: 5%
*   Other: 32%

---

### TOP INITIAL ACCESS VECTORS, ACCORDING TO TALOS IR

*   Exploit vulnerability in public-facing application: 28%
*   Unknown: 23%
*   Compromised credentials on valid accounts: 23%
*   Phishing: 19%
*   Drive-by compromise: 6%

*Note: Initial access vector is often hard to determine due to a variety of reasons — including insufficient logging or lack of visibility into the affected environment — resulting in “unknown” being highly represented.*

---

### TOP BRANDS SPOOFED IN SENDER NAMES

Cybercriminals and other malicious actors rely heavily on social engineering tactics to compromise users, which is why they commonly imitate well-known companies in their phishing emails. Commodity loaders like Emotet, Qakbot, and Trickbot, for instance, routinely use fake invoices, bank statements, or shipping notifications as phishing themes to feign legitimacy. This is reflected in our list of top spoofed brands, where we see that financial services entities and shipping services were among those that actors most frequently spoofed.

Business email compromise (BEC) operations also leverage spoofed company names to enhance legitimacy. BEC is a scam in which cybercriminals send emails to targets that appear to come from a known source making a legitimate request. The goal is to prompt the target to make unauthorized money transfers to the threat actor. Actors may impersonate well-known and trusted brands, like those represented in our list, to trick users. BEC has been on the rise in recent years, according to the FBI, and resulting in $2.7 billion in losses in 2022.

*   Bank of America
*   Walmart
*   Western Union
*   Banco Bradesco
*   Aeon
*   AT&T
*   American Express
*   Google
*   Capital One
*   DHL
*   DocuSign
*   Paypal
*   Royal Bank of Canada
*   American Airlines
*   FedEx

---

## Top MITRE ATT&CK techniques

Notably, nearly a third of the top 20 most common MITRE ATT&CK techniques fall under the defense evasion tactic, suggesting actors are devoting substantial resources to this phase of the attack chain. Techniques relating to privilege escalation and persistence also ranked high, highlighting their importance in the attack lifecycle.

*   **T1574, Hijack Execution Flow**: Hijack execution flow was the most common technique, appearing nearly twice as often as the next highest result. Hijacking execution flow refers to actors co-opting the way an operating system runs programs on a target endpoint. DLL side-loading is a common example of this, whereby actors essentially position their malware alongside the victim application so that when the program searches for its legitimate DLL, it also unwittingly executes the malicious payload. This is an effective way for actors to hide their activities under legitimate and trusted software, a technique we commonly see leveraged by APTs and cybercriminals.
*   **T1078, Valid Accounts**: The use of valid accounts was the second-most common technique we observed, underscoring adversaries’ reliance on compromised credentials and use of existing accounts. Actors use this technique to enable various stages of the attack chain. We commonly see commodity loaders deploying information-stealing malware for this very purpose. Relatedly, credentials from password stores ranked in the top five, further highlighting actors’ focus on obtaining user credentials. These findings are consistent with Talos IR data, which showed compromised credentials/valid accounts accounted for nearly a quarter of known initial access vectors in 2023.
*   **T1496, Resource Hijacking**: Resource hijacking, which ranked in the top 10, is a technique we typically see associated with the deployment of cryptocurrency mining malware, which hijacks an endpoint’s processing power for profitable gains. Cryptocurrency mining threats are highly common, as this is a low-level type of attack typically carried out by unsophisticated actors. We often see this type of malware deployed, especially soon after new vulnerabilities are disclosed, before victims have time to patch and/or in conjunction with other, more complex, malware.

---

# Ransomware and extortion

## Section highlights

*   Ransomware and pre-ransomware incidents continue to affect customers at a consistent rate — totaling the same 20 percent of Talos IR incidents as last year — with health care being the most targeted vertical.
*   For the second year in a row, LockBit was the most prolific ransomware-as-a-service (RaaS) gang, based on our findings, consistent with CISA’s assessment that it is the most deployed ransomware variant. LockBit was one of the most frequently observed ransomware threats in Talos IR this year, and affiliates accounted for more than 25 percent of the total number of victim posts on data leak sites across some 40 ransomware groups we monitor.
*   ALPHV, Clop, and BianLian also dominated the threat landscape, accounting for another quarter of all ransomware and/or data extortion compromises publicized on dark web actor sites.
*   We saw Clop affiliates consistently exploit zero-day vulnerabilities, a highly unusual tactic given the expertise, personnel, and access required to develop such exploits, suggesting the group possesses a level of sophistication and/or resources matched only by advanced persistent threats (APTs).
*   New ransomware variants are emerging that leverage leaked source code from other RaaS groups, allowing less skilled actors to enter this space. At the same time, we also see highly sophisticated operators like Clop leveraging zero-day vulnerabilities at an unprecedented pace, an interesting dichotomy demonstrating the breadth of actors in this space.
*   Actors are turning to data extortion more than ever, with this being the top threat that Talos IR responded to in Q2 2023 (April - June). Data theft extortion looks very similar to pre-ransomware activity, creating challenges for defenders.
*   Some actors are abandoning ransomware use altogether, opting for extortion instead, a trend likely influenced by ongoing law enforcement operations, better industry detections, and lower operational costs.

---

The ransomware space remained dynamic in 2023, with groups continuing to rebrand or merge, actors often working for multiple ransomware-as-a-service (RaaS) outfits at a time, and new groups continually emerging. The skill levels varied greatly as well, with experienced actors developing sophisticated exploits for zero-day vulnerabilities, while less-skilled actors relied on repurposed ransomware code to create their own threats. We also saw an emerging trend in this space, as more actors began to abandon the use of ransomware and resort to pure data theft extortion without encrypting files, presenting a new line of challenges for defenders. Despite these changes, one thing remains constant: Ransomware remains a top threat to entities worldwide.

## Ransomware attacks persist at steady pace

Ransomware and pre-ransomware made up 20 percent of the total incidents that Talos IR responded to this year, a very slight drop compared to last year. It can be difficult for defenders to determine what constitutes a pre-ransomware attack if a ransomware binary is never executed and encryption does not take place. However, there are some indications analysts use to assess if ransomware is the likely final objective, such as the use of adversary simulation frameworks like Cobalt Strike and/or credential-harvesting tools like Mimikatz, the targeting of certain critical assets such as backups, or enumeration and discovery techniques.

The health care and public health sector was the most targeted vertical in Talos IR ransomware and pre-ransomware engagements this year, compared to the education sector in 2022, as reported in last year’s Year in Review report (see Figure 1). Healthcare organizations are highly vulnerable to cyber attacks given their low downtime tolerance, often underfunded cybersecurity budgets, and possession of protected health information (PHI) that is valuable to threat actors. The COVID-19 pandemic likely exacerbated this situation in recent years, with healthcare providers strained from a resource perspective and downtime being even less tolerable.

## Old foes are top offenders as LockBit remains top threat

For a second year in a row, LockBit was the most active RaaS group, accounting for over 25 percent of the total number of posts made to data leak sites. LockBit, ALPHV, Clop, and BianLian accounted for nearly 50 percent of the total posts made to leak sites this year (Figure 2).

LockBit continued to conduct prolific ransomware operations in 2023, a finding that aligns with CISA’s assessment that it is the most deployed ransomware variant. LockBit attacks can be very impactful, affecting an organization’s information technology (IT) networks and operational technology (OT), the hardware and machines responsible for physical processes, as we have observed in Talos IR engagements. In October, CISA published guidance for securing OT environments, underscoring how significant the impact can be to these systems. LockBit was also deployed during the exploitation of two vulnerabilities in the PaperCut software, a print management solution widely used across entities in the government and education verticals, among others.

Posts made to the group’s data leak site ebbed and flowed throughout the year, with detections of LockBit activity appearing to spike in March, partially coinciding with LockBit’s deployment against vulnerable instances of the printer management software PaperCut, where it has remained consistently high (Figure 3).

---

## Ransomware space remains crowded with new and rebranded groups

Ransomware groups’ constant rebranding and/or turnover was a prominent trend this year. Multiple leaks of ransomware source code and builders — components essential to creating and modifying ransomware — have had a significant effect on the ransomware threat landscape. These leaks allow ransomware operators to rebrand or give unsophisticated actors the ability to generate their own ransomware more easily with little effort or knowledge. As more actors enter this space, Talos is seeing an increasing number of ransomware variants emerge leveraging leaked ransomware code, often leading to more frequent attacks and new challenges for cybersecurity professionals and defenders, particularly regarding actor attribution.

The volume of new ransomware variants based on leaked source code also highlights the speed at which actors take advantage of such public disclosures. Most recently, we observed a surge in new ransomware strains emerging from the Yashma ransomware builder. First appearing in May 2022, Yashma is a rebranded version of the Chaos ransomware builder (v5), which was leaked in April 2022. Since early 2023, we have seen several new Yashma strains emerge, including ANXZ and Sirattacker, likely deployed by smaller or groups of affiliates with fewer resources given their lack of widespread adoption and notoriety in the landscape. In April, we discovered a new ransomware actor, RA Group, deploying their ransomware variant based on the leaked Babuk source code. Since an alleged member of the Babuk group leaked the full source code of its ransomware in September 2021, several new variants based on the leaked code have emerged, with many appearing in 2023, including ESXiArgs, Rorschach, and RTM Locker.

While these changes in the threat landscape have largely benefitted affiliates, security researchers and defenders also have an advantage with access to the leaked code. It allows security researchers to analyze the source code and understand the attacker’s TTPs and develop effective detection rules, potentially aid in the creation of decryptors and enhance security products’ capabilities in combating ransomware threats.

---

## Affiliates turning to data theft extortion over ransomware deployment

Even with the expanding number of RaaS options, some have found success in extorting funds without deploying ransomware. In these extortion instances, an adversary steals the victim’s data but does not encrypt it. The common double extortion tactic is thereby eliminated, with the actor relying solely on the threat of leaking the information rather than also demanding payment to unlock the files. This trend is also reflected in Talos IR engagements, where extortion was the most observed threat in Q2 2023, accounting for almost a third of threats seen, a 25 percent increase from the prior quarter (January-April) (Figure 4).

Several well-known ransomware gangs — including Babuk, BianLian, and Clop — have opted for data theft extortion over ransomware, a departure from the groups’ typical ransomware attack chain (Figure 5).

Several factors have likely contributed to some threat actors’ preferences for data theft extortion instead of deploying ransomware. U.S. and international law enforcement have aggressively pursued ransomware actors in recent years, conducting major disruptions against well-known groups. Advancements in endpoint detection and response (EDR) capabilities have likely been a significant obstacle for threat actors seeking to deploy ransomware and encrypt data. Adversaries appear to consider the technique a viable way to receive a payout, demonstrating how ransomware actors are constantly working around advancements in EDR, law enforcement operations, and other barriers.

While extortion has proven to be a serious and effective threat, it has not yet outpaced the ransomware threat that has been a challenge for organizations and defenders for the past several years. We are continuing to monitor the long-term effects of this trend.

---

## Some ransomware groups consistently leverage zero-days, often affecting multiple organizations

While many inexperienced adversaries relied on code reuse this year, we also continued to see highly sophisticated operators exploiting zero-day vulnerabilities at an unprecedented pace, highlighting the broad technical diversity of actors and TTPs in this space. Ransomware actors, well-known for being opportunistic, are quick to exploit flaws when made public. When Clop, a high-profile ransomware and data extortion group, claims public responsibility for exploiting a zero-day vulnerability, additional ransomware affiliates quickly follow suit, scanning for affected systems before patches are issued (Figure 6).

In April, shortly after print management software company PaperCut became aware of unpatched servers being exploited in the wild by Clop, other ransomware groups began to exploit the critical remote code execution (RCE) vulnerability (CVE-2023-27350) as part of their attack chain. This highlights the widespread nature of this activity and ransomware operators’ strategy, often based on the disclosure of other groups leveraging high-profile security flaws to increase chances of eliciting payouts from victims.

Clop’s repeated efforts to exploit zero-day vulnerabilities is highly unusual for a ransomware group given the resources required to develop such capabilities. We saw many instances of this in 2023, beginning in January, when the Clop ransomware group launched a campaign leveraging a zero-day vulnerability (CVE-2023-0669) to target the GoAnywhere MFT platform. In May, Clop claimed responsibility for attacks involving another zero-day flaw (CVE-2023-34362) affecting Progress Software’s file transfer solution, MOVEit Transfer. These attacks also demonstrate Clop’s expanded toolkit, as the operators deployed a previously unseen web shell, dubbed LemurLoot, to exfiltrate victims’ data and extort payments on systems running MOVEit.

The vulnerabilities leveraged by ransomware affiliates/groups highlighted above all received high- or critical-severity CVSS scores, were found to be easily exploitable by Cisco Kenna, and were included in CISA’s Known Exploited Vulnerabilities catalog.

Given the resources required to develop or identify such exploits, it is possible that Clop, and/or certain members, possess a level of sophistication and funding matched only by APTs. There is no known chatter on underground forums about how Clop may have obtained these exploits, though we assess the group may have access to a sophisticated developer that appears to be focusing on identifying vulnerabilities in third-party file management systems and other network peripherals.

---

## Landscape shifts in the RaaS space due to law enforcement disruptions

Ransomware groups experienced disruptions, forcing them to adapt and/or join other RaaS outfits. In January 2023, the U.S. Justice Department announced it had disrupted the Hive ransomware group. By late January, we saw this reflected in our data, with a general dropoff in posts made to Hive’s data leak site (Figure 7).

When ransomware infrastructure gets disrupted, operators often continue their work with other groups, creating a whack-a-mole scenario for law enforcement and network defenders. For example, when Hive’s infrastructure was disrupted, many former Hive members attempted to join other ransomware groups within days of the disruption, according to our sources. This greater democratization, with an influx of new groups leveraging code from the same ransomware builders, introduces complexities for defenders attributing activity to specific groups as TTPs remain consistent across groups.

---

# Network infrastructure

## Section highlights

*   Advanced actors are attacking networking devices at a concerning rate this year, particularly China and Russia-based groups looking to advance espionage objectives and facilitate stealthy operations against secondary targets.
*   Other cybercriminals are starting to follow suit, adopting this technique to sell unauthorized access to these devices on the dark web or pivot into targeted networks and deploy ransomware.
*   Actors take advantage of security weaknesses, such as default credentials and unpatched vulnerabilities, to gain initial access to the targeted device.
*   Three of the five most targeted device vulnerabilities in this space are critical or severe, and exploitation can, in some instances, lead to full device takeover. This could provide adversaries unfettered access to core components of a target’s network and security perimeter.
*   Exploitation attempts against vulnerabilities in this space typically remained consistent throughout 2023 with occasional spikes after the vulnerabilities’ public disclosure. This suggests that targeted organizations are often failing to patch their devices in a timely manner, and actors therefore continue to see value in exploiting CVEs, even as they age.
*   To remain hidden post-compromise and establish additional methods of access without raising alarm bells, actors take steps to weaken defenses within the environment and will even introduce new vulnerabilities to exploit.
*   Talos is helping to combat this threat by supporting the Network Resilience Coalition, a group of industry leaders from network equipment vendors, network operators, and security companies that focuses on securing critical data networks.

---

Talos observed an increase in sophisticated attacks on networking devices this past year, particularly by state-sponsored actors seeking to advance espionage objectives and facilitate stealthy operations. Our investigations have largely involved threat groups affiliated with Russia and the People’s Republic of China (PRC), though it is reasonable to assume any sufficiently capable APT is, or will be, developing the capability to target network infrastructure as the success of these attacks garners increased attention. We have also recently observed targeting activity from other cybercriminals, including initial access brokers and ransomware actors seeking to profit off unauthorized access to targeted devices.

Networking equipment is an attractive target for malicious cyber actors due to the large attack surface it presents and potential access to a victim network it can offer. Though these devices are key components of an organization’s IT infrastructure and often conduits of sensitive network traffic, they are infrequently examined from a security perspective and typically poorly patched. Further, they often do not run on standard operating systems, but rather custom firmware unique to the vendor, meaning they cannot be protected or monitored with standard, one-size-fits-all security solutions. The dichotomy of high value and weak security in these devices makes them a prime target for exploitation. Because of the large presence of Cisco network infrastructure around the world, we are well-positioned to investigate and report on top-tier attackers and their campaigns.

---

## Weak security often exploited for initial access

We have seen malicious actors predominantly gain initial access to networking devices by exploiting unpatched vulnerabilities, weak or default credentials, or insecure device configurations. While security professionals may not be able to implement standard EDR solutions on networking devices as referenced above, this observation demonstrates that an organization’s defenses against this threat can be greatly improved simply through routine patching, enhanced monitoring, and improved credential management. Once initial access is obtained, threat actors will typically take further advantage of the device’s limited security by destroying evidence of an intrusion, such as wiping or disabling logs.

---

## Exploitation of vulnerabilities spike after public disclosure

Over the last year, exploitation activity against vulnerabilities in network devices typically remained consistent, though sometimes spiked following public disclosure, based on our telemetry. A spike in exploitation attempts could be due to several factors, such as a singular and very large campaign conducted by an advanced threat actor, or widespread targeting activity that was suddenly impeded by highly publicized reporting and recommendations to patch. Comparatively, the consistent targeting levels in the months after disclosure suggests affected organizations are failing to patch their devices in a timely manner and actors therefore continue to see value in exploiting these older vulnerabilities even as they age.

For example, detections for Snort IDs (SIDs) 60726 and 60725, which alert on attempts to exploit the aforementioned Fortinet vulnerability (CVE-2022-40684), spiked right after the security flaw was disclosed in mid-October 2022, then significantly lowered to a consistent level in early 2023 (Figure 8). In comparison, attempts against vulnerable Zyxel devices (CVE-2023-28771; SID 6185) began in mid-May 2023, shortly after the CVE was publicized in April, and remained relatively level for months afterward.

---

## Top vulnerabilities targeted are highly critical, easily exploitable and widespread

The vulnerabilities affecting network devices that were most frequently targeted in 2023 have high severity scores, meaning they are easily exploitable and can cause significant operational impact. Of the five most targeted vulnerabilities in this space, three have a CVSS score of 9.8 or 10, scores that are reserved for only a small number of the most serious CVEs. Exploitation of critical and severe security flaws in network devices can, in some instances, lead to full device takeover, allowing adversaries unfettered access to core components of a target’s network and security perimeter.

Furthermore, many of the affected devices are widely used by enterprises and governments globally, further exacerbating the potential impact and scope of successful compromise. Threat actors may uncover thousands of vulnerable devices when conducting mass scanning after flaws are disclosed and can often find publicly available exploits as well.

Finally, the variety of vendors represented in the list below demonstrates how universal this issue is for device providers. This is further supported by Russian intelligence contracting documents, also known as the Vulkan Files, that Talos obtained samples of this past year. These documents showed that any network device brand was vulnerable to targeting, with one scanning component targeting almost 20 different router and switch manufacturers.

Most of the CVEs listed below are also included in CISA’s lists of vulnerabilities that are commonly targeted and/or have known exploitation. Our top two vulnerabilities were also included in a CISA advisory