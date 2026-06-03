# Malicious Registrations in the Domain Name Market
## An Analysis of 2025 gTLD Registrations and Cybercriminal Demand
INTERISLE CONSULTING GROUP JUNE 2026

## Table of Contents
- [Executive Summary](#executive-summary)
- [Introduction](#introduction)
- [Malicious Registrations as a Share of the gTLD Market](#malicious-registrations-as-a-share-of-the-gtld-market)
- [Case Studies: Associated Domains & Organized Criminal Activity](#case-studies-associated-domains--organized-criminal-activity)
- [Bulk Registrations, Sales Programs, and Market Incentives](#bulk-registrations-sales-programs-and-market-incentives)
- [Discussion and Conclusion](#discussion-and-conclusion)
- [Sponsors](#sponsors)
- [Acknowledgements](#acknowledgements)
- [About Interisle Consulting Group](#about-interisle-consulting-group)
- [About the Authors](#about-the-authors)
- [Methodology](#methodology)
- [Endnotes](#endnotes)

## Executive Summary
Cybercrime is a professionalized, multinational industry that relies on a steady supply of cheap, disposable domain names to perpetrate malicious attacks at scale. This study measures the extent to which malicious actors drove new registrations in the gTLD market in 2025.

Using publicly and commercially available data, it shows that cybercriminal demand constitutes a significant share of the domain name market.

### KEY FINDINGS:
- **Criminal organizations purchased domains at scale.** Malicious actors purchased between 10% and 20% of all gTLD domain names created in 2025. This report establishes that 10% is the floor, documenting that 8.5 million of the 85 million domains created in 2025 have already been blocklisted for malicious activity. However, blocklists miss many domains registered by bad actors. Applying conservative projections for additional future blocklistings and associated domains that were not identified by blocklists, the actual number of domains registered by malicious actors in 2025 may be closer to 16.8 million, or 20% of all domains created that year. [see pages 6-8]
- **Abuse is widespread across the market, but highly concentrated at specific gTLDs, registrars, and corporate families in the industry.** Five registrars accounted for 50% of all blocklisted domains; at one registrar, 88% of new registrations were blocklisted. Multiple open gTLDs saw more than half of their new registrations used for malicious activity. Two gTLDs had nearly two million new registrations flagged for abuse. [see pages 9–16]
- **The detection, prevention, and mitigation of this activity was partial and far from effective.** Case studies in this report detail how criminal gangs registered hundreds of thousands of domain names to conduct phishing, malware, and scam campaigns. Even after U.S. government sanctions were imposed on the criminal FUNNULL organization in May 2025, it continued to acquire domain names. Small percentages of blocklisted domains were suspended by registrars and registries. [see pages 17–22]
- **Low renewal rates are an indicator of abuse.** gTLDs used by cybercriminals posted renewal rates as low as 0.5%, indicating that legitimate use was negligible. [see pages 18–20 and 23–24]
- **The market provides incentives for registrars and registry operators to take or tolerate abusive registrations.** Sales and incentive programs designed to drive growth and market share encourage sales to high-volume, repeat customers. Some registrars and registry operators appear to derive commercial benefits from selling large numbers of domains to bad actors. Even when abusive domains generate little revenue, there still may be an incentive to tolerate them when deterrence is more costly or risks losing higher-margin legitimate customers. The resulting social costs of cybercrime, however, including financial losses, business disruption, and eroded public trust, are borne by victims, businesses, and society at large. This is a classic negative externality that distorts the market and undermines the broader benefits of competition. [See pages 25–27]

Abuse is not inevitable, however. Some registries and registrars grew without attracting outsized levels of abuse. Pricing strategies, provider practices, and abuse mitigation choices can materially affect whether growth is driven by legitimate demand or by cybercriminal registrations. Improvements in domain name policies and practices are needed to reduce cybercriminals’ access to domains while supporting legitimate market growth. Additional new, open gTLDs will be introduced in the coming year and beyond. Absent more effective controls, the increase in competition and domain name supply will likely exacerbate the current situation, shifting greater costs and harm to the public.

## Introduction
Cybercrime is a pervasive, professionalized, and multinational industry that causes billions of dollars of losses and damage each year.[^1] Almost anyone can become a victim at any time. Domain names are an essential resource for committing all types of cybercrime. They provide the locations for phishing, malware, scam and fraud sites, are used to control botnets, and to advertise abusive activities through email, on social media, and via text messages.

Understanding how many domain names are being used for abusive activities, and how bad actors acquire and use those domains, is essential. This study establishes how many gTLD domain names that were registered in 2025 have been blocklisted for malicious activity. It reveals how many domain names were sold to bad actors, and provides case studies revealing what they did with them. This report places the domain abuse problem into perspective, and provides reliable data so that participants in the broader Internet community, including policy-makers, can make informed decisions.

It is possible to study domain abuse in this way in the “generic Top Level Domains,” or gTLDs, because rich data about domain registrations, transactions, and abuse are available. gTLD domains are 63% of the entire TLD space[^2], and approximately 82% of all blocklisted domains have been in the gTLDs.[^3] The gTLD space is overseen by ICANN, the Internet Corporation for Assigned Names and Numbers. ICANN determines what gTLDs exist, and awards the contractual right to operate each gTLD to a registry operator. ICANN also accredits the registrars who sell domains in the gTLDs. ICANN determines what policies govern the gTLD space, including under what circumstances registry operators and registrars must respond to abuse complaints. ICANN publishes the numbers of domain transactions made by each registrar in every gTLD[^4], and requires registrars and registry operators to make basic data about individual domain names available via the Registration Data Access Protocol (RDAP). These kinds of transaction and registration data are only partially available (and often not available at all) for the country-code TLDs.

To understand what domains are being used for abusive activities, Interisle collects data from prominent Reputation Block Lists (RBLs). These blocklists contain domain names and/or the URLs of dangerous and unwanted content, including known phishing, malware, and scam and fraud sites. RBLs are widely used as a defensive measure. Internet service providers, email providers, web browser providers, Domain Name System (DNS) resolvers, and other organizations use these RBLs to block access to (and traffic and email from) these domains and URLs, protecting their users from online threats. The RBLs we use are provided by professional security threat-reporting sources, and are used to protect literally billions of users across the world.

Blocklist data therefore provides a practical measurement of what is happening in the “real world,” the Internet ecosystem that uses the DNS. It shows what domain names that professional anti-abuse sources have identified as harmful, and what domains are being blocked by security administrators at private and public networks and services around the world. ICANN takes a similar approach with its Metrica abuse measurement system. ICANN’s security and research team notes: “We believe that it is beneficial to collect the same DNS abuse data that is reported to industry and Internet users. Security systems such as anti-spam or anti-malware gateways or firewalls that protect billions of users incorporate these data into their DNS abuse mitigation measures.”[^5]

Interisle uses only publicly and commercially available data. Our findings and reporting can be independently validated by any party who collects the same data and applies the same general methods. For details about what data we collect, and our research methodologies, please see the Methodology section at the end of this report.

## Malicious Registrations as a Share of the gTLD Market
Cybercriminals continually register new domain names in bulk to carry out their malicious activities. Various studies have analyzed the factors that drive domain abuse and malicious domain registrations. They have established that low prices tend to attract abuse, and this especially occurs in “open” gTLDs – those that are open to all registrants and have no registration limitations or requirements.[^6][^7][^8][^9][^10][^11] One major study established that each dollar reduction in domain price corresponds to a 49% increase in malicious domain registrations, that free bundled services such as web hosting drive an 88% surge in phishing domains, and that API access provided by registrars for domain registration or account creation is associated with a “staggering” 401% rise in malicious domains.[^12]

The registration of domains in batches is a well-known tactic among cybercriminals, who use them to perpetrate DNS abuse at scale. The ability to easily register domains in bulk enables attackers to quickly establish disposable infrastructure, evade detection, and scale their operations. From a security perspective, the identification and characterization of bulk domain registrations are of critical importance for abuse mitigation.[^13]

What part does this malicious activity play in the domain name market? The overall gTLD market has been growing slowly, and most newly registered domains replace domains lost through non-renewal. From 2021 through 2024, the market grew by a total of 6.2%. In 2023 the entire TLD market only grew by 1%,[^14] and the benchmark .COM TLD shrank every quarter in 2023 and 2024.[^15] 2025 saw greater growth, as registry operators and registrars placed emphasis on gaining new registrations. During 2025 the gTLDs grew by 8.1%, increasing from 233 million to just under 252 million total domains.[^16]

![gTLD Domains Under Management 2021–2025 chart]

A total of 84,961,989 gTLD domains were created in 2025. These new registrations are the most relevant to cybercrime. Cybercriminals register domains, use them, and then abandon them, registering more domains as they need. Cybercriminals very rarely renew their domain names when they reach their one-year anniversary. Renewals, and the total number of domains in any TLD or at any registrar, are not a measure of new sales or new demand in the market.

As of 18 May 2026, 8,496,811 of the domains created in 2025 had been added to blocklists — 10% of all the gTLD domains sold during 2025. About 98% of these appear to have been maliciously registered, rather than compromised after creation. (For more about malicious activity versus compromised domains, see the Methodology section.)

Those malicious domain registrations were a significant contributor to the growth of the gTLDs in 2025. In January 2025, 5.9 million gTLD domains were created and 5.5 million domains were deleted, resulting in a net growth of 408,000 domains. But 723,000 domains created in January 2025 were subsequently blocklisted, eclipsing overall growth. The number of malicious domains registered in the gTLDs also exceeded overall gTLD growth in February and May 2025:

![Total Growth, Malicious Creates, and Non-Malicious Growth 2025 chart]

![Non-Malicious Creates and Malicious Creates 2025 chart]

8.5 million is the number of blocklisted domains so far, establishing a conservative floor of how many domains were registered by bad actors in 2025. What might the actual numbers look like?

The number of new domain names being used for abusive purposes is significantly higher than 10%, for two reasons:

1. The blocklist providers do not detect or list all the abusive domain registrations. For more about this, see the “Case Studies” section below.
2. More domains that were created in 2025 will be added to the blocklists through the rest of 2026. Additional domains registered in late May 2025 through December 2025 will be blocklisted; the total will rise through December 2026.

We project that an additional 2% of 2025’s registrations may get blocklisted by the end of December 2026, raising the total to around 12% of all new registrations, or 10.1 million domains. This is because some criminals strategically “age” their domains, not using them for months in order to evade blocklist scoring systems that place less trust in recently registered young domains.[^17][^18] We base our projection on what happened the year before: 2.32 million domains created in 2024 were added to blocklists between June and December 2025.

What about maliciously registered domains that were missed by the blocklist providers? A recent study of batch registrations made by ICANN’s Office of the CTO provides a clue. It found that for every three domains appearing on blocklists, two additional domains appear to have been registered within the same registration batches–or an “80% increase in the volume of newly registered RBL domains.” In other words, bad actors may register 66% more domains than the blocklists indicate.[^19] The blocklist providers simply miss some domains purchased by bad actors. For more about this, see the “Case Studies” section later in this report.

We predict that approximately 10.1 million domains registered in 2025 will be blocklisted by the end of 2026. When we apply the associated domains projection (an additional two-thirds of registrations), this suggests that 16.8 million domains were potentially purchased by bad actors in 2025, or 20% of the total gTLD new registration market in 2025.

The 20% figure is a projection only, but it is notable that the ICANN analysis was conservative in some ways. Those researchers stated that “the true rate is likely to be higher” since they excluded ”many valid batches” such as those containing more than 1,000 domains. (In later sections of this report we document that large batches far in excess of 1,000 are regular occurrences.) The ICANN researchers stated that their results “indicate that batch registrations are prevalent, significantly predict overall abuse rates, and are useful for pivoting and expanding from known malicious ‘seed’ domain sets, particularly in certain TLDs and registrar environments.”

These numbers are not out of line with what other sources observe. Threat intelligence company Infoblox provides a widely used protective DNS solution. In 2025 Infoblox identified 100.8 million newly observed second-level domains (in both gTLDs and ccTLDs), and classified 25.1% (25 million) of them as malicious or suspicious.[^20]

In the case studies later in this report, we performed similar “expansion analyses” of several gTLDs. We found that cybercriminals registered far more domains than the blocklists indicated.

Malicious registrations were pervasive across the gTLD space. In 2025, domains were blocklisted in 566 gTLDs–in almost all of the non-brand gTLDs. Malicious registrations were created at 2,684 registrars – 88% of the 3,022 currently accredited registrars.[^21] But as detailed below, abuse was concentrated disproportionately in certain TLDs and at certain registrars.

Unless otherwise noted, blocklisting figures below for domains registered in 2025 were as of 30 April 2026.

### Malicious Registrations by TLD
Malicious registrations were made disproportionately in the new, open gTLDs:

Which gTLDs and registrars had the largest numbers of maliciously registered domains, and significant percentages of malicious registrations, in 2025? Below, “malicious registrations” is the number of domains created in a TLD (or by a registrar) in 2025 that were blocklisted some time after creation and by 30 April 2026, and the domains met our “malicious registration” criteria (see the Methodology section for details). The data indicates that certain TLDs and registrars are disproportionately associated with malicious registrations.

The gTLDs with the most blocklisted domains were:

| 2025 RANK | gTLD | OPERATOR | NEW DOMAINS CREATED (NET ADDS) IN 2025 | NEW DOMAINS CREATED IN 2025, BLOCKLISTED, AND MALICIOUS (MINIMUM 100,000) | % OF NEW DOMAINS BLOCKLISTED, AND MALICIOUS |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | .COM | Verisign | 39,469,949 | 1,927,917 | 4.9% |
| 2 | .TOP | Jiangsu Bangning Science & Technology* | 5,193,483 | 1,793,822 | 34.6% |
| 3 | .INFO | Identity Digital | 2,615,401 | 561,614 | 21.5% |
| 4 | .BOND | ShortDot SA | 1,701,566 | 514,197 | 30.2% |
| 5 | .VIP | Registry Services LLC (GoDaddy Registry) | 1,064,741 | 354,690 | 33.3% |
| 6 | .XYZ | XYZ.COM LLC | 7,236,034 | 275,896 | 3.8% |
| 7 | .SHOP | GMO Registry, Inc. | 3,308,236 | 243,660 | 7.4% |
| 8 | .PRO | Identity Digital | 714,875 | 174,184 | 24.4% |
| 9 | .ICU | ShortDot SA | 526,433 | 149,861 | 28.5% |
| 10 | .SBS | ShortDot SA | 1,280,067 | 144,403 | 11.3% |
| 11 | .MOBI | Identity Digital | 225,180 | 141,483 | 62.8% |
| 12 | .NET | Verisign | 2,226,300 | 129,357 | 5.8% |
| 13 | .CFD | Identity Digital | 490,977 | 124,386 | 25.3% |
| 14 | .CYOU | ShortDot SA | 388,161 | 116,812 | 30.1% |
| 15 | .ORG | PIR | 2,529,826 | 100,110 | 4.0% |

*\*Sponsorship transferred to Hong Kong Zhongze International Limited in January 2026. https://www.iana.org/domains/root/db/top.html*

Thirteen gTLDs had the majority of their new domains blocklisted, indicating significant purchases by bad actors. Twelve of the 20 gTLDs with the highest blocklisting rates were operated by Identity Digital. The gTLDs that were most highly blocklisted were:

| 2025 RANK | gTLD | OPERATOR | DUM DEC 2025 | NEW DOMAINS CREATED (NET ADDS) IN 2025 | NEW DOMAINS CREATED IN 2025, BLOCKLISTED, AND MALICIOUS (MINIMUM 100,000) | % OF NEW DOMAINS BLOCKLISTED, AND MALICIOUS |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | .LOCKER | Orange Domains LLC | 23,612 | 22,201 | 16,192 | 72.9% |
| 2 | .LGBT | Identity Digital | 18,102 | 9,859 | 7,116 | 72.2% |
| 3 | .TOWN | Identity Digital | 35,872 | 31,018 | 21,760 | 70.2% |
| 4 | .GDN | Joint Stock Co "Navigation-information systems" | 49,747 | 45,395 | 30,545 | 67.3% |
| 5 | .MOBI | Identity Digital | 429,361 | 225,180 | 141,483 | 62.8% |
| 6 | .XIN | Elegant Leader Limited | 127,902 | 111,875 | 65,834 | 58.8% |
| 7 | .LOAN | dot Loan Limited (PwC, Gibraltar) | 118,486 | 79,653 | 45,786 | 57.5% |
| 8 | .PICTURES | Identity Digital | 32,051 | 6,122 | 3,437 | 56.1% |
| 9 | .QPON | DOTQPON LLC | 55,749 | 58,704 | 32,317 | 55.1% |
| 10 | .MOV | Charleston Road Registry (Google) | 6,357 | 2,570 | 1,371 | 53.3% |
| 11 | .BID | dot Bid Limited (PwC, Gibraltar) | 69,578 | 32,082 | 16,858 | 52.5% |
| 12 | .PIZZA | Identity Digital | 35,877 | 9,258 | 4,794 | 51.8% |
| 13 | .AUCTION | Identity Digital | 12,419 | 6,742 | 3,457 | 51.3% |
| 14 | .PINK | Identity Digital | 26,690 | 8,810 | 4,239 | 48.1% |
| 15 | .REVIEWS | Identity Digital | 13,256 | 3,744 | 1,780 | 47.5% |
| 16 | .CLAIMS | Identity Digital | 6,072 | 2,760 | 1,310 | 47.5% |
| 17 | .PET | Identity Digital | 26,618 | 12,889 | 6,000 | 46.6% |
| 18 | .FORSALE | Identity Digital | 5,472 | 2,292 | 1,051 | 45.9% |
| 19 | .DATE | dot Date Limited (PwC, Gibraltar) | 11,107 | 5,198 | 2,190 | 42.1% |
| 20 | .LOANS | Identity Digital | 11,376 | 4,061 | 1,705 | 42.0% |

There is great variability in the percentages of malicious registrations in various TLDs. The absolute numbers are important, though–each blocklisted domain represents some amount of risk and potential damage.

An interesting case is .XYZ, which grew significantly in 2025, from 4.4 million to 8.7 million domains. Its 2025 renewal rate was only 18.7%, so it had to add a large number of new domains to make up for its losses due to non-renewal. .XYZ had 7.2 million net-adds during the year, of which 275,896 of its 2025 registrations blocklisted. That is a significant number for any TLD, but a relatively low percentage of its overall new registrations. It appears that XYZ.COM was somehow able to replace its losses and grow the TLD without attracting outsized abuse. We are not able to analyze the contributing factors in this case, but it suggests that it is possible to craft incentives, marketing programs, and/or deterrents that manage abuse levels.

Another way of examining registrations is by “registry family.” Some companies operate multiple gTLDs, delegated to them by contract with ICANN. TLDs in a “family” are under the common legal, operational, and marketing control of one entity. We do not consolidate TLDs by back-end operator, only by sponsorship control as listed in the IANA root zone record.[^22] For example, Identity Digital is the “TLD manager” of hundreds of gTLDs. It holds the ICANN contracts for them under subsidiaries such as Binky Moon LLC, Dog Beach LLC, and Identity Digital Limited.

We researched the ownership of the gTLDs and consolidated their numbers below. About 92% of the domains that were created in 2025 and then blocklisted were in gTLDs operated by just eight companies:

![REGISTRY FAMILIES WITH MOST BLOCKLISTED (MALICIOUS) DOMAINS, 2025 chart]

## Case Studies: Associated Domains & Organized Criminal Activity
We examined four TLDs—.LOAN, .PINK, .BOND, and .GIFT—as case studies. There we identified hundreds of thousands of domains registered by professional criminal organizations, accounting for most of the domains in three of the four TLDs.

We found thousands of associated domains registered by the bad actors that were never blocklisted, illustrating how the criminal registration problem is notably larger than the blocklisting numbers indicate. Starting with blocklisted domains as indicators, we found 38% to 63% more associated domains that were likely registered by the bad actors. We found significant numbers of associated domains even in heavily blocklisted TLDs.

When TLDs had high numbers of malicious registrations, their renewal rates plummeted a year later. This emphasizes the exceptionally low legitimate use of those TLDs.

Security researchers have tracked how threat actors have used programmatic mechanisms to register millions of domain names to perpetrate abuse at scale.[^25][^26] Once blocklist providers find an indicator of abuse, they analyze infrastructures and registration data to find “associated domain names” – the additional domains in the batches that are registered for malicious purposes. Registry operators can access those same kinds of data. Domain registrars have significantly greater data with which to perform these checks that other parties do not, including registrant contact data, payment details, and registrant IP addresses.

### Associated Domains
A recent study about associated domains was performed by the research team in ICANN’s Office of the CTO (OCTO).[^27] This study found that “at least 16% of newly registered gTLD domains, [created] in the first quarter of 2025, exhibited batch registration patterns.” Starting with an initial set of “seed” RBL-listed domains, the researchers found an additional 80% more domains that were associated with the blocklisted ones. This “indicates that for every three newly registered malicious domains reported through RBL feeds, batch expansion (using conservative filtering) identifies an additional two neighboring domains.” The researchers stated that “the true rate is likely to be higher” since they excluded ”many valid batches” such as those containing more than 1,000 domains. The results “indicate that batch registrations are prevalent, significantly predict overall abuse rates, and are useful for pivoting and expanding from known malicious ‘seed’ domain sets, particularly in certain TLDs and registrar environments.”

We performed “associated domain checks” or “expansion analysis” of four TLDs, using blocklisted domains to point us to potentially associated domains. We obtained registration data for all the domains in these TLDs, based on the contents of their zone files at two points (30 July and 2 September 2025), and for all the blocklisted domains. Our criteria shared similarities with the ones used in the ICANN OCTO study. We considered domains to be associated when they shared the following characteristics:

1. At least one domain in the set was blocklisted for abuse, AND
2. the domains were created by the same registrar(s), AND
3. the domains were registered within a time-bound manner (typically less than 10 minutes between consecutive registrations), AND
4. the domains used the same hosting (same nameserver pair, and/or same IP address/A record), AND
5. the domains followed the same distinctive string pattern. These are lexical similarities often produced by domain generation algorithms. These include same string length, reoccurring or progressive characters or substrings, use of all digits, use of all letters, and use of hyphens.

We then performed manual validation of the data, examining every record for every domain. This allowed us to find and confirm certain registration patterns, some of which we describe below.

### FUNNULL: Professional Criminal Domain Registrations
Some of the registrations in these case studies were the work of FUNNULL, a criminal content delivery system that is a key infrastructure provider for Southeast Asia’s cybercriminal ecosystem. FUNNULL offers one-stop services that have been used to perpetrate billions of dollars in financial losses since 2022, through cryptocurrency investment fraud and “pig butchering” scams, phishing campaigns, malware attacks, and other illicit activities.[^28][^29][^30] FUNNULL has registered and supported perhaps more than a million domain names for cybercriminals using domain generation algorithms (DGAs). FUNNULL is linked to the majority of the virtual currency investment scam websites reported to the Federal Bureau of Investigation (FBI). U.S.-based victims of these scam websites have reported over $200 million in losses, with average losses of over $150,000 per individual, although investigators believe the actual losses are much higher. Among others, FUNNULL also hosted thousands of illegal gambling sites for the Suncity Group, a transnational Chinese crime syndicate involved in laundering billions of dollars for Chinese criminal groups, and has been linked to North Korea’s Lazarus Group, a state-sponsored hacking group.[^31][^32] In the second half of 2024 alone, Quad9 blocked more than 570 million queries to the domains attributed to FUNNULL’s Polyfill.io attack.[^33] FUNNULL and its associated groups continue to be threats in 2026.[^34][^35]

On 29 May 2025, the U.S. government placed FUNNULL and its administrator Lui Lizhi on its sanctions list. This required that all assets of FUNNULL in the United States (or in the possession or control of American entities) be blocked and reported to the financial intelligence and enforcement agency of the United States Treasury Department, and the sanctions prohibited U.S. entities from transacting with any entities related to FUNNULL.[^36] In connection with the sanctions, the FBI released a list of more than 332,000 domain names it had documented on FUNNULL’s infrastructure.[^37] FUNNULL spread its activity across multiple TLDs, registrars, and hosting infrastructure. Only 56.6% of the domains on the FBI’s list made their way onto the blocklists we monitored, either before or after the FBI released its list. This is an example of how malicious registrations can be missed by RBLs, especially when the activity involves large sets of domain names, and the malicious activity is distributed.

### Case Study: .LOAN
We chose to study .LOAN because it experienced unusual growth. This open gTLD was operated by Domain Venture Partners PCC Limited (DVP) of Gibraltar until 2018, when it was placed into administration following disputes with investors. The court-appointed administrator is a Gibraltar-based accountant at PricewaterhouseCoopers.[^38][^39][^40]

.LOAN was historically a small TLD – there were only 7,000 domains in it in January 2024. Its growth surged beginning in August 2024, and by September 2025 there were 132,258 .LOAN domains in the registry, or growth of 1,880%. Of those domains, 76,892 had been blocklisted in 2025 and 2026 – about 58% of the TLD.

Using those blocklisted domains as a starting point, our expansion analysis found 31,777 additional associated domains (41% more). We therefore believe that more than 108,600 .LOAN domains were registered for abuse, or more than 82% of the domains in the TLD as of September 2025. It appears that FUNNULL made at least 100,000 of those registrations.

The following chart shows how that surge in malicious registration drove .LOAN’s fast growth, beginning in August 2024. A year later, as malicious registrations began to expire, .LOAN’s renewal rate plummeted, from its historical range of 40% to 70% down to just 4.6%. This emphasizes the exceptionally low quality of the registration base during the period in question.

![.LOAN Domains in Registry chart]

Associating domains was straightforward because so many .LOAN domains had been blocklisted, and because:

1. 4,418 .LOAN domains were attributed to FUNNULL by the FBI, and another 5,447 were attributed to FUNNULL by Infoblox. These “seed” domains were interspersed through long sequences of clearly related domain registrations.
2. The domains fell into distinct patterns. For example:
    A. Just over 100,000 of the domains (75% of the TLD) were composed of numerals only. Such domains were not intended to host businesses or personal sites, but were algorithmically generated to be used and discarded.
    B. Much of the sequence 00001.loan through 99999.loan was registered, including many of the FUNNULL domains the FBI and Infoblox identified. Six-digit domains were also registered, with gaps between them.
    C. The gaps apparently exist because FUNNULL was registering numbers across TLDs, scattering registrations across time and the domain space. For example, the FBI observed the FUNNULL domains 12529.loan and 12538.loans (plural, a different TLD), which were registered at different registrars 27 days apart. And the FBI logged FUNNULL registrations including 27271.one, 27272.loan, 272722.me, 272777.cn, and 272788.loan.
3. FUNNULL’s domains were limited to a small number of registrars and nameserver pairs. U.S. registrar Dynadot had 84,449 total domains (blocklisted plus associated), some delegated to nameservers in China. NameCheap and NameSilo had more than 6,000 each.
4. There were smaller sets of malicious registrations apparently made by other actors. For example a set of 86 domains was used for a “toll road” phishing campaign. (e.g., http://e-zpass.com-etcww.loan/) There were other blocklisted domains in clear alphabetical sequences, such as chipca.loan and chipcb.loan through chipcz.loan.

After the U.S. sanctions on FUNNULL were imposed on 29 May 2025, most of FUNNULL’s .LOAN domains remained in the zone file; they were not suspended via clientHold or serverHold. And FUNNULL registered thousands more .LOAN domains after the sanctions went into effect, including large sets at U.S.-based registrars.

Of the 76,892 blocklisted domains, about 5,541 (7.2%) were removed from the zone before their one-year anniversaries. Some, such as the batch of 86 phishing domains above, had been suspended by the registrars. Other blocklisted domains were placed on serverHold status, suspended by the registry operator.

Of the 31,774 domains we found via expansion analysis, all were still in the zone in September 2025–i.e. none had been suspended. Although there had been significant blocklistings, and the registrar and registry operator had apparently responded to some complaints about these domains and their registrant(s), the registrars and registry operator apparently did not suspend associated domains by removing them from the DNS.

### Case Study: .PINK
We chose to examine .PINK because it displayed rapid growth. In June 2024 it contained only 5,800 domains, but by March 2025 it had grown by a factor of seven, to almost 42,000 domains. .PINK was launched as a generic and open TLD.[^41] It is operated by Identity Digital, a major registry operator based in the United States.

Like .LOAN, .PINK’s growth was attributable to bad actors. 22,987 .PINK domains registered in 2024 and 2025 were blocklisted. Our expansion analysis found an additional 8,798 .PINK domains that were closely associated with the blocklisted domains, and that the RBLs had not listed. This was a 38% expansion beyond the 22,987 blocklisted domains. After expansion analysis, it appears that in September 2025, 76.3% of the domains in the .PINK TLD were associated with abusive actors.

The following chart shows that a surge in malicious registration drove .PINK’s fast growth. A year after the malicious registrations, .PINK’s renewal rate plummeted, from its historical average of 60% to 70% down to just 3.1% in December 2025. This emphasizes the exceptionally low legitimate use of the TLD during the period in question.

![.PINK Domains in Registry chart]

The abusive domains were mainly associated with FUNNULL, following some of the same patterns and registration tactics that we found in .LOAN. The FBI documented 1,839 .PINK domains registered by FUNNULL, and Infobox documented 571 more. Many of those domains were in the sequence 00001.pink through 99999.pink.

Funnull registered .PINK names in a numerical sequence, with gaps between numbers. Some of the domains were identified by security observers, and some were not identified or blocklisted at all:

| Domain | Detected by |
| :--- | :--- |
| 22238.pink | Infoblox, SURBL |
| 22253.pink | no source; associated domain |
| 22261.pink | no source; associated domain |
| 22274.pink | Spamhaus |
| 22277.pink | FBI |
| 22290.pink | FBI |
| 22291.pink | no source; associated domain |
| 22301.pink | Infoblox, Spamhaus |
| 22302.pink | no source; associated domain |
| 22314.pink | no source; associated domain |
| 22317.pink | no source; associated domain |
| 22319.pink | Spamhaus |
| 22320.pink | Spamhaus |
| 22322.pink | no source; associated domain |

FUNNULL’s .PINK domains were registered across registrars, and the bad actor mixed up blocks of related domains in order to evade detection. For example:
- 00035.pink through 00043.pink were registered at Sav.com from 9 to 11 September 2024.
- 00044.pink through 00099.pink were registered on 28 September 2024, across three registrars: Dynadot, Sav.com, and Domain International Services Limited.
- Then domains falling in the numerical sequence before those – 00030.pink through 00034.pink – were registered at Domain International Services Limited also on 28 September 2024.
- Later FUNNULL shifted to a pattern of five random letters.

Many of the nameserver pairs were not the registrars’ default nameservers that they assign automatically when registrants do not designate their own nameservers. For example, FUNNULL registered .PINK domains at U.S. registrars including Dynadot and GoDaddy, but placed the domains on nameservers n1.xundns.com and n2.xundns.com, which are operated by Chinese hosting provider DNS.LA. After a few days of being created, others were switched to China-based nameservers such as ns1.1233dns.com and ns2.951dns.com.

After the U.S. sanctions of FUNNULL were imposed on 29 May 2025, most of FUNNULL’s .PINK domains continued to resolve, and FUNNULL registered more more .PINK domains, some at U.S. registrars.

Of 19,419 domains blocklisted by September 2025, 3,156 (16.3%) had been removed from the zone by that time. Of the 8,795 domains we found via expansion analysis, all were still in the zone in September 2025 –i.e. none had been suspended by the registrars or the registry. Although there had been significant blocklistings (and sanctions), the registrars and registry operator had suspended a distinct minority of the blocklisted domains, and none of the associated domains.

There were also .PINK domains registered by other threat actors. Four hundred and forty-two .PINK domains following the pattern teleg[4 random letters].pink were registered at registrar Chengdu West. They were used to phish Telegram users, and some were blocked by Google Safe Browsing. Only 77 of them had been blocklisted by our sources; we found another 364 by association. After several months, only 34 of the 442 domains had been suspended.

![Phishing page at telegbftc.pink, 5 May 2025. Source: urlscan.io[^42]]

A different set of .PINK domains registered at Chengdu West was also used to phish Telegram users. That set was composed of thirteen random letters. Only six were ever blocklisted, and we found 176 more by association.

### Case Study: .BOND
We chose to study .BOND because of its anomalously low renewal rate, and because the number of domains in the TLD fluctuated radically. .BOND is an open gTLD operated by Shortdot SA in Luxembourg.

From January through October 2025, the “Revolver Rabbit” cybercriminal gang registered at least 350,000 .BOND domains at registrar Key-Systems.[^43] The gang used .BOND domains to distribute information-stealing malware. The domains followed a very recognizable format: hyphen-separated words followed by a five-digit number, such as security-apps-25597.bond, work-abroad-18297.bond, and cremation-services-37263.bond.

Revolver Rabbit’s malicious activity using the .BOND domains was described by security researchers in July 2024.[^44][^45] At the time, Key-Systems was promoting .BOND as a domain that would help establish registrants with a “professional image as a trusted financial entity.”[^46] Reportedly more than 500,000 .BOND domains were used in the campaign during 2024 and 2025, which would have cost a significant amount of money at retail – perhaps US$1 million or more.[^47][^48]

As a result of this activity, .BOND has had abysmal renewal rates over the last two years. .BOND’s overall renewal rate for 2025 was 0.5%. Only about one in two hundred .BOND domains renewed in 2025, underlining the exceptionally low legitimate use of the TLD.

In November and December 2025, Japanese registrar GMO Internet Group registered more than one million .BOND domains, accounting for almost all of the 1.18 million domains in the .BOND registry. GMO offered .BOND domains for an extremely low price: ¥114 or US$0.75 each. This massive influx consists almost entirely of algorithmically generated domains. Many consist of various prefixes and then letters and numerals. (3gx2q1.bond, 3gxcmq.bond, decadetjfkgc.bond, decadeuohbqe.bond, etc.) Blocklisting of these domains started accelerating in late March 2026, and we will not be surprised if they mount significantly as 2026 continues.

![.BOND Domains in Registry chart]

### Case Study: .GIFT
For our fourth case study, we randomly selected .GIFT from among a list of small, open gTLDs that have not been historically associated with abuse. The .GIFT registry is sponsored and operated by Uniregistry.

In September 2025, .GIFT had 5,977 domains in the registry. Of the .GIFT domains created in 2024 and 2025, 528 had been blocklisted. Several of those domains were known to have been registered by FUNNULL in July 2024.[^49] It appears that at least 400 of the blocklisted .GIFT domains were associated with FUNNULL, which registered them into January 2025. These domains were all composed of five random letters, and were registered at just two registrars (Dynadot and NameSilo).

Our expansion analysis found an additional 332 .GIFT domains that were closely associated with the others, and that the RBLs had not listed. This was a 63% expansion beyond the original 528 blocklisted domains. The additional domains also appear to be associated with FUNNULL, following the same five-letter pattern.[^50] After expansion analysis, it appears that 15% of the .GIFT registry was associated with abusive actors.[^51]

Of the 528 blocklisted domains, only 49 (9%) had been removed from the zone by September 2025. Of the 332 domains we found via expansion analysis, all were still in the zone in September 2025. This indicates that although there had been blocklisting, the registrars and registry operator had suspended very few of the domains, and suspended no associated domains.

In 2025, .GIFT had a relatively high 61.3% renewal rate, reflecting the TLD’s lower abuse rate, and indicating a higher-quality set of registrants.

### Renewal Rates
Low renewal rates can provide corroborating evidence of large-scale abusive registration activity.

Registries and registrars must continually register new domains in order to replace expiring domains, and must register even more in order to grow. Renewal rates are therefore a key indicator of business quality.

The benchmark .COM/.NET registry traditionally has a renewal rate of 74% to 75%, enjoying a stable base of domains that renew year after year. The well-known .ORG TLD has an even higher renewal rate, at over 80% yearly. The overall renewal rate for all gTLD domains in 2025 was 67%,[^52] (heavily influenced by the high renewal rate in the large .COM TLD). The median renewal rate for individual gTLDs was 63%, and 122 gTLDs had renewal rates below 50%. Those are overall renewal rates, for all domains in a TLD. While older domains tend to renew, the renewal rates for newly registered domains are lower.[^53]

Spamhaus considers that a new domain creation rate that is 10% to 20% higher than usual is “unusually high… This behavior suggests a large volume of domain churn, with domains being registered and cancelled quickly.”[^54]

Of gTLDs with at least 250,000 domains in them, some had overall renewal rates of less than 10% in 2025. Most of these TLDs actually grew during 2025, attracting significant numbers of malicious registrations that filled losses due to non-renewal and made growth possible.

## Bulk Registrations, Sales Programs, and Market Incentives
Bad actors tend to register sets of domains, and some consume large numbers of domains over time. These domains also tend to be low-priced, a reflection of aggressive price competition in the gTLD market and sales strategy choices made by registrars and registry operators.

### Bulk Registrations
Of the 8.3 million gTLD domains registered in 2025 and were blocklisted through 30 April 2025, we estimate that 7.3 million of them (88%) were “bulk registrations.” Prior research has documented that malicious name registration campaigns often involve registrars that offer bulk registration options.[^55][^56][^57][^58]

Under our methodology, domains are “bulk registered” if they were all blocklisted, and at least ten domains were registered through the same registrar with no more than ten minutes between consecutive registrations. Domains within these sets usually exhibit batch registration patterns. Starting with an initial set of “seed” RBL-listed domains, the researchers found an additional 80% more domains that were associated with the blocklisted ones. This “indicates that for every three newly registered malicious domains reported through RBL feeds, batch expansion (using conservative filtering) identifies an additional two neighboring domains.” The researchers stated that “the true rate is likely to be higher” since they excluded ”many valid batches” such as those containing more than 1,000 domains. The results “indicate that batch registrations are prevalent, significantly predict overall abuse rates, and are useful for pivoting and expanding from known malicious ‘seed’ domain sets, particularly in certain TLDs and registrar environments.”

We performed “associated domain checks” or “expansion analysis” of four TLDs, using blocklisted domains to point us to potentially associated domains. We obtained registration data for all the domains in these TLDs, based on the contents of their zone files at two points (30 July and 2 September 2025), and for all the blocklisted domains. Our criteria shared similarities with the ones used in the ICANN OCTO study. We considered domains to be associated when they shared the following characteristics:

1. At least one domain in the set was blocklisted for abuse, AND
2. the domains were created by the same registrar(s), AND
3. the domains were registered within a time-bound manner (typically less than 10 minutes between consecutive registrations), AND
4. the domains used the same hosting (same nameserver pair, and/or same IP address/A record), AND
5. the domains followed the same distinctive string pattern. These are lexical similarities often produced by domain generation algorithms. These include same string length, reoccurring or progressive characters or substrings, use of all digits, use of all letters, and use of hyphens.

We then performed manual validation of the data, examining every record for every domain. This allowed us to find and confirm certain registration patterns, some of which we describe below.

We observed one registrar processing more than 100 domains per minute for more than five hours. These were all algorithmically generated .BOND domains, consisting of meaningless strings of letters and numbers.

Twelve registrars accounted for more than 80% of the bulk-registered domains. The gTLD registrar with the most bulk registered domains was Gname.com Pte. Ltd. (IANA ID 1923), which registered 881,225 subsequently blocklisted domains in 4,221 batches.

### Sales Programs & Market Incentives
Volume-based discount programs and high-volume, low-margin sales strategies create strong commercial incentives for repeat bulk sales. Cybercriminals, who purchase domains in large quantities and rarely renew them, represent a large and reliable source of precisely this kind of demand.

The gTLD market is intensely competitive. The introduction of new, open gTLDs has increased the supply of domain names, leading to price wars and aggressive marketing. Some registrars and registry operators have adopted strategies that prioritize volume over quality, often at the expense of security.

The resulting social costs of cybercrime, however, including financial losses, business disruption, and eroded public trust, are borne by victims, businesses, and society at large. This is a classic negative externality that distorts the market and undermines the broader benefits of competition.

## Discussion and Conclusion
The findings of this report are clear: malicious registrations are a significant and growing problem in the gTLD market. Cybercriminals are exploiting the availability of cheap, disposable domain names to conduct large-scale malicious campaigns. The current system of detection and mitigation is insufficient, and the market incentives for registrars and registry operators to address this problem are weak or non-existent.

The concentration of malicious registrations in certain TLDs and at certain registrars suggests that targeted interventions could be effective. Registry operators and registrars have the data and the tools to identify and mitigate abusive registrations, but they often lack the incentive to do so.

Improvements in domain name policies and practices are needed to reduce cybercriminals’ access to domains while supporting legitimate market growth. Additional new, open gTLDs will be introduced in the coming year and beyond. Absent more effective controls, the increase in competition and domain name supply will likely exacerbate the current situation, shifting greater costs and harm to the public.

## Sponsors
[List of sponsors]

## Acknowledgements
[List of acknowledgements]

## About Interisle Consulting Group
[Description of Interisle Consulting Group]

## About the Authors
[Description of the authors]

## Methodology
[Description of the methodology]

## Endnotes
[^1]: [Endnote content]
[^2]: [Endnote content]
[^3]: [Endnote content]
[^4]: [Endnote content]
[^5]: [Endnote content]
[^6]: [Endnote content]
[^7]: [Endnote content]
[^8]: [Endnote content]
[^9]: [Endnote content]
[^10]: [Endnote content]
[^11]: [Endnote content]
[^12]: [Endnote content]
[^13]: [Endnote content]
[^14]: [Endnote content]
[^15]: [Endnote content]
[^16]: [Endnote content]
[^17]: [Endnote content]
[^18]: [Endnote content]
[^19]: [Endnote content]
[^20]: [Endnote content]
[^21]: [Endnote content]
[^22]: [Endnote content]
[^23]: [Endnote content]
[^24]: [Endnote content]
[^25]: [Endnote content]
[^26]: [Endnote content]
[^27]: [Endnote content]
[^28]: [Endnote content]
[^29]: [Endnote content]
[^30]: [Endnote content]
[^31]: [Endnote content]
[^32]: [Endnote content]
[^33]: [Endnote content]
[^34]: [Endnote content]
[^35]: [Endnote content]
[^36]: [Endnote content]
[^37]: [Endnote content]
[^38]: [Endnote content]
[^39]: [Endnote content]
[^40]: [Endnote content]
[^41]: [Endnote content]
[^42]: [Endnote content]
[^43]: [Endnote content]
[^44]: [Endnote content]
[^45]: [Endnote content]
[^46]: [Endnote content]
[^47]: [Endnote content]
[^48]: [Endnote content]
[^49]: [Endnote content]
[^50]: [Endnote content]
[^51]: [Endnote content]
[^52]: [Endnote content]
[^53]: [Endnote content]
[^54]: [Endnote content]
[^55]: [Endnote content]
[^56]: [Endnote content]
[^57]: [Endnote content]
[^58]: [Endnote content]

---

ally share lexical/string characteristics of hundreds of “generic,” open TLDs by ICANN in 2001
and the same nameserver set (i.e., the same per registrar- and 2012 created an increased supply of domains. The
nameserver combination). The domains in a bulk set are operators of new gTLDs have often competed on the
often in the same gTLD, but sometimes bad actors register basis of price, offering cheap domains in order to
related domains across several TLDs at the same time. establish market share. Those strategies have regularly
When examined, the domains in batches tend to be (but not always) attracted abusive registrations, and
obviously related to each other. Our method under-counts the relationship between low pricing and abuse is well
the size and occurrence of bulk registrations, because it documented,59, 60, 61 A recent ICANN-sponsored study found
counts only domains that were blocklisted. As expansion that each dollar reduction in registration fees corresponds
analyses show, there are often more registered domains in to a 49% increase in malicious domains.62 The .UK registry
the bulk set that were not listed by blocklist providers. operator, Nominet, recently acknowledged this issue when
Our method also fails to capture smaller (lower volume) launching a new growth initiative: “Mindful of trust in the
batch registrations, and those spaced out over longer .UK domain, and experience of registries elsewhere, we do
time periods. not want to support unsustainable registrations that spike
initially but then fall away or fuel domain abuse.”63
The largest set we found consisted of 10,848 blocklisted
domains created by registrar GMO Internet Group, The market will become even more competitive when
Inc. (IANA ID 49) from 18:02:02 to 23:20:38 UTC on 25 ICANN introduces more open new gTLDs in 2027 and
November 2025 – a sustained registration rate of 106 beyond.64 All else equal, the increase in domain supply and
INTERISLE CONSULTING GROUP MALICIOUS REGISTRATIONS IN THE DOMAIN NAME MARKET 25

Above: discounted first-year retail prices at registrar Porkbun.com. Some are discounted 90% off the stated retail price.
the entry of additional competitors can be expected to As a result, .COM grew by 4.5 million domains in 2025,
intensify price competition, particularly in segments where .COM’s most significant growth in several years. Most of the
buyers are price-sensitive and view products as largely growth in the gTLD market came from the open new gTLD
interchangeable, as criminals do. sector, which grew by 11 million domains in 2025.
A variety of open gTLDs have been available at retail prices Some registrars routinely keep their prices low and sell at
below US$2.00, due to registry wholesale promotions, low margins as a customer acquisition strategy. Sometimes
registrar-funded discounts, or other deep-discount pricing registrars may sell domains for below the wholesale price
strategies. Some domains are sold for as little as US$0.49. they pay the registry by cross-subsidizing the low price
with sales of other products. A cheap domain name can
How are these low prices offered? Registry operators
function as a “loss leader” that entices customers to buy a
typically drive sales by offering discounts on the wholesale
broader set of higher-margin services from the registrar,
price they charge registrars for new registrations (domain
such as web hosting and email accounts.
creates), or by offering rebates when a registrar meets
sales or growth targets. Registrars may then pass those While low retail prices are apparent on registrars’ web
savings to registrants through lower retail prices. Registries sites, the details and terms of the sales and marketing
and registrars often implement such programs by programs behind those prices are generally not made
discounting the first year of a domain registration. Then, public. Registries offer them to their registrar distribution
when the domain comes due for renewal at the end of its channels privately and sometimes under terms of business
first year, it renews at a higher price. The business logic confidentiality. Companies sometimes negotiate special
is that a low introductory price can expand the customer deals between themselves, such as to place a registry’s
base, and that some percentage of the domains will renew gTLD high up in a registrar’s web site display and search
at a higher price, creating repeatable revenue in the future. results. Some registrars offer bulk discounts, which may
or may not be advertised, and may give special prices
For example, after several years of relatively flat sales
to certain resellers and end customers who buy large
in .COM, Verisign pursued growth in 2025 by offering a
numbers of domains.66 It is therefore difficult for outside
discount program, which saw some registrars sell .COM
observers to understand exactly what incentives are being
domains to customers at retail for less than half of .COM’s
offered and subsidized by whom.
usual $10.26 wholesale price. Verisign saw evidence of
“registrars shifting towards customer acquisition” and These low-margin pricing volume discount strategies
“more registrar engagement” with its marketing programs.65 can be commercially rational, but they also create risk
INTERISLE CONSULTING GROUP MALICIOUS REGISTRATIONS IN THE DOMAIN NAME MARKET 26

and can distort incentives. Cybercriminals treat domain The persistence and scale of bulk registrations made by
names as disposable commodities: they buy them cheaply bad actors suggest the following:
and do not renew them.
1. Some registrars are apparently benefitting
When selling domains to bad actors, the registrar and commercially by selling large numbers of very
registry operator will never realize revenue from renewals, low-priced domains to abusive registrants. If
making criminals perhaps the lowest-margin customers those sales consistently produced losses, rational
in the market. However, because cybercriminals require a providers would adjust their pricing and sales
continuous supply of new domains and purchase them in strategy to limit their commercial exposure.
large volumes, they represent a large and reliable source
2. Many bad actors appear to be using acceptable,
of repeat demand.
payment instruments to pay for their
The high volumes or high proportions of abusive registrations, rather than stolen credit cards.
registrations associated with certain registry and registrar If cybercriminals were mostly paying for domains
operators suggests that some of them may be deriving with stolen credit cards, registrars would adjust
commercial benefit from sales to criminals. Even when their practices to prevent losses and credit card
abusive registrations generate little or no profit or other charge-backs. Registrars would also delete many
direct commercial benefit, registries and registrars may more domains in the Add Grace Period (AGP), which
still have an economic incentive to tolerate them. As long allows them to get refunds from the registries and
as the cost of carrying these domains remains low or from ICANN. However, the numbers of domains
commercially neutral, and deterring them is more costly or deleted in AGP appear to be far below the limits
risks losing higher-margin legitimate customers, tolerating that set off excess deletion penalties under
them can still be commercially rational. ICANN policy. Payments made by cryptocurrency or
gift cards may pass muster. In any case, it appears
While cybercriminals and certain registrars and registry
that registrars are often receiving real funds from
operators may benefit, the costs of cybercrime facilitated
cybercriminals.
by abusive registrations fall on victims, businesses, and
society at large. In economic terms this is a classic negative How cybercriminals pay for their domains, and when and
externality, where the parties who benefit from the how those payments are passing fraud checks,are areas
transaction do not bear the full costs they create. that deserve further study.
INTERISLE CONSULTING GROUP MALICIOUS REGISTRATIONS IN THE DOMAIN NAME MARKET 27

Discussion and Conclusion
The data presented in this report makes clear that a benefits from an activity, but imposes costs on unrelated
significant portion of the domain name market is driven third parties. Here cybercriminals and certain registrars
by registrations made by malicious actors. Malicious and registry operators benefit, while the costs are imposed
registrations accounted for at least 10 percent—and on victims of cybercrime and the public in general, who
possibly 20 percent—of new sales in the gTLD market suffer financial losses, business and personal disruptions,
in 2025. The number of blocklisted registrations even and an erosion of public trust.
eclipsed net gTLD market growth in the months of January,
Importantly, however, abuse on this scale is not inevitable.
February, and May 2025.
Associated domain name check studies show that abuse
While abuse was widespread, abusive registrations were detection and mitigation can be made more efficient
notably concentrated at a small number of registrars. Just and effective. Sales strategies, provider practices, and
five registrars were responsible for half of all blocklisted abuse-mitigation choices can materially affect whether
domains created in 2025. Thirteen gTLDs saw more than growth is driven by legitimate demand or by cybercriminal
half of their new registrations flagged for abuse. registrations. Better contractually binding and enforceable
policies are needed.
The case studies of .LOAN, .PINK, .BOND, and .GIFT
illustrate how professional criminal organizations
exploited the market. These actors registered domains
in massive batches—totaling hundreds of thousands of
domains—across multiple registrars and TLDs, using them
for phishing, malware distribution, and large-scale fraud.
The exceptionally low renewal rates that followed, as low
as 0.5%, confirm that these domains were not renewed
and did not represent legitimate usage. In contrast, some
TLDs and registrars grew without attracting outsized abuse,
showing that the choices that providers make do matter.
How cybercriminals pay for their domains, and when and
how payments are passing fraud checks, are areas that
deserve further study.
Bulk registrations, low prices, and minimal deterrents
make domains easily exploitable tools for cybercriminals.
While sales and incentive programs are intended to drive
growth and market share, they can also incentivize sales to
high-volume, repeat customers such as cybercriminals.
Some registrars and registries appear to derive commercial
value from criminal demand, even when selling at deeply
discounted prices.
In economic terms, this is a sign of a market out of
equilibrium with distorted incentives. It is also evidence
of a classic negative externality: a situation in which a party
INTERISLE CONSULTING GROUP MALICIOUS REGISTRATIONS IN THE DOMAIN NAME MARKET 28

Sponsors
We gratefully acknowledge the sponsors of this project
who contributed threat intelligence data, financial support,
or in-kind assistance. All aspects of the study, including the
methodology and analysis, were conducted independently
by Interisle. The findings and conclusions presented in this
report are those of Interisle alone and were not influenced
by the sponsors.
The Anti-Phishing Working Group (APWG)
Coalition for Online Accountability (COA)
DomainTools
Meta
Spamhaus
SURBL
A list of organizations that support Interisle’s data
collection activities, which we use for this and other
projects can be found at:
https://www.cybercrimeinfocenter.org/contributors
INTERISLE CONSULTING GROUP MALICIOUS REGISTRATIONS IN THE DOMAIN NAME MARKET 29

Acknowledgements
The authors wish to thank the following:
• Renée Burton and Zach Edwards of Infoblox, for their
insights about FUNNULL.
• April Lorenzen and Zetalytics, for access
to passive DNS data.
• Rod Rasmussen, Lyman Chapin, and Dave Piscitello,
for their constructive comments as the report was in draft.
• The teams at Spamhaus and SURBL, for their insights
about blocklists.
• Pete Strutt at Common Co., for design services.
• The researchers whose work is cited in this report,
and to the security professionals and members of law
enforcement who fight cybercrime.
About Interisle Consulting Group
Interisle’s principal consultants are experienced practitioners with extensive track records in industry
and academia and world-class expertise in business and technology strategy, Internet technologies
and governance, financial industry applications, and software design. For more about Interisle, please
visit: www.interisle.net
IINNTTEERRIISSLLEE CCOONNSSUULLTTIINNGG GGRROOUUPP MMAALLIICCIIOOUUSS RREEGGIISSTTRRAATTIIOONNSS IINN TTHHEE DDOOMMAAIINN NNAAMMEE MMAARRKKEETT 3300

About the Authors
Greg Aaron is an internationally recognized authority on Telecommunications and Information Administration
the use of domain names for cybercrime, and is an expert (NTIA). While in government, she was co-author of the U.S.
on DNS policy, domain registry operations, and related policy statement and related agreements that globalized
intellectual property issues. He has performed complex management of the Internet’s Domain Name System (DNS)
investigations and due diligence projects with industry, and led to the creation of the Internet Corporation for
law enforcement, law firms, and security researchers to Assigned Names and Numbers (ICANN). Ms. Rose served
address phishing, intellectual property violations, malware, on the board of Netnod, one of Europe’s most recognized
spam, and botnet cases, and has advised governments and Internet exchange point operators, and on the .US domain
online commerce providers. Mr. Aaron is Senior Research stakeholder advisory committee. She currently serves
Fellow for the Anti-Phishing Working Group, and is a on the advisory panel for AfChix, an African organization
member of M3AAWG, the Messaging, Malware and Mobile dedicated to advancing women in tech.
Anti-Abuse Working Group. As a member of ICANN’s
Security and Stability Advisory Committee (SSAC), he
advises the international community regarding the domain Dr. Colin Strutt has published and spoken extensively
name and numbering system that makes the Internet on networking technology, name collisions, enterprise
function. He has participated in numerous ICANN working management, eBusiness, and scenario planning, and
groups, including several devoted to anti-abuse and privacy has represented the interests of DEC, Compaq, and the
topics such as the EU’s General Data Protection Regulation Financial Services Technology Consortium in national
(GDPR). He was the senior industry expert on a team that and international industry standards bodies. He holds
evaluated the policy and technical qualifications of more six patents on enterprise management technology, and
than one thousand new gTLD applications to ICANN in has more than forty years of direct experience with
2012-2013. He has created products and services used by information technology as a developer, architect, and
organizations to discover and track Internet-based threats, consultant; his recent work includes the design and
and has managed large top-level domains, including .INFO, operation of a regional public safety network, providing
.ME, and .IN. Mr. Aaron is a magna cum laude graduate of technical expertise relating to patents, and analysis of
the University of Pennsylvania. world-wide Internet use. Most recently, he has been
involved in the cybercrime data analysis for the Cybercrime
Information Center and the related Interisle reports. Dr.
Karen Rose is an internationally recognized expert in Strutt holds a B.A. (with First Class Honours) and a Ph.D. in
Internet policy, technology, and development with over Computer Science from Essex University (UK).
25 years of experience in the field. Since 2017, she has
consulted on a range of Internet policy and digital economy
issues. Ms. Rose was previously a senior executive at the
Internet Society (ISOC) where she led the organization’s
work to expand Internet infrastructure and related policy
capacity around the world, as well as research on emerging
Internet issues. Prior to that, she served at the U.S. Federal
Communications Commission (FCC) and the National
INTERISLE CONSULTING GROUP MALICIOUS REGISTRATIONS IN THE DOMAIN NAME MARKET 31

Methodology
All aspects of the study, including the methodology and providers, registrars, and services are most heavily used
analysis, were conducted independently by Interisle. The and exploited by cybercriminals.
findings and conclusions presented in this report are those of
ICANN takes a similar approach with its Metrica abuse
Interisle alone and were not influenced by the sponsors.
measurement system. ICANN notes: “We believe that it
is beneficial to collect the same DNS abuse data that is
reported to industry and Internet users. Security systems
How does Interisle identify abusive
such as anti-spam or anti-malware gateways or firewalls
domain names?
that protect billions of users incorporate these data into
their DNS abuse mitigation measures. Domain Metrica
We begin with data from prominent Reputation Block Lists thus reflects how the users and network operations
(RBLs). These contain domain names and/or the URLs of communities see the domain name ecosystem through the
known phishing pages, malware, and web pages that host lens of reported DNS abuse data.”67
dangerous or unwanted content. The RBLs we use are
provided by professional security threat-reporting sources,
and are used to protect billions of user accounts across
What blocklists does Interisle use?
the world. These providers continually add and remove
domains and URLs from these lists, according to their
own criteria.
The APWG phishing feed (phishing; high-confidence only),
RBLs are widely used as a defense measure. Internet OpenPhish (phishing), PhishTank (phishing; confirmed
service providers, email providers, Web browser providers, phishing only), Spamhaus DBL (malware, phishing, and
DNS resolvers, and other organizations use these RBLs other (untagged) malicious/risky domains), SURBL
to block access to (and traffic and email from) these (malware, phishing, botnet C&C, and other (untagged)
domains and URLs, protecting their users from online malicious/risky domains), URLHaus (malware), and
threats. Pretty much every user of the Internet is protected Malware Patrol (malware). See below for the details. Each
by RBLs, including the users of corporate and university provider describes the general details of their processes.
networks, ISPs, and public wifi networks and DNS
For this study we also included domains registered in
resolvers. Web browsers such as Chrome, Safari, and Edge
2025 for use in notable cybercriminal campaigns. Most of
use reputation blocklists to prevent users from visiting
these domains were blocklisted by the RBLs we monitor,
malicious sites. Most e-mail providers use blocklists to
but some were not and we added them to our list of
protect email accounts.
maliciously registered domains. The sources are:
This data provides a practical measurement of what is
• Funnull phishing and cryptocurrency scam
happening in the “real world,” the Internet ecosystem that
campaign: list provided by the U.S. Federal Bureau
uses the DNS. It shows what domain names are being
of Investigation (FBI): https://www.ic3.gov/CSA/2025/
blocked—the domains that professional anti-abuse sources
Complete_List_of_Domains_Attributed_to_Funnull.zip
have identified as harmful, and what domains
are being blocked by security administrators at private • LabHost “Phishing-as-a-Service” (PhaaS) case: list
and public networks and services around the world. provided by the U.S. Federal Bureau of Investigation
Interisle uses this data to identify abusive domain (FBI): https://www.ic3.gov/CSA/2025/LabHost_
registration and usage trends, such as what hosting Domains.csv
INTERISLE CONSULTING GROUP MALICIOUS REGISTRATIONS IN THE DOMAIN NAME MARKET 32

• Lumma malware case: domains seized as a result of review or appeal process and the ability to redress false-
Microsoft’s filings in U.S. federal court cases 1:25-cv- positives. Academic literature and the extent of commercial
06493-MHC (injunction 12 December 2025) and use indicate that the false-positive rates are quite low
1:25-cv-02695-MHC (injunction 12 June 2025), and among the lists we have chosen.
https://www.cisa.gov/sites/default/files/2025-05/
Our choices of blocklists, and how we use them, follow
AA25-141B.stix_.xml
the considerations described in the “RBL Evaluation
• Lighthouse “Phishing-as-a-Service” (PhaaS) case: Methodology” paper by ICANN’s Office of the CTO, which is
domains seized as a result of Google’s filings in U.S. a useful guide.
federal court case 1:25-cv-09421-LAK (injunction
We use more blocklists than some other organizations
December 1, 2025)
do. There is usually only a small overlap between the
• RaccoonO365 “Phishing-as-a-Service” (PhaaS) case: domains that one blocklistlist finds versus another. By
domains seized as a result of Microsoft’s filings in U.S. using more feeds, we gain a better, more comprehensive
federal court cases 1:25-cv-07111-JSR (injunction 16 understanding of what’s happening out on the Internet. For
September 2025) more about this, see below.
• Toll road phishing campaign: list provided by Netcraft.
https://github.com/netcraftcom/public-iocs/blob/ Does Interisle’s system find all
main/state-tax-road-toll-smishing-IOCs.csv
instances of abuse?
• PDF phishing campaign: list provided by Zimperium
and Netcraft. https://github.com/Zimperium/IOC/
No. The blocklist providers we use do not claim to detect or
blob/master/2025-01-PDF-Phishing/urls.csv
list all the abusive activity happening on the Internet. The
• Hotel phishing campaign: list provided by Netcraft: data we have is only a subset of the abuse problem. Our
https://www.netcraft.com/blog/thousands-of- numbers are a floor, and the number of domain names
domains-target-hotel-guests-in-massive-phishing- being used for abusive purposes is higher. We have found
campaign and https://github.com/netcraftcom/ that our data provides reliable indicators of trends, and of
public-iocs/blob/main/2025-11%20hotel%20 where abuse is concentrated.
phishing%20IOCs.csv
• Cryptocurrency scam: list provided by Silent Push
What other data does
• Hiragana IDN phishing campaign: List provided by
Interisle collect?
Netcraft: https://github.com/netcraftcom/public-iocs/
blob/main/hiragana-%E3%82%93-IOCs.csv
Infoblox provided Interisle with data about some FUNNULL We gather data that gives context to blocklist data, and
domain names. These were used to aid our case study helps us understand where abuse is taking place. All of this
analyses, but were not added to our blocklist counts. data is publicly available. Among other things, we collect:
• DNS query data. This tells us things such as what IP
address a domain is on, and what nameservers a
How does Interisle choose
domain name is using.
what blocklists to use?
• Domain registration data. This is the authoritative
information about when a domain name was
The blocklist providers we use meet important criteria registered, the name of the registrar and its IANA ID
including very low false-positive rates, coverage of number, the domain’s contact data, and more. We
relevant kinds of abuse, and wide adoption by companies, collect it from domain registries and registrars using
governments, and academia. Each RBL also provides a RDAP and WHOIS.
INTERISLE CONSULTING GROUP MALICIOUS REGISTRATIONS IN THE DOMAIN NAME MARKET 33

• gTLD zone files we count only the second level domain (web.app), and
once only, when reporting domain totals for a TLD or
• Passive DNS to find the “first observed “ dates of
registrar portfolio.
domains.
Some RBL providers add a domain to the blocklist and then
• Feed-specific metadata. Some of our feeds provide
remove it from the blocklist after a certain time, sometimes
additional information, such as the type of abuse a
because the domain was suspended. In this report,
domain or IP address is associated with, the brand
Interisle counts how many and which domains were added
that is impersonated in a phishing attack, or a
to the lists, i.e. how many domains were identified as
malware family or type.
problems.
How does Interisle process and
How does Interisle determine the
count the data?
number of domains in a TLD or
at a registrar?
Blocklist providers continually add and remove domains
and URLs from their lists, according to their own criteria.
Our collection system collects updated data from each We determine the numbers in each gTLD, and sponsored
blocklist provider several times per day, and de-duplicates by each registrar, using domain counts from ICANN’s
domain names (both within a list and across lists) as part official registry reports. Interisle uses registrar IANA ID
of processing. numbers to distinguish registrars.
Some blocklists provide URLs. We only count a domain ICANN and the NetBeacon Institute (services provided by
name once, irrespective of how many host names or URLs KOR Labs) use the number of domain names found in zone
have been reported on that domain name. files. Zone files always contain fewer domains than the
registry itself, sometimes by 6% or more, because expired
A domain name that we extract from any blocklist will
domains pending deletion are removed from the zone file.
cause the domain name to be counted only once when
Domains suspended for abuse by registrars and registries
we calculate unique domain abuse totals. If a domain is
(via ClientHold and ServerHold) are also removed from
listed for two or more types of abuse, that domain will be
the zone file. This can increase the difference between
counted (again, once) in each relevant abuse category.
domains-in-registry and domains-in-zone.
For example, if one blocklist identifies a domain name as
a malware domain and a second identifies that domain Verisign tends to report the number of domains in the
as a phishing domain, and that domain was not listed .COM and .NET registries, which it operates. Otherwise
before, then: Verisign uses zone file size to calculate gTLD renewal
rates for the other TLD publishes in its Domain Name
• The total unique domain count is increased by one,
Industry Brief reports and gTLD registration and renewal
• The cumulative abuse count is increased by one, trend dashboards.
• The malware domain count is increased by one, and The above differences can affect the numbers reported
by various organizations, and can affect domain abuse
• The phishing domain count is increased by one.
scoring of registrars and TLDs. For example, for December
2025, Verisign reported 161 million domains in .COM in its
Only unique domains are counted toward the total industry brief, but 164.6 million in its ICANN registry report.
reported DNS abuse counts in a TLD or registrar portfolio.
Subdomain providers offer third-level domains, such as
example.web.app, and many such third-level domains are
used for phishing and other malicious activities. However,
INTERISLE CONSULTING GROUP MALICIOUS REGISTRATIONS IN THE DOMAIN NAME MARKET 34

is not reflected specifically in the ICANN reports.
How does Interisle calculate
(Registries have the detailed information about exactly
renewal rates?
which domains were deleted in the 45-day Autorenew
Grace Period.) This factor may make our renewal
We use the registration numbers in the official monthly rate calculations turn out slightly lower than what a
ICANN registry reports to calculate renewal rates. Those registry later reports publicly.
reports contain:
2. Instead of domains in the registry (which is what the
• the number of domains in each gTLD registry at the ICANN reports contain), some parties use zone file
end of each month, and size as a proxy for the size of the TLD. As noted above,
zone files always contain fewer domains than the
• how many domains were sponsored (DUM, or
registry contains.
“domains under management”), registered (created),
renewed, and deleted by each registrar in each gTLD
each month.
How does Interisle determine if
a domain has been “maliciously
We use industry-standard methods to calculate the following:
registered?”
• New Registrations: The number of domain names
added (Created) in a gTLD during a selected period.
A malicious registration is a domain name that we
In the ICANN reports these are called net-adds. This
determined was registered by a bad actor, for the purpose
includes domains created for more than a one-year
of carrying out malicious activity. A compromised domain
term. We do not count domains added and then
is owned by a legitimate registrant, but a criminal has
deleted in the Add Grace Period.
taken control of it by hacking or account compromise
• Renewals: The number of domain names in a in order to carry out malicious activity. Distinguishing
selected period that were renewed (for any length between the two is important. By identifying malicious
of time). In the ICANN reports these are called registrations, we can see where and how criminals
net-renews. purchase domain names. Also, malicious registrations can
be safely suspended by a domain name registry operator
• Renewal rate: The percentage of domain names
or registrar – the suspension will not harm anyone but
renewed during the selected time period. This is
the criminal. In contrast, suspending a compromised
calculated as the number of domain names that are
domain can harm legitimate users, preventing the innocent
renewed divided by the number of domains that
registrant’s web site and email from functioning. Those
were eligible for renewal (which is the number of
cases should be reported to the hosting provider and the
domains created one year prior (net-adds), plus the
registrant, who can secure the account and remove the
number of domains renewed one year prior). Rates
harmful activity at the source.
are calculated with the simplifying assumption that
all domain names expire and are eligible to renew We use multiple criteria to determine if a domain flagged
each year. Multi-year registrations can cause the by a blocklist has been maliciously registered. The most
renewal percentage to be very slightly overstated. important are:
The number of Restored domains is negligible, and so
1. Domain age. We look at the number of days between
we have ignored that effect.
the domain’s registration date and the time the
Two other factors can make our renewal rate calculations domain was blocklisted. (Or if registration date is not
vary slightly from those published by other sources: available via RDAP or WHOIS, the time between the
domain was first observed in a passive DNS query
1. Renewal rates are not fully measurable until 45 days
and when the domain is blocklisted.) We consider
after the end of a reporting period, and that factor
INTERISLE CONSULTING GROUP MALICIOUS REGISTRATIONS IN THE DOMAIN NAME MARKET 35

domains blocklisted within 90 days of registration and the same nameserver set (registrar-nameserver
to be malicious. Studies indicate that such domains combination), and we confirm the presence of those
are usually too new to have been compromised, and features for large batches. The domains in a bulk set
that a high percentage of maliciously registered are usually in the same gTLD, but sometimes bad actors
phishing domains tend to be used within days of register domains across several TLDs at the same time.
registration. This method excludes some maliciously
Our method under-counts the size and occurrence of
registered domains that are “aged” by bad actors (by
bulk registrations, because it counts only domains that
not using them for more than 90 days) in an attempt
were blocklisted. There may have been more registered
to improve domain reputation. Other researchers
domains in the bulk set, but the blocklist providers did
have considered domains as malicious if they were
not list them all. Our method also fails to capture smaller
blocklisted within a longer 150-day period after
(lower volume) batch registrations, and those spaced out
registration.
over longer time periods.
2. The composition of the domain name. We search
Note that bulk registrations and the concept of associated
listed domains for tell-tale strings that indicate
domain checks under policy-making consideration at
malicious use. These include strings designed to
ICANN are two related concepts. The domains in a bulk
mislead users (login, security, etc.), and brand names
registration set are by definition related to each other
that are the targets of phishing attacks (citibank,
and were presumably registered by the same party. A
whatsapp, etc.). We also search for close misspellings
competently performed associated domain check by the
and variations of these terms, which criminals often
registrar should uncover all the domains in a bulk set we
register to evade simple matching measures. Our tell-
identified, plus perhaps others.
tale strings lists include strings that we have “observed
in the wild,” i.e. seen used in confirmed attacks. In research about malicious bulk registrations and
associated domain discovery, researchers in ICANN’s Office
3. We look for clear evidence of common control and
of the CTO found that “batch registrations are prevalent,
usage, such as batches of domains registered at
significantly predict overall abuse rates, and are useful
the same time at the same registrar, delegated to
for pivoting and expanding from known malicious ‘seed’
the same nameserver pair, and for algorithmically
domain sets.”
generated domain names that follow patterns, such
as sequences of numbers and letters. (See “bulk
registrations” below.)
What kinds of abuse are counted
These methods share similarities with those used by other in this study?
researchers, such as the COMAR and MalCom methods
used by KOR Labs, the service provider to the NetBeacon
We counted a domain if it was included on a blocklist, and
Institute. Their and our calculations for malicious phishing
was a unique second-level gTLD domain.
registrations have historically been within a few percentage
points of each other. Some blocklists are dedicated to listing only domains and
URLs about a specific category of abuse. (For example,
PhishTank tracks phishing exclusively). Other blocklists will
How does Interisle define malicious
list domains associated with several kinds of abuse, and
“bulk registrations”?
will tag specific domains to certain abuse types.
Some domains appear on those blocklists without being
We define a set of domains to be bulk registered if the
specifically tagged with an abuse type by the blocklist
domains were blocklisted and at least ten domains were
provider. These categorization gaps are often the result of
registered through the same registrar with no more than
the large amount of abuse and domains being processed
ten minutes between consecutive registrations. Domains
in real-time by blocklist providers, and the multiplicity of
within these sets usually share lexical/string characteristics,
INTERISLE CONSULTING GROUP MALICIOUS REGISTRATIONS IN THE DOMAIN NAME MARKET 36

signals used in their reputation scoring systems. Some that spammers want potential victims to go to. Here spam
domains may be tagged by a blocklist provider for a is a delivery method, not the abuse being advertised.
specific type of abuse such as phishing. Conversely, some “Spam” therefore does not always describe why these
domains used for phishing or malware are not tagged as domains are problems and get blocklisted. The Budapest
such by blocklist providers such as SURBL and Spamhaus. Convention on Cybercrime (the major international treaty
designed to address Internet crime) produced a guide to
All gTLD domain name registrars state in their terms of
illustrate the multi-functional criminal use of spam.
service that domains cannot be used for illegal activities.
Some registrars suspend domains that are outside of It is a misconception that blocklist providers such as
ICANN’s definition. Spamhaus and SURBL focus entirely on spam, either as
the primary detection method, or that they curate their
lists to be used for email filtering exclusively. Rather, they
Why are some domains blocklisted
focus on whether a domain may be malicious or risky, and
without a specific abuse type?
their lists are used in a variety of protective systems. When
What is a “spam” domain? describing whether to list a domain, Spamhaus uses this
general methodology.
RBLs such SURBL and Spamhaus list domains that are used Some domains found by scanning spam messages are
for a variety of abusive purposes. These domains get listed used to perpetrate scams and frauds – investment and
because the RBL provider finds them risky and worthy cryptocurrency scams, romance and “pig butchering”
of blocking. Some of the domains on these RBLs are not scams, fake shops, scam casinos, advance fee fraud, and
tagged with a specific abuse type, as explained above. more. These types of frauds and scams resulted in the
Since some of those undifferentiated domains were found majority of cybercrime financial losses suffered in 2025.
in spam messages, and since that RBL may be used to filter Other blocklisted domains are used to operate other
email, some people colloquially call these “spam domains.” types of fraud, such as illegal pharmaceutical sites and
counterfeit product sales. These various scam, fraud,
However, “spam domains” is an often inapt term, and
and abuse domains are detected by various methods in
doesn’t explain why some domains are a problem and why
addition to email scanning.
they get blocklisted. Some of these “spam domains” are
actually scam and fraud domains. Blocklist providers presently do not tag domain listings
with specific “fraud and scam” abuse types, due to a lack of
Spam has been traditionally defined as “bulk, unsolicited
an industry-standard taxonomy, because of the diversity
email messages.” With a few exceptions, the sending of
and wide-ranging nature of scams and frauds, and because
bulk, unsolicited email messages violates the law in many
of the challenges of making such classifications on the fly
countries. However, there are two even bigger problems.
while processing large volumes of detections.
First, most spam messages are sent via criminal and
In the end, blocklist providers do not list all the domains they
duplicitous means: via botnets, via hijacked IP space, and
find in bulk unsolicited email. They list only those domains
using fictitious (forged) business names and identities to
that they judge to be unacceptable risks to Internet users.
obtain hosting and sending resources. Reputable senders
follow best practices, do not send unsolicited messages, do Interisle therefore counts domains as phishing or malware
not have their domains blocklisted, and do not advertise when a list is devoted exclusively to such an abuse type,
harmful content. or when a multi-abuse list such as SURBL or Spamhaus
specifically tags domains for those abuse types. When
Second, domains that are advertised in unsolicited bulk
looking at the overall use of domain names in this report,
email are used for various criminal purposes. Blocklist
Interisle counts all of the domains that Spamhaus and
providers such as SURBL and Spamhaus find some
SURBL list, such as when Interisle reports how many
malicious domain names by examining what is advertised
domains were blocklisted in a TLD for all kinds of abuse.
in the body of spam messages. These are the destinations
INTERISLE CONSULTING GROUP MALICIOUS REGISTRATIONS IN THE DOMAIN NAME MARKET 37

How do Interisle’s methods differ  depending upon how the data is selected and presented.
from those used by ICANN Metrica  All three organizations do some of the basics similarly.
All three place an emphasis on feed trustworthiness and
and the NetBeacon Institute?
reliability, all three gather a range of associated data such
  as domain registration records, and all de-duplicate their
The main differences are that: lists to report about unique second-level domain names.
They use some similar methods to determine which
•  Interisle uses more sources, consumes more data,
domains were maliciously registered versus compromised.
and therefore becomes aware of more blocklisted
To learn about their methodologies, please see: ICANN
domain names.
Metrica FAQ and the NetBeacon Institute methodology
•  The organizations count and report some things
(provided by KOR Labs).
differently.
Here are the data sources that each organization uses,
These differences are important to understand, because
and how many domains each source listed over the
different conclusions can be gained (or obscured)
course of a year:
NUMBER OF UNIQUE
DOMAINS LISTED
| DATA      | ABUSE TYPES   | BY THIS SOURCE   |           | ICANN   | NETBEACON  |
| --------- | ------------- | ---------------- | --------- | ------- | ---------- |
| SOURCES   | REPORTED      | IN 2025          | INTERISLE | METRICA |  INSTITUTE |
| APWG      | phishing      | 207,812          |           |         |            |
| OpenPhish | phishing      | 95,412           |           |         |            |
PhishTank
|     | phishing | 100,097 |     |     |     |
| --- | -------- | ------- | --- | --- | --- |
WMC Global
|     | phishing | (unknown) |     |     |     |
| --- | -------- | --------- | --- | --- | --- |
PhishFeed
malware, phishing, botnet
Spamhaus
|     | C&C, other (untagged)  | 9,773,569 |     |     |     |
| --- | ---------------------- | --------- | --- | --- | --- |
DBL
malicious/risky domains
malware, phishing, domains
SURBL
|     | other (untagged) malicious/ | 6,536,604 |     |     |     |
| --- | --------------------------- | --------- | --- | --- | --- |
risky domains
| URLHaus* | malware | 11,503 |     |     |     |
| -------- | ------- | ------ | --- | --- | --- |
Risky domains found in
| Invaluement |     | 183,107 |     |     |     |
| ----------- | --- | ------- | --- | --- | --- |
bodies of spam messages
Malware
|     | Malware, botnet C&C | 17,042 |     |     |     |
| --- | ------------------- | ------ | --- | --- | --- |
Patrol
| Total number of sources |     |     | 8   | 6   | 4   |
| ----------------------- | --- | --- | --- | --- | --- |
Total number of unique domains listed in 2025 by sources used 14,855,456 < 9,831,489** 375,311
* URLhaus data is now also incorporated into the Spamhaus DBL
** See below about use of SURBL and Spamhaus
INTERISLE CONSULTING GROUP MALICIOUS REGISTRATIONS IN THE DOMAIN NAME MARKET    38

There is some overlap in the domains that the above and registrars. As many researchers have documented,
sources list. And each RBL lists some domains that are not these spikes and movements often last less than four
found on any of the others. months, and some registrars display evidence of malicious
batch registrations over short time periods only, as bad
actors carry out malicious campaigns. Interisle therefore
Differences in Total Domains
publishes unredacted statistics as a matter of transparency,
Identified and to reflect what happened where.
As illustrated above, NetBeacon uses far fewer sources
Differences Counting Abuse
than Interisle, and those sources list far fewer total
domains than Interisle’s data sources. Interisle’s study
set contains almost forty times as many domains as ICANN Metrica subscribes to the SURBL and Spamhaus
NetBeacon’s. lists, but only counts a subset of the domains on those
lists. Metrica counts only those domains that SURBL and
Interisle and ICANN Metrica use multiple sources to learn
Spamhaus specifically tag for phishing, malware, and
about each type of abuse. In contrast, NetBeacon uses
botnet C&C. Metrica does not count domains that SURBL
three sources of phishing data, and only one source of
and Spamhaus do not specifically attribute to those abuse
malware data. Because NetBeacon uses fewer sources that
types. ICANN Metrica does not count those domains
detect far fewer domains, NetBeacon’s TLD and registrar
because ICANN’s contractual definition of DNS just
domain counts and scores are significantly lower than
encompasses malware, botnets, phishing, and domains
Interisle’s and ICANN Metrica’s.
used to send email advertising those, and the last category
For example, for the November 2025 time period: is not tagged or differentiated in the feeds.
NetBeacon found 28,076 phishing domains, while Interisle When Interisle studies particular abuse types, Interisle
found 299,369 – more than ten times as many. counts domains as phishing or malware when SURBL
NetBeacon reported that the .ICU TLD had 554 newly or Spamhaus specifically tag domains for those abuse
observed malicious domains (phishing + malware). Interisle types. In this report, Interisle counts all of the domains
found that .ICU had 8,683 new phishing domains alone that Spamhaus and SURBL list because the domains have
in that period—more than 15 times what NetBeacon been blocklisted as risky, and the destinations and delivery
observed—plus additional domains flagged for malware mechanisms are often interrelated and problematic.
and other problems.
Differences in Choices of
Redactions and Transparency What to Display
NetBeacon redacts the names of some registrars and TLDs ICANN Metrica provides the number of domains that
that have high levels of abuse. NetBeacon describes this are currently on the blocklists that ICANN monitors, minus
choice as “a concept of consistency”: a TLD or registrar will domains that are on the blocklists but do not appear in the
only be listed if they appear in the top ten “for 4 or more of zone file. This is meant to represent how many domains
the last 6 months, otherwise they will be redacted.” may be active threats on a given day.
Interisle believes that such redactions are incompatible Domains are being added to and removed from the
with studying the nature of domain abuse. It is common for blocklists each day. Metrica’s method tends to obscure that
spikes of abuse to occur when bad actors register domains “churn” and does not give a picture of how many domains
in certain places, and for abuse to move between TLDs total are being listed over time. Also, certain providers
INTERISLE CONSULTING GROUP MALICIOUS REGISTRATIONS IN THE DOMAIN NAME MARKET 39

keep domains on their blocklists for longer periods of We believe that the number of domains being listed for
time than others. ICANN Metrica can therefore tend to abuse is a useful indicator for the amount of criminal
emphasize the effects of those blocklists, and can tend to activity in a particular place, and it can be an interesting
show that abuse is in a steady state: rough proxy for the amount of damage that is being done.
In contrast, Interisle might display the number of domains
that are added to the blocklists in a given time period. This
reveals spikes and lulls, and the cumulative number found
over time. Here’s a chart for the same TLD (.info) and same
time period as above.
PHISHING DOMAINS IN .INFO
7,000
6,000
5,000
4,000
3,000
2,000
1,000
0
3/12 3/14 3/16 3/18 3/20 3/22 3/24 3/26 3/28 3/30 4/1 4/3 4/5 4/7
2026
New Phishing Domains Discovered
Cumulative
INTERISLE CONSULTING GROUP MALICIOUS REGISTRATIONS IN THE DOMAIN NAME MARKET 40

Endnotes
1. Federal Bureau of Investigations Internet Crime Complaint Center (ic3). Internet Crime Report 2025. https://www.
ic3.gov/AnnualReport/Reports/2025_IC3Report.pdf
2. With the country-code TLDs, or ccTLDs, being the other 37%. Verisign Domain Name Industry Brief Q1 2026. https://
www.dnib.com/articles/the-domain-name-industry-brief-q1-2026
3. Interisle monitoring of blocklists.
4. ICANN monthly registry reports: https://www.icann.org/resources/pages/registry-reports
5. https://www.icann.org/octo-ssr/metrica/faqs-en
6. Nosyk, Korczyński, Maroofi, Bayuer, et al: “INFERMAL: Inferential Analysis of Maliciously Registered Domains.” 2025.
https://www.icann.org/en/system/files/files/inferential-analysis-maliciously-registered-domains-08nov24-en.pdf
7. ICANN Office of the Chief Technology Officer: “Insights and Clarifications on the INFERMAL Study.” 10 June 2025.
https://www.icann.org/en/system/files/files/insights-clarifications-infermal-study-10jun25-en.pdf
8. Lim, Sommese, Jonker, Mok, claffy, and Kim: “Registration, Detection, and Deregistration: Analyzing DNS Abuse for
Phishing Attacks.” 17 April 2025. https://arxiv.org/pdf/2502.09549
9. Korczyński, Wullink, Tajalizadehkhoob, Moura, and Hesselman. “Statistical Analysis of DNS Abuse in gTLDs Final
Report” (SADAG). 9 August 2017. https://www.icann.org/en/system/files/files/sadag-final-09aug17-en.pdf
10. Interisle Consulting Group (Aaron, Piscitello, Rose, and Strutt): “Phishing Landscape 2025: A Study of the Scope and
Distribution of Phishing.” https://interisle.net/insights/phishing-landscape-2025-an-annual-study-of-the-scope-and-
distribution-of-phishing
11. Interisle Consulting Group (Piscitello, Rose, Strutt, and Wade): “Cybercrime Supply Chain 2025: Measurements
and Assessments of Cyber Attack Resources and Where Criminals Acquire Them.” https://interisle.net/insights/
cybercrimesupplychain2025
12. Nosyk, Korczyński, Gañán, Maroofi, Bayer, Odgerel, Tajalizadehkhoo, and Duda: “Exposing the Roots of DNS Abuse:
A Data-Driven Analysis of Key Factors Behind Phishing Domain Registrations.” CCS ‘25: Proceedings of the 2025 ACM
SIGSAC Conference on Computer and Communications Security. 2025.
https://korlabs.io/documents/6/ccs2025-infermal.pdf
13. Cheadle, Gañán, Lloyd, and Tajalizadehkhoob: Security, Stability, and Resiliency Research, Office of the CTO, ICANN.
“Detecting Malicious Domain Registration Batches: Patterns, Prevalence, and Security Implications.” December 2025.
IEEE: 2025 APWG Symposium on Electronic Crime Research (eCrime).
https://www.icann.org/en/system/files/files/detecting-malicious-domain-registration-batches-13feb26-en.pdf
14. For additional breakdowns, see the Verisign Domain Name Industry Brief reports at:
https://www.dnib.com/listing/report
15. Verisign “Q4 and Full Year 2025 Earnings Conference Call” presentation:
https://investor.verisign.com/static-files/c1fa29cb-a44d-4c32-824d-3d53e0e7c923
INTERISLE CONSULTING GROUP MALICIOUS REGISTRATIONS IN THE DOMAIN NAME MARKET 41

16. The .COM and .NET TLDs make up 70% of the gTLD space. In 2025 .COM grew by 4.6 million domains, up 2.9%,
while .NET shrank 2.2%. The new gTLD sector grew by 11 million domains, up 29.9%. The other older legacy gTLDs
grew by 2.4 million domain name registrations, or 13.7%--most of that growth came from .INFO (which grew by 1.5
million domains) and .ORG (which grew by 519,000 domains). For quarterly Domain Name Industry Brief market
reports, see https://www.dnib.com
17. Palo Alto Networks, “Strategically Aged Domain Detection.” December 29, 2021.
https://unit42.paloaltonetworks.com/strategically-aged-domain-detection/
18. Chiba, Nakano, and Koide, “DomainDynamics: Lifecycle-Aware Risk Timeline Construction for Domain Names.”
Computers & Security, 2025. https://doi.org/10.1016/j.cose.2025.104366
19. Cheadle, Gañán, Lloyd, and Tajalizadehkhoob: Security, Stability, and Resiliency Research, Office of the CTO, ICANN.
“Detecting Malicious Domain Registration Batches: Patterns, Prevalence, and Security Implications.” December 2025.
IEEE: 2025 APWG Symposium on Electronic Crime Research (eCrime). https://www.icann.org/en/system/files/files/
detecting-malicious-domain-registration-batches-13feb26-en.pdf
20. Infoblox 2025 DNS Threat Landscape Report, page 6. These included both gTLD and ccTLD domains.
https://insights.infoblox.com/resources-reports/infoblox-2025-dns-threat-landscape-report/
21. https://www.iana.org/assignments/registrar-ids/registrar-ids.xhtml
22. https://www.iana.org/domains/root/db
23 See ICANN Registrar Accreditation Agreement (RAA), paragraphs 1.3, 1.4, 1.5, and 3.11.
24. Namecheap press release: https://www.namecheap.com/about/press-releases/24-04-16/the-new-domain-
registration-web-services-platform-spaceship-wants-to-help-shape-the-unseen-future-internet/
25. Wise, Glaska, and Rocha, Infoblox. “Uncovering Actor TTP Patterns and the Role of DNS in Investment Scams.” 28
April 2025. https://www.infoblox.com/blog/threat-intelligence/uncovering-actor-ttp-patterns-and-the-role-of-dns-in-
investment-scams/
26. Interisle Consulting Group (Aaron, Piscitello, Rose, and Strutt): “Phishing Landscape 2025: An Annual Study of the
Scope and Distribution of Phishing.” September 2025. https://interisle.net/insights/phishing-landscape-2025-an-
annual-study-of-the-scope-and-distribution-of-phishing
27. Cheadle, Gañán, Lloyd, and Tajalizadehkhoob: Security, Stability, and Resiliency Research, Office of the CTO, ICANN.
“Detecting Malicious Domain Registration Batches: Patterns, Prevalence, and Security Implications.” December 2025.
IEEE: 2025 APWG Symposium on Electronic Crime Research (eCrime). https://www.icann.org/en/system/files/files/
detecting-malicious-domain-registration-batches-13feb26-en.pdf
28. U.S. Department of the Treasury, “Treasure Takes Action Against Major Cyber Scam Facilitator.” 29 May 2025.
https://home.treasury.gov/news/press-releases/sb0149
29. Eduard Kovaks, SecurityWeek, “Polyfill Supply Chain Attack Impacting 100k Sites Linked to North Korea.” 12 March
2026. https://www.securityweek.com/polyfill-supply-chain-attack-impacting-100k-sites-linked-to-north-korea/
30. Silent Push, “Infrastructure Laundering: Silent Push Exposes Cloudy Behavior Around FUNNULL CDN Renting IPs
from Big Tech.” 30 January 2025. https://www.silentpush.com/blog/infrastructure-laundering/
INTERISLE CONSULTING GROUP MALICIOUS REGISTRATIONS IN THE DOMAIN NAME MARKET 42

31. Silent Push, “Unveiling Triad Nexus: How FUNNULL CDN Facilitates Widespread Cyber Threats.” 22 October 2024.
https://www.silentpush.com/blog/triad-nexus-funnull/
32. Brian Krebs, Krebs on Security. “Infrastructure Laundering: Blending in with the Cloud.” 30 January 2025. https://
krebsonsecurity.com/2025/01/infrastructure-laundering-blending-in-with-the-cloud/
33. Quad9, “Trends H2 2024: Cyber Insights.” 11 February 2025. https://quad9.net/news/blog/trends-h2-2024-cyber-
insights/
34. Silent Push, “Post-Sanction Persistence: Triad Nexus’ Operations Infrastructure Reborn as Threat Actor Distances
Activity from FUNNULL CDN.” 14 April 2026. https://www.silentpush.com/blog/triad-nexus-funnull-2026/
35. The Daily Tech Feed, “Funnull Unleashes RingH23 to Hijack CDN and MacCMS, Redirects Millions to Malicious
Sites.”https://thedailytechfeed.com/funnull-unleashes-ringh23-to-hijack-cdn-and-maccms-redirects-millions-to-
malicious-sites/ and https://blog.xlab.qianxin.com/funnull-resurfaces-exposing-ringh23-arsenal-and-maccms-
supply-chain-attacks/
36. U.S. Department of the Treasury, “Treasure Takes Action Against Major Cyber Scam Faclitator.” 29 May 2025.
https://home.treasury.gov/news/press-releases/sb014
37. See https://www.ic3.gov/CSA/2025/250529.pdf and https://www.ic3.gov/CSA/2025/Complete_List_of_Domains_
Attributed_to_Funnull.zip
38. https://domainincite.com/23302-i-was-wrong-famous-four-bosses-were-kicked-out
39. Supreme Court of Gibraltar, including but not limited to case citation numbers 2025/GSC/022, 2023/GSC/044, 2021/
GSC/17, 2019 Comp No 03, 2016 Comp Nos 09-11.
40. https://www.iana.org/domains/root/db/loan.html
41. https://circleid.com/posts/20140417_general_availability_period_for_new_pink_top_level_domain_opens
42. https://urlscan.io/result/0196a199-f77a-72ab-a963-b28cdca76177/
43. Per WHOIS and RDAP records, blocklistings from URLHaus, and other records.
44. Barnett, James, Infoblox Threat Intel: “RDGAs: The Next Chapter in Domain Generation Algorithms.” 24 July 2024.
https://www.infoblox.com/blog/threat-intelligence/rdgas-the-next-chapter-in-domain-generation-algorithms.
45. For more about the malware and examples of its association to this series of .BOND domains, see for example:
https://www.joesandbox.com/analysis/1705331/0/html and https://www.joesandbox.com/analysis/1488516/0/html
46. “How to Stand Out in Finance: Building Credibility in a Competitive Market.” https://www.domaindiscount24.com/
en/blog/how-to-stand-out-in-finance-building-credibility-in-a-competitive-market
47. See also: Barnett, David. “An Unnatural .Bond: A Study of a ‘Megacluster’ of Malware Domains.” CircleID, 23
July 2024. https://circleid.com/posts/20240723-an-unnatural-dot-bond-a-study-of-a-megacluster-of-malware-
domains#fn8
48. Ionut Ilascu, “Revolver Rabbit Gang Registers 500,000 Domains for Malware Campaigns.” Bleeping Computer, 18
July 2024. https://www.bleepingcomputer.com/news/security/revolver-rabbit-gang-registers-500-000-domains-for-
malware-campaigns/
INTERISLE CONSULTING GROUP MALICIOUS REGISTRATIONS IN THE DOMAIN NAME MARKET 43

49. .GIFT domains were included in the FUNNULL list published by the U.S. Federal Bureau of Investigation (FBI).
See https://www.ic3.gov/CSA/2025/250529.pdf and https://www.ic3.gov/CSA/2025/Complete_List_of_Domains_
Attributed_to_Funnull.zip
50. The clusters of associated domains we found displayed functional characteristics of FUNNULL, such as malicious
advertising and redirection to yet more suspicious domains. An example is mzvzq.gift. This domain redirected,
offered a suspicious APK download (see https://urlscan.io/result/9ca11650-c0d1-4109-ab42-bc76ea9ca944/ ), and
was associated with 203.210.16.175 – an IP address blocklisted by Spamhaus. At one point mzvzq.gift redirected to
suspicious destinations on other related domains such as such as bcnkvs.top (see https://www.virustotal.com/gui/
url/1a7152589e957bc46cdfde458e7961b5db3939e805b0ca114ced65aa1fd3f910/details0)
51. We did not chart .GIFT’s performance because of unexplained DUM anomalies in one of its reports to ICANN.
https://www.icann.org/sites/default/files/mrr/gift/gift-transactions-202510-en.csv
52. Verisign DNIB, https://www.dnib.com/dashboards/gtld-registration-and-renewal-trends
53. Of the .ORG domains that came up for their first-year renewal in 2024, only 52.4% renewed. PIR Annual Impact
Report 2024. https://pir.org/annual-impact-report-2024/
54. Spamhaus Domain Reputation Update, October 2025 – March 2026. https://content.spamhaus.org/4d83c22f-84c5-
4f82-95ab-4e6b39f73db5.pdf
55. Affinito, Sommese, Akiwate, Savage, Claffy, Voelker, Botta, and Jonker. “Domain Name Lifetimes: Baseline and
Threats.” In TMA, pages 1–9, Austria, 2022. https://www.sysnet.ucsd.edu/~voelker/pubs/domain-lifetimes-tma22.pdf
56. Cheadle, Gañán, Lloyd, and Tajalizadehkhoob: Security, Stability, and Resiliency Research, Office of the CTO, ICANN.
“Detecting Malicious Domain Registration Batches: Patterns, Prevalence, and Security Implications.” December 2025.
IEEE: 2025 APWG Symposium on Electronic Crime Research (eCrime). https://www.icann.org/en/system/files/files/
detecting-malicious-domain-registration-batches-13feb26-en.pdf
57. Nosyk, Korczyński, Maroofi, Bayuer, et al: “INFERMAL: Inferential Analysis of Maliciously Registered Domains.” 2025.
https://www.icann.org/en/system/files/files/inferential-analysis-maliciously-registered-domains-08nov24-en.pdf
58. Interisle Consulting Group (Piscitello, Rose, Strutt, and Wade): “Cybercrime Supply Chain 2025: Measurements
and Assessments of Cyber Attack Resources and Where Criminals Acquire Them.” https://interisle.net/insights/
cybercrimesupplychain2025
59. Lim, Sommese, Jonker, Mok, claffy, and Kim: “Registration, Detection, and Deregistration: Analyzing DNS Abuse for
Phishing Attacks.” 17 April 2025. https://arxiv.org/pdf/2502.09549. This comprehensive analysis of phishing domains
focused on maliciously registered domains, DNS behaviors, and detection timelines, finding that attackers favored
low-cost TLDs.
60. Affinito, Sommese, Akiwate, Savage, Claffy, Voelker, Botta, and Jonker. “Domain Name Lifetimes: Baseline and
Threats.” In TMA, pages 1–9, Austria, 2022. https://www.sysnet.ucsd.edu/~voelker/pubs/domain-lifetimes-tma22.pdf
61. Examples of how low price enabled abuse at scale include when new gTLD .INFO attracted significant malicious
domain name registration as a result of “two-for-one” and registrar rebate programs in the early 2000s, (https://
web.archive.org/web/20090215123646/https://www.prweb.com/releases/2008/11/prweb1580134.htm), when
.CN reduced prices in 2007 (https://docs.apwg.org/reports/APWG_GlobalPhishingSurvey2007.pdf), and into the
new gTLDs from the 2012 round, when registrars and registries completed on price in a newly crowded market.
INTERISLE CONSULTING GROUP MALICIOUS REGISTRATIONS IN THE DOMAIN NAME MARKET 44

(“Spamhaus Presents: The World’s Worst Top Level Domains.” 2016. “https://www.spamhaus.org/resource-hub/
domain-reputation/spamhaus-presents-the-worlds-worst-top-level-domains/#introduction)
62. Nosyk, Korczyński, Maroofi, Bayuer, et al: “INFERMAL: Inferential Analysis of Maliciously Registered Domains.” 2025.
https://www.icann.org/en/system/files/files/inferential-analysis-maliciously-registered-domains-08nov24-en.pdf
63. https://nominet.uk/blog/growing-uk/
64. https://newgtldprogram.icann.org/en
65. “.com is Back as Verisign Discounts Bear Fruit.” DomainIncite.com, 24 April 2025. https://domainincite.com/31007-
com-is-back-as-verisign-discounts-bear-fruit
66. For example: https://web.archive.org/web/20260521152940/https://realtimeregister.com/solutions/domains/
domain-promotions/specialpromotions
67. https://www.icann.org/octo-ssr/metrica/faqs-en
INTERISLE CONSULTING GROUP MALICIOUS REGISTRATIONS IN THE DOMAIN NAME MARKET 45