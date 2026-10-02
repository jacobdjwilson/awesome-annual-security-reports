# THE 2026 SPYCLOUD IDENTITY THREAT REPORT
Organization: SpyCloud  
Report Title: Identity-Threat-Report  
Year: 2026  

## Table of Contents
- [Introduction: Mapping the New Identity Terrain](#introduction-mapping-the-new-identity-terrain)
- [Executive Summary: Key Takeaways](#executive-summary-key-takeaways)
- [Section 01: Trailing Ahead to Operational Maturity](#section-01-trailing-ahead-to-operational-maturity)
- [Section 02: Blind Spots Become Initial Access Vectors](#section-02-blind-spots-become-initial-access-vectors)
- [Section 03: The Attack Map Extends Beyond the Perimeter](#section-03-the-attack-map-extends-beyond-the-perimeter)
- [Section 04: Expanding Identity Access Paths](#section-04-expanding-identity-access-paths)
- [Section 05: The Cost of a Slower Pace](#section-05-the-cost-of-a-slower-pace)
- [Section 06: Charting the Path Forward](#section-06-charting-the-path-forward)
- [Section 07: The Journey Ahead](#section-07-the-journey-ahead)
- [Appendix – Methodology](#appendix--methodology)

---

SPYCLOUD.COM  
Know the terrain  
THE 2026 SPYCLOUD IDENTITY THREAT REPORT  
BENCHMARKS, BLIND SPOTS, AND STRATEGIES FOR DETECTING, REMEDIATING, AND REDUCING IDENTITY THREATS ACROSS HUMAN AND NON-HUMAN IDENTITIES  

---

## Introduction: Mapping the New Identity Terrain

Identity exposure is measurable, operational, and fixable. Yet most organizations still struggle to manage it consistently.

Many security teams are navigating with an outdated map – one built for well-marked trails, not the sprawling backcountry attackers now operate in. The gap between what organizations can see and what attackers can reach is the terrain this report sets out to chart.

Today’s identity attack surface extends far beyond traditional boundaries. It now stretches past employee credentials to session cookies and refresh tokens, non-human identities (NHIs) tied to AI agents and APIs, and third-party partners and ecosystems. As that terrain expands, attack prevention increasingly depends less on how well an organization knows its own camp and more on how it can identify exposed identity assets outside its perimeter – and remediate them before attackers take advantage.

Report findings are based on a survey of 750 cybersecurity leaders and practitioners across North America, the United Kingdom, and select European markets. This report benchmarks how organizations with 500 employees or more detect, remediate, and govern identity threats, where critical blind spots remain, and what distinguishes the most mature identity security programs.

### The Landscape Attackers Are Exploring Today
SpyCloud continuously recaptures identity assets circulating in the criminal underground, extending well beyond what most organizations can see in their existing tooling.

- **1+ Trillion** recaptured identity assets
- **65.7 Billion** distinct identity records
- **17+ Billion** session cookies recaptured
- **63+ Million** API keys and tokens

---

## Executive Summary: Key Takeaways

### 01. Identity-Based Events Are Now a Routine Reality
More than two-thirds (68%) of organizations experienced an identity-based event in the past year, with affected organizations averaging eight events, confirming that identity compromise has become an operational reality rather than an isolated incident.

### 02. NHIs Are Now the Leading Route for Initial Access
NHI-related misuse was the top reported identity-based event type (42%), followed by a ransomware event enabled by a compromised identity (39%) and account takeover involving employee or contractor identities (38%).

- **42%**: Misuse or compromise involving non-human identity
- **39%**: Ransomware event enabled by a compromised identity
- **38%**: Account takeover involving employee or contractor identities

### 03. Visibility Gaps Leave Critical Markers Unseen
Organizations that experienced identity events were significantly less likely to have visibility into stolen session cookies (37% vs. 50%) and personal devices (40% vs. 52%), suggesting that blind spots continue to fuel successful attacks.

- **Stolen session cookie visibility**: 37% (Identity events) vs. 50% (No identity events)
- **Stolen personal device visibility**: 40% (Identity events) vs. 52% (No identity events)

### 04. The Governance Map Has Not Kept Pace
Ninety-one percent (91%) of organizations use AI tools or agents with internal access, but only 56% have formal governance and ownership for AI- and NHI-related privileges.

- **91%**: Use AI tools with internal access
- **56%**: Have formal governance for AI

### 05. Confidence Can Hide the Biggest Blind Spots
C-suite leaders were far more confident in their NHI visibility than frontline operators (66% vs. 50%). While the U.S. and Canada largely tracked the global baseline, the UK reported the highest confidence (53%) despite experiencing the highest identity event rate (77%), demonstrating that confidence does not necessarily reflect coverage.

### 06. Industry Differences Reveal Different Frequency and Impact of Identity Events
The Government sector reported experiencing a much higher frequency of identity events (92.3% vs. 68% total), and government orgs reported the highest average event volume (10 events vs. 8 total average). Manufacturing organizations, on the other hand, were significantly less likely to have experienced an identity-based event (58% vs. 68% total), but when they did, the fallout was worse, reporting customer or partner trust loss as a business impact (56.9% vs. 40.2% total) and higher average impacts across the board – a classic “fewer, but costlier” pattern.

### 07. The Trail Extends Beyond Organizational Boundaries
Third-party malware infections (23%) and API key/application exposures (22%) were cited as the leading causes of supply chain identity events across respondents. Vendor remediation validation is uneven, even across technology-heavy sectors. Telecommunications leads with the highest active validation rate at 68%, while Technology / Software organizations report the lowest rate at 38%, revealing meaningful differences in third-party identity governance.

### 08. The Best Organizations Prove What’s Possible
Germany emerged as a benchmark for third-party identity governance, with 76% of organizations actively confirming vendor remediation, demonstrating that stronger operational practices can substantially improve supply chain visibility.

### 09. Scale Influences Confidence, But Not Certainty
Large enterprises (5,000+ employees) reported significantly higher confidence in their identity visibility than mid-market organizations, but confidence alone did not consistently translate into better outcomes.

### 10. Manual Remediation Creates Costly Detours
Organizations relying on manual remediation reported higher incident response costs (39%) and customer trust loss (47%) compared to their peers who report using high levels of automation (32% and 36%, respectively).

---

## Section 01: Trailing Ahead to Operational Maturity

Know the terrain  

The data in this year’s report suggests that operational maturity is more closely associated with resilience than company size, industry, or geography. Organizations with more mature identity threat protection programs report lower identity-based event rates and stronger visibility, monitoring, remediation, governance, and automation practices.

### In This Section
- The Identity Threat Protection Maturity Trail
- Identity-based event rates by maturity tier
- What sets identity resilience leaders apart

### 1.1 The Identity Threat Protection Maturity Trail
To benchmark organizational readiness, respondents were grouped into four maturity tiers based on their identity exposure across visibility, monitoring, governance, automation, and remediation capabilities.

- **Tier 01 | Reactive (9%)**: Limited visibility, manual processes, and inconsistent remediation
- **Tier 02 | Building (37%)**: Building foundational processes but still challenged by visibility and operational consistency
- **Tier 03 | Operational (45%)**: Repeatable workflows, measurable outcomes, and increasing use of automation
- **Tier 04 | Optimized (9%)**: Continuous monitoring, strong governance, and automated remediation across key identity workflows

### 1.2 Identity-Based Event Rates by Maturity Tier
Building organizations experience the highest incident rate, likely reflecting greater visibility into identity exposures before mature processes and automation begin reducing risk. From there, data shows a clear maturity effect: identity-based event rates decline substantially as organizations move from Building to Operational and ultimately Optimized.

*(Organizations reduce identity risk as they progress along the maturity trail)*

### Trail Marker: Maturity Varies by Sector
Industry alignment seemingly influences identity security maturity. Telecommunications (18.4%) – which has been on the receiving end of a growing number of targeted attacks in recent years – and Retail & Ecommerce (13.4%) have the highest concentration of organizations operating at the Optimized maturity level, while Insurance reports the highest share of Reactive programs (17.7%), underscoring that some industries remain earlier in their operational journey.
- **Telecom (Optimized)**: 18.4%
- **Retail / E-Commerce (Optimized)**: 13.4%
- **Insurance (Reactive)**: 17.7%

---

## Section 02: Blind Spots Become Initial Access Vectors

Know the terrain  

Identity-based events are a recurring operational reality, not isolated incidents. Sixty-eight percent (68%) of organizations experienced an identity-based event in the past 12 months, and affected organizations averaged 8 identity-based events annually, with nearly half (49%) experiencing 6–10 events.

### In This Section
- Confidence vs. identity-based event rate by market
- Attackers exploit what organizations can’t see
- What sets identity resilience leaders apart

Despite the frequency of these events, organizations remain highly confident in their ability to identify identity exposures. Nearly half (46%) describe themselves as very confident in their visibility. Moreover, confidence increases with organizational seniority. Two-thirds (66%) of C-suite leaders believe they have adequate visibility into non-human identities (NHIs), compared with 50% of frontline security operators.

The disconnect becomes even more apparent when organizations look at the identity events they are actually experiencing. Rather than traditional employee account compromise, machine identities and other non-human identities now account for the most common identity-based events reported by security teams.

### Identity-Related Events (Past 12 Months)
- **NHI misuse / AI agents / bots**: 42%
- **Ransomware via compromised identity**: 39.7%
- **Account takeover (employees)**: 38.3%
- **Insider threat / employment fraud**: 35.6%
- **Malware-related credential exposure**: 33.7%
- **Phishing-related credential exposure**: 30.7%
- **Third-party / supply chain identity event**: 26.8%
- **API key compromise or misuse**: 26.5%
- **Hijacked session**: 15.8%

### Confidence vs. Identity-Based Event Rate by Market
*(Very confident in visibility [% of respondents] vs. experienced an identity-based event [past 12 months])*

- **United Kingdom**: 53.3% confident vs. 76.7% event rate (23.4 points gap)
- **North America (United States & Canada)**: 46.0% confident vs. 68.0% event rate (22.0 points gap)
- **European Markets (Spain, Germany, the Netherlands, Austria, Switzerland)**: 41.2% confident vs. 62.8% event rate (21.6 points gap)

> **High Confidence Doesn’t Always Mean Lower Risk**  
> Across the regional segments shown, organizations report relatively high confidence in their visibility, yet identity-based events remain common. The disconnect is most pronounced in the United Kingdom, which reports both the highest visibility confidence (53.3%) and the highest identity-based event rate (76.7%), reinforcing a central finding of this report: confidence does not equal coverage.

### Attackers Exploit What Organizations Can’t See
Organizations that avoided identity-based events consistently monitored more exposure types than those that experienced incidents. Visibility into two areas stood out most in affecting whether an organization experienced identity-based events:

- **Stolen Session Cookies**: 37% (with visibility) vs. 50% (without visibility)
- **Personal Devices with Corporate Access**: 40% (with visibility) vs. 52% (without visibility)

The findings reinforce a central theme of this report: attackers exploit what organizations cannot see.

### What Sets Identity Resilience Leaders Apart
Visibility and continuous monitoring improve dramatically as organizations progress along the Identity Threat Protection Maturity Trail. By the time organizations reach the Optimized tier, confidence in visibility and proactive monitoring become defining operational strengths.

- **Reactive**: 26% very confident in visibility | 0% continuously monitor identities
- **Building**: 42% very confident in visibility | 3% continuously monitor identities
- **Operational**: 46% very confident in visibility | 27% continuously monitor identities
- **Optimized**: 84% very confident in visibility | 93% continuously monitor identities

The most mature organizations combine broad visibility with continuous monitoring, enabling them to identify and remediate identity exposure before it becomes an incident.

### Trail Marker: Phishing and Malware Remain Persistent Access Paths
Phishing and malware continue to create boundless opportunities for bad actors, providing them with stolen credentials, session cookies, refresh tokens, and more to carry out account takeover, session hijacking, ransomware, and other attacks.
- **Social Engineering**: 37%
- **Phishing**: 40%
- **Incomplete Visibility on Phishing Events**: 53%

---

## Section 03: The Attack Map Extends Beyond the Perimeter

Know the terrain  

AI tools, agents, applications, vendors, and partners are creating new identity paths into the business. As these connections expand, identity risk increasingly comes from privileged access that sits outside traditional governance and visibility.

### In This Section
- AI adoption has outpaced governance
- The AI trail is harder to track than organizations think
- NHIs are now the leading route for initial access

### 3.1 AI Adoption Has Outpaced Governance
Nearly every organization (91%) now uses AI tools or agents with access to internal systems, applications, or data. Yet only 56% have formal policy and clear ownership for managing AI- and NHI-related privileges. Another 41% rely on informal processes or partial ownership.

### 3.2 The AI Trail Is Harder to Track Than Organizations Think
Organizations overwhelmingly believe they have visibility into AI-related identity exposure. Nearly all organizations (95%) agree they have adequate visibility into NHI exposures associated with AI tools, agents, service accounts, applications, or bots.

> **Confidence Does Not Equal Coverage**  
> AI- and NHI-related exposures are the least-monitored category of risk in this study.

### 3.3 Survey Says: NHIs Are Now the Leading Route for Initial Access
The visibility gap has real consequences. NHI-related misuse was the most commonly reported identity-based event (42%). Meanwhile, 50% of affected organizations cited exposed, compromised, or overprivileged NHIs, including API keys, tokens, and service accounts, as common access paths, and 31% identified them as the single most common initial access vector.

The challenge is especially acute in the selected European markets surveyed, where 34% of affected organizations identified exposed, compromised, or overprivileged NHIs as their most common initial access vector.

Perceived risk does not always track with actual events. While only 28% of organizations overall consider misconfigured or overprivileged NHIs to be a high-risk threat, Government organizations are substantially more likely to do so at 41%, suggesting heightened awareness of this emerging identity threat.

#### Primary Initial Access Vector Rank
1. **Exposed / overprivileged non-human identities**: 31%
2. **Phishing / social engineering**: 17%
3. **Stolen session cookies / tokens**: 16%
4. **Exposed or weak credentials**: 14%
5. **Third-party / supply chain**: 11%
6. **Insider threat**: 8%
7. **Unmanaged devices**: 4%

> **Compromised NHIs** are nearly 2x as likely to be the primary entry point compared to phishing.  
> **European Markets**: 34% of affected organizations identified NHIs as their most common initial access vector.

---

## Section 04: Expanding Identity Access Paths

Know the terrain  

### In This Section
- Shadow access, not just shadow IT
- What sets identity resilience leaders apart

Governance helps bring the trail into view. Formal governance doesn’t just assign ownership. It improves visibility across the broader identity ecosystem. For example, 49% of organizations with formal AI governance have visibility into personal devices with corporate access, compared with 36% of organizations relying on informal governance.

### Trail Marker: Shadow Access, Not Just Shadow IT
As AI tools, agents, service accounts, and applications gain access to business systems, identity risk increasingly stems from shadow access: privileged connections that exist outside traditional governance and visibility.

Overprivileged NHIs are often less a technology problem than an operational one, reflecting unclear ownership, inconsistent governance, and identity hygiene gaps.

### What Sets Identity Resilience Leaders Apart
Leaders at Optimized organizations don’t stop at identifying third-party identity exposures. They consistently verify that threats have been remediated, reducing the risk of unresolved exposures across their vendor ecosystem.

The maturity gap is substantial:

| Maturity Tier | Lack a Consistent Verification Process | Actively Confirm Vendor Remediation |
| :--- | :--- | :--- |
| **Reactive** | 70% | 26% |
| **Building** | 48% | 49% |
| **Operational** | 32% | 68% |
| **Optimized** | 13% | 87% |

### Trail Marker: Industry Benchmarks Challenge Assumptions
Vendor remediation validation varies meaningfully by industry.

- **Highest Active Validation Rates**:
  - Telecommunications: 68%
  - Energy, Extraction & Utilities: 63%
  - Retail & Ecommerce: 62%
- **Lowest Active Validation Rates**:
  - Federal Government: 52%
  - Travel & Hospitality: 44%
  - Technology / Software: 38%

### Trail Marker: The Malware-to-Supply-Chain Pipeline
Many supply chain identity incidents begin with common exposure hygiene failures rather than sophisticated attacks.
- **23%**: Malware-infected third-party devices
- **22%**: Exposed API keys or app access involving vendors or partners

---

## Section 05: The Cost of a Slower Pace

Know the terrain  

Identity exposure creates an ongoing operational burden that extends far beyond the initial incident. Nearly half (49%) of affected organizations experienced 6 to 10 identity-based events in the past year, while another 13% battled 11 to 25 events, making investigation, remediation, and validation a recurring demand on security teams.

How organizations respond to those exposures has a direct impact on business outcomes.

### In This Section
- Many organizations are still taking the long way around
- Every detour adds pain
- Identity exposure remediation maturity
- What sets identity resilience leaders apart

### 5.1 Many Organizations Are Still Taking the Long Way Around
Organizations relying on manual or case-by-case remediation consistently report greater business impact than those with more automated workflows.

- **Customer or Partner Trust Loss** (Loss of confidence that impacts relationships and future business): 47% (manual) vs. 36% (automated)
- **Increased Incident Response Costs** (Higher spending to investigate, respond, and remediate identity incidents): 39% (manual) vs. 32% (automated)
- **Brand or Reputational Damage** (Negative perception that impacts brand value and market position): 39% (manual) vs. 35% (automated)

### 5.2 Every Detour Adds Pain
Despite the clear benefits of automation, most organizations remain in a transitional phase. While relatively few still rely entirely on manual processes, only about one in five have reached fully optimized remediation and investigation capabilities.

### 5.3 Identity Exposure Remediation Maturity
Organizations relying on manual or case-by-case remediation consistently report greater business impact than those with more automated workflows.

*(67 out of every 100 companies are in transition)*

- **Reactive (12%)**: Respond case-by-case with no consistent process
- **Building (34%)**: Developing repeatable remediation workflows
- **Operational (33%)**: Regularly remediate based on prioritized tasks
- **Optimized (21%)**: Automate and optimize remediation across systems

> **Trail Marker: The Remediation Window Compounds Risk**  
> Every hour between exposure and remediation is time attackers can use what they already have – especially for critical exposures like session cookies and tokens stolen by malware or in phishing attacks. Organizations with automated remediation workflows cut that window significantly and see lower incident response costs and customer trust loss as a result.  
> Automation doesn’t simply improve efficiency. It reduces the time identity exposures remain available for attackers to exploit. Organizations with more automated remediation experience lower operational costs, fewer business impacts, and more consistent response. As identity-based events become more frequent, reducing remediation time becomes a competitive advantage.

### What Sets Identity Resilience Leaders Apart
Automation is one of the clearest operational differences across the Identity Threat Protection Maturity Trail. As organizations mature, they move from manual, reactive workflows to fully automated and orchestrated remediation.

#### Organizations with Fully Automated & Orchestrated Remediation Workflows by Tier:
- **Reactive**: 1%
- **Building**: 11%
- **Operational**: 24%
- **Optimized**: 81%

Fully automated remediation remains rare until organizations reach the Optimized tier. The sharp increase from 24% of Operational organizations to 81% of Optimized organizations highlights automation as one of the defining capabilities that separates trail leaders from the rest of the market.

---

## Section 06: Charting the Path Forward

Know the terrain  

### In This Section
- Get the full picture: expand visibility beyond the perimeter
- Shorten the trail: Automate response and remediation
- Close the loop: Verify vendor remediation

Identity exposure can’t be addressed through a single technology, process, or policy. The strongest programs build operational maturity over time, strengthening visibility, accelerating remediation, and validating outcomes across an expanding identity ecosystem.

The survey findings suggest organizations understand this challenge. The top planned investments over the next 12–18 months reflect a balanced approach rather than a search for a single solution.
- **35%** plan to automate identity-related incident response workflows.
- **32%** plan to enhance supply chain and vendor risk management.
- **31%** plan to reduce identity exposure across employees.

Together, these priorities point to a practical roadmap for reducing identity exposure. The organizations making the greatest progress focus on three operational priorities.

### 1. Get the Full Picture: Expand Visibility Beyond the Perimeter
Leading organizations continuously monitor identity exposure across employees, vendors, any and all devices accessing work applications, session cookies and tokens, AI tools, and NHIs.

As the identity ecosystem expands, visibility must extend beyond traditional user accounts. Organizations that broaden visibility across these exposure types are better positioned to identify emerging risks before they become identity-based incidents.

### 2. Shorten the Trail: Automate Response & Remediation
Visibility without action creates more alerts, not better outcomes. Trail leaders reduce exposure faster through automated investigation, remediation, and validation workflows, reducing the time attackers have to exploit exposed identities.

Key capabilities include:
- Credential Rotation
- Session & Token Revocation
- Privilege Reduction
- Automated Response Orchestration

### 3. Close the Loop: Verify Vendor Remediation
Mature programs do not simply identify third-party exposure. They confirm it has been remediated. Nearly 40% of organizations lack a consistent process to verify vendor remediation, leaving them vulnerable to unresolved identity exposures across third-party ecosystems.

Verifying remediation closes the loop between detection and response, helping make sure identity risks are actually eliminated rather than simply identified.

### What Identity Resilience Leaders Do Consistently
Organizations reaching the Optimized tier consistently:
- Maintain broad visibility across human and non-human identities
- Continuously monitor identity exposure
- Automate investigation and remediation
- Govern AI and NHI access through formal ownership
- Verify remediation across third-party ecosystems

Together, these capabilities distinguish organizations that simply respond to identity exposure from those that manage it as a measurable, repeatable operational discipline.

---

## Section 07: The Journey Ahead

Know the terrain  

### In This Section
- Benchmark your position on the trail

The organizations performing best are not necessarily eliminating identity exposure. They are identifying exposures sooner, responding more consistently, and reducing the operational and business impact when incidents occur.

The difference is operational maturity. Organizations that continuously improve visibility, remediation, governance, and validation are better equipped to stay ahead of an expanding identity attack surface.

### Trail Marker: Benchmark Your Position on the Trail
Where are you on the Identity Threat Protection Maturity Trail? Assess your organization’s capabilities across five key dimensions.

| Capability | Reactive | Building | Operational | Optimized |
| :--- | :---: | :---: | :---: | :---: |
| **Visibility** | | | | |
| **Monitoring** | | | | |
| **Governance** | | | | |
| **Automation** | | | | |
| **Vendor Remediation Verification** | | | | |

*Less Mature ➔ More Mature*  
[Benchmark your maturity - Take the assessment]

---

## Appendix – Methodology

### 01. Respondents
This report is based on a survey of 750 cybersecurity decision-makers and practitioners conducted in June 2026. Results are reported at a 95% confidence level with a ±3.58% margin of error.

- **Security architect or engineer**: 23%
- **Identity and access management (IAM) director, manager, or specialist**: 22%
- **Security director, manager, or team lead**: 20%
- **CIO, CISO, or IT security executive**: 19%
- **Security operator, analyst, or incident responder**: 11%
- **Security administrator**: 3%
- **Other role in IT security**: 2%

### 02. Company Size
- **500–999 employees**: 20%
- **1,000–4,999 employees**: 42%
- **5,000–9,999 employees**: 29%
- **10,000–25,000 employees**: 8%
- **More than 25,000 employees**: 1%

### 03. Geography
- **United States**: 27%
- **Canada**: 20%
- **United Kingdom**: 20%
- **Select European markets (Spain, Germany, The Netherlands, Austria, Switzerland)**: 33%

### 04. Industries
- **Manufacturing**: 13%
- **Healthcare**: 12%
- **Energy, Extraction and Utilities**: 11%
- **Insurance**: 11%
- **Retail & Ecommerce**: 11%
- **Financial Services / Banking**: 10%
- **Professional Services**: 8%
- **Technology / Software**: 8%
- **Telecommunications**: 5%
- **Education**: 4%
- **Government – Federal**: 3%
- **Government – State/Local**: 2%
- **Travel & Hospitality**: 2%

### About SpyCloud
SpyCloud transforms recaptured identity data from the criminal underground into actionable intelligence that helps organizations prevent, detect, and respond to identity-based threats. Its automated identity threat protection solutions help stop ransomware and account takeover, detect insider threats, protect employee and consumer identities, and accelerate cybercrime investigations.

To learn more about SpyCloud’s holistic approach to identity threat protection and see your organization’s exposed identity data, visit [spycloud.com »](spycloud.com)

<!-- CONVERSION_METADATA: {"source": "https://github.com/jacobdjwilson/awesome-annual-security-reports", "date": "2026-10-02", "model": "gemini-3.5-flash-lite"} -->
