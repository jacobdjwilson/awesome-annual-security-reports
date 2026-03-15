# Early Warning Signals: When Attacker Behavior Precedes New Vulnerabilities

An empirical analysis of pre-disclosure spikes in malicious activity — and what they signal about the vulnerability lifecycle.

## Table of Contents
- [Key Takeaways](#key-takeaways)
- [Do Spikes in Attacker Activity Foreshadow New Vulnerabilities?](#do-spikes-in-attacker-activity-foreshadow-new-vulnerabilities)
- [Codifying the Relationship](#codifying-the-relationship)
- [Defining a Spike](#defining-a-spike)
- [Narrowing the Dataset to Maximize Signal Integrity](#narrowing-the-dataset-to-maximize-signal-integrity)
- [Revealing the Signal: Attacker Activity as a Leading Indicator of New Cyber Vulnerabilities](#revealing-the-signal-attacker-activity-as-a-leading-indicator-of-new-cyber-vulnerabilities)
- [Attackers Leveraging Old Vulnerabilities](#attackers-leveraging-old-vulnerabilities)
- [Why Might Attackers Do This?](#why-might-attackers-do-this)
- [Defenders’ Six-Week Critical Window](#defenders-six-week-critical-window)
- [Why the Skew?](#why-the-skew)
- [Why Does This Signal Really Matter?](#why-does-this-signal-really-matter)
- [Recommendations for Defenders](#recommendations-for-defenders)
- [Methodology](#methodology)
- [Spike Detection](#spike-detection)
- [Global Spike](#global-spike)
- [Local Spike](#local-spike)
- [Defining Spike-to-CVE Pairs](#defining-spike-to-cve-pairs)

---

## Key Takeaways
This report explores the correlation between spikes in attacker activity and subsequent CVE disclosures in edge technologies. Our findings suggest a repeatable pattern with predictive value — useful for all defenders, from analysts to CISOs.

1. **Spikes in attacker activity often precede new cyber vulnerabilities.**
   In 80 percent of cases we analyzed, significant spikes in opportunistic attacker activity against edge technologies were followed by the disclosure of a new CVE affecting the same technology within six weeks. This recurring pattern may offer early warning value.
2. **These spikes give defenders a defined window to prepare.**
   The clustering of new CVEs within six weeks of attacker spikes provides defenders with a concrete timeframe to increase monitoring, harden systems, and preemptively act — even before a vulnerability is known. CISOs can use this window to justify early planning or investment.
3. **Blocking early reconnaissance may keep systems off attacker inventories.**
   Spikes may reflect exploit-based reconnaissance designed to identify exposed systems. Blocking the associated IPs during these phases may prevent inclusion in attacker inventories — reducing the likelihood of being targeted later, even if different IPs are used for exploitation of the new CVE emerging weeks later.
4. **Enterprise edge technologies show the strongest patterns.**
   After filtering out ambiguous cases and noise, all spike-CVE pairs we observed involved internet-facing assets commonly deployed in enterprise environments — such as VPNs, firewalls, and products from vendors like Cisco, Fortinet, Citrix, and Ivanti.
5. **Most spikes involved real exploits — not scanning.**
   The majority of activity leading up to CVEs was not generic scanning but exploit attempts against previously known vulnerabilities. This supports two likely motives: testing inputs that may lead to new CVE discovery, or inventorying systems for future exploitation when a new flaw becomes known.
6. **State-sponsored actors have repeatedly targeted edge infrastructure.**
   Nation-state groups like the Typhoons have reportedly focused on enterprise-focused edge devices for pre-positioning, surveillance, and access persistence. All products studied in this analysis are enterprise-focused edge systems, highlighting both enterprise and national security stakes.

## Do Spikes in Attacker Activity Foreshadow New Vulnerabilities?
GreyNoise has repeatedly observed spikes in attacker activity — including scanning, brute forcing, and exploitation attempts — targeting specific technologies in the weeks leading up to the public disclosure of new vulnerabilities affecting those same technologies.

This raised a compelling hypothesis: Could these individual incidents reflect a broader trend — one where attacker behavior, as measured by GreyNoise’s Global Observation Grid (GOG), offers an early warning signal for the emergence of new CVEs?

The data supports this possibility. After analyzing all GreyNoise tags (CVSS 6+ CVEs) associated with edge technologies, we found a consistent pattern: spikes in attacker activity often precede new vulnerability disclosures. This pattern was only observed across a specific subset of enterprise edge products — spanning eight vendors — though we did not limit our analysis to enterprise technologies.

## Codifying the Relationship
To test our hypothesis, we analyzed attacker activity over time — specifically, the daily count of unique IPs observed — across GreyNoise tags associated with edge technologies. These included tags tracking scanners, crawlers, and brute forcing, as well as tags linked to CVEs with a CVSS score of six or higher. Our analysis began in September 2024, following a major enhancement of GreyNoise’s Global Observation Grid (GOG).

We used the same set of edge-focused tags featured in our prior report on resurgent vulnerabilities. Our goal this time: to identify statistically significant spikes in malicious activity and examine whether they consistently preceded the disclosure of new CVEs, helping us assess whether attacker behavior could serve as a signal for defenders.

## Defining a Spike
To ensure rigor, we only counted a day’s activity as a “spike” if it met two conditions. This dual threshold helps ensure the spike is both globally anomalous and locally unusual — filtering out noise and highlighting activity that truly stands out.

1. **Globally Elevated:** The daily unique IP count exceeded the median for that tag’s entire history, plus two times the interquartile range (IQR).
2. **Locally Elevated:** The daily count also exceeded the 28-day rolling mean (14 days before and after), plus two rolling standard deviations (same period as rolling mean).

## Narrowing the Dataset to Maximize Signal Integrity
To ensure the integrity of our findings, we filtered out tags that introduced noise or lacked meaningful trend signals. Specifically, we excluded tags that exhibited:
- **Quasi-stationarity:** Consistent, heartbeat-like patterns that lacked clear anomalies.
- **Excessive CVE volume:** Vendors with so many vulnerabilities that linking specific spikes to individual CVEs became statistically meaningless.
- **Discontinuous data:** Gaps or irregularities in the time series that made trend analysis unreliable.
- **No qualifying spikes:** Tags that did not meet our defined threshold for anomalous activity.

After applying these filters, we were left with 216 statistically significant spikes in attacker activity, observed from September 2024 onward. Each spike was then paired with the next newly disclosed CVE affecting the same product associated with the tag.

## Revealing the Signal: Attacker Activity as a Leading Indicator of New Cyber Vulnerabilities
Across eight enterprise vendors, GreyNoise observed that spikes in attacker activity (white dots) against specific edge technologies often preceded the disclosure of new CVEs (red dots) affecting those same products — typically within six weeks. While not necessarily causal, this recurring pattern suggests that attacker behavior can serve as an early signal for emerging vulnerabilities, especially in perimeter-facing systems.

![Chart showing spike events (white dots) preceding CVE disclosures (red dots)]

MikroTik, for example, has a signal but probably shouldn’t be used to inform preemptive defenses. With several spikes before the one emergent CVE, it’s difficult to draw any correlation between the spikes and the new CVE. Citrix follows a similar pattern, albeit less pronounced.

On the other hand, other vendors tend to have clear and definitive patterns. Ivanti is perhaps the most striking example, with very tight and marked spike-to-new-CVE patterns. Likewise, Fortinet is an example of very rapid successions of ‘there’s a spike’ and ‘there’s a new CVE.’ In these situations, defenders sometimes have days to prepare before a new CVE emerges.

## Attackers Leveraging Old Vulnerabilities
The age of each vulnerability also stood out to us. Take Cisco CVE-2011-3315, for example — we observed significant spikes in activity against this 14 year old vulnerability just before the emergence of a new vulnerability. Or CVE-2017-15944, affecting PAN-OS — an eight year old flaw still in play, serving as an indicator of new vulnerabilities affecting PAN-OS.

This theme is like a beating drum in our recent research: old vulnerabilities are persistent problems, and attackers know how to use them to inflict damage and reap the rewards of successful operations.

## Why Might Attackers Do This?
Several plausible motivations may explain why attacker behavior often spikes ahead of new vulnerability disclosures:

1. **Target confusion through broad activity:** For vendors like Ivanti, we frequently observed simultaneous spikes across multiple tags. This may be an intentional tactic to obscure the attacker’s true focus.
2. **Pre-positioning through system inventorying:** Many spikes may reflect reconnaissance — attackers proving systems using older exploits to catalog exposed assets. These systems may later be targeted when a new vulnerability emerges.
3. **Spikes as signals of zero-day discovery:** In some cases, spikes may reflect more than reconnaissance — they could represent active attempts to discover new vulnerabilities.

## Defenders’ Six-Week Critical Window
Across all 216 spike events we studied, 50 percent were followed by a new CVE within three weeks, and 80 percent within six weeks.

![Distribution chart of Spike-to-New CVE Delta]

## Why the Skew?
The six-week window doesn’t apply evenly across all vendors. The pattern breaks down most notably for Citrix, Cisco, and MikroTik.

- **Cisco:** Somewhat more consistent than Citrix, but still exhibits many long-tail cases beyond six weeks.
- **Citrix:** In about half of all spike cases, a new CVE follows more than six weeks later.
- **MikroTik:** Wide variability; attacker spikes are not a reliable signal for anticipating new CVEs.

## Why Does This Signal Really Matter?
This report highlights a powerful signal: spikes in attacker activity often precede new CVEs. This gives defenders a rare chance to act early — before vulnerabilities are even disclosed. All of the spikes we analyzed occurred in enterprise-focused edge technologies — a category that continues to attract attention from sophisticated threat actors.

## Recommendations for Defenders
1. **Block Pre-Disclosure Activity to Stay Off Target Lists:** Block IPs involved in significant spikes of exploit-driven reconnaissance.
2. **Don’t Assume “Fully Patched” Means “Fully Safe”:** Spikes may reflect reconnaissance that leads to new discoveries. Even patched systems might be probed in advance of a new CVE.
3. **Use Spike-CVE Patterns for Strategic Planning:** Use these patterns to prioritize patching, strengthen visibility, harden exposed services, or reassess use of high-risk technologies.

## Methodology
We analyzed attacker activity using GreyNoise’s Global Observation Grid (GOG), focusing on edge technology tags from September 2024 onward.

### Spike Detection
A day qualified as a spike only if it met both of the following conditions:

#### Global Spike
Per tag over the full period, a day $t$ was considered a global spike if:
$x_t > \text{median}(x) + 2 \times \text{IQR}(x)$

#### Local Spike
A local spike was defined as:
$x_t > \mu(t-14, t+14) + 2\sigma(t-14, t+14)$

*Where:*
- $x_t$ is the unique IP count for day $t$.
- $x$ is the vector of daily unique IPs for that tag across all days.
- $\text{IQR}$ is the interquartile range of $x$.
- $\mu$ is the rolling mean.
- $\sigma$ is the rolling standard deviation.

### Defining Spike-to-CVE Pairs
- Matched each spike to the first new CVE (CVSS 6+) affecting the same vendor/technology.
- Ensured each spike was linked to only one CVE, and each CVE could have multiple spikes associated.
- Filtered out vendors with quasi-stationary activity, excessive CVE volume, or discontinuous time series.