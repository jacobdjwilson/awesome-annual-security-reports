# SANS 2025 Threat Hunting Survey: Advancements in Threat Hunting Amid AI and Cloud Challenges

## Table of Contents
- [Executive Summary/Introduction](#executive-summaryintroduction)
- [Plan the Hunt, Hunt the Plan—or Just Wing It?](#plan-the-hunt-hunt-the-planor-just-wing-it)
- [Worth It, or Just a Wild Goose Chase?](#worth-it-or-just-a-wild-goose-chase)
- [What Threat Hunting Is Catching in 2025](#what-threat-hunting-is-catching-in-2025)
- [Tracking Threat Actors in the Digital Wild West](#tracking-threat-actors-in-the-digital-wild-west)
- [DIY Threat Hunting—The Trend of Keeping It In-House](#diy-threat-huntingthe-trend-of-keeping-it-in-house)
- [Keeping Up with Evolving Threats](#keeping-up-with-evolving-threats)
- [The Roadblocks and Workarounds for Threat Hunts](#the-roadblocks-and-workarounds-for-threat-hunts)
- [Conclusion](#conclusion)

---

## Executive Summary/Introduction

The 2025 SANS Threat Hunting Survey marks a decade of tracking how organizations evolve their threat hunting capabilities. This year’s findings reinforce that threat hunting remains a critical function within security operations, with organizations prioritizing agility, methodology refinement, and better integration of intelligence sources. Although formal methodologies saw a slight decline, the trend toward structured approaches continues, indicating that organizations are balancing flexibility with repeatable processes.

One of the most significant shifts this year is the decline in organizations outsourcing their threat hunting, with more teams opting to build internal capabilities. This shift aligns with the broader push for in-house expertise, particularly in defining methodologies, collecting intelligence, and performing hunt missions. However, a shortage of skilled personnel remains a primary challenge, exacerbated by budget constraints, the increasing complexity of threat landscapes, and the persistent difficulties of cloud threat hunting. Visibility across cloud environments and hunting in diverse log sources continue to be pain points, alongside the struggle to normalize data across disparate security tools.

Organizations are continuing their focus on improving automation and AI-driven hunting, although the impact of AI-based techniques on uncovering threat actors remains limited. Despite this, organizations have a clear push to integrate AI into their processes, suggesting a strategic investment in future capabilities rather than immediate operational gains.

When it comes to adversaries, business email compromise (BEC) remains the most discovered threat when threat hunting. However, ransomware detections have declined, potentially due to improved mitigation strategies or faster attack execution by ransomware groups. Catching nation-state threats via threat hunting has slightly risen this year, highlighting a steady presence of nation-state threats in the cyber landscape. We also find that “living off the land” (LOTL) techniques remain the most prevalent tactic across all adversary groups, reinforcing the need for behavior-based threat hunting.

**Key findings:**
- 45% of organizations now update methodologies as needed, up from 35% in 2024.
- Organizations fully outsourcing threat hunting dropped to 30%, down from 37% last year.
- 61% of respondents cite skilled staffing shortages as a primary barrier to success.
- Ransomware detections declined from 63% to 46%, but targeted exfiltration remains a concern at 57%.
- 76% of organizations report seeing LOTL techniques in nation-state attacks, unchanged from last year.
- Organizations increasing staffing investment (10% or more) sit at 40%, with 31% not planning to make changes.
- The use of commercial tools for tracking the threat landscape declined to 58% (from 70%), with internally built tools rising to 48%.
- 76% of organizations are using vendor blogs and papers as a priority source for their threat intelligence and research.
- EDR/XDR remains the top-ranked tool for threat hunting, followed by SIEM and NDR solutions.

![Figure 1. Demographics of Survey Respondents: Charts showing top 4 industries, organizational size, operations/headquarters, and top 4 roles.]

---

## Plan the Hunt, Hunt the Plan—or Just Wing It?

The 2025 data indicates a slight decline in organizations with formally defined threat hunting methodologies (46%, down from 51% in 2024), as shown in Figure 2. Although this remains a strong indication of maturity within the industry, the drop suggests that some organizations may struggle to maintain structured approaches to threat hunting.

![Figure 2. Types of Methodologies: Bar chart comparing 2023, 2024, and 2025 data on formal, ad hoc, and planned methodologies.]

When we look at who is building methodologies and who is performing threat hunting, there is a pretty large divide between these two groups. CISOs (53%) and external entities (49%) are the most prominent contributors to methodology development alone. Interestingly, only 15% of dedicated threat hunting teams contribute to methodology development.

When it comes to organizations updating their methodologies, we see a notable increase in those reviewing and adjusting them on an as-needed basis, rising to 45% from 35% in 2024.

![Figure 3. Methodologies vs. Staffing: Bar chart comparing 2022-2025 data on whether methodologies affect staffing or vice versa.]

---

## Worth It, or Just a Wild Goose Chase?

This year’s data shows a decline in organizations that formally measure the effectiveness of their threat hunting programs, dropping to 51% from 64% in 2024 (see Figure 4).

![Figure 4. Formally Measuring Success: Line chart showing the percentage of organizations measuring success from 2021 to 2025.]

![Figure 5. Improvement of Overall Security: Bar chart showing the perceived improvement in security posture resulting from threat hunting.]

---

## What Threat Hunting Is Catching in 2025

We found a clear distinction between the areas organizations prioritize for effective threat hunting and the environments where threat hunting is most challenging. Servers (26%) and workstations (25%) rank as the top priorities. However, cloud environments present the biggest challenge, with 39% of respondents citing them as the most complex area.

![Figure 6. Threat Hunting Focus Areas: Bar chart comparing importance vs. difficulty across workstations, servers, network, cloud, and portable devices.]

Business email compromise (BEC) remains the most detected attack type, although it has decreased to 64% from 68% in 2024 (see Figure 7).

![Figure 7. Types of Attacks: Bar chart comparing 2024 and 2025 detection rates for BEC, ransomware, nation-states, and industrial espionage.]

![Figure 8. Techniques by Actor Type: Bar chart showing prevalence of LOTL, off-the-shelf tools, custom malware, etc., across different actor types.]

![Figure 9. Nation-State Techniques: Bar chart comparing 2024 and 2025 techniques used by nation-state actors.]

![Figure 10. Ransomware Techniques: Bar chart comparing 2024 and 2025 techniques used by ransomware actors.]

![Figure 11. Espionage Techniques: Bar chart comparing 2024 and 2025 techniques used by criminal actors in industrial espionage.]

---

## Tracking Threat Actors in the Digital Wild West

This year, we see a notable shift toward automation in threat hunting strategies, with 37% of organizations now automatically generating new hunts based on evolving threat intelligence, up from 30% in 2024.

---

## DIY Threat Hunting—The Trend of Keeping It In-House

The percentage of organizations outsourcing their threat hunting dropped from 37% in 2024 to 30%, reflecting a shift toward building in-house threat hunting capabilities (see Figure 12).

![Figure 12. Year-Over-Year Outsourcing: Line chart showing the decline in outsourcing from 2021 to 2025.]

![Figure 13. Outsourcing Approaches: Bar chart showing who defines hunting parameters in outsourced environments.]

![Figure 14. Threat Tracking Tools: Bar chart comparing 2024 and 2025 usage of commercial, open source, and internally built tools.]

---

## Keeping Up with Evolving Threats

Organizations significantly increased their reliance on a diverse range of sources to stay ahead of evolving attacker techniques, with the most notable growth in vendor blogs and papers, rising from 59% in 2024 to 76% this year (see Figure 15).

![Figure 15. Sources of Intelligence: Bar chart comparing 2024 and 2025 sources used to stay updated on attacker techniques.]

---

## The Roadblocks and Workarounds for Threat Hunts

Over the past year, the most pressing challenge in threat hunting has remained the shortage of skilled personnel, cited by 61% of respondents. Budget constraints surged to 49%, up from 40% in 2024.

![Figure 16. Staff Investment: Bar chart showing planned changes in staffing investment.]

![Figure 17. Tool Investment: Bar chart showing planned changes in tooling investment.]

---

## Conclusion

The 2025 SANS Threat Hunting Survey highlights the ongoing evolution of threat hunting as organizations refine their methodologies, enhance their tooling, and balance internal expertise with outsourced support. The overall trajectory for threat hunting into the future remains positive, with more organizations recognizing the value of proactive threat hunting as a critical pillar of their cybersecurity defenses.

[^1]: MITRE, “ATT&CK,” https://attack.mitre.org
[^2]: “Introducing the PEAK Threat Hunting Framework,” www.splunk.com/en_us/blog/security/peak-threat-hunting-framework.html
[^3]: “TaHiTI,” www.betaalvereniging.nl/en/safety/tahiti
[^4]: “Enterprise Detection & Response: The Pyramid of Pain,” https://detect-respond.blogspot.com/2013/03/the-pyramid-of-pain.html