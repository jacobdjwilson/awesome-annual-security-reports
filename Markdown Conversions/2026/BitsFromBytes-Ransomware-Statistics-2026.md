# Ransomware Statistics 2026: Attacks, Costs, and the 70-to-1 Ratio Nobody Talks About

**BitsFromBytes Research**  
May 27, 2026

## Table of Contents
- [Ransomware Statistics 2026](#ransomware-statistics-2026)
- [Attack volume: how bad did 2025 actually get?](#attack-volume-how-bad-did-2025-actually-get)
- [The cost numbers: payments, recovery, and total damage](#the-cost-numbers-payments-recovery-and-total-damage)
  - [Ransom payments vs. total damage](#ransom-payments-vs-total-damage)
  - [Individual incident costs](#individual-incident-costs)
  - [Industry cost comparison](#industry-cost-comparison)
- [The 70-to-1 ratio: why payment behavior is the wrong metric](#the-70-to-1-ratio-why-payment-behavior-is-the-wrong-metric)
- [Attack vectors: how ransomware actually gets in](#attack-vectors-how-ransomware-actually-gets-in)
- [The active threat groups in 2026](#the-active-threat-groups-in-2026)
- [The AI acceleration](#the-ai-acceleration)
- [Notable incidents of 2025](#notable-incidents-of-2025)
- [Law enforcement impact: what the takedowns actually changed](#law-enforcement-impact-what-the-takedowns-actually-changed)
- [Ransomware statistics at a glance: reference table](#ransomware-statistics-at-a-glance-reference-table)
- [Frequently asked questions](#frequently-asked-questions)

---

## Ransomware Statistics 2026

Ransomware payments fell to $813 million in 2024. Total ransomware damages that year reached approximately $57 billion. That’s a ratio of roughly 70 to 1: for every dollar a victim hands over in ransom, ransomware generates approximately $70 in total economic damage across the victim ecosystem — downtime, recovery, legal exposure, regulatory fines, and reputational loss.

This ratio doesn’t appear in any single industry report. It’s a cross-source calculation, and it reframes the entire ransomware conversation. Most coverage focuses on payment behavior — who paid, how much, whether payment rates are rising or falling. That lens is useful but narrow. The story in 2025–2026 data is that ransomware has industrialized past the point where any single metric captures its impact. Attack volume up 58%. Payment rates down to record lows. Active gang count up 40%. Total damage climbing toward $57 billion annually. All of those things are simultaneously true.

This article compiles the most authoritative ransomware data available as of April 2026 — sourced directly from the Verizon DBIR, FBI IC3, Sophos, IBM, Chainalysis, and CrowdStrike — with the numbers that let you understand the real scale, not just the headline payment figures.

---

## Attack volume: how bad did 2025 actually get?

Over 7,000 organizations were publicly identified as ransomware victims on dark web leak sites in 2025, with some tracking services reporting figures above 7,500 — representing a 58% year-over-year increase from approximately 4,750 in 2024, according to GuidePoint Security and DarkOwl tracking.

These are confirmed, publicly named victims. The actual count of ransomware incidents is substantially higher: many victims pay quietly, never disclose the attack, and never appear on a leak site. The leak-site figure is a floor, not a ceiling.

The Verizon 2025 Data Breach Investigations Report — which analyzed over 16,000 real-world security incidents — found ransomware present in 44% of all data breaches, a finding corroborated by TechTarget’s ransomware trends analysis, up from 32% the prior year. That is a 37.5% single-year increase in ransomware’s share of total breaches. Ransomware was involved in 75% of system-intrusion-pattern breaches specifically.

The FBI’s 2025 IC3 Annual Report, released April 6, 2026, documented 63 new ransomware variants identified in 2025 — approximately 5.25 new variants per month. The top active variants by impact on critical infrastructure: Akira, Qilin, RansomHub, LockBit, and Medusa.

Additional frequency benchmarks:
- Halcyon tracks 95 active ransomware gangs globally, a 40% increase year-over-year
- Approximately 15 organizations are victimized by ransomware daily, per Halcyon data
- U.S. ransomware incidents increased 50% in the first ten months of 2025 (5,010 incidents vs. 3,335 in 2024), per Cyble research
- 55 new ransomware-as-a-service (RaaS) families emerged in 2024, a 67% increase (Travelers Insurance)

**The critical infrastructure concentration:** Roughly half of all 2025 attacks targeted sectors underpinning modern economies — manufacturing, healthcare, energy, transportation, and financial services. Manufacturing alone saw a 61% year-over-year surge in attacks.

---

## The cost numbers: payments, recovery, and total damage

### Ransom payments vs. total damage

Total cryptocurrency payments to ransomware operators reached approximately $813 million in 2024 (down 35% from the 2023 record of $1.1 billion), per Chainalysis blockchain transaction analysis. Preliminary 2025 data tracks near the same level (~$820 million).

Total global ransomware damages in 2025 are estimated at approximately $57 billion annually, per Cybersecurity Ventures modeling. The $57 billion figure includes ransom payments, downtime losses, recovery costs, legal and regulatory exposure, and reputational damage — not ransom alone.

The derived ratio: $57B total damage ÷ $813M ransom payments = approximately 70x. For every dollar paid in ransom, the broader ransomware ecosystem generates roughly $70 in total economic harm. This is why payment refusal — while often the correct tactical decision — doesn’t solve the ransomware problem. The damage is already largely done before the ransom demand is issued.

### Individual incident costs

IBM’s Cost of a Data Breach 2025 report — the same report used in our data breach statistics 2026 analysis — found the average cost of a ransomware breach reached $5.08 million — higher than the overall average data breach cost of $4.44 million and reflecting the operational disruption component unique to ransomware.

Sophos’ State of Ransomware 2025 report — based on a survey of 5,000 IT/cybersecurity professionals across 14 countries — provides the most granular breakdown of what organizations actually pay versus what they report:

| Metric | 2024 | 2025 | Change |
| --- | --- | --- | --- |
| Median ransom demand | $2 million | $1.32 million | −34% |
| Average ransom payment | $2 million | $1 million | −50% |
| Median actual payment | $150,000 | $115,000 | −23% |
| Average recovery cost (excl. ransom) | — | $1.53 million | −44% from prior year |
| % who negotiated lower than demand | — | 53% | — |
| % who paid exact demand | — | 29% | — |

The gap between demand ($1.32M median) and actual payment ($115K median) reflects aggressive negotiation. 53% of organizations that paid ransoms in 2025 negotiated a lower amount than the initial demand. The negotiation is real and the outcome is material.

**Healthcare costs a category of their own:** The IBM data shows healthcare remains the most expensive industry for breaches at an average of $7.42 million per incident in 2025 — for the broader data breach context, see our cybersecurity statistics 2026 overview — down from $9.77 million in 2024, but still 2.5x the global average, and the most expensive sector for the 15th consecutive year.

### Industry cost comparison

| Industry | Average breach cost (IBM 2025) | Ransomware prevalence |
| --- | --- | --- |
| Healthcare | $7.42 million | Highest regulatory exposure |
| Financial services | $6.08 million | High |
| Critical infrastructure | $4.82 million | Rising rapidly |
| Education | $3.80 million | High; 66% of K-12 districts have no cybersecurity staff |
| Global average (all sectors) | $4.44 million | 44% of all breaches (Verizon) |

---

## The 70-to-1 ratio: why payment behavior is the wrong metric

This is the analytical frame that most ransomware coverage misses.

Payment refusal rates hit a record: 64% of ransomware victims refused to pay in 2025, up from 59% in 2024, per Verizon DBIR 2025. That sounds like progress. Organizations are more resilient, backups are better, recovery is faster. Law enforcement disruption of groups like LockBit and ALPHV/BlackCat in 2024 contributed to payment refusal by demonstrating that payments don’t guarantee data deletion or decryptor delivery.

But victim counts rose 58% in the same period. Refusal doesn’t prevent the attack — it changes the cost structure. An organization that refuses to pay still incurs:
- Average recovery cost: $1.53 million (Sophos)
- Average downtime cost: documented in the billions cumulatively across sectors
- Regulatory exposure: particularly in healthcare (HIPAA) and finance (SEC incident disclosure rules)
- Reputational damage: quantified differently per sector

The decision not to pay is correct in most cases — it denies revenue to ransomware operators and avoids funding future attacks. But framing it as a “win” while victim counts climb 58% creates false confidence. The $57 billion in total damage isn’t primarily driven by ransom payments ($813M). It’s driven by everything else.

97% of organizations with encrypted data were able to recover it in 2025, per Sophos — via backups, decryption tools, or payment. That’s a resilience improvement. But recovery capability doesn’t reverse the cost of 22+ days of operational disruption (the average downtime per incident) or the liability exposure from exfiltrated data.

---

## Attack vectors: how ransomware actually gets in

Understanding the initial access vectors matters more than the ransom statistics for defense planning. Sophos State of Ransomware 2025 documents the 2025 distribution:

| Initial vector | 2025 share | Change from 2024 |
| --- | --- | --- |
| Exploited vulnerabilities | 32% | Most common; rising |
| Compromised credentials | 23% | Down from 29% |
| Phishing | 18% | Up from 11% |
| Other/unknown | 27% | — |

Vulnerability exploitation overtook compromised credentials as the leading initial access vector — a shift driven primarily by edge device vulnerabilities: VPNs, firewalls, and network gateways exposed to the internet by design. Our VPN security statistics 2026 article covers the 82.5% growth in VPN CVEs that contributes directly to this attack surface. The Verizon 2025 DBIR documented a shocking compression of the exploitation timeline: for new critical vulnerabilities affecting edge devices, the median time between vulnerability publication and mass exploitation by attackers was zero days. Attackers were weaponizing CVEs before defenders could patch them.

CrowdStrike’s 2025 Global Threat Report added the most structurally concerning finding: 79% of initial access attacks are now malware-free — relying instead on stolen credentials, legitimate remote management tools, and living-off-the-land techniques that bypass traditional endpoint detection. The implication: organizations running antivirus and EDR as their primary detection layer are invisible to the majority of ransomware intrusions until the encryption event itself. Our best endpoint security software guide covers detection tools designed for this credential-based threat model.

Access broker advertisements on dark web forums increased 50% year-over-year (CrowdStrike 2025). The RaaS economy has separated the “initial access” function from the “ransomware deployment” function — specialists sell network footholds to ransomware operators, enabling less technically sophisticated groups to run sophisticated attacks.

**The dwell time compression:** The median time from initial intrusion to ransomware execution fell from 9 days in 2022 to 5 days in 2025 (Sophos). Attackers are deploying faster to reduce detection windows. 63% of attackers still go undetected for up to 6 months before deploying ransomware, per Fortinet’s ransomware statistics research — using dwell time to map networks, disable security controls, and exfiltrate data before triggering encryption.

90%+ of ransomware attacks that reached the ransom stage originated from unmanaged devices (Microsoft 2024 data). Personal devices, unregistered IoT hardware, and contractor-owned machines are the primary entry point for the attacks that actually complete.

---

## The active threat groups in 2026

The FBI IC3 2025 report named five dominant variants by impact on critical infrastructure: Akira, Qilin, RansomHub, LockBit, and Medusa.

The landscape is notable for its turnover. LockBit was disrupted by international law enforcement in February 2024, its infrastructure seized and affiliates arrested — yet variants continue operating and LockBit remains among the top five by FBI count. The disruption degraded but did not eliminate the operation. This pattern repeats: ALPHV/BlackCat was disrupted in December 2023 and March 2024, yet its affiliates largely migrated to RansomHub.

Qilin emerged as the fastest-growing operation: carrying out 81 attacks in June 2025 alone, a 47.3% month-over-month rise. Dragonforce surged by 212.5% in attack volume. The market is consolidating around fewer dominant players while simultaneously producing new entrants constantly — the 63 new variants documented by the FBI in 2025 confirm that affiliate recruitment and RaaS tooling are outpacing law enforcement disruption.

**Double extortion is now the standard model:** 87.6% of ransomware claims involve both encryption and data exfiltration/threatened publication (Travelers Insurance). Organizations can restore from backups and still face extortion over stolen data. The “immutable backup solves ransomware” framing is obsolete — it solves encryption, not the extortion of exfiltrated data.

---

## The AI acceleration

The FBI IC3 2025 report documented AI use by cybercriminals for the first time in the report’s history. The IC3 received more than 22,000 complaints referencing AI-enabled attacks, with adjusted losses exceeding $893 million. FBI documentation specifically cited ransomware operators using AI to generate convincing phishing emails, synthetic video content, and voice cloning to enable initial access.

Broader research puts the AI exposure higher: an MIT study of 2,800 incidents found 80% of 2025 ransomware attacks leveraged AI tools — from deepfake phone calls to AI-generated phishing campaigns. 82.6% of phishing emails in 2025 contained AI-generated content (KnowBe4). 41% of ransomware families examined include AI-driven components to adapt payloads and evade defenses.

The defensive implication is direct: AI-generated phishing emails now achieve click rates of approximately 54% — matching human-crafted spear phishing at roughly 95% lower operational cost for the attacker (Harvard Business Review research, 2024). Organizations running user awareness training as their primary phishing defense are facing a different cost curve than they were two years ago.

---

## Notable incidents of 2025

- **Change Healthcare** — The most significant single ransomware event in recent history. Initially reported in February 2024 as affecting over 100 million individuals, by mid-2025 the confirmed breach victim count had reached 193 million — the largest healthcare data exposure ever recorded in the United States. The ALPHV/BlackCat group was responsible; UnitedHealth Group paid a reported $22 million ransom, then faced re-extortion from a splinter group.
- **PowerSchool** — A December 2024 ransomware attack on K-12 education software provider PowerSchool exposed data on 62 million students and 9.5 million teachers across North America.
- **Yale New Haven Health** — A March 2025 attack compromised data on approximately 5.6 million patients. An $18 million class-action settlement was announced in October 2025.
- **Marks & Spencer** — The London-based retailer’s May 2025 attack by the Pay2Key group caused operational disruption severe enough that the company disclosed its pre-tax profit fell 90% in a six-month period.
- **DaVita** — One of the largest U.S. kidney care providers was attacked in April 2025 by the Interlock group, exposing personal and health information on 2.7 million individuals.
- **NASCAR** — The Medusa ransomware gang attacked in April 2025, stealing more than 1 terabyte of sensitive data and demanding a $4 million ransom.

---

## Law enforcement impact: what the takedowns actually changed

The 2024 LockBit disruption (Operation Cronos, February 2024) and ALPHV/BlackCat seizure provided the most visible proof to date that coordinated international law enforcement can meaningfully damage ransomware infrastructure. The FBI, Europol, UK NCA, and other agencies seized LockBit’s decryption keys, arrested affiliates, and published the names of its administrators.

The measurable effect: LockBit’s attack volume dropped sharply in Q1 2024. The immeasurable counterfactual: RansomHub and other groups absorbed the displaced affiliates within months, and total attack volume continued rising through 2025.

IBM’s research shows organizations that involve law enforcement in ransomware incidents save an average of $990,000 per breach ($4.38M average cost with law enforcement vs. $5.37M without) — an 18% cost reduction for an action that carries no fee. In 2024, 63% of ransomware victims that involved law enforcement avoided paying ransom at all (FBI IC3).

The CISA StopRansomware advisory portal publishes active threat group intelligence, indicator-of-compromise feeds, and mitigation guidance for each major ransomware family. NIST’s Cybersecurity Framework 2.0 maps ransomware controls across its five functions — Identify, Protect, Detect, Respond, and Recover — and is the reference framework most US federal agencies now use for incident response planning. For any organization hit by ransomware, reporting to both CISA and FBI IC3 triggers the law enforcement engagement that produces the $990K average saving. For practical Zero Trust architecture guidance that addresses the edge device vulnerability problem driving 32% of initial access, see our VPN speed and privacy awards 2026 article, which covers the enterprise transition away from legacy VPN.

---

## Ransomware statistics at a glance: reference table

| Metric | Figure | Source |
| --- | --- | --- |
| Ransomware present in all data breaches | 44% | Verizon DBIR 2025 |
| Year-over-year increase in ransomware’s share of breaches | +37.5% | Verizon DBIR 2025 |
| Organizations victimized on leak sites (2025) | 7,000–7,500+ | GuidePoint / DarkOwl |
| YoY increase in publicly named victims | ~58% | GuidePoint 2025 |
| Crypto ransom payments (2024) | $813 million | Chainalysis |
| Total ransomware damages (2025 est.) | ~$57 billion | Cybersecurity Ventures |
| Damage-to-payment ratio | ~70:1 | BitsFromBytes analysis |
| Average ransomware breach cost | $5.08 million | IBM 2025 |
| Healthcare breach cost (highest sector) | $7.42 million | IBM 2025 |
| Median ransom demand (2025) | $1.32 million | Sophos |
| Median actual payment (2025) | $115,000 | Verizon DBIR |
| Recovery cost average (excl. ransom) | $1.53 million | Sophos |
| Victims refusing to pay | 64% | Verizon DBIR 2025 |
| Active ransomware gangs | 95 | Halcyon |
| New RaaS families (2024) | 55 (+67% YoY) | Travelers Insurance |
| New ransomware variants (2025) | 63 | FBI IC3 2025 |
| Top entry vector | Exploited vulnerabilities (32%) | Sophos 2025 |
| Malware-free initial access attacks | 79% | CrowdStrike 2025 |
| Attacks involving double extortion | 87.6% | Travelers Insurance |
| Law enforcement cost saving per breach | ~$990,000 | IBM 2025 |
| AI-enabled attacks (2025) | 80% of incidents | MIT / Varonis |

---

## Frequently asked questions

### How many ransomware attacks happen per day in 2026?
Approximately 15 organizations are victimized by ransomware daily, per Halcyon tracking. US-specific data from Cyble recorded 5,010 ransomware incidents in the first ten months of 2025 — approximately 17 incidents per day in the US alone. These figures count confirmed, documented attacks; actual incident rates including unreported events are substantially higher.

### What is the average cost of a ransomware attack in 2026?
IBM’s Cost of a Data Breach 2025 report found the average ransomware breach costs $5.08 million — higher than the overall average breach cost of $4.44 million. This figure includes detection and escalation, notification, post-breach response, and lost business costs. It excludes ransom payment, which is separately negotiated. Healthcare incidents average $7.42 million per breach.

### Are ransomware payments going up or down?
Ransom payments are declining. The median actual payment fell from $150,000 in 2024 to $115,000 in 2025 (Verizon DBIR). Average payments fell 50% from $2 million to $1 million (Sophos). Total cryptocurrency payments to ransomware operators were $813 million in 2024, down 35% from 2023. However, total economic damage from ransomware continues rising — the decline in payments does not reflect declining attack impact.

### Which industries are most targeted by ransomware?
Manufacturing, healthcare, government, and financial services bear the highest attack volumes. Manufacturing saw a 61% year-over-year surge in 2025. Healthcare is the most expensive sector per incident at $7.42 million average. The FBI IC3 2025 report specifically names healthcare, manufacturing, and government facilities as the primary targets of the top five ransomware variants.

### What is ransomware-as-a-service (RaaS)?
RaaS is a model where ransomware developers provide tooling, infrastructure, and support to affiliate operators who run the actual attacks and share revenue with the developers. 55 new RaaS families emerged in 2024. The model enables less technically sophisticated actors to conduct sophisticated attacks, which is why 95 active ransomware gangs are now tracked — up 40% year-over-year.

### Should I pay a ransomware demand?
Most cybersecurity authorities advise against payment. 64% of victims refuse, and those who involve law enforcement before deciding save an average of $990,000 per breach (IBM 2025). Payment doesn’t guarantee decryption or data deletion — and in the double extortion model (87.6% of 2025 incidents), paying the ransom doesn’t prevent the stolen data from being published. CISA’s StopRansomware guidance recommends reporting to both CISA and FBI IC3 before making any payment decision.

### What is the fastest-growing ransomware group in 2025?
Qilin conducted 81 attacks in June 2025 alone — a 47.3% month-over-month increase — making it the most active single-month operator tracked by Cyfirma. Dragonforce saw the most dramatic percentage increase at 212.5% growth. RansomHub, which absorbed significant ALPHV/BlackCat affiliate migration following the 2024 law enforcement disruption of that group, is the most significant structural successor to LockBit as a dominant RaaS platform.

<!-- CONVERSION_METADATA: {"source": "https://github.com/jacobdjwilson/awesome-annual-security-reports", "date": "2026-10-10", "model": "gemini-3.8-flash"} -->
