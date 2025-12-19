# BSIMM12 Digest: The CISO’s Guide to Next-Gen AppSec

## Table of Contents
- [Introduction](#introduction)
- [What is BSIMM?](#what-is-bsimm)
- [Key AppSec trends in BSIMM12](#key-appsec-trends-in-bsimm12)
- [Emerging AppSec activities in BSIMM12](#emerging-appsec-activities-in-bsimm12)
- [BSIMM12 findings by industry](#bsimm12-findings-by-industry)
- [Using BSIMM to improve AppSec programs](#using-bsimm-to-improve-appsec-programs)
  - [1. Identify maturity phase](#1-identify-maturity-phase)
  - [2. Embrace DevSecOps](#2-embrace-devsecops)
  - [3. Implement key activities](#3-implement-key-activities)
  - [4. Define roles and responsibilities](#4-define-roles-and-responsibilities)
  - [5. Getting started](#5-getting-started)
- [Next steps](#next-steps)
- [The Synopsys difference](#the-synopsys-difference)

---

## Introduction

As the rate of software development accelerates, organizations are forced to adopt new practices and undergo cultural shifts. DevOps, with its focus on rapid service delivery, was born of these needs. When done right, the DevOps approach helps organizations build reliable software quickly, with fewer roadblocks than agile or waterfall methodologies.

But with change comes challenges. Many organizations have struggled to adapt and improve their application security (AppSec) practices to keep pace with development cycles. Even after shifting left and investing in tooling integrations, many continue to push vulnerable code into production. Getting the right mix of tools, people, and processes is a constant challenge. Using too few tools leaves gaps in the security posture, while using too many tools leads to friction and tool fatigue for developers.

How can security leaders know how much is too much when it comes to their AppSec activities? How little is too little? What investment makes sense for their organization? What investment is overspending or duplicating efforts?

These are the questions that Synopsys Building Security In Maturity Model (BSIMM) and its annual report were created to answer.

## What is BSIMM?

In 2008, consultants, researchers, and data experts in what is now the Synopsys Software Integrity Group set out to gather data on the various paths that organizations take to address the challenges of software security. Their goal was to examine organizations that were highly effective in software security initiatives, conduct in-person interviews on those organizations’ activities, and then publish their findings.

The BSIMM report—now annual and in its 12th iteration—offers a unique perspective based on data gleaned from real-world observations. It provides CISOs and other security leaders with a model and framework to test, measure, and benchmark their own software security programs, including key activities, practices, and tools to consider implementing.

Regardless of how well-known the organization or how mature its AppSec program, executives can use BSIMM as a measuring stick to gauge themselves against industry trends, risks, priorities, and other factors. When used to its full capacity, BSIMM functions as a roadmap for creating or improving a successful AppSec program that is tailored to the specific needs of each organization. Executives can identify their own goals and objectives and then layer in BSIMM data to determine where additional effort and investment are needed.

![Page 2 footer with synopsys.com](Image description: Page 2 footer with synopsys.com)

## Key AppSec trends in BSIMM12

Each year, BSIMM reveals key market trends and what they mean for AppSec leaders. These trends indicate overarching, or more holistic, shifts in how industries approach their software security programs. Executives can review these trends to help evolve their own programs by identifying any gaps and determining what activities would be beneficial to add or augment. Some of the key trends are listed below.

### High-profile ransomware and supply chain disruptions spur scrutiny of software security

Over the past two years, BSIMM data shows a 61% increase in the “identify open source” activity and a 57% increase in the “create SLA boilerplate” activity among participating organizations.

### Businesses are learning how to translate risk into numbers

Organizations are exerting more effort to collect and publish their software security initiative data, demonstrated by a 30% increase of the “publish data about software security internally” activity over the past 24 months.

### Increased capabilities for cloud security

Increased executive attention, likely combined with engineering-led efforts, has resulted in organizations developing their own capabilities for managing cloud security and evaluating their shared responsibility models. There was an average of 36 new observations over the past two years across activities related to cloud security.

### Security teams are lending resources, staff, and knowledge to DevOps practices

BSIMM data shows software security teams moving away from mandating security behaviors and toward a partnership role, sharing resources, staff, and knowledge with their development peers to ensure security efforts are included in the critical path for software delivery.

### Continuous defect discovery and continuous improvement

BSIMM12 indicates that more organizations are implementing modern defect discovery approaches and favoring continuous monitoring and reporting rather than using a “point in time” defect discovery approach. While governing approaches remain mostly manual, governance-as-code is trending upward and currently observed in 15% of the organizations measured in BSIMM12.

### Security testing in QA automation has doubled

Over the past two years, the “include security tests in QA automation” activity has doubled. In the same time span, the activity “integrate opaque-box security tools into the QA process” increased by more than 50%.

### Building a software Bill of Materials

BSIMM data shows an increase in capabilities focused on inventorying software; creating a software Bill of Materials; understanding how the software was built, configured, and deployed; and on the organization’s ability to redeploy based on security telemetry.

![Page 3 footer with synopsys.com](Image description: Page 3 footer with synopsys.com)

## Emerging AppSec activities in BSIMM12

Activities tend to change over time as the software security environment and organizational priorities change. For example, BSIMM12 data indicates a 61% increase in the “identify open source” activity over the past two years, probably due to the prevalence of open source components in modern software and the rise of attacks using popular open source projects as vectors.

### Highest growth activities over the past 24 months

The activities that showed the highest growth include the following:

*   Use orchestration for containers and virtualized environments (560% increase)
*   Ensure cloud security basics (555% increase)
*   Use application containers to support security goals (214% increase)
*   Include security tests in QA automation (100% increase)
*   Perform design review for high-risk applications (69% increase)
*   Include security resources in onboarding (64% increase)
*   Identify open source (61% increase)

## BSIMM12 findings by industry

Each year, BSIMM offers a glimpse into the current success, weakness, and maturity of organizations within specific industry verticals. This allows CISOs and other security leaders to compare data against their industry peers and pinpoint areas of specific need in their own AppSec programs. BSIMM12 represents 128 organizations across nine verticals.

### Important industry comparisons

Key takeaways from every BSIMM report include which industries outperform their peers. In BSIMM12, FinTech, Internet of Things (IoT), cloud, and independent software vendors (ISVs) stand out.

*   **The leaders in maturity.** IoT, cloud, and ISVs are the three most mature verticals represented in BSIMM12. IoT organizations show the highest level of maturity in practices related to front-loading design (i.e., decisions at earlier stages of the design process), including “training,” “security features and design,” and “architectural analysis.” In the “architecture analysis” practice, IoT organizations are significantly higher than other verticals, perhaps because many IoT devices are expected to function in production environments for long periods of time. Cloud organizations are ahead in the “code review” practice, perhaps due to the explosion of code created by cloud firms over the past few years.
*   **Regulated industries.** Financial services, healthcare, and insurance firms all operate in highly regulated industries. BSIMM12 found that large financial services organizations reacted to regulatory pressures by starting software security programs much earlier than their healthcare and insurance counterparts.
*   **Healthcare.** Despite the similarity of compliance and regulatory drivers across the three verticals, healthcare generally trails insurance and financial services in its software security maturity.
*   **FinTech.** Introduced in BSIMM11, the FinTech vertical exceeds in identifying open source and controlling its risk. IoT organizations are nearly identical in identifying open source, but FinTech organizations show more than double the observation rate in controlling open source risk.

![Page 4 footer with synopsys.com](Image description: Page 4 footer with synopsys.com)

## Using BSIMM to improve AppSec programs

For CISOs new to BSIMM, the depth of data and wealth of information can be intimidating. But regardless of size, maturity level, or industry, security leaders can leverage BSIMM as a roadmap to help develop, improve, and mature their software security programs. The following activities provide a good foundation or starting point.

### 1. Identify maturity phase

BSIMM defines three maturity phases of an AppSec program. Identifying whether an organization is emerging, maturing, or optimizing is a necessary foundation from which to build. Executives should review the common markers of each phase (see chart below) to determine where they currently stand.

| Maturity Phase | Description