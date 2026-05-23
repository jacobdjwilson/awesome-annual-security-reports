# Ransomware Review: First Half of 2024

## Table of Contents
- [Executive Summary](#executive-summary)
- [Leak Site Trends in the First Half of 2024](#leak-site-trends-in-the-first-half-of-2024)
- [Threat Group Activity](#threat-group-activity)
- [Law Enforcement Takedowns and Disruptions](#law-enforcement-takedowns-and-disruptions)
- [Other Ransomware Groups](#other-ransomware-groups)
- [New Kids on the Block](#new-kids-on-the-block)
- [Rebrands](#rebrands)
- [Industries and Regions Impacted](#industries-and-regions-impacted)
- [The Data and Where It Comes From](#the-data-and-where-it-comes-from)
- [Conclusion](#conclusion)
- [Additional Resources](#additional-resources)

## Executive Summary

Unit 42 monitors ransomware and extortion leak sites closely to keep tabs on threat activity. We reviewed compromise announcements from 53 dedicated leak sites in the first half of 2024 and found 1,762 new posts. This averages to approximately 294 posts a month and almost 68 posts a week. Of the 53 ransomware groups whose leak sites we monitored, six of the groups accounted for more than half of the compromises observed.

In February, we reported a 49% increase year-over-year in alleged victims posted on ransomware leak sites. So far, in 2024, comparing the first half of 2023 to the first half of 2024, we see an even further increase of 4.3%. The higher level of activity observed in 2023 was no fluke.

Activity from groups like Ambitious Scorpius (distributors of BlackCat) and Flighty Scorpius (distributors of LockBit) has largely fallen off due to law enforcement operations. However, other threat groups we track such as Spoiled Scorpius (distributors of RansomHub) and Slippery Scorpius (distributors of DragonForce) have joined the fray to fill the void.

Industries most impacted by ransomware were manufacturing (16.4% of observed posts), healthcare (9.6%) and construction (9.4%). Like with manufacturing, healthcare is extremely sensitive to disruptions and downtime.

The U.S. was home to the most victims by far in the first half of 2024. With 917 compromises, the US received 52% of total attacks. In order of impact, the remaining top 10 nations were: Canada, the U.K., Germany, Italy, France, Spain, Brazil, Australia and Belgium.

Newly disclosed vulnerabilities primarily drove ransomware activity as attackers moved to quickly exploit these opportunities. Threat actors regularly target vulnerabilities to access victim networks, elevate privileges and move laterally across breached environments. We’ll list some of the most common vulnerabilities being exploited in 2024.

---

## Leak Site Trends in the First Half of 2024

Our team monitors data from dedicated leak sites (DLS) that are often only accessible through the dark web. Throughout our analysis, we compare the first half of 2024 (1H24) to the first half of 2023 (1H23) so that we are accounting for any seasonal fluctuations that can occur due to annual holidays, travel seasons and other recurring events that may impact threat activity.

**Key Findings:**
- 4.3% year-over-year increase in compromise announcements
- 1H24: 1,762 compromise announcements from 53 sites – with the top six groups responsible for more than half of the compromises
- 1H23: 1,688 compromise announcements
- 1H24 averaged 68 leak site posts per week
- Ransomware announcements continue to increase, despite multiple notable law enforcement disruptions and arrests
- The LockBit leak site remains the most active, posting misleading information and old data

![Figure 1. Month-by-month comparison of ransomware leak site reports.]

Figure 1 shows a month-by-month breakout of the numbers, comparing each of the first six months in 2023 with each of the first six months in 2024. We observed a notable decrease in ransomware leak site reports in June of 2024. Significant decreases in activity on the LockBit and 8Base leak sites largely accounted for this drop.

## Threat Group Activity

Leak site data indicates 53 ransomware groups have been active so far in 2024, but the top six ransomware groups account for a little more than half of the total compromises. Unit 42 tracks threat groups using a naming system that pairs a modifier with a designated constellation per group.

![Figure 2. Comparing the top six ransomware groups from all of 2023 with the first half of 2024.]

As seen in Figure 2, four ransomware groups that were among the six most active in 2023 remained among the most active so far this year. During the first half of 2024, Ambitious Scorpius (distributors of ALPHV/BlackCat) and Chubby Scorpius (distributors of CL0P) dropped out of the top rankings. These groups were displaced by Dark Scorpius (distributors of BlackBasta) and Transforming Scorpius (distributors of Medusa).

Threat actors regularly target vulnerabilities to access victim networks, elevate privileges and move laterally across breached environments. Below are some of the more prolific vulnerabilities exploited by ransomware groups in the first half of 2024:
- CVE-2018-13379 - Fortinet SSL VPN
- CVE-2024-1709 - ConnectWise ScreenConnect
- CVE-2024-1708 - ConnectWise ScreenConnect
- CVE-2024-27198 - TeamCity
- CVE-2024-4577 - PHP-CGI script engine
- CVE-2020-1472 - Netlogon Remote Protocol
- CVE-2024-26169 - Microsoft Windows Error Reporting Service

## Law Enforcement Takedowns and Disruptions

Law enforcement activity continues to have a wide-reaching impact on the ransomware threat landscape in 2024. Highlights include:
- **January 2024**: U.S. law enforcement arrested a prominent member of Muddled Libra.
- **February 2024**: Law enforcement takedown of the LockBit 3.0 Tor site.
- **March 2024**: Ambitious Scorpius finalized an exit scam.
- **May 2024**: U.K., U.S. and Australia unmasked and sanctioned the leader of Flighty Scorpius.
- **May 2024**: GhostSec announced its exit from ransomware.
- **May 2024**: Law enforcement seized control of BreachForums.
- **June 2024**: Law enforcement arrested the leader of Muddled Libra (aka Scattered Spider).
- **June 2024**: BreachForums administrator ShinyHunters retired.
- **July 2024**: Law enforcement arrested another leader of Muddled Libra.

## Other Ransomware Groups

Chubby Scorpius (CL0P) activity fell dramatically in 2024, accounting for less than 0.75% of total posts. Other groups inactive on leak sites in 2024 include Bashful Scorpius (Nokoyawa), KelvinSecurity, Losttrust, Mushy Scorpius (Karakurt), Spicy Scorpius (AvosLocker), and Stumped Scorpius (NoEscape).

## New Kids on the Block

- **Spoiled Scorpius (RansomHub)**: First announced in February 2024. Achieves access via SocGholish malware and SEO poisoning.
- **Slippery Scorpius (DragonForce)**: Notorious for extorting victims via phone calls and leaking audio.
- **Burning Scorpius (LukaLocker)**: Encrypts Windows and Linux; uses direct phone-based extortion.
- **Alpha/MyData**: Relatively new and unstable.
- **Trisec**: Claims to be state-sponsored/Tunisian-affiliated.
- **DoNex**: Financially motivated, active since March 2024.
- **Quilong**: Targeted plastic surgery centers in Brazil.
- **Blackout**: Active since late February 2024.

## Rebrands

After the Ambitious Scorpius exit scam, we are monitoring for rebrands. Flighty Scorpius has seen a decline following law enforcement action, though new ransomware like "Brain Cipher" (based on LockBit 3.0 code) has emerged.

## Industries and Regions Impacted

Manufacturing remains the most impacted sector (16.4%), followed by healthcare (9.6%) and construction (9.4%).

![Figure 3. Industries affected by ransomware in the first half of 2024.]

The U.S. remains the primary target (52% of attacks).

![Figure 4. Nations where organizations were affected by ransomware in the first half of 2024.]

## The Data and Where It Comes From

Analysis is based on publicly reported information from 53 dedicated leak sites and Unit 42 Incident Response engagements. We advise caution as leak site data may omit victims who pay quickly or misrepresent the source of data.

## Conclusion

While law enforcement has successfully disrupted several major groups, the ransomware ecosystem remains resilient, with new actors quickly filling voids. Palo Alto Networks provides protection through Network Security solutions, Prisma Cloud, and the Cortex product line.

If you have been compromised, contact the Unit 42 Incident Response team:
- **North America**: 866.486.4842
- **EMEA**: +31.20.299.3130
- **APAC**: +65.6983.8730
- **Japan**: +81.50.1790.0200

## Additional Resources

*(List of 40+ references omitted for brevity, as per original document structure)*

Copyright © 2025 Palo Alto Networks. All Rights Reserved