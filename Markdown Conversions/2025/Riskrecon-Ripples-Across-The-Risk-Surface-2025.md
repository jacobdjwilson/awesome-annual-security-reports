# Ripples Across The Risk Surface 2025

**Organization:** Riskrecon  
**Year:** 2025  

## Table of Contents
- [Introduction](#introduction)
- [Findings](#findings)
- [Important Terms](#important-terms)
- [How Common Are Multi-Party (Ripple) Incidents?](#how-common-are-multi-party-ripple-incidents)
- [How Do Ripple Events Differ From Single-Party Incidents?](#how-do-ripple-events-differ-from-single-party-incidents)
- [Who Bears The Costs From Ripple Incidents?](#who-bears-the-costs-from-ripple-incidents)
- [What Kinds Of Firms Generate Or Receive Ripple Incidents?](#what-kinds-of-firms-generate-or-receive-ripple-incidents)
- [How Do Ripples Flow Between Sectors & Revenue Bands?](#how-do-ripples-flow-between-sectors--revenue-bands)
- [Conclusion](#conclusion)

---

## Introduction

As our parents taught us, our actions impact the people around us. However, in the case of cybersecurity incidents, it is also the case that the things that happen to us also impact those around us. When one organization’s security incident reaches out to impact third parties, we refer to these multi-party incidents as “ripple events.” These ripple events have been the subject of several reports in our IRIS series over the years.

In the first ripple reports, we introduced our definition of multi-party ripple incidents and described their essential attributes. We covered their frequency and size, who is impacted by them, and the magnitude of those impacts. Later, we used the MITRE ATT&CK framework to dive deeper into the mechanics of ripple incidents. In this latest edition, we’re revisiting some of these previous topics with more precision (and some models!) to provide more actionable insights on these types of incidents.

This edition examines more than 1,500 cybersecurity ripple incidents covering the time period from 2008 to 2024. This collection of incidents involved more than 1.2K unique generating firms and more than 12K[^1] unique receiving firms. In this report, we aim to update our understanding of how these incidents occur and propagate to help your organization avoid being caught up in someone else’s mess (or being the cause of someone else’s mess, as our parents used to scold us). Feel free to review the terminology below before diving into the report.

[^1]: Yes, that’s a 10x difference between generating and receiving these events!

---

## Findings

- **Less common but more costly.** While single-party security incidents are more likely to occur, multi-party ripple events routinely trigger losses that are routinely 10 times higher for the organizations that generate them.
- **Downstream losses are rising.** Historically, the primary victims (generators) of ripple events bore most of the costs, but losses for organizations impacted downstream (receivers) have risen steadily and now rival those of initial victims.
- **Larger firms face outsized risk.** More smaller firms get swept up in ripple events, but larger organizations ($10B+ revenue) are twice as likely on a per-firm basis to both generate and receive multi-party incidents.
- **Exposure amplified in some sectors.** Finance, Healthcare, and Education sectors are disproportionately affected as receivers, while Finance, Public, and Utilities are more likely to generate ripple effects.
- **Ripples cascade across tiers.** Propagation tends to cluster among mid-to-large firms but often flows downstream from mid-sized organizations into their smaller suppliers and partners, magnifying systemic risk.
- **Threat profiles differ dramatically.** Ripple incidents show markedly higher involvement from nation-states, hacktivists, and criminal actors compared to single-party events. System intrusions, DDoS attacks, and fraud schemes dominate multi-party incidents.

---

## Important Terms

**Security Incident:** An incident that compromises the confidentiality, integrity, or availability of an information asset.

**Multi-Party Incident (aka “Ripple events”):** A cyber incident that affects multiple organizations. This usually involves a compromise to a central victim that generates downstream loss incidents for various third parties.

---

## How Common Are Multi-Party (Ripple) Incidents?

Figure 1 starts us off with a picture of how the frequency of ripple incidents has shifted over time. We’ve plotted counts of unique ripple events, using the date of the generating incident to place it in time. The frequency of ripple events grew steadily from 2008, peaking close to 150 each year during the 2010s before stabilizing at closer to 100 per year.

There is usually a reporting lag for cyber incidents in our incident data, so the count from 2024 is likely artificially low. We used a simple time series model[^2] on the cumulative count of ripple incidents over time to extrapolate the likely totals for both 2024 and 2025, shown as “Projected” counts in Figure 1. The error bars represent the approximate range we can expect the projected counts to land in.

![Figure 1: Counts of multi-party (ripple) incidents over time showing actual vs projected data from 2009 to 2025.]

[^2]: “Simple”, as in “it won’t impress anyone at a statistics conference, but it probably works decently well.”

---

## How Do Ripple Events Differ From Single-Party Incidents?

Now, when we were snarky teenagers[^3] we might have sighed and said that single-party incidents involve a single firm and ripple incidents involve several, but we can do better than that. Also, we can dispense with one large difference immediately: single-party incidents are far more common than ripple incidents. To give a sense of scale to this claim, consider that the overall modeled likelihood of a single-party incident is ~8.4%[^4] while the probability for ripple events is only ~0.7%. Keep that in mind as we progress through this section: in general, single-party incidents are much more likely to impact your firm.

With that out of the way, let’s turn to some basic characteristics like firm size and sector, where we use the ripple generator to assign an incident to a revenue band or industry sector.

![Figure 2: Proportion of single vs. multi-party incidents by annual revenue, showing distributions across revenue bands from less than $10M to more than $100B.]

Figure 2 shows the proportion of single-party incidents and ripple incidents by firm revenue. There is some variation, but overall the distributions are roughly similar, with the smallest firms taking up the largest share and the proportions generally declining as the firms get larger.

In general, single and multi-party incidents follow similar patterns across firmographic dimensions—but notable exceptions exist.

Moving on to differences by sector in Figure 3, we see roughly similar distributions. While it may seem boring to highlight ways in which single-party and ripple incidents are roughly similar, it shows that these larger, multi-party incidents have the potential to impact firms of the same size and sector as single-party incidents do.

![Figure 3: Proportion of single vs. multi-party incidents by sector, comparing incident frequency across various industry verticals.]

Like you, we are more interested in differences than similarities. To that end, Figure 4 shows comparisons of single-party and ripple events by incident pattern[^5] and actor.

Focusing on pattern first, while system intrusion is fairly equally common, some other differences emerge. For example, accidental disclosures, physical threats, and insider misuse are considerably more prevalent among single-party incidents. On the other side of the ledger, DoS attacks, scam or fraud, and defacement incidents are all much more common among ripple incidents.

When it comes to who is responsible for these attacks, there are also some significant differences in the “actor” portion of Figure 4. Employees appear to be much more likely to be involved in single-party incidents, which aligns with the prevalence of accidental disclosures and insider misuse patterns.

On the other hand, ripple incidents see a much higher prevalence of hacktivists, nation states and criminal Individuals as the actors. While the latter two make some sense as actors looking to inflict as much damage as possible, the hacktivist difference may seem surprising at first.

We dug into the specific incidents in our data and discovered two large categories of attack. First, many involve hostile attacks against governments or nation-states for socio-political objectives. The other major grouping consists of attempts to embarrass the target into fixing a specific security vulnerability.

[^3]: Apologies to all of our parents. We may have been a wee bit insufferable.
[^4]: See our IRIS reports for this and more!
[^5]: See Appendix A for definitions of incident patterns.

> **WANT MORE RESEARCH ON RIPPLES?**
> The report you’re reading now isn’t our first Ripples Rodeo. It started way back in 2019 with the original Ripples Across the Risk Surface, with another edition in 2021. In late 2023, we took the series in a new direction with Ripples Across the ATT&CK Surface.
> 
> That study analyzed nearly 900 historical ripple events to identify the top MITRE ATT&CK techniques used to generate and propagate them. We also examined top mitigations for the most common techniques to help your organization from getting swept up in their wake.

![Figure 4: Proportion of single vs. multi-party incidents by pattern and actor, highlighting the prevalence of specific threat types and threat actors.]

---

## Who Bears The Costs From Ripple Incidents?

To answer this question, we first classified our ripple incidents based on the proportion of all associated losses that were borne by the generator firm versus the receiving firm(s). Figure 5 below shows the results indicating that overall, ripple generators bear the bulk of the total incident costs.

![Figure 5: Relative share of costs borne by ripple event generators vs. receivers, categorized from "All Generator" to "All Receiver".]

**Important Terms**
- **Ripple Generator:** The initial or primary victim of a ripple incident.
- **Ripple Receiver:** Organizations affected by the generating event.

As a proportion of overall losses, the generators of multi-party incidents bear most of the cost.

Next, we wondered if this changed if instead of looking at the costs for an entire incident across all firms, we instead examined the costs incurred by each firm individually. The answer is shown in Figure 6, which displays the distribution of the per firm costs from single-party incident firms, ripple generator firms and ripple receiver firms.

Once again, per firm, generators tend to incur more losses than receivers, which in turn incur more losses per firm than those from single-party incidents. In fact, the typical (median) cost for generators is 2.6x higher for generator firms ($4.7M versus $1.8M). The difference in extreme losses is even greater, clocking in at 6.5x higher for generator firms ($371.0M versus $57.0M).

![Figure 6: Per-firm losses for single-party incidents, ripple event generators, and receivers, comparing median and 95th percentile costs.]

These figures all make the per-firm costs for single-party events pale in comparison. Falling victim to a cyber incident that ends up being a multi-party ripple event can lead to typical losses 10x greater and extreme losses 14x greater than if the incident involves only your single firm.

However, this happy agreement between the overall and per-firm costs did not quite satisfy us, so we decided to check how the per-firm costs have shifted over time for generators and receivers, shown in Figure 7. Over time, the per-firm costs for ripple receivers have been increasing and now are roughly the same as the per-firm costs for generators. This highlights the increasing dangers faced by firms of being caught up in an incident involving another party.

![Figure 7: Per-firm losses over time for ripple event receivers and generators, showing the convergence of costs.]

---

## What Kinds Of Firms Generate Or Receive Ripple Incidents?

In this section, we’re going to peer inside multi-party ripple incidents to examine some of their internal characteristics. Specifically, we’re going to revisit this note from our original 2019 Ripples report:

> “We considered including an alternative view that would scale the number of ripple events by the number of registered organizations in that sector. It’s possible that Business Support and Finance are on top just because they have the most companies, rather than because they’re more prone to spawning ripple events. If we make that simple adjustment to normalize for firms in each sector, the top five shift to Management, Public, Information, Business Support, and Utilities. That’s different enough that we’ll likely come back to this in future research to do it justice. For now, just keep it in mind.”

The point is that when we describe the prevalence of firms as generators or receivers from different industries or revenue bands, we should be accounting for how common firms are in those industries or revenue bands.

To achieve this, we employed a logistic regression model that counts each ripple generator or receiver firm as a positive case, and all other firms that experience only single-party events as negative cases. We then used this model to estimate the relative likelihood of firms being generators or receivers.

To make this concrete, let’s begin by examining ripple generators and receivers by firm size, as measured by revenue. First consider Figure 8, which shows the proportions of firms comprising ripple generators or receivers. As we can see, the bars are large at the bottom and become progressively smaller as firm size increases.

![Figure 8: Breakdown of ripple event generators and receivers by revenue, showing raw proportions.]

But this may simply be because there are many more small firms than large ones! So let’s turn to Figure 9, which shows the adjusted likelihoods of a firm in a particular revenue band being a ripple generator or receiver. The bars are shaded to highlight relative likelihoods greater than one.

Our adjustment has essentially reversed the picture entirely! While the largest firms comprise the smallest overall proportion of ripple generators and receivers (Figure 8), adjusting for the number of such firms that exist reveals that they are about twice as likely to be involved in multi-party incidents (Figure 9).

![Figure 9: Modeled relative likelihood of firms generating or receiving ripple events by revenue.]

If we apply the same adjustment at the sector level, we get Figure 10. Here, the Financial, Healthcare, and Education sectors receive more than their fair share of ripple effects. On the generator side, the adjusted likelihoods suggest that the Financial, Public, Information, Transportation, and Utilities sectors are more likely to experience incidents that spread across their third-party networks.

![Figure 10: Modeled relative likelihood of firms generating or receiving ripple events by sector.]

---

## How Do Ripples Flow Between Sectors & Revenue Bands?

The previous section considered a static description of the firms that make up ripple incident generators and receivers, independent of how impacts flow between firms. We shift here to a more dynamic view that examines how ripple impacts connect generators and receivers. However, we still want to do so in a relative fashion that accounts for the overall populations of firms.

To do this, consider the hypothetical schematic in Figure 11, which shows two imaginary ripple events. Each box (node) is a firm, and the arrows between them (edges) define generator to receiver relationships. If we expand this diagram to include all firms and ripple events, we end up with a giant graph with thousands of nodes and edges.

![Figure 11: Illustration of a hypothetical graph structure between firms in ripple events.]

We can then use this graph to answer questions about how ripple events flow between groups of firms, such as by counting the number of edges flowing from large firms to small firms. However, since we want to adjust for the relative frequency of firms as we did in prior sections, we instead count edges relative to an equivalent graph but with all the edges randomly permuted between firms.

A concrete example will help ground this discussion, so consider Figure 12, which displays the relative degree of flow between firms of different sizes compared to a random assignment of connections. The heavier the arrow, the more flow there is between firms of those sizes than we’d expect if the connections were random. So, for example, there are 5.3x more generator-receiver pairs flowing from “$10B to $100B” firms up to “More than $100B” firms than we’d expect if those pairs were assigned randomly.

![Figure 12: Ripple incident generator to receiver flow between firms of different revenue sizes.]

An equivalent plot for industry sectors would be visually overwhelming, with arrows flying around between 20 different nodes[^6]. Instead, we’ll isolate a single sector and visualize the rate of ripple activity flowing into and out of that particular sector. We’ll begin in Figure 13 focusing on the Finance sector. The arrows on the left denote ripple activity flowing into the Finance sector, while the arrows on the right denote ripple activity flowing from Finance into other sectors.

![Figure 13: Rates of inflow & outflow for ripple events surrounding the Finance sector.]

Figure 14 focuses on the Retail sector, highlighting that the Professional & Administrative sectors tend to send the most ripple activity in that direction and that multi-party ripples are most likely to flow out of the Retail sector into Administrative, Mining, and Agriculture.

![Figure 14: Rates of inflow & outflow for ripple events surrounding the Retail sector.]

[^6]: Third-party relationships are more complicated than a late season episode of Lost!

---

## Conclusion

As this year’s Ripples Report clearly demonstrates, the fallout from cyber incidents rarely stops at the initial victim. Multi-party ripple events continue to amplify losses across interconnected ecosystems—impacting suppliers, partners, and customers alike. With downstream losses now rivaling those of primary victims, it’s no longer enough to focus solely on your organization’s internal defenses. True resilience demands a deep understanding of your digital supply chain.

Every connection introduces new risk. Larger firms are twice as likely to generate and receive ripple events, and industries such as Finance, Healthcare, and Education remain disproportionately exposed. As these relationships grow in complexity, the need for continuous visibility into the cybersecurity posture of your vendors has never been more urgent. Knowing who you’re connected to—and how well they manage their own risks—is essential to preventing your organization from becoming the next ripple generator or downstream casualty.

The data is clear: ripple events magnify systemic risk, and strong cybersecurity hygiene across your vendor ecosystem is a decisive factor in limiting exposure. Organizations that can leverage insights to identify high-risk relationships early are far better positioned to mitigate the cascading impacts of a breach.