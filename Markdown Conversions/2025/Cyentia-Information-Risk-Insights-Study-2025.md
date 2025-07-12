Information Risk
Insights Study
It's About Time

IRIS

2
0
2
5

## Table of Contents
- [Introduction](#introduction)
- [Acknowledgements](#acknowledgements)
- [KEY FINDINGS](#key-findings)
- [1Q ARE SECURITY INCIDENTS BECOMING MORE COMMON?](#1q-are-security-incidents-becoming-more-common)
  - [Are all types of incidents following the same trend?](#are-all-types-of-incidents-following-the-same-trend)
  - [Key Risk Insight](#key-risk-insight)
- [2Q DO INCIDENT TRENDS DIFFER ACROSS ORGANIZATIONS?](#2q-do-incident-trends-differ-across-organizations)
  - [Key Risk Insight](#key-risk-insight-1)
- [3Q IS THE PROBABILITY OF INCIDENTS INCREASING?](#3q-is-the-probability-of-incidents-increasing)
  - [Key Risk Insight](#key-risk-insight-2)
- [4Q HAVE SECURITY INCIDENTS GOTTEN MORE COSTLY?](#4q-have-security-incidents-gotten-more-costly)
  - [Key Risk Insight](#key-risk-insight-3)
- [5Q DO LOSS TRENDS DIFFER AMONG EVENT TYPES?](#5q-do-loss-trends-differ-among-event-types)
  - [Key Risk Insight](#key-risk-insight-4)
- [6Q ARE INTRUSION METHODS CHANGING OVER TIME?](#6q-are-intrusion-methods-changing-over-time)
  - [Key Risk Insight](#key-risk-insight-5)
- [7Q WHAT ARE WE MISSING FROM CURRENT EVENTS?](#7q-what-are-we-missing-from-current-events)
  - [Key Risk Insight](#key-risk-insight-6)
- [METHODOLOGY](#methodology)
  - [Data Collection](#data-collection)
  - [Incident Likelihood](#incident-likelihood)
  - [Financial Losses](#financial-losses)
- [INCIDENT PATTERN DEFINITIONS](#incident-pattern-definitions)
- [CHARTS & TABLES FROM PRIOR IRIS STUDIES](#charts--tables-from-prior-iris-studies)

## Introduction
Welcome to the 2025 edition of the (roughly) biennial Information Risk Insights Study (IRIS). The last one was in 2022, so it’s about time we got this to you. Thanks for your patience.

Fittingly, time is of the essence in this IRIS. Not just because it’s a tad overdue, but because it’s literally about time—cyber risk trends over time, to be specific.

Cybersecurity is ever-changing, and there’s an implicit assumption that risk is always increasing. But is it?

Are cyber events occurring at greater frequency? Is an organization more likely to have a breach now than 15 years ago? Which types of incidents have become more common over time? Have the financial impacts of cyber events increased or decreased? Are risk factors trending the same way for all sectors and sizes of organizations?

We explore these questions and more by analyzing a huge historical dataset of cyber events and losses from 2008 through 2024. As always, our goal is to dispel the fog of FUD surrounding cyber risk so you can see it more clearly and manage it more effectively. Thanks for reading!

## Acknowledgements
The Cyentia Institute wishes to acknowledge and thank the Cybersecurity Division and the Office of the Chief Economist at the Cybersecurity and Infrastructure Security Agency (CISA) for sponsoring this study. It is our sincere hope that this research will aid community efforts to manage cyber risk.

“Time isn't a straight line... It's all bumpy wumpy.”[^1]
~The Eleventh Doctor

[^1]: “Actually, from a non-linear, non-subjective viewpoint, it's more like a big ball of wibbly-wobbly, timey-wimey stuff.” - The Tenth Doctor

The IRIS research draws heavily upon Zywave’s (formerly Advisen) Cyber Loss Data, which contains over 150,000 security incidents[^2] and associated financial losses[^3] spanning decades. The data is compiled from publicly available sources, such as breach disclosures, public company filings, litigation details, and Freedom of Information Act requests.

It is the most comprehensive source of cybersecurity incidents and losses available. Additionally, Cyentia does extensive processing of this base dataset to extend and enrich it for cyber risk analysis use cases.

[^2]: We use the terms security incident, cyber event, and loss event interchangeably. This refers to actual incidents that compromised the confidentiality, integrity, or availability of a firm’s information assets.
[^3]: We use the terms losses or costs to refer to the financial consequences of incidents.

## KEY FINDINGS

*   On average, 3,000 significant security incidents are publicly reported or discovered each quarter. That’s a 650% increase over the last 15 years.
*   Cyber events affecting smaller businesses are far more common overall, but relative to population size, the rate among the largest corporations is 620 times higher.
*   The annual probability of any given organization experiencing a cyber event has almost quadrupled since 2008.
*   The probability of a <$1B firm suffering an incident has more than doubled, while the annual likelihood for a $100B+ organization has fallen 50%.
*   Losses from a typical security incident have absolutely exploded, rising 15-fold from a median of $190K to almost $3 million!
*   The cost of more extreme “tail loss” events is also up 5-fold, ballooning to $32 million.
*   Cyber events aren’t just costing more—they’re hurting the bottom line more than ever before. We’ve seen an 8-fold increase in costs as a proportion of annual revenue.
*   Median losses for professional services firms are up 25x over the last 15 years! Alternatively, there’s been a huge decrease in loss magnitude among retailers.
*   Compromising user credentials remains the most common intrusion technique over the last decade, fluctuating between 43% and 60% of all incidents.
*   Exploitation of web applications is up 6x for smaller firms, while targeting third-party relationships has doubled among large organizations.

Like what you see? Join the vision!

We intend to continue the IRIS in the future to discover even more insights for managing information risk. If you’d like to join in that effort by contributing relevant data or sponsoring research, please reach out to us via the contact form at [www.cyentia.com/iris](www.cyentia.com/iris).

## 1Q ARE SECURITY INCIDENTS BECOMING MORE COMMON?

To many of you, the answer to this question seems so obvious that it’s hardly worth asking. But we’re not ones to let any assumption go unchallenged. As it turns out, this one is solidly backed by historical data—at least in terms of reported incidents[^4]. Figure 1 shows a 650% increase in the average number of incidents added to the public record each quarter in 2024 (~3,000) versus the rate set 15 years ago (~450).

But there’s a lot more going on than simply “incidents are way up!”[^5] The proliferation of large-scale data breaches combined with the rolling out of breach disclosure laws certainly drove the steady climb early in this timeframe. The plateau beginning in 2013 corresponds with the emergence of advanced persistent threats (APTs)[^6] that employed a “low and slow” rather than “smash and grab” strategy. The reacceleration circa 2019 was spurred by the rapid rise of ransomware (see Figure 2) and exacerbated by the COVID-19 pandemic. We could go on, but you get the point. These trends have reasons.

[^4]: This entire report is based on analyzing incidents that make their way into the public record through outward signs or impacts, mandatory reporting, voluntary disclosure, company filings, public lawsuits, etc.
[^5]: Yes—we’re aware that the “incidents are way down” in the last quarter of 2024. But we’re fairly confident that number will go up once the reporting lag catches up and flushes all those as-yet-unknown events into the open. Spoiler alert: we test (and confirm) this in Q7.
[^6]: To be clear, we’re not saying APT attacks started in 2013. But that’s when Mandiant’s APT1 report published and community awareness of these events ballooned. This slowed the rate of publicly reported incidents because attackers (even cybercriminals) were more discrete and much of the threat intel and incident response community was focused on APTs rather than standard cybercriminals.

![Line chart showing the number of security incidents publicly reported or discovered each quarter from 2008 to 2024. The chart shows a general upward trend with a plateau in the mid-2010s and a reacceleration around 2019, ending with a dip in the final quarter of 2024 attributed to reporting lag.](Image description)
Figure 1: Number of security incidents publicly reported or discovered each quarter

### Are all types of incidents following the same trend?

We just mentioned the rise of ransomware, which prompts a related question: Are all types of incidents trending the same way? The crisscrossed lines in Figure 2 are sufficient for a definitive “nope,” but let’s highlight some of these trends that meaningfully impact organizations’ security strategies.

The data in our analysis is clear:

"NO"

At the top of Figure 2, below, system intrusion (unauthorized access to systems, applications, or networks) has long reigned supreme among incident patterns[^7]. The particular techniques attackers use to infiltrate networks and systems have undoubtedly changed, but we’ll dig into that later (see Q6). For now, simply observe that the most common category of incident experienced by organizations hasn’t really changed in the last 15 years.

[^7]: See Appendix B for definitions of these incident patterns.

![Line chart showing the relative frequency (percentage of all incidents) of different incident patterns over time from 2009 to 2024 (rolling 12mo.). System intrusion is consistently the most frequent. Ransomware shows a sharp increase from around 2019. Accidental disclosure shows a sharp decrease over the same period. Insider misuse and physical threat show downward trends.](Image description)
Figure 2: Relative frequency of incident patterns over time (rolling 12mo. 2009-2024)

Now let’s also observe what has changed. The aforementioned rise of ransomware in recent years is, in fact, unprecedented. So is accidental disclosure’s precipitous drop over roughly the same period. We could go into far more detail on ransomware trends, but we’ve already done that in another IRIS.

We’d love to think that “oopsies” as a major cause of data disclosure are a thing of the past, but we suspect human nature will reassert itself at some point.

Physical threats and insider misuse show a marked downward trend over the years. Compared to more scalable remote alternatives, the “hands-on” approach to data theft has fallen out of favor. Data handling regulations and endpoint protections—such as encryption at rest—have further contributed to its decline. Insider misuse never rises above fourth place among all incident patterns, which goes against the long-standing “employees are the enemy” mentality. Sure, employees are often targeted in cyberattacks, but they’re usually not acting with malicious intent.

### Key Risk Insight

The data shows how fluid and contextual the cyber threat landscape really is and how important your firmographic footprint is to that, as we will show throughout this report.

Quantifying that risk, especially at the board level, means understanding these patterns as time sensitive, not timeless.

Today’s dominant risk may be tomorrow’s footnote, and cyber risk models need to keep pace.

Further, if your security strategy isn’t recalibrating with these changes in risk, you’re planning for a past that no longer exists.

~ Jack Freund
Executive Fellow | The Cyentia Insitute

If it seems like a lot more incidents are happening these days, it’s not just recency bias.

The overall rate has seen more than a sixfold increase over the last 15 years.

## 2Q DO INCIDENT TRENDS DIFFER ACROSS ORGANIZATIONS?

This seems like another obvious answer on the surface because it’s well known that certain organizations make more attractive targets, some have poor defenses, and others are just plain unlucky. But what we’re really after here is whether there are inherent differences between different types of firms. Figure 3 attempts to open the door to that question by comparing trends across organizations grouped by their annual revenue.

![Line chart showing the proportion of all incidents in each revenue tier over time from 2009 to 2024 (rolling 12mo.). Smaller businesses (<$100M) account for the largest and growing share of incidents, while larger organizations (>$1B) show a declining share.](Image description)
Figure 3: Proportion of all incidents in each revenue tier (rolling 12mo. 2009-2024)

Rebutting the “Who would attack little ‘ol us?” argument, smaller businesses (<$100M annual revenue) see the biggest overall share of incidents. What’s more, that share is growing over time. The proportion of events affecting larger organizations (>$1B annual revenue), on the other hand, appears to be declining over the last 15 years.

The data in our analysis is clear: smaller businesses—those under $100M in annual revenue—account for the largest share of incidents, countering the idea that they're too minor to target.

There’s more to this story, however, as astute readers have probably already discerned. The obvious objection to the prior chart’s depiction of trends is that it does not account for the number of firms that exist in each revenue tier[^8]. Sure, more incidents affect small businesses, but they vastly outnumber large corporations.[^9] What happens when we factor in the relative number of firms in each group? Figure 4 gives the answer—a complete reversal of fortune!

[^8]: We use data from Dun & Bradstreet for the number of organizations in each revenue tier.
[^9]: The Small Business Administration estimates that 99.9% of all businesses are small. [https://advocacy.sba.gov/2024/07/23/frequently-asked-questions-about-small-business-2024/](https://advocacy.sba.gov/2024/07/23/frequently-asked-questions-about-small-business-2024/)

![Line chart showing the relative number of incidents compared to the number of firms in each revenue tier over time from 2009 to 2024 (rolling 12mo.). The chart shows multiples indicating how many times higher the incident rate is compared to the number of firms. Larger revenue tiers consistently show much higher multiples than smaller tiers, although the trend for the largest tiers is declining.](Image description)
Figure 4: Relative number of incidents to number of firms in each revenue tier (rolling 12mo. 2009-2024)

The multiples shown in Figure 4 compare the number of incidents across a revenue tier with the number of organizations within it. The higher the multiple, the higher the average rate of incidents per organization in each tier. While larger organizations show a declining trend in the relative number of incidents, they remain disproportionately affected by them. The $100B+ tier has experienced 620 times more incidents than the number of megacorporations in this segment. Though the smallest firms experience the largest number of incidents in absolute terms, only a fraction of them (0.53x) are actually affected.

Let’s turn next to frequency-based disparities among different industries. Since we’ve established the importance of adjusting for the number of firms in each segment, we can skip to the punch line. Figure 5 groups sectors[^10] based on their relative event frequency.[^11]

[^10]: Sectors throughout this report use the North American Industry Classification System (NAICS). Our labels are short versions of NAICS sectors—generally the first word of the official sector name.
[^11]: A multiple >1 indicates higher relative incident frequency based on the number of firms in a sector; <1 indicates the opposite (low relative frequency).

![Scatter plot grid showing the relative number of incidents compared to the number of firms in each sector over time from 2009 to 2024 (rolling 12mo.). Sectors are grouped into panels based on their historical relative frequency (Very High, High, Low, Very Low). Lines within each panel show the trend for specific sectors. Public and Management are in Very High. Finance and Information are in High, showing declining trends. Utilities, Mining, Manufacturing, and Transportation are in Low, showing increasing trends.](Image description)
Figure 5: Relative number of incidents to number of firms in each sector (rolling 12mo. 2009-2024)

The Public and Management sectors are the only two that have historically exhibited a very high relative incident frequency. For the former, we attribute that to mandatory disclosure requirements that typically exceed those in the private sector.

### Key Risk Insight

Incidents involving small and midsize businesses (SMBs) are far more common overall, but the relative incident frequency among large enterprises is much higher.

The Management sector is a bit of an oddball in NAICS, consisting mainly of holding companies. We suspect part of what’s going on here is that incidents affecting their subsidiaries are being attributed to them as the parent entity.

Moving to the upper-right panel, the Finance sector has historically seen a high share of incidents relative to the number of firms that exist. But that rate has fallen over time, perhaps due in part to the industry’s outsized security budgets. The Information sector continues to experience an elevated incident rate, yet is currently well below its high-water mark. Together, these industries control money and data flowing through the economy, so it’s no surprise they receive more than their fair share of cyberattacks.

Energy and supply chain sectors are creeping up in incident frequency—Utilities, Mining, Manufacturing, and Transportation are no longer sitting safely below the line.

Industries with historically low relative incident frequencies are split into two groups—those likely to remain low for the foreseeable future and those that will soon cross over the line of demarcation. We find it unsettling to see energy and supply chain sectors such as Utilities, Mining, Manufacturing, and Transportation (which includes oil and gas pipelines in NAICS) increasing in relative frequency. The Professional sector has already crossed that line, which is quite concerning given that they offer advice and services to the rest of us.

## 3Q IS THE PROBABILITY OF INCIDENTS INCREASING?

This question may initially sound similar to the previous two, but those involved tallying the total number of incidents reported across many organizations. Here, we explore how the likelihood of a single organization having an incident is changing over time. If that nuance isn’t quite clear, think of it like this: what are the chances your firm will suffer a significant incident this year?

We’ll begin by changing our perspective from the past to the future—except how the future was modeled in the past… over time. Jeepers, this timey-wimey stuff is confusing, isn’t it? Maybe a chart will help; Figure 6 tracks the modeled probability[^12] of a typical organization[^13] experiencing an incident in the next 12 months.

It is understandable if cybersecurity folks can’t hold back an “I told you so!” here because overall incident probability has almost quadrupled over the last 15 years. We could stop there, issue a press release, and bid you adieu until the next installment, but we’re just getting started.

[^12]: See appendix for details on our approach to modeling annualized incident probability.
[^13]: We use “typical” to remind readers that this model doesn’t account for the many factors that would make incidents more or less likely for a particular organization. We’ll look at some of those later.

![Line chart showing the historical probability of a typical firm having an incident in the next year from 2008 to 2024. The probability increases from around 2.5% in 2008 to over 9% in 2024, with a plateau in the mid-2010s and a sharp rise in the 2020s.](Image description)
Figure 6: Historical probability of a firm having an incident in the next year

The probability that a typical firm will experience a significant security incident has almost quadrupled over the last 15 years.

“But wait,” we hear you saying, “doesn’t the probability for different types of cyber events change over time?”

You’re not wrong. We simply can’t cram everything into this one study.

New studies are always in the pipeline — we regularly publish extra analysis like that on our website at [www.cyentia.com/iris](www.cyentia.com/iris).

What if we told you that the probability of a <$100M firm suffering a security incident has more than doubled, while the chance of a $100B+ megacorporation suffering an incident has dropped by a third over the same time frame? Well, that’s exactly what Figure 7 tells us.

![Line chart showing the annualized incident probability for firms in each revenue tier over time (rolling 12mo.). The probability for smaller firms (<$100M) shows a significant increase, while the probability for the largest firms (>$100B) shows a decrease.](Image description)
Figure 7: Annualized incident probability for firms in each revenue tier (rolling 12mo.)

Unfortunately, our dataset is silent on the underlying factors behind these trends, so all we can offer is some speculation. Perhaps cybercriminals have shifted to more volume-oriented (“low-hanging fruit”) strategies over time. Maybe the pace of digitalization has outpaced SMBs’ ability to defend their growing attack surfaces, while the bigger enterprise security budgets offset that. Maybe increased regulatory pressures on large corporations are gradually hardening enterprise security architectures. Whatever the cause(s), these are important trends that are worth further research by our industry.

So, an organization’s size matters when evaluating the likelihood of incidents. Now, let’s see what happens when we treat industry as a feature of interest. Figure 8 paints that picture.

Allow us to briefly describe what you’re looking at. Sectors are sorted in descending order by the latest probability estimate. So, a typical manufacturing firm has an 11% chance of having a security incident in the next 12 months—up from ~2% 15 years ago.

![Grid of line charts showing the annualized incident probability for firms in selected sectors over time from 2008 to 2024 (rolling 12mo.). Each chart shows the trend for a specific sector, sorted by the latest probability estimate. Manufacturing, Retail, Public, Financial, Healthcare, Utilities, Information, and Entertainment sectors are shown, each with varying trend lines.](Image description)
Figure 8: Annualized incident probability for firms in each sector (rolling 12mo.)

We could spend oodles of time combing through historical evidence behind the peaks and troughs for certain industries, but we’ll leave that to eager readers. Suffice it to say that incident probability trends can be significantly different depending on firmographics (which are reflective of evolving business models, changes in the threat landscape, shifting adversary goals, etc.). That's intuitive, but perhaps seeing this confirmed will help validate the need to incorporate such factors into your cyber risk assessments.

Sorry to disappoint if you were hoping to see updated versions of the old school IRIS charts/tables for incident likelihood by sector and revenue tier. Since this version of the IRIS focuses on trends over time, Figures 7 and 8 replaced those. But we recreated some of the key figures and stuck them in Appendix C as a thank you to our loyal readers.

### Key Risk Insight

Overall, the chances of any given organization experiencing an incident have gone up.

But that trend has flattened or even reversed in some sectors and size tiers.

Our analysis in this section focuses on the likelihood of experiencing at least one security incident within a year. It is possible, of course, for organizations to suffer multiple incidents, and veteran IRIS readers may recall that we've supplied probability tables for two, three, or five incidents in a 12-month period.

We decided not to include that in this edition because a) it's already a long report, and b) feedback suggested most cyber risk models focused on single-event likelihood. However, we have not abandoned that concept and will continue that research outside of this study.

Visit [www.cyentia.com/iris](www.cyentia.com/iris) to get additional analysis of multi-incident probabilities.

## 4Q HAVE SECURITY INCIDENTS GOTTEN MORE COSTLY?

We’ve covered the evolving frequency and likelihood of cyber events—now it’s time to talk dollars and cents. Let’s begin by establishing the distribution of financial losses from cyber events using Figure 9, which reproduces a classic IRIS chart with the latest and greatest data.[^14]

[^14]: All loss amounts considered in this report have been converted to 2024 dollars to adjust for inflation.

![Distribution plot (on a log scale) showing the distribution of reported losses for security incidents from 2015 to 2024. Key statistics like median ($603K), 95th percentile ($32M), geometric mean ($464K), and mean ($14M) are indicated. The plot shows a long tail of large losses and a noticeable bump or "shoulder" in the lower half of the distribution.](Image description)
Figure 9: Distribution of reported losses for security incidents from 2015 to 2024

The typical (median[^15]) incident costs about $600K, while more extreme (95th percentile) losses swell to $32 million. Note that Figure 9 is plotted on a log scale, so the tail of large losses is longer than it appears. If it’s not too much to “shoulder,” also note the bump in the lower half of the distribution. We’ll explore that later.

[^15]: Prior IRIS used the geometric mean for a typical loss. Since the growing “shoulder” in lower part of the distribution pulls the geomean down, the median is better central measure for the updated distribution.

NOTE: Losses analyzed in this study tend to reflect direct losses that are easier to quantify (e.g., response costs or lost revenue) and/or identify from public records (e.g., class action suits or U.S. Securities and Exchange Commission (SEC) filings). Indirect and intangible impacts often aren’t captured. Thus, this represents a conservative view of financial losses associated with cyber events.

Indeed, moving from a static distribution to a more dynamic view reveals some major shifts. Median losses from a security incident have absolutely exploded over the last 15 years