# Cloud Compliance Pulse 2025

## Table of Contents
- [Executive Summary](#executive-summary)
  - [How we built a credible snapshot](#how-we-built-a-credible-snapshot)
  - [What Part 1 tells: Key insights](#what-part-1-tells-key-insights)
- [Part 1: Half-yearly cloud-compliance benchmark](#part-1-half-yearly-cloud-compliance-benchmark)
  - [Global headline ﬁndings](#global-headline-ﬁndings)
    - [Ten most-broken cloud-control checks in our 50-organisation benchmark](#ten-most-broken-cloud-control-checks-in-our-50-organisation-benchmark)
  - [Breakdown by cloud service provider](#breakdown-by-cloud-service-provider)
    - [Cloud compliance ﬁndings: Overview](#cloud-compliance-ﬁndings-overview)
  - [Top compliance violations and business impact](#top-compliance-violations-and-business-impact)
  - [Recommendations at a glance](#recommendations-at-a-glance)
- [Part 2: Cloud-provider deepdives](#part-2-cloud-provider-deepdives)
  - [Cloud security and IAM vulnerabilities](#cloud-security-and-iam-vulnerabilities)
  - [2025 IAM & Cloud Security Incidents (Q1–Q2)](#2025-iam--cloud-security-incidents-q1q2)
  - [Vulnerabilities and Fixes related to IAM (Early 2025)](#vulnerabilities-and-fixes-related-to-iam-early-2025)
    - [January 16, 2025](#january-16-2025)
      - [CVE-2025-0693: IAM Username Enumeration Flaw](#cve-2025-0693-iam-username-enumeration-ﬂaw)
    - [February 2025 (Early)](#february-2025-early)
      - [CVE-2025-1969: TEAM Feature Spooﬁng Flaw](#cve-2025-1969-team-feature-spooﬁng-ﬂaw)
    - [March 2025](#march-2025)
      - [CVE-2025-2598: Credential Leak in AWS CDK CLI](#cve-2025-2598-credential-leak-in-aws-cdk-cli)
      - [Path Traversal in EC2 SSM Agent (Reported by Cymulate)](#path-traversal-in-ec2-ssm-agent-reported-by-cymulate)
      - [CVE-2025-21614 / ALAS-2025-2739: DoS in Amazon Linux SSM Agent](#cve-2025-21614--alas-2025-2739-dos-in-amazon-linux-ssm-agent)
  - [Microsoft Azure Vulnerabilities and Mitigations (First Half of 2025)](#microsoft-azure-vulnerabilities-and-mitigations-first-half-of-2025)
    - [CVE-2025-29813 (Azure DevOps token hijacking)](#cve-2025-29813-azure-devops-token-hijacking)
    - [CVE-2025-29972 (Azure Storage Resource Provider SSRF)](#cve-2025-29972-azure-storage-resource-provider-ssrf)
    - [CVE-2025-29827 (Elevation-of-Privilege in Azure Automation)](#cve-2025-29827-elevation-of-privilege-in-azure-automation)
    - [CVE-2025-47733 (Azure Power Apps data exposure)](#cve-2025-47733-azure-power-apps-data-exposure)
    - [Azure Misconﬁgurations](#azure-misconﬁgurations)
    - [Microsoft’s Mitigation Measures](#microsofts-mitigation-measures)
  - [Google Cloud Platform Vulnerabilities and Fixes (Early 2025)](#google-cloud-platform-vulnerabilities-and-fixes-early-2025)
    - [January 2025](#january-2025)
      - [“ImageRunner” Bug in Cloud Run](#imagerunner-bug-in-cloud-run)
    - [April 2025](#april-2025)
      - [“ConfusedComposer” Issue in Cloud Composer](#confusedcomposer-issue-in-cloud-composer)
      - [CVE-2025-4600: Parsing Bug in Classic Load Balancer](#cve-2025-4600-parsing-bug-in-classic-load-balancer)
      - [Login Flaw in Looker BI](#login-ﬂaw-in-looker-bi)
    - [General / Ongoing Improvements](#general--ongoing-improvements)
      - [IAM Hardening Across GCP](#iam-hardening-across-gcp)
- [Part 3: Regulatory radar](#part-3-regulatory-radar)
  - [Legal provisions: cloud security, IAM, AI identities](#legal-provisions-cloud-security-iam-ai-identities)
  - [Global Overview](#global-overview)
  - [Regional Trend: Data & AI Laws Impacting Cloud IAM](#regional-trend-data--ai-laws-impacting-cloud-iam)
    - [AI Governance Rising Across APAC](#ai-governance-rising-across-apac)
    - [Emerging Standards for AI Identity Management](#emerging-standards-for-ai-identity-management)
  - [United States](#united-states)
    - [State-Level Identity Law Expansion](#state-level-identity-law-expansion)
    - [Federal Enforcement Action](#federal-enforcement-action)
    - [National IAM Mandates & Zero Trust Push](#national-iam-mandates--zero-trust-push)
    - [Legislative & Standards Evolution](#legislative--standards-evolution)
  - [European Union](#european-union)
    - [Regulatory Momentum Beyond DORA and eIDAS 2.0](#regulatory-momentum-beyond-dora-and-eidas-20)
    - [EU AI Act (Expected Mid-2025)](#eu-ai-act-expected-mid-2025)
    - [GDPR and ePrivacy Rule Evolution](#gdpr-and-eprivacy-rule-evolution)
    - [Enforcement Highlights (2025)](#enforcement-highlights-2025)
    - [Policy Direction: Strong Authentication & Transparency](#policy-direction-strong-authentication--transparency)
- [Part 4: Identity-driven breach casebook](#part-4-identity-driven-breach-casebook)
  - [Data breaches and identity-based threats](#data-breaches-and-identity-based-threats)
  - [Healthcare/Education](#healthcareeducation)
  - [Finance/Business](#financebusiness)
  - [Government/Public Sector](#governmentpublic-sector)
  - [Telecom/Technology](#telecomtechnology)
  - [Identity hygiene now, resilient cloud tomorrow: Takeaways and next steps](#identity-hygiene-now-resilient-cloud-tomorrow-takeaways-and-next-steps)

---

## Executive Summary
From the Unosecur Research & Intelligence Team: July 2025

[https://docs.google.com/document/d/1Xsix1agtUPtEdEM8cLA2vQxO5ANPg_xcsOyAk7A_FgE/edit?tab=t.0#heading=h.xaygixsl9xkj](https://docs.google.com/document/d/1Xsix1agtUPtEdEM8cLA2vQxO5ANPg_xcsOyAk7A_FgE/edit?tab=t.0#heading=h.xaygixsl9xkj)

Every board is now on the hook for two promises: “Innovate fast” and “Never be tomorrow’s breach headline.” Yet most published cloud-security studies rely on self-reported surveys that can’t be traced back to real controls—or they’re dominated by one region or industry. Our enterprise customers told us they need something different: a data-pure, statistically balanced view of where cloud-control hygiene really breaks down so they can justify budgets, tune roadmaps, and walk into audits with hard numbers instead of anecdotes.

### How we built a credible snapshot
Between 1 January and 30 June 2025, 169 organisations ran our free Identity-Security Posture Test. We drew a stratiﬁed random sample of 50 ﬁrms, balanced across industry, geography, and primary cloud provider, to hit a 90% conﬁdence level with ±10% precision while still publishing on a half-year cadence. Every record is an automated scan mapped directly to ISO 27001/27002, PCI DSS v4, SOC 2, CIS v8, and GDPR clauses; all company identiﬁers were pseudonymized in line with GDPR. The result is laboratory-grade data that a regulator, insurer, or auditor can reproduce.

### What Part 1 tells: Key insights
1.  40 is the average control failures per tenant.
2.  98% of ﬁrms had at least one high-severity gap in the sample.
3.  Cloud-speciﬁc weak spots: AWS = password-only admins; GCP = project-wide TokenCreator roles; Azure = subscription-level “Owner/Contributor.”
4.  70% of high-severity ﬁndings stem from four gap families: missing MFA, over-privileged roles, stale or duplicate credentials, and unmanaged service-account keys.
5.  68% of tenants violated ISO 27002 - 5.17: privileged accounts without MFA (#1 violated clause).

Missing MFA and excessive privilege aren’t bleeding-edge threats—they’re unlocked doors that ransomware crews and auditors spot ﬁrst. These basic gaps are often the entry point for major breaches and compliance failures.

Enforcing four core controls can eliminate most audit ﬁndings and breach paths: IdP-based MFA, just-in-time admin elevation, automatic rotation of keys older than 30 days, and vaulting service-account secrets.

Organizations that adopt these controls report clear outcomes: faster audit cycles, reduced cyber-insurance premiums, and a stronger position in enterprise sales engagements.

Unosecur’s platform—and this benchmark—exist to make that shift measurable every six months, helping teams stay proactive and accountable.

## Part 1: Half-yearly cloud-compliance benchmark
Coverage window: 1 January – 30 June 2025
Sample analysed : 50 organisations

Most public “state-of-cloud-security” studies pool breach anecdotes or self-reported surveys. Our benchmark is different: every data point comes from an automated control scan that maps one-for-one to ISO 27001, PCI DSS v4, SOC 2, CIS v8, and GDPR clauses. Because we stratiﬁed by industry, geography, and primary cloud provider, security leaders can compare their estate against peers on an apples-to-apples basis.

Consider this study as a market-wide “medical check-up” for cloud security. Instead of self-reported surveys, it uses real diagnostic scans, so the ﬁndings are as concrete as blood test numbers. If your competitors are showing high cholesterol (weak MFA, stale keys), you need to know where you stand before the next breach or audit hits the headlines.

The 50-company sample is 18 tech/SaaS, 9 ﬁnancial, 8 healthcare, 8 retail, 7 manufacturing, with 23 based in the AWS-heavy Americas, 16 in EMEA where AWS and GCP are evenly split, and 11 in Azure-dominant APAC.

Like any credible market survey, results depend on how you pick the sample. We deliberately balanced companies by size, industry, and geography, so no single giant bank or West Coast tech ﬁrm can tilt the averages. That means you can trust that the percentages represent “normal” businesses, not just outliers.

### Global headline ﬁndings
#### Ten most-broken cloud-control checks in our 50-organisation benchmark

| Rank | Control violated (plain wording) | Orgs affected (out of 50) | % of sample | Why it matters |
| :--- | :------------------------------ | :------------------------ | :---------- | :------------- |
| 1    | Admin account without MFA (ISO 27002 § 5.17) | 34 | 68% | One phished password can hand over the whole cloud estate. |
| 2    | Project-wide Service-Account User / TokenCreator role (GCP) | 26 | 52% | Any workload can mint tokens for every service account. |
| 3    | No separation-of-duties on KMS keys | 24 | 48% | One person can both create and decrypt master keys. |
| 4    | No SoD on service-account roles | 23 | 46% | The same user grants and uses machine privileges, hiding abuse. |
| 5    | Write permissions granted with no business justiﬁcation | 22 | 44% | Auditors ﬂag it as a PCI DSS v4 Req 7.2 breach. |
| 6    | User-managed service-account keys older than 90 days | 21 | 42% | Leaked JSON key = permanent, MFA-less API access. |
| 7    | Self-managed SA keys instead of provider-managed | 20 | 40% | Keys sit in code repos; no auto-revocation on staff exit. |
| 8    | Users bypassing corporate SSO for local log-ins | 20 | 40% | Breaks MFA policy and central logging; SOC 2 CC6 hit. |
| 9    | Service account with Admin privileges | 19 | 38% | Malware running as the build bot gets root-like power. |
| 10   | Human user allowed to impersonate service accounts | 18 | 36% | An insider can act as any workload, blurring audit trails. |

### Breakdown by cloud service provider
On average, each company had 40 cloud control failures. Think of them as unlocked doors or spare keys under the mat. Nearly all ﬁrms had at least one high-risk gap, and the worst offender (missing MFA on admin accounts) is the digital equivalent of leaving the server room unlocked.

Different clouds have different ways of optimal working. In AWS, too many admins still operate without two-factor login. In Google Cloud, machine accounts hold sweeping powers. In Azure, companies leave subscription-wide “Owner” roles lying around. If you run multi-cloud, you can’t assume one provider’s settings protect you in another.

#### Cloud compliance ﬁndings: Overview
![Pie chart showing cloud compliance findings by provider: AWS 63% (23 organizations scanned), Azure 27% (14 organizations scanned), GCP 10% (13 organizations scanned).](https://example.com/cloud-compliance-findings-overview.png)

1.  AWS is also the most-used platform in the study (23 of 50 companies), but even after adjusting for that, AWS still shows the highest per-tenant failure count.
2.  This does not mean AWS is inherently less secure; it means customers are running more workloads there and leaving more controls unchecked.
3.  Azure’s low share may reﬂect lighter adoption or incomplete scanner onboarding, so organisations should conﬁrm all subscriptions are being examined.

### Top compliance violations and business impact
The changing percentage share may partly reﬂect less scanning coverage. What the data tells us is simple: if your company runs on any of these three platforms, you have a ready reckoner of the most common compliance violations. For multi-cloud businesses, this data reinforces that not all environments carry the same risk. Assuming they do could leave serious gaps unaddressed.

Santhosh Jayaprakash
Founder and CEO, Unosecur

| Cloud provider | Top failed control | Typical business impact |
| :------------- | :----------------- | :---------------------- |
| GCP | Service Account User/TokenCreator at project scope | Token forgery; lateral movement across projects |
| Azure | Owner/Contributor role at subscription level | Unrestricted resource deletion or crypto-mining |
| AWS | IAM user with AdministratorAccess and no MFA | Full-account compromise - ransomware, data exﬁltration |

### Recommendations at a glance
Our half-year benchmark conﬁrms what incident headlines hint: basic identity controls, especially MFA and least-privilege, remain the soft spot in multi-cloud estates. The pattern is plain: most companies still stumble on basic identity hygiene. The good news is the ﬁx list is short, cheap, and measurable. If you tackle these basics now, you’ll not only avoid tomorrow’s breach headlines but also sail through ISO, SOC 2, and PCI audits with fewer ﬁndings and lower insurance costs.

Enabling MFA and pruning admin roles are settings in your identity provider, not multi-year transformations. Rotate old keys and vault machine credentials, and you’ve neutralised 70% of what auditors ﬂagged, often in a single quarter.

1.  **Mandate MFA on every privileged login**: ISO 27002 § 5.17, SOC 2 CC6, PCI 8.5.1.
2.  **Adopt just-in-time