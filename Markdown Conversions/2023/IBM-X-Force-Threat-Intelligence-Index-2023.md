# X-Force Threat Intelligence Index 2023
## Table of contents
[Executive summary](#executive-summary)
[Report highlights](#report-highlights)
[Key stats](#key-stats)
[Top initial access vectors](#top-initial-access-vectors)
[Top actions on objectives](#top-actions-on-objectives)
[Top impacts](#top-impacts)
[Cyber-related developments of Russia’s war in Ukraine](#cyber-related-developments-of-russias-war-in-ukraine)
[The malware landscape](#the-malware-landscape)
[Threats to OT and industrial control systems](#threats-to-ot-and-industrial-control-systems)
[Geographic trends](#geographic-trends)
[Industry trends](#industry-trends)
[Recommendations](#recommendations)
[About us](#about-us)
[Contributors](#contributors)
[Appendix](#appendix)

The year 2022 was another tumultuous one for cybersecurity. While there was no shortage of contributing events, among the most significant were the continuing effects of the pandemic and the eruption of the military conflict in Ukraine. Disruption made 2022 a year of economic, geopolitical and human upheaval and cost—creating exactly the kind of chaos in which cybercriminals thrive.

And thrive they did.

IBM Security® X-Force® witnessed opportunistic threat actors who capitalize on disorder, using the landscape to their advantage to infiltrate governments and organizations across the globe.

The IBM Security X-Force Threat Intelligence Index 2023 tracks new and existing trends and attack patterns and includes billions of datapoints ranging from network and endpoint devices, incident response (IR) engagements, vulnerability and exploit databases and more. This report is a comprehensive collection of our research data from January to December 2022.

We provide these findings as a resource to IBM clients, cybersecurity researchers, policymakers, the media and the larger community of security industry professionals and industry leaders. Today’s volatile landscape, with its increasingly sophisticated and malicious threats, requires a collaborative effort to protect business and citizens. More than ever, you need to be armed with threat intelligence and security insights to stay ahead of attackers and fortify your critical assets.

So you too can thrive.

# Executive summary
In 2022, we modified how we examined portions of our data. The changes allow us to offer more insightful analysis and align more closely to industry standard frameworks. That, in turn, enables you to make more informed security decisions and better protect your organization from threats.

Changes to our analysis in 2022 included:

- Initial access vectors: Adopting the MITRE ATT&CK framework to track initial access vectors more closely aligns our research findings with the broader cybersecurity industry and allows us to identify important trends at the technique level.

- Exploits and zero day compromises: Extrapolating from our robust vulnerability database—which includes nearly 30 years of data—helps lend context to our analysis and identify the actual threat posed by vulnerabilities. This process also lends context to the diminishing proportion of weaponizable exploits and impactful zero days.

- Threat actor methods and their impact: Uncoupling the steps threat actors take during an attack from the actual impact of an incident allowed us to identify critical stages of an incident. This process, in turn, uncovered areas that responders should be prepared to handle in the aftermath of an incident.

How our data analysis changed for 2022

Top actions on objectives observed: In almost one-quarter of all incidents remediated in 2022, the deployment of backdoors at 21% was the top action on objective. Notably, an early year spike in Emotet, a multipurpose malware, contributed significantly to the jump in backdoor activity observed year over year. Despite this spike in backdoor activity, ransomware, which held the top spot since at least 2020, constituted a large share of the incidents at 17%, reinforcing the enduring threat this malware poses.

Extortion was the most common attack impact on organizations: At 27%, extortion was the clear impact of choice by threat actors. Victims in manufacturing accounted for 30% of incidents that resulted in extortion, as cybercriminals continued the trend of exploiting a strained industry.

Phishing was the top initial access vector: Phishing remains the leading infection vector, identified in 41% of incidents, followed by exploitation of public-facing applications in 26%. Infections by malicious macros have fallen out of favor, likely due to Microsoft’s decision to block macros by default. Malicious ISO and LNK files use escalated as the primary tactic to deliver malware through spam in 2022.

Increase in hacktivism and destructive malware: Russia’s war in Ukraine opened the door to what many in the cybersecurity community expected to be a showcase of how cyber enables modern warfare. Although the direst cyberspace predictions haven’t come to fruition as of this publication, there was a notable resurgence of hacktivism and destructive malware. X-Force also observed unprecedented shifts in the cybercriminal world with increased cooperation between cybercriminal groups, and Trickbot gangs targeting Ukrainian organizations.

# Report highlights
Percentage of attacks with extortion
Threat actors sought to extort money from victims in more than one-quarter of all incidents to which X-Force responded in 2022. The tactics they use have evolved in the last decade, a trend expected to continue as threat actors more aggressively seek profits.

Share of incidents that saw backdoors deployed
Deployment of backdoors was the top action on objective last year, occurring in more than one in five reported incidents worldwide. Successful intervention by defenders likely prevented threat actors from fulfilling further objectives that may have included ransomware.

Ransomware’s share of attacks
Even amid a chaotic year for some of the most prolific ransomware syndicates, ransomware was the second most common action on objective, following closely behind backdoor deployments and continuing to disrupt organizations’ operations. Ransomware’s share of incidents declined from 21% in 2021 to 17% in 2022.

*27%*
*21%*
*17%*

# Key stats
Drop in reported phishing kits seeking credit card data
Almost every phishing kit analyzed in the data sought to gather names at 98% and email addresses at 73%, followed by home addresses at 66% and passwords at 58%. Credit card information, targeted 61% of the time in 2021, fell out of favor for threat actors—data shows it was sought in only 29% of phishing kits in 2022, a 52% decline.

Share of global attacks that targeted the Asia-Pacific region
Asia-Pacific retained the top spot as the most-attacked region in 2022, accounting for 31% of all incidents. This statistic represents a five percentage point increase from the total share of attacks to which X-Force responded in the region in 2021.

Share of 2022 vulnerabilities with known exploits
Twenty-six percent of 2022’s vulnerabilities had known exploits. According to data that X-Force has tracked since the early 1990s, that proportion has been dropping in recent years, showcasing the benefit of a well-maintained patch management process.

Percentage of phishing attacks using spear phishing attachments
Attackers preferred weaponized attachments, deployed by themselves or in combination with links or spear phishing via service.

Increase in the number of thread hijacking attempts per month
There were twice as many thread hijacking attempts per month in 2022, compared to 2021 data. Spam email leading to Emotet, Qakbot and IcedID made heavy use of thread hijacking.

Percentage of incidents involving phishing for initial access
Phishing operations continued to be the top pathway to compromise in 2022, with 41% of incidents remediated by X-Force using this technique to gain initial access.

*52%*
*31%*
*26%*
*62%*
*100%*
*41%*

# Top initial access vectors
In 2022, X-Force moved from tracking initial access vectors as broader categories, such as phishing and stolen credentials, to the initial access techniques listed within the MITRE ATT&CK Matrix for Enterprise framework. This shift allows X-Force to track important trends more granularly at the technique level. It also provides more readily consumable and cross-comparable data and aligns with the broader industry’s standardization efforts.

**Figure 1:** *A pie chart showing the top initial access vectors X-Force observed in 2022. The largest slice of the pie is "Phishing - Spear phishing attachment" at 25%, followed by "Exploit public-facing application" at 26%, "Phishing - Spear phishing link" at 14%, "External remote services" at 12%, "Valid accounts - Local" at 7%, "Valid accounts - Domain" at 5%, "Hardware additions" at 3%, "Valid accounts - Default" at 2%, "Phishing - Spear phishing via service" at 2%, and "Valid accounts - Cloud" at 2%.*

Top initial access vectors 2022

Phishing (T1566), whether through attachment, link or as a service, remains the lead infection vector, which comprised 41% of all incidents remediated by X-Force in 2022. This percentage holds steady from 2021 after having increased from 33% in 2020. Looking at all phishing incidents, spear phishing attachments (T1566.001) were used in 62% of those attacks, spear phishing links (T1566.002) in 33% and spear phishing as a service (T1566.003) in 5%. X-Force also witnessed threat actors use attachments alongside phishing as a service or links in some instances.

IBM X-Force Red data from 2022 further highlights the value of phishing and mishandled credentials to threat actors. Across 2022’s penetration tests for clients, X-Force Red found that approximately 54% of tests revealed improper authentication or handling of credentials. The X-Force Red Adversary Simulation team regularly performed spear phishing with QR codes targeting multifactor authentication (MFA) tokens. Many organizations lacked visibility into applications and endpoints exposed through identity access management and single sign-on (SSO) portals, such as Okta.

In second place, exploitation of public-facing applications (T1190)—defined as adversaries taking advantage of a weakness in an internet-facing computer or program—was identified in 26% of incidents to which X-Force responded.

**Figure 2:** *A pie chart showing the types of phishing subtechniques as a percentage of total phishing cases observed by X-Force in 2022. "Phishing Attachment" is the largest slice at 62%, followed by "Phishing Link" at 33%, and "Phishing via service" at 5%.*

This correlates to what past Threat Intelligence Index reports referred to as “vulnerability exploitation” and marks a drop from 34% in 2021.

In third place, abuse of valid accounts (T1078) was identified in 16% of the observed incidents. These are cases where adversaries obtained and abused credentials of existing accounts as a means of gaining access. These incidents included cloud accounts (T1078.004) and default accounts (T1078.001) at 2% each, domain accounts (T1078.002) at 5%, and local accounts (T1078.003) at 7%.

Phishing kits lasting longer, targeting PII over credit card data

Credit card information dropped significantly from being targeted 61% of the time in 2021 to 29% of phishing kits in 2022.

IBM Security analyzed thousands of phishing kits from around the world for the second year in a row and discovered kit deployments are operational longer and reaching more users. The data indicates that the lifespan of phishing kits observed has more than doubled year over year, while the median deployment across the data set remained relatively low at 3.7 days.

Overall, the shortest deployment lasted minutes and the longest, discovered in 2022, ran longer than three years. Our investigation found the following:

- One-third of deployed kits lasted approximately 2.3 days last year, more than double the length of the year prior when the same proportion lasted no longer than one day.

- Approximately half of all reported kits impacted 93 users, whereas in 2021, each deployment on average had no greater than 75 potential victims.

- The maximum total victims of one reported phishing attack was just over 4,000, although this was an outlier.

- Almost every reported phishing kit analyzed sought to gather names at 98%. This was followed by email addresses at 73%, home addresses at 66% and passwords at 58%.

- Credit card information dropped significantly from being targeted 61% of the time in 2021 to 29% of phishing kits in 2022.

- Lower instances of phishing kits seeking credit card data indicate that phishers are prioritizing personally identifiable information (PII), which allows them broader and more nefarious options. PII can either be gathered and sold on the dark web or other forums or used to conduct further operations against targets.

The top brands observed being spoofed are made up mostly of the biggest names in tech. X-Force believes this shift from 2021’s somewhat more diverse list is due to improved ability to identify the brands that a kit is configured to spoof, not just the one it’s targeting by default. Many phishing kits are multipurpose, and the brand being spoofed can be changed by altering a simple parameter. For example, a kit can spoof Gmail by default, but a one-line update changes it into an attack spoofing Microsoft.

Stolen credentials for such services are valuable. Gaining access to accounts that victims use to manage entire portions of their online presence can open the door for access to other accounts. Attackers’ focus on this form of initial access is highlighted in the 2022 Cloud Threat Landscape Report, which found a more than threefold increase at 200% of the number of cloud accounts being advertised for sale on the dark web over what was observed in 2021.

**Figure 3:** *A table showing the top spoofed brands in 2021 and 2022. In 2022, the top 10 are: 1. Microsoft, 2. Google, 3. Yahoo, 4. Facebook, 5. Outlook, 6. Apple, 7. Adobe, 8. AOL, 9. PayPal, 10. Office365. In 2021, the top 10 are: 1. Microsoft, 2. Apple, 3. Google, 4. BMO Harris Bank, 5. Chase, 6. Amazon, 7. Dropbox, 8. DHL, 9. CNN, 10. Hotmail.*

Top spoofed brands year over year

Vulnerabilities
Vulnerability exploitation—captured for 2022 as exploitation of public-facing applications (T1190)—placed second among top infection vectors and has been a preferred method of compromise by attackers since 2019. Vulnerabilities were exploited in 26% of attacks that X-Force remediated in 2022, 34% in 2021, 35% in 2020 and 30% in 2019.

Not every vulnerability exploited by threat actors results in a cyber incident. The number of incidents resulting from vulnerability exploitation in 2022 decreased 19% from 2021, after rising 34% from 2020. X-Force assessed that this swing was driven by the widespread Log4J vulnerability at the end of 2021.

Exploitation for access is a key area of research that the team at X-Force Red Adversary Simulation Services pursued to keep simulating advanced threats. The team increased its focus on vulnerability research for exploitation of operating systems (OS) and applications to expand access and perform privilege escalation. This focus was largely due to past exercises with long-standing clients who have hardened traditional Active Directory attack paths and the need to pursue new attack paths.

While vulnerabilities are a common initial access vector, and the industry responds to several major ones in any given year, not every vulnerability is the same. It’s important for decision makers to take a full view of the vulnerability landscape and ensure they’re equipped with the necessary context to understand the real threat a given vulnerability poses to their networks.

Almost 30 years ago and predating the advent of the Common Vulnerabilities and Exposures (CVE) system, X-Force began building a robust vulnerability database. This database is now one of the most comprehensive in the cybersecurity industry. While vulnerabilities are a major risk to security, there are far more reported vulnerabilities than there are known weaponized exploits. Further, despite public attention on zero days, the actual number of known zero days is dwarfed by the total number of known vulnerabilities.

Share of incidents resulting from vulnerability exploitation over the last four years
*2020: 35%*
*2021: 34%*
*2019: 30%*
*2022: 26%*

**Figure 4:** *A line graph showing the total X-Force database of vulnerabilities versus exploits over the past five years. The x-axis shows the years 2018-2022. The y-axis shows the number of vulnerabilities and exploits, ranging from 0 to 30,000. The line for "Sum of total vulnerabilities" increases from 17,923 in 2018 to 23,964 in 2022. The line for "Sum of total exploits" increases from 6,505 in 2018 to 6,290 in 2022.*

Total X-Force database of vulnerabilities versus exploits

Every year sees a new record number of vulnerabilities discovered. The total number of vulnerabilities tracked in 2022 was 23,964 compared to 21,518 in 2021. The trend of year-to-year vulnerability increases has persisted over the last decade. To the benefit of defenders, analysis of our vulnerability database showed the proportion of known, viable exploits to reported vulnerabilities decreasing in recent years—36% in 2018, 34% in 2019, 28% in 2020, 27% in 2021 and 26% in 2022.

These numbers can shift with the exposure of zero days and exploits being developed for older vulnerabilities—sometimes years after they’re identified—and there are several potential explanations behind this decline. First, the establishment of formal bug bounty programs has incentivized the proactive discovery of vulnerabilities within applications. Additionally, a handful of widely popular and well-established vulnerabilities exist that already serve as a means of system exploitation for attackers, reducing the need for threat actors to develop new exploits. The drop is likely due to a combination of multiple factors but doesn’t point to vulnerability exploitation becoming less of a threat.

While the proportion of exploits to vulnerabilities drops, the severity of those exploits X-Force tracks has increased in the last five years. In 2018, 58% of vulnerabilities had a Common Vulnerability Scoring System (CVSS) score of medium, 4.0-6.9 out of 10, compared to just under 36% high, 7.0-9.9. The spread between those two inverted in 2021, and high severity vulnerabilities now account for five percentage points more than those that scored medium.

**Figure 5:** *A stacked bar chart showing the CVSS scores of vulnerabilities in the X-Force database for the years 2018-2022. The chart shows the percentage of vulnerabilities that are critical, high, medium, and low. In 2018, the percentages are: Critical 6%, High 36%, Medium 58%, Low 0.4%. In 2019, the percentages are: Critical 6%, High 38%, Medium 55%, Low 0.4%. In 2020, the percentages are: Critical 4%, High 47%, Medium 49%, Low 0.4%. In 2021, the percentages are: Critical 4%, High 49%, Medium 46%, Low 0.5%. In 2022, the percentages are: Critical 4%, High 47%, Medium 42%, Low 0.6%.*

CVSS scores of vulnerabilities in X-Force database

Still, of all the vulnerabilities X-Force has tracked since 1988, 38% of them rank high, with only 1% coming in at the critical score of 10. Half of tracked vulnerabilities rank medium with the remaining 11% coming in at low, 3.9 and below. These scores alone don’t correlate to the real-world severity of any one CVE, since it doesn’t account for how exploitation is accomplished or if an exploit even exists. However, the scores do help defenders compare vulnerabilities and prioritize how quickly to address them. The Figure 6 graphic on the following page helps to put into perspective the true nature of the vulnerability problem facing the cybersecurity industry.

**Figure 6:** *A graphic showing the growth of vulnerabilities, exploits and zero days since 1988. Also included is a timeline of major events involving vulnerabilities since 1993. The graphic includes three lines: one for vulnerabilities, one for zero days, and one for weaponized exploits. The line for vulnerabilities starts at 0 in 1988 and increases to over 250,000 in 2022. The line for zero days starts at 0 in 1988 and increases to around 7,000 in 2022. The line for weaponized exploits starts at 0 in 1988 and increases to around 80,000 in 2022. The timeline includes the following events: 1993: XFDB precursor; 1997: XFDB (ISS) founded; 1999: CVE founded; 2003: Metasploit created; 2004: Exploit DB created; 2008: Conficker; 2011: Beast; 2012: Crime; 2013: Breach; 2014: Heartbleed, Poodle, Shellshock; 2015: Freak; 2016: Sweet32; 2017: EternalBlue; 2018: Spectre, Meltdown; 2019: BlueKeep; 2020: Sunburst, Supernova, Zerologon; 2021: Log4J, Wreck Sudo; 2022: Follina, ProxyNotShell, Spring4Shell, SynLapse. The graphic also includes a table showing the cumulative vulnerabilities, exploits, and zero days since 1988. The table shows: Total vulnerabilities: 228,167, Total exploited vulnerabilities: 78,156 (34%), Total unexploited vulnerabilities: 150,011 (66%), Total zero days: 7,327 (3%), Critical: 2,746 (1%), High: 86,595 (38%), Medium: 114,480 (50%), Low: 24,274 (11%).*

The vulnerability problem

Operational technology (OT) vulnerabilities
Industrial control systems (ICS) vulnerabilities discovered in 2022 decreased for the first time in two years—457 in 2022 compared to 715 in 2021 and 472 in 2020. One explanation for this may be found in ICS lifecycles and how they’re generally managed and patched. Attackers know that with demand for minimal downtime, long equipment lifecycles and older, less-supported software, many ICS components and OT networks are still at risk of older vulnerabilities. Infrastructure is usually in place for many years longer than standard office workstations, which extends the lifespan of ICS-specific vulnerabilities beyond those that can exploit IT.

# Top actions on objectives
Previously, the X-Force Threat Intelligence Index examined the broad category of top attacks. For 2022, X-Force dissected this classification into two distinct categories: the specific actions threat actors took on victim networks, or adversary action on objective, and the intended or realized effect of that action on the victim, or impact.

According to X-Force Incident Response data, deployment of backdoors was the most common action on objective, occurring in 21% of all reported incidents. This was followed by ransomware at 17% and business email compromise (BEC) at 6%. Malicious documents (maldocs), spam campaigns, remote access tools and server access were discovered in 5% of cases each.

**Figure 7:** *A bar chart showing the top actions on objectives observed by X-Force in 2022. The chart shows the following percentages: Malware - Backdoors: 21%, Malware - Ransomware: 17%, Business email compromise (BEC): 6%, Server access: 5%, Tool - Remote access: 5%, Spam campaign: 5%, Malware - Maldoc: 5%.*

Top actions on objectives 2022

In cases where a backdoor deployment was classified as an action on objective, it’s probable that the threat actor had additional plans when the backdoor was operationalized. Successful intervention by security teams or incident responders likely prevented the threat actor from fulfilling further objectives. Such further malicious activity would likely have included ransomware, as about two-thirds of those backdoor cases had the markings of a ransomware attack.

Increased backdoor deployment may also be due to the amount of money this kind of access can generate on the dark web. Compromised corporate network access from an initial access broker typically sells for several thousands of US dollars. This type of access may be sought by malicious actors looking to make a quick profit by avoiding issues with maintaining access while moving laterally and exfiltrating high-value data. Those malicious actors who lack access to the requisite malware to establish access themselves may also seek backdoors.

Initial access brokers typically attempt to auction their accesses, which X-Force has seen at USD 5,000-10,000, though final prices may be less. Others have reported accesses selling for USD 2,000-4,000, with one reaching USD 50,000. These amounts compare to the significantly lower price for something like a single credit card, seen offered for under USD 10.

Backdoors led to a notable spike in Emotet cases in February and March. That spike inflated the ranking of backdoor cases significantly, as those deployed in this timeframe account for 47% of all backdoors identified globally throughout 2022. Following Emotet’s hiatus from July through November—after which it ramped back up for nearly two weeks at much lower volume—the number of backdoor cases dropped significantly.

**Figure 8:** *A line graph showing the distribution of Emotet cases across 2022. The x-axis shows the months of the year. The y-axis shows the percentage of cases. The graph shows a large spike in cases in February and March, followed by a sharp decline and a small increase in November.*

Distribution of Emotet cases across 2022

Ransomware
Even amid a chaotic year for some of the most prolific ransomware syndicates, ransomware was the second most common action on objective, following closely behind backdoor deployments and continuing to disrupt organizations’ operations. Ransomware’s share of incidents declined from 21% in 2021 to 17% in 2022.

An IBM Security X-Force study revealed there was a 94% reduction in the average time for the deployment of ransomware attacks. What took attackers over two months in 2019 took just under four days in 2021. With attackers moving faster, organizations must take a proactive, threat-driven approach to cybersecurity.

One particularly damaging way ransomware operators distribute their payload across a network is by compromising domain controllers. A small percentage, approximately 4%, of network penetration test findings by X-Force Red revealed entities that had misconfigurations in Active Directory that could leave them open to privilege escalation or total domain takeover. In 2022, X-Force also observed more aggressive ransomware attacks on underlying infrastructure, such as ESXi and Hyper-V. The potentially high impact of these attack methods underscores the importance of securing domain controllers and hypervisors properly.

As ransomware groups and related access brokers come and go, X-Force has seen regular churn in the top groups active in this space. X-Force encountered 19 ransomware variants in 2022, compared to 16 in 2021. LockBit variants comprised 17% of total ransomware incidents observed, up from 7% in 2021. Phobos tied with WannaCry for second at 11%. The top groups in 2022 displaced 2021’s first place REvil, also known as Sodinokibi, with 37% of cases in 2021, and second place Ryuk with 13%, both down to 3%. LockBit 3.0 is the latest variant of the LockBit ransomware family that’s part of a ransomware-as-a-service (RaaS) operation associated with LockerGoga and MegaCortex. LockBit has been in operation since September 2019, and LockBit 3.0 was released in 2022. A significant portion of the LockBit 3.0 source code appears to have been borrowed from the BlackMatter ransomware.

Ransomware attack average duration
*2019: 2+ months*
*2021: 3+ days*

**Figure 9:** *A bar chart showing the ransomware variants and the frequency with which they were observed in X-Force Incident Response engagements in 2022. The chart shows the following percentages: LockBit: 17%, Phobos: 11%, WannaCry: 11%, BlackCat: 9%, Conti: 6%, Djvu: 6%, Babuk: 6%, 5x2tr: 3%, Hive: 3%, DefrayX: 3%, Vice Society: 3%, Makop: 3%, MedusaLocker: 3%, Venom: 3%, Ryuk: 3%, Cat4er: 3%, Venus: 3%, Lizard: 3%, REvil: 3%.*

2022 ransomware variants and frequency

Researchers first discovered Phobos ransomware in early 2019. Based on similarities in code, delivery mechanisms, exploitation techniques and ransom notes, Phobos was identified as a fork of the previously known ransomware families Crysis and Dharma. Phobos has been commonly used for smaller-scale attacks, which involve lower ransom demands. Email phishing campaigns and exploitation of vulnerable Remote Desktop Protocol (RDP) ports are the main distribution methods observed for Phobos.

WannaCry, first seen in 2017, spreads itself by using EternalBlue to exploit the vulnerability in the Microsoft Server Message Block 1.0 (SMBv1) server (MS17-010). Several cases of WannaCry or Ryuk that X-Force saw in 2022 were the result of infections from three to five years ago and occurred on old, unpatched equipment, highlighting the importance of proper cleanup after such events.

Business email compromise (BEC)
BEC held its rank of third in 2022 with 6% of incidents to which X-Force responded. This rank is slightly lower than 8% of attacks in 2021 and 9% for fifth place in 2020. It displaced 2021’s second place attack, which was server access attacks. This type of attack occurs when an attacker gains access to a server for unknown end goals—which in 2022 was more granularly classified by what type of access those actors achieved. Spear phishing links were used in half of BEC cases to which X-Force responded. Malicious attachments and abuse of valid accounts were used to enable BEC attempts in 25% of cases each.

# Top impacts
X-Force also took a closer look at the effect of incidents on victim organizations to better understand the impact that threat actors sought to have through the incidents to which X-Force responded. With this information, organizations can get a better understanding of the most common impacts to plan responses to potential future incidents more effectively.

The analysis found that more than one in four incidents aimed to extort victim organizations—making it the top impact observed across incidents remediated by X-Force. The observed extortion cases were most frequently achieved through ransomware or BEC, and often included the use of remote access tools, cryptominers, backdoors, downloaders and web shells.

**Figure 10:** *A bar chart showing the top impacts X-Force observed in incident response engagements in 2022. The chart shows the following percentages: Extortion: 27%, Data theft: 19%, Credential harvesting: 11%, Data leak: 11%, Brand reputation: 9%.*

Top impacts 2022

**Figure 11:** *A pie chart showing the percentage of extortion cases by industry X-Force observed in incident response engagements in 2022. The chart shows the following percentages: Manufacturing: 30%, PBC services: 22%, Finance & insurance: 13%, Energy: 13%, Retail & wholesale: 9%, Transportation: 4%, Media & telecom: 4%, Education: 4%.*

Percentage of extortion cases by industry 2022

Data theft came in second and accounted for 19% of all incidents that X-Force remediated. Credential harvesting that led to stolen usernames and passwords and required corresponding mitigations accounted for 11%. Incidents where X-Force could identify targeted information actually leaked after being stolen was less common than the theft of data at 11%. Impacts to brand reputation, such as disruption to the services clients provide to their customers, accounted for 9% of incidents. See Appendix for the full list of impacts X-Force tracked. Incidents that impacted victims’ brand reputation were mainly distributed denial of service (DDoS) attacks, which are also frequently used to extort victims to pay money to stop the attack.

Notable developments in online extortion
| Year | Event | Tactic |
|---|---|---|
| 2013 | Cryptolocker—one of the first major ransomware outbreaks | Data encryption |
| 2014 | DDoS 4 Bitcoin, Armada Collective | Ransom DDoS |
| 2015 | Chimera ransomware adds threat of leaking stolen data online | Double extortion |
| 2017–18 | BitPaymer and SamSam | Big game hunting |
| 2020 | Vastaamo ransomware case | Triple extortion |

While extortion is most commonly associated with ransomware today, extortion campaigns have included a variety of methods to apply pressure on their targets. These include DDoS threats, encrypting data and, more recently, double and triple extortion threats combining several previously seen elements.

Another tactic that at least one ransomware group experimented with starting in 2022 was making the data they had stolen more accessible to downstream victims. By making it easier for secondhand victims to identify their data among a data leak, operators seek to increase the subsequent pressure on the organization targeted by the ransomware group or affiliate in the first place. In 2023, X-Force expects to see threat actors experimenting with enhanced or novel downstream victim notification to increase the potential legal and reputational costs of an intrusion.

Often, both defenders and victims of cyberattacks focus on the observed impacts to an organization by threat actors. However, it’s important to consider the intentions of threat actors, their capabilities and how they evolve over time. This approach enables better discernment of what the next evolution of capabilities may be. Given the ever-expanding menu of extortion options and ransomware actors’ primary goal of financial gain, the X-Force team assesses that threat actors will continue to evolve and expand their extortion methodologies to find new ways to pressure victims into paying.

# Cyber-related developments of Russia’s war in Ukraine
Russian state-sponsored cyber activity following Russia’s invasion of Ukraine has not, as of this publication, resulted in the widespread and high-impact attacks originally feared by Western government entities. However, Russia has deployed an unprecedented number of wipers against targets in Ukraine, highlighting its continued investment in destructive malware capabilities. Furthermore, the invasion has led to the resurgence of hacktivist activity undertaken by groups sympathetic to either side, as well as a reordering of the Eastern European cybercriminal landscape.

Considering Russia’s demonstrated advanced capabilities for cyberattacks against critical infrastructure since 2015, international cybersecurity agencies issued a warning in April 2022. The warning mentioned potentially significant cyber operations and related disruptions in Ukraine and elsewhere. X-Force assessed the most significant threats that have emerged include the return of hacktivism and wiper malware, as well as