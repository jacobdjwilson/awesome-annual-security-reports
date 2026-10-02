# DDoS Threat Intelligence Report
Organization: Netscout  
Report Title: Threat-Report  
Year: 2026  

## Table of Contents
- [Introduction](#introduction)
- [Executive Summary](#executive-summary)
- [Key Findings](#key-findings)
- [Global and Regional Attacks](#global-and-regional-attacks)
- [A View from the Arbor Cloud SOC](#a-view-from-the-arbor-cloud-soc)
- [The State of DDoS: 1H 2026](#the-state-of-ddos-1h-2026)
- [Fully Managed: What DDoS-for-Hire Sells Now](#fully-managed-what-ddos-for-hire-sells-now)
- [Residential Proxy Networks and DDoS](#residential-proxy-networks-and-ddos)
- [Conclusion](#conclusion)
- [Methodology](#methodology)

---

## INTRODUCTION

The first half of 2026 did not introduce a new class of distributed denial-of-service (DDoS) attack. Familiar attacks grew in scale and became easier to buy. This report draws on NETSCOUT’s ATLAS global threat intelligence, original ASERT research on DDoS-for-hire platforms and residential proxy networks, and operational observations from the Arbor Cloud Security Operations Center (SOC). Together, these perspectives show how attacks are changing and what those changes mean for providers and enterprises.

### VISIBILITY AT A GLOBAL SCALE
- **9,146,021**: DDoS attacks observed
- **209**: Countries and territories impacted
- **800+ TBPS**: Global peak traffic across protected network edges
- **413**: Industry verticals
- **12,031**: Autonomous system numbers (ASNs)
- **TWO-THIRDS**: Of routed IPv4 space under ATLAS visibility.

---

## EXECUTIVE SUMMARY

NETSCOUT ATLAS recorded more than 9.1 million DDoS attacks in the first half of 2026, but the larger story is a shift in how attacks are launched and sourced. High-impact attacks became more frequent, direct-path methods accounted for roughly two-thirds of observed attacks, and carpet-bombing continued to gain share.

DDoS-for-hire services made attacks easier to launch, while residential proxy networks supplied source addresses that looked like ordinary subscribers. Together, these developments put more pressure on defenses to distinguish malicious traffic from legitimate demand.

That distinction matters because attacks can disrupt services without saturating a link. Connection state and application capacity can fail first, while traffic spread across many destinations can evade per-host detection thresholds. Preserving service therefore requires more than bandwidth or coarse filtering. Providers need greater dedicated scrubbing capacity at their network edges, with selective mitigation and headroom for concurrent attacks. Enterprises need on-premises protection close to the services they operate themselves. For both, cloud-delivered mitigation remains a necessary complement for distributed attacks, overflow, and events that exceed local capacity.

---

## KEY FINDINGS

### Global Scale
**Attack volume and high-impact growth**
1. NETSCOUT ATLAS recorded more than 9.1 million DDoS attacks across 209 countries and territories in 1H 2026. Attacks clearing 1Tbps or 1Gpps increased 1,286 percent year over year.

**IPv6 attacks reached a new threshold**
2. ATLAS observed its first IPv6 attack exceeding 1Tbps. Active mitigation of IPv6 attacks rose more than 300 percent year over year, while IPv6's share of observed attacks held roughly flat.

### Carrier Mitigation Capacity
**Direct-path and carpet-bombing gained share**
3. Direct-path methods accounted for 64.40 percent of observed attacks in 1H 2026 and gained share for a third consecutive half-year. Separately, carpet-bombing rose from 3.97 percent of attacks in 1H 2025 to 4.54 percent in 1H 2026.

### DDoS for Hire and Attack Economics
**The shortest attacks gained share**
4. Attacks lasting one minute or less increased from 1.6 percent of observed attacks in 2H 2023 to 3.1 percent in 1H 2026.

### Residential Proxy Supply
**Residential proxy sources participated in DDoS attacks**
5. ASERT paired residential proxy network tracking with DDoS telemetry to identify proxy sources participating in attacks.

---

## GLOBAL AND REGIONAL ATTACKS (1H 2026)

### GLOBAL ATTACK COUNT
**9,146,021**

- **LATAM ATTACK COUNT**: 1,125,099
- **APAC ATTACK COUNT**: 1,951,248
- **NAMER ATTACK COUNT**: 1,469,259
- **EMEA ATTACK COUNT**: 4,167,164

---

## A VIEW FROM THE ARBOR CLOUD SOC

While the findings in this report are drawn from NETSCOUT ATLAS global threat intelligence and original ASERT research, analysts in the NETSCOUT Arbor Cloud SOC reached many of the same conclusions in 1H 2026 from a separate vantage point. Working across Arbor Cloud’s global mitigation infrastructure, which runs the full Arbor DDoS attack protection portfolio, they observed no fundamentally new attack techniques but a continued maturation of the DDoS ecosystem and a restoration of large-scale attack capability following a period of law enforcement disruption. Actors have regained both the infrastructure and the operational capacity to sustain higher attack volumes while still executing large, high-impact campaigns when they choose to. Observations from the SOC appear alongside the relevant findings throughout this report.

---

## THE STATE OF DDoS: 1H 2026

Attack volume rose again in 1H 2026, increasing by nearly a quarter against 1H 2025 and extending a three-half trend. The rise accelerated across the period, making higher attack frequency part of the operating baseline.

Impact also moved upward. Attacks clearing 1Tbps or 1Gpps increased 1,286 percent year over year, moving high-capacity events into routine planning for providers that must preserve customer service during overlapping incidents and routine peaks.

At the same time, the attack mix shifted toward classes that coarse network controls mitigate less effectively. Direct-path methods accounted for roughly two-thirds of attacks in 1H 2026 and gained share for a third consecutive half-year. On the targeting side, carpet-bombing continued to grow from a smaller base.

Flowspec and blackhole routing remain useful, but their granularity and scale limits can produce significant over-blocking. As direct-path and carpet-bombing attacks take more share, more traffic has to be inspected and mitigated selectively so that attack traffic is suppressed while legitimate traffic keeps flowing.

### ATTACK VOLUME, BY HALF
ATLAS observed nearly one-quarter more DDoS attacks in 1H 2026 than in 1H 2025, with the increase accelerating across the three intervals shown in Figure 1.

- **1H 2025**: +2.71%
- **2H 2025**: +18.33%
- **1H 2026**: (Representing accelerated volume growth)

![Figure 1: Daily attack counts, Jan 2025 to Jun 2026.]

> **FROM THE ARBOR CLOUD SOC**  
> We see the same pattern. In one case a 3.5 Tbps UDP flood targeted a hosting provider. Attacks at that scale are almost always short, typically no more than one to two minutes, and this one ran two minutes. All of the attack traffic was mitigated with no customer-visible impact and no collateral effect on other customers sharing the scrubbing capacity. Tuning of our mitigation templates has made handling these events largely automated within the SOC.

### HIGH-IMPACT ATTACKS, BY HALF (1Tbps+ and/or 1Gpps+)
Attacks clearing 1Tbps or 1Gpps increased 1,286 percent year over year.

- **1H 2025**: 79 (+111%)
- **2H 2025**: 167 (+556%)
- **1H 2026**: 1,095

![Figure 2: High-impact attacks by half.]

Much of that increase traces to a small set of high-capacity botnets. Operators associated with Aisuru, Kimwolf, Jackskid, Mossad, and their successors have raised the attack-generation capacity of individual nodes, so fewer compromised devices are needed to reach a given attack size. Their methods emphasize packet, query, request, transaction, and connection rates rather than raw bandwidth, which stresses state tables in firewalls, load balancers, and other stateful devices before link capacity becomes the constraint.

The same shift puts pressure on the routers themselves. Multi-Gpps attacks have overwhelmed individual line cards in peering-edge routers that did not have device self-protection in place. When that happens the card stops forwarding, and everything riding on it goes down with the attack, including customers and peers that were never targeted.

Capacity at that scale now reaches far beyond well-resourced actors, and providers need mitigation headroom for routine peaks, overlapping incidents, and maintenance windows.

IPv6’s share of observed attacks held roughly flat year over year, but two things changed underneath it. ATLAS recorded its first IPv6 attack exceeding 1Tbps in 1H 2026 and active mitigation of IPv6 attacks rose more than 300 percent.

### ATTACK METHODOLOGY AND TARGETING MODE
Direct-path and reflection/amplification are attack methodologies. Monotargeting and carpet-bombing are targeting modes. The two dimensions are independent. Direct-path has taken share from reflection/amplification in each of the last three half-years.

| Attack methodology | Share of total |
| :--- | :--- |
| Direct-path | 64.40% |
| Reflection/amplification | 35.60% |

| Targeting mode | Share of total |
| :--- | :--- |
| Monotargeting | 95.46% |
| Carpet-bombing | 4.54% |

![Figure 4: DDoS attacks by six-month interval: direct path vs reflection/amplification.]

---

## CARPET-BOMBING

Carpet-bombing accounted for a small but growing share of attacks in 1H 2026. A carpet-bombing attack spreads its traffic across many destination addresses inside a prefix rather than concentrating it on a single host. Traffic to each address can stay below per-host detection thresholds while the aggregate arriving at the network edge is large enough to affect the network or shared infrastructure.

Carpet-bombing rose from 3.97% to 4.54% of all observed attacks across the three halves.

![Figure 5: Daily carpet-bombing attacks by attack class, 1H 2025 through 1H 2026.]

> **FROM THE ARBOR CLOUD SOC**  
> A SaaS provider was hit with a significant carpet-bombing event, and the Adaptive DDoS Protection capabilities in the solution were crucial. Per-host thresholds alone would have missed it, since the attack stayed below them on every individual address. A threshold across the entire netblock caught it and started mitigation before the bandwidth for the customer's whole /24 was overwhelmed. That incident and two others were handled within a week for the same customer, with no impact to them and no collateral impact across our wider customer base.

---

## VECTOR AND COMPLEXITY TRENDS

Frequently observed vectors in 1H 2026 were dominated by two groups. TCP state manipulation, including ACK, SYN, RST, and SYN/ACK floods, works against connection tables in firewalls, load balancers, and NAT devices rather than against link capacity, and matches what the DDoS-for-hire market advertises in its Layer 4 catalogues. DNS appeared both as reflection/amplification and as direct query floods, with daily DNS attack counts rising across the window. Reflection/amplification methods including STUN, NTP, SSDP, and memcached remained in steady use, often blended with the above to stress bandwidth and state simultaneously.

By vector class, UDP-borne attacks were the most frequent, ahead of TCP, DNS, and ICMP.

Single-vector attacks are now a slim majority at 52.27 percent. Where multiple vectors are used, moderate combinations remain the norm and large combinations stay rare. The pattern is consistent with free-tier storefronts that present one method already selected, and with experienced operators who add complexity only when a simpler attack stops working.

![Figure 6: Global attack vector type, daily.]  
![Figure 7: Percentage of all observed attacks mitigated by each method, 1H 2025 through 1H 2026.]

> **FROM THE ARBOR CLOUD SOC**  
> We are seeing the same trend toward single-vector attacks. With large volumetric attacks there is no need for complexity until the attack stops working. When it stops working, that is where we see sophisticated actors changing vectors rapidly, using tools built into the platforms they launch from.

---

## WHAT FLOWSPEC AND BLACKHOLE ROUTING MITIGATE

Network controls and dedicated intelligent DDoS mitigation systems, like NETSCOUT's Arbor Threat Mitigation Systems (TMS), do different jobs. Flowspec is well suited to some reflection/amplification traffic, where a handful of rules can describe what needs to be dropped. Direct-path attacks are harder, because router and switch hardware limits how many filtering rules can be held and how specific they can be, and coarse rules lead to under or over blocking. Blackhole routing, or remotely triggered black hole (RTBH) filtering, comes in two forms, and neither one preserves service. The destination-based form (D/RTBH) drops everything addressed to the target, which protects the rest of the network by taking the target offline. The source-based form (S/RTBH) drops everything arriving from a chosen set of source addresses, which keeps the target reachable but cuts off every user in those ranges, legitimate or not. Against carpet-bombing both forms are blunt instruments: The attack is spread across an entire prefix, so blocking by destination means dropping traffic to many customers at once, and the sources are too numerous and too widely distributed to enumerate. Dedicated scrubbing capacity continues to carry the bulk of mitigation across attack classes that require selectivity.

*(Attacks may receive more than one treatment, so values do not sum to the overall mitigation rate).*

---

## HOW MUCH GETS MITIGATED

Across all observed attacks in 1H 2026, service-provider mitigation rates changed little from 1H 2025 while attack counts rose by roughly a quarter. With the rate flat and the volume higher, providers mitigated more attacks in absolute terms, and more attacks also reached their intended target. That does not mean providers are ignoring attacks; provider controls often prioritize continuity of shared network infrastructure, with customer protection delivered via dedicated DDoS services where deployed. Enterprises must still plan for mitigation capability on-premises, close to the services being defended.

- **1H 2025**: 23.12%
- **2H 2025**: 22.35%
- **1H 2026**: 22.24%

![Figure 8: Share of attacks mitigated, by six-month interval.]

---

## WHERE THE CAPACITY HAS TO GO

The attack classes gaining share are the ones that often require selective mitigation, and that changes what a provider’s mitigation capacity must do. Network controls still have their place. NTP reflection is a good case for Flowspec: A small number of rules describe the traffic, and few customers depend on inbound NTP from arbitrary sources, so the collateral cost is acceptable.

Preserving service for the targeted customer is a different job. As more attack traffic arrives from residential address space; spreads across a whole prefix; or exhausts connection state in firewalls, load balancers, and other stateful devices before bandwidth becomes the constraint, more of it has to be detected, diverted, and sent to selective mitigation that can distinguish malicious behavior from legitimate demand.

Outbound mitigation is a different operational problem than inbound customer protection, and it is often less broadly deployed. The same is true for crossbound traffic, which transits the network without originating or terminating on it. Both matter more as per-node botnet capacity rises. Outbound attacks clearing 1Tbps or 1Gpps caused operational impact for broadband and mobile operators worldwide in 1H 2026, and at that scale the traffic can degrade the originating or transit network before it reaches the target.

Reducing that exposure takes two things: suppression that identifies coordinated attack behavior on the way out while leaving unaffected subscriber traffic alone, and remediation of the sources themselves. That means finding and cleaning up botnet nodes, residential proxy nodes, and open reflectors and amplifiers on the operator’s network and on downstream customer networks, supported by source address validation, traffic analysis, and a working abuse response process. Proxy providers draw bandwidth from consumer devices inside subscriber networks, turning them into attack sources without the subscriber’s knowledge. The mechanics of that enrollment are covered in the residential proxy section.

Across all of it, providers need enough dedicated capacity for routine mitigation, concurrent incidents, and predictable headroom.

Two shifts drive what arrives at that capacity: the DDoS-for-hire market’s move to a subscription software model, and residential proxy networks supplying source addresses that look like ordinary subscribers. Both are covered in the sections that follow.

---

## FULLY MANAGED: WHAT DDoS-FOR-HIRE SELLS NOW

ASERT observed increased standardization across DDoS-for-hire booter/stresser services in 1H 2026. The storefronts present professionally: clean landing pages, documented method catalogues, tiered pricing, free trials, cryptocurrency payment, and prominent claims of defeating the major commercial mitigation providers. Their control panels expose sophisticated options via a repeatable interface, which reduces the technical effort required to configure an attack. That uniformity runs deeper than the storefront.

### KEY FINDINGS
- **Attack duration is compressing toward the floor**: Attacks lasting one minute or less have roughly doubled as a share since 2H 2023.
- **Attacks are sold on delivery, not volume**: Bypass variants and rate-based methods have displaced raw bandwidth.
- **Source address quality is now part of the product**: Platforms advertise pools of IP addresses, not just capacity.
- **Most storefronts are the same platform underneath**: Matching price tiers and near-identical panel technology point to white-labelled shared infrastructure, with plans running from a free tier to five figures a month.

### ATTACK DURATION IS COMPRESSING TOWARD THE FLOOR
Short attacks are taking a growing share of everything we see. Since 2H 2023 the band of attacks lasting one minute or less roughly doubled, from 1.6 percent to 3.1 percent, and the one- to-two-minute band rose 37 percent. The increase holds in every year-over-year comparison across that window. Nothing above two minutes has moved the same way, and the 15-to-30-minute band has gone in the other direction. Roughly three points of share have moved out of the bands above 15 minutes and into the bands below five.

The storefronts explain the shift, and the free tier is only part of it. On every service reviewed, the launch form loads preconfigured: a single concurrent attack, a duration field prefilled at 60 seconds, and a free method already selected. The shift is in the mix, not the majority. Longer attacks are still the bulk of what we see, and the paid tiers still sell them.

- **194**: ≤1 minute
- **137**: 1 to 2 minutes
- **105**: 2 to 5 minutes
- **100**: 5 to 15 minutes
- **86**: 15 to 30 minutes
- **91**: 30 to 60 minutes
- **95**: Over 60 minutes  
*(Source: NETSCOUT ATLAS attack data, indexed to 2H 2023 = 100)*

![Figure 9: Change in each duration band's share of all attacks, indexed to 2H 2023 = 100.]

### ATTACKS ARE SOLD ON DELIVERY, NOT VOLUME
Platforms sell by naming the defense they claim to beat. Method listings include vectors branded for specific hosting providers and tagged as mitigation tests, and bypass variants target major content delivery networks, commercial mitigation services, and popular multiplayer game platforms. Customers are buying a claim that the traffic will arrive. These are seller claims and should not be treated as independently verified performance results.

The unit of measure has changed to match. Catalogues now advertise rate: packets per second at Layers 3 and 4, connections per second against stateful devices, queries per second against resolvers, and requests or transactions per second at Layer 7. Layer 4 catalogues are dominated by TCP state manipulation built around ACK, PSH-ACK, RST, FIN, and out-of-sequence packets, and several platforms sell low-rate variants built specifically to stay below volumetric detection thresholds.

Two mechanisms explain this. State exhaustion fills connection tables in firewalls, load balancers, and NAT devices, which can fail well below the point at which a transit link saturates. Sheer rate overwhelms application backends, resolvers, and session handling regardless of state, and neither mechanism requires large bandwidth.

### SOURCE ADDRESS QUALITY IS NOW PART OF THE PRODUCT
One platform’s headline capacity figure is a claimed pool of several hundred thousand IP addresses rather than a bandwidth number. A Layer 7 flood that must survive a modern CDN cannot originate from a datacenter range, a known bad ASN or an address with a poor reputation. It needs to come from real ISPs, real subscriber allocations, and plausible geographies, which is precisely what the residential proxy market sells.

### MOST STOREFRONTS ARE THE SAME PLATFORM UNDERNEATH
The services reviewed present themselves as commercial software. They ship REST APIs and command line clients alongside the web panel, publish method glossaries, maintain blogs, and borrow their copy from enterprise software marketing, promising no lock-in and enterprise concurrency.

The similarity runs deeper than the presentation. Pricing tiers and plan options match closely across services that present themselves as competitors, and the panels run near-identical backend web technology. The ladder those tiers describe is wide: a no-barrier free tier at the bottom and advertised figures of several terabits per second gated behind subscriptions priced around twenty thousand dollars a month at the top end. Those capacity figures are seller claims, not independently verified attack measurements. The most economical explanation is white-labelled shared infrastructure, with a small number of platform operators supplying a larger number of storefronts. If that holds, both the market and the effective target set for disruption are smaller than the storefront count suggests.

### THE SHAPE OF THE MARKET
The market has settled: a small number of shared backends, a price ladder running from free to five figures, methods sold on delivery, and short bursts aimed at device state. At the top of that ladder, what sells is traffic that arrives from addresses that carry no signal.

---

## RESIDENTIAL PROXY NETWORKS AND DDoS

A residential proxy network (RPN) is an umbrella term for commercial services that offer traffic anonymization, IP access, and bandwidth for a fee. Commercial RPNs route traffic through internet-connected consumer devices, so the traffic uses addresses assigned to residential or mobile access networks rather than datacenter ranges. For DDoS defense, the issue is not naming every proxy but recognizing when many sources that look ordinary are acting together as attack infrastructure.

### PROXY NODE PROLIFERATION
Unlike botnets, which rely on exploitation and malware to recruit new nodes, RPNs operate as or collaborate with bandwidth broker platforms. Users are promised passive income for sharing a residential connection, and developers of software and mobile apps can generate revenue by embedding a proxy provider's SDK.

A much larger share of the pool is enrolled covertly. Users install an app that turns the device into a proxy without informed consent, and researchers have observed consumer hardware shipped with proxyware preinstalled.

### RESIDENTIAL PROXIES AS A DDoS DETECTION CHALLENGE
ASERT tracks residential proxy infrastructure and pairs it with DDoS telemetry, so proxy sources participating in attacks can be identified without treating residential address space as malicious. The signals worth watching:
- Many sources converging on the same destination or function
- Traffic rate changes that move in step across those sources
- The same protocol behavior repeating across them
- Connections between proxy clients and the backhaul infrastructure they depend on

This is what makes proxy-sourced attacks tractable. Individual proxy addresses look legitimate, the client population would feed a feed with millions of entries, home connections rotate addresses so entries age out quickly, and RPN customers cycle through proxies fast enough that a node often makes one connection and then idles. Coordination is the durable signal; the client address is not.

![Figure 10: Daily elements associated with proxy clients observed participating in DDoS activity.]  
*(Google announced the takedown of a notorious RPN on July 2, reporting at least 2 million nodes. After accounting for aging-out on the feed, ASERT observed a drop of around 2 million tracked devices).*

### DUAL-USE OF PROXIES
The RPN market is not uniform. Many operators serve only commercial customers, who use proxies for geographic testing, advertising verification, data collection, and privacy services. Other networks carry illicit proxying and DDoS traffic alongside that legitimate demand, on the same infrastructure. Google, law enforcement, and partners recently announced takedowns of several RPNs that operated on both sides.

That dual use matters because source quality is part of the attack product. Proxies with strong IP reputation are marketed as premium inventory, while proxy pools with weaker reputations can be additionally monetized through DDoS-for-hire.

We continue to monitor whether the effects of this takedown persist. Prior booter, stresser, and botnet takedowns have often had transient effects, with new entities taking the place of those removed.

### BACKHAUL VISIBILITY AND DDoS SUPPRESSION
ASERT borrowed the technique from botnet tracking. Proxy clients change frequently, but backhaul infrastructure changes more slowly, because clients must contact it for instructions or service access. This is not command and control: The operator does not control the device, and the proxy can decline or drop the connection at any time.

At the time of writing, ASERT tracked 130 IPv4 addresses as RPN backhaul infrastructure. Once online, an address often stays static for weeks or months, and backhaul often covers sequential ranges within a /24, indicating that RPNs reserve entire address ranges at hosting providers.

Tracking backhaul infrastructure identifies the nodes; it does not detect or mitigate the attacks. Knowing the backhaul lets an operator find which hosts inside their own network, or a downstream customer’s, are acting as proxy nodes. Outbound and crossbound attack traffic from those hosts can then be detected and suppressed.

![Figure 11: Backhaul IPv4 addresses of residential proxy networks tracked by ASERT.]

---

## CONCLUSION

Attack volume rose through the first half of 2026, and the mix changed with it. Direct-path methods now represent roughly two-thirds of observed attacks. Carpet-bombing continues to gain share as a targeting mode, multivector attacks remain common, and residential proxy networks make malicious traffic look more like ordinary user traffic. Coarse network controls can contain a shrinking portion of attacks, but containment is not service preservation. As malicious traffic becomes more distributed, direct, state-intensive, and difficult to distinguish from legitimate residential traffic, providers need enough dedicated mitigation capacity at their edges to detect, divert, inspect, and surgically mitigate more traffic while keeping customer services available. Enterprises need on-premises mitigation for services that operate from their own environments. Cloud-delivered mitigation remains the off-premises complement for distributed attacks, overflow, and events that exceed local capacity.

---

## METHODOLOGY

The data in this report is derived from NETSCOUT’s ATLAS Threat Intelligence, which provides unparalleled internet visibility at a global scale, collecting, analyzing, prioritizing, and disseminating data on DDoS attacks from 209 countries and territories, 413 industry verticals, and 12,031 autonomous system numbers (ASNs).

NETSCOUT maps the DDoS landscape via passive, active, and reactive vantage points, providing unique visibility into global attack trends. Our visibility covers two-thirds of the routed IPv4 space, across network edges that carried global peak traffic of over 800Tbps in 1H 2026. By tracking multiple botnets and DDoS-for-hire services that leverage millions of abused or compromised devices, we monitor tens of thousands of daily DDoS attacks. Our global intelligence spans attack signatures for more than 100 threat actors, ensuring proactive defense against evolving threats.

### ABOUT ASERT
ASERT is NETSCOUT's elite group of engineers and researchers specializing in information security. Their breadth and depth of knowledge and real-world experience combined with NETSCOUT's unique, unrivaled visibility into global internet traffic and the threat landscape, enables them to provide insights and remediation for customers to manage active threats and their long-term security profile.

The ASERT team shares insights via threat blogs, customer advisories, and DDoS Threat Intelligence reports to increase knowledge and preparation for all global organizations dealing with evolving threats.  
*Learn more at netscout.com/asert*

### ABOUT NETSCOUT
NETSCOUT SYSTEMS, INC. (NASDAQ: NTCT) is a leading provider of observability, AIOps, cybersecurity, and DDoS attack protection solutions. NETSCOUT protects the connected world from cyberattacks and performance and availability disruptions through its unique data mediation platform and solutions powered by its pioneering deep packet inspection at scale technology.

NETSCOUT threat intelligence continuously delivers relevant, actionable DDoS intelligence that organizations can use proactively to defend against DDoS attacks and other cyberthreats. The world's most demanding government, enterprise, and service provider organizations rely on NETSCOUT visibility and DDoS protection capabilities to protect the digital services that advance our connected world.  
*Visit netscout.com*

---

## NETSCOUT DDoS PROTECTION SOLUTIONS

To defend against the evolving threats documented in this report, NETSCOUT offers comprehensive DDoS protection backed by the world's best AI-powered threat intelligence and more than 25 years of DDoS experience. NETSCOUT’s Arbor Adaptive DDoS Protection is a purpose-built solution designed to protect the availability of your mission-critical services. Our best-in-class portfolio of products includes:

- **Arbor Sightline**: Real-time visibility and anomaly detection using flow telemetry across service provider and enterprise networks. Provides early warning of developing attacks and enables rapid response coordination.
- **Arbor Edge Defense (AED)**: Inline, always-on protection blocking both inbound DDoS attacks and outbound threat communications. Prevents compromised devices from participating in attacks while protecting against inbound floods.
- **Arbor Threat Mitigation System (TMS)**: High-throughput scrubbing removing malicious traffic before reaching business-critical services. Scales to multiterabit attack volumes while maintaining legitimate traffic flow.
- **ATLAS Intelligence Feed (AIF)**: Live global, AI-powered and human-curated threat intelligence tailored to Arbor solutions, updating blocklists and detection logic in near real-time based on observations from NETSCOUT's worldwide visibility platform.
- **Arbor Sightline Mobile**: Specialized visibility for mobile packet core environments, providing international mobile subscriber identity (IMSI) attribution and detection of carpet-bombing attacks affecting wireless networks.
- **Arbor Cloud**: A cloud-based, fully managed DDoS attack protection service that has 16 regional scrubbing centers, over 33Tbps of dedicated mitigation capacity and is intelligently integrated with NETSCOUT's Arbor on-premises solutions.

These solutions work in concert to provide defense-in-depth against the full spectrum of threats documented in this report, from AI-enhanced adaptive attacks to multiterabit IoT botnet floods to sophisticated hacktivist campaigns.

---

**Contributors**  
- Hardik Modi, Editor  
- Chris Conrad, Contributing Editor  
- Roland Dobbins, Researcher  
- Max Resing, Researcher  
- Kinjal Patel, Researcher  
- Tom Marsland, Contributor, Arbor Cloud SOC  

©2026 NETSCOUT SYSTEMS, INC. All rights reserved. NETSCOUT, and the NETSCOUT logo are registered trademarks of NETSCOUT SYSTEMS, INC., and/or its subsidiaries and/or affiliates in the USA and/or other countries. All other brands and product names and registered and unregistered trademarks are the sole property of their respective owners.  
SECR_001_EN-2503 1H 2026 09/2026

<!-- CONVERSION_METADATA: {"source": "https://github.com/jacobdjwilson/awesome-annual-security-reports", "date": "2026-10-02", "model": "gemini-3.5-flash-lite"} -->
