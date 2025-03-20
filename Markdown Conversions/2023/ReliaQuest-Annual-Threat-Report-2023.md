# ReliaQuest Annual Cyber-Threat Report 2023

**Make Security Possible**

## Table of Contents
- [Executive Summary](#executive-summary)
- [The Evolving Cyber Threat Landscape: Understanding the Current Risks](#the-evolving-cyber-threat-landscape-understanding-the-current-risks)
- [What Our Data Revealed](#what-our-data-revealed)
  - [Active Months and Targeted Sectors](#active-months-and-targeted-sectors)
  - [Most Common Kill Chain Phases](#most-common-kill-chain-phases)
  - [Most Commonly Detected Techniques](#most-commonly-detected-techniques)
- [GreyMatter Digital Risk Protection (GMDRP) Alert Trends](#greymatter-digital-risk-protection-gmdrp-alert-trends)
  - [Most Common GMDRP Risk Alerts](#most-common-gmdrp-risk-alerts)
  - [Alerts via Sector](#alerts-via-sector)
  - [What Steps Should Defenders Take Now?](#what-steps-should-defenders-take-now)
- [Initial Access Broker (IAB) Trends](#initial-access-broker-iab-trends)
  - [Most Common Access Types](#most-common-access-types)
  - [Most Commonly Targeted Countries](#most-commonly-targeted-countries)
  - [Most Commonly Targeted Sectors](#most-commonly-targeted-sectors)
  - [Case Study: Exotic Lily](#case-study-exotic-lily)
- [Initial Access Malware](#initial-access-malware)
  - [QakBot](#qakbot)
  - [Emotet](#emotet)
  - [GootLoader](#gootloader)
  - [IcedID](#icedid)
  - [SocGholish Malware Distribution Framework](#socgholish-malware-distribution-framework)
  - [What Steps Can Defenders Take Now?](#what-steps-can-defenders-take-now-1)
- [Vulnerability Intelligence](#vulnerability-intelligence)
  - [Where the Risks Lie](#where-the-risks-lie)
  - [Risk Calculation](#risk-calculation)
  - [Vulnerabilities Deep Dive](#vulnerabilities-deep-dive)
    - [Spring4Shell RCE Vulnerability](#spring4shell-rce-vulnerability)
    - [Log4Shell Vulnerability](#log4shell-vulnerability)
    - [Oracle EBS Vulnerability](#oracle-ebs-vulnerability)
    - [Fortinet Authentication Bypass Vulnerability](#fortinet-authentication-bypass-vulnerability)
  - [What Steps Can Defenders Take Now?](#what-steps-can-defenders-take-now-2)
- [Ransomware Intelligence](#ransomware-intelligence)
  - [Ransomware Attack Kill Chain](#ransomware-attack-kill-chain)
  - [Most Targeted Sectors](#most-targeted-sectors-1)
  - [Most Active Ransomware Groups](#most-active-ransomware-groups)
  - [Case Study: LockBit](#case-study-lockbit)
  - [What Steps Can Defenders Take Now?](#what-steps-can-defenders-take-now-3)
- [Cobalt Strike Ransomware Intelligence](#cobalt-strike-ransomware-intelligence)
  - [What Our Data Tells Us?](#what-our-data-tells-us)
  - [What Steps Can Defenders Take Now?](#what-steps-can-defenders-take-now-4)
- [Conclusion](#conclusion)

---

## Executive Summary

This report offers an in-depth and inclusive view of the cyber-threat landscape, over what has been an exceptionally challenging 12 months for cyber security professionals (1 February 2022 to 1 February 2023). Over the course of this period, the ReliaQuest Threat Research Team has identified trends across several data sources and analyzed them to provide readers with insights into cyber-threat trends and observations. During a reporting period that saw Russia’s invasion of Ukraine, a continued risk of ransomware attacks and data extortion, and an avalanche of high-risk vulnerabilities, we identified the following key events and patterns:

-   The attempted exploitation of exposed remote services was the most commonly detected attack technique. Those services, including virtual private networks (VPNs) and remote desktop protocol (RDP), pose a very high risk. A wide range of attackers, including cybercriminals and nation-state–aligned groups, have exploited them to access a network or establish persistence on it.
-   ReliaQuest identified wide use of defense evasion techniques, notably indicator removal, data destruction, and the sub-technique of clear command history. This emphasizes the significant efforts threat actors place on obfuscating their activity.
-   ReliaQuest’s GreyMatter Digital Risk Protection (GMDRP) service yielded data that identified especially vulnerable sectors. They are most susceptible to: fraud via impersonating retail web domains, significant risk from exposed credentials (particularly for financial services), and exploitation of open ports at utilities companies.
-   CVE-2022-22965 (aka Spring4Shell) is regarded to pose the greatest risk of all high-risk vulnerabilities, for its available and easy exploits and its potential to cause a technical and business impact.
-   The most common access type advertised by initial access brokers (IABs) was RDP, which accounted for 24.4% of all ReliaQuest “tippers” published in the reporting period.  RDP access was also the costliest type being offered, with an average median price of approximately $1,000.
-   Initial-access malware continued to be delivered mainly by phishing emails. Threat actors adapted their techniques to circumvent organizational controls, and in ReliaQuest customer environments, we detected many instances of the “Emotet,” “SocGholish,” “IcedID,” “GootLoader,” and “Bumblebee” malware.
-   “LockBit” was, overwhelmingly, the most active ransomware group, and is increasingly using the SocGholish malware distribution framework to gain initial access to networks which is making their efforts more potent. We anticipate even more use of SocGholish by ransomware groups during 2023.
-   NameCheap was the most common registrar of Cobalt Strike team servers, followed by Ename Technology and MarkMonitor. These registrars are primarily content delivery networks (CDNs) used for domain fronting. Domain fronting is used to conceal user traffic and is commonly used by threat actors for command and control (C2) purposes.

**What’s in the Report?**

In this first ReliaQuest Annual Cyber-threat Report, we cover activity observed from 1 February 2022 to 1 February 2023:

-   Trends in events recorded in GreyMatter
-   The most commonly found risk types on GMDRP
-   Trends related to initial access brokers (IABs): the cybercriminal gatekeepers that enable a raft of malicious activity
-   An introduction to vulnerability intelligence, highlighting the “red-flag” flaws in platforms that ReliaQuest customers use most
-   Trends related to ransomware, including a breakdown of the most commonly targeted sectors and regions
-   Trends related to Cobalt Strike and command-and-control (C2) systems used by ransomware operators

## The Evolving Cyber Threat Landscape: Understanding the Current Risks

The cyber threat landscape is increasingly complex and subject to consistent change. The rapid advancement of technology and reliance on digital systems leave individuals and organizations facing an array of cyber threats. While cybercriminals and nation-state aligned threats use varying techniques, there are consistent observable trends that are used by many of these groups. Taking a deep dive into these trends by collating and analyzing data sources across our customer environments, allowed us to identify several insights into the state of the current cyber threat landscape.

Our report starts by looking at observations on active times of the year, most commonly observed kill chain phases and attacker techniques, before moving onto insights into a typical attack lifecycle. This involves the identification and exploitation of security weaknesses by an IAB, vulnerability exploitation, before moving to a network compromise by a ransomware actor. We conclude the report by identifying trends related to Cobalt Strike usage, which remains one of the most common methods of facilitating C2 over a compromised network, often used by ransomware actors.

As our CEO Brian Murphy has previously stated, cybersecurity likely represents the greatest technical challenge of our generation. By taking a retrospective look at the data from the previous year, we aim to enable our customers to take the best stance on preventing the cyber threats of 2023.

## What Our Data Revealed

The data for this analysis was extracted from customer incidents collated by ReliaQuest. The data set covers February 1, 2022, 00:00:00 UTC to February 1, 2023, 00:00:00 UTC (12 months). There were 35,024 true-positive incidents during that reporting period.

### Active Months and Targeted Sectors

![Image description: Number of true-positive tracked incidents per month]
*Figure 1: Number of true-positive tracked incidents per month*

Figure 1 shows a steady increase in true positives[^1], notably between August 2022 and January 2023, but with a noticeable drop-off in December 2023—potentially because threat actors were less active over the end-of-year festive holiday season.

[^1]: A True Positive or Confirmed Incident is an event or alert which identified malicious activity that resulted in  either an attempt or successful unauthorized access, use, modification, or destruction of any information system or data.

![Image description: Average number of incidents per customer sector]
*Figure 2: Average number of incidents per customer sector*

The number in front of each Figure 2 sector shows how many incidents, on average, any given client in that sector can expect to see over the course of a year. We calculated it by dividing the number of incidents affecting that sector (the number at the end of each teal bar) by the number of GreyMatter customers operating in that sector. The red line indicates the average number of incidents all customers can expect to see over a year: 71. For that we divided the total number of GreyMatter incidents for all customers by the total number of customers. If a sector has the red line going through the grey bar, that  sector has more incidents than average. Construction had the most during this reporting period, followed by transportation, then wholesale trade.

The perceived lack of cybersecurity maturity, controls, and tools paired with the significant impacts of outages is likely to have placed the Construction, Transportation, and Wholesale Trade sectors in the cross-hairs of threat actors.

Each of these sectors are increasingly relying on IT to drive efficiencies making them susceptible to cyber attacks.

### Most Common Kill Chain Phases

![Image description: Kill chain phases detected in incidents, ranked by prevalence]
*Figure 3: Kill chain phases detected in incidents, ranked by prevalence*

Figure 3 highlights the most commonly detected kill-chain phases, identified through incident data. You can see the efficiency of GreyMatter in identifying malicious activity in the early stages of an attack lifecycle (e.g., initial access and reconnaissance), before an attacker has time to progress their intrusion or establish persistence on a targeted network. ReliaQuest focuses heavily on detection, and ensuring customers are in the best possible position to respond in the early stages of threat actor activity.

### Most Commonly Detected Techniques

![Image description: Top 10 most detected techniques]
*Figure 4: Top 10 most detected techniques*
Taken from our collection of true positive incident data was the most commonly observed attacker techniques, detailing methods identified by ReliaQuest as part of investigations on customer environments. Figure 4 above highlights the top 10 of these techniques, including T1133 External Remotes Services which was overwhelmingly the most commonly seen technique. This comes as no surprise; exposed remote services, including VPN, Citrix, TeamViewer or RDP, represent one of the most common methods of enabling initial access onto a targeted network, or establishing persistence. We have observed significant threat actor interest in identifying exposed RDP servers, which has resulted in a flourishing ecosystem of cybercriminal activity in identifying, exploiting, then selling RDP accesses onto interested third parties; we go into more detail on these accesses in our section related to initial access broker (IAB) activity later in this paper.

Also represented within the top ten techniques was T1070 Indicator Removal and T1485 Data Destruction, which were the 8th and 10th most observed respectively. Indicator Removal refers to the attempt from adversaries to delete or modify artifacts generated within systems, to remove evidence of their actions on objective and hinder investigative efforts.  Data destruction refers to adversary attempts to destroy data and files on specific systems or in large numbers on a network to interrupt availability to systems, services, and network resources. We found these techniques notable in particular due to the implications they have on defenders. To deny Defense Evasion and Impact techniques, organizations should prioritize technical controls and ensure sufficient monitoring is in place to identify suspicious activity. As we move on to the top sub-techniques identified in our data set, we also see sub-techniques that map back to the Defense Evasion tactic which again reiterates our previous stance. The top 10 most commonly observed can be seen in Figure 5.

![Image description: Top 10 most commonly observed sub-techniques]
*Figure 5: Top 10 most commonly observed sub-techniques*

Within the top 10 sub-techniques in the 8th spot is T1070.003 Clear Command History, which involves an adversary attempting to clear the command history of a compromised account, in an attempt to conceal the actions undertaken during an intrusion. This emphasizes the importance of detecting suspicious activity early in the attack lifecycle before a threat actor has a chance to establish persistence on your network; with capable threat actors it’s often extremely difficult to fully remove their presence if they have developed several methods of gaining access.

The most commonly observed sub technique was T1595.003 Word List Scanning. This refers to threat actor attempts to iteratively probe infrastructure using brute-forcing and crawling techniques. While this technique employs similar methods to brute force techniques, its goal is the identification of content and infrastructure rather than the discovery of valid credentials. Word lists used in these scans may contain generic, commonly used names and file extensions or terms, that are specific to a particular software. Adversaries may also create custom, target-specific wordlists using data gathered from other reconnaissance techniques. The best method of minimizing the risk from Wordlist scans is ensuring services are not unnecessarily exposed to the internet, i.e., make sure your systems, resources, and infrastructure are not exposed externally unless they have a specific business requirement.

## GreyMatter Digital Risk Protection (GMDRP) Alert Trends:

Known as GreyMatter Digital Risk Protection (GMDRP) ReliaQuest customers can receive intelligence, risks, and alerts that enable security operations to make informed decisions about threats to their environments. This capability also enhances visibility of previously unknown threats, by enriching incidents with actionable intel, reducing the number of false positives, and driving faster business outcomes.

By continually monitoring open, deep, and dark web sources to isolate legitimate threats and provide quick and easy remediation, it provides a unique view of security threats outside an organization. If a risk is detected, GMDRP customers receive context-rich alerts with clear response steps via the GreyMatter alert process and workflow. This includes  alert-assignment, automated-action, and mitigation recommendations. For more information on GMDRP, see our solutions brief.

GMDRP covers 40 unique risk types that affected most sectors during the reporting period. They include credential exposure, impersonating domains and phishing sites, leaked documents, and exposed code. The data for this section was extracted from all the alerts provided to ReliaQuest customers in GMDRP from February 1, 2022, 00:00:00 UTC to February 1, 2023, 00:00:00 UTC (12 months).

### Most Common GMDRP Risk Alerts

Figure 6 shows the top 20 most common risk types escalated to ReliaQuest GMDRP customers. This intelligence can be used to consider how the types of risk are managed across your business

![Image description: Most common risk types, by thousands of GMDRP alerts]
*Figure 6: Most common risk types, by thousands of GMDRP alerts*

The most common was, overwhelmingly, credential exposure—unsurprising, given the abundance of third-party breaches, risky user practices, and insufficient controls over managing credentials. In recent blogs we have commonly referred to the huge problem of credential exposure, which continues to fuel a host of cyber threats. Stolen credentials are the most common method of gaining initial access to networks. According to the 2022 Verizon Data Breach Investigations Report, stolen credentials enabled initial access in over 50% of 20,000 analyzed incidents.

The next most-common alert was for a detection of an exposed marked document. This can be documents with protective markings or data loss prevention (DLP) identifiers, but also technical and commercial documents (e.g., security assessments, product designs, legal documents, payroll data), which are often unmarked. Exactly why such sensitive documents get breached so often probably depends on the targeted organization, but most likely it is facilitated by a combination of risky user practices and insufficient data-loss prevention policies and controls.

The third and fourth most-commonly represented asset types were impersonating domains and impersonating subdomains. These are registered domains masquerading as a client’s brand, company name, or domain, typically using typo-squatting and combosquatting. This is not a new issue, nor will it surprise anyone to see it represented so highly on our most commonly triggered alerts list. Domain impersonation occurs because it continues to work and many companies struggle to understand how they can detect such infringements and quickly take the sites down.

Other reasons for the explosion of fake domains include the sheer number of top-level domains (TLDs) that go beyond the usual .com, .net, and .org. Try to register a domain, and you’ll be presented with probably dozens of options with various spellings and TLDs; it’s this variety that is being exploited to trick internet users.

Another factor is the low barrier of entry to the world of cybercrime. The criminal underground has responded to novice threat actors’ demand for registering and hosting domains, setting up phishing services or professionally-spoofed pages on a large scale, and lots of niche tools that support these enterprises; if you need it, someone will probably sell it to you, or even share it for free. There are also many tutorials and advice to aid fraud on the web—and they do not require substantial resources, whether technical or financial.

### Alerts via Sector

As part of our analysis of the GMDRP data, we also determined which ReliaQuest customer sectors received the most alerts, divided by the total number of current customers. The output of this can be seen below in Figure 7, highlighting the top 10 with the highest number. (So, remember, the results reflect only specific companies/sectors making up ReliaQuest’s customer base.)

![Image description: Ten ReliaQuest-customer sectors that received the most alerts, divided by total number of clients]
*Figure 7: Ten ReliaQuest-customer sectors that received the most alerts, divided by total number of clients*

Table 1 cross-references those ten sectors with the ten most common risk types. We divided the total number of alerts by the total number of ReliaQuest customers in each sector, to give a more accurate representation of the exposure to each risk type. From this table we can see which risks are most pertinent for specific sectors.

| Risk Type                 | Finance and Insurance | Professional, Scientific, and Technical Services | Health Care and Social Assistance | Retail Trade | Information | Accommodation and Food Services | Wholesale Trade | Manufacturing | Mining, Quarrying, and Oil and Gas | Public Administration |
| :------------------------ | :-------------------- | :------------------------------------------------ | :--------------------------------- | :----------- | :---------- | :------------------------------ | :-------------- | :------------ | :--------------------------------- | :------------------- |
| CREDENTIAL EXPOSURE       | 501.14                | 353.25                                            | 235.48                             | 859.43       | 38949.24    | 108.19                          | 590.47          | 883.08        | 88.64                              | 178                  |
| MARKED DOCUMENT           | 331.37                | 789.32                                            | 8.48                               | 456.48       | 77.67       | 17.12                           | 1031.67         | 612.54        | 2.09                               | 26.36                |
| IMPERSONATING DOMAIN      | 220.53                | 192.61                                            | 72.1                               | 795.1        | 385.62      | 216.38                          | 322.93          | 364.31        | 152.73                             | 61.73                |
| IMPERSONATING SUBDOMAIN   | 71.63                 | 271.12                                            | 17.56                              | 99.05        | 445.52      | 31.19                           | 214.2           | 500.38        | 24.91                              | 71.18                |
| EXPIRED CERTIFICATE       | 58.12                 | 34.24                                             | 28.44                              | 60.71        | 215.1       | 89.81                           | 40.6            | 64.54         | 138.64                             | 17.55                |
| OPEN PORT                 | 35.95                 | 113.39                                            | 34.08                              | 65.81        | 2812.43     | 272.31                          | 125.6           | 291.38        | 81                                 | 13.64                |
| EVIDENCE OF CREDENTIAL ACCESS | 18.92                 | 63.12                                             | 6.75                               | 201          | 288.14      | 278.88                          | 20.87           | 64.69         | 5.64                               | 12.64                |
| IMPERSONATING MOBILE APP  | 18.54                 | 33.68                                             | 11.06                              | 95.52        | 243.57      | 113.62                          | 212.67          | 139.54        | 79.64                              | 44.09                |
| UNAUTHORIZED CODE COMMIT  | 13.9                  | 84.17                                             | 5.73                               | 56.33        | 84.9        | 31.38                           | 50.87           | 92.92         | 20.45                              | 39.27                |
| WEAK CERTIFICATE          | 9.22                  | 50.4                                              | 4.1                                | 16           | 211.76      | 16.38                           | 14.13           | 15.15         | 75.55                              | 3.73                 |

*Table 1: Ten most common risk types per sector, by number of GMDRP alerts*

The first data point that stands out is the abundant credentials of financial and insurance companies being exposed. The surface reason is obvious: access to credentials for financial services are a high priority for financially motivated cybercriminals. But the appeal is likely compounded by a lack of authentication practices; a recent study found that only 32% of financial service companies authenticate account logins with additional measures, such as two-factor authentication (2FA). For financial services, the level of risk is determined by the sufficiency of controls and the motive of a threat actor eyeing up accounts.

Open port exposures were also very common in the information sector, which includes telecommunication companies. This alert type relates to risky ports that have been left open on client domains or IP addresses. Ports are typically a security risk if the services running on them are misconfigured, unpatched, or otherwise vulnerable. Threat actors can easily identify unnecessarily exposed ports, which often can identify exploitable services.

For interested threat actors, there are several guides to scanning and exploiting exposed ports. The one quoted in Figure 8 highlights common mistakes companies make with ports, including insufficient authentication or misconfiguration of file transfer protocol (FTP) servers.

>During the reporting period (February 1, 2022 to February 1, 2023, ReliaQuest identified 231,150 impersonating domains and 162,895 impersonating subdomains.

![Image description: Excerpt of a port-scanning guide shared on a cybercriminal forum]
*Figure 8: Excerpt of a port-scanning guide shared on a cybercriminal forum*

Some ports should only be exposed internally; a good example is the infamous Port 445, which is used for Microsoft Directory Services for Active Directory (AD) and for the Server Message Block (SMB) protocol over TCP/IP. This port has been exploited over the years, notably with the use of the “WannaCry” ransomware and similar SMB exploits. It is not totally clear why telecommunications would be so susceptible to exposed ports, but it is realistically possible that many exposures are linked to the necessity for communication, plus the likelihood that telecommunications companies will have wider ranges of IP addresses to manage.

Another detail that won’t shock most readers is the number of impersonating domains targeting retail and trade sector companies. These domains can easily be created, often through dedicated phishing kits that are widely available on cybercriminal forums. We found several examples, including the kit referenced in Figure 9, aimed at spoofing Google and available to rent for $2,000 per month. That kit was advertised on a high-profile Russian-language cybercriminal forum, and offers the ability to clone Google accounts, steal browser information, and reportedly bypass 2FA.

Retail domains might be spoofed to steal accounts or financial information—which then can be used to commit fraud, drop malware, or sell access on to third parties. Domain impersonation can have a devastating impact. If used as part of a social engineering campaign (such as involving business email compromise or BEC), financial losses could be huge. There are also fake domains that are used to trick users into downloading malware, or harvesting credentials; this is the most common reason.

>Domains targeting retail and trade sector companies can easily be created, often through dedicated phishing kits that are widely available on cybercriminal forums.

![Image description: Forum advertisement of a phishing kit dedicated to spoofing Google]
*Figure 9: Forum advertisement of a phishing kit dedicated to spoofing Google*

### What Steps Should Defenders Take Now?

Based on the observations, we recommend taking certain steps to manage your external exposures.

-   In order to minimize Defence Evasion and Impact techniques, organizations should ensure sufficient monitoring is in place to identify suspicious or abnormal activity. This activity could be unusual login attempts, changes to system configurations or permissions, or attempts to delete files.
-   Credential exposure inevitably affects every company, to some extent. The risk can be managed best through a four-step program: Identify breached credentials, validate that the credentials are current, contain the credentials usage, and educate the credential’s user. For more information, why not navigate to our blog on credential exposure?
-   Exposed ports are a tricky business to manage; every organization is different, in terms of operational requirements and risk appetite. To manage the risk, first enumerate and document which services are publicly accessible from the internet. Perform a risk assessment; which services needs to be publicly accessible? (Close those that do not.)
-   Limiting access to specific ports can also be an interim solution if they cannot be closed entirely. Restricting access to only the IP addresses or range used by your administrators and relevant systems (using the service on that port) will minimize the risk profile for the environment.
-   Vulnerability management teams should prioritize vulnerabilities that have known exploits, if they are relevant to systems exposed to the network.
-   For domain impersonation risk, visibility is key. Ensure that registered domains, branding information, IP address ranges, and other assets are all sufficiently monitored for suspicious activity. This will help ensure that any domains spoofing your brand—potentially through typo-squatting or use of an incorrect TLD—can be quickly identified and remediated based on the risk they pose. This risk can be tracked over time, enabling security teams to act quickly and proportionately to submit domain takedown requests or mitigate otherwise. Monitoring for domain impersonation can be achieved through ReliaQuest GMDRP.

## Initial Access Broker (IAB) Trends

IABs give ransomware operators the tools to compromise a wealth of victims. A symbol of cybercrime professionalization, these brokers act as the “middlemen” in cyber threat operations: finding vulnerable organizations, exploiting them to access their systems, then selling that access to the highest bidder on dark-web forums. Their rise in popularity has aligned with the trend of ever-lower barriers to enter the world of cybercrime, which is also aided by the rise and spread  of commodity malware and cybercriminal affiliate memberships.

Our monitoring of IABs dates back to 2014, when the sale of access to systems first began making ripples in the cybercriminal underground. IAB activity has been synonymous with the consistent threat posed by ransomware activity, and IABs often work directly with ransomware groups to identify susceptible networks for exploitation.

Our breakdown of IAB activity during the reporting period can be seen in Figure 10, taken from analysis of IAB “tipper” intelligence update reports provided to ReliaQuest customers. Each week, the Threat Research Team manually collects posts advertising initial access to compromised systems from select high-profile Russian-language forums, publishing the intelligence the threat actor provides about the victim as a tipper in GreyMatter Intel. We prioritize listings that contain the most intelligence about a victim (e.g., targeted sector or region) and that align with our priority intelligence requirements, client interests, and corporate strategy.

### Most Common Access Types

The most common access type listed by IABs was RDP, which accounted for 24.4% of all tippers released  during the reporting period. This was followed by VPN-RDP—representing VPN access to the RDP dedicated server of the victim—and VPN access. There was a significant difference among median prices of access types; the highest was $1,000, for RDP access. The greatest interquartile range was $2,700 for RDP access; the interquartile range refers to the middle 50% of the distribution. The average for VPN access was $500.

![Image description: Most common IAB access types listed for sale, and price ranges from 01 Feb 2022 – 01 Feb 2023]
*Figure 10: Most common IAB access types listed for sale, and price ranges from 01 Feb 2022 – 01 Feb 2023*

RDP accesses being the type most sold and sought comes as no surprise. RDP applications remain favorites of IABs, given the relative ease with which they enable compromise through default or stolen passwords obtained via brute-force attacks. Despite significant research identifying unsecured RDP as one of the biggest threats facing business, organizations are failing to sufficiently secure their devices. Weak credentials often grant access, enabling threat actors  to compromise these applications easily and drive more malicious activity.

Automated vending cart (AVC) websites, like Russian Market, have thrived in the ecosystem of stolen RDP credentials. Russian Market offers a one-stop shop for cybercriminals wishing to purchase RDP access and a range of other  assets/services, including stolen card verification values (CVV), credit card dumps, account credentials extracted  from malware stealer logs, and other illegally sourced items.

That AVC site offers easy-to-use search and filter functions to navigate the sections and tailor results to required needs. However, that functionality is only accessible to users who have deposited funds to their Russian Market account—an increasingly common tactic for AVC sites to encourage users to show intent to access and use the site. Russian Market is available on both the clear and dark web, and appears to be growing in popularity, although competing platforms are beginning to emerge.

![Image description: AVC site Russian Market sells compromised RDP credentials]
*Figure 11: AVC site Russian Market sells compromised RDP credentials*

### Most Commonly Targeted Countries

The most commonly targeted country for IAB activity was overwhelmingly the US. This is unlikely to change in the long-term future (over one year), as cybercriminals frequently perceive US-based companies as offering large financial rewards, and spur other threat actors for political reasons. Some cybercriminals opportunistically target whatever entity can provide a profit, but for others, the US is still seen as the traditional enemy, and, for Russian-speaking cybercriminals, former Commonwealth of Independent States countries should not be targeted.

![Image description: Countries most commonly targeted by IAB activity between 01 Feb 2022 – 01 Feb 2023]
*Figure 12: Countries most commonly targeted by IAB activity between 01 Feb 2022 – 01 Feb 2023*

>Cybercriminals frequently perceive US-based companies as offering large financial rewards, and spur other threat actors for political reasons.

### Most Commonly Targeted Sectors

The most commonly targeted sectors list revealed interesting insights. Manufacturing took top place, prompting the publication of 142 tippers. Manufacturing is also the most commonly targeted sector for ransomware activity; this highlights the key role IABs play in identifying and supplying access to ransomware operators and other extortionists. There was a significant sectoral difference among median prices of IAB access. The highest median price was $5,500, for a banking entity, and the greatest interquartile range was $23,000, also for a banking entity. Access to a banking entity is sold for the highest prices because it represents significant financial opportunity. But banks are likely to have substantial security budgets to avoid such risks—budgets likely not matched by other heavily targeted sectors. As a result, banking access is much less common—warranting only 14 tippers in 2022—and is more likely to generate interest from buyers; scarcity justifies the high price.

![Image description: Sectors most commonly targeted by IAB activity]
*Figure 13: Sectors most commonly targeted by IAB activity*

### Case Study: Exotic Lily

The data behind IABs shows that all sectors have some sort of access being solicited on the dark web. How do these brokers get access to a company’s environment? ReliaQuest uncovered a good example to hold up for examination. The “Exotic Lily” IAB began by sending elaborate phishing emails from what appeared to be a potential business prospect, to the inbox of a high-profile employee. This was accomplished by spoofing a legitimate domain, eaglemine[.]com, using a similar TLD: eaglemine[.]co.

Because the purported organization was a potential sales lead for the recipient, Exotic Lily succeeded in establishing communication. They next sent the recipient a ZIP file, named for_company.zip, from the legitimate file-transfer website WeTransfer[.]com, to bypass email security gateways. Unzipped, the file contained an IMG file with the name project_requirments.img; when mounted, it likely contained a LNK file that the user clicked. This resulted in a Python interpreter being loading into memory and executing a Python script, which downloaded a Cobalt Strike beacon. ReliaQuest attributed the malicious activity to Exotic Lily by continuously monitoring the known infrastructure of that IAB.

![Image description: Typical IAB lifecycle, as observed with Exotic Lily]
*Figure 14: Typical IAB lifecycle, as observed with Exotic Lily*

Security operations need internal- and external-event visibility. Securing an environment against IABs is accomplished through a robust security program, using defense in depth (DiD) strategies for internal and external locations. IABs like Exotic Lily are highly skilled at profiling users and developing phishing campaigns tailored to them. A robust security awareness program allows users to spot indicators of suspicious activity and act accordingly.

## Initial Access Malware

In addition to identifying and stealing credentials for RDP, VPN, and other remote-access software, IABs are prolific at using malware to access a network.

### QakBot

IAB-run “QakBot” spam campaigns in 2023 have frequently used malicious OneNote files to deliver malware that grants initial access to a system. Our research across the cybercriminal underground revealed users of multiple dark-web forums sharing information and articles about QakBot’s operators. They said the operators used HTML smuggling techniques to deliver malware using SVG images embedded in HTML email attachments, toward the end of 2