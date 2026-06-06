# Information Risk Insights Study: It's About Time (IRIS 2025)

## Table of Contents
- [Introduction](#introduction)
- [Key Findings](#key-findings)
- [Q1: Are Security Incidents Becoming More Common?](#q1-are-security-incidents-becoming-more-common)
- [Q2: Do Incident Trends Differ Across Organizations?](#q2-do-incident-trends-differ-across-organizations)
- [Q3: Is the Probability of Incidents Increasing?](#q3-is-the-probability-of-incidents-increasing)
- [Q4: Have Security Incidents Gotten More Costly?](#q4-have-security-incidents-gotten-more-costly)
- [Q5: Do Loss Trends Differ Among Event Types?](#q5-do-loss-trends-differ-among-event-types)
- [Q6: Are Intrusion Methods Changing Over Time?](#q6-are-intrusion-methods-changing-over-time)
- [Q7: What Are We Missing From Current Events?](#q7-what-are-we-missing-from-current-events)

---

## Introduction
Welcome to the 2025 edition of the (roughly) biennial Information Risk Insights Study (IRIS). Fittingly, time is of the essence in this IRIS. Not just because it’s a tad overdue, but because it’s literally about time—cyber risk trends over time, to be specific.

Cybersecurity is ever-changing, and there’s an implicit assumption that risk is always increasing. But is it? We explore these questions and more by analyzing a huge historical dataset of cyber events and losses from 2008 through 2024. As always, our goal is to dispel the fog of FUD surrounding cyber risk so you can see it more clearly and manage it more effectively.

**Acknowledgements**: The Cyentia Institute wishes to acknowledge and thank the Cybersecurity Division and the Office of the Chief Economist at the Cybersecurity and Infrastructure Security Agency (CISA) for sponsoring this study.

---

## Key Findings
- On average, 3,000 significant security incidents are publicly reported or discovered each quarter. That’s a 650% increase over the last 15 years.
- Cyber events affecting smaller businesses are far more common overall, but relative to population size, the rate among the largest corporations is 620 times higher.
- The annual probability of any given organization experiencing a cyber event has almost quadrupled since 2008.
- Losses from a typical security incident have absolutely exploded, rising 15-fold from a median of $190K to almost $3 million.
- Compromising user credentials remains the most common intrusion technique over the last decade.

---

## Q1: Are Security Incidents Becoming More Common?
Figure 1 shows a 650% increase in the average number of incidents added to the public record each quarter in 2024 (~3,000) versus the rate set 15 years ago (~450).

![Figure 1: Number of security incidents publicly reported or discovered each quarter]

The plateau beginning in 2013 corresponds with the emergence of advanced persistent threats (APTs) that employed a “low and slow” strategy. The reacceleration circa 2019 was spurred by the rapid rise of ransomware (see Figure 2).

![Figure 2: Relative frequency of incident patterns over time]

---

## Q2: Do Incident Trends Differ Across Organizations?
Smaller businesses (<$100M annual revenue) see the biggest overall share of incidents. However, when factoring in the relative number of firms in each group, a complete reversal of fortune occurs.

![Figure 3: Proportion of all incidents in each revenue tier]
![Figure 4: Relative number of incidents to number of firms in each revenue tier]

The Public and Management sectors are the only two that have historically exhibited a very high relative incident frequency.

---

## Q3: Is the Probability of Incidents Increasing?
Overall incident probability has almost quadrupled over the last 15 years.

![Figure 6: Historical probability of a firm having an incident in the next year]

The probability of a <$100M firm suffering a security incident has more than doubled, while the chance of a $100B+ megacorporation suffering an incident has dropped by a third over the same time frame.

---

## Q4: Have Security Incidents Gotten More Costly?
The typical (median) incident costs about $600K, while more extreme (95th percentile) losses swell to $32 million.

![Figure 9: Distribution of reported losses for security incidents from 2015 to 2024]

Median losses from a security incident have risen 15-fold from $190K to almost $3 million.

---

## Q5: Do Loss Trends Differ Among Event Types?
The "shoulder" in the overall loss distribution results from a proliferation of fairly small losses from accidental disclosure events.

![Figure 14: Distribution of reported losses by incident pattern]

While ransomware losses surge past $27M at the high end, top-tier system intrusions have dropped sharply—down to $7.4M from over $200M.

---

## Q6: Are Intrusion Methods Changing Over Time?
Using Valid Accounts to gain illicit access has held the pole position for the entire time period. Exploit Public-Facing Applications and External Remote Services have surged from single-digit percentages to heights of 38% and 30%, respectively.

![Figure 16: Prevalence of ATT&CK Initial Access techniques observed in incidents over time]

---

## Q7: What Are We Missing From Current Events?
We analyzed cyberattacks collected via Feedly’s intelligence capabilities to see what our core incident dataset might be missing.

![Figure 18: Number of security incidents publicly reported or discovered each quarter (including Feedly data)]

The median loss for Feedly-sourced cyber events stands at $28.5M, which is 30x higher than that of our historical dataset ($603K). This corroborates the utility of monitoring current events to help compensate for the reporting lag in risk data.

---
*Note: This report is based on analyzing incidents that make their way into the public record through outward signs or impacts, mandatory reporting, voluntary disclosure, company filings, public lawsuits, etc.*

---

| $786.9M | IRIS 2025 IT'S ABOUT TIME |
|                   |     | $1K | $10K | $100K   | $1M | $10M    | $100M  | $1B     |                           |
Source: IRIS 2025 (Cyentia Institute)
Figure 19: Comparison of reported financial losses from incidents by source
| THE CYENTIA INSTITUTE CYENTIA.COM |     |     |     |     |     |     |     | 29  |     |
| --------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

THE CYENTIA INSTITUTE CYENTIA.COM 30
IRIS
2025
IT'S
ABOUT
TIME
Much of what we see (or don’t see) here goes
back to sourcing methods. The primary source
of our historical loss data, Zywave, has a strong
focus on the insurance and reinsurance market.
They’re diligent in gathering datapoints on all
aspects of losses, both large and small. Minor Key Risk Insight
loss events might be interesting to insurers
managing risk across a large portfolio of
If your cyber risk analysis relies
organizations, but media outlets tend to focus
on near-term trends, consider
on major breaches or disruptions. Since such
incorporating sources that
events rarely go unnoticed, they’re ripe for
emphasize current events to
open-source intel collection. If you’re focused
supplement historical event data.
on tail risk—which is what many execs are
most concerned with—closely tracking these
mega-loss events is essential.
One of my favorite
things about my time
on Verizon's DBIR
team was working
with the scores
of external organizations
that contribute data for
analysis in that report. It's
something I'm glad we've
been able to continue in our
research at Cyentia.
I'm grateful to all our data
partners and sponsors who
make it possible for us to do
impactful research for the
community. Reach out if
you have data that would
unlock new avenues of cyber
risk analysis!
~ Wade Baker PhD
Co-Founder | The Cyentia Insitute

THE CYENTIA INSTITUTE CYENTIA.COM 31
IRIS
2025
IT'S
ABOUT
TIME
A1
ME THODOLOGY
Data Collection
The IRIS research draws heavily upon Zywave’s Cyber Loss Data, which contains over 150,000 security
incidents and associated losses spanning decades. The data is compiled from publicly available sources,
such as breach disclosures, company filings, litigation details, and Freedom of Information Act requests. It
is the most comprehensive source of cybersecurity incidents and losses available.
That said, we’re not claiming this dataset is all-inclusive. We can only analyze incidents that make their
way into the public record through outward signs or impacts, mandatory reporting, voluntary disclosure,
etc. That’s not all the events that occurred over the timeframe, of course, but we have high confidence that
significant cyber events are well represented.
Additionally, Cyentia does extensive processing of Zywave’s base dataset to extend and enrich it for
cyber risk analysis use cases. This is done using a combination of classification models, natural language
processing (NLP), taxonomy mapping, malware behavioral analysis, and manual tagging by our analysts.
Incident and loss data collected by Feedly is used for the last section to study trends we might be missing
from current events. We started with 2024 events identified by Feedly’s Cyber Attacks AI model. We further
refined this by focusing on “memes,” which is Feedly’s method of clustering articles and information on a
trending topic. The point is that we’re not simply counting articles in this analysis. Finally, we reviewed the
identified events to train a classification model to distinguish successful incidents affecting organizations
from other threats and trends that aren’t comparable to our core dataset.
GOT DATA FOR THE NEXT IRIS?
If you have information on security incidents
and losses and might be willing to contribute
anonymized data for analysis in a future IRIS,
please reach out! We’re especially keen to
incorporate insights from cyber insurance
claims and incident response investigations.

THE CYENTIA INSTITUTE CYENTIA.COM 32
IRIS
2025
IT'S
ABOUT
TIME
Incident Likelihood
Though we don’t delve into it in this edition, readers of prior IRIS may recall that we have modeled the
frequency of security incidents over a fixed 10 year time period, allowing for the fact that organizations can
have more than one in a single year. We took the same approach in this edition, expanding the model to
include a time component. Ultimately, we present estimates as the annual probability of an organization
experiencing at least one event.
To do this, we divide our historical dataset into 12-month rolling windows and count the number of incidents
for each organization. This gives us a large number of observations that allow us to more confidently model
the annualized loss event frequency.
We then treat these observations as samples from an underlying probability distribution and use random
effects models to estimate the parameters both overall and within specific slices like industry and revenue
bands over time. The result is a closed-form representation of the probability that an organization will
experience a certain number of incidents in a given year that can change over time.
Additionally, in prior IRIS reports we reported both upper and lower bound estimates for incident likelihood.
We’ve dropped that distinction in this edition in favor of exclusively using the more risk-averse upper bound
estimate.
In a nutshell, the difference between these approaches stems from the count of organizations used as the
denominator for the calculation. We don’t know how many exist throughout the world, so the upper bound
uses the total number of organizations that exist in our historical incident database. While it’s true that this
approach excludes some extremely secure or lucky firms, the fact is that those prone to incidents in the
future have probably had one at some point in the past. The result is a more conservative estimate that we
believe is more suitable for risk management.
Financial Losses
Financial losses tend to be less reported than other data points for cyber events. There are many reasons
for this, but the result is that the majority of incidents in our dataset do not include anything about losses.
Those that do tend to reflect direct losses that are easier to quantify (e.g., response costs or lost revenue)
and/or identify from public records (e.g., class action suits or SEC filings). Indirect and intangible impacts
usually aren’t captured.
The good news, from a data standpoint, is that the record of losses from major security incidents—like
those we analyze in this study—is more complete than for minor events due to increased visibility and
reporting. Thus, we hold that our loss dataset is sufficient to form a well-supported model of cyber events
over the last 15 years.
Note that all financial loss values presented in this report have been adjusted for inflation.

THE CYENTIA INSTITUTE CYENTIA.COM 33
IRIS
2025
IT'S
ABOUT
TIME
A2
INCIDE NT PAT TE RN
DE FINITIONS
All security incidents in our historical dataset are assigned one of these mutually exclusive23 patterns using
a combination of natural language processing techniques and human expert assessment.
ACCIDENTAL DISCLOSURE: Data stores that are inadvertently left accessible to
unauthorized parties, typically through misconfigurations on the part of the data custodian.
DOS ATTACK: Any attack intended to render online systems, applications, or networks
unavailable, typically by consuming processing or bandwidth resources.
DEFACEMENT: Any unauthorized content modification to an organization’s website or
other online assets.
FRAUD OR SCAM: Any incident that primarily employs various forms of deception to
defraud the victim of money, property, identity, information, and so on.
INSIDER MISUSE: Inappropriate use of privileged access, either by an organization’s own
employees and contractors or a trusted third party.
PHYSICAL THREATS: Threats that occur via a physical vector, such as device tampering,
snooping, theft, loss, sabotage, and assault.
RANSOMWARE: A broad family of malware that seeks to encrypt data with the promise to
unlock upon payment or seeks to completely eradicate data/systems without the pretense
of collecting payment.
SYSTEM FAILURE: All unintentional service disruptions resulting from system, application,
or network malfunctions or environmental hazards.
SYSTEM INTRUSION: All attempts to compromise systems, applications, or networks by
subverting logical access controls, elevating privileges, deploying malware, and so on.
23 Yes, it’s true that an incident could involve more than one of these (e.g., system intrusion and ransomware). However, the purpose of these patterns is to represent the primary
nature of the event.

THE CYENTIA INSTITUTE CYENTIA.COM 34
IRIS
2025
IT'S
ABOUT
TIME
CHARTS & TABLES FROM
PRIOR IRIS STUDIES
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
Figure A1: Relative probability of one or more loss events among sectors (Figure 5 in IRIS 2022). The point
of comparison is the overall median across all organizations.
Figure A2: Relative probability of one or more loss events among annual revenue tiers. The point of
comparison is the overall median across all organizations.
rotces
naidem
ot
evitaleR
A3
Source: IRIS 2025 (Cyentia Institute)
More than $100B (3.46x)
$10B to $100B (2.49x)
$1B to $10B (1.20x)
$100M to $1B (0.80x)
$10M to $100M (0.67x)
Less than $10M (0.60x)
Source: IRIS 2025 (Cyentia Institute)

Losses observed per sector
|                            |     |     |     |     |     | Sector                     |     | Geometric mean |       | Median 95th percentile |       |
| -------------------------- | --- | --- | --- | --- | --- | -------------------------- | --- | -------------- | ----- | ---------------------- | ----- |
|                            |     |     |     |     |     | Administrative             |     |                | $318K | $529K                  | $31M  |
|                            |     |     |     |     |     | Agriculture                |     |                | $1M   | $2M                    | $3M   |
|                            |     |     |     |     |     | Construction               |     |                | $164K | $189K                  | $5M   |
|                            |     |     |     |     |     | Education                  |     |                | $226K | $249K                  | $6M   |
|                            |     |     |     |     |     | Entertainment              |     |                | $147K | $282K                  | $12M  |
|                            |     |     |     |     |     | Financial                  |     |                | $951K | $1M                    | $194M |
|                            |     |     |     |     |     | Healthcare                 |     |                | $524K | $557K                  | $14M  |
|                            |     |     |     |     |     | Hospitality                |     |                | $687K | $600K                  | $62M  |
| Losses observed per sector |     |     |     |     |     | Losses observed per sector |     |                |       |                        |       |
|                            |     |     |     |     |     | Information                |     |                | $783K | $718K                  | $217M |
Sector Geometric mean Median 95th percentile Sector Management Geometric mean $343K Median $332K 95th percentile $140M
Administrative $318K $529K $31M AMdamnuinfaiscttruartiivneg $3$118MK $5$219MK $$4321MM
Agriculture $1M $2M $3M MAginriicnuglture $$11MM $$12MM $$23MM
Construction $164K $189K $5M OCothnesrt rsuecrtvioicnes $$216624KK $$314889KK $4$15MM
Education $226K $249K $6M PEdroufceastsioionnal $$420206KK $$723469KK $1$76MM
Entertainment $147K $282K $12M PEnutbelirctainment $$213447KK $$221842KK $$1182MM
Financial $951K $1M $194M RFienaaln Ecsiatalte $$294541KK $2$316MK $1$924MM
Healthcare $524K $557K $14M RHeetaalitlhcare $$857224KK $$754567KK $$4154MM
Hospitality $687K $600K $62M THroasdpeitality $$960827KK $6$010MK $$2632MM
Information $783K $718K $217M TInrfaonrsmpaotritoantion $$278863KK $$479108KK $$22137MM
Management $343K $332K $140M UMtailnitaiegsement $$131433KK $$134362KK $1$430MM
Manufacturing $1M $1M $42M Manufacturing S$o1uMrce: IRIS$ 120M25 (Cyentia Ins$ti4tu2teM)
| Mining |     |     | $1M $1M |     | $2M | Mining |     |     | $1M | $1M | $2M |
| ------ | --- | --- | ------- | --- | --- | ------ | --- | --- | --- | --- | --- |
Other seFrviigcuesre A3: Loss $m26a2gKnitu$d3e48 sKummary st$a4t1isMtics Obyth esre scetrovric (eTsable 4 in IR$I2S6 22K022$)348K $41M
| Professional |     | $400K | $736K |     | $17M | Professional |     |     | $400K | $736K | $17M |
| ------------ | --- | ----- | ----- | --- | ---- | ------------ | --- | --- | ----- | ----- | ---- |
| Public       |     | $234K | $214K |     | $18M | Public       |     |     | $234K | $214K | $18M |
Real Estate $244K $236K $2M Real Estate Typical $244K Extreme $236K $2M
| Retail          |     | $872K | $746K |     | $45M | Retail |     |     | $872K | $746K | $45M |
| --------------- | --- | ----- | ----- | --- | ---- | ------ | --- | --- | ----- | ----- | ---- |
| More than $100B |     |       |       |     |      |        | $6M |     |       | $259M |      |
| Trade           |     | $902K | $1M   |     | $23M | Trade  |     |     | $902K | $1M   | $23M |
Transportation $286K $490K $23M Transportation $286K $490K $23M
Ut$i1li0tiBe sto $100B $113K $146K $3M $U2Mtilities $113K $$217416MK $3M
Source: IRIS 2025 (Cyentia Institute) Source: IRIS 2025 (Cyentia Institute)
| $1B to $10B |     |     |     |     |       | $2M |     |      | $57M |     |     |
| ----------- | --- | --- | --- | --- | ----- | --- | --- | ---- | ---- | --- | --- |
|             |     |     |     |     | $446K |     |     | $12M |      |     |     |
$100M to $1B
| $10M to $100M  |     |     |      |       | $325K |     |     | $7M  |       |     |     |
| -------------- | --- | --- | ---- | ----- | ----- | --- | --- | ---- | ----- | --- | --- |
| Less than $10M |     |     |      |       | $412K |     |     | $11M |       |     |     |
|                | $1K |     | $10K | $100K |       | $1M |     | $10M | $100M | $1B |     |
Source: IRIS 2025 (Cyentia Institute)
Figure A4: Distribution of reported cyber event losses by annual revenue of affected firms (Figure 7 in IRIS
2022)
IRIS 2025 IT'S ABOUT TIME
THE CYENTIA INSTITUTE CYENTIA.COM 35

THE CYENTIA INSTITUTE IS A WIDELY-RESPECTED, RESEARCH AND DATA SCIENCE FIRM
WORKING TO ADVANCE CYBERSECURITY KNOWLEDGE AND PRACTICE.
We accomplish that goal through collaborative research publications like the
IRIS series and analytic services that help our clients manage cyber risk.
Visit cyentia.com for more information.