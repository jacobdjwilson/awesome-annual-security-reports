# 2025 US Cyber Industry Exposure Database and Loss Curve

## Table of Contents
- [Executive Summary and IED Results](#executive-summary-and-ied-results)
- [Full 2025 Cyber Risk Landscape Commentary](#full-2025-cyber-risk-landscape-commentary)
- [Methodology Detail](#methodology-detail)
- [A) Define IED Form and Scope](#a-define-ied-form-and-scope)
- [B) Development of IED US Policy Population](#b-development-of-ied-us-policy-population)
- [C) GC Average Policy Terms](#c-gc-average-policy-terms)
- [D) Cyence Model 7 Baseline Population Universe](#d-cyence-model-7-baseline-population-universe)
- [E) Testing: Written Premium, Loss Ratio, Ground-Up vs. Gross Loss](#e-testing-written-premium-loss-ratio-ground-up-vs-gross-loss)
- [F) Cyence Model 7 IED Tail Event Sets](#f-cyence-model-7-ied-tail-event-sets)
- [G) Reflecting Cyence Universe Cat Tail Across US Population](#g-reflecting-cyence-universe-cat-tail-across-us-population)
- [Cyence Model 8 and Future Iterations of IED](#cyence-model-8-and-future-iterations-of-ied)
- [Closing Remarks](#closing-remarks)
- [Contributors](#contributors)

---

# WHITE PAPER
## 2025 US Cyber Industry Exposure Database and Loss Curve
A collaboration between Guidewire Cyence and Guy Carpenter

The cyber landscape has been rapidly changing throughout 2025. US federal deregulation and defunding of key cyber agencies, nation-state cyber activity and ongoing foreign wars: these developing conditions create new uncertainty, and present new opportunities for cyber attackers to capitalize on the uncertainty.

Guidewire Cyence and Guy Carpenter (GC) are releasing a newly constructed, fully unique and up-to-date US Cyber Industry Exposure Database and Loss Curve (IED). The IED satisfies a number of use cases, including market exposure measurement, aggregation benchmarking, data supplement and support, and various risk transfer vehicle calculations. Cyence and GC plan to maintain this collaboration with regular updates, new version releases and additional functionality for the IED product beyond 2025, including the expansion from US to a global view. This paper will explore Cyence and GC opinions on market conditions, showcase IED statistical outputs, and provide a step-by-step walkthrough of our IED build logic.

We abide by the principle of full transparency: a single numerical curve without insight into its construction should not be sufficient justification to trust a model. Thus, our goal with this paper is to encourage deeper discussions not only on the technical findings, but also any potential areas for improvement in future iterations, to garner trust and comfort in our collaborative solution. We look forward to this discussion.

---

## Executive Summary and IED Results

As expounded upon later in the “Define IED Form and Scope” section, an Industry Loss Curve is fundamentally an ascending curve of possible extreme cyber loss scenarios, each assigned a unique likelihood. In this case, the Cyence and GC loss curve results include sets of both the largest event per simulation years (“Occurrence Exceedance Probabilities” or “OEP”), and total annual loss years (“Aggregate Exceedance Probabilities” or “AEP”).

![Table of benchmark statistics including 1-in-100 loss, 1-in-250 loss, expected loss, projected US annual written premium, and projected US cyber industry loss ratio.]

*   Loss estimates from Cyence Model version 7: Premium statistics provided by GC
*   Estimated count of US Cyber Policies (primary): 4.97 million
*   Manufacturing, Financial Services and Retail Trade sectors have the largest presence in extreme tail events
*   12 month in-force affirmative cyber exposure data for analysis as of Q4 2024
*   *53% loss ratio is composed of attritional loss (42 percentage points) and cat loss (11 percentage points)

### OEP and AEP VaR (Value at Risk) curves
![Line chart showing OEP vs AEP tail beyond 1 in 50 return period.]

---

## Full 2025 Cyber Risk Landscape Commentary

There is volatility in the current cyber risk landscape. The volatility encompasses all sectors and sizes of businesses, as well as all targeted and mass attack strategies. Ransomware and Business Email Compromise (BEC) attacks remain persistent into Q1 2025. We expect BEC attack frequency to increase at least in the short term, as AI penetrates the attack landscape.

Cyber modelers and financial markets are all monitoring the conflict in Ukraine. If this conflict were to end in 2025, significant amounts of cyber-attack resources could be freed up to potentially renew attacks against other wealthy/insured nations. Furthermore, if US/Russia political tensions instead deteriorate over the next year, the US could expect heightened nation-state backing for potential attacks against US providers.

The other major cyber market shock the world is watching is the defunding of federal cyber security programs in the US. CISA (Cybersecurity and Infrastructure Security Agency) has seen its program reduced by $10M in annual funding and approximately 10% of its workforce. FedRAMP (Federal Risk and Authorization Management Program) initiatives to pursue AI-related measures have been scrapped in 2025. All elements point toward a more loosely regulated, potentially less secure digital environment.

---

## Methodology Detail

### A) Define IED Form and Scope
Characteristics of the IED project can be categorized as follows:
- **US Cyber-Insured Population**: Independent Cyence Loss + GC Exposures
- **Methodology**: Cyence Model Version 7 “Bottom-up” Model Approach
- **Output**: US Cyber Industry Loss Ratio + Written Premium Estimate; OEP / AEP per sim year, beyond 1 in 50 RP

### B) Development of IED US Policy Population
The base set of cyber-insured US businesses is constructed via the formula:
(Insured US Businesses) = (Count of Total US Businesses) * (Cyber Insurance Take-up Rates)

### C) GC Average Policy Terms
![Table showing average policy terms by revenue band including premium, limit, retention, and attachment.]

### D) Cyence Model 7 Baseline Population Universe
Cyence currently holds firmographic and technographic detail on a population of approximately 600,000 US businesses and subsidiaries. This set has been further refined to 200,000 for the purposes of this exercise.

### E) Testing: Written Premium, Loss Ratio, Ground-Up vs. Gross Loss
Total estimated written premium of $9.52B represents the US cyber market as of hypothetical Policy/Calendar year 2024.

### F) Cyence Model 7 IED Tail Event Sets
The Cyence model projects 11 accumulation paths to populate the OEP curve tail beyond the 1-in-50 year return period, including Hypervisor Outages, AWS/Azure Cloud Outages, and various OS-based Mass Ransomware deployments.

### G) Reflecting Cyence Universe Cat Tail Across US Population
Cyence uses a controlled scaling method to extrapolate US-insured population cat events. Scaling is uniquely applied per event, per revenue band and per sector to reflect individual characteristics of each event type and affected population.

---

## Cyence Model 8 and Future Iterations of IED
Cyence Model 8 will be released in phases over 2026, featuring:
- Full mapping of world industries via domain identification.
- Added event sets (SaaS/PaaS SPOFs, Mass Non-Malicious Software Update, Business Email Compromise).
- Global IED with geo-granularity.
- IED tracking of industry influences over time.

---

## Closing Remarks
We acknowledge the uncertainty surrounding a scaling exercise of this magnitude in the SME space, but we are confident that our extensive US market-share research across all tail contributing event paths can provide a reasonable and realistic collection of industry loss scenarios. The Cyence IED/ILC event set is fundamentally data-driven; there are no elements of event narrative present that have not been observed in history in some shape or form.

---

## Contributors
- **Brian Choi**, Lead Data Scientist, Guidewire Cyence
- **Maurizio Gobbato**, Head of Cyber Catastrophe Modeling, Guidewire Cyence
- **Jess Fung**, Managing Director – NA Cyber Analytics Lead, Guy Carpenter
- **Shu Iida**, Senior Vice President – Cyber Catastrophe Analytics, Guy Carpenter
- **Douglas Stromberg**, Director of Product Management, Guidewire Cyence
- **Ariel Yeung**, Principal Data Scientist, Guidewire Cyence

[^1]: https://www.verisk.com/4a25ed/siteassets/media/pcs/pcs-cyber-catastrophe-notpetyas-tail.pdf