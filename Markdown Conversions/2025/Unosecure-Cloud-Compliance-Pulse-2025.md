# Cloud Compliance Pulse 2025

**Organization:** Unosecure  
**Report Title:** Cloud-Compliance-Pulse  
**Year:** 2025

## Table of Contents
- [Executive Summary](#executive-summary)
- [Part 1: Half-year compliance benchmark](#part-1-half-year-compliance-benchmark)
- [Part 2: Cloud-provider deep dives](#part-2-cloud-provider-deep-dives)
- [Part 3: Regulatory radar](#part-3-regulatory-radar)
- [Part 4: Identity-driven breach casebook](#part-4-identity-driven-breach-casebook)

---

## Executive Summary

From the Unosecur Research & Intelligence Team: July 2025

[Link to full document](https://docs.google.com/document/d/1Xsix1agtUPtEdEM8cLA2vQxO5ANPg_xcsOyAk7A_FgE/edit?tab=t.0#heading=h.xaygixsl9xkj)

Every board is now on the hook for two promises: “Innovate fast” and “Never be tomorrow’s breach headline.” Yet most published cloud-security studies rely on self-reported surveys that can’t be traced back to real controls—or they’re dominated by one region or industry. Our enterprise customers told us they need something different: a data-pure, statistically balanced view of where cloud-control hygiene really breaks down so they can justify budgets, tune roadmaps, and walk into audits with hard numbers instead of anecdotes.

### How we built a credible snapshot
Between 1 January and 30 June 2025, 169 organisations ran our free Identity-Security Posture Test. We drew a stratified random sample of 50 firms, balanced across industry, geography, and primary cloud provider, to hit a 90% confidence level with ±10% precision while still publishing on a half-year cadence. Every record is an automated scan mapped directly to ISO 27001/27002, PCI DSS v4, SOC 2, CIS v8, and GDPR clauses; all company identifiers were pseudonymized in line with GDPR. The result is laboratory-grade data that a regulator, insurer, or auditor can reproduce.

### Key Insights
- **40** is the average control failures per tenant.
- **98%** of firms had at least one high-severity gap in the sample.
- **Cloud-specific weak spots:** AWS = password-only admins; GCP = project-wide TokenCreator roles; Azure = subscription-level “Owner/Contributor.”
- **70%** of high-severity findings stem from four gap families: missing MFA, over-privileged roles, stale or duplicate credentials, and unmanaged service-account keys.
- **68%** of tenants violated ISO 27002 - 5.17: privileged accounts without MFA (#1 violated clause).

---

## Part 1: Half-year compliance benchmark

**Coverage window:** 1 January – 30 June 2025  
**Sample analysed:** 50 organisations

Most public “state-of-cloud-security” studies pool breach anecdotes or self-reported surveys. Our benchmark is different: every data point comes from an automated control scan that maps one-for-one to ISO 27001, PCI DSS v4, SOC 2, CIS v8, and GDPR clauses. 

The 50-company sample is 18 tech/SaaS, 9 financial, 8 healthcare, 8 retail, 7 manufacturing, with 23 based in the AWS-heavy Americas, 16 in EMEA where AWS and GCP are evenly split, and 11 in Azure-dominant APAC.

### Global headline findings
**Ten most-broken cloud-control checks in our 50-organisation benchmark**

| Rank | Control violated (plain wording) | Orgs affected (out of 50) | % of sample |
| :--- | :--- | :--- | :--- |
| 1 | Admin account without MFA (ISO 27002 § 5.17) | 34 | 68% |
| 2 | Project-wide Service-Account User / TokenCreator role (GCP) | 26 | 52% |
| 3 | No separation-of-duties on KMS keys | 24 | 48% |
| 4 | No SoD on service-account roles | 23 | 46% |
| 5 | Write permissions granted with no business justification | 22 | 44% |
| 6 | User-managed service-account keys older than 90 days | 21 | 42% |
| 7 | Self-managed SA keys instead of provider-managed | 20 | 40% |
| 8 | Users bypassing corporate SSO for local log-ins | 20 | 40% |
| 9 | Service account with Admin privileges | 19 | 38% |
| 10 | Human user allowed to impersonate service accounts | 18 | 36% |

### Breakdown by cloud service provider
![Chart showing cloud provider distribution: AWS 63%, Azure 23%, GCP 14%]

- **AWS:** 23 companies scanned.
- **Azure:** 10 companies scanned.
- **GCP:** 13 companies scanned.

---

## Part 2: Cloud-provider deep dives

### AWS IAM & Cloud Security (Q1–Q2 2025)
- **Jan 16, 2025:** CVE-2025-0693 (IAM Username Enumeration Flaw) - Fixed by normalizing response times.
- **Feb 2025:** CVE-2025-1969 (TEAM Feature Spoofing Flaw) - Fixed in TEAM v1.2.2.
- **Mar 2025:** CVE-2025-2598 (Credential Leak in AWS CDK CLI) - Fixed in v2.178.2.
- **Mar 2025:** Path Traversal in EC2 SSM Agent - Fixed in versions ≥3.3.1802.0.

### Microsoft Azure Vulnerabilities
- **CVE-2025-29813:** Azure DevOps token hijacking (CVSS 10.0). Mitigated by Microsoft.
- **CVE-2025-29972:** Azure Storage Resource Provider SSRF. Patched.
- **CVE-2025-29827:** Elevation-of-Privilege in Azure Automation. Patched.
- **CVE-2025-47733:** Azure Power Apps data exposure. Patched.

### Google Cloud Platform
- **Jan 2025:** “ImageRunner” bug in Cloud Run fixed.
- **Apr 2025:** “ConfusedComposer” issue in Cloud Composer fixed.
- **Apr 2025:** CVE-2025-4600 (Parsing bug in Classic Load Balancer) fixed.

---

## Part 3: Regulatory radar

### Global Overview
- **EU:** DORA entered into force 17 Jan 2025. eIDAS 2.0 implementing acts adopted May 2025.
- **India:** Digital Personal Data Protection Act (2023) in force since 26 Oct 2024.
- **United States:** New Jersey A3912 (AI/Deepfake identity theft). CISA/White House pushing Zero Trust mandates.
- **EU AI Act:** Expected mid-2025, classifying AI systems by risk and requiring identity management for high-risk AI.

---

## Part 4: Identity-driven breach casebook

### Healthcare/Education
- **PowerSchool (US):** 62 million records exfiltrated via compromised employee password.
- **Western Sydney Univ (Australia):** OneLogin SSO credentials compromised.
- **Ascension Health (US):** 437,329 records stolen via third-party cloud interface flaw.

### Finance/Business
- **TD Bank (US):** Insider threat/credential stuffing incident.
- **Freddie Mac (US):** Consumer data breach reported Feb 2025.
- **Hertz (US):** Partner (Cleo Communications) breach via stolen credentials.
- **VeriSource (US):** 4 million records exfiltrated via stolen credentials.

### Telecom/Technology
- **Orange Group (Romania):** 600K records stolen via compromised operational credentials.
- **Telefónica (Spain):** 2.3 GB of data exfiltrated via stolen employee credentials.
- **SK Telecom (South Korea):** Admin credentials stolen, millions of records affected.
- **Marks & Spencer (UK):** Ransomware attack via phished admin credentials.

---

*For identity security, they trust us. Ready to secure your enterprise identities? Take a free risk assessment!*

**Unosecur | Unified Identity Fabric at Runtime**