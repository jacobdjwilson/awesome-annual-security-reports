# 2025 DDoS Threat Analysis and Industry Perspectives
## Towards Accountability and Resilience

## Table of Contents
- [Foreword: Resilience, Accountability, and the Changing Nature of Disruption](#foreword-resilience-accountability-and-the-changing-nature-of-disruption)
- [Executive Summary](#executive-summary)
- [Key Findings at a Glance](#key-findings-at-a-glance)
- [Key Observations](#key-observations)
- [DDoS Attack Source Distribution: APAC](#ddos-attack-source-distribution-apac)
- [DDoS Attack Source Distribution: Middle East Africa](#ddos-attack-source-distribution-middle-east-africa)
- [DDoS Attack Source Distribution: Europe](#ddos-attack-source-distribution-europe)
- [DDoS Attack Source Distribution: Americas](#ddos-attack-source-distribution-americas)
- [2020-2025 Trend: Growing Scale and Hidden Complexity](#2020-2025-trend-growing-scale-and-hidden-complexity)
- [Regional Analysis: Balkanisation and Local Resilience](#regional-analysis-balkanisation-and-local-resilience)
- [Attack Vectors and Hidden Threats](#attack-vectors-and-hidden-threats)
- [Beyond Record Sizes: Measuring User Impact](#beyond-record-sizes-measuring-user-impact)
- [Extended Analysis: Resilience, Accountability & Market Dynamics](#extended-analysis-resilience-accountability--market-dynamics)
- [Outlook for 2026](#outlook-for-2026)
- [Recommendations](#recommendations)
- [Conclusion](#conclusion)
- [Data Sources and Methodology](#data-sources-and-methodology)

---

## Foreword: Resilience, Accountability, and the Changing Nature of Disruption

For years, discussion around distributed denial-of-service (DDoS) attacks centred on a single question: how large can an attack become?

As bandwidth expanded and botnets scaled, each year brought new records. Terabit-level floods that once seemed extraordinary are now increasingly routine. The industry responded predictably - building larger scrubbing centres, adding automation, and focusing on raw capacity.

Yet over the past year, something shifted.

High-profile disruptions across cloud platforms, communications networks, transport systems, and consumer services revealed a deeper issue. In many cases, outages were not caused by insufficient capacity, but by architectural complexity, cross-border dependencies, and opaque operational layers. The question moved from “How big was the attack?” to “Why did this fail, and who is accountable?”

DDoS is no longer just a technical event measured in packets and bits. Its impact is felt when payments stall, flights are delayed, games disconnect, or public services become inaccessible. Even partial degradation can erode trust quickly.

At the same time, the broader environment is changing. Regulatory scrutiny has intensified. Data sovereignty requirements are expanding. The once borderless internet is fragmenting into regions with distinct rules, expectations, and risk profiles. Architectural decisions that prioritised centralisation and convenience are now being reassessed through the lens of resilience and control.

Capacity still matters. But it is no longer sufficient.

Resilience today depends on where mitigation occurs, how traffic is routed, how quickly incidents are detected and communicated, and how clearly responsibility is defined when systems fail.

This report presents data from real-world mitigation activity in 2025, not simply to catalogue record-breaking attacks, but to examine what those events reveal about the structure of modern digital infrastructure. It explores evolving attack patterns, regional dynamics, and the growing importance of accountability in maintaining service continuity.

Disruption is inevitable. The defining question is no longer scale, but how systems are designed to withstand it - and how institutions respond when they do not.

---

## Executive Summary

In 2025, Nexusguard mitigated more than **686,000 DDoS attacks**, with peak activity reaching **1.40 Tbps**, **167 million packets per second**, and **1.04 million HTTP/2 requests per second**.

These figures reflect continued expansion in both attack capability and defensive capacity.

The data confirms that disruption is no longer defined by size alone.

The evidence suggests that while capacity remains essential, resilience is increasingly determined by architectural design, operational responsiveness, and clarity of accountability.

Attackers are increasingly favouring distributed and structurally disruptive techniques. In 2025, the most significant carpet-bombing event simultaneously targeted 177 `/24` prefixes, overwhelming aggregation points without generating a headline-level peak. Such attacks exploit architectural concentration rather than bandwidth ceilings.

Multi-vector campaigns have become routine. Network floods are frequently combined with application-layer abuse and protocol exploitation, requiring correlation across layers and timely operational judgement when automated systems reach their limits.

Regional dynamics also shape outcomes. Attack volumes and peak activity varied significantly across Asia–Pacific, EMEA, and Latin America, reflecting differences in infrastructure topology, customer concentration, and regulatory context. These variations underscore the importance of regionally resilient architectures.

Perhaps most notably, the year’s activity reveals a widening gap between peak volume and user impact. Several disruptive incidents stemmed not from record-breaking bandwidth, but from routing constraints, latency amplification, or mitigation side effects. For users, degraded performance is often indistinguishable from outage.

---

## Key Findings at a Glance

- **Scale is routine. Structural weakness is not.** Large volumetric attacks are increasingly common; distributed techniques that exploit architectural blind spots are more disruptive.
- **Carpet-bombing is resurging.** The largest observed event targeted 177 prefixes simultaneously, demonstrating how modest flows can create systemic impact.
- **Multi-vector is the default.** Cross-layer coordination and operator intervention are now central to effective mitigation.
- **Region matters.** Attack patterns and impact vary significantly by geography, reinforcing the need for localised resilience strategies.
- **User impact is decoupled from peak size.** Latency, routing constraints, and mitigation side effects often determine real-world disruption.

---

## Key Observations

| Increase | Decrease | | | |
| --- | --- | --- | --- | --- |
| Total Attacks | | Attack Sizes | | |
| vs. 2024 | +97.3% | 1.4 Tbps | VS. 2024 | +45.7% |
| | | Peak Volumetric Attack | | |
| 1.04 Million requests per second | VS. 2024 | +67.6% | | |
| Peak Application Layer Attack | | | | |
| **Top 3 Attack Types** | DNS Reflection Attack | IP Fragmentation Attack | TCP ACK Attack | |
| vs. 2024 | 427.4% | 55.3% | 603% | |
| **Attack Category** | Volumetric (Direct Flood) | Volumetric (Amplification) | Application Attack | |
| vs. 2024 | 53.55% | -68.1% | -32.2% | |

---

## DDoS Attack Source Distribution: APAC

![APAC Attack Distribution Chart showing regional breakdown percentages]

| Country Name | Aggregate Value |
| --- | --- |
| China | 14.3% |
| Hong Kong | 11.5% |
| India | 9.6% |
| Japan | 8.9% |
| Vietnam | 7.2% |
| Philippines | 6.0% |
| Indonesia | 5.5% |
| South Korea | 4.7% |
| Malaysia | 4.6% |
| Thailand | 2.6% |
| Others | 25.1% |

---

## DDoS Attack Source Distribution: Middle East Africa

![Middle East Africa Attack Distribution Chart showing regional breakdown percentages]

| Country Name | Aggregate Value |
| --- | --- |
| United Arab Emirates | 18.0% |
| Oman | 14.6% |
| South Africa | 10.2% |
| Turkey | 8.9% |
| Saudi Arabia | 7.5% |
| Iraq | 4.6% |
| Iran | 4.3% |
| Seychelles | 3.5% |
| Israel | 3.2% |
| Kenya | 2.3% |
| Others | 24.9% |

---

## DDoS Attack Source Distribution: Europe

![Europe Attack Distribution Chart showing regional breakdown percentages]

| Country Name | Aggregate Value |
| --- | --- |
| Germany | 13.4% |
| Netherlands | 12.3% |
| France | 11.4% |
| United Kingdom | 11.1% |
| Russia | 7.8% |
| Italy | 5.5% |
| Ukraine | 4.8% |
| Spain | 3.8% |
| Poland | 3.5% |
| Ireland | 2.9% |
| Others | 23.5% |

---

## DDoS Attack Source Distribution: Americas

![Americas Attack Distribution Chart showing regional breakdown percentages]

| Country Name | Aggregate Value |
| --- | --- |
| United States | 43.9% |
| Brazil | 17.8% |
| Canada | 11.3% |
| Mexico | 5.7% |
| Argentina | 4.5% |
| Colombia | 4.3% |
| Chile | 2.7% |
| Venezuela | 1.8% |
| Peru | 1.69% |
| Ecuador | 0.89% |
| Paraguay | 0.55% |
| Puerto Rico | 0.12% |
| U.S. Virgin Island | 0.07% |
| Guam | 0.03% |
| N. Mariana Island | 0.01% |
| American Samoa | 0.00% |
| U.S. Minor Outly | 0.00% |
| Jamaica | 0.00% |
| Cayman Islands | 0.00% |
| Others | 3.6% |

---

## 2020-2025 Trend: Growing Scale and Hidden Complexity

| Year | Gbps | Mpps | KRPS | Carpet Bombing (/24 Count) |
| --- | --- | --- | --- | --- |
| 2020 | 795.2 | 58.3 | 104 | 1 |
| 2021 | 1155.4 | 100.4 | 187.4 | 61 |
| 2022 | 904.8 | 97.4 | 225.2 | 77 |
| 2023 | 1301.1 | 172.5 | 496.1 | 79 |
| 2024 | 962.2 | 118.6 | 620.5 | 41 |
| 2025 | 1402.2 | 167.1 | 1040 | 177 |

_Figure 1 - 6 years DDoS attack trend_

From 2020 to 2025 the scale of observed DDoS attacks increased steadily. Peak bandwidth climbed from roughly 795 Gbps to 1.40 Tbps, packet rates from 58 Mpps to 167 Mpps, and web‑layer request rates from about 104,000 requests per second to over 1 million. The largest carpet‑bombing attack targeted 177 `/24` prefixes simultaneously, compared with just one prefix in 2020. These trends illustrate the arms race between attackers who leverage ever‑larger botnets and defenders who build bigger pipes and scrubbing centres. Attackers also broadened their toolsets: stealthy SYN‑ACK floods and distributed UDP fragments are now used alongside classic amplification techniques.

But bigger attacks are only part of the story. As backbone capacity grows and endpoints get faster, it is natural that volumetric attacks become more voluminous. A few years ago a 300 Gbps flood could take a major ISP offline; today many networks treat that as background noise. The more meaningful question is whether users stay online when attacks occur. A terabit‑class flood routed through the wrong mitigation centre can still break applications if latency spikes or if legitimate traffic is inadvertently blocked. When traffic traverses multiple jurisdictions, regulatory constraints can delay or prevent rerouting, leaving customers stranded. Measuring success therefore requires looking beyond the record numbers to understand the user experience and the broader network impact.

![Peak bandwidth 2020–2025 graph]
_Figure 2 - Peak bandwidth 2020–2025_

![Peak packet rate 2020–2025 graph]
_Figure 3 - Peak packet rate 2020–2025_

![Peak RPS 2020–2025 graph]
_Figure 4 - Peak RPS 2020–2025_

![Carpet bombing prefixes graph]
_Figure 5 - Carpet bombing prefixes_

### Carpet‑Bombing (`/24`) Events by Year

The figure above on prefixes illustrates an often‑overlooked menace. Carpet bombing (also called “bit‑and‑piece” attacks) involves sending small floods to hundreds of IP prefixes simultaneously. Individually each stream looks harmless, but when they converge downstream they saturate backbone routers and aggregation points. This technique has existed for years yet remains under‑reported because it rarely produces record‑breaking single flows. Instead, its success lies in overwhelming the control plane and causing collateral damage across many networks.

Attackers increasingly blend TCP ACK, RST and SYN‑ACK floods with UDP reflection to evade signature‑based detection. The 177‑prefix event in 2025 underscores how broad and stealthy such campaigns have become.

---

## Regional Analysis: Balkanisation and Local Resilience

![Attack distribution by continent chart]
_Figure 6 - Attack distribution by continent_

In 2025 the majority of attacks mitigated by Nexusguard targeted Asia–Pacific (excluding China), which accounted for 35.8% of events. EMEA represented 26.6%, Latin America 23.6% and the Americas 14%. The Asia–Pacific and Japan (APJ) region had by far the largest number of unique victim IP addresses (49,175), reflecting both a large customer base and increasing regional threats.

The uneven distribution of attacks also highlights a broader geopolitical shift: the internet is fragmenting into regional networks with their own rules, infrastructure and trust models. Data‑sovereignty laws, sanctions and geopolitical tensions have prompted many countries to localise cloud services and require that critical traffic remains within regional borders. This “balkanisation” means that attacks and defences are now shaped as much by politics and regulation as by technology. It also presents opportunities for regional players. Local providers can offer better alignment with national regulations, faster support, and deeper understanding of regional threats than global hyperscalers. As a result, governments and enterprises are increasingly selecting local partners for critical security functions.

### Monthly Peak Bandwidth by Region

Regional peaks varied throughout the year. APJ experienced the overall highest peak in October, while the Americas saw a major surge in April. Latin America’s peaks were elevated early in the year before stabilising, and EMEA’s peaks remained moderate but consistent. These differences reflect regional threat actors, economic cycles and the distribution of large customers. They also underscore the importance of local‑first design: high peaks in one region should not automatically trigger mitigation in distant regions, as that can unnecessarily degrade performance or run afoul of local laws.

![Monthly peak bandwidth by region chart]
_Figure 7 - Monthly peak bandwidth by region (2025)_

### High‑Bandwidth Attacks and Local Resilience

Although Nexusguard recorded 376 attacks exceeding 50 Gbps and 76 attacks over 100 Gbps in 2025, the overwhelming majority were smaller than 50 Gbps. By contrast, Cloudflare’s Q3 2024 report documented more than 200 attacks above 3 Tbps, showing that global scale depends heavily on customer mix. More importantly, record‑sized attacks no longer have the shock factor they once did. Many networks routinely handle volumes that would have been catastrophic a few years ago. The challenge now is to build regional scrubbing capacity and failover paths so that mitigation does not introduce cross‑border latency or violate data‑residency requirements. Local resilience includes deploying on‑premises filters, reserving headroom in regional links and practising failovers that keep traffic within the same jurisdiction.

### Attack Volumes and Monthly Patterns

Across 2025 Nexusguard processed 686,869 DDoS mitigation events. The number of events peaked in September, surpassing 101,000 attacks, and steadily declined towards December. HTTPS floods contributed 103,163 events—about 15% of all attacks—and showed spikes in June and September. The monthly cadence suggests that attackers concentrate campaigns around certain geopolitical events, shopping seasons or vulnerability disclosures. It also exposes an uncomfortable truth: many outages are still caused by “dumb” volumetric floods, not sophisticated zero‑day exploits. Attackers simply use cheap IoT botnets to saturate uplinks, and if the provider’s network is not over‑provisioned the attack succeeds. Automated defence systems can classify these floods instantly, but they cannot conjure spare capacity or reroute traffic through congested public peering points. Because of this, defenders must invest in architecture and capacity planning as much as in detection algorithms.

![Monthly HTTP(S) attack events graph]
_Figure 8 - Monthly HTTP(S) attack events_

---

## Attack Vectors and Hidden Threats

Carpet bombing—or bit‑and‑piece flooding—remains one of the least publicised yet most effective DDoS techniques. Instead of focusing traffic on a single victim IP, attackers spread small flows across dozens or hundreds of prefixes. Each individual flow appears benign to scrubbing systems, but collectively they saturate aggregation routers and exhaust the control plane. Over the past five years, the number of prefixes targeted in the worst carpet‑bombing attack grew from 1 to 177. Packet rates per prefix exploded as attackers blended TCP ACK, RST and SYN‑ACK floods with UDP reflection to evade signature‑based detection. Carpet bombing campaigns often go unnoticed in public reporting because they do not produce headline‑worthy peaks; nonetheless they have brought down entire regions when routers crashed under the aggregate load.

### Multi‑Vector Attacks and Protocol Exploitation

Attackers are increasingly combining multiple vectors in a single campaign. In 2025 more than 862,000 Nexusguard incidents involved a single vector, 233,000 used two vectors, and 53,000 utilised three or more. Campaigns often mixed carpet bombing, TCP amplification, DNS floods, HTTP/2 request floods and IPv6 exploitation. Netscout’s threat report notes the growing use of geo‑spoofing and ISP masking to bypass geo‑block filters. F5 Labs observed botnets using reinforcement learning to adapt mid‑attack. Our own telemetry recorded a massive HTTP/2 flood on 23 December 2025 that peaked at 1.04 M requests per second and DNS Applications layer floods reaching 88 Gbps. These incidents demonstrate that attackers are not content with brute force alone; they tailor attacks to exploit protocol weaknesses and overwhelm specific layers of the stack.

![Network attack duration distribution graph]
_Figure 9 - Network attack duration distribution_

![Application layer attack duration distribution graph]
_Figure 10 - Application layer attack duration distribution_

---

## Beyond Record Sizes: Measuring User Impact

The DDoS narrative often focuses on record‑breaking volumes, but the more important question is what happened to the people and services behind those graphs. Did websites stay responsive? Were there login delays? Did DNS time out? Attack size is becoming less relevant because infrastructure is getting bigger; a 300 Gbps attack is now considered “background noise” for many networks. The story beneath the graphs involves routing policies, regional versus global traffic, and whether mitigation introduced collateral damage. Focusing only on packet volumes risks conflating volume with value and missing the essential point: were users protected end to end?

To illustrate why impact matters more than peak metrics, we summarise several events from recent years that had tangible consequences despite (or because of) their size:

### December 2025: Aisuru-Kimwolf campaign
Security telemetry revealed an unprecedented DDoS campaign peaking at 31.4 Tbps, launched by the Aisuru-Kimwolf botnet against Cloudflare’s infrastructure and its customers. While the attack was mitigated before widespread outages occurred, its scale exposed a critical reality: attacks at this magnitude place stress not just on a single service, but on the shared internet infrastructure that millions of users depend on.

For everyday users, the risk in such events is systemic rather than immediate. Even when websites remain online, congestion can lead to slower page loads, degraded streaming quality, intermittent service failures, and increased latency across unrelated platforms. These attacks demonstrate how a single large-scale campaign can quietly degrade user experience across regions, without a clear “outage” to point to.

### October 2025: Steam and Riot Games disruptions
In October 2025, major gaming platforms experienced widespread disruptions. Multiplayer sessions dropped unexpectedly, matchmaking failed, and online services became intermittently unreachable. Although no single company formally confirmed the root cause, cybersecurity analysts widely suspected a DDoS campaign targeting shared infrastructure.

For users, this translated into broken leisure time: games freezing mid-match, competitive rankings affected by forced disconnects, and paid services becoming temporarily unusable. These incidents highlight that DDoS attacks no longer target only enterprises or governments. Entertainment platforms, social services, and consumer applications are increasingly caught in the blast radius, affecting millions of users who may not even realise they are experiencing the effects of a cyberattack.

### January 2025: MegaFon carpet-bombing
In early 2025, a carpet-bombing style DDoS campaign targeted Russian telecom operator MegaFon and its subsidiaries. Rather than overwhelming a single endpoint, the attack spread traffic across a wide range of IP prefixes, degrading service across large geographic areas.

For everyday users, the impact was immediate and frustrating: mobile calls failing, mobile data becoming unreliable, slow or unreachable websites, and disrupted messaging services. This type of attack illustrates how DDoS is no longer about knocking a single website offline. It is about reducing the reliability of basic connectivity, turning everyday digital services into something unpredictable.

### January 2, 2025: NTT Docomo outage
Japan’s largest mobile operator, NTT Docomo, suffered a prolonged DDoS-induced outage that lasted nearly eleven hours. During this period, popular consumer services such as the “goo” portal, Lemino video streaming, and the d-pay payment service were severely impacted.

For nearly 90 million subscribers, this meant failed mobile payments, inaccessible online content, and unreliable digital services throughout the day. For users trying to commute, shop, or pay for services, the attack became a real-world inconvenience with financial and logistical consequences — not a technical anomaly.

### December 26, 2024: Japan Airlines disruption
A DDoS attack against Japan Airlines disrupted ticketing systems and internal operations, delaying more than 70 flights and cancelling several others. Ticket sales were temporarily halted, and customer service systems struggled to cope.

For passengers, this translated into missed connections, long queues, confusion at airports, and disrupted travel plans during a peak holiday period. Even though the attack itself was relatively short-lived, its downstream effects rippled through tightly coupled logistical systems, demonstrating how digital disruptions quickly become physical ones.

### May 2024: Internet Archive sustained attack
In May 2024, the Internet Archive came under a sustained, multi-day DDoS attack that left the Wayback Machine and digital library services intermittently unavailable.

For journalists, researchers, students, and everyday users, this meant losing access to historical web records, academic materials, and cultural archives relied upon for work and study. Unlike commercial outages, the impact here was not financial loss, but loss of access to shared digital memory, underscoring how DDoS attacks can affect public knowledge and information continuity.

### January 17, 2024: Belgian rail outage
Belgium’s national rail operator was forced to shut down its website and mobile application following a DDoS attack. While trains continued to run, passengers were unable to check schedules, purchase tickets, or receive real-time updates.

For commuters and travellers, this created uncertainty and inconvenience: missed connections, inability to plan journeys, and increased reliance on physical counters and announcements. The incident highlights how DDoS attacks can disrupt daily life even when core infrastructure remains operational.

### January 2023: Killnet protest attacks on Germany
Following geopolitical tensions, pro-Russian hacktivist groups launched DDoS attacks against German government agencies, banks, and airport websites. While many services were restored quickly, the attacks temporarily blocked access to public information portals.

For citizens, the immediate impact was the inability to access government services, financial portals, and travel information. More broadly, these attacks demonstrated how DDoS has become a tool of digital protest, used to signal political intent by disrupting everyday civic interactions rather than causing lasting technical damage.

Across these incidents, the pattern is clear:

Modern DDoS attacks increasingly target availability, reliability, and trust, rather than outright destruction. Even when services remain partially online, users experience slowdowns, failures, uncertainty, and frustration.

From streaming and payments to travel, communication, and public services, DDoS attacks are no longer abstract technical events. They are quality-of-life disruptions, felt by ordinary users long before they make headlines.

### Modern DDoS Attacks Degrade Service Availability and Reliability
Services may remain reachable but experience latency, packet loss, and increased error rates.

```
[Client Internet] ---> [Edge Router] ---> [Load Balancer] ---> [Application Cluster] ---> [Backend Database]
                         |                    |                     |
                  (Increased Latency)   (Service Errors)     (User Impact Degradation)
```

---

## Extended Analysis: Resilience, Accountability & Market Dynamics

### Hyperscaler dependence vs local‑first resilience
Modern businesses rely heavily on hyperscale cloud providers and global content-delivery networks. This reliance has delivered unprecedented scalability and speed of deployment, but it has also introduced a structural trade-off: when a centralised provider suffers an outage, the resulting blast radius can span entire regions or even multiple continents.

In 2025, several high-profile incidents demonstrated this dynamic, where a single cloud region or CDN node failure led to widespread service disruption. These events reinforced a critical lesson for operators and enterprises alike: resilience cannot be inherited from a provider; it must be deliberately designed.

Local-first resilience addresses this challenge by distributing mitigation and control closer to where traffic originates and terminates. This includes building regional scrubbing capacity, deploying redundant instances across multiple clouds, reserving headroom on regional links, and establishing failover procedures that keep critical traffic within national or jurisdictional boundaries. Importantly, this approach does not reject the cloud. Instead, it treats cloud services as one layer within a broader, layered defence strategy, where local control over routing, filtering and failover remains essential.

The table below summarises the structural differences between hyperscaler-centric architectures and local-first or hybrid designs.

| Dimension | Hyperscaler‑centric | Local‑first / hybrid |
| --- | --- | --- |
| Primary mitigation location | Centralised global POPs | Regional / national scrubbing nodes |
| Failure mode | Single region outage cascades globally | Failures contained to local region |
| Traffic during attack paths | Backhauled across borders | Kept within local or national paths |
| Latency impact | High and unpredictable during incidents | Low and bounded |
| Regulatory exposure | High (cross‑border routing) | Lower (data locality maintained) |

_Figure 11 - Key differences between hyperscalers and local-first/hybrid architectures_

These differences become most visible during incidents. Centralised architectures tend to propagate failures across wide geographies, while local-first approaches contain disruption and preserve service quality for unaffected regions.

This contrast is further illustrated in the conceptual risk comparison shown in Figure 12.

![Blast Radius & Resilience: Hyperscaler vs Local-first chart]
_Figure 12: Conceptual risk comparison of hyperscaler‑centric versus local‑first architectures (higher values indicate greater risk/exposure)._

Rather than optimising solely for convenience or scale, local-first resilience reduces blast radius, limits regulatory exposure and improves customer visibility. While it may introduce additional architectural complexity, it provides greater predictability under stress and better protection of user experience.

### Accountability, complexity and trust
As outages became more visible and impactful, the industry’s focus shifted. In 2025, the central question was no longer whether a provider could withstand a particular attack size, but who was accountable when systems failed and why the architecture proved fragile.

Outages rarely stem from a single cause. They are typically the result of layered dependencies accumulated over time, spanning applications, platforms, networks and operational processes. When failures occur, boards of directors, regulators and customers increasingly demand clear answers: what happened, which systems were affected, how users were impacted, and what changes will prevent recurrence.

Trust, in this context, is built through clarity rather than claims. Providers that can articulate incidents coherently and transparently are better positioned to maintain confidence, even when failures occur.

Figure 13 visualises how multiple architectural and operational layers contribute to outage complexity.

![Outage Responsibility Stack chart]
_Figure 13: Outage responsibility stack showing how failures can cascade across layers._

This growing emphasis on accountability is also reflected in how performance is evaluated. The industry has moved away from a narrow focus on capacity metrics toward measures that reflect operational responsiveness and transparency.

| Then (Capacity‑centric) | Now (Accountability‑centric) |
| --- | --- |
| Maximum Tbps mitigated | Time to detection |
| Number of scrubbing nodes | Time to customer notification |
| AI / automation claims | Root‑cause clarity |
| SLA uptime | Incident transparency |
| Marketing benchmarks | Post‑incident confidence |

_Figure 14: Shift from capacity-centric metrics to accountability-centric metrics_

Capacity remains necessary, but it is no longer sufficient. Detection speed, communication quality and post-incident confidence now play a central role in how providers are assessed by regulators, customers and partners.

![Impact of Fragmentation Drivers on Architecture Choice chart]
_Figure 15 - Impact of Fragmentation Drivers on Architecture Choice_

Global-first, hyperscaler-centric models emerged in an era of relatively uniform regulation and unrestricted cross-border data flows. As fragmentation increases, these models face growing stress. Centralised control can amplify failure impact, complicate compliance across jurisdictions and reduce operators’ ability to manage traffic and mitigation decisions locally.

Regional and local-first models respond to these pressures by design. By keeping traffic, mitigation and operational decision-making within defined jurisdictions, they align more naturally with data-sovereignty mandates and latency-sensitive services. This approach simplifies compliance, limits failure domains and restores operational certainty, particularly for CSPs and public-sector organisations.

Hybrid models bridge these approaches. They preserve access to global scale while re-establishing local control where regulatory, operational or performance considerations demand it. For many operators, this reflects a pragmatic reality: cloud services remain valuable, but they can no longer serve as the sole foundation for resilience in a fragmented internet.

Buyer behaviour reflects this change. Figure 16 shows how purchasing priorities have evolved in recent years.

![Shift in Buyer Motivations chart]
_Figure 16 - Shift in Buyer Motivations_

Where cost efficiency and global reach once dominated decision-making, compliance, jurisdictional trust, predictable latency and proximity of support have decisive factors. This shift helps explain why smaller, regionally focused providers are gaining relevance. Their strength lies not in competing on sheer scale, but in their ability to adapt quickly to local conditions, provide direct operational support and tailor services to regional risk profiles.

In this environment, competitive advantage is increasingly defined by balance. Success belongs to organisations that can combine global capability with local nuance, aligning their architectures with the fragmented, regulated and latency-sensitive nature of today’s internet.

---

## Outlook for 2026

Combining our statistics with industry reports yields several expectations for 2026:

- **Hyperscaler dependence will be tempered by local‑first design.** Organisations will design for regional independence, multi‑cloud deployments and explicit control over routing and failover. Scrubbing centres will be built closer to end users, and cross‑border dependencies will be reduced.
- **Hyper‑volumetric attacks will grow but context will matter more.** Botnets leveraging IoT devices and cloud servers will produce ever‑larger floods. However, record peaks will matter less than service continuity. Providers will increasingly be judged on their ability to maintain performance and user experience during attacks. This will require investment in regional capacity, surge planning and traffic engineering.
- **Stealth and multi‑vector attacks will proliferate.** Carpet bombing will remain a favourite technique, joined by novel protocol abuses. Attackers will coordinate multiple vectors across layers, requiring defenders to integrate on‑premises filtering, cloud scrubbing and intelligent routing.
- **Accountability and regulation will drive procurement.** Providers will be selected based on transparency, visibility and alignment with local laws. Organisations will demand clear incident reports, root cause analyses and commitments to improvements.
- **AI will augment, not replace, human judgement.** While machine learning reduces noise and spots anomalies faster, over‑reliance on fully autonomous mitigation can delay response. Defenders will combine AI detection with clear escalation paths, manual overrides and architectural safeguards.
- **Regional providers will gain market share.** Digital fragmentation will favour local players who can navigate regulatory environments and build trust. Partnerships between global and regional providers will become common as customers seek both scale and localisation.

---

## Recommendations

- **Build systems for transparency and accountability.** Ensure you can trace attacks through every layer and explain what happened. Prepare clear communications for stakeholders and regulators.
- **Design local resilience.** Avoid over‑reliance on a single hyperscaler. Deploy regional scrubbing, keep critical traffic within appropriate jurisdictions, and practise failovers.
- **Prepare for stealthy, multi‑vector attacks.** Implement detection that can identify distributed low‑rate floods across many prefixes. Combine on‑premises and cloud‑based defences, and integrate threat intelligence.
- **Use AI judiciously and retain human oversight.** Treat machine learning as an assistant that highlights anomalies and reduces noise, but ensure experienced operators can intervene when necessary.
- **Measure what matters.** Track latency, packet loss, session success and other user‑centric metrics during attacks. Avoid focusing solely on peak volumes.
- **Embrace regional partnerships.** Work with local providers to meet compliance requirements and leverage regional expertise. Build layered architectures that blend global reach with local control.
- **Share intelligence and collaborate.** Participate in industry information‑sharing platforms and coordinate responses with peers and regulators. Collective awareness strengthens the ecosystem.

---

## Conclusion

In 2025 the DDoS landscape demonstrated that size alone no longer defines severity. Attackers leveraged larger botnets and stealthier techniques, while defenders built bigger pipes and smarter filters. Yet the true challenges lay in the fragility of architectures, the limitations of hyperscaler dependence, the emergence of regional regulations and the need for accountability. The internet is fragmenting into multiple, sovereign internets, and success will hinge on the ability to design for local resilience while maintaining global reach. Looking forward, organisations that prioritise user experience, transparency and balanced architectures will weather the storm, while those who chase only record numbers may find themselves unprepared when the next flood hits.

---

## Data Sources and Methodology

The statistics presented here derive from Nexusguard’s global scrubbing network. Each mitigation event is counted once, regardless of duration or size. Peak values capture the single largest observed bandwidth, packet rate and request rate during the year. The carpet‑bombing metric records the number of `/24` prefixes targeted simultaneously in the most extreme carpet‑bombing attack; it does not represent the number of such attacks. Charts were generated from the supplied Excel workbook, and external figures from Cloudflare, Akamai, Radware, Netscout, F5 Labs, Imperva and FS‑ISAC provide additional context. Where industry data is quoted, we cite the original sources.

---

Established in 2008 and headquartered in Singapore, Nexusguard is a global leader in DDoS protection. Using proprietary Bastions technology and a global network of over 50 scrubbing centers, we provide comprehensive protection for networks, web applications, and DNS against malicious attacks. Trusted by 100+ CSPs, including top global providers, and protecting 50,000+ ASNs, we deliver scalable solutions ensuring service availability, operational continuity, and peace of mind. Nexusguard also enables CSPs to offer DDoS-protection-as-a-service, unlocking new revenue opportunities. 

[www.nexusguard.com](https://www.nexusguard.com) for more information.


<!-- CONVERSION_METADATA: {"source": "https://github.com/jacobdjwilson/awesome-annual-security-reports", "date": "2026-07-26", "model": "gemini-3.5-flash-lite"} -->
