# Security Status Report 2025 H1

## Table of Contents
- [Executive Overview](#executive-overview)
- [Highlights of the First Half of 2025](#highlights-of-the-first-half-of-2025)
- [Mobiles](#mobiles)
  - [Apple iOS](#apple-ios)
  - [Apple Transparency Report](#apple-transparency-report)
  - [Android](#android)
- [Significant Vulnerabilities](#significant-vulnerabilities)
  - [Vulnerabilities in figures](#vulnerabilities-in-figures)
- [APT Operations, Organised Groups, and Associated Malware](#apt-operations-organised-groups-and-associated-malware)
- [OT Threat Analysis](#ot-threat-analysis)
- [Threat Study by Indicator](#threat-study-by-indicator)
- [Useful Links](#useful-links)

---

## Executive Overview

The purpose of this report is to synthesize the cyber security information of the last few months (from mobile security to the most relevant news and the most common vulnerabilities), adopting a point of view that covers most aspects of this discipline, in order to help the reader understand the risks of the current landscape.

This semester, two news items stand out. Although apparently unrelated, we believe they have a common denominator.

The U.S. government announced in April 2025 that it would stop funding MITRE to operate and maintain the Common Vulnerabilities and Exposures (CVE) system. This system has been managed by MITRE since 1999 with funding from the Department of Homeland Security (DHS) and the Cybersecurity and Infrastructure Security Agency (CISA). Yosry Barsoum, vice president of MITRE, warned that the contract would expire on April 16, 2025, and that, if not renewed, there would be serious consequences. The main reason pointed to be a budget cut driven by the Trump administration, although CISA and other sources did not publicly detail the exact reasons.

The potential service disruption generated alarm in the cyber security community. Fortunately, hours before the expiration, CISA stepped in and temporarily renewed MITRE's contract, avoiding an immediate disruption of CVE services. This solution was yet considered temporary and highlighted the fragility of relying on a single government funder for such a critical resource. In response, the creation of the CVE Foundation, an independent entity driven by members of the CVE board itself, was announced. The entity will ensure the long-term sustainability and neutrality of the system.

On the other hand, in June, what appeared to be one of the biggest cyber security incidents in history was revealed: the leak of 16 billion passwords and login credentials for services such as Google, Apple, Facebook, GitHub, Telegram... and even government portals. The investigation was led by the Cybernews team, which detected at least 30 databases of different sizes, some with more than 3.5 billion records each. It did not look like an attack on a single company, but a massive collection of thefts. It was eventually learned that the alleged “leak” of 16 billion passwords was not a new leak or a recent attack, but a compilation of credentials previously stolen over the years through infostealer-type malware, previous breaches and credential stuffing attacks. The affected sites were not recently compromised to obtain these credentials.

What happened (as other times) is that a massive database was compiled and exposed, composed of records already circulating in underground forums and marketplaces. There is no evidence that it contains unpublished data (or at least, not a relevant amount) or extracted from new breaches. The first news went unnoticed by the mainstream media. While the cyber security industry was biting its nails for 24 hours for fear of losing the CVE system, the world went on. The second news, in contrast, opened generic news in all countries, with front pages and reports. Everyone knew about the leak. In this case, the world was on edge while the industry suspected (by pure logic) that it was a compilation of old thefts of no great significance. The numbers were not so much in technical reality as in a headline.

When the continuity of CVE was compromised, the alarm was immediate: experts, companies, and security managers realized that losing this infrastructure meant flying blind in the face of vulnerabilities, a chaos that would affect incident response, infrastructure protection and global coordination. However, the password leak, despite its enormous media coverage, did not generate the same professional concern because, in essence, it did not alter the threat landscape or introduce new risks: it was, above all, noise and recycling of already exposed data.

This phenomenon highlights a persistent gap between what really matters in the industry for digital resilience and what the headlines capture. The media tends to amplify the most spectacular or easily understood incidents, even if their real impact is limited, while structural issues - such as critical infrastructure financing and governance - are relegated or overlooked.

This not only distorts the user's perception, who often ends up believing any amplified alarm without context, but also reflects a certain immaturity in news coverage: the right experts are rarely consulted and the underlying technical consequences are rarely explained. The industry, for its part, reveals that what is really important is not always what is most visible, and that security depends more on the solidity of its foundations - such as CVE - than on the sensational nature of the incidents that make the front pages. Are we still, perhaps, too far removed from the user?

Whether you are an amateur or a professional, it is important to be able to keep up with relevant cyber security news: what is the most relevant thing going on? What is the current landscape? Through this report, the reader will have a tool to understand the state of security from different perspectives and will be able to learn about its current state and project possible short-term trends. The information gathered is based in large part on the compilation and synthesis of internal data, contrasted with public information from sources we consider to be of quality. Let's go!

## Highlights of the First Half of 2025

*(Content omitted for brevity in this example, but would follow the structure provided in the source text)*

## Mobiles

### Apple iOS

*(Content regarding iOS 18/26, vulnerabilities, and fragmentation)*

### Apple Transparency Report

*(Content regarding government requests for data)*

### Android

*(Content regarding Android 16, Advanced Protection, and vulnerabilities)*

## Significant Vulnerabilities

*(Table of CVEs and scoring)*

### Vulnerabilities in figures

*(Charts and analysis of CVE distribution)*

## APT Operations, Organised Groups, and Associated Malware

*(Analysis of APT28, Lazarus, Primitive Bear, and Mythic Leopard)*

## OT Threat Analysis

*(Analysis of the Aristeo system and threat statistics)*

## Threat Study by Indicator

*(Analysis of IOCs in collaboration with Maltiverse)*

## Useful Links

*(Placeholder for links)*

---
2025 © Telefónica Cybersecurity & Cloud Tech, S.L.U. All Rights Reserved.

---

rectly through an IP or indirectly from a domain) and within that machine a resource is specified through
a path.

In the end, in the context of malware, every IP and domain will be part of a URL to request a resource.
Whether it is a URL that directs us to a phishing site and has a domain very similar to the original or it may be
that the URL serves as a download point for malware.

It is important to determine what is at the end of the URL and categorize it properly to know what type of
threat we are dealing with. This is precisely what we have asked in the Maltiverse database, and the
following results have been found:

Malware Download

185119

62,20%

Phishing

Lumma Stealer

Formbook

Clearfake

95977

32,25%

5613

1,89%

4559

1,53%

851

0,29%

 2025 © Telefónica Cybersecurity & Cloud Tech, S.L.U. All Rights Reserved.

Page 31 de 37

FAKEUPDATES

DCRat

Stealc

Vidar

Coper

Security Status Report 2025 H1

695

0,23%

537

291

0,18%

0,10%

290

0,10%

272

0,09%

There are no surprises regarding the two categories with the highest number of indicators: phishing and
malware download. Because if there is a classic in cyber security regarding what awaits us at the end of a
URL, it is precisely these two major categories.

However, they are categories that group or assimilate a large part of what we find in the long tail. The rest of
the categories are more explicit and even indicate to which malware family they belong.

In the last edition we had Stela Stealer as the star malware. It has disappeared, but in its place comes
Lumma Stealer, hitting hard and with the same functionality: stealing data. It affects Microsoft Windows
systems and mainly uses the phishing vector via e-mails.

It is followed in the ranking by FormBook, another stealer disguised as a trojan, which also has a MacOS
version in addition to Windows.

The rest are distributed, as we can see, among the most widespread malware families. Infrastructure that
serves as a download point, to capture orders and even to temporarily deposit stolen information. A long line
of families with different DNA but with a common malicious payload.

Which domains are most commonly used by URLs marked as malicious?

We consulted Maltiverse this year to find out which domains appear most frequently in the URLs studied.

It is interesting to note which services, mostly legitimate, are the most used by malware writers and their
associated campaigns.

In the end, a URL will have a host or redirect and needs an executable web space or application that at some
point it will use for its purposes. It is the domain that will “tell us” where it has been hosted and what service
it has used (illegitimately, for example).

vercel.app

webflow.io

10281

3,45%

9480

3,19%

 2025 © Telefónica Cybersecurity & Cloud Tech, S.L.U. All Rights Reserved.

Page 32 de 37

github.io

pages.dev

github.com

weebly.com

godaddysites.com

duckdns.org

r2.dev

glitch.me

Security Status Report 2025 H1

6892

4940

3448

2325

1913

1519

1319

1154

2,32%

1,66%

1,16%

0,78%

0,64%

0,51%

0,44%

0,39%

As usual, the top spots belong to online services that allow you to host web content for free: vercel.app,
weflow.io, github.io.

It's a common pattern: Why take a risk on private hosting or compromised servers when they offer free and
anonymous hosting?

There are also domains associated with these malicious URLs that use dynamic domain resolvers:
duckdns.org. In essence, they are actually naked IPs that through a free DNS service can be resolved to a
particular subdomain and even if they need to migrate the malicious infrastructure, they move the IP
address and will continue to resolve to the new location.

As we can see, in one type of service or another, the keynote is always: free and anonymous. Two
characteristics that are sought after and used zealously by cybercriminals.

Which countries are the IP addresses on which malicious activity has been detected?

Before answering the question, it should be clarified that just because a country appears in this ranking does
not mean that there is malicious intent with respect to that country. Many countries stand out from the rest
because they have more services and hosting companies, which translates directly into greater fraudulent
use. A server can be hosted in a country and the criminal organization that uses it can come from another
nationality.

India

68265

20,34%

United States of America

52462

15,63%

 2025 © Telefónica Cybersecurity & Cloud Tech, S.L.U. All Rights Reserved.

Page 33 de 37

China

Singapur

Vietnam

Russia

Germany

Brazil

United Kingdom

Pakistan

Security Status Report 2025 H1

30877

9,20%

17491

5,21%

16084

4,79%

13246

3,95%

11178

8914

7091

3,33%

2,66%

2,11%

6855

2,04%

There are no major variations in this aspect in recent years. These are countries with large technological
infrastructures and, therefore, as mentioned above, they have a proportionally greater potential to be used
by cybercrime.

What kind of maliciousness do IP addresses engage in?

We could conclude that certain governments request access to data "too often," but we could also argue
that justice may operate more quickly there, or that there may be more fraud in these locations the
interpretation is free. Below are some conclusions based on our analysis:

Suspicious host

Mail Spammer

HTTP Spammer

Malicious host

Bruteforce

Hacking

158322

47,17%

143953

42,89%

117679

35,06%

81556

24,30%

59340

17,68%

57975

17,27%

 2025 © Telefónica Cybersecurity & Cloud Tech, S.L.U. All Rights Reserved.

Page 34 de 37

Security Status Report 2025 H1

Port Scanner

SSH Attacker

Proxy

HTTP Attacker

55216

16,45%

54335

16,19%

51675

15,40%

42955

12,80%

Later, when a label is added with the explanation of why: spam, indiscriminate scans, etc., the suspicious
host label is not removed as it is a further refinement. Another type of generalist labeling is found in
“Malicious host”. Identical meaning, although it adds a little more certainty in the preliminary diagnosis.

If we aggregate the tags by specific IP address activity, we see that SPAM, both HTTP and Mail, top the
ranking with more than 80% of the tags. Remember that tags overlap, so the same IP can contain several of
them. A generalist of “suspicious” and “HTTP Spammer”, for example, or even that the same IP is used for
port scanning because it has been a detected activity at some point in time.

SSH Attacker is a unique category. It almost certainly belongs to groups of infected hosts coordinated by a
Mirai-type botnet. Mass scanning for easy access via SSH (Secure Shell) has been a constant feature of the
Internet for decades (as was Rlogin or telnet in its early days). Almost 16.19% of IP addresses have been
observed performing attacks on SSH (mostly dictionary attacks on the login).

Likewise, “Bruteforce” refers to the continuous attempt to perform brute-force authentication (actually,
again: dictionaries of common usernames and passwords). This category adds up to almost 17.68%.

In another subcategory, indiscriminate scans, we find: Port and Host scanner. IP addresses that have been
detected by performing mass scans of entire ranges or multiple ports on specific hosts. That is, horizontal
scans looking for certain ports or vertical scans (in depth) on a group of hosts.

The  “Proxy” category with almost 15.4% are systems that, either deliberately or unsuspectedly, serve as a
gateway or hop to other machines to hide the origin of certain attacks or unauthorized access.

Overall, we find the “hacking” category with 17.27% closing the ranking. These are nodes that have been
observed performing attacks in general, either trying to find SQL vulnerabilities or launching exploits. Often,
these are vulnerability scanners used indiscriminately and, of course, without authorization.

 2025 © Telefónica Cybersecurity & Cloud Tech, S.L.U. All Rights Reserved.

Page 35 de 37

Security Status Report 2025 H1

What are the top level domains (TLDs) with the most malicious domains?

As we know, a domain resolves to an IP address. In the world of cybercrime, domains are of paramount
importance because they allow you to make use of it and change the IP address if the currently active server
ceases its malicious activity.

A domain is composed of several levels. If you look at them, they are stretches of strings separated by dots. If
we get these groups from right to left they form a hierarchy. The rightmost one is the highest level domain.

Hence, we can group the domains categorized as malicious by their highest level domain. The result of the
top 10 is this:

xyz

com

io

top

org

app

net

dev

shop

gg

43193

29,52%

34609

23,65%

9768

5170

4705

4188

3532

2896

6,68%

3,53%

3,22%

2,86%

2,41%

1,98%

2450

1,67%

1831

1,25%

“xyz” tops our TLD ranking this semester. Although it disputes in alternation the leadership with “com”, it
rises strongly and snatches the baton. “xyz” was born in 2014 and was pushed by Google for matching its
parent: “abc.xyz”.

Why is “xyz” the “favorite” of malware creators? Because of its competitive prices: from $0.99 per year it is a
more than attractive figure to use domains of this TLD.

Regarding “.app” it is especially curious as it is a TLD for which Google paid more than $25 million to ICANN
in February 2015 to take control of it. Moreover, it is a TLD for which HTTPS traffic is mandatory.

 2025 © Telefónica Cybersecurity & Cloud Tech, S.L.U. All Rights Reserved.

Page 36 de 37

Security Status Report 2025 H1

“gg” which sneaks into our top 10 is a geographic TLD belonging to Guernsey. An island in the English
Channel, belonging to the United Kingdom. It is a TLD lately associated with video games and e-sports sites.

What malicious categorization do the studied domains possess?

Domains are closely linked to URLs (of which they are part) and also, of course, to the IP addresses to which
a domain resolves.

Finally, let us see how the top 10 of these domains have been classified over the last six months.

Phishing

Metastealer

Formbook

Lumma Stealer

Virut

Malware Download

Joker

Xworm

BumbleBee

Bankbot

44483

39659

14389

8623

6708

5077

2394

1734

1608

1406

30,40%

27,10%

9,83%

5,89%

4,58%

3,47%

1,64%

1,19%

1,10%

0,96%

As we have already mentioned, there is a very close relationship between domains and URLs and this can be
seen in the top 10 categories: phishing and malware in general. The rest belong to malware families that
have had an impact.

 2025 © Telefónica Cybersecurity & Cloud Tech, S.L.U. All Rights Reserved.

Page 37 de 37

Security Status Report 2025 H1

USEFUL LINKS

Do not just stay in the top layer of cyber security analysis, the semi-annual reports are both cumulative and
summarized. Telefónica Tech's cyber security blog has much more information and news which may be
interesting for you. Here are our most relevant articles.

 CYBER SECURITY

The truth about the 320 seconds to hack Bitcoin: a technical analysis
Analysis of an intrusion on the Aristeo platform as a demo of Its predictive capabilities
Linux and the vulnerability paradox: More reports, more security?

   ARTIFICIAL INTELLIGENCE

https://telefonicatech.com/en/blog/the-incredible-inner-world-of-llms-i

The incredible inner world of LLMs (II)

La tokenización y el caballero andante Don Quijote

The information contained in this document is property of Telefónica Cybersecurity & Cloud Tech S.L.U. (hereinafter “Telefónica Tech”) and/or
any other entity within the Telefónica Group or its licensors.

Telefónica Tech and/or any Telefónica Group company or Telefónica Tech's licensors reserve all intellectual property rights (including any
patents or copyrights) arising out of or relating to this document, including the rights to design, produce, reproduce, use, and sell this
document, except to the extent that such rights are expressly granted to third parties in writing. The information contained in this document
shall be changed at any time without notice.

Telefónica Tech shall not be liable for any loss or damage arising from the use of the information contained herein.

Telefónica Tech and its trademarks (as well as any trademarks belonging to the Telefónica Group) are registered trademarks. Telefónica Tech
and its subsidiaries reserve all rights therein.

This report is published under a Creative Commons Attribution - Share Alike license

 2025 © Telefónica Cybersecurity & Cloud Tech, S.L.U. All Rights Reserved.

Page 38 de 37