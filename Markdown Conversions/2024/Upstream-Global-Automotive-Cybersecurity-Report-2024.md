# Global Automotive Cybersecurity Report 2024

## Table of Contents
- [Opening letter from our CEO](#opening-letter-from-our-ceo)
- [Methodology](#methodology)
- [Executive summary](#executive-summary)
- [Chapter 1: The automotive cybersecurity inflection point](#chapter-1-the-automotive-cybersecurity-inflection-point)
  - [Analyzing the potential scale of automotive cyber risks](#analyzing-the-potential-scale-of-automotive-cyber-risks)
  - [Threat actors motivation has also shifted towards scale and massive impact](#threat-actors-motivation-has-also-shifted-towards-scale-and-massive-impact)
  - [The financial perspective: the rising cost of cyber attacks on the Automotive and Smart Mobility ecosystem](#the-financial-perspective-the-rising-cost-of-cyber-attacks-on-the-automotive-and-smart-mobility-ecosystem)
  - [The internal impact: the dynamic SBOM](#the-internal-impact-the-dynamic-sbom)
  - [Spotlight: social media has become a breeding ground for automotive cyber activities](#spotlight-social-media-has-become-a-breeding-ground-for-automotive-cyber-activities)
  - [The Automotive and Smart Mobility ecosystem is entering a new era of GenAI, democratizing attacks but also cyber defense](#the-automotive-and-smart-mobility-ecosystem-is-entering-a-new-era-of-genai-democratizing-attacks-but-also-cyber-defense)
- [Chapter 2: Automotive cybersecurity trends](#chapter-2-automotive-cybersecurity-trends)
  - [Review of incidents](#review-of-incidents)
  - [Overview of 2023 CVEs](#overview-of-2023-cves)
  - [The EV charging ecosystem is rapidly expanding](#the-ev-charging-ecosystem-is-rapidly-expanding)
  - [Commercial fleets](#commercial-fleets)
  - [Smart mobility IoT devices & services](#smart-mobility-iot-devices-services)
  - [Insurance](#insurance)
  - [Autonomous vehicles](#autonomous-vehicles)
  - [The impact of Right to Repair on agriculture vehicles](#the-impact-of-right-to-repair-on-agriculture-vehicles)
- [Chapter 3: 2023’s diverse attack vectors](#chapter-3-2023s-diverse-attack-vectors)
  - [Increasingly sophisticated attacks open the door for large-scale impact across the entire ecosystem](#increasingly-sophisticated-attacks-open-the-door-for-large-scale-impact-across-the-entire-ecosystem)
  - [Telematics and application servers](#telematics-and-application-servers)
  - [Remote keyless entry systems](#remote-keyless-entry-systems)
  - [ECUs](#ecus)
  - [APIs](#apis)
  - [Mobile applications](#mobile-applications)
  - [Infotainment systems](#infotainment-systems)
  - [EV charging infrastructure](#ev-charging-infrastructure)
  - [Bluetooth](#bluetooth)
  - [OTA updates](#ota-updates)
  - [V2X attacks](#v2x-attacks)
- [Chapter 4: The regulatory reality](#chapter-4-the-regulatory-reality)
  - [Generative AI is reshaping the Automotive and Smart Mobility ecosystem, but regulations are still evolving](#generative-ai-is-reshaping-the-automotive-and-smart-mobility-ecosystem-but-regulations-are-still-evolving)
  - [Cybersecurity regulations make headway worldwide](#cybersecurity-regulations-make-headway-worldwide)
  - [The expansion of UNECE WP.29 R155 and ISO/SAE 21434](#the-expansion-of-unece-wp29-r155-and-isosae-21434)
  - [The EU Cyber Resilience Act promotes extended cybersecurity resilience](#the-eu-cyber-resilience-act-promotes-extended-cybersecurity-resilience)
  - [ISO 15118 secures vehicle-to-grid communications](#iso-15118-secures-vehicle-to-grid-communications)
  - [The SEC echoes the increasing focus on cybersecurity incidents](#the-sec-echoes-the-increasing-focus-on-cybersecurity-incidents)
  - [NHTSA updates cybersecurity best practices](#nhtsa-updates-cybersecurity-best-practices)
  - [EV charging infrastructure cybersecurity regulations continue to expand and deepen](#ev-charging-infrastructure-cybersecurity-regulations-continue-to-expand-and-deepen)
  - [Vehicle data and privacy regulations are inevitable](#vehicle-data-and-privacy-regulations-are-inevitable)
- [Chapter 5: Threats from the deep and dark web](#chapter-5-threats-from-the-deep-and-dark-web)
  - [What is the deep and dark web?](#what-is-the-deep-and-dark-web)
  - [Gray hats blurring the line between black hats and white hats](#gray-hats-blurring-the-line-between-black-hats-and-white-hats)
  - [What occurs in the deep and dark web?](#what-occurs-in-the-deep-and-dark-web)
  - [Ransomware actors increasingly target automotive suppliers](#ransomware-actors-increasingly-target-automotive-suppliers)
- [Chapter 6: Automotive cybersecurity solutions](#chapter-6-automotive-cybersecurity-solutions)
  - [Protecting the vehicle during its entire lifecycle](#protecting-the-vehicle-during-its-entire-lifecycle)
  - [Security by design](#security-by-design)
  - [Multi-layered cybersecurity stack](#multi-layered-cybersecurity-stack)
  - [Developing an effective vSOC](#developing-an-effective-vsoc)
  - [Automotive-specific threat intelligence offers a proactive approach to risk](#automotive-specific-threat-intelligence-offers-a-proactive-approach-to-risk)
  - [Upstream’s cloud approach to automotive cybersecurity](#upstreams-cloud-approach-to-automotive-cybersecurity)
  - [The Upstream Platform](#the-upstream-platform)
  - [Upstream Managed vSOC](#upstream-managed-vsoc)
  - [Enhancing vSOC investigations with GenAI](#enhancing-vsoc-investigations-with-genai)
  - [Upstream AutoThreat® PRO Cyber Threat Intelligence](#upstream-autothreat-pro-cyber-threat-intelligence)
- [Chapter 7: Predictions for 2024](#chapter-7-predictions-for-2024)
- [References](#references)

---

## Opening letter from our CEO

It is my pleasure to present you with the 2024 Global Automotive Cybersecurity Report.

Connectivity and software-defined architectures have been at the forefront of monumental changes in the Automotive and Smart Mobility ecosystem over the past several years, but as more functionality is being exposed, cybersecurity risks are growing dramatically.

This report, which marks Upstream’s sixth annual report, analyzes how Automotive and Mobility cybersecurity risks have evolved from experimental hacks to large-scale attacks, shifting the industry's focus to impact.

As predicted last year, automotive cybersecurity is reaching an inflection point. Cyber incidents have grown significantly in risk and impact, threatening safety and carrying operational implications. With threat actor motivation shifting towards large-scale impact on mobility assets, stakeholders across the ecosystem must also evaluate the potential financial implications of cybersecurity incidents.

Over the last year, the Automotive and Smart Mobility ecosystem adopted new standards and collaborated with regulators around the world on how to adapt future regulations to keep connected and software-defined assets secure. We’ve also been busy preparing for the upcoming second milestone of UNECE WP.29 R155, scheduled to take effect in July 2024, increasing its scope to all new vehicles.

2023 was the year of the GenAI revolution. GenAI is increasingly used by threat actors to introduce scale and new attack methods. But, in the coming months and years GenAI will also transform automotive cybersecurity tools and workflows and introduce unprecedented efficiencies to vSOC teams.

This inflection point illustrates the progress that adversaries continue to make, and reaffirms our commitment as an industry to continually innovate and deliver secure automotive and smart mobility experiences.

Upstream has led the effort to secure connected vehicles and mobility assets since 2017, when we first introduced the Upstream Platform, which proved to be a fundamental, innovative pillar in the automotive cybersecurity technology stack.

We've been helping some of the world's leading Automotive and Smart Mobility organizations—OEMs, suppliers, mobility IoT vendors, fleets and mobility service providers—comply with cybersecurity regulations and protect millions of vehicles and mobility assets.

With advanced cybersecurity tools and knowledge at our disposal, we are well-equipped to overcome the challenges in 2024 and ahead.

Best regards,

Yoav Levy
Co-Founder & CEO

---

## Methodology

The Automotive industry relies on Upstream's continuously updated database of cybersecurity incidents.

To compile this comprehensive report, Upstream researchers investigated over 1468 incidents, some as early as 2010, and monitored hundreds of deep and dark web forums to compile this comprehensive, actionable report that will help you safely navigate the year ahead.

Upstream monitors and analyzes worldwide automotive cyber incidents to learn, understand, and help protect the entire Smart Mobility ecosystem from existing and emerging threats.

Upstream’s AutoThreat®¹ cyber threat intelligence platform uses advanced technology and automation tools to constantly search all layers of the web for new cyber incidents in the automotive ecosystem and index them to the AutoThreat® platform.

Our researchers and analysts carefully categorize and analyze the data we collect to gain a deeper understanding of cyber threats, adversaries' motivation and activities, and their impact on mobility assets.

Each incident and relevant contextual data—such as the attack's geolocation, impact, attack vector, company type, and required proximity of the attacker to its target—are added to the platform to create an accurate and actionable repository.

Incidents examined in this report were sourced from the media, academic research, bug bounty programs, verified social media accounts of government law enforcement agencies worldwide, the Common Vulnerabilities & Exposures database, as well as other publicly-available online sources.

In addition to publicly reported cyber incidents, Upstream’s analysts monitor the deep and dark web for threat actors that operate behind the scenes of automotive-focused cyber attacks. These incidents are discussed in a separate chapter of this report titled "Threats from the Deep and Dark Web", and are excluded from statistics and charts in other chapters, unless indicated otherwise.

While every effort has been made to identify and analyze every reported automotive and smart mobility cyber incident, there may be additional attacks that have not been publicly reported, and therefore, have not been included in this report.

Select details of the publicly reported incidents are available in the AutoThreat® Intelligence Cyber Incident Repository. Additionally, a comprehensive analysis is available to AutoThreat® PRO² customers.

---

## Executive Summary

Connectivity is continuing to transform the Automotive and Smart Mobility ecosystem, increasing cybersecurity risks as more functionality is exposed. 2023 marked the beginning of a new era in automotive cybersecurity. Each attack carries greater significance today, and may have global financial and operational repercussions for various stakeholders. Upstream's 2024 Global Annual Cybersecurity Report examines how cybersecurity risks have evolved from experimental hacks into large-scale risks, focusing on safety and trust, operational availability, data privacy, and financial implications.

In 2023, Automotive and Mobility cybersecurity witnessed a dramatic shift toward large-scale incidents

- 95% of attacks were remote
- 64% of attacks were executed by black hat actors

The proportion of incidents with a “High” or “Massive” impact dramatically doubled from 2022 to 2023, accounting for nearly 50% of all incidents.

Threat actors motivation has also shifted towards scale and massive impact

- 65% of deep and dark web cyber activities had the potential to impact thousands to millions of mobility assets.
- 37% of deep and dark web cyber activities had the potential to impact multiple stakeholders, on a global scale.

OEMs take a multifaceted approach to protecting connected and software-defined vehicles, as well as IoT/OT assets

- With frequent OTA updates, the SBOM is no longer static—but rather constantly evolving, long after a vehicle leaves the factory—and risk profiles continuously change.
- The growing reliance on backend systems highlights the urgent need for OEMs to safeguard both the software components and sensitive data.
- GenAI has the potential to transform automotive cybersecurity solutions and operations, enabling agile investigations, automating vSOC workflows, and even generating complex insights based on deep and dark web data and in-depth TARA.

---

## Chapter 1: The automotive cybersecurity inflection point

### Analyzing the potential scale of automotive cyber risks

Automotive cybersecurity threats have evolved rapidly in a very short span of time. In 2015, Charlie Miller spent three years—from research to exploit—to hack the safety-critical in-vehicle network of a single vehicle.⁴ In 2023, a team of security researchers spent a mere few months hacking over a dozen different car makers. The team hacked telematic systems, automotive APIs, and the infrastructure that supports them. They discovered numerous vulnerabilities that allowed them to remotely impact the command & control of vehicles and access sensitive OEM and consumer data.⁵

In 2023, automotive cybersecurity witnessed a dramatic shift toward large-scale incidents.

1 VEHICLE
2015

MILLIONS
OF VEHICLES
2023

It’s important to note that when analyzing scale, the focus is on potential impact. It is impossible to assess the exact impact of each incident based on publicly reported information.

Upstream analyzed publicly disclosed automotive cybersecurity incidents between 2021 and 2023 according to the potential scale of impacted mobility assets, including vehicles, users, mobility devices and more. Upstream’s analysis categorized incidents according to four levels of impact—starting from “Low”, which includes incidents that have the potential to impact under 10 assets, up to “Massive”, which includes incidents that have the potential to impact millions of mobility assets.

Breakdown of publicly disclosed cybersecurity incidents by potential scale, 2023

| Number of Mobility Assets Potentially Impacted | 2021  | 2022  | 2023  |
| :--------------------------------------------- | :---- | :---- | :---- |
| LOW (Up to 10)                                 | 42.5% | 40.4% | 35.9% |
| MEDIUM (Up to 1,000)                           | 36.7% | 37.5% | 44.1% |
| HIGH (Thousands)                               | 19.6% | 20.6% | 14.6% |
| MASSIVE (Millions)                             | 1.2%  | 1.5%  | 5.4%  |

IN 2023 THE PROPORTION OF INCIDENTS WITH A “HIGH” OR “MASSIVE” IMPACT DRAMATICALLY DOUBLED TO NEARLY 50%

During both 2021 and 2022, “High” or “Massive” (potential to impact thousands-million of mobility assets) incidents accounted for approximately 20% of total incidents. But, in 2023, the proportion of incidents with a “High” or “Massive” impact dramatically doubled to nearly 50%.

Overall, the number of "Medium" scale attacks, which have the potential to impact up to 1,000 vehicles and mobility assets, has remained constant over the last three years. But the number of low-scale attacks has gone down dramatically in 2023 due to the emergence of new attack vectors that enable hackers to gain control over many more vehicles and assets with lower thresholds of knowledge and resources.

To illustrate the operational disruption impact of cyber attacks on mobility service providers consider an attack which occurred in September 2023. A leading US-based trucking and fleet management solutions provider experienced a ransomware attack that resulted in customers being unable to electronically log their on-road hours—as required by federal regulations—or track their transported inventory.⁶

In response, the company hired external cybersecurity experts to investigate the attack and applied for a waiver from the US Federal Motor Carrier Safety Administration to allow truckers to use paper logs until service was restored.⁷

Almost three weeks passed before the company was able to resolve the issue, causing serious operational disruption for thousands of truck drivers, fleet operators, and inventory management teams.

### Threat actors motivation has also shifted towards scale and massive impact

In addition to incidents disclosed in the media (clear web), it’s critical to assess the impact of deep and dark cyber activities and the incentives driving threat actors. Based on Upstream’s analysis of deep and dark web automotive cybersecurity activities, analyzing the 300 most active threat actors, nearly half of the activities (48%) were targeting more than one OEM or automotive supplier, and 37% had the potential to impact mobility assets across many stakeholders on a global scale.

In 2023, nearly 65% of deep and dark web cyber activities had the potential to impact thousands to millions of mobility assets.

Breakdown of deep and dark web threat actor activities by scale, 2023

| Scale   | Percentage |
| :------ | :--------- |
| Low     | 10.7%      |
| Medium  | 24.7%      |
| High    | 59.7%      |
| Massive | 5.0%       |

Breakdown of deep and dark web threat actor targets, 2023

| Target                     | Percentage |
| :------------------------- | :--------- |
| Single OEMs / Stakeholder  | 10.7%      |
| Several OEMs / Stakeholders | 37.3%      |
| Global                     | 59.7%      |

When zooming in on black hat and fraud activities in the deep and dark web, the potential scale and areas of interest also indicate a rapidly growing risk. Currently, 67% of malicious activities (threat actors categorized as black hats and fraud operators) have a “High” or “Massive” impact (compared to 45% across all actors) and 58% of activities involve multiple OEMs or have a global reach (compared to 48% across all threat actors).

When analyzing the areas of interest, the impact of black hats and fraud operators continues to deepen.

- 13% of activities are focused on vehicle manipulation tools.
- 12% of activities are focused on gaining access to sensitive data and PII.
- Nearly 50% are related to vulnerability exploits.⁸

Black hat and fraud operators activities by potential scale, 2023

| Scale   | Percentage |
| :------ | :--------- |
| Low     | 8.9%       |
| Medium  | 23.7%      |
| High    | 59.3%      |
| Massive | 8.1%       |

Black hat and fraud operators activities targets, 2023

| Target                     | Percentage |
| :------------------------- | :--------- |
| Single OEMs / Stakeholder  | 10.4%      |
| Several OEM's / Stakeholders | 41.5%      |
| Global                     | 48.1%      |

Black hat and fraud operators activities areas of interest, 2023

| Area of Interest      | Percentage |
| :-------------------- | :--------- |
| Vulnerablilty Exploits | 49.5%      |
| Diagnostic Software   | 19.3%      |
| Vehical Manipulation Tools | 12.6%      |
| PII                   | 11.9%      |
| Car Hacking Manuals   | 6.7%       |

### The financial perspective: the rising cost of cyber attacks on the Automotive and Smart Mobility ecosystem

Automotive and Smart Mobility cyber attacks have severe financial repercussions leading to recalls or OTAs, production shutdowns, ransomware payments, and vehicle thefts. Additional repercussions include data and privacy breaches, which can damage a brand's reputation and customer trust and can eventually lead to large regulatory fines and diminishing revenue.

Given the shift toward large-scale cybersecurity incidents—with nearly 50% of incidents in 2023 impacting thousands-millions of mobility assets⁹—it’s crucial for vehicle security operations center (vSOC) teams to analyze the financial impact of these incidents.

In June 2023, a leading Taiwan-based semiconductor manufacturer disclosed a cybersecurity incident involving a ransomware group and one of its IT hardware suppliers, which led to the leakage of information pertinent to initial setup and configuration of the system.¹⁰ The attackers claimed to gain access to internal documents with confidential information, demanding a $70 million ransom to decrypt the data and prevent its release online—making it the largest known ransom demand in history. While the breach could affect multiple automotive stakeholders, the company reported that neither its business operations nor customer information were affected by the cyber incident at its supplier. The company also immediately terminated its data exchange with this supplier following the incident.

In November 2023, a large Australian automotive group with 12 dealerships and hundreds of employees was attacked by the same ransomware group, who stole more than 50 GB of sensitive customer and internal data. Over 91,000 files were stolen, including payroll information, lease agreements, payout information, service quotes, invoices, crash assistance forms, CRM data, registration paperwork, and employee driver and motor vehicle sales licenses. The stolen files were published at the end of November, after the ransom deadline had expired.¹¹

#### Analyzing the financial impact of a cybersecurity incident

Trying to quantify the safety, privacy, and financial risks of automotive cybersecurity incidents is no small feat. The potential impact of automotive cyber threats is significant and can pose risks to the safety of drivers and passengers, disrupt business operations, compromise data privacy, and result in financial losses for OEMs as well as the entire supply chain.

In the next two illustrations we will analyze two incidents that occurred in 2023 and suggest a financial impact model, based on publicly available information.

The goal of this framework is to highlight the massive financial impact of cybersecurity risks.

This analysis doesn’t intend to be definitive, but rather a framework for estimating a range of potential financial risks.

#### Key Financial Implications of Automotive Cyber Threats

| Impact                           | Description