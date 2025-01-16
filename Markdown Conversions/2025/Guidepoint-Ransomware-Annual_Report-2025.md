# GRIT 2025 Ransomware & Cyber Threat Report

## Table of Contents
- [A Note From GRIT](#a-note-from-grit)
- [Methodology](#methodology)
- [GRIT’s Ransomware Taxonomy](#grits-ransomware-taxonomy)
- [Annual Ransomware Summary](#annual-ransomware-summary)
- [Annual Ransomware Trends](#annual-ransomware-trends)
- [Annual Taxonomy Trends](#annual-taxonomy-trends)
- [Threat Actor Spotlight: RansomHub](#threat-actor-spotlight-ransomhub)
- [Industry Spotlight: Critical Infrastructure](#industry-spotlight-critical-infrastructure)
- [Annual Vulnerability Analysis](#annual-vulnerability-analysis)
- [Other Reporting and Events](#other-reporting-and-events)
- [Field Report: Post-Compromise Detection](#field-report-post-compromise-detection)
- [Annual Wrap Up](#annual-wrap-up)

## A Note From GRIT
Welcome to Ransomware and Cyber Threat Insights 2025, the expanded annual report that has grown from the original Ransomware Report issued in 2022 and 2023 by GuidePoint Security’s Research and Intelligence Team (GRIT). Since Q3 2024, we have opted to expand the scope of GRIT’s reporting beyond ransomware to include additional reporting and information covering the wider cybercrime landscape.

As a result of our collocation and collaboration with GuidePoint’s Digital Forensics and Incident Response (DFIR) teams, 2024 has provided us with access to hundreds of cybercrime response cases and their associated data, allowing us to better understand the threat landscape at the operational and strategic level, refined from relevant tactical details. We hope to translate this understanding and data into actionable insight in this annual report for you, the reader.

As we will illustrate throughout this report, the cybercrime landscape has adapted to changes and threats from international law enforcement, forcing changes in attribution, operational tempo, and tactics – changes doubtlessly made at a cost to the threat actors involved. In order to keep pace with these changes as they develop and continue complicating our adversaries' efforts, it is more important than ever to remain aware of the current threat landscape. We hope that this report helps in your process of doing so.

Happy Hunting,
- GRIT

## Methodology
- Data collected for this report was obtained from publicly available resources, including the sites and blogs of threat groups themselves, and has not been validated by alleged victims. As a result of these sources, as well as unknowable outcomes and figures of victims that have not been publicly disclosed, the number of observed attacks in this report and the total number of attacks conducted will not be equal.
- GRIT has reviewed collected data for potential duplications or inaccuracies and adjusted accordingly to best reflect the actual impacts of ransomware and cybercrime. We note that ransomware and cybercrime groups are likely to employ denial and deception to complicate research efforts and retain or build credibility among peers; to this end, we have reviewed each group and validated that its claims are at least as likely as not to be genuine before including them in our data set. While our process effectively rules out clear fabricators, we cannot completely rule out groups in which the number or qualities of victims may have been exaggerated or inflated. As a result of these differences in our approach, our numbers may periodically differ from other public reporting, particularly if this reporting does not scrutinize group claims and history.
- Throughout this report’s ransomware analysis, we include data and analysis of several groups that may be better described as "extortion" groups rather than "ransomware" groups. These groups may eschew encryption and focus only on data exfiltration and extortion or may not perform intrusion operations of any kind, instead extorting or re-extorting organizations based on historically compromised data. While these groups do not deploy ransomware, we have included them in our reporting due to their relationships with other ransomware groups and their impact on the extortion-based cybercrime environment.
- Finally, we make efforts to exclude from our data those groups that self-identify as “hacktivists,” compromised data brokers and markets, or non-financially motivated data thieves and leakers that may employ similar tactics, techniques, and procedures (TTPs) as ransomware and other cybercriminal groups. While these actors and venues doubtlessly have impacts, we distinguish them from financially-motivated cybercrime and data extortion, which is the primary focus of this report.
- Despite the above caveats, we have always and will continue to assess that our reporting and data are useful in aggregate while acknowledging that the underlying data sources have variability. We strongly believe that this report provides a consistent and accurate representation of the threat landscape over a given period and that our observations of the underlying trends remain valuable for Defenders.

## GRIT’s Ransomware Taxonomy
By subdividing ransomware groups, GRIT can more consistently observe the behavior and trends of ransomware groups as they progress in operational maturity and sophistication. We distinguish ransomware groups by placing them into these six categories:
- **Emerging.** This category is reserved for new ransomware groups within their first three months of operations. These organizations may be short-lived, resulting in an Ephemeral group; may be determined to have Splintered or Rebranded from an Established group; or may move on to further develop their operations and TTPs over time.
- **Ephemeral.** These groups are short-lived, with varied but low victim rates. Observed victims are usually posted in a single or short series of large postings rather than a continuous flow over time. Ephemeral groups, by definition, terminate operations, spin-off, or rebrand within three months of formation. These groups may or may not have dedicated infrastructure (i.e., data leak sites and chat support) as part of their operations.
- **Developing.** These groups have generally conducted operations for three months or longer, resulting in a recurring flow of victims. Developing groups do not generally appear to be directly linked to other ransomware groups as a Splinter or Rebrand but may include some experienced ransomware operators. Developing groups often improve their people, processes, or technology over time by recruiting additional members, refining TTPs, or improving the quality of their associated ransomware and encryption. These groups generally have dedicated infrastructure (i.e., data leak sites and chat support) as part of their operations.
- **Splinter.** These groups consist of a plurality of members from previously Developing or Established groups and may have formed either by choice or due to exclusion. These groups may be identified by very similar or overlapping TTPs and tooling or through HUMINT gathered through interactions with personas on the deep and dark web. Splinter groups differ from Rebrands by the continued existence of the original organization as the Splinter group operates.
- **Rebrand.** These groups consist in whole, or in part, of former Developing or Established groups. Rebrands often maintain the same people, processes, and technology as the original group. Rebrands are generally undertaken in order to minimize attention from law enforcement or intelligence officials or to avoid negative publicity.
- **Established.** These groups have generally operated successfully for at least nine months and have well-defined and consistent tactics, techniques, and procedures. Established groups often possess functional units that enable sustained ransomware operations, with specialists focused on areas such as personnel, encryption, negotiations, etc. These organizations successfully employ technology and redundant infrastructure to support their operations.

Additionally, in order to account for and describe periods of activity and inactivity, we may periodically append the following adjectives to help in understanding a threat actor's activity, dormancy, or dissolution:
- **Intermittent.** We append the adjective "Intermittent" to groups across the spectrum of classifications that have repeatedly (i.e., more than twice) demonstrated a tendency towards periods of dormancy followed by periods of activity. We distinguish these groups from defunct groups and dormant groups.
- **Dormant.** We append the adjective "Dormant" to groups across the spectrum of classifications that have not claimed victims in a substantial period of time, but for which we cannot confirm disollution. An example would be a previous Developing group which has not claimed victims in two months, but which maintains actively resolving infrastructure.
- **Defunct.** We append the adjective "Defunct" to groups which we know to be dissolved, or which have not claimed victims in a substantial portion of time and no longer present "signs of life" such as active infrastructure.

## Annual Ransomware Summary
Total Publicly Posted Ransomware Victims: 4,848
Number of Tracked Ransomware Groups: 88
Average Daily Victims: 13.2

- “The More Things Change, The More They Stay the Same”
As we published our third annual report analyzing ransomware, GRIT found itself inevitably drawn to this old maxim, reflecting on key aspects of the cybercrime landscape remaining inflexible even as TTPs and tactical details changed month by month. In the wake of year-over-year exponential growth going back a half-decade, many of us expected another banner year for ransomware; thanks to the persistence and effectiveness of international law enforcement operations, this was not the case. In 2024, we observed an overall minimal year-over-year growth of victim volume of only 8.72%, which pales in comparison to 2022-2023’s 76.8% growth.

As we close 2024 with ransomware’s two largest groups – LockBit and Alphv – substantially disabled and dissolved (respectively), the continued tempo of ransomware operations has demonstrated the staying power of Ransomware-as-a-Service (RaaS) as a business model. Without a single point of failure for disruption, law enforcement “decapitation” operations are rendered less impactful. Affiliates not ensnared in the subsequent dragnet have proven free to realign with other groups and resume operations, albeit under different circumstances and with a hopefully greater fear of future arrest. Law enforcement’s disruption of infrastructure and key tools has faced similar difficulties, driven by the diversity and availability of myriad replacement options. Financially-motivated cybercriminals remain resilient.

Initial access vectors observed in 2024 for ransomware and data extortion remain diverse, with stolen valid credentials and exploitation of new and historical vulnerabilities remaining among the most common. The risk posed by these access vectors is disproportionately experienced by small-to-midsized businesses (SMBs) that may lack the financial resources to detect and respond to them in a timely manner. Large enterprise environments, however, remain susceptible to the sophisticated and persistent “Big Game Hunting” approach favored by some Established groups.

If the above sounds pessimistic, we ask that you stick with us for the duration of this report, which highlights many reasons for optimism. In addition to a slowing growth rate overall, we have also observed increasingly high-visibility disruptions by global law enforcement of individual actors and tooling and the incredibly effective application of international sanctions. As we enter 2025, it is crucial that we understand and appreciate where these approaches have succeeded totally, where they have succeeded partially, and where they have failed. We believe that this report will help you in your understanding of just that and remain hopeful that 2025 will be the year ransomware not only slows its expansion–but actually decreases.

## Annual Ransomware Trends
GRIT observed a record number of victims claimed by ransomware actors throughout 2024. The ransomware ecosystem saw some significant shifts during Q1 with the disruption of LockBit and Alphv (also known as Black Cat or stylized as AlphV) departure via an “exit scam.” We assess that these impacts directly contributed to a decline in observed victim volume in Q2 and early Q3, a relative “slump” that would later be outpaced by a record-setting Q4. The bulk of observed victims formerly concentrated largely amid two “front-runners” in recent years, was attributed to a wider range of groups in 2024. While RansomHub quickly emerged as the largest group by victim volume, Akira, Play, and other Established groups demonstrated an increased operational tempo year-over-year, potentially reflecting the realignment of experienced affiliates to a broader array of RaaS groups. Realignment may partly be to blame for a concurrent increase in the number of distinct named threat groups observed in 2024, which increased 42% year-over-year from 62 in 2023 to 88 in 2024. Finally, Clop, a data extortion and former ransomware group best known for exploitation of Managed File Transfer appliances in wide-scale campaigns, returned from a period of dormancy to claim 66 redacted victims tied to a vulnerability in Cleo software in December, explaining a substantial end-of-year spike.

![Rate of Publicly Posted Ransomware Victims, 2024]

- Despite the crippling of LockBit and the absence of Alphv, the anticipated “summer lull” decrease in activity during late Q2 and early Q3 was minimal in 2024. We attribute this partly to RansomHub’s rapidly increasing operational tempo observed during the same period.
- During the Q3-Q4 period of 2022 and 2023, ransomware activity either remained stagnant or decreased, but 2024 bucked this trend. In Q4, GRIT observed the largest number of claimed ransomware victims since we began formally tracking ransomware victims in 2022. This activity burst was partly aided by sizeable claims from newcomer Funksec (90 – though we will explore the questionable veracity of these victims later in this report) and the return of the intermittently operating Established group, Clop (66).
- Finally, what we have dubbed the “middle class” of the ransomware ecosystem contributed strongly across a more significant number of groups, including consistent operations from Qilin (16), Hunters International (15), and BianLian (12).

![Most Impacted Industries, 2024]
- Manufacturing remained the industry most frequently impacted by ransomware groups in 2024, with 67% of the distinct ransomware groups tracked by GRIT having claiming at least one victim within the industry over the course of the year.
- Banking and Finance experienced a relative and objective decrease in its share of ransomware victims relative to others, decreasing from the sixth-most impacted industry (245 observed victims) in 2023 to the tenth-most impacted industry (185 observed victims) in 2024, presenting a nearly 25% decrease in observed attacks year-over-year. This decrease could be attributed in part to increased defensive measures emplaced within the industry, by increased regulatory and notification requirements, or by other factors.
- Play, the third most impactful ransomware group in 2024 by victim volume, did not claim any victims in the healthcare industry in 2024. While we note that we cannot rule out any healthcare victims impacted by Play in general (such as those who may have paid a ransom or which the group opted not to claim publicly), this deviates substantially from the observed trend of increased numbers of victims in the healthcare industry (+13% YoY) which we have observed in 2024.
- Conversely, we observed a 36% YoY increase in claimed Government institutions, placing “Government” within the “top 10” most impacted list. Anecdotally, we note that this coincides with a slight increase in global (non-US) impacts in 2024 and several emerging groups overtly claiming ideological motivations for their actions.

![Geographic Breakdown of Ransomware Victims, 2024]
Top 10:
1. United States
2. United Kingdom
3. Canada
4. Germany
5. Italy
6. France
7. India
8. Brazil
9. Spain
10. Australia

- The United States remained the country most impacted by ransomware by several orders of magnitude, accounting for 51.53% of all observed ransomware attacks in 2024, a marginal increase of 1.5% from 2023. It continues to be the most impacted country regarding the number of raw ransomware victims claimed by threat groups. The share of victims rose from 49% in 2023 to just over 51% in 2024.
- While we cannot confidently assess the extent to which sanctions against LockBit’s administrator, LockBitSupp, have disrupted the group’s revenue generation, the introduction of these sanctions likely increased the percentage of US victims who were unable or unwilling to pay in 2024.
- Brazil and India experienced increased ransomware attacks from 2023 to 2024, rising 56.06% and 46.75% respectively. In both cases, Established groups LockBit and RansomHub were among the most impactful groups in terms of victim volume. Throughout 2024, we have assessed that an expanding economy and vulnerable attack surfaces may drive increased effects against Brazil and India.

![Ransomware Impacts by Country, 2024]

![Most Impactful Ransomware Groups - 2024]
RansomHub
- RansomHub has steadily increased their operational tempo since their first posts in February 2024 to become the most active group during the year's second half. RansomHub was not alone in claiming an uptick of activity in H2 2024, with other Ransomware groups such as Akira and Play demonstrating similar increases.
LockBit
- LockBit entered 2024 as the long-standing dominant ransomware group with the highest tempo by victim, but the group faced substantial disruption in the wake of February’s international Operation Cronos. Now facing sanctions that have all but eliminated victims’ willingness to pay the group in the United States, Australia, and the United Kingdom, the group’s most experienced affiliates have likely departed, resulting in the single-digit monthly victim totals observed throughout Q3.
Play
- Play has maintained a generally consistent victim post rate throughout 2024 and was among the most homogenous attackers; 83.43% of Play’s victims in 2024 were US-based organizations, and the group accounted for more than any other ransomware group towards observed attacks at 11%. Notably and in contrast to other “top” groups, Play is “presumed to be a closed group, designed to ‘guarantee the secrecy of deals,’” according to an assessment from CISA.

![Daily Victim Posts and Active Groups by Week, Q4 2024]
- Q4 of 2024 represents the most active quarter by victim volume that we have observed since GRIT began formally tracking ransomware data in 2022; Ransomware groups collectively posted 1667 victims in Q4, a 49% YoY increase relative to Q4 2023.
- Visualization of victim posts reveals a clear spike in November near the Thanksgiving holiday, during which security teams were likely to be understaffed or less alert to enterprise intrusions. November also marked RansomHub’s densest month by victim volume at 99 victims.
- Later in Q4, we observed the return of the intermittently operating Established group, Clop, for another mass-exploitation campaign, resulting in the posting of 66 victims on Christmas Eve. Others, including the less mature groups Bashe, El Dorado, and KillSec, also established a regular operational cadence, averaging over a post per day during this period.
- Finally, we note that Q4 also represented the highest number of distinct, named ransomware groups per quarter since we began formally tracking ransomware data. The number spiked to 61 in Q4 2024, representing a 24.49% increase relative to Q3 2024 and a 35.56% YoY increase relative to Q4 2023. This reflects the growing number of distinct, named groups entering the ransomware ecosystem in 2024, including 17 that emerged in Q4 alone.

## Annual Taxonomy Trends
![Post Rates per Month, 2024]
- Established groups remained the most prolific in the ransomware landscape and were responsible for the majority of observed victims throughout most of 2024. We note that LockBit’s disclosure of 121 victims over three days in May likely skewed data significantly, which can be clearly viewed in our visualization of the data below. This “dumping” of victims may have represented a clearing out of “backlog” victims or historical victims that had not previously been posted.
- Interestingly, less sophisticated and mature Emerging and Developing groups claimed an above-average “market share” of victims in Q2, which we attribute to the realignment of experienced affiliates from Alphv and LockBit following the former’s dissolution and the latter’s law enforcement disruption. As a result, groups that might have otherwise needed more time to scale their operations likely benefited from acquiring skilled affiliates early or experienced affiliates may have formed additional groups themselves.
- However, by Q3 and Q4, “market share” returned to baseline, with Established groups again accounting for most observed victims. This could be attributed to a further realignment of former Alphv and LockBit affiliates with more substantial, mature, or sophisticated groups to retain illicit revenue-generating capabilities, as well as former Developing groups “graduating” to Established status with time.
- Finally, Q4 saw an increase in the number of new distinct named ransomware groups, several of which immediately began recurring operations; this influx can be observed in the rise of attacks attributable to Emerging groups from October through December.

![Industry Victims by Taxonomy Classification]
Established
1. Manufacturing
2. Healthcare
3. Technology
4. Retail and Wholesale
5. Consulting
Rebrand
1. Manufacturing
2. Education
3. Healthcare
4. Construction
5. Retail and Wholesale
Ephemeral
1. Healthcare
2. Government
3. Banking and Finance
4. Engineering
5. Automotive
Developing
1. Manufacturing
2. Technology
3. Healthcare
4. Retail and Wholesale
5. Banking and Finance
Emerging
1. Technology
2. Manufacturing
3. Consulting
4. Retail and Wholesale
5. Banking and Finance

- Manufacturing remained the most victimized industry across most of the GRIT’s taxonomy classifications, reflecting targeting by actors across the gamut of sophistication and maturity. The prevalence of manufacturing organizations in the global north, the large attack surface commonly associated with such organizations, and the increased motivation for payment in cases of operational disruption all likely contribute to these results.
- Healthcare victims became more prevalent among the most prolific and sophisticated Established groups and rose to the second spot from their previous position in third during 2023. These victims were once considered “taboo” for ransomware groups due to the additional scrutiny that such attacks could garner from law enforcement. However, Established groups have appeared emboldened to openly claim healthcare victims in 2024, possibly spurned by the success of Alphv’s alleged payment in the wake.
- Ephemeral groups proved to be the biggest outliers relative to their peers regarding which industries they impacted, disproportionately affecting victims in the Engineering and Automotive industries, with neither sector being among the most commonly victimized by any other subset of our taxonomy.
- Finally, we note the outsized presence of Government organizations among Ephemeral groups’ victims; this could reflect short-lived groups with political or ideological motivations or the behavior of groups that have not realized that Government organizations are unlikely to pay ransom demands in most circumstances.

![Top 5 Countries by Taxonomy Classification]
Established
1. United States
2. Canada
3. United Kingdom
4. Germany
5. France
Rebrand
1. United States
2. Germany
3. Canada
4. United Kingdom
5. Australia
Ephemeral
1. United States
2. Brazil
3. Germany
4. Canada
5. United Kingdom
Developing
1. United States
2. United Kingdom
3. India
4. Italy
5. Brazil
Emerging
1. United States
2. Canada
3. Italy
4. Jamaica
5. Netherlands

- The United States remains the most impacted by ransomware groups of all taxonomy classifications, from the immature and unsophisticated through ton the prolific and mature.
- We note that Brazil and India disproportionately attracted attacks from Developing groups. As Developing groups frequently lack the experience and resources of more mature groups, targets in developing economies may prove more viable or attractive. Conversely, for larger and more well-resourced groups, ”Big Game Hunting” against large organizations capable of paying larger ransoms likely results in greater targeting of the Global North.

## Threat Actor Spotlight: RansomHub
Since first appearing publicly in February 2024, RansomHub has quickly risen to become the most prolific Ransomware-as-a-Service group by observed victim volume, surging past its peers for every month in 2024 since June. The group continues to record a high number of victims on their data leak site monthly, demonstrating an operational tempo not matched by any other ransomware group since LockBit. In Q4 2024 alone, RansomHub managed to claim 239 victims resulting from affiliate operations – the total number inclusive of victims who may have paid a ransom is likely much higher.

RansomHub’s origin can be traced to a preceding ransomware group, Knight. Knight itself can be traced as a Rebrand of the Cyclops ransomware group, which publicly announced the rebrand on the Cyclops data leak site in July 2023, seemingly to generate interest and publicity for the group. The operators of Cyclops appear to have worked under the Knight umbrella until publicly offering to sell their operations in February 2024 – the same time at which RansomHub began operations. While we do not know whether Knight’s ransomware was actually sold and purchased by RansomHub, or whether RansomHub merely represents yet another Rebrand, we have observed sufficient reporting on similarities between RansomHub’s encryptor and that of Cyclops/Knight to conclude that RansomHub almost certainly benefitted from the Cyclops/Knight encryptor in rapidly spinning-up operations.

![RansomHub’s data leak site displaying victims with countdown timers]

We first covered RansomHub during our April 2024 GRIT Ransomware Report, when the seemingly fledging group was just starting to rise among their peers in terms of victim volume. We noted their attractive affiliate program and its subsequent advertising on dark web forums, such as RAMP, as a driving force in what was likely to be a successful ransomware operation, but we did not yet fully anticipate how active the group would become in the following months.

Perhaps in response to Alphv’s allegations of “exit scamming,” RansomHub has advertised to affiliates that affiliates receive payments first before paying the core administrators, a reversal of the typical process, alongside an attractive 90/10 ransom split in favor of the affiliate. Coinciding with the dissolution of Alphv and the law enforcement disruption of LockBit, the timing of RansomHub’s debut almost certainly has contributed to their success to date and allowed for the absorption of experienced but displaced affiliates drawn in part by these attractive terms. In our experience, RansomHub has provided two wallets to victims during communications, making it easy for both the main operator and affiliate to ensure they get their proceeds directly from the victims.

RansomHub was notably active on the dark web cybercrime RAMP during the start of the group’s operations. Their spokesperson, under the moniker “koley,” routinely updated a thread titled “[RaaS] 2024 RansomHub,” as seen in the below forum post:

![February 2024 post on RAMP from ”koley,” detailing RansomHub’s capabilities]

The initial posts we observed from the “koley” persona on RAMP detailed the features of the RansomHub encryptor and the rules laid out for potential affiliates, with updates to the post highlighting features added to the encryptor. These updates continued until July 2024, when the updates stopped for unknown reasons; we note that given the observed victim volume, at this point, RansomHub’s administrators may have determined that additional recruiting may have been superfluous. The group’s subsequent success and media coverage likely allowed a more widespread “marketing” approach than any posts on an invite-only dark web forum.

Barring any disruptive actions from law enforcement, GRIT assesses that RansomHub will continue to be a prolific threat within the ransomware ecosystem. However, overall effectiveness and long-term viability remain unknown, and the group’s high victim volume is likely to attract global law enforcement attention like LockBit, Alphv, Hive, and REvil before them.

![File Upload and Chat Infrastructure Logins for RansomHub]

## Industry Spotlight: Critical Infrastructure
In 2021, a ransomware attack on Colonial Pipeline, the largest pipeline for transporting refined petroleum products in the United States, sent ripples through the operators of critical infrastructure and governments worldwide. While it was not the first attack of its kind, the ensuing publicity and human impact of fuel disruptions made it so that United States lawmakers could not ignore the vulnerability of these systems critical to our daily lives.

Shortly after the attack, President Biden issued Executive Order 14028, which not only laid the foundation for future cybersecurity legislation but also made strides in eliminating information barriers between operators of critical infrastructure and government agencies. Since then, multiple bipartisan efforts have been made to strengthen the defenses of critical infrastructure.

In addition to funding and oversight, the Cyber Incident Reporting for Critical Infrastructure Act of 2022 (CIRCIA) proposed mandatory reporting requirements to the Cybersecurity and Infrastructure Security Agency (CISA) for private companies with critical infrastructure ties experiencing a cybersecurity incident. This legally-enforced transparency was not meant as a regulatory speedbump but rather an opportunity for CISA and, more broadly, the Department of Homeland Security to better assist, understand, and respond to cyber incidents that involve critical infrastructure.

In 2024, we had the opportunity to see the early effects of CIRCIA and subsequent guidance from CISA on our visibility into cyberattacks against critical infrastructure; largely, impacts appear to have been more localized and response more measured than in response to earlier critical infrastructure intrusions such as Colonial Pipeline.

For example, in August 2024, the Port of Seattle was impacted by the ransomware group Rhysida, disrupting key systems at Seattle-Tacoma International Airport. Per a statement from the Port in September, the organization did not pay the ransom and opted to rebuild affected systems manually. Countless more impacts were observed on smaller disparate victims providing critical services. However, the Port of Seattle ultimately recovered, a ransom was not paid, and any visible effects on the public did not extend for a protracted period of time. We cannot confidently assess the extent to which this more moderate response benefitted from CIRCIA or CISA support, but at a broader level, the response to impacts appears to be more structured and less panicked.

GRIT has discussed the increased appetite of ransomware groups to victimize the Healthcare industry on several occasions, and hospitals are frequently dual-categorized as belonging to US Critical Infrastructure. Despite their importance to everyday life, hospitals have historically been forced to be frugal with their information technology budgets, making them vulnerable to disruptive ransomware attacks. Much like their counterparts in Energy & Utilities, Government, and Transportation, downtime at a hospital or other public health system directly impacts human life. CIRCIA has laid the groundwork for a public/private partnership to minimize these vulnerable organizations by sharing threat intelligence and guidance. Monetary investment in cyber defenses for critical infrastructure, whether through public or private sector funding, remains necessary - but closing the information gap to better understand effects will doubtlessly support future response efforts and investments.

We can also look outside the United States for further justification of the importance of protecting critical infrastructure. In January, Russian-affiliated actors deployed a piece of malware, dubbed FrostyGoop by Dragos, against a power plant in Ukraine. This malware was designed specifically to impact internal control systems (ICS), which run industrial equipment necessary for the plant to deliver power to customers. Dragos reported that the attackers, in this case, intentionally disrupted these systems in the cold month of January, leaving thousands without power and heat. While this attack was clearly designed to impact local support for the war effort, similar tactics and technology could be used for financial gain via ransomware and data extortion in future attacks. To paraphrase an old adage, we are best suited to preparing in peace for the effects of tactics that could be deployed against us in conflict.

## Annual Vulnerability Analysis
Common Vulnerabilities and Exposures (CVEs) are cataloged and categorized “security issues” found in software or hardware. Each CVE is a unique identifier or serial number for specific vulnerabilities that can be exploited and used to cause hardware or software to behave in an unintended manner. These vulnerabilities are often exploited for the purpose of gaining unauthorized access to systems. Common Vulnerabilities and Exposures are frequently (although not always) accompanied by a Common Weakness Enumeration (CWE). These CWEs are the categorized mistakes developers might have inadvertently introduced to their software or hardware. CWEs describe the underlying categorized weakness that could lead to vulnerabilities.

2024 saw significant activity in the vulnerability landscape, marked by the publication of over 39,000 published CVEs, a nearly 40% increase over the 28,000 CVEs published in 2023. Of these ~39,000, 34,434 (~88%) included CVSS scores, allowing analysts to evaluate and prioritize vulnerabilities by impacts and effects. Despite this, with a daily average of 378 CVEs published, organizations risk drowning in the sheer volume of potentially relevant vulnerabilities, which could present attackers with opportunities and subsequent organizational risk.

To better understand the intersection of vulnerabilities with cybercrime campaigns, GRIT opted to perform further analysis of the year’s CVEs in review. Beyond the details already covered, we began with breakdowns by severity as reflected in the CVSS score:

CVSS Score | Count
----------|----------
6.50 | 2,550
5.50 | 2,500
8.80 | 2,311
9.80 | 2,261
7.80 | 2,254

Top 5 CVSS count for 2024

The high frequency of CVEs with scores between 7.5 and 9.8 highlights the high level of risk level that is being identified on a regular basis for defenders to track. At 15,000 vulnerabilities, roughly 44% of the vulnerabilities published in 2024 were designated “High” or ”Critical.” In other words, enterprise risk is amplified not only by the sheer number of vulnerabilities but also by the prevalence of those with the potential for severe impact if exploited.

### CISA’s KEV Catalog Analysis
The Known Exploited Vulnerabilities (KEV) catalog, maintained by CISA, focuses on identifying and addressing vulnerabilities actively exploited by threat actors. The main goal of the KEV catalog is to prioritize and mitigate vulnerabilities that pose significant risks to federal agencies, organizations, and critical infrastructure. The KEV serves as an excellent resource for Defenders in determining which vulnerabilities are confirmed to have been exploited “in the wild.”

CISA’s KEV catalog disclosed 187 vulnerabilities as under active exploitation in 2023 and 186 in 2024, highlighting limitations either in adversary abilities to exploit high volumes of vulnerabilities or in CISA’s ability to document and track the same. Regardless, for all of its helpfulness and insight, we do not and should not consider the KEV to be comprehensive, complete, or the timeliest in understanding which vulnerabilities are under exploitation across the entire world – but only in those areas with direct relevance for federal organizations and critical infrastructure.

### Underlying Weaknesses
Diving into the driving force behind vulnerability exploitation, the trends of weaknesses leading to vulnerabilities are interesting to consider, particularly in the context of threat actors' abilities to develop their own exploits targeting CWE categories associated with code execution, privilege escalation, or credential harvesting – each of which can be instrumental in obtaining an initial foothold, establishing persistence, or pivoting laterally in a compromised environment. Comparing the top CWEs for vulnerabilities added to the KEV database in 2024 versus 2023 highlights subtle but meaningful shifts in exploitation trends:

CWE | 2023 Count | 2024 Count | Usage Trend Analysis
----------|----------|----------|----------
CWE-416 | 16 | 10 | Significant reduction; possibly due to improved mitigation techniques in modern compilers/software.
CWE-78 | 14 | 14 | Remains consistent, highlighting the continued threat of improperly sanitized input in critical systems.
CWE-20 | 11 | 0 | Absent from 2024's top CWEs; likely prioritized by vendors in implementing secure design frameworks.
CWE-502 | 8 | 11 | Potential increased focus from attackers on exploiting serialized data, potentially in IoT and cloud systems.
CWE-787 | 9 | 7 | Minor reduction; memory-related vulnerabilities continue to be a concern in hardware-level flaws.
CWE-79 | 6 | 5 | Remains prominent across all CVEs, emphasizes prevalence of web-facing vulnerabilities.

In 2024, CWE-78 (OS Command Injection; Improper Neutralization of Special Elements used in an OS Command) remains at the forefront with 14 occurrences, consistent with 2023 and underscoring the enduring appeal of this weakness for attackers seeking to execute arbitrary commands on target systems. However, CWE-416 (Use After Free), which led the 2023 list with 16 occurrences, has dropped to 10 occurrences in 2024. This decline may indicate increased vendor attention to memory management flaws, or it could suggest a pivot by threat actors toward other exploit types that require less expertise or a pointed interest in targeting newer systems.

Notably, CWE-502 (Deserialization of Untrusted Data) has risen to prominence in 2024 with 11 occurrences compared to 8 in 2023, reflecting potentially growing exploitation of serialized data streams, which can lead to remote code execution. Similarly, CWE-22 (Path Traversal) and CWE-287 (Improper Authentication), both with nine occurrences in 2024, highlight a likely continued focus on leveraging vulnerabilities that allow unauthorized access to sensitive files or systems.

CWE-77 (Command Injection) and CWE-787 (Out-of-Bounds Write) maintain a steady presence, both with seven occurrences in 2024.