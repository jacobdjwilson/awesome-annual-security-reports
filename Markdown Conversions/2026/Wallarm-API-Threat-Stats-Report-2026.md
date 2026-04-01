# API THREATSTATS™ REPORT 2026
## The New API Risk Multiplier

## Table of Contents
- [Executive Summary](#executive-summary)
- [How API Risk Evolved Across 2025](#how-api-risk-evolved-across-2025)
- [API Vulnerability Trends](#api-vulnerability-trends)
- [API Exploit Trends](#api-exploit-trends)
- [API Breach Trends](#api-breach-trends)
- [Key Takeaways](#key-takeaways)
- [About Wallarm](#about-wallarm)

---

## Executive Summary

If an attacker could control only one part of your infrastructure, they would pick your APIs. No one is surprised when you say that APIs are the backbone of modern digital business, but not everyone realizes that they’ve also become the most effective way in for attackers.

The findings are clear and consistent across every dataset we examined, no guesswork required. Attackers are not chasing exotic flaws. They are exploiting repeatable failures in identity, access control, and exposed interfaces, often at machine speed and massive scale. APIs dominate vulnerability disclosures, account for nearly half of confirmed exploited vulnerabilities, and sit at the center of the most consequential breaches of the year.

Three themes define API risk in 2025:

### Abuse Beats Bugs
The API ThreatStats Top 10 shows attackers favor logic abuse, trust failures, and resource consumption over traditional code defects. Those behaviors surface most clearly as cross-site issues and broken access control, which rose to the top by attack volume. Injections remain a persistent, high-impact threat, not because attackers prefer them, but because APIs still process vast amounts of untrusted input at scale.

### AI Security is API Security, Now with Consequences
36% percent of published AI vulnerabilities involve APIs. And 36% (yes, the same percentage) of AI-related exploited vulnerabilities also involve APIs. As AI adoption accelerates, APIs have become the primary interface attackers use to reach models, data pipelines, and automated workflows.

### Autonomy Changes the Blast Radius
Model Context Protocol (MCP) emerged as a leading indicator of where API risk is heading. Although arguably still early in adoption, MCP accounted for 14% of published AI vulnerabilities, showed explosive growth during the year, and was involved in a Top 10 API breach. When APIs act on behalf of agents, failures no longer just expose data, they delegate authority.

---

## How API Risk Evolved Across 2025

The Wallarm API ThreatStats Top 10 shows how attackers actually target APIs in production, based on what we see happening, not what looks risky on paper. 

### The 2025 Leaderboard
Cross-Site Issues emerge as the dominant API threat in 2025. While they ranked mid-pack in 2024, they moved decisively upward and finished the year as the most abused category overall.

### Injections Remain a Constant Anchor Threat
While Injections took the top spot in 2024, they ranked second overall in 2025 and never fell below the second position in any quarter. It’s clear that despite years of industry education about injections, APIs continue to process vast volumes of untrusted input and pass it directly into downstream systems.

### Broken Access Control Continues to Enable Scale
Broken Access Control holds the third position for the year, down from the number two spot last year. It was consistently third with a bump to first in Q4.

---

## API Vulnerability Trends

We analyzed as close to a complete set of published vulnerabilities from 2025 as possible, 67,058 security bulletins in total. 

- 11,053 vulnerabilities (17%) were API-related.
- 2,185 vulnerabilities (3%) were AI-related.
- 786 vulnerabilities overlapped both categories (36% of all AI vulnerabilities are also API vulnerabilities).

![Chart showing API vulnerability characteristics: 59% no authentication, 97% single-request, 98% easy/trivial, 99% remote]

---

## API Exploit Trends

For this section of the report, we analyzed CISA’s Known Exploited Vulnerabilities (KEV) catalog entries added during calendar year 2025 (n=245).

- 106 of the 245 KEVs (43%) are API-related.
- 24% of KEVs are AI-related.
- 36% of AI-related KEVs are also API-related.

Clearly, exploited AI risk is very often exploited API risk.

---

## API Breach Trends

This section analyzes 60 API-related breach incidents disclosed in 2025.

### Top 10 API Breaches for 2025
1. **700Credit/Fintech**: 5.6M victims; unsafe trust in third-party API.
2. **Qantas/Airline**: 6M records stolen; weak authentication.
3. **Salesloft Drift/Software**: OAuth token compromise.
4. **SwissBorg/Cryptocurrency**: $41M stolen; credential/API access abuse.
5. **Hosting Providers MPC/AI**: 3,000+ servers; path traversal in MCP servers.
6. **Anthropic/Claude APIs**: Platform exposed via access control weaknesses.
7. **LangSmith/AI Tooling**: Internal service exposure.
8. **Steam/Gaming Platform**: 89 million records; automated abuse.
9. **Oracle Cloud/Cloud Services**: Cloud management API vulnerability.
10. **Condé Nast (Wired)**: BOLA and scraping abuse.

---

## Key Takeaways

### For Security Practitioners
- **Design for abuse, not just correctness**: Controls must be inline and per-request.
- **Treat identity as the primary attack surface**: Focus on token lifecycle and scope.
- **Assume every exposed API will be discovered and scripted**: Rate limiting and behavioral detection are mandatory.

### For CISOs and Security Leaders
- **API risk is business risk**: APIs sit on revenue flows and customer data.
- **AI security failures are overwhelmingly API-driven**: Do not treat AI security as a separate silo.
- **Measure what attackers exploit**: Align metrics to observed abuse rather than theoretical checklists.

---

## About Wallarm

Wallarm is the leading API security company, purpose-built to protect modern cloud-native and AI-driven architectures. Our platform delivers complete visibility, intelligent threat detection, and real-time protection for all types of APIs like REST, GraphQL, gRPC, and AI/Agent-based APIs.

**Learn More**
- Website: [wallarm.com](https://wallarm.com)
- Blog: [lab.wallarm.com](https://lab.wallarm.com)
- X (Twitter): [x.com/wallarm](https://x.com/wallarm)
- LinkedIn: [linkedin.com/company/wallarm](https://linkedin.com/company/wallarm)
- YouTube: [youtube.com/@wallarmchannel](https://youtube.com/@wallarmchannel)
- Explore Product: [tour.playground.wallarm.com](https://tour.playground.wallarm.com)