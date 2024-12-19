# GRIT 2023 ANNUAL REPORT

## Ransomware Report

### Contents
[2023 Threat Group Breakdown](#2023-threat-group-breakdown)
[Ransomware in Depth: Major Events, Observations, and Trends in 2023](#ransomware-in-depth-major-events-observations-and-trends-in-2023)
[Final Thoughts](#final-thoughts)
[Appendix](#appendix)
[2023 Ransomware Activity “by the numbers”](#2023-ransomware-activity-by-the-numbers)
[Signposts of Ransomware Activity and 2024 Outlook](#signposts-of-ransomware-activity-and-2024-outlook)
[Annual Ransomware Summary](#annual-ransomware-summary)
[Methodology](#methodology)

### Methodology
Data collected for this report was obtained from publicly available resources, including information disclosed by threat groups themselves, and has not been validated by all alleged victims. As such, the number of publicly observed attacks and the actual number of attacks conducted may not be equal. Some groups do not publicize all of their victims, and almost all groups offer an option to withhold announcement if the victim pays a ransom within a specified timeframe or will remove posted details of the victims once a ransom has been paid. Additionally, some groups include incomplete information about their victim or claim an attack despite having successfully attacked only a small subset of their target. For these reasons, the data in this report is useful in aggregate, but should be evaluated as a report consisting of data sources that have variability. Despite this variability, we still consider this report as an accurate representation of the ransomware threat landscape.

We note that this report includes data and analysis of several groups that may be better described as "extortion" groups rather than "ransomware" groups. These groups may eschew encryption and instead focus only on data exfiltration and extortion, or may not perform intrusion operations of any kind, instead extorting or re-extorting organizations based on historically compromised data. While these groups do not deploy ransomware, we are including them in our reporting due to their relationships with other ransomware groups and their impact on the extortion-based cybercrime environment.

In keeping with best practices in analytic tradecraft, we have we have made efforts to clearly distinguish between our assessments and the underlying factual evidence which supports it. Statements beginning with or containing the words “we assess” should be considered analytic judgments based on the expertise and experience of GRIT’s analysts coupled with the strength and corroboration of underlying sources. Statements of probability – such as “likely,” “almost certainly,” and “probably” reflect levels of confidence in an analytic assessment based on the strength and corroboration of underlying sources. “Unlikely” and similar terms reflect low confidence, “likely” and “probably” reflect moderate confidence, and “almost certainly” reflect high confidence within the scope of this report.

### Ransomware Summary
In last year’s Annual Ransomware Report, GRIT identified ransomware as "the most prolific and impactful threat to our networks, data, and operational capabilities," with more than 2,500 publicly posted victims observed in 2022. While we predicted a continuing steady increase in ransomware activity, 2023 outpaced our expectations, with year-over-year victim volume nearly doubling, driven in part by multiple mass exploitation campaigns impacting hundreds of organizations.

In total, we observed 63 distinct ransomware groups leverage encryption, data exfiltration, data extortion, and other novel tactics to compromise and publicly post 4,519 victims across all 30 of GRIT's tracked industries, and in 120 countries.

Relative to the remainder of the year, Ransomware’s operational tempo in 2023 began slowly, with a progressive increase in victim posting building up to a record high of 1,353 victim posts in Q3, followed by a comparatively mild 1,170 victim posts in Q4. As Q4's drop-off does not appear to correlate with any significant changes in the ransomware ecosystem, results from January 2024 may yet show whether victim volume will decrease, remain constant, or return to form by increasing in the new year.

#### Key Highlights
The United States was by far the most impacted country in 2023. Among posted victims, 2,199 were US-based organizations, accounting for 49% of all observed ransomware attacks in 2023. Eight out of the ten most impacted countries were within North America and Europe, with Brazil and Australia as the sole outliers. The same "top ten" most impacted countries were home to 76% of all observed victim organizations, of which 27% impacted non-US countries.

From an industry perspective, GRIT observed most impacts affecting a limited subset of industries. 62% of all observed victims belong to one of the "top ten" most-impacted industries, with Manufacturing and Technology remaining the two most-impacted industries; Manufacturing and Technology represented 12.9% and 7.9% of all victims, respectively.

In line with GRIT's taxonomy for classifying ransomware groups, long-term Established groups accounted for the overwhelming majority of observed victims (85%), followed by Developing groups (10%). Ephemeral and Emerging groups, as the newest and shortest-term entrants, lagged behind their maturing counterparts but still posed a significant threat to worldwide organizations, exacerbated by less "reliable" actors and frequently recycled malware. We note that for 2023, we have attributed only one Rebrand group in Black Suit, stemming from the now inactive Established group, Royal. Conversely, we have not definitively attributed any Splinter groups in 2023, though groups that we currently classify as Emerging or Ephemeral may, in time, show indications of having Splintered from other organizations.

### ANNUAL
### Ransomware Summary (cont’d)
Tactically, 2023 presented repeated opportunities for new entrants in the ransomware ecosystem. This was achieved either through reduced technical barriers such as the recycling of leaked ransomware builders and commodity malware, or the recycling of previously leaked data for re-extortion and claims of attacks that never were. For those established groups with resources and technical expertise, exploitation of high-severity and zero-day vulnerabilities provided a reliable means of exploiting victims at scale, a trend we assess as likely to continue into 2024 as a means of overcoming improvements in security.

Law enforcement disruptions and rumors thereof circulated the ransomware community in 2023, culminating in a highly publicized takedown of Alphv's dark web leak site. Regrettably, Alphv chose not to go down without a fight, and its continued presence and operations highlight the resiliency of Ransomware's most entrenched groups. Targeting of victims previously considered "off limits”, such as schools and hospitals, is expected to continue, as are attempts to attract additional attention to high-impact ransomware attacks. This brinksmanship, which aligns with several of the novel coercive techniques we observed in 2023, will likely attract the attention of both law enforcement and potential affiliates over time.

### ANNUAL
### 2023 Ransomware Activity by the Numbers
**Total Publicly Posted Ransomware Victims**
4,519
**Number of Tracked Ransomware Groups**
63
**Average Posting Rate (per day)**
12.4

Activity ramped up considerably throughout Q1 into Q2, then held steady at around 100-140 posted victims per week for the remainder of 2023, with the exception of observable decreases in early August and October. An observable increase in victim volume in early September stems from a large "dump" of victim postings by the groups RansomedVC and Cactus.

Substantial increases in victim volume can be observed in March, June, and July following Clop's mass exploitation campaigns that impacted enterprise users of two distinct managed file transfer applications.

*A bar graph shows the total posts per month from January to December 2023. The graph shows a steady increase from January to March, a peak in June and July, and a decrease in August, followed by a rise in September and a subsequent decrease for the remainder of the year.*

**Total Posts**
4,519
**Average Posts / Week**
86.9
**Total Groups**
63
**Average Groups / Week**
16.6

A quarterly breakdown of 2023's data shows a consistent and significant uptick in the volume of victims posted relative to the two preceding years. Emblematic of this increase, Q3 of 2023 resulted in a higher volume of victim postings than the Q3 totals of 2021 and 2022 combined.

The rate of publicly posted ransomware victims from 2021 to 2022 saw a 4.2% decrease in activity year over year. Comparatively, from 2022 to 2023, ransomware victim posting increased by a staggering 80.1%. While mass exploitation campaigns contributed substantially to this large increase, such attacks contributed just over 5% of the total victims for 2023, demonstrating this year's significant increase in ransomware activity overall.

*A bar graph shows the victim posting rates per quarter from 2021 to 2023. The graph shows a consistent increase in victim postings each year, with a significant jump in Q3 of 2023.*

### Most Impactful Ransomware Threat Groups - 2023
*A bar graph shows the victim posting rates per quarter for the top 10 most impactful ransomware groups in 2023. The graph shows that LockBit consistently had the highest number of victim postings throughout the year, followed by Alphv and Clop.*

Following a slow close to 2022, LockBit’s activity surged considerably in the first quarter of 2023, and the group maintained a steady pace of operations throughout the year, even during periods when other groups were far less active. GRIT observed a slower summer from LockBit compared to their average, possibly indicating conflicts with affiliates, processes, or or infrastructure, consistent with problems described in open security reporting. This may have contributed to LockBit’s announcement in November, in which LockBit publicized a "policy" change that indicated the minimum acceptable ransom demand would be directly related to the victim organization revenue. Additionally, on November 15th, 2023, LockBit suffered an outage affecting all of it’s known Dark Web infrastructure. The issue was resolved later that day, with no indications as to what caused the outage.

Including Clop's mass exploitation campaigns and the May 2023 bulk posting of victims by 8Base, LockBit’s share among the “top 10” settled at 32% for the remainder of the year.

The Established group Royal began the year with a high and consistent volume of victims before a precipitous drop in Q3, when their leak site went dark. The group is believed to have since Rebranded as "Black Suit", which began continuing operations in Q4.

Play, a group responsible for only around 1% of observed victims in 2022, quietly and significantly increased their operations to become the fourth-most prolific group in 2023, in terms of observed victims.

GRIT observed the 6th- and 7th-most victims from Bianlian and Akira, despite the publication of ransomware decryptors which would degrade the effectiveness of encryption as leverage. Both groups appear to have quickly pivoted to extortion based solely on exfiltrated data and have maintained a significant operational capacity.

While retaining its place as the second-most impactful ransomware group, Alphv earned significant media coverage this Fall after claiming breaches against MGM Resorts and Caesars International through an elaborate social engineering campaign conducted by the prominent threat group, Scattered Spider.

*A stacked area chart shows the cumulative victims by threat group from January 1st to December 31st, 2023. The chart shows that LockBit had the highest number of cumulative victims, followed by Alphv, Clop, and Play.*

Interestingly, while Rhysida (Developing) was not a leading group in terms of total posted victims, coming in 13th amongst competing groups, the group caused disproportionate impacts on traditionally sensitive industries, including Education, Healthcare, and Government sectors. 46 of Rhysida's 74 posted victims belong to one of these three industries.

Among Manufacturing industry victims, the US was impacted five times as much as the next highest country, Germany. Specifically, the US saw 265 impacted Manufacturing victims, while Germany saw a significantly lower number of Manufacturing victims at 48. Manufacturing was the most impacted industry for almost every month in 2023, excluding May, when it placed behind Technology by a single observed victim.

The "top 10" most impacted industries accounted for 2,794 (62%) of all posted victims and were impacted by all but one of the groups tracked by GRIT – Free Civilian, a group with only two posted Ukrainian victims in late January 2023. Free Civilian, a self-proclaimed pro-Russian hacktivist group, has been reported as a Russian GRU persona by Microsoft and Mandiant. Given the typical diversity of impacted victims, limited victim diversity may serve as a future indicator for government-sponsored “faux-ransomware” operations.

Alphv's status as one of the leading ransomware groups impacting the Healthcare industry may continue after their response to law enforcement efforts to shut down their operations. After restoring operations, Alphv announced a change to affiliate rules, allowing the targeting of critical infrastructure. This may lead less scrupulous affiliates to disproportionately target hospitals and other healthcare providers using Alphv's ransomware.

### Most Impacted Industries - 2023
*A bar graph shows the number of public victims for the top 10 most impacted industries in 2023. The graph shows that Manufacturing was the most impacted industry, followed by Technology and Healthcare.*

1- **Manufacturing**
*   LockBit
*   Alphv
*   Play
2- **Technology**
*   LockBit
*   Clop
*   Alphv
3- **Healthcare**
*   LockBit
*   Alphv
*   Bianlian
4- **Education**
*   LockBit
*   Rhysida
*   Akira
5- **Retail & Wholesale**
*   LockBit
*   Play
*   Alphv

### Geographic Breakdown of Ransomware Victims (2023)
1.  United States
2.  United Kingdom
3.  Canada
4.  Germany
5.  France
6.  Italy
7.  Australia
8.  Spain
9.  India
10. Brazil

Most Impacted:
Established ransomware groups dominated the ransomware ecosystem when compared to less mature groups as classified in our taxonomy. Despite representing less than a third of all distinct observed groups operating during 2023, Established groups generated a disproportionately high victim volume.

Established groups eventually ceded some of their dominant market share during Q4, with a greater portion of observed victims stemming from operations of Developing and Emerging groups. GRIT has previously observed a slight slowdown in the operations tempo of Established groups over the preceding two years. A portion of the decrease in activity could also potentially be attributed to law enforcement's temporary disruption of the Established group Alphv in December 2023.

Only one group, Black Suit, was classified as a Rebrand during 2023, whose victims account for a minute subset of the overall 2023 data. While other groups may be later determined by GRIT to be Rebrands or Splinter groups, only Black Suit's Rebrand was sufficiently attributable.

## 2023 Threat Group Breakdown
*A line graph shows the post rates per month for different group types from January to December 2023. The graph shows that Established groups consistently had the highest post rates, followed by Developing groups.*

The number of days in which each group type was active in 2023 paints a clear picture of the distinction between them within GRIT's taxonomy. “Days active” was measured by the number of distinct dates on which each group type updated their data leak sites with additional victims.

Established groups, which most frequently follow the Ransomware-as-a-Service model, generally have multiple affiliates acquiring victims at any given time, which allows them to post a near-continuous flow of victims to their data leak sites. Such groups also possess greater resources and staffing, which could support more timely and frequent updates.

Ephemeral groups, by contrast, are short-lived, resulting in minimal victim postings over short periods of time, as indicated by their minimal activity on data leak sites.

Developing groups – defined by GRIT's taxonomy as nascent groups focused on evolution, improvement, and TTP refinement – have demonstrated continuing operations and the ability to generate a consistent stream of victims. While not as well-resourced or entrenched as Established groups, we still expect to see higher levels of activity from these groups than short-term Ephemeral groups or newly arrived Emerging groups. The observable days of activity for Developing groups support this definition, presenting a substantial level of activity second only to Established groups.

### 2023 Activity by GRIT Taxonomy Classification
| GRIT Taxonomy Group Type | Days Active in 2023 (Across All Groups) |
| :----------------------- | :------------------------------------ |
| Established              | 353                                   |
| Rebrand                  | 14                                    |
| Developing               | 160                                   |
| Ephemeral                | 10                                    |
| Emerging                 | 19                                    |

Emerging groups were the only group type with Government amongst their most victimized industries, and Government victims were, in turn, the most impacted by Emerging groups. Emerging groups may be entirely new to the ransomware ecosystem and select targets differently than more mature groups, who may avoid government targets to avoid undesired attention from law enforcement.

Healthcare targets rose in popularity among both Established and Developing groups in 2023. Healthcare victims often hold a large amount of PII data, rendering them a high-value target for more mature ransomware groups capable of exploiting or extorting based on large volumes of data. While the Healthcare industry was once considered off-limits and less frequent as targets by Established groups, we have witnessed this norm eroding in 2023.

Manufacturing remains one of the most highly victimized industries across most group categories. This is likely driven in part by cybersecurity challenges within manufacturing organizations, as well as the fact that these organizations often suffer significant costs from operational disruption of manufacturing processes, potentially rendering them more likely to pay ransoms in support of a fast recovery.

### Industry Victims by Taxonomy Classification
**Established**
| Victim Industry           | Number of Public Victims |
| :------------------------ | :----------------------- |
| Manufacturing             | 440                      |
| Technology                | 274                      |
| Healthcare                | 158                      |
| Banking and Finance       | 213                      |
| Retail and Wholesale      | 205                      |

**Rebrand**
| Victim Industry                 | Number of Public Victims |
| :------------------------------ | :----------------------- |
| Government                      | 13                       |
| Manufacturing                   | 11                       |
| Entertainment, Hospitality, & Tourism | 8                        |
| Healthcare                      | 8                        |
| Technology                      | 5                        |

**Ephemeral**
| Victim Industry     | Number of Public Victims |
| :------------------ | :----------------------- |
| Manufacturing       | 12                       |
| Consulting          | 6                        |
| Legal               | 6                        |
| Construction        | 5                        |
| Education           | 5                        |

**Developing**
| Victim Industry      | Number of Public Victims |
| :------------------- | :----------------------- |
| Manufacturing        | 53                       |
| Healthcare           | 37                       |
| Education            | 35                       |
| Technology           | 30                       |
| Construction         | 25                       |

**Emerging**
| Victim Industry                 | Number of Public Victims |
| :------------------------------ | :----------------------- |
| Government                      | 13                       |
| Manufacturing                   | 11                       |
| Entertainment, Hospitality, and Tourism | 8                        |
| Healthcare                      | 8                        |
| Retail and Wholesale            | 205                      |

Relative to their share of the ransomware ecosystem, Developing and Emerging groups disproportionately impacted Healthcare organizations more often than Established groups. Healthcare has historically been considered “off limits” for some ransomware programs as this brings negative press coverage and extra attention from law enforcement agencies. Despite this, Established groups saw a relative increase in Healthcare victims from the previous year.

Emerging groups disproportionately victimized organizations within the Retail and Wholesale industry – an industry whose market value increased from $71.8 Billion to $77.2 Billion, according to the Business Research Company. This 7% increase in market value, coupled with a propensity for weaker cybersecurity postures among mid-size organizations, could make this industry a more appealing target for ransomware groups.

Manufacturing consistently remains the most affected industry across all group classifications. Over 20% of victims belong to the manufacturing industry across all group classifications except Emerging groups.

*A stacked bar chart shows the percentage of industry victims by taxonomy classification. The chart shows that Manufacturing was the most impacted industry across all group classifications except for Emerging groups.*

### Geographic Victims by Taxonomy Classification
*A series of maps show the geographic distribution of victims by taxonomy classification. The maps show that the United States was the most impacted country across all group classifications.*

**Top 5 Countries By Taxonomy Classification**
| Established | Developing | Emerging | Ephemeral | Rebrand |
| :---------------- | :---------------- | :---------------- | :---------------- | :---------------- |
| 1. United States | 1. United States | 1. United States | 1. United States | 1. United States |
| 2. United Kingdom | 2. United Kingdom | 2. Canada | 2. Italy | 2. Germany |
| 3. Canada | 3. Germany | 3. Italy | 3. Canada | 3. Canada |
| 4. Germany | 4. Italy | 4. Jamaica | 4. Argentina | 4. United Kingdom |
| 5. France | 5. Canada | 5. Netherlands | 5. Germany | 5. Australia |
|  |  | 5. United Kingdom |  |  |

The United States was the most impacted country across all group classifications, reflecting its status as an attractive target for ransomware groups from inception through maturity. This is likely due to the perception of victim organizations in the US as more likely to pay ransoms and the profit-maximizing nature of ransomware operations.

Emerging and Ephemeral groups appear to target more victims outside of the Global North, potentially limited by language barriers or technical proficiency, or to maintain a lower profile while beginning operations. As groups progress across the maturity spectrum, victim concentration appears to shift towards North American and Western European targets.

Throughout 2023, GRIT hypothesized that the price of Bitcoin may correlate with ransomware victim posting rates. As we closed out the year, we examined the year's complete data to validate or refute this hypothesis.

A cursory review of victim posts and Bitcoin prices across weekly intervals in 2023 reveals two possible focal points. The first is the general trend of an overall rise of Bitcoin value appearing to correlate with an increase in ransom victim posts during the first three months of the year, along with a steady increase in ransomware reports.

The second is an observable and dramatic shift between the rise of Bitcoin value in contrast with a decline in victim reports from October until the end of the year.

## Ransomware in Depth: Major Events, Observations, and Trends in 2023
*A line graph shows the rate of posted ransomware victims versus the price of Bitcoin in USD in 2023. The graph shows a general correlation between the two, with a noticeable divergence in the last quarter of the year.*

Methodically structuring our data painted a clearer picture and allowed us to better view trends with less noise. Firstly, Clop’s mass exploitation campaigns resulted in the posting of 54 different victims at one time on March 18. This mass exploitation campaign is abnormal and skews the data that would otherwise be indicative of overall operational tempo. Similarly, the Developing group 8Base debuted their data leak site on May 23rd, with 66 victims posted simultaneously. Those victims were almost certainly acquired throughout the preceding months, likewise, skewing our data. These victims were removed from the associated graph to better demonstrate the overall trend in ransomware operational tempo during 2023.

We calculated a 4-day period simple moving average to better normalize victim post data and account for variances between dates of initial compromise and the date of a victim's post to a group's site.

Comparing this moving average with the price of Bitcoin, a much stronger correlation can be observed between posting rates and Bitcoin value. Supporting this observable correlation through data, we see a correlation coefficient of .565, demonstrating a moderate correlation. Limiting our focus to just the data from January through September before October's drop further yields a 0.747 correlation coefficient, reflecting a strong correlative relationship between victim post rates and Bitcoin value over time.

*A line graph shows the rate of posted ransomware victims versus the price of Bitcoin in USD in 2023, with outliers removed. The graph shows a stronger correlation between the two, with a noticeable divergence in the last quarter of the year.*

In reviewing the decreased correlation from October through the end of the year, we considered the root cause and the drivers of our hypothesis, searching for potential explanations. While we cannot conclusively rule out other drivers, we note that Bitcoin value surged during this time period, driven by announcements that the US Securities and Exchange Commission (SEC) may approve Bitcoin futures exchange-traded funds (ETF), which would provide a path for investors to purchase Bitcoin and Bitcoin derivatives through stock market exchange services.

Although we cannot affirm the motivations and drivers of individual ransomware actors, we note our findings as potentially suggestive of ransomware group activity increasing with interest in Bitcoin procurement over time, with increased activity correlating a moderate to high amount during periods of value growth in the cryptocurrency. We observed a similar correlation between the price of Bitcoin and the posting rates of ransomware groups during our 2022 ransomware report, which strengthens our assessment of a relationship between the two data sets, as this now appears to be a year-over-year trend. The dataset in 2022 did not experience the end-of-the-year separation between the trendlines as did 2023’s data.

We note and acknowledge that we lack insight into the number of ransomware victims that pay ransoms across the year and that the addition of such data may substantially impact or change our findings.

*A line graph shows the rate of posted ransomware victims versus the price of Bitcoin in USD in 2023, with outliers removed. The graph shows a stronger correlation between the two, with a noticeable divergence in the last quarter of the year.*

*A line graph shows the rate of posted ransomware victims versus the price of Bitcoin in USD in 2023, with outliers removed. The graph shows a stronger correlation between the two, with a noticeable divergence in the last quarter of the year.*

### Major Events in Ransomware: 2023 at a Glance
| Date           | Event                                     |
| :------------- | :---------------------------------------- |
| January 16     | Bianlian Decryptor Released               |
| February 8     | Clop's GoAnywhere Campaign                |
| March 29       | 3CX Supply Chain                          |
| June 1         | Clop's MOVEit Campaign                    |
| August 29      | Qakbot Disrupted                          |
| September 18   | Scattered Spider Casino Attacks           |
| October 7      | Reignition of Israel - Palestine Conflict |
| December 15    | New SEC 8-K Rules Take Effect             |
| December 19    | Alphv Disruption                          |

### Major Events in Ransomware: Clop’s MOVEit Campaign
Clop's mass exploitation of Progress Software's MOVEit managed file transfer software impacted hundreds of victims across multiple industries in a lightning campaign, with impacts continuing throughout the Summer. The incident would go on to become one of the most reported cybersecurity stories of the year, with reporting providing information ranging from technical details of the exploit through to the ensuing fallout and data publication. Notably, the campaign mirrors earlier Clop mass exploitation campaigns, with the group executing an elaborate, coordinated plan to exploit previously unknown vulnerabilities, resulting in data theft and extortion for profit.

The patience and planning demonstrated by the group in this case and other mass exploitation campaigns that rely on "zero-day" vulnerabilities are crucial to maximizing impact and revenue extraction before an associated vulnerability can be discovered and patched. To support Clop's "all at once" approach to exploitation, the group automated and tested a process that would extract all available data held by victim companies that ran the impacted application exposed to the internet. As the operation came to light in early June, Clop updated their data leak site with a generic message inviting anyone who believed that they might have been affected to reach out to them to prevent the publication of sensitive data collected in the campaign. This approach likely reduced the time burden of contacting individually impacted victims and initial communications unlikely to lead to settlement.

While the group worked through any ensuing negotiations with victims and began posting the data of non-compliant organizations to their data leak site, they very likely encountered issues with hosting the substantial amount of exfiltrated data on their existing infrastructure, facing limitations of the onion protocol, which hosted their site and the illegal nature of the data's possession. With necessity as the mother of invention, Clop would go on to experiment with alternative hosting strategies with varying levels of success. The group tried uploading data on a per-victim basis to clearnet sites hosted on domains directly naming the victim. This approach gained headlines, but the process was likely deemed too resource-intensive for Clop, who ultimately only used this approach on a handful of victims.

As an alternative strategy, the group also hosted victim data in a series of Torrent files. This strategy leveraged the inherently distributed nature of the Torrent protocol to make a more reliable, albeit significantly slower, solution to sharing stolen data. These actions by Clop demonstrate the difficulty of pulling off a true successful mass exploitation campaign, including managing "long tail" logistical considerations such as data storage. In spite of early issues, the incident would go on to be considered one of if not the largest single incident of data theft in history. Should mass exploitation campaigns spread as a tactic to other threat groups, Clop may prove to be a model for this style of attack and associated scale.

### Major Events in Ransomware: Scattered Spider attacks Major Casinos
In September 2023, two of the largest entertainment companies in the country, MGM Resorts International and Caesars Entertainment, confirmed downtime caused by ransomware attacks. As details emerged, the two attacks seemed to share a common thread, a connection with a threat group and new affiliate of Alphv, referred to as Scattered Spider by security researchers. Alphv called public attention to the attack by posting a diatribe to their data leak site in an attempt to place pressure on MGM after they refused payment. After weeks of downtime, MGM reported that their losses in this single attack would exceed $100 million USD. Unconfirmed details also emerged about the method of ingress for both the MGM and Caesars attacks; both were said to be a result of social engineering by Scattered Spider, which is known for its skill in English-language social engineering to circumvent Identity and Access Management.

A frequent tactic in this space, and one employed by Scattered Spider in the past, is breaching network accounts via calls to an organization’s help desk. Threat actors, armed with information about an employee obtained from LinkedIn and a convincing story, aim to exploit established account recovery processes to gain access to privileged user accounts at a target organization. Social engineering tactics are as effective as they are hard to detect, and the strongest prevention for such attacks is policy and training – both human elements attempting to compensate for technological gaps. Of course, social engineering as a method of initial access is not new to ransomware actors. Phishing, which is also considered a form of social engineering, continues to pose a threat to every organization with an email presence. However, as email filtering technology improves and users become more knowledgeable, their impact is often limited. Ransomware groups seem to have adjusted to these headwinds, but actors like Scattered Spider show there is still a potential for large-scale compromises via exploitation of the human attack surface.

### Major Events in Ransomware: LockBit’s new Affiliate Rules
In September, LockBit, the most prolific ransomware group of 2023, announced a new set of affiliate rules regarding the negotiation of ransoms with future victims. These new rules, which the group presented in a poll earlier in the year to collect affiliate feedback, implemented significant guardrails around how individual affiliates may price and negotiate ransoms. The new rules first define a sliding scale based on the victim’s revenue to determine how high an affiliate must set their initial extortion demand. Furthermore, once the initial demand is calculated, the new rules forbid affiliates from negotiating discounts in excess of 50%. These actions are seemingly motivated by a reduction in ransom payments, a trend that could ultimately affect LockBit leadership’s revenue. LockBit seems to have made these new rules effective starting October 1.

### Major Events in Ransomware: SEC Updates Guidance on incident notifications
On July 26th, 2023, the US Securities and Exchange Commission (SEC) announced new rules regarding the disclosure of “material” cybersecurity incidents experienced by public companies. The new rules, which were made effective December 18, 2023, provide guidance around how quickly a victimized organization must notify the public and shareholders of a cybersecurity incident. Specifically, public companies now must file an SEC Form 8-K with details of the incident’s nature, scope, and timing within four days of it becoming “material.” These new rules have already significantly influenced how organizations respond to ransomware and other forms of cybersecurity attacks.

In the past, public companies have provided notice to shareholders about cyberattacks for the purpose of informing them about potential impacts to the organization’s “bottom line.” With the advent of the new SEC rule, companies are forced to provide notice on a shorter timeline and in greater detail. Ultimately, this puts added pressure on organizations affected by ransomware to identify materiality of a given breach; the new notification requirements provide protection for both shareholders and individuals who may have personal data compromised. By shedding light on incidents that might otherwise be concealed, the new SEC rule aims to bring more accountability to organizations victimized by ransomware.

### Major Events in Ransomware: Law Enforcement Disruption of Alphv
Starting as early as December 8th, 2023, and culminating in a seizure message posted to their data leak site on December 15th, several arms of United States and international law enforcement cooperated to disrupt the Alphv, also known as Black Cat, Ransomware-as-a-Service (RaaS) operation. The main impact to the group was the seizure of private keys for over 900 Tor sites operated by Alphv, leading to their eventual shutdown and takeover. In addition, law enforcement was able to capture decryption keys for around 500 recent victims of the RaaS group, meaning that any organizations affected by the group in a several-month timespan could potentially recover their encrypted data without cooperating with Alphv.

The disruption immediately sent shockwaves throughout the cybersecurity industry. While many celebrated the apparent takedown, Alphv quickly attempted to restore their operations. The law enforcement actions against the group have not yet resulted in arrests of  Alphv affiliates or leadership, leaving Alphv operators to remain active. Several hours after the Alphv data leak site was changed to a law enforcement seizure notice, the site changed again, this time to a message from Alphv. This “unseizure,” appears to have occurred as a result of Alphv maintaining access to the keys needed to update the content served by the group’s Onion URL. The resulting message from Alphv, written fully in Russian, taunted law enforcement and advised their affiliates that they remained unscathed.

The group pointed visitors to a new Tor site, not under the control of law enforcement, and defined several new rules for operations going forward. Primarily, the group dramatically changed their payment structure for affiliates, who would now receive 90% of any ransom payments they generate. This change was likely motivated by the need to prevent a departure of affiliates who no longer trust the group following the law enforcement seizure. The 90% affiliate share offered by Alphv also contrasts with Lockbit’s stated shares of 60-80% - most likely an attempt to motivate affiliates to stay with the Alphv program instead of moving to their largest competitor. Alphv also announced that they would no longer be negotiating discounts with victims, and that they would be removing rules preventing the targeting of critical infrastructure. While law enforcement actions in this case had a noticeable impact on the ongoing operations of one of the most prolific ransomware groups, Alphv continues to maintain operations today.

### Major Events in Ransomware: Published Decryptors impact Ransomware Operations
Besides law enforcement arrests, one of the biggest disruptors to ransomware operations continues to be the threat of a public decryptor, either from reverse engineering, because of a cryptographic weakness, or intentional and unintentional leaks. The business model of ransomware groups depends on the group or affiliates being the only holders of decryptors, with the resulting victim need used as leverage to extort the victim for payment.

Early in January 2023, a team at Avast released a free decryptor for BianLian’s ransomware. Their program leveraged a flaw in the group’s encryption binary to ultimately guess and implement the key for decryption in a reasonable amount of time, given access to the encrypting binary. After seeing success, Avast released another decryptor in June, this time for the then-Emerging group Akira. Both events led to obvious and immediate changes in the threat actors’ operations. BianLian and