# 2025 US Cyber Industry Exposure Database and Loss Curve

A collaboration between Guidewire Cyence and Guy Carpenter

## Introduction

The cyber landscape has been rapidly changing throughout 2025. US federal deregulation and defunding of key cyber agencies, nation-state cyber activity, and ongoing foreign wars: these developing conditions create new uncertainty and present new opportunities for cyber attackers to capitalize on the uncertainty.

For example, recent reductions in US federal oversight over security standards for large cloud providers presents the opportunity for such providers to decrease resource allocation toward security protocols or vulnerability remediation, both previously standard practices in the industry.

Nevertheless, large cloud providers may also benefit from any newly freed resource, potentially accelerating R&D velocity with fewer regulatory obligations. It is entirely possible that this improved velocity on network security innovation would outweigh the vast reduction of federally established protocols. However, the ultimate impact of these procedural adjustments cannot easily be measured: in all likelihood, deregulation impacts on security will overtake efficiency benefits, at least in the short term. Therefore, it can be considered that the general 2025 cyber industry landscape is at a higher risk level than in 2024.

In response to this tumultuous moment in time, financial and insurance markets require a fresh estimate of industry cyber exposure. In this spirit, Guidewire Cyence (Cyence) and Guy Carpenter (GC) are releasing a newly constructed, fully unique and up-to-date US Cyber Industry Exposure Database and Loss Curve (IED).

The IED satisfies a number of use cases, including market exposure measurement, aggregation benchmarking, data supplement and support, and various risk transfer vehicle calculations. Cyence and GC plan to maintain this collaboration with regular updates, new version releases, and additional functionality for the IED product beyond 2025, including the expansion from US to a global view. This paper will explore Cyence and GC opinions on market conditions, showcase IED statistical outputs, and provide a step-by-step walkthrough of our IED build logic.

We abide by the principle of full transparency: a single numerical curve without insight into its construction should not be sufficient justification to trust a model. Thus, our goal with this paper is to encourage deeper discussions not only on the technical findings, but also any potential areas for improvement in future iterations, to garner trust and comfort in our collaborative solution. We look forward to this discussion.

## Table of Contents

The opening sections of this paper capture the main findings of the IED project and the general cyber landscape opinions shared across GC and Cyence. Readers who wish to examine IED build details can refer to the sections under “IED Methodology Detail.” Finally, we provide a preview of future IED iterations for successive Cyence model versions.

*   [Executive Summary and IED Results](#executive-summary-and-ied-results)
*   [Full 2025 Cyber Risk Landscape Commentary](#full-2025-cyber-risk-landscape-commentary)
*   [Methodology Detail](#methodology-detail)
    *   [A) Define IED Form and Scope](#a-define-ied-form-and-scope)
    *   [B) Development of IED US Policy Population](#b-development-of-ied-us-policy-population)
    *   [C) GC Average Policy Terms](#c-gc-average-policy-terms)
    *   [D) Cyence Model 7 Baseline Population Universe](#d-cyence-model-7-baseline-population-universe)
    *   [E) Testing: Written Premium, Loss Ratio, Ground-Up vs. Gross Loss](#e-testing-written-premium-loss-ratio-ground-up-vs-gross-loss)
    *   [F) Cyence Model 7 IED Tail Event Sets](#f-cyence-model-7-ied-tail-event-sets)
    *   [G) Reflecting Cyence Universe Cat Tail Across US Population](#g-reflecting-cyence-universe-cat-tail-across-us-population)
*   [Cyence Model 8 and Future Iterations of IED](#cyence-model-8-and-future-iterations-of-ied)
*   [Closing Remarks](#closing-remarks)
*   [Contributors](#contributors)

## Executive Summary and IED Results

As expounded upon later in the “Define IED Form and Scope” section, an Industry Loss Curve is fundamentally an ascending curve of possible extreme cyber loss scenarios, each assigned a unique likelihood. In this case, the Cyence and GC loss curve results include sets of both the largest event per simulation years (“Occurrence Exceedance Probabilities” or “OEP”), and total annual loss years (“Aggregate Exceedance Probabilities” or “AEP”). Other cyber risk metrics are also included in the analysis, but some high-level benchmark statistics from our analysis can be summarized as follows:

|                                        | US Cyber Market Insurance Results ($B) | Projected US Annual Written Premium | Projected US Cyber Industry Loss Ratio | Note