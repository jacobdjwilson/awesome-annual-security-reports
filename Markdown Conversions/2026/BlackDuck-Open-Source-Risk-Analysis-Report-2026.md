# 2026 Open Source Security and Risk Analysis Report

## Table of Contents
- [Welcome to the 2026 OSSRA Report](#welcome-to-the-2026-ossra-report)
- [The Way Software Is Written Has Changed](#the-way-software-is-written-has-changed)
- [The Expanding Attack Surface](#the-expanding-attack-surface)
- [About This Year’s Data](#about-this-years-data)
- [Methodology](#methodology)
- [Industry Coverage](#industry-coverage)
- [The Black Duck KnowledgeBase](#the-black-duck-knowledgebase)
- [Data Collection Period](#data-collection-period)
- [Key Findings](#key-findings)
- [Codebase Complexity Over Time](#codebase-complexity-over-time)
- [How We Identify Open Source](#how-we-identify-open-source)
- [Security Risk: Vulnerabilities](#security-risk-vulnerabilities)
- [Understanding the Drivers](#understanding-the-drivers)
- [High-Risk Vulnerabilities](#high-risk-vulnerabilities)
- [Top Vulnerabilities in 2025](#top-vulnerabilities-in-2025)
- [Supply Chain Attacks: 2025 in Review](#supply-chain-attacks-2025-in-review)
- [AI Model Risk: An Emerging Attack Surface](#ai-model-risk-an-emerging-attack-surface)
- [Vulnerability Patterns by Industry](#vulnerability-patterns-by-industry)
- [Legal and IP Risk: Licensing](#legal-and-ip-risk-licensing)
- [License Conflicts at Historic Highs](#license-conflicts-at-historic-highs)
- [Understanding License Conflicts](#understanding-license-conflicts)
- [Why License Conflicts Are Accelerating](#why-license-conflicts-are-accelerating)
- [The 2,675 Conflicts Finding](#the-2675-conflicts-finding)
- [Top 10 Open Source Licenses](#top-10-open-source-licenses)
- [License Risk Categories](#license-risk-categories)
- [The AI License Challenge](#the-ai-license-challenge)
- [Components Without Licenses](#components-without-licenses)
- [License Conflicts by Industry](#license-conflicts-by-industry)
- [Practical License Governance](#practical-license-governance)
- [Obsolescence Management and Maintenance Debt](#obsolescence-management-and-maintenance-debt)
- [The 90% Problem](#the-90-problem)
- [The Zombie Component Problem](#the-zombie-component-problem)
- [Version Currency](#version-currency)
- [The Update Question](#the-update-question)
- [The EU Cyber Resilience Act](#the-eu-cyber-resilience-act)
- [Implications for Component Governance](#implications-for-component-governance)
- [Industry Maintenance Patterns](#industry-maintenance-patterns)
- [The Value of Discipline](#the-value-of-discipline)
- [Yesterday’s Gone: Living in the AI Era](#yesterdays-gone-living-in-the-ai-era)
- [AI Coding Adoption: The Scale](#ai-coding-adoption-the-scale)
- [The Governance Gap](#the-governance-gap)
- [Shadow AI](#shadow-ai)
- [Conclusion and Recommendations: Addressing Open Source Risk](#conclusion-and-recommendations-addressing-open-source-risk)
- [What the Data Tells Us](#what-the-data-tells-us)
- [What Organizations Need](#what-organizations-need)
- [The Black Duck Application Security Portfolio](#the-black-duck-application-security-portfolio)
- [Introducing Signal: An Evolutionary Addition to the Black Duck Portfolio](#introducing-signal-an-evolutionary-addition-to-the-black-duck-portfolio)
- [Getting Started](#getting-started)
- [About Black Duck](#about-black-duck)

---

## Welcome to the 2026 OSSRA Report

The “Open Source Security and Risk Analysis” (OSSRA) report has been the industry’s definitive look at the state of open source code for a decade. Each year, we analyze anonymized findings from commercial codebases audited by the Black Duck Audit Services team, and this provides an unmatched, real-world view of how open source is used—and sometimes misused—across every major industry. This year’s findings document a pivotal moment: The explosion of AI-assisted development has fundamentally altered the risk landscape for software and the baseline for compliance with new regulatory initiatives such as the EU Cyber Resilience Act (CRA) and the Digital Operational Resilience Act (DORA).

## The Way Software Is Written Has Changed

The mean number of open source vulnerabilities per codebase has more than doubled. License conflicts have surged to their highest levels in OSSRA history, driven largely by the proliferation of third-party dependencies. And the average codebase now contains over 84,000 files—a figure that has quadrupled in just five years.

The urgency of these findings is underscored by real-world attack data: 65% of the organizations Black Duck surveyed in 2025 reported experiencing a software supply chain attack in the past year. These are active threats impacting enterprises across every industry.

The traditional approach to application security was designed for a world where humans wrote code at human speed. Today, AI-generated code is using open source at unprecedented scale, compounding the rate of software development, and AppSec teams are struggling to keep pace. AI coding assistants—tools like GitHub Copilot, Cursor, Claude Code, and Windsurf—are now as fundamental to the developer’s toolkit as a compiler or a debugger. According to Black Duck’s research, 67% of organizations are already using AI-powered coding assistants. And 76% of companies that prohibit their developers from using AI coding assistants acknowledge that they’re being used anyway, against corporate policies.

![Infographic showing 65% of organizations reported a supply chain attack and 76% of companies acknowledge unauthorized AI coding assistant usage.]

The challenges outlined in this report are not caused by AI coding tools themselves, but by the scale and speed they enable. Detecting its use within your supply chain is an evolving challenge facing every organization. Just as open source transformed software development—and is now a permanent fixture in how software is built—AI-assisted coding is here to stay.

This report provides the data you need to understand what’s happening in the open source landscape and how it affects your security, legal, and operational risk posture. Our goal is to give you the insights to make informed decisions in an environment that continues to evolve.

## The Expanding Attack Surface

The number of files per codebase is up 74% year-over-year. Components per application have increased 30%. And the volume of disclosed vulnerabilities continues to accelerate, driven by factors such as the Linux Kernel team’s 2024 decision to become a CVE Numbering Authority—a single change that added thousands of new CVE assignments to kernel-related code.

The result is that security teams face more findings to evaluate, prioritize, and remediate than ever before. This is a reality of application security, not a failing of security tools. The question organizations must answer is whether their security approach has the precision to separate genuine risk from background noise—and whether their security tools provide the intelligence needed to guide remediation decisions.

Organizations relying on surface-level scanning of software—whether from legacy tools or newer AI-only solutions—face a structural disadvantage. This year’s data reveals that audited codebases contain 581 vulnerabilities on average. Clearly, you need more than a list of findings. You need context: exploitability data, remediation guidance, coverage beyond CVE databases, and the ability to detect open source that entered your codebase outside of package managers.

The sections that follow examine what this year’s data reveals across three dimensions of risk: security vulnerabilities, license compliance, and the impact of software obsolescence, also known as operational sustainability. We then discuss how organizations can address these challenges using both established approaches and emerging capabilities.

## About This Year’s Data

The findings in this report are derived from the anonymized data produced by Black Duck Audit Services while auditing commercial and proprietary codebases for M&A transactions, regulatory compliance, and internal risk assessment.

The Black Duck Audit team evaluates and presents audit data by splitting single-customer codebases into multiple analyses, termed “projects.” This technique provides a more granular approach to analyzing increasingly larger customer codebases and presents highly accurate component identification and dependency tracking. While we still refer to customers’ overall “codebases” in the OSSRA, at a more granular level, the 947 codebases submitted to Black Duck between November 2024 and October 2025 entail the analysis of nearly 3,000 individual projects.

### Methodology

| Metric | Value |
| :--- | :--- |
| Codebases scanned | 947 |
| Individual projects analyzed | 2,843 |
| M&A transactions represented | 197 |
| Maximum number of projects associated with a single codebase | 50 |

*Table 1. Scope of analyses 2024-25 (Source: Black Duck Audits)*

Black Duck audits employ multiple detection methods to create a comprehensive inventory of open source components:
- **Dependency analysis**: examines package managers and manifest files.
- **Snippet analysis**: identifies code fragments that match known open source.
- **Binary analysis**: investigates compiled code where source is unavailable.
- **CodePrint analysis**: matches files against the Black Duck KnowledgeBase™.

This multifactor approach is essential for accuracy. Relying solely on declared dependencies—what appears in a package.json or pom.xml—misses a significant portion of the open source present in a codebase, including vendor code, copy-pasted snippets, and transitive dependencies.

## Industry Coverage

The codebases in this year’s analysis span 17 industries, with Enterprise Software/SaaS representing the largest segment at 415 codebases. Notably, Energy and Clean Tech doubled its representation from last year’s report, while Healthcare, Health Tech, and Life Sciences saw a significant decline—shifts that reflect broader M&A activity patterns in these sectors.

## The Black Duck KnowledgeBase

All findings are matched against the Black Duck KnowledgeBase, the most comprehensive and battle-tested repository of open source intelligence in the world. This foundation is what enables Black Duck to deliver verified analysis, exploitability data, and remediation guidance that other tools—including AI-only solutions—can only guess at.

- **3.2 petabytes** of open source software metadata and archives
- **10+ million** open source projects from 58,000+ data sources
- **317,000** vulnerabilities and **63,000** Black Duck Security Advisories delivering vulnerability intelligence
- **3,000** licenses tracked
- **20+ years** of continuous curation by security experts

## Data Collection Period

The findings in this report are based on audits conducted between November 2024 and October 2025, providing the most current view of open source usage and risk available.

## Key Findings

Open source adoption continues to accelerate, and the scale and complexity of open source—along with the risks that accompany it—are growing across every dimension we measure.

| Metric | OSSRA 2025 | OSSRA 2026 | YoY Change |
| :--- | :--- | :--- | :--- |
| Codebases containing open source | 97% | 98% | 1 pt |
| Mean OSS components per application | 911 | 1,180 | 30% |
| Median file count per codebase | 16,082 | 21,672 | 35% |
| Mean file count per codebase | 48,415 | 84,499 | 74% |
| Maximum projects per codebase | 21 | 50 | 138% |

*Table 2. Open source adoption and codebase growth metrics*

As shown in Table 2, open source is now effectively universal in commercial software. Only 2% of the codebases we audited contained no open source components—and even that figure likely represents specialized legacy systems rather than new development. For practical purposes, if you’re building software today, you’re building with open source.

## Codebase Complexity Over Time

The median codebase file count has grown from 16,082 to 21,672 in just one year, a 35% increase that reflects the ongoing growth in application complexity driven by microservices architectures, AI/ML dependencies, and AI-assisted development velocity.

While likely only one of several factors, the timing of the file count growth corresponds with the mainstream adoption of AI coding assistants. GitHub Copilot reached general availability in June 2022; by late 2023, it and its competitors had become standard tools for millions of developers.

## How We Identify Open Source

| Detection Method | Percentage |
| :--- | :--- |
| Automated (Package manager analysis, manifest file scanning) | 84% |
| Deep analysis (Snippet matching, binary analysis, manual review) | 16% |

*Table 4. Open source component detection methods (Source: Black Duck Audits)*

In our audits, 84% of open source components were identified through automated detection methods. But the 16% requiring deeper analysis tells an important story. This code entered the codebase outside of standard package management, through vendor dependencies copied directly into repositories, code snippets pulled from Stack Overflow or generated by AI assistants, or binary components included without source.

## Security Risk: Vulnerabilities

If there’s one finding that defines the 2026 OSSRA, it’s this: Mean vulnerabilities per codebase have more than doubled.

| Metric | 2023–24 | 2024–25 | Change |
| :--- | :--- | :--- | :--- |
| Codebases with at least one vulnerability | 86% | 87% | 1 pt |
| Mean vulnerabilities per codebase | 280 | 581 | 107% |
| Median vulnerabilities per codebase | 59 | 78 | 32% |
| Mean unique vulnerabilities per codebase | 154 | 237 | 54% |
| Maximum vulnerabilities in a single codebase | 34,736 | 38,998 | 12% |

*Table 5. Vulnerability landscape: Key metrics and year-over-year changes*

## Understanding the Drivers

The doubling of mean vulnerabilities reflects multiple converging factors:
1. **Component growth**: 30% more components per codebase.
2. **Component selection patterns**: AI coding assistants tend to suggest popular, well-established libraries which often have longer vulnerability histories.
3. **Development velocity**: AI-assisted development accelerates the rate at which new dependencies enter codebases.
4. **Disclosure acceleration**: The Linux Kernel team became a CVE Numbering Authority (CNA) in early 2024, resulting in a dramatic increase in kernel-related CVE assignments—from 290 in 2023 to over 3,500 in 2024.

## High-Risk Vulnerabilities

| Metric | 2023–24 | 2024–25 |
| :--- | :--- | :--- |
| Codebases with high-risk vulnerabilities | 81% | 78% |
| Codebases with critical-risk vulnerabilities | 48% | 44% |

*Table 7. High- and critical-risk vulnerability trends*

## Top Vulnerabilities in 2025

| Rank | CVE/BDSA | Unique Count | Percentage of Codebases |
| :--- | :--- | :--- | :--- |
| 1 | BDSA-2021-3651 | 998 | 35% |
| 2 | BDSA-2025-2047 (CVE-2025-27789) | 870 | 21% |
| 3 | CVE-2022-25883 | 798 | 21% |
| 4 | BDSA-2020-0964 (CVE-2020-11023) | 791 | 28% |
| 5 | BDSA-2020-0686 (CVE-2020-11022) | 788 | 28% |
| 6 | BDSA-2019-1138 (CVE-2019-11358) | 745 | 27% |
| 7 | BDSA-2014-0063 | 672 | 25% |
| 8 | BDSA-2017-2930 (CVE-2015-9251) | 651 | 25% |
| 9 | BDSA-2024-3717 (CVE-2024-37890) | 632 | 21% |
| 10 | BDSA-2015-0567 | 571 | 23% |

*Table 8. Top 10 most prevalent CVEs and BDSAs in 2025*

## Supply Chain Attacks: 2025 in Review

65% of the organizations Black Duck surveyed in 2025 reported experiencing a software supply chain attack in the past year.
- **66%** of malicious packages were created for typosquatting, dependency confusion, or social engineering.
- **34%** were hijacked legitimate packages.

## AI Model Risk: An Emerging Attack Surface

49% of organizations now include open source AI/ML models in the software they ship. These models present unique governance challenges:
- **Visibility**: They can be embedded in ways that evade standard manifest-based detection.
- **Licensing**: Models often carry unclear or custom terms.
- **Regulatory Pressure**: The EU AI Act requires accountability for model provenance and training data.

## Vulnerability Patterns by Industry

| Industry | % with High/Critical Risk |
| :--- | :--- |
| EdTech | 100% |
| Retail and eCommerce | 93% |
| Financial Services and FinTech | 92% |
| Energy and Clean Tech | 89% |
| Big Data, AI, BI, Machine Learning | 88% |
| Healthcare, Health Tech, Life Sciences | 88% |
| Manufacturing, Industrials, Robotics | 88% |
| Aerospace, Aviation, Automotive, Transportation, Logistics | 87% |
| Telecommunications and Wireless | 87% |
| Cybersecurity | 85% |
| Internet of Things | 85% |
| Marketing Tech | 83% |
| Enterprise Software/SaaS | 80% |
| Internet and Software Infrastructure | 80% |
| Internet and Mobile Apps | 78% |
| Computer Hardware and Semiconductors | 59% |
| Virtual Reality, Gaming, Entertainment, Media | 48% |

*Table 9. Vulnerability prevalence by industry*

## Legal and IP Risk: Licensing

Two-thirds of audited codebases contain license conflicts—the highest rate in OSSRA history.

| Metric | OSSRA 2025 | OSSRA 2026 |
| :--- | :--- | :--- |
| Codebases with license conflicts | 56% | 68% |
| Mean license conflicts per codebase | 51% | 69% |
| Median license conflicts per codebase | 5 | 8 |
| Maximum license conflicts in a single codebase | 1,109 | 2,675 |

*Table 10. License conflict metrics: Year-over-year comparison*

## The AI License Challenge

Only 54% of organizations evaluate AI-generated code for IP and license risks, and just 24% perform comprehensive IP, license, security, and quality evaluations. AI coding assistants trained on vast public codebases can inadvertently introduce code from projects with restrictive licenses, creating a "license laundering" problem.

## Obsolescence Management and Maintenance Debt

More than 9 out of 10 codebases contain components that are significantly outdated, abandoned by their maintainers, or running versions that are years behind current releases.

| Metric | OSSRA 2025 | OSSRA 2026 |
| :--- | :--- | :--- |
| Codebases with components 4+ years out-of-date | 90% | 92% |
| Codebases with components showing no development in 2+ years | 91% | 93% |
| Codebases with components not using latest version | 91% | 93% |
| Codebases with components 10+ versions behind current | 90% | 92% |

*Table 16. Component maintenance and operational risk metrics*

## The EU Cyber Resilience Act

The CRA, which took effect in December 2024, introduces mandatory cybersecurity requirements for products with digital elements. By September 2026, vulnerability reporting requirements become mandatory. Organizations must be able to resolve potential exploit paths in a timely and transparent manner to remain compliant.

## Conclusion and Recommendations: Addressing Open Source Risk

What the data tells us is that the scale of open source usage has outpaced traditional manual governance. Organizations need:
1. **Comprehensive Visibility**: Moving beyond manifest files to include binary and snippet analysis.
2. **Automated Policy Enforcement**: Integrating security and license checks into the CI/CD pipeline.
3. **AI Governance**: Establishing clear policies for the use of AI coding assistants and AI models.
4. **Maintenance Discipline**: Prioritizing the remediation of technical debt to meet regulatory requirements like the CRA.

## About Black Duck

Black Duck is the industry leader in automated security and management solutions for software supply chains. Our portfolio provides the intelligence and automation needed to secure the modern software development lifecycle.

---

m known vulnerabilities . This
represents a commitment by the manufacturer to handle vulnerabilities effectively throughout the product’s support period . The support period must
be transparent to users of the product and represent the reasonable lifespan of the product . Absent a shorter product lifespan, the CRA expects
vulnerability management for a minimum of five years .

Manufacturers must maintain access to security updates for 10 years after the end of the support period, as well as maintain regulatory access for
all technical documentation relating to its cybersecurity policies, practices, and decisions for at least 10 years .

This has direct implications for open source governance and component selection . If a manufacturer ships a product containing an open source
component that has a known exploitable vulnerability, they have obligations to meet . If they ship with an obsolete version of a component, they have
obligations to meet . If they fail to triage vulnerabilities reported to the component maintainers, they have obligations to meet . How the manufacturer
handles these obligations determines if they meet the expectations of the CRA . If those expectations aren’t met, the penalties are percentages of the
manufacturers’ global revenue .

Consider this in light of our audit findings: 93% of codebases contain components with no development activity in over two years . These “zombie
components” represent potential CRA compliance gaps . If a vulnerability is disclosed in one of these abandoned projects after a product ships, the
manufacturer faces a choice: fork the project and maintain it themselves, find an alternative and refactor the product, or accept the potential for CRA
penalties . None of these options are simple or inexpensive .

blackduck .com  |  25
blackduck .com  |  25

Vulnerability Reporting

Beginning September 2026, manufacturers, distributors, and importers must report actively exploited vulnerabilities
and severe security incidents to the Computer Security Incident Response Team (CSIRT) designated as coordinator of
the Member State where they have their main establishment, as well as to ENISA, the EU agency for cybersecurity .

The reporting timeline is aggressive but does allow for coordinated embargoes .

•  Initial notification within 24 hours of becoming aware of a vulnerability known to be exploitable (e .g ., proof-of-

concept code is available)

•  Follow-up notification within 72 hours of triage confirming that the product with digital elements is potentially

exploitable to the vulnerability

•  Final report within 14 days after a corrective measure, such as a patch, is available

This 24-hour requirement demands that manufacturers don’t rely on continuous scanning of codebases and instead
have an accurate, complete, and clear inventory indicating component usage and version—an SBOM .

SBOM Requirements

The CRA mandates that manufacturers create and maintain an SBOM encompassing at least the product’s direct
dependencies . While manufacturers are not required to make their SBOM publicly available, market surveillance
authorities, such as ENISA and CSIRTs, may request it for validation, audit, or incident investigation purposes .

The SBOM must be kept current throughout the product’s lifespan and support period, ensuring that any component
change or patch is reflected in the documentation . This is an ongoing obligation tied to the product life cycle .

The requirements align with evolving international standards . CISA’s 2025 draft guidance on SBOM generation
demands precise identification of upstream suppliers, automation-ready formats (CycloneDX, SPDX), and critically,
the inclusion of transitive dependency data . Given that 64% of open source components in a typical codebase are
transitive dependencies, this last requirement is significant . Organizations must document the libraries they chose and
the libraries those libraries depend on .

Without a comprehensive
inventory of third-
party components and
proactive notification of
changes in risk—such
as new vulnerabilities
documented in the
European Vulnerability
Database (EUVD)—
manufacturers will
struggle to meet the
aggressive timelines
CRA requires.

blackduck .com  |  26

Open source stewards are defined as a legal entity
that voluntarily and specifically performs security
analysis, including publishing patches, for defined
open source libraries.

Open Source Stewards: Bridging Commercial Support and OSS

The CRA introduces a novel category of economic actor: the “open source steward .” Where most people understand the role a
manufacturer plays in the secure development of their products, open source is different . Some open source projects are extremely
popular and attract many developers . Linux or Kubernetes are perfect examples of such efforts . Other projects are just as impactful but
have fewer developers, such as OpenSSL or Log4J . And some projects may have fewer than 10 people involved in their development .

Historically, a commercial support model for open source meant buying support from entities that distribute versions of specific libraries .
Red Hat Linux is a perfect example of this model . But where Red Hat provides support for a fee covering its distribution, the upstream
projects in that distribution remain community supported .

The CRA seeks to ensure that all third-party code is supported, and to meet this objective it defined the role of “open source steward .”
At its core, an open source steward takes responsibility for an open source component and its maintenance . There is no default open
source steward for any given open source project, and stewards aren’t obligated to be a “steward for life .” Although foundations such as
the Apache Software Foundation, the Eclipse Foundation, and the Linux Foundation are expected to become stewards, maintainers of
small projects are also eligible . Open source stewards aren’t subject to the penalties that manufacturers are, but they do have obligations
to report exploitability information and coordinate resolution of vulnerabilities .

Steward obligations include

•  Establishing and documenting a cybersecurity policy to foster secure development and effective vulnerability handling

•  Cooperating with market surveillance authorities and taking corrective actions when requested

•  Reporting actively exploited vulnerabilities (to the extent they are involved in the product’s development)

•  Reporting severe incidents affecting the network and information systems they use in the development or maintenance of the product

For organizations consuming open source, these obligations have practical implications . Projects governed by established foundations—
those with formal stewardship—will have documented cybersecurity policies and vulnerability-handling processes . Projects maintained
by individual developers or informal communities may not . This doesn’t make ungoverned projects less valuable, but it does make their
maintenance trajectory less predictable—a factor that matters when selecting components for products that must remain compliant for
five or more years .

blackduck .com  |  27
blackduck .com  |  27

Supply Chain Accountability

The CRA fundamentally changes how supply chain compliance works . Previously, for most manufacturers of products with digital
elements, compliance was a matter of internal policies and legal agreements with direct vendors . The CRA extends accountability to
the entire software supply chain, including open source components .

Manufacturers must conduct cybersecurity risk assessments that include inspection of third-party components integrated into
the final product . When a manufacturer learns of a potential vulnerability in a product component—including third-party and open
source components—it must report the vulnerability to the entity maintaining the component . Importers and distributors must inform
manufacturers of any vulnerabilities identified in products they handle .

This creates a chain of accountability that flows through the entire ecosystem . A vulnerability in a transitive dependency—a
component the development team never explicitly chose—becomes the manufacturer’s responsibility to track, report, and remediate .

Implications for Component Governance

The CRA recognizes that the “ship and forget” product security model that has allowed maintenance debt to accumulate across the
industry has negatively impacted users of digital products for years . Organizations selling software in the EU market must

•  Understand component life cycle at selection time . The five-year minimum support period means organizations must evaluate the
maintenance trajectory of open source components before incorporating them—not just discover EOL status after a version of the
product is released . Components from projects with active maintainers, established governance, and clear roadmaps present lower
compliance risk than components from projects showing signs of abandonment .

•  Track component status continuously . A component that was actively maintained when selected may become abandoned
or obsolete during the lifespan of the product . Organizations need ongoing visibility into the maintenance status of their
dependencies—direct and transitive—to identify compliance risks before they become compliance failures .

•  Maintain current SBOMs . The CRA’s requirement for life cycle–maintained documentation means SBOMs must be regenerated

with each product update, including patches .

•  Establish vulnerability response processes . The 24-hour reporting requirement demands mature and automated vulnerability

management processes . Organizations must be able to identify if a vulnerability—whether newly disclosed or previously disclosed
but with no exploitability information—affects their products and then initiate reporting . That reporting needs to be done within a
single day . If the vulnerability does impact the product once triage is performed, additional reporting is required within 72 hours .

The OSSRA data suggests software development teams have significant work ahead . With 92% of codebases containing
components four or more years out-of-date, and 93% containing components with no development activity in two years, most
organizations are starting from a position of substantial maintenance debt . The CRA provides a regulatory forcing function—but the
remediation work required is substantial and deadlines are fast approaching .

With 92% of codebases
containing components
four or more years
out-of-date, and 93%
containing components
with no development
activity in two years,
most organizations
are starting from a
position of substantial
maintenance debt.

blackduck .com  |  28

The Cyber Resilience Act makes supply chain hygiene a
compliance imperative. Organizations selling software
in the European market must have robust cybersecurity
programs and be able to respond to exploitable
vulnerabilities within 24 hours.

Industry Maintenance Patterns

Maintenance practices vary significantly across industries, reflecting different development cultures and regulatory environments .

Best Maintenance Practices

Industry

Percentage of
components <1 year old

Percentage using
latest version

Aerospace, Aviation, Automotive,
Transportation, Logistics
Computer Hardware and
Semiconductors
Manufacturing, Industrials,
Robotics
Healthcare, Health Tech,
Life Sciences

34%

31%

29%

27%

18%

15%

14%

12%

Table 19 . Industries with best component maintenance practices

Safety-critical industries consistently show better maintenance metrics—probably not because they update more aggressively, but because they
add dependencies more carefully . Fewer components mean fewer maintenance obligations . Rigorous vetting processes filter out components
without strong maintenance track records .

blackduck .com  |  29

Poorest Maintenance Practices

Industry

Percentage of
components <1 year old

Percentage using
latest version

Internet and Mobile Apps

14%

Marketing Tech

Big Data, AI, BI, Machine
Learning

EdTech

13%

15%

16%

5%

4%

6%

5%

Table 20 . Industries with poorest component maintenance practices

Fast-moving sectors with high component counts show the poorest maintenance metrics . The JavaScript/npm ecosystem
common in these industries produces particularly large dependency trees with rapid version churn—a combination that makes
keeping current especially difficult .

The Value of Discipline

The good news: Effective dependency management makes a measurable difference . According to Black Duck’s supply chain
security research, organizations that are highly effective at tracking and managing open source dependencies are significantly
more prepared to secure their open source software—85% versus just 57% for the overall survey population .

The challenge is that fewer than half of organizations rate themselves as highly effective at this fundamental practice .

Maintenance debt doesn’t stabilize—it grows . Skipped updates make future updates harder, increasing the likelihood of skipping
future updates . The cycle accelerates until external forcing functions—security incidents, compatibility failures, regulatory
requirements like the CRA—mandate action .

The organizations with the best outcomes are those that invest in component governance— thorough, careful component
selection; continuous monitoring; and disciplined update practices—before they are forced to do so . The investment pays dividends
not just in reduced maintenance burden but in reduced vulnerability exposure and smoother compliance when regulations demand
accountability .

Organizations
highly effective
at dependency
management are
significantly more
prepared to secure
their software—85%
versus 57% for the
overall population.

blackduck .com  |  30

Yesterday’s Gone:
Living in the AI Era

Software development has entered a new era . The tools developers use, the speed at which they work, and the volume of code they
produce have all transformed in the span of 18 months . AI coding assistants—GitHub Copilot, Cursor, Claude Code, Amazon Q,
Windsurf, Tabnine, and others—have moved from experimental curiosities to essential infrastructure .

This section examines what our data reveals about AI adoption, the governance challenges organizations face, and how these
trends connect to the risk patterns documented throughout this report .

AI Coding Adoption: The Scale

The adoption curve for AI coding assistants has been steeper than almost any technology in software development history . What
began as autocomplete suggestions has evolved into full-function code generation .

Constantly (daily, integrated into standard workflows)

13%

AI coding assistant usage

Percentage of respondents

Frequently (multiple times per week)

Sometimes (few times per month)

Rarely (experimental use only)

31%

23%

18%

Never/not permitted

4%

Unverified/unmonitored usage

11%

Table 21 . AI coding assistant usage frequency (Source: Black Duck, “Balancing AI Usage and Risk in 2025”)

blackduck .com  |  31
blackduck .com  |  31

Forty-four percent of DevSecOps professionals now use AI coding assistants frequently or constantly—and they are deeply
integrated into daily workflows . Add for occasional users, more than three-quarters of the industry has adopted these tools to
some degree .

Black Duck’s “State of Embedded Software Quality and Safety” report corroborates these findings from a different angle: 89 .3%
of embedded software organizations have developers using AI assistants . In an industry known for conservative technology
adoption, AI coding tools have nonetheless achieved widespread penetration .

The adoption extends beyond code generation . Our DevSecOps survey found that 97% of organizations are using open source
AI models (such as those from Hugging Face) in their development workflows . However, the transition from experimentation to
production is more selective . According to Black Duck’s supply chain security research, only 49% of organizations incorporate
open source AI/ML models directly into the software they ship . AI has become both the means of production and, increasingly,
part of the product itself .

The Governance Gap

While AI adoption has been rapid, governance practices have not kept pace .

Only 24% of organizations perform
comprehensive IP, license, security, and
quality evaluations for AI-generated code.

According to Black Duck’s supply chain survey, 76% of respondents said their organizations check AI-generated code for
security risks, but only 54% evaluate it for IP and license risks, and just 56% assess quality issues . Altogether, only 24% perform
comprehensive IP, license, security, and quality evaluations for AI-generated code—leaving significant oversights in software
supply chains .

This governance gap matters because of what AI
assistants actually do in practice .

Dependency selection . When generating code, AI
assistants frequently suggest imports and dependencies .
A request to “parse JSON dates” might generate code that
imports moment .js, date-fns, or dayjs—with the AI making
the selection based on training data patterns, not security
or maintenance considerations .

Pattern replication . AI models are trained on vast
codebases . When they generate code, they replicate
patterns from that training data—including coding styles,
architectural approaches, and potentially vulnerabilities . A
pattern that appears frequently in training data will appear
frequently in generated code, regardless of whether it’s
secure .

The dependency multiplication effect . When a
developer manually adds a dependency, there’s at least a
moment of consideration: Do I need this? Is it maintained?
What does it pull in? When an AI assistant suggests an
import as part of a larger code block, that moment often
disappears . The developer is focused on the functionality,
not the dependency .

This effect compounds across teams and time . The
dependencies AI assistants choose aren’t random;
they reflect training data . Popular libraries appear more
frequently in training data and are therefore suggested
more frequently . When vulnerabilities are discovered
in these popular libraries, the blast radius is significant
precisely because both human developers and AI
assistants have gravitated toward the same widely
adopted solutions .

blackduck .com  |  32

Shadow AI

Why Shadow AI Happens

Not all AI coding assistant usage is sanctioned . Table 22 reveals a “shadow AI”—developers
using AI tools without organizational approval, visibility, or governance .

Shadow AI indicator

Source

Finding

Using AI without permission

DevSecOps survey

11%

Using AI against policy

Embedded Software report

18%

Organizations aware of
unsanctioned use

Embedded Software report

18%

Table 22 . Shadow AI usage and governance gaps

Eleven percent of DevSecOps professionals admit to using AI coding assistants in an
“unverified/unmonitored” way without official permission . This figure likely understates the
reality—respondents may underreport behavior they know violates policy .

Black Duck’s “State of Embedded Software Quality and Safety” report found an even higher rate:
18% of organizations know that developers are using AI tools even when organizational policy
prohibits it .

Shadow AI creates risks that organizations cannot manage because they cannot see them:
unknown code provenance, potential license contamination, security oversights, compliance
failures in regulated industries, and IP exposure when proprietary code is transmitted to cloud
services for processing .

Development Velocity Shown in the OSSRA Data

The OSSRA data shows acceleration across every metric we track . While we cannot attribute
these trends to any single cause, the patterns are dramatic .

Productivity pressure . Developers face relentless pressure
to ship features . AI assistants accelerate development .
When policy prohibits tools that make developers faster,
some developers will use them anyway .

Perceived low risk . Many developers view AI assistants
as “just fancy autocomplete”—helpful but not fundamentally
different from other IDE features .

Inadequate alternatives . Organizations that ban AI
assistants without providing alternative productivity tools
leave developers to choose between policy compliance and
getting their work done .

Inconsistent enforcement . Policies that exist on paper
but aren’t technically enforced become suggestions rather
than requirements .

blackduck .com  |  33

Acceleration Across Every Metric

Metric

OSSRA
2022

OSSRA
2024

OSSRA
2026

5-year change

Mean file count

24,094

29,332

84,499

251%

Mean components per
codebase

~700

~850

1,180

   69%

Mean vulnerabilities per
codebase

~200

~250

581

Median vulnerabilities

66

46

78

191%

   18%

Table 23 . Five-year acceleration in codebase metrics (2022–2026)

From 2021 to 2023, growth was steady but manageable—single-digit or low double-digit percentage increases . Beginning in 2024,
every metric accelerated dramatically .

•  File counts increased 65% from the 2023 to 2024 OSSRA, then another 74% from 2024 to 2025

•  Vulnerabilities per codebase increased 107% in a single year

•  Component counts increased 29 .5% year-over-year

This timing coincides with mainstream AI coding assistant adoption . GitHub Copilot reached general availability in June 2022; by
late 2023, it and its competitors had become standard tools for millions of developers .

However, correlation is not causation . Multiple factors are at play, and the codebases in our M&A audit data weren’t built in
a year—they represent years of accumulated development decisions . AI-assisted development may be accelerating existing
patterns, but it’s one factor among several, including disclosure acceleration (notably the Linux Kernel CNA change), microservices
architectures, and the continued growth of open source ecosystems .

blackduck .com  |  34

The Path Forward

The challenges outlined in this section are not caused by AI coding tools themselves, but by the scale and velocity they enable .
Just as open source transformed software development—and is now a permanent fixture in how software is built—AI-assisted
coding is here to stay .

The organizations that navigate this transition successfully will be those that

•  Establish clear AI governance rather than prohibition (which drives usage underground)

•  Integrate security into AI-assisted workflows rather than treating AI-generated code as a separate category

•  Maintain visibility into what tools developers are using and what code they’re producing

•  Invest in comprehensive evaluation of AI-generated code across security, license, and quality dimensions

The data in this report provides the context for understanding these challenges . The following section discusses how Black Duck’s
portfolio of solutions helps organizations address them .

blackduck .com  |  35
blackduck .com  |  35

Conclusion and
Recommendations:
Addressing
Open Source Risk

What the Data Tells Us

The findings in this report document a software landscape that has fundamentally changed .
Mean open source components per codebase have grown to 1,180 . Mean vulnerabilities
have more than doubled to 581 . License conflicts have reached their highest levels in OSSRA
history . And more than 90% of codebases carry significant maintenance debt .

These trends reflect the new reality of software development . AI-assisted coding has
accelerated the pace at which code is written and dependencies are added . Open source
has become effectively universal—98% of the audited codebases contain open source
components . And the complexity of modern applications continues to grow, with file counts
quadrupling over five years .

This is the environment organizations must navigate . The question is whether organizations
have the visibility, intelligence, and processes to manage open source risk at this scale .

What Organizations Need

The data in this report points to several capabilities that organizations need to address
the changing software security environment .

Depth of analysis . Our audits found that 16% of open source components entered
codebases outside of standard package management—vendor dependencies copied
into repositories, code snippets from Stack Overflow or AI assistants, and binary
components without source . Tools that rely solely on manifest scanning miss this code
entirely .

Intelligence beyond CVEs . Black Duck Security Advisories provide earlier and deeper
analysis of open source risks, including issues that never receive a CVE . Black Duck
independently researches and validates open source vulnerabilities and offers richer
technical context for remediation . BDSAs include accurate vulnerable version ranges,
patch information, and fixed versions, giving development and security teams precise
guidance on what’s impacted and how to resolve vulnerabilities quickly .

License visibility . With 68% of codebases containing license conflicts—and the
combinatorial complexity of 1,180 components creating over 695,000 potential
pairings—organizations need automated detection that goes beyond declared
dependencies to identify conflicts in transitive dependencies and AI-generated code .

Operational awareness . When 93% of codebases contain components with no
development activity in over two years, organizations need visibility into component
age, maintenance status, and upstream viability—before a vulnerability is discovered in
an abandoned project with no upstream fix .

Workflow integration . With 44% of developers using AI coding assistants frequently or
constantly, security analysis must integrate into the environments where developers
work—IDEs, pull requests, and CI/CD pipelines .

AI model risk Insights . Organizations need to identify and analyze open source
AI models, including their usage, licensing, and data origins within a codebase .
This capability helps manage the increasing complexity of AI models in software
development and integrate them into SBOMs for compliance transparency .

blackduck .com  |  36

The Black Duck Application Security Portfolio

Black Duck’s application security solutions are specifically built to address these requirements .

Black Duck SCA

Black Duck® SCA provides deep open source analysis through multiple detection methods—dependency analysis,
snippet matching, binary analysis, AI model identification, and CodePrint matching against the Black Duck
KnowledgeBase . This multimethod approach identifies the open source that manifest-only scanning misses .

Black Duck SCA delivers

•  Comprehensive vulnerability detection through Black Duck Security Advisories, including coverage for vulnerabilities with no CVE

equivalent and corrected CVSS scores where NVD assessments are inaccurate

•  License compliance analysis that identifies conflicts across complex dependency trees, including custom and modified licenses

that require legal review

•  Remediation guidance that provides actionable fix recommendations, not just findings

•  Obsolescence information with insight into component age, maintenance status, and version currency

In late 2025, Black Duck rolled out AI model scanning for Black Duck SCA .

•  Models identified anywhere . Our signature-based scanning detects AI/ML models even if they’re deliberately obscured or not

listed in your build manifest . No more guessing what’s in your codebase .

•  License clarity . Black Duck SCA identifies model licenses to keep you compliant, whether it’s open source or commercial

software, saving you from costly legal surprises .

•  Deep insights made simple . A dedicated UI screen serves up model-specific metadata showing what the model is good at (e .g .,
code completion) and details on datasets . This helps teams build usage policies like “no retrained foundational models” with
ease .

•  Seamless integration. AI model scanning plugs right into your existing Black Duck workflows, leveraging our SBOM engine for a

unified SCA experience .

•  Supply chain transparency . Any model identified or manually added to a project can be included in an SBOM to satisfy customer

and industry requirements .

This early version of AI model scanning for Black Duck SCA is focused on identification and licensing, but it’s built to scale .
Future updates will bring deeper insights into security and operational risks introduced by models, and more customized policy
configuration .

blackduck .com  |  37
blackduck .com  |  37

Polaris Platform

Black Duck Polaris™ Platform unifies SAST, SCA, and DAST capabilities
with intelligent prioritization across finding types . Polaris enables
organizations to

The Black Duck Application Security Portfolio

Solution

Strength

Best for

•  Consolidate tooling rather than managing separate scanners with redundant and

conflicting findings

•  Prioritize effectively across vulnerability types based on severity, exploitability, and

business context

•  Integrate with developer workflows through IDE plug-ins and CI/CD pipeline integration

and SCM integrations

Black Duck Assist

Black Duck Assist™ provides AI-powered guidance within existing tools,
helping developers understand findings and act on them efficiently .
Assist accelerates the path from finding to fix by providing contextual
remediation advice .

The KnowledgeBase Foundation

What enables these capabilities is the Black Duck KnowledgeBase—the most
comprehensive repository of open source intelligence available .

•  3 .2 petabytes of open source software metadata and archives

•  10+ million open source projects from 58,000+ data sources

•  317,000 known vulnerabilities and 63,000 Black Duck Security Advisories

•  3,000 licenses tracked

•  20+ years of continuous curation by security experts

This foundation is what distinguishes Black Duck’s analysis from tools that rely on
surface-level scanning or AI-only approaches . The KnowledgeBase provides ground truth—
accurate and actionable vulnerability data, accurate severity assessments, confirmed
remediation paths, and comprehensive license intelligence . This depth is what enables
findings you can act on with confidence .

Black Duck
SCA

Deep open source
analysis, vulnerability
data (BDSAs), license
compliance

Polaris

Unified SAST/SCA/
DAST platform, intelligent
prioritization, developer-
first workflows

Black Duck
Assist

AI-powered guidance
within existing tools

Comprehensive OSS
and supply chain
risk management,
M&A due diligence,
compliance, SBOM
generation

Organizations
wanting a unified
SaaS platform
with developer-
first workflows
and intelligent
prioritization

Helping developers
understand and act
on findings

blackduck .com  |  38

Introducing Signal: An Evolutionary Addition to the Black Duck Portfolio

Black Duck Signal™ represents the next step in Black Duck’s application security evolution—extending the
portfolio with AI-native capabilities while building on the KnowledgeBase foundation that makes accurate
analysis possible .

Signal is designed to augment your existing AST capabilities, not replace them . Where Black Duck SCA provides deep, precise
analysis of open source components with accurate and actionable vulnerability data, Signal will extend coverage to first-party code
and languages where traditional tooling has gaps . Signal will plug directly into your AI-coding assistants for fast feedback . Where
Polaris provides intelligent prioritization across finding types, Signal will add contextual analysis to help determine which findings
represent genuine risk in a specific environment .

Planned Capabilities

Contextual analysis . Signal is designed to go beyond reachability to provide contextual risk assessment . Reachability answers
whether vulnerable code can be reached; contextual analysis will consider the application’s architecture, inputs, and controls to
help assess actual risk profile .

Fix suggestions . Signal will generate fix suggestions tailored to specific codebases—not generic patches, but implementations
that fit existing coding patterns and architectural approaches . Fix generation will leverage KnowledgeBase remediation patterns
combined with AI code understanding .

Extended language coverage . Traditional AST tools require language-specific parsers and rules . Signal’s AI-powered analysis is
designed to extend coverage across languages without requiring language-specific tooling—complementing the deep analysis that
language-specific tools provide while covering gaps in legacy languages, emerging frameworks, and code that traditional parsers
don’t yet support .

AI workflow integration . Signal is being designed to operate within AI coding assistant environments—GitHub Copilot, Cursor,
Claude Code, Windsurf, and others—providing security feedback where developers increasingly work .

Built on the KnowledgeBase

What will distinguish Signal from other AI-powered security tools is its foundation . Signal will augment LLM capabilities with
KnowledgeBase intelligence—combining AI pattern recognition with human-vetted ground truth . The result is designed to be
analysis that is both intelligent and accurate: capable of identifying novel issues while grounded in accurate and actionable
vulnerability data, confirmed remediation patterns, and comprehensive license intelligence .

Signal is not a replacement for proven approaches—it’s an extension of them . Organizations will benefit from combining the deep
analysis of Black Duck SCA and Polaris with Signal’s AI-native capabilities, applying each where it delivers the most value .

blackduck .com  |  39

Getting Started

The challenges documented in this report—growing vulnerability counts, increasing
license complexity, accumulating maintenance debt, and the accelerating pace of AI-
assisted development—are addressable with the right combination of tools, processes,
and intelligence .

For organizations addressing these challenges today: Black Duck SCA, Polaris, and
Assist are available now . These solutions provide the depth of analysis, breadth of
coverage, and workflow integration that modern software development requires .
Contact your Black Duck representative to discuss how these capabilities align with
your security objectives .

For organizations interested in Signal: The Signal Early Access Program provides
access to Signal’s capabilities as they become available, along with onboarding
support and direct feedback channels to the product team . The program is designed for
organizations that want to extend their existing Black Duck deployment with AI-native
capabilities and help shape the product’s development . To learn more, contact your
Black Duck representative or visit blackduck .com/signal .

blackduck .com  |  40

About Black Duck

Black Duck® meets the board-level risks of modern software with True Scale Application
Security, ensuring uncompromised trust in software for the regulated, AI-powered
world . Only Black Duck solutions free organizations from tradeoffs between speed,
accuracy, and compliance at scale while eliminating security, regulatory, and licensing
risks . Whether in the cloud or on premises, Black Duck is the only choice for securing
mission-critical software everywhere code happens . With Black Duck, security leaders
can make smarter decisions and unleash business innovation with confidence . Learn
more at www .blackduck .com .

©2026 Black Duck Software, Inc . All rights reserved . Black Duck is a trademark of Black Duck Software, Inc . in the United States and other countries . All other names mentioned herein are trademarks or registered trademarks of their respective owners . March 2026

blackduck .com  |  41

blackduck .com  |  42