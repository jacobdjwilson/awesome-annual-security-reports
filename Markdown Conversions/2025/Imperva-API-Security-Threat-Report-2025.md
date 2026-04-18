# Imperva API Threat Report: The API Battleground

## Table of Contents
- [Executive Summary](#1-executive-summary)
- [About The Data & Methodology](#2-about-the-data--methodology)
- [The Api Threat Landscape](#3-the-api-threat-landscape)
    - [Why APIs are the primary attack surface](#31-apis-are-the-primary-attack-surface)
    - [API attack volume & growth patterns](#32-api-attack-volume--growth-patterns)
    - [Which endpoints attackers target (and why)](#33-which-endpoints-attackers-target-and-why)
- [Threat Actor Behaviors & Tactics](#4-threat-actor-behaviors--tactics)
    - [Attack methods](#41-attack-methods)
    - [Top API attack categories & insights](#42-top-api-attacks--high-level-categories--insights)
    - [The API logic exploit crisis](#43-the-api-logic-exploit-crisis)
    - [Tools & automation used by attackers](#44-tools--automation-used-by-attackers)
- [Emerging Exploit Trends (H2 Signals)](#5-emerging-exploit-trends)
    - [Misconfigured third-party integrations](#51-misconfigured-third-party-integrations)
    - [Parameter tampering](#52-parameter-tampering)
    - [Shadow / unauthenticated APIs](#53-shadow--unauthenticated-apis)
- [Business & Regulatory Impact](#6-business--regulatory-impact)
- [Types Of Attacks Against Api Endpoints](#7-types-of-attacks-against-api-endpoints)
    - [CVE attack vectors (Log4j, WebLogic, Joomla)](#71-common-cve-attack-vectors-on-api-sites)
    - [Industry targets](#72-top-targeted-industries-for-api-attacks)
    - [Common pattern across industries](#73-common-pattern-across-industries)
- [Strategic Guidance For Executives & Cisos](#8-strategic-guidance-for-executives--cisos)
- [Defense Best Practices For Practitioners (Playbook)](#9-defense-best-practices-for-practitioners-playbook)
- [Conclusion: Toward Adaptive Api Security](#10-conclusion-toward-adaptive-api-security)
- [Appendix — Glossary](#appendix--glossary)

---

## 1. Executive Summary

In the first half of 2025 (H1 2025), Imperva observed a decisive shift: APIs are now the primary battlefield. Across 4,000+ monitored environments, we recorded more than 40,000 API incidents. While APIs account for roughly 14% of all attacks, they attract ~44% of advanced bot activity, showing attackers concentrate their smartest automation on API logic rather than noisy scans. Most alarming: we observed an application-layer DDoS spike that reached 15 million requests per second (RPS) against a financial API — a clear demonstration that attackers now combine scale with stealth.

The most damaging attacks today are valid API calls that bend business logic — promo loops, gift-card cracking, targeted data scraping, and credential-driven account takeovers. These requests look normal to signature-based tools and static rate limits, so defenders drown in alerts for malformed traffic while the real attacks slip through the very logic that powers your business.

> "WE OBSERVED AN APPLICATION-LAYER DDoS SPIKE THAT REACHED 15 MILLION REQUESTS PER SECOND AGAINST A FINANCIAL API"

### What Defenders Must Do Differently
Add business context and runtime intelligence on top of traditional controls. That means continuous API discovery, runtime contract/schema enforcement, object-level authorization, behavior-driven bot detection tied to business KPIs (promo redemptions, refund spikes, reservation rates), and adaptive throttling. These capabilities turn “valid” requests into defensible events, not missed threats.

### Key Truths From Our Telemetry
- **Attackers focus on where money, identity and workflows live** — data-access, checkout/payment, and authentication endpoints.
- **Business-logic abuse (BOLA) and parameter tampering are the dominant vectors**; signature-only defenses and coarse rate limits miss them.
- **Shadow and partner APIs create the largest operational blind spots**; combined with headless browsers and botnets, attackers can extract value while blending into normal traffic.

### Operational Model (Fast Wins)
**DISCOVER >> ASSESS >> MITIGATE**
Discover every endpoint (public, private, shadow); assess their business impact and risk; mitigate with runtime enforcement, adaptive bot controls, and DDoS protection. These steps yield immediate, measurable risk reduction.

### Top Actions For Leaders
1. Implement continuous API discovery and classify endpoints by business impact.
2. Enforce runtime schema validation and object-level authorization for high-risk APIs.
3. Deploy context-aware bot mitigation and adaptive throttling for checkout/auth/data endpoints.
4. Operationalize API ownership (product + security), publish a short set of API KPIs to the board, and run API-specific tabletop exercises.
5. API-aware telemetry and business-context detection to stop the attacks that look “normal” but are anything but.

---

## 2. About the Data & Methodology

In just the first half of 2025, our Threat Research team at Imperva collected and examined real-world API attack data from thousands of customer environments around the globe. We wanted to understand exactly how bad actors are probing, breaking, and bending API logic—so you can see the full picture and defend against it.

### Here’s What We Looked At:
- **40,000+ API incidents**: In the first six months of 2025, from small probes to full-scale breaches.
- **Bot telemetry & fingerprinting**: Tracking both web-based and mobile-app bots to see how they hide and behave.
- **CVE exploit tracking**: Focused on known troublemakers like Log4j, Oracle WebLogic, and Joomla vulnerabilities.
- **DDoS forensics**: Spotlighting attacks that overwhelmed APIs—like the 15 million-RPS application-layer flood we stopped on a major financial endpoint.
- **Endpoint behavior analysis**: Including request volumes, spikes, and weird patterns that signal abuse.

### Our Approach
1. Categorize techniques (scraping, account takeover, fraud) and map them to the affected endpoints (authentication, checkout, data-access).
2. Correlate behaviors by flagging outliers—whether it’s a sudden burst of traffic or a slow, steady trickle that drips under standard alerts.
3. Segment by industry, so you know which sectors are under the heaviest fire.
4. Synthesize business logic insights —we didn’t just count attacks; we dug into how and why they worked, so your team can plug the gaps before attackers exploit them.

### Limitations
Dataset reflects Imperva customer footprint and controlled labs; absolute global volumes may differ, but behavioral trends and relative distributions are robust.

---

## 3. The API Threat Landscape

### 3.1 APIs Are the Primary Attack Surface
APIs expose business logic — not just data. They execute account changes, payments, promotions, and access controls. In our analysis, attackers treat APIs as direct money channels: exploiting workflows yields immediate financial or identity returns. Whereas web UI attacks often require human interaction, API attacks scale automatically: one script can enumerate millions of resources or drive thousands of promo redemptions per minute.

### 3.2 API Attack Volume & Growth Patterns
We base these findings on Imperva’s global telemetry—drawing from WAF logs, API gateway records, bot management sensors, and DDoS mitigation feeds across 4,000+ customer environments.

**Key Observations:**
- **A Historic Spike in API Attacks**: 44% of advanced bot traffic now attacks APIs, up from under 30% just two years ago.
- **Volume of Attacks Is Skyrocketing**: 40,000+ API incidents recorded in the first six months of 2025—an average of 220 incidents per day.
- **DDoS Goes Application-Layer**: We observed a record 15 million RPS application-layer DDoS against a financial API. 68% of all API-focused DDoS traffic hit financial services.

### 3.3 Which Endpoints Attackers Target (and why)
![API Attacks by Endpoint Type: Data Access 37%, Checkout 32%, Authentication 16%, Product 11%, Admin 4%]

- **Data-Access Endpoints (~37%)**: Targeted for valuable intelligence and low friction.
- **Checkout & Payment Endpoints (~32%)**: Targeted for direct revenue theft and complex workflow exploitation.
- **Authentication Endpoints (~16%)**: Targeted for Account Takeover (ATO) and token theft.
- **Gift-Card & Promo-Validation Endpoints (~5%)**: Targeted for low-value, high-volume fraud.
- **Shadow or Misconfigured Endpoints (~3%)**: Targeted because they often bypass WAFs and bot filters.

---

## 4. Threat Actor Behaviors & Tactics

### 4.1 Attack Methods
![Chart of attack methods: Scraping 31%, Payment Fraud 26%, ATO 12%, Scalping 11%, User Details Harvesting 6%, File Upload/RCE 4%, Gift Card Fraud 4%, Session Hijacking 2%, Carding 1%, Coupon Guessing 1%, Admin Access 1%, Sensitive Data Access 1%]

### 4.2 Top API Attacks — High-Level Categories & Insights
![Chart of top API attacks: Data Leakage 27%, RCE/RFI 13%, Business Logic 11%, API Violation 9%, Path Traversal/LFI 8%, XSS 7%, Automated Attack 6%, SQLi 4%, Protocol Manipulation 4%, Authentication Bypass 3%, Backdoor/Trojan 2%, SSRF 2%, MISC 4%]

### 4.3 The API Logic Exploit Crisis
Business-logic abuse is dangerous because it is invisible to WAFs and signatures. Because each request follows the documented API contract, traditional firewalls see them as harmless.

### 4.4 Tools & Automation Used By Attackers
Attackers use a compact, powerful toolkit:
- **Browser Impersonation**: Puppeteer, Selenium.
- **Botnets & Proxy Pools**: To rotate IPs and geo-locations.
- **Payload Generators**: Burp, Postman scripts.
- **Exploit Frameworks**: Metasploit, CVE kits.

---

## 5. Emerging Exploit Trends

### 5.1 Misconfigured Third-Party Integrations
Bots probe vendor/SaaS/cloud APIs that are loosely connected to core systems. Audit their scopes and remove unused privileges.

### 5.2 Parameter Tampering
Bots tweak query parameters and request sequences to subvert business logic. Defenses must validate semantics (e.g., "price must match known SKU pricing").

### 5.3 Shadow / Unauthenticated APIs
Hidden or test endpoints often lack auth or throttling. Force all traffic through a central gateway and discovery system.

---

## 6. Business & Regulatory Impact
API breaches lead to financial loss, reputation damage, and regulatory fines (GDPR, HIPAA, PCI-DSS). API security is a business-continuity issue.

---

## 7. Types Of Attacks Against API Endpoints

### 7.1 Common CVE Attack Vectors on API Sites
- **Log4j (CVE-2021-44228)**: ~50% of all CVE probes.
- **Oracle WebLogic**: ~30% of all CVE probes.
- **Joomla**: ~20% of all CVE probes.

### 7.2 Top Targeted Industries for API Attacks
![DDoS Attacks on API Endpoints: Financial Services 37%, Travel 26%, Entertainment & Art 14%, Telecom & ISPs 13%, Other 10%]

---

## 8. Strategic Guidance For Executives & CISOs
1. **Map API-to-Business Impact**: Assign risk scores based on what the API controls.
2. **Assign “API Owners”**: Designate product and security liaisons for every critical API.
3. **Metrics & Reporting**: Surface API security metrics to the board.
4. **Integrate into Architecture**: Move to a Zero-Trust API model.
5. **Continuous Testing & Sharing**: Institutionalize red team exercises.
6. **Business-Level Communication**: Frame API incidents as business problems.

---

## 9. Defense Best Practices For Practitioners (Playbook)
1. **Continuous API Discovery & Classification**: Find every endpoint.
2. **Schema Validation & Contract Enforcement**: Reject deviations from approved models.
3. **Behavioral Anomaly Detection**: Build normal-use baselines.
4. **Adaptive Rate Limits & Bot Management**: Throttle based on risk context.
5. **Strong Authentication/Authorization**: Use short-lived, scoped tokens.
6. **Supply Chain & Configuration Hygiene**: Patch ruthlessly and vet third-party integrations.
7. **Monitoring & Rapid Response**: Centralize logs from WAF, gateway, and SIEM.
8. **Prepare API-Specific Incident Playbooks**: Pre-plan revocation and rotation steps.

---

## 10. Conclusion: Toward Adaptive API Security
Protecting APIs demands more than firewalls and static rules. It requires full visibility, behavior-based detection, and protections embedded into workflows. The volume and sophistication of API attacks will continue to grow; the best time to act is now.

---

## Appendix — Glossary
- **BOLA**: Broken Object Level Authorization
- **ATO**: Account Takeover
- **RCE**: Remote Code Execution
- **PoW**: Proof of Work
- **JWT**: JSON Web Token

[BACK TO TABLE OF CONTENTS](#table-of-contents)