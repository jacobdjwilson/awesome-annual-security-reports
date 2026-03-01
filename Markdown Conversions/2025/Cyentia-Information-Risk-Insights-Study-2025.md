# Information Risk Insights Study (IRIS) 2025: It's About Time

**Organization:** Cyentia  
**Report Title:** Information-Risk-Insights-Study  
**Year:** 2025

The Cyentia Institute is a research firm working to improve cyber risk management through our analytical services and data-driven research publications. You can download the IRIS 2025 and find related content at [www.cyentia.com/iris](http://www.cyentia.com/iris).

## Table of Contents
- [Introduction](#introduction)
- [Acknowledgements](#acknowledgements)
- [Key Findings](#key-findings)
- [Are Security Incidents Becoming More Common?](#are-security-incidents-becoming-more-common)
- [Do Incident Trends Differ Across Organizations?](#do-incident-trends-differ-across-organizations)
- [Is the Probability of Incidents Increasing?](#is-the-probability-of-incidents-increasing)
- [Have Security Incidents Gotten More Costly?](#have-security-incidents-gotten-more-costly)
- [Do Loss Trends Differ Among Event Types?](#do-loss-trends-differ-among-event-types)
- [Are Intrusion Methods Changing Over Time?](#are-intrusion-methods-changing-over-time)
- [What Are We Missing From Current Events?](#what-are-we-missing-from-current-events)
- [Methodology](#methodology)
- [Appendix A: Incident Pattern Definitions](#appendix-a-incident-pattern-definitions)

## Introduction
Welcome to the 2025 edition of the (roughly) biennial Information Risk Insights Study (IRIS). The last one was in 2022, so it’s about time we got this to you. Thanks for your patience.

Fittingly, time is of the essence in this IRIS. Not just because it’s a tad overdue, but because it’s literally about time—cyber risk trends over time, to be specific.

Cybersecurity is ever-changing, and there’s an implicit assumption that risk is always increasing. But is it?

Are cyber events occurring at greater frequency? Is an organization more likely to have a breach now than 15 years ago? Which types of incidents have become more common over time? Have the financial impacts of cyber events increased or decreased? Are risk factors trending the same way for all sectors and sizes of organizations?

We explore these questions and more by analyzing a huge historical dataset of cyber events and losses from 2008 through 2024. As always, our goal is to dispel the fog of FUD surrounding cyber risk so you can see it more clearly and manage it more effectively. Thanks for reading!

## Acknowledgements
The Cyentia Institute wishes to acknowledge and thank the Cybersecurity Division and the Office of the Chief Economist at the Cybersecurity and Infrastructure Security Agency (CISA) for sponsoring this study. It is our sincere hope that this research will aid community efforts to manage cyber risk.

> “Time isn't a straight line... It's all bumpy wumpy.”[^1]  
> ~The Eleventh Doctor

## Key Findings
The IRIS research draws heavily upon Zywave’s (formerly Advisen) Cyber Loss Data, which contains over 150,000 security incidents[^2] and associated financial losses[^3] spanning decades. The data is compiled from publicly available sources, such as breach disclosures, public company filings, litigation details, and Freedom of Information Act requests. It is the most comprehensive source of cybersecurity incidents and losses available. Additionally, Cyentia does extensive processing of this base dataset to extend and enrich it for cyber risk analysis use cases.

- **On average, 3,000 significant security incidents are publicly reported or discovered each quarter.** That’s a 650% increase over the last 15 years.
- **Cyber events affecting smaller businesses are far more common overall**, but relative to population size, the rate among the largest corporations is 620 times higher.
- **The annual probability of any given organization experiencing a cyber event has almost quadrupled since 2008.**
- **The probability of a <$1B firm suffering an incident has more than doubled**, while the annual likelihood for a $100B+ organization has fallen 50%.
- **Losses from a typical security incident have absolutely exploded**, rising 15-fold from a median of $190K to almost $3 million!
- **The cost of more extreme “tail loss” events is also up 5-fold**, ballooning to $32 million.
- **Cyber events aren’t just costing more—they’re hurting the bottom line more than ever before.** We’ve seen an 8-fold increase in costs as a proportion of annual revenue.
- **Median losses for professional services firms are up 25x over the last 15 years!** Alternatively, there’s been a huge decrease in loss magnitude among retailers.
- **Compromising user credentials remains the most common intrusion technique over the last decade**, fluctuating between 43% and 60% of all incidents.
- **Exploitation of web applications is up 6x for smaller firms**, while targeting third-party relationships has doubled among large organizations.

**Like what you see? Join the vision!**  
We intend to continue the IRIS in the future to discover even more insights for managing information risk. If you’d like to join in that effort by contributing relevant data or sponsoring research, please reach out to us via the contact form at [www.cyentia.com/iris](http://www.cyentia.com/iris).

## Are Security Incidents Becoming More Common?
To many of you, the answer to this question seems so obvious that it’s hardly worth asking. But we’re not ones to let any assumption go unchallenged. As it turns out, this one is solidly backed by historical data—at least in terms of reported incidents[^4]. Figure 1 shows a 650% increase in the average number of incidents added to the public record each quarter in 2024 (~3,000) versus the rate set 15 years ago (~450).

But there’s a lot more going on than simply “incidents are way up!”[^5] The proliferation of large-scale data breaches combined with the rolling out of breach disclosure laws certainly drove the steady climb early in this timeframe. The plateau beginning in 2013 corresponds with the emergence of advanced persistent threats (APTs)[^6] that employed a “low and slow” rather than “smash and grab” strategy. The reacceleration circa 2019 was spurred by the rapid rise of ransomware (see Figure 2) and exacerbated by the COVID-19 pandemic. We could go on, but you get the point. These trends have reasons.

![Image description: Figure 1: Number of security incidents publicly reported or discovered each quarter. The chart shows a steady climb from ~450 in 2008 to a peak of ~3,000 in 2024, with a notable plateau in the mid-2010s and a sharp rise in the 2020s, followed by a reporting lag dip in the final quarter of 2024.]

We just mentioned the rise of ransomware, which prompts a related question: Are all types of incidents trending the same way? The crisscrossed lines in Figure 2 are sufficient for a definitive “nope,” but let’s highlight some of these trends that meaningfully impact organizations’ security strategies.

**Are all types of incidents following the same trend? "NO"**

At the top of Figure 2, below, system intrusion (unauthorized access to systems, applications, or networks) has long reigned supreme among incident patterns[^7]. The particular techniques attackers use to infiltrate networks and systems have undoubtedly changed, but we’ll dig into that later (see Q6). For now, simply observe that the most common category of incident experienced by organizations hasn’t really changed in the last 15 years.

![Image description: Figure 2: Relative frequency of incident patterns over time (rolling 12mo. 2009-2024). System intrusion remains the highest at ~60%. Ransomware shows a massive spike starting around 2019. Accidental disclosure shows a significant downward trend.]

Now let’s also observe what has changed. The aforementioned rise of ransomware in recent years is, in fact, unprecedented. So is accidental disclosure’s precipitous drop over roughly the same period. We could go into far more detail on ransomware trends, but we’ve already done that in another IRIS. We’d love to think that “oopsies” as a major cause of data disclosure are a thing of the past, but we suspect human nature will reassert itself at some point.

Physical threats and insider misuse show a marked downward trend over the years. Compared to more scalable remote alternatives, the “hands-on” approach to data theft has fallen out of favor. Data handling regulations and endpoint protections—such as encryption at rest—have further contributed to its decline. Insider misuse never rises above fourth place among all incident patterns, which goes against the long-standing “employees are the enemy” mentality. Sure, employees are often targeted in cyberattacks, but they’re usually not acting with malicious intent.

> **Key Risk Insight**  
> The data shows how fluid and contextual the cyber threat landscape really is and how important your firmographic footprint is to that, as we will show throughout this report. Quantifying that risk, especially at the board level, means understanding these patterns as time sensitive, not timeless. Today’s dominant risk may be tomorrow’s footnote, and cyber risk models need to keep pace. Further, if your security strategy isn’t recalibrating with these changes in risk, you’re planning for a past that no longer exists.  
> ~ Jack Freund, Executive Fellow | The Cyentia Institute

**Key Risk Insight**  
If it seems like a lot more incidents are happening these days, it’s not just recency bias. The overall rate has seen more than a sixfold increase over the last 15 years.

## Do Incident Trends Differ Across Organizations?
This seems like another obvious answer on the surface because it’s well known that certain organizations make more attractive targets, some have poor defenses, and others are just plain unlucky. But what we’re really after here is whether there are inherent differences between different types of firms. Figure 3 attempts to open the door to that question by comparing trends across organizations grouped by their annual revenue.

![Image description: Figure 3: Proportion of all incidents in each revenue tier (rolling 12mo. 2009-2024). Smaller businesses (<$10M and $10M-$100M) represent the largest and growing share of incidents, while the share for larger organizations (>$10B) is declining.]

Rebutting the “Who would attack little ‘ol us?” argument, smaller businesses (<$100M annual revenue) see the biggest overall share of incidents. What’s more, that share is growing over time. The proportion of events affecting larger organizations (>$1B annual revenue), on the other hand, appears to be declining over the last 15 years.

The data in our analysis is clear: smaller businesses—those under $100M in annual revenue—account for the largest share of incidents, countering the idea that they're too minor to target.

There’s more to this story, however, as astute readers have probably already discerned. The obvious objection to the prior chart’s depiction of trends is that it does not account for the number of firms that exist in each revenue tier[^8]. Sure, more incidents affect small businesses, but they vastly outnumber large corporations.[^9] What happens when we factor in the relative number of firms in each group? Figure 4 gives the answer—a complete reversal of fortune!

![Image description: Figure 4: Relative number of incidents to number of firms in each revenue tier (rolling 12mo. 2009-2024). The chart shows that while large firms (>$100B) have a declining trend, they still experience incidents at a rate 620x higher than their population size compared to the smallest firms (<$10M) at 0.53x.]

The multiples shown in Figure 4 compare the number of incidents across a revenue tier with the number of organizations within it. The higher the multiple, the higher the average rate of incidents per organization in each tier. While larger organizations show a declining trend in the relative number of incidents, they remain disproportionately affected by them. The $100B+ tier has experienced 620 times more incidents than the number of megacorporations in this segment. Though the smallest firms experience the largest number of incidents in absolute terms, only a fraction of them (0.53x) are actually affected.

Let’s turn next to frequency-based disparities among different industries. Since we’ve established the importance of adjusting for the number of firms in each segment, we can skip to the punch line. Figure 5 groups sectors[^10] based on their relative event frequency.[^11]

![Image description: Figure 5: Relative number of incidents to number of firms in each sector (rolling 12mo. 2009-2024). Public and Management sectors show very high relative frequency. Finance and Information are high but declining. Utilities, Manufacturing, and Professional are low but increasing.]

The Public and Management sectors are the only two that have historically exhibited a very high relative incident frequency. For the former, we attribute that to mandatory disclosure requirements that typically exceed those in the private sector. The Management sector is a bit of an oddball in NAICS, consisting mainly of holding companies. We suspect part of what’s going on here is that incidents affecting their subsidiaries are being attributed to them as the parent entity.

Moving to the upper-right panel, the Finance sector has historically seen a high share of incidents relative to the number of firms that exist. But that rate has fallen over time, perhaps due in part to the industry’s outsized security budgets. The Information sector continues to experience an elevated incident rate, yet is currently well below its high-water mark. Together, these industries control money and data flowing through the economy, so it’s no surprise they receive more than their fair share of cyberattacks.

Industries with historically low relative incident frequencies are split into two groups—those likely to remain low for the foreseeable future and those that will soon cross over the line of demarcation. We find it unsettling to see energy and supply chain sectors such as Utilities, Mining, Manufacturing, and Transportation (which includes oil and gas pipelines in NAICS) increasing in relative frequency. The Professional sector has already crossed that line, which is quite concerning given that they offer advice and services to the rest of us.

**Key Risk Insight**  
Incidents involving small and midsize businesses (SMBs) are far more common overall, but the relative incident frequency among large enterprises is much higher. Energy and supply chain sectors are creeping up in incident frequency—Utilities, Mining, Manufacturing, and Transportation are no longer sitting safely below the line.

## Is the Probability of Incidents Increasing?
This question may initially sound similar to the previous two, but those involved tallying the total number of incidents reported across many organizations. Here, we explore how the likelihood of a single organization having an incident is changing over time. If that nuance isn’t quite clear, think of it like this: what are the chances your firm will suffer a significant incident this year?

We’ll begin by changing our perspective from the past to the future—except how the future was modeled in the past… over time. Maybe a chart will help; Figure 6 tracks the modeled probability[^12] of a typical organization[^13] experiencing an incident in the next 12 months.

It is understandable if cybersecurity folks can’t hold back an “I told you so!” here because overall incident probability has almost quadrupled over the last 15 years.

![Image description: Figure 6: Historical probability of a firm having an incident in the next year. The probability rises from 2.5% in 2008 to 9.3% in 2024, with a plateau in the mid-2010s.]

“But wait,” we hear you saying, “doesn’t the probability for different types of cyber events change over time?” You’re not wrong. We simply can’t cram everything into this one study. New studies are always in the pipeline — we regularly publish extra analysis like that on our website at [www.cyentia.com/iris](http://www.cyentia.com/iris).

What if we told you that the probability of a <$100M firm suffering a security incident has more than doubled, while the chance of a $100B+ megacorporation suffering an incident has dropped by a third over the same time frame? Well, that’s exactly what Figure 7 tells us.

![Image description: Figure 7: Annualized incident probability for firms in each revenue tier (rolling 12mo.). The chart shows rising probability for smaller firms (under $1B) and a declining probability for the largest firms (over $100B).]

Unfortunately, our dataset is silent on the underlying factors behind these trends, so all we can offer is some speculation. Perhaps cybercriminals have shifted to more volume-oriented (“low-hanging fruit”) strategies over time. Maybe the pace of digitalization has outpaced SMBs’ ability to defend their growing attack surfaces, while the bigger enterprise security budgets offset that. Maybe increased regulatory pressures on large corporations are gradually hardening enterprise security architectures. Whatever the cause(s), these are important trends that are worth further research by our industry.

So, an organization’s size matters when evaluating the likelihood of incidents. Now, let’s see what happens when we treat industry as a feature of interest. Figure 8 paints that picture.

Sectors are sorted in descending order by the latest probability estimate. So, a typical manufacturing firm has an 11% chance of having a security incident in the next 12 months—up from ~2% 15 years ago.

![Image description: Figure 8: Annualized incident probability for firms in each sector (rolling 12mo.). Manufacturing (11.2%), Retail (10.9%), Public (9.1%), and Financial (8.4%) show the highest current probabilities.]

Suffice it to say that incident probability trends can be significantly different depending on firmographics (which are reflective of evolving business models, changes in the threat landscape, shifting adversary goals, etc.). That's intuitive, but perhaps seeing this confirmed will help validate the need to incorporate such factors into your cyber risk assessments.

**Key Risk Insight**  
Overall, the chances of any given organization experiencing an incident have gone up. But that trend has flattened or even reversed in some sectors and size tiers.

Our analysis in this section focuses on the likelihood of experiencing at least one security incident within a year. It is possible, of course, for organizations to suffer multiple incidents. We decided not to include that in this edition because feedback suggested most cyber risk models focused on single-event likelihood. Visit [www.cyentia.com/iris](http://www.cyentia.com/iris) to get additional analysis of multi-incident probabilities.

## Have Security Incidents Gotten More Costly?
We’ve covered the evolving frequency and likelihood of cyber events—now it’s time to talk dollars and cents. Let’s begin by establishing the distribution of financial losses from cyber events using Figure 9, which reproduces a classic IRIS chart with the latest and greatest data.[^14]

![Image description: Figure 9: Distribution of reported losses for security incidents from 2015 to 2024. The median loss is $603K, the geometric mean is $464K, and the 95th percentile is $32M. The chart uses a log scale.]

The typical (median[^15]) incident costs about $600K, while more extreme (95th percentile) losses swell to $32 million. Note that Figure 9 is plotted on a log scale, so the tail of large losses is longer than it appears.

**NOTE:** Losses analyzed in this study tend to reflect direct losses that are easier to quantify (e.g., response costs or lost revenue) and/or identify from public records (e.g., class action suits or SEC filings). Indirect and intangible impacts often aren’t captured. Thus, this represents a conservative view of financial losses associated with cyber events.

An overall distribution like Figure 9 is useful for illuminating the big picture, but it obscures any shifts in losses that may be happening over time. To visualize how the costs of cyber events have evolved, we’ll track two reference points—the median and 90th percentile—during the 15-year timeframe. The results are shown in Figure 10.

![Image description: Figure 10: Trend analysis of median and 90th percentile losses. Median losses rose 15.2x from $189.9K in 2008 to $2.9M in 2024. 90th percentile losses rose 4.75x from $6.0M to $28.5M.]

Median losses from a security incident have absolutely exploded over the last 15 years, rising 15-fold from $190K to almost $3 million! The cost of extreme events[^16] at the upper end of the distribution has also risen substantially (~5x). So, yeah—the financial toll of cyber events is definitely getting bigger.

It’s a no-brainer that larger firms would experience larger losses. We include Table 1 to reconfirm that fact and arm you with the most recent stats to inform loss estimates that are better sized to your organization.

### Table 1: Loss statistics by revenue tier
| Revenue | Loss percentile 50% | Loss percentile 95% |
| :--- | :--- | :--- |
| More than $10B | $2.2M | $266.2M |
| $1B to $10B | $1.8M | $61.8M |
| $100M to $1B | $466.7K | $12.3M |
| Less than $100M | $357.0K | $9.1M |

Measuring losses as a percentage of the victim firm’s annual revenue works well for normalizing impact. Median losses fall well below 1% of revenue for the majority of incidents. But as Figure 11 attests, that ratio has grown by nearly 8x over the last 15 years. The top 5% of loss events continue to exceed the annual revenue of affected firms.

![Image description: Figure 11: Trend analysis of median and 95th percentile losses as a percent of revenue. Median losses as % of revenue rose from 0.08% to 0.65% (7.84x increase).]

We’ll now briefly demonstrate that industry makes a difference too. Figure 12 highlights three industries that represent distinct rising, flat, and falling trends.[^17]

![Image description: Figure 12: Trend analysis of median and 90th percentile event losses for example sectors. Professional Services shows a 25.7x increase in median loss. Education is relatively flat. Retail shows a massive decrease (0.02x of original median).]

When it comes to the escalating costs of security incidents, no industry has been hit as hard as Professional Services. Median losses for firms in that sector are up 25x over the last 15 years! The Administrative, Financial, Healthcare, Manufacturing, and Public sectors also exhibit increasing trends for loss magnitude.

Event losses in the Education sector show a fairly steady, albeit increasing, trajectory. And then there’s the Retail sector, which seems to have figured out a way to cut the price tag of a security incident. Current losses for both typical and extreme events are a fraction of their starting points in 2008. We suspect the push for PCI compliance and Chip-and-Pin technology may have helped limit the amount of data that can be easily exfiltrated from retailers. Since larger breaches generally (but not linearly[^18]) correspond with higher losses, this would help cap potential losses.

**Key Risk Insight**  
Not only do typical security incidents cost more these days (up 15x since 2008)—they hurt a lot more too (up 8x relative to annual revenue).

## Do Loss Trends Differ Among Event Types?
There is a pronounced “shoulder” in the lower half of the distribution in Figure 9. Whenever a bimodal tendency like this exists, it’s worth investigating. We discovered that the shoulder has grown over time, as evidenced by Figure 13.

![Image description: Figure 13: Ridge plot showing loss distribution shape in successive 10-year windows. The plot shows a "pronounced shoulder" developing in the lower loss ranges in more recent years (2015-2024).]

The shoulder in the overall loss distribution actually results from a proliferation of fairly small losses from accidental disclosure events. Incidents tied to physical threats and insider misuse also contribute to lower losses, but those patterns are considerably less common.

![Image description: Figure 14: Distribution of reported losses by incident pattern (2008 to 2024). Accidental disclosure, Insider misuse, and Physical threats cluster at the lower end of the loss spectrum, while Ransomware and System Intrusion dominate the higher end.]

A possible explanation is that the growing shoulder reflects the rollout of regulations over the years that require public disclosure of even relatively minor data loss events.

![Image description: Figure 15: Trend analysis of median and 90th percentile losses by incident pattern. Accidental disclosure/Insider misuse costs are down. System intrusion 90th percentile is down sharply. Ransomware median loss has ballooned 20.49x.]

Losses stemming from accidental disclosure and insider misuse have indeed declined over time. Conversely, the median loss magnitude for system intrusion and ransomware incidents has risen, with the latter ballooning 20-fold! The decline in costs associated with system intrusions at the top end of the distribution is both dramatic and curious.

**Key Risk Insight**  
Both the magnitude and trend of losses from security incidents depend heavily on the type of event. This supports the need for risk scenarios to specify threats. While ransomware losses surge past $27M at the high end, top-tier system intrusions have dropped sharply—down to $7.4M from over $200M.

## Are Intrusion Methods Changing Over Time?
Tracking common adversary tactics, techniques, and procedures (TTPs) behind cyber events can bridge the divide between risk assessments and risk treatment. MITRE ATT&CK offers a knowledge base of TTPs that is convenient for this purpose.

### Figure 16: Prevalence of ATT&CK Initial Access techniques observed in incidents over time
| Rank | Technique | 2016 | 2018 | 2020 | 2022 | 2024 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1st | Valid Accounts | 57% | 60% | 54% | 43% | 46% |
| 2nd | Exploit Public-Facing App | 5% | 5% | 14% | 38% | 34% |
| 3rd | Phishing | 18% | 25% | 16% | 30% | 28% |
| 4th | Trusted Relationship | 12% | 16% | 15% | 15% | 12% |
| 5th | Hardware Additions | 35% | 31% | 29% | 35% | 10% |
| 6th | External Remote Services | <1% | <1% | 8% | 9% | 10% |
| 7th | Replication / Removable Media | 30% | 29% | 19% | 8% | 9% |
| 8th | Drive-by Compromise | <1% | <1% | 5% | 1% | 1% |
| 9th | Supply Chain Compromise | <1% | <1% | <1% | <1% | <1% |

Using Valid Accounts to gain illicit access has held the pole position for the entire time period. Phishing has also consistently ranked among the top techniques. The “moving-up-the-charts” award goes to Exploit Public-Facing Applications and External Remote Services. Both have surged from single-digit percentages to heights of 38% and 30%, respectively.[^19]

![Image description: Figure 17: Prevalence of ATT&CK Initial Access techniques observed by revenue tier. Abusing Valid Accounts is rising for the largest corporations (>$10B) but trending down for smaller firms. Phishing and exploiting applications are most prevalent among smaller firms (<$100M).]

Attacks targeting Trusted Relationships disproportionately affect larger organizations, which makes sense given their extensive portfolio of third-party vendors.

## What Are We Missing From Current Events?
We analyzed cyberattacks collected via Feedly’s intelligence capabilities to see what our core incident dataset might be missing from recent media coverage.

![Image description: Figure 18: Number of security incidents publicly reported or discovered each quarter. Feedly data for Q4-2024 shows over 3,500 incidents, filling the "dip" seen in the historical dataset caused by reporting lag.]

The 3,500+ incidents observed by Feedly during Q4-2024 fill the hole in our base historical dataset. This corroborates our suspicion of a reporting time lag.

### Table 2: Top threat actors associated with 2024 security incidents by sector (via Feedly)
| FINANCE | HEALTHCARE | PUBLIC |
| :--- | :--- | :--- |
| Lazarus Group | Shiny Hunters | Alpha Spider |
| RansomHub | GhostEmperor | Volt Typhoon |
| RansomHub | Vanilla Tempest | Flax Typhoon |

### Table 3: Comparison of top ATT&CK Initial Access techniques observed in incidents by source
| Name | Cyentia (2014-2023) | Cyentia (2024) | Feedly (2024) |
| :--- | :--- | :--- | :--- |
| Phishing (T1566) | 2nd | 3rd | 1st |
| Valid Accounts (T1078) | 1st | 1st | 2nd |
| Exploit Public-Facing App (T1190) | 6th | 2nd | 6th |
| Supply Chain Compromise (T1195) | 9th | 9th | 3rd |
| Hardware Additions (T1200) | 3rd | 5th | - |
| Drive-by Compromise (T1189) | 8th | 8th | 4th |
| Replication / Removable Media (T1091) | 4th | 7th | 7th |
| Trusted Relationship (T1199) | 5th | 4th | - |
| External Remote Services (T1133) | 7th | 6th | 5th |

The relative prominence of Supply Chain Compromise in Feedly’s collections is interesting because very few public incident disclosures list this as an initial access technique. Feedly’s collections may grant a forward-looking, headline-driven view, while our legacy data offers more of an actuarial perspective.

![Image description: Figure 19: Comparison of reported financial losses from incidents by source. Feedly-sourced events show a median loss of $28.5M, which is 30x higher than the historical median of $603K. This reflects the media's focus on major "tail risk" events.]

**Key Risk Insight**  
If your cyber risk analysis relies on near-term trends, consider incorporating sources that emphasize current events to supplement historical event data.

> "I'm grateful to all our data partners and sponsors who make it possible for us to do impactful research for the community. Reach out if you have data that would unlock new avenues of cyber risk analysis!"  
> ~ Wade Baker PhD, Co-Founder | The Cyentia Institute

## Methodology

### Data Collection
The IRIS research draws heavily upon Zywave’s Cyber Loss Data (>150,000 incidents). Cyentia does extensive processing to extend and enrich it using classification models, NLP, taxonomy mapping, and manual tagging. Feedly data from 2024 was used to study current event trends, focusing on "memes" (clusters of articles).

### Incident Likelihood
We modeled the frequency of security incidents over 12-month rolling windows. We use random effects models to estimate parameters overall and within specific slices. We use the more risk-averse upper bound estimate for likelihood, using the total number of organizations in our historical database as the denominator.

### Financial Losses
Losses tend to be under-reported. Those that are reported reflect direct losses (response costs, lost revenue). All financial loss values in this report have been adjusted for inflation to 2024 dollars.

## Appendix A: Incident Pattern Definitions
All security incidents are assigned one of these mutually exclusive[^23] patterns:

- **ACCIDENTAL DISCLOSURE:** Data stores inadvertently left accessible (e.g., misconfigurations).
- **DOS ATTACK:** Attacks intended to render systems unavailable by consuming resources.
- **DEFACEMENT:** Unauthorized content modification to websites.
- **FRAUD OR SCAM:** Deception to defraud the victim of money, identity, or information.
- **INSIDER MISUSE:** Inappropriate use of privileged access by employees or trusted third parties.
- **PHYSICAL THREATS:** Threats via physical vectors (theft, loss, tampering).
- **RANSOMWARE:** Malware that seeks to encrypt data with the promise to unlock it for a fee.
- **SYSTEM INTRUSION:** Unauthorized access to systems, applications, or networks (excluding ransomware).
- **SYSTEM FAILURE:** Non-malicious incidents resulting in the loss of availability or integrity.

***

[^1]: "Actually, from a non-linear, non-subjective viewpoint, it's more like a big ball of wibbly-wobbly, timey-wimey stuff." - The Tenth Doctor
[^2]: We use the terms security incident, cyber event, and loss event interchangeably.
[^3]: We use the terms losses or costs to refer to the financial consequences of incidents.
[^4]: Based on incidents that make their way into the public record through outward signs, mandatory reporting, etc.
[^5]: We are aware that "incidents are way down" in the last quarter of 2024 due to reporting lag.
[^6]: Mandiant’s APT1 report (2013) ballooned community awareness, which paradoxically slowed the rate of publicly reported incidents as attackers became more discrete.
[^7]: See Appendix B for definitions of these incident patterns.
[^8]: We use data from Dun & Bradstreet for the number of organizations in each revenue tier.
[^9]: The Small Business Administration estimates that 99.9% of all businesses are small.
[^10]: Sectors use the North American Industry Classification System (NAICS).
[^11]: A multiple >1 indicates higher relative incident frequency; <1 indicates the opposite.
[^12]: See appendix for details on our approach to modeling annualized incident probability.
[^13]: "Typical" reminds readers that this model doesn’t account for all factors making incidents more or less likely for a specific firm.
[^14]: All loss amounts have been converted to 2024 dollars to adjust for inflation.
[^15]: Prior IRIS used the geometric mean; the median is a better central measure for the updated distribution.
[^16]: We switch between 95th and 90th percentile for losses; 90th is used in time series models for reliability.
[^17]: Appendix C includes a table that gives median and extreme loss values for all sectors.
[^18]: Prior IRIS have demonstrated that losses do not follow a flat cost-per-record formula.
[^19]: Percentages are based on incidents for which at least one ATT&CK technique was identified.
[^20]: Global 2000: Industry Titans Battle the Beast of Supply Chain Cyber Risk (with SecurityScorecard).
[^21]: The State of Third-Party Risk Management (with RiskRecon).
[^22]: This is why many charts show an apparent downturn in 2024.
[^23]: While an incident could involve more than one, these represent the primary nature of the event.

---

ock upon payment or seeks to completely eradicate data/systems without the pretense of collecting payment.SYSTEM FAILURE: All unintentional service disruptions resulting from system, application, or network malfunctions or environmental hazards.SYSTEM INTRUSION: All attempts to compromise systems, applications, or networks by subverting logical access controls, elevating privileges, deploying malware, and so on.3A

C H A R T S & TA B L E S F RO M
PR I O R I R I S S T U D I E S

This appendix contains up-to-date versions of selected figures from IRIS 2022 that provide probability and
loss comparisons among sectors and revenue bands. If there are other figures you'd like to see from an IRIS
of yesteryear, let us know!

Education (1.60x)

Information (1.55x)

Professional (1.50x)

Financial (1.44x)

Healthcare (1.34x)

Public (1.34x)

Retail (1.19x)

Hospitality (1.15x)

Management (1.08x)

Manufacturing (1.03x)

Trade (0.97x)

Entertainment (0.94x)

Real Estate (0.93x)

Administrative (0.92x)

Agriculture (0.92x)

Other (0.92x)

Construction (0.91x)

Transportation (0.78x)

Mining (0.76x)

Utilities (0.62x)

i

r
o
t
c
e
s
n
a
d
e
m
o
t
e
v
i
t
a
l
e
R

Figure A1: Relative probability of one or more loss events among sectors (Figure 5 in IRIS 2022). The point
of comparison is the overall median across all organizations.

Source: IRIS 2025 (Cyentia Institute)

$1B to $10B (1.20x)

$10B to $100B (2.49x)

More than $100B (3.46x)

$100M to $1B (0.80x)

$10M to $100M (0.67x)

Less than $10M (0.60x)

Figure  A2:  Relative  probability  of  one  or  more  loss  events  among  annual  revenue  tiers.  The  point  of
comparison is the overall median across all organizations.

Source: IRIS 2025 (Cyentia Institute)

3 4

THE CYENTIA INSTITUTE CYENTIA.COMIRIS 2025 IT'S ABOUT TIME

Losses observed per sector

Sector

Geometric mean Median 95th percentile

Administrative

$318K

$529K

Agriculture

$1M

$2M

Construction

$164K

$189K

Education

$226K

$249K

Entertainment

$147K

$282K

Financial

Healthcare

$951K

$1M

$524K

$557K

$687K
Hospitality
Losses observed per sector
$783K
Information

$600K

$718K

$31M

$3M

$5M

$6M

$12M

$194M

$14M

$62M

$217M

Losses observed per sector

Sector

Geometric mean Median 95th percentile

Sector
Management

Geometric mean Median 95th percentile
$140M
$332K

$343K

Administrative

$318K

$529K

$31M

Manufacturing
Administrative

$1M
$318K

$1M
$529K

Agriculture

$1M

$2M

$3M

Mining
Agriculture

$1M
$1M

$1M
$2M

Construction

$164K

$189K

$5M

Other services
Construction

$262K
$164K

$348K
$189K

Education

$226K

$249K

$6M

Professional
Education

$400K
$226K

$736K
$249K

Entertainment

$147K

$282K

$12M

Public
Entertainment

$234K
$147K

$214K
$282K

Financial

Healthcare

Hospitality

Information

$951K

$1M

$194M

Real Estate
Financial

$524K

$557K

$14M

Retail
Healthcare

$687K

$600K

$62M

Trade
Hospitality

$244K
$951K

$236K
$1M

$872K
$524K

$746K
$557K

$902K
$687K

$1M
$600K

$783K

$718K

$217M

Transportation
Information

$286K
$783K

$490K
$718K

Management

$343K

$332K

$140M

Utilities
Management

$113K
$343K

$146K
$332K

$42M
$31M

$2M
$3M

$41M
$5M

$17M
$6M

$18M
$12M

$2M
$194M

$45M
$14M

$23M
$62M

$23M
$217M

$3M
$140M

Manufacturing

Mining

$1M

$1M

$1M

$1M

$42M

Manufacturing

$1M
$42M
Source: IRIS 2025 (Cyentia Institute)

$1M

$2M

Mining

$1M

$1M

Other services

Figure A3: Loss magnitude summary statistics by sector (Table 4 in IRIS 2022)

$41M

Other services

$262K

$348K

$262K

$348K

Professional

$400K

$736K

$17M

Professional

$400K

$736K

Public

Real Estate

Retail

Trade

$234K

$214K

$18M

Public

$234K

$214K

$244K

$236K

$2M

Real Estate

$244K

$236K

$872K

$746K

$45M

Retail

$902K

$1M

$23M

Trade

$872K

$746K

$902K

$1M

Transportation

$286K

$490K

$23M

Transportation

$286K

$490K

Utilities

$113K

$146K

$3M

Utilities

$113K

$146K

$2M

$41M

$17M

$18M

$2M

$45M

$23M

$23M

$3M

Source: IRIS 2025 (Cyentia Institute)

Source: IRIS 2025 (Cyentia Institute)

Figure A4: Distribution of reported cyber event losses by annual revenue of affected firms (Figure 7 in IRIS
2022)

35

THE CYENTIA INSTITUTE CYENTIA.COMIRIS 2025 IT'S ABOUT TIME$2M$57M$6M$259M$412K$11M$325K$7M$446K$12M$2M$271MTypicalExtremeLess than $10M$10M to $100M$100M to $1B$1B to $10B$10B to $100BMore than $100B$1K$10K$100K$1M$10M$100M$1BSource: IRIS 2025 (Cyentia Institute)THE CYENTIA INSTITUTE IS A WIDELY-RESPECTED, RESEARCH AND DATA SCIENCE FIRM
WORKING TO ADVANCE CYBERSECURITY KNOWLEDGE AND PRACTICE.

We accomplish that goal through collaborative research publications like the
IRIS series and analytic services that help our clients manage cyber risk.

Visit cyentia.com for more information.