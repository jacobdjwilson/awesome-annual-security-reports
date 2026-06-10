# The Salesforce Threat Landscape 2026: Lessons and Risks for 2026

**Organization:** WithSecure  
**Report Title:** Salesforce-Threat-Landscape-Report  
**Year:** 2026

## Table of Contents
- [Executive summary](#executive-summary)
- [Salesforce Data as a High-Leverage Target](#salesforce-data-as-a-high-leverage-target)
- [Extortion Economics and High-Trust Access Paths](#extortion-economics-and-high-trust-access-paths)
- [WithSecure Cloud Protection for Salesforce: Detection Telemetry and Threat Patterns](#withsecure-cloud-protection-for-salesforce-detection-telemetry-and-threat-patterns)
- [Geographic Distribution of Affected Organizations](#geographic-distribution-of-affected-organizations)
- [Distribution of Malicious Detections by Content Type](#distribution-of-malicious-detections-by-content-type)
- [Top Detections Observed in 2025](#top-detections-observed-in-2025)
- [Examples of Observed Malicious Content](#examples-of-observed-malicious-content)
- [Adversary-in-the-Middle (AitM) Quishing Campaign](#adversary-in-the-middle-aitm-quishing-campaign)
- [Publicly Reported Incidents](#publicly-reported-incidents)
- [Emerging Salesforce Attack Surfaces: Agents, Automation, and Data Flows](#emerging-salesforce-attack-surfaces-agents-automation-and-data-flows)
- [Salesforce Platform Security-Related Changes](#salesforce-platform-security-related-changes)
- [Mitigation and Recommendations](#mitigation-and-recommendations)
- [Conclusion](#conclusion)

---

## Executive summary

In 2025, Salesforce environments became direct targets of sophisticated, financially motivated cybercrime groups. Historically, most Salesforce security incidents were associated with misconfigurations or vulnerabilities identified by security researchers. Over the past year, however, multiple incidents and extortion-driven campaigns demonstrated deliberate targeting of Salesforce data as a high-leverage asset.

Rather than exploiting platform vulnerabilities, attackers relied on social engineering, credential theft, OAuth token misuse, and supply-chain compromise. These techniques enabled access to sensitive customer and business data by abusing legitimate access paths and delegated trust. Recent threat activity further highlights how adversary-in-the-middle phishing can undermine MFA protections at the identity provider layer, reinforcing how Salesforce environments inherit risk from upstream identity decisions even in the absence of platform vulnerabilities.

WithSecure Cloud Protection for Salesforce detection telemetry reinforces this perspective, showing a growing prevalence of URL-driven threats delivered through routine business workflows, including embedded links and QR code lures. These attacks increasingly blend into expected operational activity and extend beyond file-based malware, with files most often acting as containers for malicious links rather than the threat itself.

At the same time, Salesforce continued to expand its platform capabilities through automation, agent-based execution, and AI-driven workflows. While these capabilities deliver significant business value, they also introduce new security considerations. For instance, identity risks increasingly manifest not only at login time, but also through delegated, persistent, and non-human execution contexts.

This report analyses the Salesforce threat landscape in 2025 using WithSecure Cloud Protection for Salesforce detection telemetry alongside publicly disclosed incidents. It examines why Salesforce data has become a high-leverage target, documents key attack paths observed during the year, and assesses emerging risks introduced by automation and agent-based capabilities. The report concludes with governance-aligned defensive considerations for teams responsible for Salesforce integration, oversight, and risk management.

**AUTHOR:** Karmina Aquino, Head of Threat Intelligence, WithSecure Cloud Protection for Salesforce

---

## Salesforce Data as a High-Leverage Target

Salesforce has evolved far beyond its origins as a customer relationship management platform. For many organizations, it now functions as a central system of record for customer data, revenue operations, contractual relationships, and support workflows. Salesforce environments are deeply integrated with internal systems, cloud services, and third-party vendors through APIs and OAuth-based authorization mechanisms.

This evolution has expanded both the value and the attack surface of Salesforce. While traditional enterprise security models focused on perimeter defences and endpoint compromise, Salesforce environments expose data primarily through identity, application trust, and automation.

---

## Extortion Economics and High-Trust Access Paths

Modern cybercrime is mostly financially driven. Threat actors increasingly prioritize techniques that maximize leverage while minimizing operational cost and exposure per intrusion. Extortion economics favour data theft over service disruption.

**Attackers seek platforms that:**
- Store sensitive and regulated data
- Are critical to business operations
- Cause pressure through legal, regulatory, or reputational consequences

**Salesforce environments align closely with these criteria. They commonly contain:**
- Personally identifiable information (PII) governed by GDPR, CCPA, and similar regulations
- Sales forecasts, pipeline data, and contractual and pricing information
- Customer communications and support records

**Salesforce also presents attackers with attractive operational characteristics:**
- API-driven access that blends into normal business activity
- OAuth tokens that bypass interactive authentication
- Integration models that assume long-term trust

These reduce the chances of immediate detection and increase dwell time once access is obtained.

---

## WithSecure Cloud Protection for Salesforce: Detection Telemetry and Threat Patterns

### Malicious Detection Rates Observed in 2025
Based on telemetry from WithSecure Cloud Protection for Salesforce, malicious detection activity increased consistently throughout 2025, with growth accelerating in the second half of the year and reaching a level in Q4 that was approximately eight times higher than in Q1 when measured across all scans.

The acceleration was most evident in Q3 and Q4, possibly reflecting a combination of heightened attacker activity, broader detection coverage, and introduction of new detection mechanisms. Detections during this period align with several publicly reported, high-profile Salesforce-related incidents, suggesting increased adversary focus on the platform. The observed upward trend also indicates improvements in detection visibility over time, as additional detection logic and coverage enabled threats that may previously have gone unnoticed to be identified.

---

## Geographic Distribution of Affected Organizations

Organizations that experience malicious detections during 2025 were distributed across all major geographic regions, indicating that malicious activity targeting Salesforce environments was not confined to a specific location. Affected organizations were observed in North America, Europe, Asia-Pacific, and other regions, underscoring the global nature of the threat activity captured in the telemetry.

While malicious detections were observed worldwide, a significant share of affected organizations was concentrated in a small number of countries. The three most frequently affected countries during 2025 were the United States, the United Kingdom, and Australia, which together accounted for approximately 53.5% of affected organizations. All three are primarily English-speaking regions.

![Geographic distribution chart: Europe 41.56%, North America 38.96%, Oceania 10.39%, Asia-Pacific 7.79%, Africa <1%, South America <1%]

---

## Distribution of Malicious Detections by Content Type

Most malicious detections observed in 2025 were associated with URLs rather than files. Approximately 98% of all malicious detections were URL-based, while file-based detections accounted for a comparatively small share of observed activity. This distribution indicates that malicious activity targeting Salesforce environments during this period relied primarily on web-based delivery mechanisms rather than file-borne malware.

### Observed Patterns in Malicious URLs
Analysis of malicious URLs observed in Salesforce environments during 2025 shows that attacker infrastructure spanned a wide range of domain ages. Newly registered domains were commonly associated with fast-moving phishing campaigns, while longer-lived domains were often reused or repurposed to support multiple attack efforts.

In many cases, even when the underlying domain persisted over time, the specific URLs or subdomains used for malicious activity were short-lived. Attackers frequently rotated these components to support individual campaigns, limit exposure, and evade simple blocking approaches.

---

## Top Detections Observed in 2025

Approximately 95% of malicious files and URLs detected in 2025 were identified using just two detection types. These dominant detections were primarily associated with malicious URLs used in social engineering, phishing, and credential-harvesting campaigns.

Nearly all malicious document detections involved embedded malicious links. In these cases, the document acted as an initial delivery mechanism, with URLs identified during file analysis rather than through direct user interaction. Attackers commonly use this approach because document attachments are typically perceived as legitimate business artifacts, and links embedded within documents often appear less suspicious than standalone URLs.

---

## Examples of Observed Malicious Content

The following examples illustrate how these dominant detections manifested in real-world attacks observed from WithSecure Cloud Protection for Salesforce detection telemetry during 2025.

- **Cloud Storage Phishing:** A phishing message impersonating a legitimate iCloud storage notification, warning recipients that they are nearing their storage limit.
- **Malicious Application Delivery Site:** A URL that prompted users to download a mobile application package from an untrusted source. The malicious app spies on user activities.
- **Multi-stage Salesforce Phishing:** A phishing email impersonating a Salesforce notification, prompting recipients to review an issue via an embedded link. The link redirects to a fraudulent Salesforce login page designed to collect credentials and subsequently presents a fake multi-factor authentication prompt.

---

## Adversary-in-the-Middle (AitM) Quishing Campaign

Detection telemetry from 2025 shows sustained activity associated with QR code phishing or quishing campaigns that leveraged adversary-in-the-middle (AitM) techniques to compromise user identities. These were commonly delivered through email and other routine business communications, using QR codes to shift user interaction away from traditional links.

By prompting users to scan codes with mobile devices, attackers reduced visibility into the destination URL and bypassed many traditional endpoint and email security controls that focus on link inspection. This shift also moved the authentication flow away from the original device, complicating detection and response.

---

## Publicly Reported Incidents

In 2025, multiple publicly reported security incidents indicated that organized cybercriminal groups increasingly targeted Salesforce environments.

- **Identity-Based Access Abuse (Gehenna):** In mid-2025, a threat actor known as Gehenna publicly claimed to have exfiltrated a large volume of CRM data from an organization’s Salesforce environment.
- **OAuth Device Flow Authorization Abuse (UNC6040):** Activity attributed to the threat actor group tracked as UNC6040 was observed compromising multiple large organizations’ Salesforce environments throughout mid-2025. The group abused the OAuth Device Flow authorization to gain access.
- **Supply-Chain Compromise (Salesloft Drift & Gainsight):** These incidents demonstrate how compromise of a single integration vendor can immediately propagate across multiple customer environments, resulting in a broader blast radius.
- **AitM Vishing Attacks:** Campaigns combined AitM phishing kits with vishing (voice phishing) techniques to bypass MFA controls enforced at the identity provider layer.

---

## Emerging Salesforce Attack Surfaces: Agents, Automation, and Data Flows

The evolution of Salesforce from a CRM platform into an automation- and agent-driven ecosystem introduces new attack surfaces. These emerging risks are not defined by exploitation of platform vulnerabilities, but by shifts in how trust, authorization, and decision-making are delegated to non-human systems.

- **Agents as Autonomous Actors:** Actions performed by agents are still executed under an identity and privilege model, but the connection between human intent and execution becomes less direct.
- **Automation as an Amplification Layer:** Automation magnifies the impact of existing access by enabling actions to occur at scale and speed.
- **Data as an Input to Automated Decision-Making:** In data-dependent systems, compromised inputs may alter system behaviour, influence automated processes, or result in unintended information disclosure.

### Proof-of-Concept: ForcedLeak
ForcedLeak is a proof-of-concept demonstrated by security researchers at Noma Labs to illustrate how automated agents interacting with dynamic data sources could be influenced into unintentionally disclosing information.

---

## Salesforce Platform Security-Related Changes

In response to the threats observed, Salesforce implemented several mitigations, such as:
- Preventing Connected app creation through both API and UI
- Restricting uninstalled connected app usage by requiring explicit permissions
- Removing OAuth device flow pathway from Data Loader
- Disabling compromised applications from AppExchange (e.g., Salesloft Drift and Gainsight)
- Enforcing Trusted URL allowlists for Agentforce and Einstein Generative AI agents
- Releasing malicious file scanning capability for Salesforce Files

---

## Mitigation and Recommendations

Effective risk management requires a layered approach designed to address evolving usage patterns and a changing threat landscape.

- **Establish Clear Visibility and Ownership:** Maintain an inventory of users, service accounts, connected applications, agents, and automation workflows.
- **Manage Integration and Third-Party Risk:** Treat Salesforce integrations as extensions of your own environment.
- **Strengthen Identity and Access Governance:** Focus on how access is granted, delegated, and reviewed over time.
- **Monitor for Anomalous Behaviour and Misuse:** Treat anomalous behaviour by trusted identities or systems as a potential indicator of misuse.
- **Governance of Automated and Agent-Based Execution:** Define clear limits on what automated systems and agents are allowed to do.
- **Data Governance and Content Oversight:** Extend governance practices to how data is consumed by automated systems.
- **Prepare for Incident Response and Recovery:** Maintain incident response procedures specific to Salesforce environments.
- **Implement Periodic Security and Configuration Reviews:** Establish a recurring review cadence to reassess Salesforce security posture.

---

## Conclusion

The Salesforce threat landscape in 2025 suggests that attacks targeting Salesforce environments have moved beyond exploratory or opportunistic stages and reached mainstream adoption among financially motivated threat actors. Adversaries rely on delegated authorization, trusted integrations, and routine workflows to reach sensitive data and create leverage over organizations.

Organizations that treat Salesforce security as an ongoing program, supported by layered detection, clear ownership, and periodic control reviews, will be better positioned to manage evolving risk. Security controls that extend visibility into trusted workflows, rather than focusing solely on isolated events or traditional boundaries, will be critical to sustaining resilience as both the platform and threat landscape continue to evolve.

---

ts evolve into
visibility into content and interactions complex, multi-vendor ecosystems that
Content & Data
flowing through Salesforce environments, combine identity providers, integrations,
alongside file-focused protections. automation, and logic-driven workflows,
security risk increasingly emerges from
Looking ahead to 2026 and beyond, how trusted components interact, Automations & Agents
the threat activity observed in 2025 rather than from isolated vulnerabilities or
Expanding trust surfaces in Salesforce environments

The Salesforce Threat Landscape 2026 40 (40)
#1 Cyber Security Solution for
Modern Salesforce Threats
cloudprotection.com