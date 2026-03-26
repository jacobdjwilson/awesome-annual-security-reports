# Under the Surface: Uncovering Cyber Risk in the Global Supply Chain

**Organization:** Bitsight  
**Year:** 2025  
**Author:** Ben Edwards  

## Table of Contents
- [Introduction](#introduction)
- [How Big Are Digital Supply Chains?](#how-big-are-digital-supply-chains)
- [Critical Supply Chain Links](#critical-supply-chain-links)
- [Security Performance in Critical Supply Chain Links](#security-performance-in-critical-supply-chain-links)
- [Conclusions and Recommendations](#conclusions-and-recommendations)
- [Methodology](#methodology)

---

## Introduction

Interconnectedness is a fundamental feature of most human endeavors. Whatever the goal, success regularly depends on the cooperation of different entities, each with their own specialty.

As we have entered the digital age, new specialities and new methods of collaboration have made it easier than ever to work together; software can be installed in minutes, and services can be accessed with a few clicks and keystrokes. This ease of collaboration allows for organizations to focus on their mission, while leveraging others to provide the necessary tools to navigate the rapidly evolving digital landscape. Of course, this extends beyond single relationships. Consumers of one product provide to many others, who themselves provide to many others, and so forth, creating the global supply chain.

However, this interconnectedness is not without risk. By relying on others, organizations develop dependencies over which they may have limited control. This means that disruptions experienced by partners can affect not just a single organization, but also a remarkably large portion of the global economy. Recent history has given us numerous incidents where a disruption at one single company has long-ranging and cascading effects. To name a few in the first half of the current decade:

- SolarWinds (December 2020)
- Colonial Pipeline (May 2021)
- Kaseya (July 2021)
- PyTorch (December 2022)
- TSCM (February 2023)
- 3CX (April 2023)
- Apple, Microsoft, others
- Okta (October 2023)
- Snowflake (May 2024)
- Crowdstrike (July 2024)

In many of these cases, an unexpected yet critical player in the global supply chain experiences an event (whether because of a targeted attack or an unfortunate circumstance) that causes (or had the potential to cause) cascading effects. Costs for these types of events are difficult to assess, but estimates usually break into the billions of dollars and sometimes orders of magnitude more, with insured losses only covering a fraction of the overall event. In our ever more connected world, in which nearly all interactions are mediated through the internet, having an in-depth knowledge of the digital supply chain, understanding risk, and taking action is critical.

Bitsight believes that the best way for the global market to address these challenges is through the use of principled, data-driven analysis of interconnectedness and exposure. We are in a unique position to offer insights into this increasingly common and impactful problem. This report leverages Bitsight data drawn from a variety of sources, including third-party relationships, our security scanning technologies, entity mapping, and financial data.

![A diagram illustrating the comprehensive nature of Bitsight's data resources, showing the intersection of third-party relationships, security scanning, entity mapping, and financial data.]

In particular, we examine the digital supply chains of more than 500,000 consumer organizations, using 42,600 different products across 12,000 providers, comprising nearly 61.5M relationships. This allows us to make several key observations:

1. **Supply chains are vast.** We find that a typical organization employs hundreds of products from dozens of providers.
2. **Providers have 2.5x larger supply chains compared with the consumers they serve.** The providers we observe in our data set tend to have larger supply chains compared with their consumer customers. With a larger attack surface to defend, providers tend not to perform as strongly as consumers.
3. **There are several areas of concentrated risk across the supply chain.** In some sectors and industries, providers who serve <1% of companies service more than 50% of the market share (based on their clients’ revenue).
4. **We highlight the “Critical 99,”** the top 99 providers weighted by revenue to determine the proportion of the market share they serve. Additionally, we analyze “hidden pillars,” specialized providers that, despite lacking global reach, play a crucial role in major industries.
5. **33% of US organizations rely on companies listed by the US Department of Defense as “Chinese Military Companies.”** In the current geopolitical zeitgeist, it is more important than ever to understand “who” is in your supply chain.

---

## How Big Are Digital Supply Chains?

The first questions to ask before any data-driven investigation of supply chain risk should be “what is it composed of?” and “how big is it?” 

![Figure 1: Overall size of supply chain by various measures, showing distributions for Hosting Providers, Internet Facing Assets, Product Categories, Providers, and Products.]

The scope of Figure 1 clearly shows that the size of a digital supply chain can be vast. Some organizations rely on thousands (or, in rare cases, tens of thousands) of different products supplied by hundreds of providers. Despite this “heavy tail,” we see that organizations still typically have to manage around 100 different products spread across a dozen or so providers.

> **Key Point:** The typical organization has to manage hundreds of products, and dozens of providers in direct relationships. This does not include the extended “nth party” relationships (the suppliers of suppliers).

![Figure 2: Supply chain size between providers (dark dots) and consumers (light dots), showing that providers have significantly more products, providers, and internet-facing assets.]

> **Key Point:** Providers have a larger digital supply chain compared with consumers, presenting a much larger potential attack surface.

![Figure 3: All of the relationships in our third-party risk management data visualized as a network, showing a dense, tangled web of connections.]

![Figure 4: Correlation between organization size and various measures of supply chain size, showing positive linear regression lines across all metrics.]

---

## Critical Supply Chain Links

We start with the most basic view, specifically “what proportion of organizations we track use a particular provider” (Figure 5).

![Figure 5: Distribution of proportion of organizations using a particular provider.]

Ultimately, what we should focus on is both the number of organizations a particular provider serves and the market share of the organizations who use that provider. 

![Figure 6: Comparison of proportion of organizations using a particular provider, with a "break even" line.]

![Figure 7: A sample of hidden pillars of the global supply chain, i.e. providers that are used by a small subset of very large companies.]

> **Key Point:** Some providers only serve a small number of companies, but a large portion of the global supply chain when the size of the customer revenue is considered. We call these hidden pillars of the global supply chain because these hidden pillars are critical to the global supply chain but may not appear so based solely on the number of customers they serve.

![Figure 8: Top 99 providers weighted by revenue to determine the proportion of the market share they serve.]

![Figure 9: Industry market share comparisons, highlighting providers that "punch above their weight" in specific sectors.]

![Figure 10: UAE market share compared to global market share.]

> **Key Point:** Providers may have a small global market share, but an outsized presence in a particular sector or geography.

![Figure 11: Top Chinese providers to the US supply chain.]

> **Key Point:** 33% of the US supply chain relies on companies listed by the US Dept of Defense as a “Chinese Military Company.” Two-thirds of the US supply chain relies on the companies in Figure 11.

![Figure 12: Digitization and organizations and market share.]

> **Key Point:** In the global supply chain, critical organizations with large market share may have just a few dozen employees.

---

## Security Performance in Critical Supply Chain Links

![Figure 13: Average risk vector scores for providers and non-providers in our data set, comparing performance across 22 risk vectors.]

![Figure 14: Letter grades of providers across various levels of market penetration.]

> **Key Point:** Large providers (and providers in general) tend to have worse security posture than the overall population of organizations that Bitsight monitors.

![Figure 15: New Event rates for providers vs market share.]

![Figure 16: New Event rates for providers vs market share, correlating assets and remediation time.]

> **Key Point:** There are providers with large market share that are among some of the worst performing security organizations.

> **Key Point:** There are major supply chain players (>25% market share) that have a large market share, a large attack surface with many vulnerabilities, and exceptionally long remediation times for those vulnerabilities.

---

## Conclusions and Recommendations

If the global supply chain is a tangled web of providers of physical goods, software, services, and hosting, then this is also true of any particular organization’s supply chain. It’s likely smaller, but still likely dauntingly large. So what is a CISO or risk manager to do in the face of this complexity?

- **Enumerate your supply chain.** Knowing is half the battle, and the first step here is understanding who is enabling your organization’s mission.
- **Evaluate criticality.** Every piece of equipment, software, and data your company utilizes was selected after due consideration. But some are more critical than others.
- **Assess your providers’ security.** The first step to knowing who your critical providers are is to understand their security posture.
- **Reach out.** These providers may not have a clear view of their own security issues. Bitsight includes the ability to Enable Vendor Access.
- **Look deeper.** With your third-party network on its way to better security, it’s time to examine how your extended supply chain is faring.
- **Evaluate your own criticality.** If your own organization is a critical player in the global supply chain, then it’s possible that an incident could not just affect you, but also disrupt the supply chain.

---

## Methodology

This analysis relies on data from three different data sources collected by Bitsight:

1. **Fourth party relationship data.** Known relationships between entities and the products/services they leverage.
2. **Organization data.** Identification of internet assets and ownership, enriched with firmographic data.
3. **Events data.** Security data derived from Bitsight’s security assessment technologies, examining hygiene, compromise, and incident history.

The results in this research are derived from a snapshot of data collected at the end of October of 2024.

©2024, BitSight Technologies, Inc. and its affiliates (“Bitsight”). BITSIGHT® is a registered trademark of Bitsight. All rights reserved.