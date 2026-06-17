# Cloud Compliance Pulse 2025
## The half-year cloud identity and access compliance benchmark

## Table of Contents
- [Executive Summary](#executive-summary)
- [Part 1: Half-year compliance benchmark](#part-1-half-year-compliance-benchmark)
- [Part 2: Cloud-provider deep dives](#part-2-cloud-provider-deep-dives)
- [Part 3: Regulatory radar](#part-3-regulatory-radar)
- [Part 4: Identity-driven breach casebook](#part-4-identity-driven-breach-casebook)

---

## Executive Summary
From the Unosecur Research & Intelligence Team: July 2025

Every board is now on the hook for two promises: “Innovate fast” and “Never be tomorrow’s breach headline.” Yet most published cloud-security studies rely on self-reported surveys that can’t be traced back to real controls—or they’re dominated by one region or industry. Our enterprise customers told us they need something different: a data-pure, statistically balanced view of where cloud-control hygiene really breaks down so they can justify budgets, tune roadmaps, and walk into audits with hard numbers instead of anecdotes.

### How we built a credible snapshot
Between 1 January and 30 June 2025, 169 organisations ran our free Identity-Security Posture Test. We drew a stratified random sample of 50 firms, balanced across industry, geography, and primary cloud provider, to hit a 90% confidence level with ±10% precision while still publishing on a half-year cadence. Every record is an automated scan mapped directly to ISO 27001/27002, PCI DSS v4, SOC 2, CIS v8, and GDPR clauses; all company identifiers were pseudonymized in line with GDPR. The result is laboratory-grade data that a regulator, insurer, or auditor can reproduce.

### What Part 1 tells: Key insights
- **40**: is the average of control failures per tenant.
- **98%**: of firms had at least one high-severity ISO 27002 - 5.17: privileged accounts without MFA gap in the sample (the #1 violated clause).
- **68%**: of high-severity findings stem from four gap families: missing MFA, over-privileged roles, stale or duplicate credentials, and unmanaged service-account keys.
- **Cloud-specific weak spots**: 
    - AWS = password-only admins
    - GCP = project-wide TokenCreator roles
    - Azure = subscription-level “Owner/Contributor”

1. Missing MFA and excessive privilege aren’t bleeding-edge threats—they’re unlocked doors that ransomware crews and auditors spot first. These basic gaps are often the entry point for major breaches and compliance failures.
2. Organizations that adopt these controls report clear outcomes: faster audit cycles, reduced cyber-insurance premiums, and a stronger position in enterprise sales engagements.
3. Enforcing four core controls can eliminate most audit findings and breach paths: IdP-based MFA, just-in-time admin elevation, automatic rotation of keys older than 30 days, and vaulting service-account secrets.
4. Unosecur’s platform—and this benchmark—exist to make that shift measurable every six months, helping teams stay proactive and accountable.

---

## Part 1: Half-year compliance benchmark
**Coverage window:** 1 January – 30 June 2025
**Sample analysed:** 50 organisations

Most public “state-of-cloud-security” studies pool breach anecdotes or self-reported surveys. Our benchmark is different: every data point comes from an automated control scan that maps one-for-one to ISO 27001, PCI DSS v4, SOC 2, CIS v8, and GDPR clauses. Because we stratified by industry, geography, and primary cloud provider, security leaders can compare their estate against peers on an apples-to-apples basis.

Consider this study as a market-wide “medical check-up” for cloud security. The 50-company sample is 18 tech/SaaS, 9 financial, 8 healthcare, 8 retail, 7 manufacturing, with 23 based in the AWS-heavy Americas, 16 in EMEA where AWS and GCP are evenly split, and 11 in Azure-dominant APAC.

### Global headline findings
**Ten most-broken cloud-control checks in our 50-organisation benchmark**

| Rank | Control violated (plain wording) | Orgs affected (out of 50) | % of sample | Why it matters |
| :--- | :--- | :--- | :--- | :--- |
| 1 | Admin account without MFA (ISO 27002 § 5.17) | 34 | 68% | One phished password can hand over the whole cloud estate. |
| 2 | Project-wide Service-Account User / TokenCreator role (GCP) | 26 | 52% | Any workload can mint tokens for every service account. |
| 3 | No separation-of-duties on KMS keys | 24 | 48% | One person can both create and decrypt master keys. |
| 4 | No SoD on machine privileges, service-account roles | 23 | 46% | The same user grants and uses privileges, hiding abuse. |
| 5 | Write permissions granted with no business justification | 22 | 44% | Auditors flag it as a PCI DSS v4 Req 7.2 breach. |
| 6 | User-managed permanent, MFA-less service-account keys older than 90 days | 21 | 42% | Leaked JSON key = MFA-less API access. |
| 7 | Self-managed SA keys instead of provider-managed | 20 | 40% | Keys sit in code repos; no auto-revocation on staff exit. |
| 8 | Users bypassing corporate SSO for local log-ins | 20 | 40% | Breaks MFA policy and central logging; SOC 2 CC6 hit. |
| 9 | Service account with Admin privileges | 19 | 38% | Malware running as the build bot gets root-like power. |
| 10 | Human user allowed to impersonate service accounts | 18 | 36% | An insider can act as any workload, blurring audit trails. |

### Breakdown by cloud service provider
![Chart showing AWS, GCP, and Azure findings distribution]

- **AWS**: 23 organisations scanned (63% of total findings).
- **GCP**: 13 organisations scanned (10% of total findings).
- **Azure**: 14 organisations scanned (27% of total findings).

---

## Part 2: Cloud-provider deep dives
### 2025 IAM & Cloud Security Incidents (Q1–Q2)

#### AWS
- **CVE-2025-0693**: IAM Username Enumeration Flaw (Jan 2025). Resolved by normalizing response times.
- **CVE-2025-1969**: TEAM Feature Spoofing Flaw (Feb 2025). Patched in TEAM v1.2.2.
- **CVE-2025-2598**: Credential Leak in AWS CDK CLI (Mar 2025). Fixed in v2.178.2.
- **EC2 SSM Agent**: Path traversal weakness fixed in versions ≥3.3.1802.0.

#### Microsoft Azure
- **CVE-2025-29813**: Azure DevOps token hijacking (CVSS 10.0). Mitigated by Microsoft.
- **CVE-2025-29972**: Azure Storage Resource Provider SSRF.
- **CVE-2025-29827**: Elevation-of-Privilege in Azure Automation.
- **CVE-2025-47733**: Azure Power Apps data exposure.

#### Google Cloud Platform
- **ImageRunner Bug (Cloud Run)**: Fixed Jan 28, 2025.
- **ConfusedComposer (Cloud Composer)**: Fixed April 13, 2025.
- **CVE-2025-4600**: Parsing bug in Classic Load Balancer.

---

## Part 3: Regulatory radar
Globally, regulations are tightening around cloud security, identity management, and AI agents.

- **EU**: DORA (Digital Operational Resilience Act) entered into force Jan 17, 2025. eIDAS 2.0 mandates Digital Identity Wallets. The EU AI Act (expected mid-2025) will classify AI systems by risk.
- **India**: Digital Personal Data Protection Act (2023) in force since Oct 2024.
- **China**: Mandates real-name verification for online identities.
- **United States**: New Jersey A3912 expands identity theft to include AI/deepfakes. CISA and the White House continue pushing Zero Trust mandates.

---

## Part 4: Identity-driven breach casebook
Major breaches since January 2025 attributable to stolen or misused identities:

- **Healthcare/Education**:
    - **PowerSchool**: 62 million records accessed via compromised employee password.
    - **Western Sydney Univ**: OneLogin SSO credentials compromised.
    - **Ascension Health**: 437,329 patients affected via cloud-based interface flaw.
- **Finance/Business**:
    - **TD Bank**: Insider threat/credential misuse (2022 incident, disclosed 2025).
    - **Hertz**: Cleo Communications vendor breach via stolen credentials.
    - **VeriSource**: 4 million records exfiltrated via stolen credentials.
- **Telecom/Technology**:
    - **Orange Group**: 600K records stolen via compromised operational credentials.
    - **Telefónica**: Internal ticketing system breach via stolen employee credentials.
    - **SK Telecom**: Malware exfiltrated data via stolen admin credentials.
    - **Marks & Spencer**: Scattered Spider ransomware via phished admin credential.

---

## Identity hygiene now, resilient cloud tomorrow: Takeaways
1. **MFA everywhere**: AWS, Azure, and regulatory bodies (HIPAA/DORA) are making MFA non-negotiable.
2. **Mature machine-identity governance**: Token provenance and AI-agent tagging are becoming audit requirements under PCI DSS 4.0 and NIST 800-63.
3. **Live evidence over static attestations**: Insurers and regulators now demand real-time dashboards proving least privilege and key hygiene.

_Unosecur | Unified Identity Fabric at Runtime_