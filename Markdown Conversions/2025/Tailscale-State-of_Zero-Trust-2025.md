# The State of Zero Trust 2025

## Table of Contents
- [Introduction](#00-introduction)
- [Data transparency](#01-data-transparency)
- [Executive summary](#02-executive-summary)
- [The push toward identity-native access](#03-the-push-toward-identity-native-access)
- [Legacy VPNs](#04-legacy-vpns)
- [Productivity vs. security](#05-productivity-vs-security)
- [Security trends and the road ahead](#06-security-trends-and-the-road-ahead)
- [What’s next](#07-whats-next)
- [Recommendations](#08-recommendations)

---

## 00// Introduction
_from Avery Pennarun, CEO of Tailscale_

It’s 2025, and the perimeter is dead.

If your mental model of a secure network still involves “inside” and “outside,” it’s time for an update. Most companies know this — at least, they say they do. Our latest survey suggests Zero Trust has become the new checkbox buzzword. Unfortunately, saying “Zero Trust” and actually doing it are two very different things.

These are my three takeaways from the data:

**everyone's frustrated**
IT teams are overwhelmed by tool sprawl and manual processes. Security leaders are stuck enforcing policies users constantly work around. Engineers just want to get things done — and they say current access setups are too slow, too fragile, and too painful. Different problems, same conclusion: the legacy model isn’t working.

**zero trust is half-deployed at best**
Nearly every organization says they’re “on a Zero Trust journey,” which is a polite way of saying they aren’t done, and maybe never will be. Fewer than a third have implemented the foundational parts — strong identity, least privilege, and verifying before trusting. It’s a journey, sure — but one where most teams don’t have a map, the GPS is glitchy, and someone in the back is asking if we’re there yet.

**there's some light at the end of the tunnel**
There’s real interest in emerging approaches: identity-first networking, modular security systems, and policy engines that adapt (instead of break) when things change. And with AI accelerating both innovation and risk, there’s new urgency to get access right — not just for users, but for services, agents, and infrastructure itself.

This report isn’t about adding more buzzwords — it’s about creating a clear baseline of where the industry really stands on Zero Trust today. We hope it helps surface the biggest gaps, highlight emerging practices that are actually working, and offer practical direction for where secure access goes next.

---

## 01// Data transparency

All statistics and insights in this report are based on Tailscale’s 2025 Secure Access and Zero Trust Adoption Survey, conducted with 1,000 IT, security, and engineering professionals. 

### Methodology
Tailscale conducted this study in partnership with Kelsey White and PureSpectrum. The online survey was completed by n=1,000 engineering, security, development, and IT professionals across the United States and Canada. Management-level employees comprised about two-thirds of the sample, including twenty-three percent from the C-suite. Data was collected from April 21 to 28, 2025.

![Chart showing survey respondents by seniority: 6% entry-level, 6% mid-level, 8% senior-level, 7% team lead, 26% manager, 23% executive (C-level or VP), 24% director]

---

## 02// Executive summary

### Zero Trust in theory, not in practice
In 2025, organizations are under pressure to secure increasingly distributed, hybrid, and cloud-native environments — but the tools they rely on are frustrating and outdated (especially VPNs). 

### Access and connectivity redesign priorities
![Chart showing redesign priorities: 49% stronger security, 45% increased speed/performance, 38% scalability, 33% cost savings, 32% better UX/UI, 30% integration, 26% automation, 25% better access controls/visibility]

*   **99%** of companies want to redesign their access and connectivity approach.
*   **Only 1%** report being satisfied with the status quo.

### Key Findings
*   **Fewer than a third** of organizations use identity-based access as their primary model.
*   **68%** of organizations still rely on manual provisioning for network access.
*   **92%** of organizations are juggling multiple solutions for network security.
*   **83%** of respondents have bypassed security processes.
*   **68%** of respondents report retaining access to former employers’ systems after leaving.
*   **42%** say their security and access model will be outdated within two years.

---

## 03// The push toward identity-native access

Identity-native security — where access to systems is determined by user and device identity, not by network location — has become a pillar of Zero Trust. However, many organizations still operate in a hybrid mode, layering identity on top of a network-centric foundation.

### Reasons for delaying or deprioritizing networking or security upgrades
*   **42%** risk of disruption to workflows or integrations.
*   **39%** leadership or organizational priorities.
*   **35%** cost or resource constraints.
*   **34%** recent or ongoing rollout of other tools.
*   **33%** unclear business case or uncertain ROI.

---

## 04// Legacy VPNs

Virtual Private Networks (VPNs) are no longer fit for purpose. They are slow, brittle, and overly permissive.

### Current VPN limitations
*   **40%** Security risks
*   **35%** Latency/speed issues
*   **34%** High ops overhead
*   **28%** Integration challenges
*   **25%** Inability to scale
*   **24%** Throughput issues
*   **23%** Employee complaints

---

## 05// Productivity vs. security

Security and productivity are co-dependent. Rigid controls lead to workarounds, and bad user experience is a security risk.

*   **32%** of IT and security professionals say their top challenge is balancing security with speed and productivity.
*   **31%** cite enforcing IT rules and dealing with unauthorized tools.
*   **48%** of companies are actively trying to consolidate tools.

---

## 06// Security trends and the road ahead

In the next year, we predict enterprise organizations will measure Zero Trust maturity by how well they cover all pillars (identity, devices, network, applications, data) in an integrated way.

*   **Automation and AI:** Moving away from binary, rule-based access toward risk-aware, context-sensitive decisions (Continuous Adaptive Trust).
*   **The Knowledge Gap:** 55% of respondents expressed skepticism or said they didn’t know where to look for better solutions.

---

## 07// What’s next

1.  **Identity will become the foundation:** Identity is the new perimeter.
2.  **Implicit trust will disappear:** Every access, whether human or service, will be authenticated.
3.  **VPNs will be redefined:** Shift toward peer-to-peer and mesh architectures.
4.  **AI will power both defense and attack:** Defenders must evolve faster than automated adversaries.
5.  **Security will become part of engineering culture:** Security policies will be designed with UX in mind.

---

## 08// Recommendations

1.  **Develop an identity-first access strategy:** Audit systems and integrate with a central identity provider.
2.  **Accelerate VPN replacement plans:** Pilot a Zero Trust Network Access (ZTNA) solution.
3.  **Tighten onboarding/offboarding:** Establish a zero-tolerance policy for ex-employees retaining access.
4.  **Consolidate and integrate tools:** Reduce complexity by retiring overlapping security tools.
5.  **Improve user experience:** Security should be mostly invisible.
6.  **Enable and educate:** Set up an internal Security Champions program.
7.  **Implement Just-In-Time (JIT) and least privilege access:** Do not grant standing access unless necessary.
8.  **Boost monitoring:** Strengthen monitoring of access patterns and alert systems.
9.  **Plan for scalability:** Prefer cloud-delivered services that scale automatically.
10. **Align with a Zero Trust framework:** Use NIST 800-207 or CISA’s Zero Trust Maturity Model to track progress.