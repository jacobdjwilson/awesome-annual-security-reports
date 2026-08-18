# BSIMM16 REPORT 2026

## Table of Contents
- [Part 1: Executive Summary](#part-1-executive-summary)
  - [Welcome to BSIMM16](#welcome-to-bsimm16)
  - [BSIMM16 Data Highlights](#bsimm16-data-highlights)
  - [Trends and Insights Summary](#trends-and-insights-summary)
  - [Call to Action](#call-to-action)
  - [What is the BSIMM?](#what-is-the-bsimm)
  - [The BSIMM Skeleton](#the-bsimm-skeleton)
- [Part 2: Trends and Insights](#part-2-trends-and-insights)
  - [AI/ML is Reshaping Application Security Priorities](#aiml-is-reshaping-application-security-priorities)
  - [Preparing Humans for AI Code Generation](#preparing-humans-for-ai-code-generation)
  - [Security Tools vs LLM Coding Tools](#security-tools-vs-llm-coding-tools)
  - [Regulatory Pressures](#regulatory-pressures)
  - [Technical Solutions to Regulatory Requirements](#technical-solutions-to-regulatory-requirements)
  - [Standing up Processes to Meet Requirements](#standing-up-processes-to-meet-requirements)
  - [Solving the Documentation Problem](#solving-the-documentation-problem)
  - [Software Security Training is Evolving](#software-security-training-is-evolving)
  - [Topics We’re Watching](#topics-were-watching)
- [Part 3: For Practitioners](#part-3-for-practitioners)
  - [Introduction](#introduction)
  - [SSDF-BSIMM Mapping Updated for BSIMM16](#ssdf-bsimm-mapping-updated-for-bsimm16)
  - [AI/ML and BSIMM16](#aiml-and-bsimm16)
  - [Six Key Activities: Using the BSIMM to Deal with AI/ML](#six-key-activities-using-the-bsimm-to-deal-with-aiml)

Organization: BlackDuck  
Report Title: BSIMM16  
Year: 2026  

---

# PART 1: EXECUTIVE SUMMARY

In 2008, application security, research, and analysis experts set out to gather data on the different paths that organizations take to address the challenges of securing software. Their goal was to conduct in-person interviews with organizations that were known to be highly effective in software security initiatives (SSIs), gather details about their efforts, analyze the data, and publish their findings to help others.

The result was the Building Security In Maturity Model (BSIMM), a descriptive model—published as BSIMM1—that provides a baseline of observed activities (i.e., controls) for SSIs to build security into software and software development. Because these initiatives often use different methodologies and different terminology, the BSIMM also creates a common vocabulary everyone can use as well as a common methodology for starting and improving SSIs of any size and in any vertical market.

Since BSIMM1 in 2008, we’ve been early reporters on security program changes across people, process, technology, culture, compliance, digital transformation, and much more. Welcome to the BSIMM16 report, and thank you for reading.

## WELCOME TO BSIMM16

If you’re in charge of an SSI, understanding the BSIMM and its use by participants will help you plan strategic improvements. If you’re running the technical aspects of an initiative, you can use the how-to guide (in Part 5) and activity descriptions (in Part 8) to help define tactical improvements to people, process, technology, and culture.

Each BSIMM annual report is the result of studying real-world SSIs, which many organizations refer to as their application or product security program or as their DevSecOps effort. Each year, firms in different industry verticals use the BSIMM to create a software security scorecard for their programs that they then use to inform their SSI improvements. Here, we present BSIMM16, building on the work of previous years and based on refreshed data from recently performed assessments, including observations of 111 firms.

In the rapidly changing software security field, it’s important to understand what other organizations are doing in their own SSIs. Comparing the efforts of more than 100 companies to yours will directly inform your strategy for improvement and growth.

BSIMM core knowledge stems from the activities we have directly observed in our participants—the group of firms that use the BSIMM as part of their SSI management. Each participant has their own unique SSI with an emphasis on the building security in activities important to their business objectives, but they collectively use the activities captured here. We organize that core knowledge into a software security framework (SSF), represented in Part 8. The SSF comprises four domains—Governance, Intelligence, SSDL Touchpoints, and Deployment—with those domains currently composed of 128 activities. The Governance domain, for example, includes activities that fall under the organization, management, and measurement efforts of an SSI.

From an executive perspective, you can view BSIMM activities as preventive, detective, corrective, or compensating controls implemented in a software security risk management framework. Positioning the activities as controls allows for easier understanding of the BSIMM’s value by governance, risk, compliance, legal, audit, and other executive management groups.

As with any research work, some terms have specific meanings in the BSIMM. The box below shows the most common BSIMM terminology.

### BSIMM TERMINOLOGY

Nomenclature has always been a problem in computer security, and software security is no exception. Several terms used in the BSIMM have a particular meaning for us, and the following list highlights some of the most important ones used in this document:
- **Activity**. Actions or efforts carried out or facilitated by the SSG as part of a practice. Activities are divided into three levels in the BSIMM based on observation rates.
- **Capability**. A set of BSIMM activities spanning one or more practices working together to serve a cohesive security function.
- **Champions**. A group of interested and engaged developers, cloud security engineers, deployment engineers, architects, software managers, testers, or people in similar roles who have an active interest in software security and contribute to the security posture of the organization and its software.
- **Data pool**. The collection of assessment data from the current participants.
- **Domain**. One of the four categories the framework is divided into, i.e., Governance, Intelligence, SSDL Touchpoints, and Deployment.
- **Participants**. The group of firms in the current data pool.
- **Practice**. A grouping of BSIMM activities. The SSF is organized into 12 practices, three in each of four domains.
- **Satellite**. A group of individuals that is organized and leveraged by an SSG. This term has largely been replaced by security champions.
- **Secure SDL (SSDL)**. Any software lifecycle with integrated software security checkpoints and activities.
- **Software security framework (SSF)**. The basic structure underlying the BSIMM, comprising 12 practices divided into four domains.
- **Software security group (SSG)**. The internal group charged with carrying out and facilitating software security. The group’s name might also have an appropriate organizational focus, such as application security group or product security group.
- **Software security initiative (SSI)/software security program (SSP)**. An organization-wide program to instill, measure, manage, and evolve software security activities in a coordinated fashion. Also referred to in some organizations as an application security program, product security program, or perhaps as a DevSecOps program.

---

## BSIMM16 DATA HIGHLIGHTS

Use the information in this section to answer common questions about BSIMM data, such as, "What are some data pool statistics?," "Which activities are most firms doing?," and, "How are software security efforts changing over time?"

_Note: Items in italic purple refer to specific BSIMM activities in Part 8._

Activities are the building blocks of the BSIMM, the smallest units of granularity implemented across organizations to build SSIs. Rather than dictating a set of prescriptive activities, the purpose of the BSIMM is to descriptively observe and quantify the actual activities carried out by various kinds of SSIs across many organizations.

The BSIMM is an observational model that reflects current software security efforts, so we adjust it annually to keep it current, but for the first time, there have been no changes to the BSIMM framework this year. Many activities saw significant growth but none to the extent that moving activities between levels seemed necessary. Some level 3 activities (for example, _[T3.2] Provide training for vendors and outsourced workers_ and _[CMVM3.4] Operate a bug bounty program_) are coming close to the number of observations for level 2 activities for those practices but are only near activities that are slowly declining. Rather than rushing to make changes based on less than solid trends, we made the decision to not move activities this year and to just let the trends develop further. In addition, while we considered some new activities, the things that would have gone into them are largely covered in existing activities.

Unique in the software security industry, the BSIMM project has grown from nine participating companies in 2008 to 111 in 2026, with approximately 3,700 software security group (SSG) members and 6,500 security champions. The average age of participants’ SSIs is 5.6 years, but the BSIMM project shows consistent growth even as participants enter and leave over time—we added 16 firms for BSIMM16 and dropped 26 others whose data hadn’t been refreshed. Increasingly, we see firms not just assessing their overall programs but how well they reach into their business units and teams as well. While these business unit assessments provide valuable data to the firms that request them, we have not added the data from these assessments to the data pool recorded in the annual report.

This 2026 edition of the BSIMM report—BSIMM16—examines anonymized data from the software security activities of 111 organizations across different verticals, including Cloud, Financial Services, Financial Technology (FinTech), Healthcare, Independent Software Vendors (ISVs), Insurance, Internet of Things (IoT), and Technology Organizations.

The 7 Habits of Highly Effective People explores the theory that successful individuals share common qualities in achieving their goals and that these qualities can be identified and applied by others. The same premise can be applied to SSIs. Listed in Table 1 are the "Top 10" most observed activities in the BSIMM16 data pool. (While we call this list the Top 10, there are actually 12 activities this year thanks to some ties in observation rates.) The data suggests that if your organization is working on its own SSI, you should consider implementing these activities. We discuss the "Top 10" more in Part 9.

### BSIMM16 "TOP 10" ACTIVITIES

| Observation % | Activity |
| --- | --- |
| 87.6% | _[CMVM1.1] Create or interface with incident response._ |
| 82.6% | _[SM1.4] Implement security checkpoints and associated governance._ |
| 79.3% | _[SE1.2] Ensure host and network security basics are in place._ |
| 78.5% | _[CR1.4] Use automated code review tools._ |
| 78.5% | _[PT1.1] Use external penetration testers to find problems._ |
| 77.7% | _[CP1.2] Identify privacy obligations._ |
| 76.9% | _[ST1.1] Perform edge/boundary value condition testing during QA._ |
| 76.0% | _[CP1.3] Create policy._ |
| 73.6% | _[AA1.1] Perform security feature review._ |
| 72.7% | _[CP1.1] Unify regulatory pressures._ |
| 72.7% | _[SR1.2] Create a security portal._ |
| 72.7% | _[SR1.5] Identify open source._ |

**Table 1. TOP ACTIVITIES BY OBSERVATION PERCENTAGE.** The most frequently observed activities in BSIMM16 are likely important to all SSIs. (Due to observation rate ties, there are 12 activities in this year’s "Top 10.")

Table 2 shows some activities that have experienced exceptionally high growth over the past 12 months. Not surprisingly, some of these activities, such as _[T2.12] Provide expertise via open collaboration channels_, are mentioned in the Trends and Insights section. In addition, the _[CMVM2.4] Streamline incoming responsible vulnerability disclosure_ activity introduced in BSIMM12 continues its strong growth in observation count as we reported last year. The growth of _[SE3.9] Protect integrity of development toolchains_ is not unexpected as many firms have been doing so, but the activity was only introduced to the BSIMM framework in BSIMM14—historically, the BSIMM focused more on the operating environment of software, not the development environment. _[SE3.10] Protect the integrity of development endpoints_, introduced in BSIMM15, is seeing similar "growth" and just missed the Top 10 list.

### BSIMM16 TOP ACTIVITIES GROWTH BY COUNT

| Increase | Description |
| --- | --- |
| 15 | _[CMVM2.4] Streamline incoming responsible vulnerability disclosure._ |
| 12 | _[SE3.9] Protect integrity of development toolchains._ |
| 10 | _[T2.12] Provide expertise via open collaboration channels._ |
| 9 | _[CMVM3.3] Simulate software crises._ |
| 9 | _[PT2.3] Schedule periodic penetration tests for application coverage._ |
| 8 | _[T3.2] Provide training for vendors and outsourced workers._ |
| 8 | _[CMVM3.5] Automate verification of operational infrastructure security._ |
| 8 | _[SR3.4] Create standards for technology stacks._ |
| 8 | _[SE3.6] Create bills of materials for deployed software._ |
| 7 | _[CR2.6] Use custom rules with automated code review tools._ |

**Table 2. TOP ACTIVITIES BY RECENT GROWTH IN OBSERVATION COUNT.** These activities had the largest growth in BSIMM16, which means they are likely important to your program now or will be soon.

---

## TRENDS AND INSIGHTS SUMMARY

The BSIMM trends and insights we’ve identified are a distillation of software security lessons learned across 111 organizations that collectively have 10,200 security professionals helping about 223,700 developers do good security work on about 91,200 applications. Use this information to inform your own strategy for improvement.

Trends describe shifts in SSI behavior that affect activity implementation across multiple areas. Larger in scope than an activity, or even a capability that combines multiple activities within a workflow, we believe these trends show the way organizations are executing groups of activities within their evolving culture. In addition to the in-depth sections for practitioners in Part 3, which also covers how application security and the BSIMM are evolving in response to AI, we report on trends in more depth in Part 2.

### AI CONTINUES TO BE A MAJOR FOCUS

AI continued to be a major area of focus for all organizations in the last year, with many firms doing something around it, such as _[SR3.5] Create standards controlling and guiding the adoption of new technologies_, which we introduced in BSIMM15; AI is a major part of that for every firm where it was observed. Knowing what is going on around AI and attacks against it are very important as we saw with _[AM1.5] Gather and use attack intelligence_, which saw 10% growth over BSIMM15.

### MEETING GOVERNMENT REGULATIONS

In response to self-attestation requirements for selling software to the US government, many firms have put special emphasis on activities that can aid in compliance. One such mandate is the need to build software bills of materials (SBOMs), and we observed a related 30% increase in _[SE3.6] Create bills of materials for deployed software_ and an increase of more than 40% in _[SE2.4] Protect code integrity_. Similar efforts from governments around the world are also driving changes in software security programs.

### SOFTWARE SECURITY TRAINING IS EVOLVING

To meet the ever-changing needs of the industry and its changing cultures, software training is evolving as well. While _[T1.1] Conduct software security awareness training_ has slightly reversed its long decline, the days of sitting in a classroom or in computer-based training for hours or days at a time are being replaced by just-in-time training methods such as _[T2.12] Provide expertise via open collaboration channels_, which saw a 29% increase over BSIMM15, as well as other methods that meet the immediate needs of developers or short-form training, although that can have less of an effect in today’s fast-moving development environment.

---

> TAKE STOCK OF YOUR SSI. IT’S IMPORTANT TO PERIODICALLY LOOK AT YOUR PROGRAM THROUGH A DIFFERENT LENS.

## CALL TO ACTION

Use the information in this section to prioritize improvements in your SSI and perhaps also in the SSIs of your most important software suppliers and partners.

Every SSI has room for improvement, whether it’s improving scale, effectiveness, depth, risk management, the framework of deployed activities, resourcing, or anything similar. The following suggestions represent the broad efforts we see happening in BSIMM participants, with various parts likely right for your program as well.

### PLAN YOUR JOURNEY
- **Take stock of your SSI**. It’s important to periodically look at your program through a different lens, and the BSIMM enables that. Use the guidance in Part 5 to create your own SSI scorecard and compare it to your expectations.
- **Create a vision and a strategic plan**. Use the activity descriptions in Part 8 when creating a prioritized action plan for business areas where your current SSI efforts fall short. Typical investment areas include risk management, digital transformation, technical debt removal, technology insertion, and process improvement.

### GET A HANDLE ON WHAT YOU HAVE
- **Inventory all your code**. It’s likely that you’ll need specialized automation to keep track of all the code you write and all the code you bring in from outside the organization. A simple application inventory will be useful for some things, such as naming risk managers, but you’ll quickly need specialized inventories, such as SBOMs, API and microservices lists, various as-code artifacts, code that is subject to specific compliance needs, and much more.
- **Automate, automate, automate**. Search for ways to eliminate error-prone manual processes and reduce friction between governance and engineering groups, including automating security decisions. This will require some policy-as-code effort and tools integration, which might require bringing development skills into the SSG.
- **Gather all the data**. As more processes become code (and more policies and standards become machine-readable), day-to-day development and operations will generate significantly more telemetry about what’s happening and why. Use this data to ensure that everything’s working as expected.

### MAKE THE RIGHT INVESTMENTS
- **Innovate in digital transformation**. Encourage your SSG and other security stakeholders to experiment with ways to deliver security value directly into engineering processes, especially where current security testing tools don’t always keep up with engineering changes, such as with serverless architectures, single-page applications, AI, and zero trust.
- **Secure the software supply chain**. Nearly every organization today uses third-party code and provides code as a third party to other organizations. While producing SBOMs is easy, the management of software, SBOMs themselves, vendors, and vulnerability information is much more complicated.
- **Expand software security into adjacencies**. Even perfect software can have its security undermined by mistakes elsewhere in the organization. Make explicit ties between the SSI and other security stakeholders working in areas such as container security, orchestration security, cloud security, infrastructure security, and site reliability.

The data shows that new SSIs—from just started to 18 months old—are typically doing about 33 BSIMM activities. These organizations are also beginning to scale these activities across their software portfolio, deal with all the changes going on around them, and evolve their risk management strategy accordingly.

---

## SOME READING SUGGESTIONS FOR THIS REPORT
- If you’re experienced with the BSIMM, or if you need some content to help make your case with executive management, then Part 2 (Trends and Insights) is probably what you’re looking for.
- If this is your first time with the BSIMM, we recommend first reading Part 5 for context and then returning here to decide what to read next.
- If you’re starting an SSI or an SSG, or looking to mature an existing program, start with Part 5 (Quick Guide to SSI Maturity), move to Part 3’s How to Build or Upgrade an SSI, and then read through the activities in Part 8.
- If you want to get right into the types of software security controls organizations are using in their SSIs, or if you are working on building out capabilities, then read Part 8.
- If you want to see a summary of the BSIMM16 data (plus our analysis), review Part 9.

---

## WHAT IS THE BSIMM?

As Figure 1 shows, the BSIMM can be thought of as three different parts. This annual report is part of the long-term study, and we will discuss the framework below. Individual assessments are not discussed in any detail in this report, but they provide the data used each year.

```
[Framework] <---> [Individual Assessments] <---> [Long-term Study]
```
**Figure 1. ASPECTS OF THE BSIMM.** The framework provides the structure, individual assessments provide the data used by the BSIMM, and the long-term study provides the analysis used in this annual report.

---

## THE BSIMM SKELETON

The BSIMM skeleton provides a way to view activities at a glance, which is useful when thinking about your own SSI. The skeleton is shown in Figure 2, organized by domains and practices. A detailed version that includes activity references and level information is also available in Part 7. More complete descriptions of the activities along with examples are available in Part 8 of this document.

Use this skeleton to understand the software security activities included in BSIMM16. A list of software security controls can be a very helpful guide here—the BSIMM project has worked since 2008 to ensure that its content matches real-world efforts.

### GOVERNANCE

#### STRATEGY & METRICS
- Publish process and evolve as necessary.
- Educate executives on software security.
- Implement security checkpoints and associated governance.
- Enforce security checkpoints and track exceptions.
- Publish data about software security internally and use it to drive change.
- Create or grow a security champions program.
- Require security sign-off prior to software release.
- Create evangelism role and perform internal marketing.
- Use a software asset tracking application with portfolio view.
- Make SSI efforts part of external marketing.
- Identify metrics and use them to drive resourcing.
- Integrate software-defined lifecycle governance.
- Integrate software supply chain risk management.

#### COMPLIANCE & POLICY
- Unify regulatory pressures.
- Identify privacy obligations.
- Create policy.
- Build a PII inventory.
- Require security sign-off for compliance-related risk.
- Implement and track controls for compliance.
- Include software security SLAs in all vendor contracts.
- Ensure executive awareness of compliance and privacy obligations.
- Document a software compliance story.
- Ensure compatible vendor policies.
- Drive feedback from software lifecycle data back to policy.

#### TRAINING
- Conduct software security awareness training.
- Deliver on-demand individual training.
- Include security resources in onboarding.
- Enhance security champions through training and events.
- Create and use material specific to company history.
- Deliver role-specific advanced curriculum.
- Host software security events.
- Require an annual refresher.
- Provide expertise via open collaboration channels.
- Reward progression through curriculum.
- Provide training for vendors and outsourced workers.
- Identify new security champions through observation.

---

### INTELLIGENCE

#### ATTACK MODELS
- Use a data classification scheme for software inventory.
- Identify potential attackers.
- Gather and use attack intelligence.
- Build attack patterns and abuse cases tied to potential attackers.
- Collect and publish attack stories.
- Build an internal forum to discuss attacks.
- Have a research group that develops new attack methods.
- Monitor automated asset creation.
- Create and use automation to mimic attackers.
- Create technology-specific attack patterns.
- Maintain and use a top N possible attacks list.

#### SECURITY FEATURES & DESIGN
- Integrate and deliver security features.
- Application architecture teams engage with the SSG.
- Leverage secure-by-design components and services.
- Create capability to solve difficult design problems.
- Form a review board to approve and maintain secure design patterns.
- Require use of approved security features and frameworks.
- Use secure coding standards.
- Create standards for technology stacks.
- Find and publish secure design patterns from the organization.
- Create standards controlling and guiding the adoption of new technologies.

#### STANDARDS & REQUIREMENTS
- Create security standards.
- Create a security portal.
- Translate compliance constraints to requirements.
- Identify open source.
- Create a standards review process.
- Create SLA boilerplate.
- Control open source risk.
- Communicate standards to vendors.

---

### SSDL TOUCHPOINTS

#### ARCHITECTURE ANALYSIS
- Perform security feature review.
- Perform design review for high-risk applications.
- Use a risk methodology to rank applications.
- Perform architecture analysis using a defined process.
- Standardize architectural descriptions.
- Have SSG lead design review efforts.
- Have engineering teams lead AA process.
- Drive analysis results into standard design patterns.
- Drive tests with design review results.
- Make the SSG available as an AA resource or mentor.

#### CODE REVIEW
- Perform opportunistic code review.
- Use automated code review tools.
- Make code review mandatory for all projects.
- Assign code review tool mentors.
- Use custom rules with automated code review tools.
- Use a top N bugs list (real data preferred).
- Use centralized defect reporting to close the knowledge loop.
- Build a capability to combine AST results.
- Create capability to eradicate bugs.
- Automate malicious code detection.
- Enforce secure coding standards.

#### SECURITY TESTING
- Perform edge/boundary value condition testing during QA.
- Drive tests with security requirements and security features.
- Integrate opaque-box security tools into the QA process.
- Drive QA tests with AST results.
- Include security tests in QA automation.
- Perform fuzz testing customized to application APIs.
- Leverage code coverage analysis.
- Begin to build and apply adversarial security tests (abuse cases).
- Implement event-driven security testing in automation.

---

### DEPLOYMENT

#### PENETRATION TESTING
- Use external penetration testers to find problems.
- Feed results to the defect management and mitigation system.
- Use penetration testing tools internally.
- Penetration testers use all available information.
- Schedule periodic penetration tests for application coverage.
- Use external penetration testers to perform deep-dive analysis.
- Customize penetration testing tools.

#### SOFTWARE ENVIRONMENT
- Use application input monitoring for security purposes.
- Ensure host and network security basics are in place.
- Implement cloud security controls.
- Define secure deployment parameters and configurations.
- Protect code integrity.
- Use application containers to support security goals.
- Use orchestration for containers and virtualized environments.
- Use code protection.
- Use application behavior monitoring and diagnostics.
- Create bills of materials for deployed software.
- Perform application composition analysis on code repositories.
- Protect integrity of development toolchains.
- Protect the integrity of development endpoints.
- Do attack surface management for deployed applications.

#### CONFIGURATION MANAGEMENT & VULNERABILITY MANAGEMENT
- Create or interface with incident response.
- Identify software defects found in operations monitoring and feed them back to engineering.
- Track software defects found in operations through the fix process.
- Have emergency response.
- Develop an operations software inventory.
- Streamline incoming responsible vulnerability disclosure.
- Fix all occurrences of software defects found in operations.
- Enhance the SSDL to prevent software defects found in operations.
- Simulate software crises.
- Operate a bug bounty program.
- Automate verification of operational infrastructure security.
- Publish risk data for deployable artifacts.

**Figure 2. THE BSIMM SKELETON.** Within the SSF, the 128 activities are organized into 12 BSIMM practices, which are held within four domains.

---

# PART 2: TRENDS AND INSIGHTS

## NORMALIZED BSIMM ACTIVITY COUNTS

When tracking historical data across the BSIMM data pool, sometimes it is necessary to adjust the raw activity counts to match the current year’s BSIMM data pool count. This allows us to perform apples-to-apples comparisons and accurately report on activity growth or decline. As such, historical percentages and counts reported in the BSIMM16 Trends and Insights section may not align with BSIMM15 or prior reports.

This year has been defined by firms coming to grips with challenges on multiple fronts: government regulations, developer use of large language models (LLMs), application security programs that are both lean and enable development instead of hindering it, to name just a few. Training is changing across the industry as well, as companies prepare for LLM-assisted code authorship and shifting how they treat security knowledge from being a new discipline to expected working knowledge in their developers. With this 16th iteration of the BSIMM, we can report on long-term trends from the data pool.

## AI/ML IS RESHAPING APPLICATION SECURITY PRIORITIES

In BSIMM15, we created a new activity meant to track how SSIs were preparing to support the use of LLM technologies in the SDLC, _[SR3.5] Create standards controlling and guiding the adoption of new technologies_. In the year since, we have observed that firms have approached or are preparing to approach this challenge through working groups and tiger teams of cross-discipline professionals who can anticipate and prepare for a variety of risks, i.e., legal, technical, operational, privacy, and security. While some firms are grappling with security testing and the architectural concerns associated with integrating this new functionality into the software they ship, many are also grappling with challenges brought by "vibe coding," or the process of creating software and source code through a conversation with an LLM agent vs relying solely on human developers for coding.

## PREPARING HUMANS FOR AI CODE GENERATION

Human developers remain the first line of defense against the introduction of risk into firms’ software portfolios, especially with the newly available AI/ML tooling in use. Currently, LLM-generated code is not secure by default, but it looks plausible, professional, and well-written, even if it may be missing key security controls or include exploitable logic that would produce vulnerabilities in the released product. The first step in understanding what the weaknesses of LLM code generation are involve a general reading of the available attack intelligence published by researchers as they dig into this new technology, and _[AM1.5] Gather and use attack intelligence_ saw a 10% increase over BSIMM15. One of the earliest pieces of actionable guidance that firms can provide to developers is restricting where the new tooling can be used until a level of trust is established, so some firms invested in _[AA1.4] Using a risk ranking methodology to rank applications_, which saw a 12% increase over the previous year as firms determined which applications were cleared to allow LLM-generated code commits. Until LLM agents can generate code at the level of experienced and trained senior developers, firms will need to understand what their shortcomings are and where it is safe to use them.

## SECURITY TOOLS VS LLM CODING TOOLS

With human developers being the first line of defense as firms seek to build trust in their LLM-generated code, automated security tools are the next line. To enforce coding standards and ensure that the code not only adheres to general industry best practices but internal firm-specific practices as well, _[CR2.6] Use custom rules with automated code review tools_ has seen an increase of 10% over the previous year as firms adapt to the quirks present in LLM-generated code. While automated processes are on the rise, manual processes continue to decline, and firms are investing less in _[ST1.3] Driving tests with security requirements and security features_ as they look to shore up automated solutions to problems caused by increased automation—accordingly, observations of that activity dropped by 9% in the past year. As off-the-shelf automated solutions to LLM-generated code problems become more available, we expect firms to prioritize them, but we would still encourage robust human-driven testing of any features developed in conjunction with AI.

## REGULATORY PRESSURES

Over the past few years, governments have been grappling with the nationwide impacts of software security vulnerabilities and have sought to pass regulations and requirements that seek to protect their populations from the harm that exploited software vulnerabilities can have. Governing bodies for major markets are requiring or have already required software assurance actions from vendors and suppliers, and firms have begun to meet those requirements. Observations of _[SE3.10] Protect the integrity of development endpoints_ have grown by 6 observations since its introduction in BSIMM15, which is when we also added _[SE3.9] Protect integrity of development toolchains_, which has grown by 12 observations over the same period of time. With the Cyber Resiliency Act approved in the EU regulatory process, we’ll have to see if mandated design review and security requirement-based activities increase as the 2027 deadline to comply approaches.

## TECHNICAL SOLUTIONS TO REGULATORY REQUIREMENTS

When choosing to meet a regulatory requirement, firms overwhelmingly choose to implement automated solutions where they are available and affordable. Two such areas that we saw growth in were automating infrastructure security verification and SBOM generation. As governments seek to manage risk in digital products, they mandate that firms maintain the capability to generate SBOMs, so we have measured an almost 30% growth in observations of _[SE3.6] Create bills of materials for deployed software_. As cloud platforms become even more ubiquitous, the automation and tooling they enable allows firms to meet operational security requirements, so the activity _[CMVM3.5] Automate verification of operational infrastructure security_ grew by more than 50% over the previous year. As automation enables security best practices among early adopters and security-aware firms, we can expect governments to codify realistic security mandates into regulations to encourage more widespread adoption.

## STANDING UP PROCESSES TO MEET REQUIREMENTS

Another area that government regulations can impact is found in the manual processes that firms may have shifted focus away from in the drive to save limited resources for automation. However, not all manual processes can be discontinued without issue, so governments are requiring that firms better manage risk through visibility and communications. One activity that has seen almost a 20% growth over the previous year is likely driven by industry and governmental requirements, i.e., _[PT2.3] Schedule periodic penetration tests for application coverage_. Another area that is especially important for the upcoming European Cyber Resilience Act (EU CRA) as well as the US Government Self-Attestation Requirement is the requirement to facilitate processes that allow vendors to better respond to reports from customers, researchers, and government entities, which helps explain why _[CMVM2.4] Streamline incoming responsibility vulnerability disclosure_ grew by over 40% since BSIMM15. As firms seek to meet compliance requirements within the EU CRA, we expect to see even more growth in activities around design reviews, risk assessments, and security requirements.

## SOLVING THE DOCUMENTATION PROBLEM

It’s an old saw in the development profession that documentation is the first thing everybody complains about and the last thing anybody wants to do. The security regulations being passed by governments have almost as many requirements around creating documentation as they have for firms to perform security actions in the first place, so many of the firms seeking to pass an audit or prove compliance are often engaged in _[CP3.1] Document a software compliance story_, which can walk auditors through all the documentation generated by that firm; accordingly, this activity grew by more than 20% over the past year. Another area that government regulations are pushing firms toward is the area of increased security requirement fidelity, and one way firms are meeting that push is with _[SR3.4] Create standards for technology stacks_, which distill security requirements into easily consumable engineering documents for developers to follow and grew by more than 40% over the past year.

## SOFTWARE SECURITY TRAINING IS EVOLVING

In the long-term trends section of the BSIMM15 report, we reported that traditional software security training (_[T1.1] Conduct software security awareness training_) had reached an all-time low of just 51.2% of the firms in the BSIMM15 data pool still conducting software security awareness training. This follows a long decline that has been in progress since BSIMM2. At the time of the BSIMM15 report, we had not yet begun to look deeper and speculated that the topic might be poised to begin a comeback, with some anecdotal evidence pointing in that direction.

Instead, what we found as we discussed the topic with experts and began to ask questions during BSIMM assessments is that software security training is evolving. The traditional training method of attending a multi-hour or multi-day class is on the decline, but new training methods are taking its place. We reported that _[T2.12] Provide expertise via open collaboration channels_ is on a steep rise, providing nearly instantaneous access to subject matter experts and training on a topic of immediate importance, a just-in-time training capability. Firms are also beginning to supplement these open collaboration channels with targeted, short-form training nuggets based on immediate needs that are being identified by trends in application security test efforts (an example of _[T2.8] Create and use material specific to company history_ and _[CR2.8] Use centralized defect reporting to close the knowledge loop_). They’re also being identified via attack intelligence (_[AM1.5] Gather and use attack intelligence_, _[AM2.6] Collect and publish attack stories_), with knowledge being turned into bite-sized, easily consumed training tidbits that do not take engineers away from their main tasks for very long. These bite-sized training tidbits might be an email blast to developers or short-form videos of perhaps 5-10 minutes. These tidbits might be targeted at a specific team or even individual developers, depending on need, or they may be sent out to everyone.

Several things seem to be driving this, namely, that traditional classroom training methods are disruptive and costly. In the days of waterfall development, sending developers to a day or several days of training had an impact, but it was nowhere near as severe as in the world of two-week sprints. Just-in-time tidbits are more immediately actionable than hours of training that might not be useful for weeks or even months. Generational differences are also in play here as younger staff members are more culturally in tune with short-form informational efforts.

## TOPICS WE’RE WATCHING

This year continued to see changes in how firms integrated new technologies into their software and met regulatory challenges. The demands of cloud, toolchains, tools, application security adjacencies, AI, and government scrutiny have led to a vastly increased program scope, which is in turn necessitating a new era of shared responsibility between SSGs, engineering, legal, and other stakeholders interested in taking advantage of AI/LLM technologies.

Participant feedback indicates that the following might influence their future efforts:
- The continuing impact of regulations on the software industry as governments mandate security as an essential element of software products that run in critical infrastructure.
- How things change as the industry continues to mature and develop security solutions for developer use of AI.

---

# PART 3: FOR PRACTITIONERS

## INTRODUCTION

In Part 3, we take a look at industry topics that are important for software security programs as well as review how to build or upgrade a software security program.

## SSDF-BSIMM MAPPING UPDATED FOR BSIMM16

The NIST SP 800-218 v1.1 Secure Software Development Framework (SSDF) standard was released in February 2022 and specifies 42 different tasks that organizations should do as part of a secure software development lifecycle (SSDL), as well as things to do to secure the development environment. The SSDF draws from a wide variety of existing frameworks as both a basis for itself and as references that organizations can use. One of the most referenced frameworks is the BSIMM, and accordingly, the SSDF refers to it and Executive Order 14028 more than any other framework (see Figure 3).

### Top 10 Referenced Standards/Frameworks
- EO 14028: 42
- BSIMM: 39
- BSAFSS: 38
- IEC62443: 38
- SP800181: 37
- SP80053: 35
- SP800161: 35
- PCISSLC: 28
- OWASPSAMM: 26
- SCSIC: 23

**Figure 3. SSDF REFERENCES TO OTHER FRAMEWORKS.** The BSIMM is the second most referenced framework in the NIST standard.

Unfortunately, the NIST standard refers to BSIMM12, and between BSIMM12 and BSIMM16, many BSIMM activity numbers have changed as activities became more or less common—for example, the SSDF references SE2.6 from BSIMM12, but after the NIST standard was published, SE2.6 became more common and is now known as SE1.3. Looking for SE2.6 will not work unless you know the activities have changed.

Since the SSDF standard was released, 13 activities have moved between levels, but because some are referenced by more than one SSDF task, a total of 16 tasks have been affected. Table 3 shows the updated BSIMM mappings for these 16 tasks.

### SSDF TASKS AFFECTED BY BSIMM MOVES

| Task (Original) | Change | BSIMM16 | Task (Original) | Change | BSIMM16 |
| --- | --- | --- | --- | --- | --- |
| PO.1.1 SE2.6 | Becomes | SE1.3 | PW.4.4 SR2.4 | Becomes | SR1.5 |
| PO.1.2 SM2.2 | Becomes | SM1.7 | SR3.1 | Becomes | SR2.7 |
| PO.2.2 T3.4 | Becomes | T2.11 | PW.7.2 CR1.6 | Becomes | CR2.8 |
| PO.4.1 SM2.2 | Becomes | SM1.7 | PW.9.1 SE2.2 | Becomes | SE1.4 |
| PO.4.2 SM2.2 | Becomes | SM1.7 | PW.9.2 SE2.2 | Becomes | SE1.4 |
| PW.1.1 AM2.2 | Becomes | AM3.4 | RV.1.1 CMVM2.1 | Becomes | CMVM1.4 |
| AM2.5 | Becomes | AM3.5 | CMVM3.7 | Becomes | CMVM2.4 |
| AA1.3 | Becomes | AA2.4 | RV.1.3 CMVM2.1 | Becomes | CMVM1.4 |
| PW.2.1 AA1.3 | Becomes | AA2.4 | CMVM3.7 | Becomes | CMVM2.4 |
| PW.4.1 SR2.4 | Becomes | SR1.5 | RV.2.1 CMVM2.2 | Becomes | CMVM1.3 |
| SR3.1 | Becomes | SR2.7 | RV.2.2 CMVM2.1 | Becomes | CMVM1.4 |

**Table 3. SSDF TASKS AFFECTED BY BSIMM MOVES.** Several BSIMM activities have changed activity numbers since NIST released the SSDF, so this table updates the NIST references to their current BSIMM activity numbers.

BSIMM14 and BSIMM15 added activities that could be mapped to NIST standards but have not officially been mapped by NIST. Table 4 shows these unofficial mappings.

| Task (Original) | Change | BSIMM16 |
| --- | --- | --- |
| PO.1.1 | None | Could Add SE3.9 |
| PO.3.1 | None | Could Add SE3.9 |
| PO.3.2 | None | Could Add SE3.9 |
| PO.3.3 | None | Could Add SE3.9 |
| PO.5.1 | None | Could Add SE3.10 |
| PO5.2 | None | Could Add SE3.10 |

**Table 4. NEW BSIMM ACTIVITIES THAT COULD BE MAPPED TO THE SSDF STANDARD.** These BSIMM activities did not exist when NIST released the SSDF standard, but they could apply to these SSDF tasks.

By updating NIST’s original mapping of BSIMM12 activities to the SSDF tasks with the current BSIMM16 activity numbers, readers can better track NIST’s intent to the current BSIMM framework.

## AI/ML AND BSIMM16

The most common question we get asked is, "How is BSIMM16 going to change for AI/ML?" Well, here’s the answer: we’re updating and highlighting existing activities that have an impact on AI/ML security, and in BSIMM15, we added, in our opinion, a long overdue activity (_SR3.5_ discussed below) around proactively planning to mitigate the impacts of new technologies on security.

### AI/ML

Application security, like any area of technology, has to keep pace with rapid developments that seemingly upend everything once or twice a decade. The AI/ML and LLM releases of the past few years are both exciting and terrifying for security professionals: exciting because new LLMs can perform many security tasks that were exclusively human, and terrifying because they can also perform many hacking tasks that were exclusively human. On a technical level, LLMs represent a new attack surface with a new class of vulnerabilities and security requirements that the industry is still figuring out in real time. As if that weren’t enough, LLMs seem to completely reinvent themselves every month by not only adding features and improving functionality but also by moving into completely new areas: first text and chat, then image generation, and at the time of writing, desktop productivity tasks.

To stay ahead of the innovation curve, developers need AppSec programs to provide solutions, guidance, and best practices that help them safely adopt new technology. In return, AppSec needs to rely on subject matter experts to both help them understand how these new technologies will be used as well as to get buy-in from development to stay flexible as the threat landscape evolves. This collaborative effort will often involve members from legal for support around regulatory updates, operations and IT for the software environment, and communications teams to keep everyone up to date.

## SIX KEY ACTIVITIES: USING THE BSIMM TO DEAL WITH AI/ML

Plenty of existing BSIMM activities can help teams address the AI/ML problem space. Whether the priority is keeping on the right side of emerging regulations, defending against emerging attacks, or enabling developers who want to take advantage of coding copilots, BSIMM16’s six key activities can help:
- **_[SR3.5] Create standards controlling and guiding the adoption of new technologies_**. While AI/ML may seem new and intimidating, SSGs have been faced with integrating security best practices into anything and everything new that their developers could think up for years. Since the first version of the BSIMM was published, SSGs have had to secure mobile applications, cloud environments, containers, new languages, and new frameworks, all while developers have shifted from waterfall and spiral development lifecycles to Agile lifecycles and DevSecOps cultures. Some firms have proactively created working groups that examine these new technologies and processes to understand potential security needs while the industry is still reeling from being turned upside down once again. This activity is beneficial to firms looking to take advantage of innovations that are on the cutting edge of technology. It’s not enough to have one smart individual who researches interesting new topics and then tells people about it; this is an activity for firms that rigorously examine and workshop the implications of adopting a new technology and then create actionable guidance for developers, IT, and operations to follow. We’ll be looking for new security requirements and controls, updates to policy, tooling customizations, and other proactive methods that firms use to fill the gap left by the absence of industry best practices for brand-new technologies.
- **_[AM1.5] Gather and use attack intelligence_**. While most firms may rely on automated tooling and skilled pen testers to thoroughly exercise an application’s potential security vulnerabilities, that’s not an option for technologies as new as LLMs. Instead, researchers are hard at work finding new ways to attack and defeat AI/ML safeguards or discover new vulnerabilities and exploits that don’t exist in today’s software types. It’s up to individual organizations to have a designated threat intelligence function that collects publicly available research and helps everyone learn about these emerging vulnerability exploits.
- **_[AM3.4] Create technology-specific attack patterns_**. Once new exploits are collected, organizations should build a catalog of attacks specific to the use cases and types of AI/ML or LLM that developers are integrating or taking advantage of. These attack patterns should cover everything from novel attacks like prompt injection to traditional vulnerabilities that could apply to the API interface, cloud host, or other technologies that make up the complete implementation to uncover potential interactions, e.g., potentially using prompt injection to get an LLM to output malicious payloads that could compromise underlying databases or parsers.
- **_[SFD3.1] Form a review board to approve and maintain secure design patterns_**. Once attack patterns are built for the organization’s intended AI/ML or LLM uses, firms should seek to combine solutions and mitigations to the attacks in approved design patterns. These patterns could cover all parts of a scratch-built AI/ML-enabled application or provide security guidance when integrating commercially available AI/ML components.
- **_[SM3.5] Integrate software supply chain risk management_**. It’s vital to remember that despite how new LLMs feel, they are still hosted in cloud environments or released as open source bundles of Python and training data. Firms should expand software supply chain risk management to account for attacks that could compromise third-party AI/ML services by fully documenting and understanding the shared responsibility model for cloud-hosted services, mandating privacy and security service-level agreements (SLAs) in vendor contracts, and expanding the data classification guide to cover types of data that can and can’t be shared with third-party AI/ML solutions. Additionally, companies will want to build requirements around training data to prevent potential legal issues.
- **_[CMVM1.1] Create or interface with incident response_** or **_[CMVM2.4] Streamline incoming responsible vulnerability disclosure_**. As AI/ML and LLMs become more integrated into software products, vulnerabilities discovered by external researchers or internal teams will require rapid disclosure handling and operational response. Streamlining vulnerability intake and coordinating with incident response ensures that newly discovered AI-specific flaws (such as model extraction, data poisoning, or prompt injection exploits) are remediated quickly and effectively across the product lifecycle.

---
[^1]: Footnote content here.

---

m, defined
liability due to the inclusion of copyrighted data or that prevent processes for interacting with software security stakeholders,
the “Garbage In, Garbage Out” problem that can compromise and a documented software security approach that is clearly
the AI/ML model’s integrity by sourcing problematic or false connected to executive expectations for both managing
training data. software security risk and progressing along a roadmap to
scale security capabilities. A maturing SSI is learning from
• [CR1.5] Make code review mandatory for all projects. For firms
its existing efforts, likely making consistent, incremental
that aren’t looking to build or maintain AI/ML applications or
improvements in the SSDL and key security integrations.
LLMs but still want to take advantage of the efficiency gains
Example improvements include:
of this new technology, the first avenue for many of them
is enabling developers to take advantage of AI/ML copilots - Reducing friction across business and development
that can speed up source code creation and updates. These stakeholders
copilots aren’t infallible, and the source code they produce is - Protecting people’s productivity gains through automation
likely to not be perfectly secure, so to address the potential investments
for vulnerabilities included in source code generated by AI/ML - Building bridges to other parts of the firm through
copilots, we would advise checking the source code for those evangelism, defect discovery, software supply chain
vulnerabilities. Making automated static application security protection, and incident response
testing ( SAST) scans mandatory will go a long way to making - Undergoing a “shift everywhere” transformation to efficiently
AI/ML-enabled development more secure. test software artifacts as soon as appropriate
- Adjusting the security strategy to keep pace with changes in
WHAT’S NEXT? risk and risk management processes
- Finding solutions to systemic problems and making them
As we conduct BSIMM assessments under the BSIMM16 broadly available as reusable, pre-approved IP
framework, we’ll continue to measure how firms are securing - Responding quickly when attacks or other circumstances
AI, ML, and LLMs. Look for an update in the next annual BSIMM uncover a lack of resiliency
report as firms continue to solve AI/ML security problems and
• Enabling. An enabling SSI ensures that all stakeholders can
industry best practices catch up.
meet their objectives without putting the organization at
unacceptable risk. The following are important principles for an
enabling SSI:
HOW TO BUILD OR UPGRADE AN SSI
- There is continuous evangelizing about the best way for all
Putting someone in charge is just a first step in building an SSI, stakeholders to meet security expectations, ensuring that the
there will be iterations of planning, growth, measurement, and path of least resistance for development and deployment is
bridge-building. You can use the processes below to guide your also the most secure path, along with investing to proactively
SSI’s growth from newly emerging through dependable maturity. overcome various people, process, technology, and cultural
growing pains.
- The evolutionary needs of the SSI are harmonized with the
The BSIMM is not just a long-term software security study goals of business initiatives, such as digital transformation,
or a single-purpose SSI benchmarking tool—it also eases open source use, and cloud adoption.
management and evolution for anyone in charge of software - A mature and integrated response to process and technical
security, whether that person is currently in a central risk invokes an innovation engine to make reasonably future-
proof solutions.
BSIMM16 19

- The use of culturally engrained approaches to automation, management. This SSG stayed in the corporate organization
blameless review of failures, and protection of critical chart, had the power to enact organization-wide policy, and
resources—people, for example—allow more time to tackle expanded its efforts outward through, for example, tooling
security innovation. and security champions. This path was seen most often in
- A platform engineering perspective removes security activity regulated industries such as banking, insurance, FinTech, and
silos and ensures that all telemetry and benefits are available healthcare but was also seen in ISV and technology firms.
to all stakeholders everywhere.
• Organizations where the SSG was started by engineering
It’s compelling to imagine that organizations could reach a state technical leadership (e.g., senior application architects) as
of emerging, maturing, or enabling simply by applying a certain a part-time role and focused on technical software security
number or mix of activities to specific percentages of the staff and efforts, such as configuration hardening, technology stack
software portfolio, but that doesn’t happen. Experience shows that standards, secure coding standards, and security tool
SSIs usually reach an emerging stage by organizing all the ad hoc integration, which was often done for a single toolchain or
software security efforts they’re already doing into one program. project. As evangelism efforts convinced other development
SSIs usually proceed to the maturing stage by focusing on the projects to use the same technical controls, the technical
activities that are right for them without regard for the total activity leadership usually worked with a CTO, VP Engineering, or
count—this is especially true when considering the complexity of other technology executive to establish a centralized security
scaling some activities across 100, 1,000, or 10,000+ applications function within the engineering domain. The centralized
or people. function—often still part time—then used its influence to
establish its own type of governance, which was often peer
Organizations rarely move their entire SSI from emerging to
pressure to set some development process, create and
enabling all at once. We have seen SSIs form, break up, and re-
manage security standards, and ensure that the silos of
form over time, so an SSI might shift between emerging, maturing,
engineering, testing, and operations were aware of and adhered
and enabling a few times over the years. In addition, capabilities
to general security expectations. This path was most often
within an SSI (e.g., supply chain security or training) likely won’t
seen in technology, cloud, and ISV firms but was also seen in
progress through the same states at the same rate. We’ve noted
other verticals.
cases where one capability—vendor management, for example—
might be emerging, while the defect management capability is Regardless of its origin point, each culture usually arrived at an SSI
maturing, and the defect discovery capability is in the enabling driven by a centralized, dedicated SSG whose function is to ensure
stage. There is also constant change in tools, skill levels, external that appropriate software security activities are happening across
expectations, attackers, attacks, resources, culture, and everything the portfolio, so nearly all SSIs that are more than a couple of years
else. You can use the BSIMM16 participants scorecard (see Figure old are driven top-down by governance objectives, even those
18 in Part 7) to see the frequency with which BSIMM activities started by engineering for engineering. Evangelism, peer pressure,
are observed across all participants, but use your own metrics to and local implementations go only so far in formally implementing
determine if you’re making the progress that’s right for you. software security risk management as a culture.
Today, as you start or plan a major revamp of your SSI, just get
CONSTRUCTION LESSONS FROM OUR
started. You can start in corporate, or you can start in engineering.
PARTICIPANTS
You can start with governance as a top priority, or you can focus
The purpose of the BSIMM is to measure SSIs. While the BSIMM on some technical controls. In any case, history seems to show
doesn’t directly measure SSI architecture, evolution, or motivations, that SSIs gravitate toward a focus on policy along with process
our experience with more than 304 organizations since 2008 has that ensures adherence. Yours likely will as well.
highlighted cultural differences in SSI implementations.
No SSI is built in a vacuum. Whether your SSI is just emerging or
has some capabilities in the maturing stage, knowledge from both
the struggles and successes of other organizations can save you WHETHER YOUR SSI IS
time and disruption. As software security becomes an important
goal for any organization, multiple internal groups might each JUST EMERGING OR HAS
be taking their own approach to their goals. Understanding and
harmonizing these cultural and technological views into a single SOME CAPABILITIES IN
SSI is important to long-term success.
THE MATURING STAGE,
CULTURES
KNOWLEDGE FROM BOTH
Whether implicitly or explicitly, organizations choose the path for
their software security journey by tailoring goals, methods, tools,
THE STRUGGLES AND
resources, and approaches according to their individual cultures.
There have always been two distinct cultures in the BSIMM
SUCCESSES OF OTHER
participants:
• Organizations where the SSG was started by executives in a ORGANIZATIONS CAN SAVE
central corporate group (e.g., under a CISO) as a full-time role
and chartered with software security governance, including YOU TIME AND DISRUPTION.
compliance, testing, remediation monitoring, and risk
BSIMM16 20

A NEW WAVE IN ENGINEERING CULTURE
Over the past few years, we’re seeing a new wave of software Executive-led Engineering-led
Compliance-oriented Procedure-oriented
security efforts emerging from engineering teams. These teams
are usually responsible for delivering a product or value stream
(such as is common within ISVs) or maintaining a technology
domain (such as the “cloud security group” or a part of some
digital transformation group). Some organizations refer to Centralized
governance (SSG)
these collective security efforts as site reliability engineering,
DevSecOps, or GitOps security, but some have no specific name
for it at all.
2nd-generation
At least three factors drive these new efforts: engineering-led efforts
(DevOps)
• The confluence of process friction, unpredictable impacts
on delivery schedules, adversarial internal relationships,
and a growing number of human-intensive processes from
existing SSIs; top-down governance doesn’t fit culturally or
technologically with new engineering processes. Corporate Modern hybrids Engineering
(GRC) (DevSecOps) (self-service)
• The demands and pressures from modern software delivery
practices, be they cultural such as Agile and DevOps, or
technology-based such as cloud- and orchestration-based;
gates and checkpoints built for maximum assurance often
Corporate Engineering
cause unacceptable disruption in processes built for speed.
Figure 4. SSG EVOLUTION. These groups might have started in
• The shift to engineer self-service, typically seen as self-service
corporate or in engineering, but in general, they settled on enforcing
IT (cloud), configuration and deployment (DevOps), and compliance with tools. The new wave of engineering efforts is shifting
development (open source use and continuous integration); where SSGs live, what they focus on, who is accountable for what, and
the ability to instantiate infrastructure and pipelines is also the how stakeholders work together.
ability to integrate your own security tools and configurations.
This new software security effort is frequently happening
The important lesson here is that this is likely happening in your
independently from the lessons learned that an experienced SSG
organization as well—perhaps narrowly in a few development
might provide. In addition, this effort is driving many application
teams or perhaps broadly as a cultural shift across all of
lifecycle processes ever faster, regardless of whether the
engineering. Taking an SSI to the maturing stage—and possibly
organization is ready to do software security risk management at
to enabling as well—requires acknowledging this engineering
that speed.
effort and building bridges between all stakeholders who have
The governance-oriented approaches we’ve seen for years, along ownership of the different aspects of software security. It also
with this new wave of engineering-oriented efforts, are increasingly requires acknowledging that these different stakeholders have
coexisting within the same organization. In addition, they often different business objectives and different views of risk, risk
have competing objectives, which is pulling traditional governance- management, and risk tolerance relative to those objectives.
driven programs into modern and evolving hybrids. Figure 4 shows Ensuring that everyone can meet their objective while also keeping
this ongoing SSG evolution. the organization safe is a major goal for every SSI.
BSIMM16 21
s0002
ylraE
6002
acriC
yadoT

UNDERSTANDING MORE ABOUT DEVOPS a single application and technology stack. Even so, these groups
sometimes struggle to institutionalize durable gains, usually
The DevOps movement has highlighted the tensions between
because the engineers have not yet been able to turn capability
established SSIs and engineering efforts that address software
into either secure-by-default functionality or automation-friendly
security their own way with their own processes. Given
assurance—at least not beyond the most frequently encountered
different objectives, we find that the outcomes desired by
security issues and beyond their own spheres of influence.
these two approaches usually differ—rather than the top-down,
compliance-driven style of governance-minded teams, these Engineering groups tend to view security as an enabler of software
newer engineering-minded teams are more likely to prototype features and code quality. These groups recognize the need for
good ideas for securing software, which results in the creation of having security standards but tend to prefer incremental steps
even more code and infrastructure on the critical path to delivery toward governance-as-code as opposed to a large manual-steps-
(e.g., security features, homespun vulnerability discovery, security with-human-review approach to enforcement. This tends to result
guardrails). in engineers building security features and frameworks into
architectures, automating defect discovery techniques within a
Here, security is just another aspect of quality, and availability
software delivery pipeline, and treating security defects like any
is just another aspect of resilience. To keep pace with both
other defect. Traditional human-driven security decisions are
software development process changes (e.g., CI/CD adoption)
modeled into a software-defined workflow as opposed to being
and technology architecture changes (e.g., cloud, container, and
written into a document and implemented in a separate risk
orchestration adoption), engineering efforts are independently
workflow handled outside of engineering. In this type of culture,
evolving both how they apply software security activities
it’s not that the traditional SDLC gates and risk decisions go away,
and, in some cases, what activities they apply. The changes
it’s that they get implemented differently and usually have different
these engineering teams are making include downloading and
goals compared to those of the governance groups. SSGs, and
integrating their own security tools, spinning up self-service cloud
likely security champions groups as well, that begin to support this
infrastructure and virtual assets as they need them, following
approach will speed up both convergence of various efforts and
policy on the use of open source software (OSS) in applications
alignment with corporate risk management goals.
but routinely downloading many other open source packages
to build and manage software and processes, etc. Engineering To summarize the lessons from our participants, scaling an
efforts and their associated fast-paced evolutionary changes are emerging SSI across a software portfolio is hard for everyone,
putting governance-driven SSIs in a race to retroactively document, and stakeholders need to understand the lessons above before
communicate, and even automate the knowledge they hold so that investing heavily in the journey from emerging to maturing.
it can be useful to everyone.
Today’s evolving cultural and technological environments require
Cloud service providers, software pipeline and orchestration a concerted effort at converging governance and engineering
platforms, and even QA tools have also begun adding their view of objectives to create a cohesive SSI that ensures the software
software security in their feature sets. For example, organizations portfolio is appropriately protected.
are seeing platforms like GitHub, Azure DevOps, and GitLab
competing by using security as a differentiator. Evolving vendor- FOR AN EMERGING SSI: SDLC TO SSDL
provided features might be signaling to both the marketplace and It’s unlikely that any organization is doing nothing about software
adopting organizations that vendors believe security must be security. Even an organization without a formal initiative or a
included in developer tools and that engineering security initiatives defined owner likely has some software security policy, AST, and/
should feel comfortable relying on these external platforms as or processes for working with stakeholders. Provided below
the basis of their security telemetry and even their governance are actionable steps for consolidating an ad hoc effort into an
workflows. emerging SSI. Keep in mind that most SSIs are multiyear efforts
with real budgets, mandates, and ownership behind them, though.
Again, the important lesson is that this is likely happening in your
In addition, while all initiatives look different and are tailored to
organization as well. Your path to an emerging or mature SSI must
fit a particular organization, most initiatives share common core
account for this federation of software security responsibilities
activities (see Table 10 in Part 7).
and use of external providers, yet also enable every stakeholder to
meet their business and security objectives. Figure 5 organizes the steps and suggested timeline to establish
an emerging SSI, along with the associated BSIMM activities.
CONVERGENCE AS A GOAL
It also includes a notional level of effort anticipated across
We frequently observe governance-oriented SSIs planning centrally, people and budget, as well as estimated duration, all on a 1-to-3
seeking to proactively define an ideal risk posture during their scale. The effort and cost to reach each of these goals will vary
emerging or early maturity phases. Initial uptake of the provided across companies, of course, as they are primarily affected by
controls (e.g., security testing) is usually by those teams that have risk objectives, organizational structure, and portfolio size. For
experienced real security issues and are looking for help, while example, deploying onsite static analysis across 10 applications
other teams might take a wait-and-see approach. using a common pipeline in one business unit will likely have
a lower level of effort than deploying that same static analysis
We also observe that engineering efforts prototype controls
across 10 applications built in 10 toolchains in 10 business units.
incrementally, building on existing tools and techniques that
already drive software delivery. Gains happen quickly in these
emerging efforts, perhaps given the steady influx of new tools and
techniques introduced by engineering but also helped along by the
fact that each team is usually working in a homogenous culture on
BSIMM16 22

APPLY
|       | CREATE A  | DOCUMENT   |     | INVENTORY     |     |                 |     | DEPLOY DEFECT   |     |              |     |
| ----- | --------- | ---------- | --- | ------------- | --- | --------------- | --- | --------------- | --- | ------------ | --- |
|       |           |            |     |               |     | INFRASTRUCTURE  |     |                 |     | PUBLISH AND  |     |
|       | SOFTWARE  | AND        |     | APPLICATIONS  |     |                 |     | DISCOVERY FOR   |     |              |     |
| PHASE |           |            |     |               |     | SECURITY IN     |     |                 |     | PROMOTE THE  |     |
|       | SECURITY  | SOCIALIZE  |     | IN THE SSG’S  |     |                 |     | HIGH-PRIORITY   |     |              |     |
|       |           |            |     |               |     | SOFTWARE        |     |                 |     | PROCESS      |     |
|       | GROUP     | THE SSDL   |     | PURVIEW       |     |                 |     | APPLICATIONS    |     |              |     |
ENVIRONMENTS
|            |       | SM1.1 |     |       |     |     |       |     |       |     | SM1.4 |
| ---------- | ----- | ----- | --- | ----- | --- | --- | ----- | --- | ----- | --- | ----- |
|            | CP1.1 | SM2.7 |     |       |     |     |       |     |       |     | SM3.4 |
| GOVERNANCE |       |       |     |       |     |     | SE1.4 |     |       |     |       |
|            |       | AM3.5 |     |       |     |     |       |     |       |     | CP1.3 |
|            |       | CR2.7 |     |       |     |     |       |     |       |     | SR1.1 |
|            |       |       |     | AM1.2 |     |     |       |     |       |     | SM1.3 |
|            | T1.1  | SR1.2 |     |       |     |     |       |     |       |     |       |
| ENABLEMENT |       |       |     | CP2.1 |     |     |       |     | AA1.4 |     | SR1.2 |
SFD1.1
CMVM2.3
AA1.1
CR1.4
FLAW AND
SR1.5
| DEFECT   | SFD1.2 |     |     | SR1.5 |     |     |     |     |     |     | ST3.6 |
| -------- | ------ | --- | --- | ----- | --- | --- | --- | --- | --- | --- | ----- |
ST1.4
DISCOVERY
PT1.1
CMVM3.4
SE1.2
| OPERATIONS |     |     |     | CMVM1.1 |     |     | SE1.3 |     |     |     |     |
| ---------- | --- | --- | --- | ------- | --- | --- | ----- | --- | --- | --- | --- |
SE2.7
|               |          | ●       |      |     |        |     |            |     |   ●        |     |     ●    |
| ------------- | -------- | ------- | ---- | --- | ------ | --- | ---------- | --- | ---------- | --- | -------- |
|               |          | ●       |   ●  |     | ●   ●  |     | ●   ●   ●  |     | ●   ●   ●  | ●   |   ●   ●  |
|               | ●   ●    | ● ●   ● |   ●  | ●   | ●   ●  |     | ●   ●   ●  |     | ●   ●   ●  | ●   |   ●   ●  |
| People Budget | Duration |         |      |     |        |     |            |     |            |     |          |

The arrow of time (x-axis) is a notional order of efforts. Although this diagram appears to depict a waterfall process, many of these
efforts will be happening at the same time, and some will be repeated multiple times.
Figure 5. GETTING STARTED ROADMAP WITH NOTIONAL EFFORTS. This roadmap is supplemented with relative
effort levels so that organizations can plan the resources needed for their emerging SSI.
Note that the getting started roadmap shown in Figure 5  Note that an SSG leader with a young initiative (e.g., less than 18
includes some activities that have a high impact for emerging  months) working on foundations should not expect or set out to
SSIs, even though they appear to be rarely observed in the  quickly implement too many BSIMM activities. Firms can absorb
BSIMM data pool. This happens because newly added BSIMM  only a limited amount of technology, hiring, cultural, and process
activities start with an observation rate of zero (e.g., [ST3.6]  change at any given time. The BSIMM16 data shows that SSIs
added for BSIMM11). These are foundational activities, even  having an age of 18 months or less at the time of assessment (20
if organizations are just starting to add them to their journeys.  of 111 firms) have an average score of about 32, showing they
Importantly, the steps described here are not specific to  are investing in software security but are not rushing ahead too
| where in the organization the SSG is created—the SSG can be  |     |     |     |     |     | rapidly. |     |     |     |     |     |
| ------------------------------------------------------------ | --- | --- | --- | --- | --- | -------- | --- | --- | --- | --- | --- |
centralized in a governance group or an engineering group, or
it can be federated across both. Regardless, governance and
engineering functions will have to cooperate to ensure the
achievement of organizational software security goals.
| BSIMM16 |     |     |     |     |     |     |     |     |     |     | 23  |
| ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

DOCUMENT AND SOCIALIZE THE SSDL
CHECKLIST FOR EMERGING SSIs
To start, you’ll want to publish security policies and standards
through established governance, risk, and compliance (GRC) 1. Document and socialize the SSDL. Tell all stakeholders the
channels to complement existing IT security standards or create expectations for software security.
those channels as necessary to secure the SDLC. The SSG can
2. Create an SSG. Put a dedicated group in charge and give
also create a security portal (e.g., website or wiki) that houses
them resources.
SSDL information centrally [SR1.2]. Similar to the approach for
3. Inventory applications. Decide on what you’re going to
prioritizing defect discovery efforts by categorizing attacks and
focus on first, then apply good risk management.
bugs [AM3.5, CR2.7], we observe these emerging SSIs drive
initial standards creation from industry top risks, leveraging 4. Apply infrastructure security. Don’t put good software on
general sources such as MITRE, ISO, and NIST to form baseline bad systems or in poorly constructed networks (cloud or
requirements. otherwise).
Getting the word out about the organization’s top risks and what 5. Deploy defect discovery. Determine the issues in today’s
can be done about them is a key part of the SSG’s job. We observe in-progress and production applications, then plan for
these leaders using every channel possible (e.g., town halls, brown tomorrow.
bags, communities of practice forums, messaging channels) to 6. Manage discovered defects. Resolving issues reduces risk.
socialize the software security message and raise awareness of
7. Publish and promote. Roll out the secure SDLC and promote
the SSDL [SM2.7].
it both bottom-up and top-down.
Following are some details on the steps shown in Figure 5.
The included activity references are meant to help the reader
understand the associations between the topic being discussed
and one or more BSIMM activities. Note that the references don’t INVENTORY APPLICATIONS
mean the topic being discussed is fully equivalent to the activity, One of the first activities for any SSG is to create an initial
for example, when we say, “…initial inventory [AM1.2]” (i.e., Use inventory of the application portfolio under its purview [AM1.2,
a data classification scheme for software inventory), we don’t CMVM2.3]. As a starting point, the inventory should include
mean that having the initial inventory encompasses the totality each application’s important characteristics (e.g., programming
of [AM1.2], just that having it will likely be something you’ll do on language, architecture type, open source used [SR1.5]). Particularly
your way to implementing [AM1.2]. To continue using [AM1.2] as useful for monitoring and incident response activities [CMVM1.1],
an example, most organizations will not set about implementing many organizations will include relevant operational data in
this activity and get it all done all at once. Instead, an organization the inventory (e.g., where the application is deployed, owners,
will likely create an initial classification scheme and inventory, emergency contacts).
implement a process to keep the inventory up to date, and then
Inventory efforts tend to favor a top-down approach in the
decide how to create a view that’s meaningful for stakeholders.
beginning, usually starting with a questionnaire to elicit data from
Every activity has its own nuances and components, and every
business managers who serve as application owners, then using
organizational evolution path for its emerging SSI will be unique.
tools to find OSS. The SSG also tends to focus on understanding
CREATE A SOFTWARE SECURITY GROUP where sensitive data resides and flows (e.g., PII inventory)
[CP2.1] and the resulting business risk level associated with the
The most important first step for all SSIs is to have a dedicated
application (e.g., critical, high, medium, low).
SSG that can get resources and drive organizational change, even
if it’s a group of one person coordinating organizational efforts. When working with engineering teams, these efforts commonly
The SSG must understand which software security goals are attempt to extract software inventory data from the tools used to
important to the business and establish policy and process to drive manage IT assets. By scraping these software and infrastructure
everyone in that direction. At a minimum, the SSG should identify configuration management databases or code repositories, the
the risk management, compliance, and contractual requirements SSG crafts an inventory brick by brick rather than top-down.
that the organization must adhere to [CP1.1]. Using awareness
Maintaining an application inventory is a capability to be built over
training [T1.1] to then help ensure that everyone understands their
time rather than a one-time effort. To remain accurate and current,
security responsibility is a common approach.
the inventory must be regularly monitored and updated. As with
The SSG must work with engineering teams to establish a all data currency efforts, it’s important to make sure the data isn’t
common understanding of the approach to software security, overly burdensome to collect and is periodically spot checked for
which might be, for example, to set up automated defect discovery, validity. Organizations should favor automation for application
address security questions from developers with reusable security discovery and management whenever possible.
features [SFD1.1], and act as an advisor for design decisions
[SFD1.2].
BSIMM16 24

APPLY INFRASTRUCTURE SECURITY MANAGE DISCOVERED DEFECTS
Bad infrastructure security can undermine good software security, Unaddressed security defects are unmanaged risks. At first, there
which means the SSG must ensure that host and network security will be a large backlog of discovered security defects that will
basics are in place [SE1.2, SE3.10] as well as cloud security have to be bundled and passed through the risk exception process
controls [SE1.3]. Security engineers might begin by conducting and prioritized into the development backlog. After resolving the
this work manually, then baking these settings and changes into technical debt, the ongoing defect management process should
their software-defined infrastructure scripts [SE1.4] to ensure both be designed to deal with security defects as they are introduced to
consistent use within a development team and scalable sharing prevent their release into production systems.
across the organization.
When security defects are discovered, it is the responsibility of
Forward-looking organizations that have adopted software and the SSI to make sure they are logged and tracked through to
network orchestration technologies [SE2.7] (e.g., Kubernetes, completion [CMVM1.3]. Security defects can come from diverse
Envoy, Istio) get maximum impact from them with the efforts sources, including penetration testers [PT1.2], security tooling
of even an individual contributor, such as a security-minded [CR1.4], and operations [CMVM1.2], but ideally, they are logged in a
DevOps engineer. Though many of the technologies in which single source of truth for tracking purposes.
security engineers specify hardening and security settings are
PUBLISH AND PROMOTE THE PROCESS
human-readable, engineering groups don’t typically take the time
to extract and distill a document-based security policy from these With a strategy in hand, an understanding of the portfolio, and
codebases. security expectations set with engineering teams, the SSG
documents the SSDL [SM1.1] and begins collecting telemetry
DEPLOY DEFECT DISCOVERY
[SM1.4]. The SSDL should include clearly documented goals,
Regardless of business drivers, one of the quickest ways of roles, responsibilities, and activities, but the most usable SSDLs
transitioning unknown risk to managed risk is through defect also include process diagrams and provide contextual details for
discovery—automated tools, both static and dynamic, provide fast, each stakeholder. Many organizations seeking to consolidate ad
regular insight into the portfolio security posture, with experts hoc efforts into an emerging SSI will find a variety of SSDLs in use
doing the detailed testing for important applications [AA1.1, across engineering teams. In these cases, the new SSDL might
CMVM3.4]. While not necessarily done for the entire application be a replacement for all such approaches, but it might also have
portfolio, conducting some targeted vulnerability discovery to some parts that are abstract enough to account for processes until
get a feel for the current risk posture allows firms to motivate they can be rolled into the new approach. Publication is a good
the necessary conversations with stakeholders to gain buy-in time for the SSG to start a software security hub where the SSG
and prioritize remediation. Organizations tend to determine their can disseminate knowledge about processes and about software
high-priority applications via risk ranking [AA1.4], then phase in a security as a whole [SR1.2].
combination of manual testing techniques against these high-
In a top-down approach, organizations favor creating policy
priority applications, relying on automated testing techniques for
[CP1.3] and standards [SR1.1] that can be followed and audited
portfolio coverage.
like any other business process. Rather than documents,
Static and dynamic software testing techniques each provide however, engineering teams might favor implementing their part
unique views into an application’s security posture. Static of an SSDL inside of pipelines [SM3.4] and scripts [ST3.6] or by
analysis can look for issues inside the code the organization prescribing reusable security blocks that meet expectations. Over
develops [CR1.4] and inside third-party components [SR1.5]. time, the SSG will also have to deliver some policy in the form of
Dynamic application security testing (DAST) [ST1.4] can uncover governance-as-code in engineering pipelines [SM1.4].
immediately exploitable issues and help provide steps to
While executives have likely been engaged to get the SSI to this
reproduce attacks. In addition, QA groups can help ensure that
point, this is a good time to ensure that they are being regularly
development streams are adhering to security expectations.
kept up to date with software security. Remember, executive teams
All these testing results assist with prioritization and displaying
need to understand not only how the SSI is performing but also
impact to executive leadership.
how other firms are solving software security problems and the
Manual testing efforts generally start by bringing in third-party ramifications of not investing in software security [SM1.3].
assessors [PT1.1] on a regular cadence, either upon major
PROGRESS TO THE NEXT STEP IN YOUR JOURNEY
milestones or, more commonly, as a periodic out-of-band exercise
to assess the most critical applications. Even where an internal Usually done as part of moving to the mature stage, the SSG then
penetration testing function exists, a third party periodically proceeds to scale the SSI. For example, this scaling might be done
bringing in a unique perspective will be beneficial. by creating a security champions program, improving the inventory
capability based on lessons learned, automating the basics, doing
Note that engineering groups will tend to favor empowering
more prevention, and then repeating. As the initiative matures and
pipelines and testers with automation and allow engineering
the business grows, there will be new challenges for the SSG to
leadership or individual engineering teams to define some aspects
address, so it will be crucial to ensure that feedback loops are in
of mandatory testing and remediation timelines. It’s important
place for the program to consistently measure its progress and
to ensure static, dynamic, and manual testing creates minimal
maturity.
unnecessary friction in engineering processes.
BSIMM16 25

FOR A MATURING SSI: HARMONIZING can scale across the firm. Establishing this structure might not
OBJECTIVES involve hiring staff immediately, but it will likely entail assembling
a full-time team to implement key foundational activities central
With the foundations established, SSG leaders shift their attention
to supporting the assurance objectives further defined and
to scaling risk-based controls across the entire software portfolio
institutionalized in policy [CP1.3], standards [SR1.1], and processes
and enabling development to find and fix issues early in the
[SM1.1].
software lifecycle. The SSI has likely reached the emerging stage
across multiple capabilities (see Figure 5) and is maturing specific The SSG will require a mix of skills, including technical security
aspects of its initiative. This maturing includes both adding new knowledge, scripting and coding experience, and architectural skill.
activities and scaling existing ones (see Figure 6). It specifically As organizations migrate toward their view of DevSecOps, the SSG
includes building bridges between various software security might build its own software in the form of security automation,
efforts in corporate and engineering groups. defect discovery in CI/CD pipelines, and infrastructure- and
governance-as-code. SSGs often need to mentor, train, and work
directly with developers, so communication skills, teaching ability,
and practical knowledge are must-haves for at least some SSG
O
pti
mize P
la
n
s
p
t
e
a
r
f
s
f
o
.
n
E
,
s
1
s
0
e
,
n
o
ti
r
a
1
ll
0
y,
0
t
—
he
w
S
h
S
o
G
m
i
u
s
s
a
t
g
im
ro
p
u
r
p
o v
o
e
f
t
p
h
e
e
o
s
p
e
le
c
—
ur
w
it
h
y
e
p
t
o
h
s
e
t
r
u
o
re
n e
o f
the software portfolio and all the processes that generate it, so
management skills, risk management perspectives, an ability to
contribute to engineering value streams, and an ability to break
silos are critical success factors.
e
ta
rg
SSI M
CY
A
C
T
L
U
E
RING
n fi
e
D
W
r
w
o
h
i
l
t
e
i
h
l
s
e
i n
s
p
u
e
o
c
n
s
h
g
s
i
e
a
n
s
s
e
s
e
p
in
r
r
i
o
g
n
d
g
f
u
u
t
c
n
e
t
c
a
s
t
m
i
e
o
s
c
n
,
u
a
w
r
l
i
e
t
t
y
i t
s
l
e
e
e
n
s
e
g
s
i
i
n
n
u
d
e
c
i
e
h
v
r
i d
a
o
s
u
r
a
S
s
l
e
s
it
c
e
t
u
a
R
r
k
i
e
i
t
n
l
y
i
g
a
a
b
o
r
i
c
n
li
h
t
l
y
i
e
t e
E
a
c
d
n
t
g
e
,
r
in
s
e
h
e
ip
r,
e e
tn DevOps Engineer, or similar. Their responsibilities often include
I
comparison and selection of security tools, definition of secure
design guidelines and acceptable remediation actions, and
Emerging SSI
P ilot
i
d
m
el
p
iv
le
e
m
ry
e
, a
n
n
ta
d
t i
o
o
p
n
e
o
ra
f
t
i
i
n
o
f
n
ra
s
s
.
t
H
ru
a
c
rm
tu
o
re
n
-
i
a
z
s
in
-c
g
o
l
d
e
e
a d
f
e
o
r
r
s
s
h
e
ip
cu
v
r
i
e
e w
pa
s
c
a
k
c
a
r
g
o
i
s
n
s
g ,
t he
SSG and engineering is a critical step to success.
Build new capability
CHECKLIST FOR MATURING SSIs
Figure 6. MOVING FROM EMERGING TO MATURING. Building an 1. Unify structure and consolidate efforts. Formalize
emerging SSI usually focuses on collecting activities into a single organization, staffing, objectives, budgets, and approach,
e
program. Moving from emerging to maturing requires ongoing iterative
then tell everybody about it.
improvements and expansions. Piloting new capabilities (e.g., security z
champions or software supply chain risk management) likely requires 2. Expand security controls. Increase program impact through i
P
reapplying the emerging approach for a specific set of activities. policy, testing, training, and other quick wins.
m l
3. Engage development. Use security champions to build
bridges and harmonize software security objectives. a
This section on maturing an SSI repeats some of the foundational i
BSIMM activities from the “FOR AN EMERGING SSI” section. We 4. Inventory and select in-scope software. Expand the t n
do this because most organizations won’t treat SSI creation as a
application inventory to include all software, not just
p
applications.
waterfall process. Instead, they will, for example, establish policy,
set up a champions program, deploy defect discovery tools, etc., 5. Enforce security basics everywhere. Use automation to
O
in overlapping, incremental improvement cycles. In addition, many ensure that you run software only on good systems (cloud
organizations will determine in the emerging phase that some or otherwise).
activities can wait a bit while engaging in other, more necessary,
6. Integrate defect discovery and prevention. Use automation
software security efforts. In either case, this is a good place for a
and integration to scale and shift defect discovery and
reminder to keep working on foundational activities.
prevention everywhere.
UNIFY STRUCTURE AND CONSOLIDATE EFFORTS 7. Upgrade incident response. Ensure that software security
experts are involved in all software security events and
The first step is to ensure that there is a single SSI and to provide
improve the program from lessons learned.
the proper resources for the owner tasked with shepherding the
organization so the group can meet risk management objectives. 8. Repeat and improve. Growth does not happen in a straight
At this point, the SSI might include multiple SSGs and owners (e.g., line—you will have to revisit, remeasure, and replan multiple
across major products or business units), so working to harmonize times.
these efforts must be a key goal. The organization will want to
ensure that the SSI is supported by a full-time team—an SSG— that
CYCLE
BSIMM16 26
e a t gr e tn I P i lDonfiee t
BEumiledr gneinwg cSaSpIability SSI MATURING

EXPAND SECURITY CONTROLS SSG can also roll out software security training [T2.9] tailored to
the most common security defects identified through application
Next, it’s time to use existing knowledge to choose the important
security testing (AST), often cataloged by technology stack and
software security activities to initiate, scale, or improve. This
coding language.
knowledge includes SSI scope, compliance, technology stacks,
and deployment models, as well as the issues uncovered in defect
INVENTORY AND SELECT IN-SCOPE SOFTWARE
discovery efforts. Common activity choices are policy [CP1.3],
It’s important to take an enterprise-wide perspective when
SDLC checkpoint conditions [SM1.4], testing [AA1.2, CR1.4, ST1.4,
building a view into the software portfolio. Engaging directly
PT1.3, SR1.5], and training [T1.7], which are typically built out in
with application business owners by, for example, using
a quick-win approach. When choosing and implementing new
questionnaire-style data gathering is a good start. It’s useful
controls, it’s often easier to get buy-in by showing adherence
to focus on applications (with owners who are responsible for
to well-known guidance (e.g., BSIMM, NIST SSDF, regulators)
risk management) as the initial unit of inventory measure, but
or choosing security controls that align with general industry
remember that many vital software components aren’t applications
guidance (e.g., OWASP, CWE, analysts). The organization will want
(e.g., libraries, APIs, scripts, pipeline tests, infrastructure-as-code).
to ensure that activity selection includes an appropriate mix of
In addition to understanding application characteristics (e.g.,
preventive [SR1.1, SFD2.1] and detective (e.g., testing) controls to
programming language, architecture type such as web or mobile,
maximize positive impacts on the organization’s risk posture.
the revenue generated) as a view into risk, you’ll want to capture
and maintain the same information for all software, focusing on
understanding where sensitive data resides and flows (e.g., PII
ESSENTIALLY, THE SSG
inventory) [CP2.1], along with the status of active development
projects.
IS A GROUP OF PEOPLE—
Rather than taking an organizational structure and owner-based
WHETHER ONE PERSON, view, engineering teams usually attempt to understand software
inventory by extracting it from the same tools they use to manage
10, OR 100—WHO MUST their IT assets. They usually combine two or more of the following
approaches to software inventory creation:
IMPROVE THE SECURITY
• Discovery, import, and visualization of assets managed
by the organization’s cloud and data center virtualization
POSTURE OF THE
management consoles
SOFTWARE PORTFOLIO. • Scraping and extracting assets and tags from infrastructure-as-
code held in code repositories, as well as processing metadata
from container and other artifact registries
• Outside-in web and network scanning for publicly discoverable
ENGAGE DEVELOPMENT assets, connectivity to known organizational assets, and
related ownership and administrative information
As noted throughout this section, engineering teams are likely
already thinking about various aspects of security related to With a software inventory in hand, the SSG will impose security
design, configuration, infrastructure, and deployment. Engaging requirements using formalized risk-based approaches to cover as
development begins by creating mutual awareness of how the SSG much of the software portfolio as possible. Using simple criteria
and development teams see the next steps in maturing security (e.g., software size, regulatory constraints, internal- vs. external-
efforts—and successfully engaging early on relies on bridge- facing, data classification), they’ll assign a risk classification (e.g.,
building and credentialing the SSG as competent in development high, medium, low) to each application [AA1.4] and define the initial
culture, toolchains, and technologies. It also includes building set of software and project teams with which to prototype security
awareness around which security capabilities constitute an SSDL activities. Although application risk classifications are often the
and beginning to determine how those capabilities are expected to primary driver, we have observed firms using other information,
be conducted. Building consensus on what role each department such as whether a major change in application architecture is
will play in improving capabilities over the next evolutionary cycle being undertaken (e.g., shift to a cloud-native architecture) or
greatly facilitates success. whether the software contains critical code (e.g., cryptography,
proprietary business logic). Firms find it beneficial to include in the
To facilitate tool adoption, the SSG might dedicate some portion
selection process some engineering teams that are already doing
of their efforts or build a team of security champions [SM2.3]
some security activity organically.
to serve as tool mentors to help development teams not only
integrate the tools but also triage and interpret results [CR1.7].
Although the primary objective is to embed security leadership
inside development, these individuals also serve as both key
points of contact and interface points for the SSG to interact with
engineering teams and monitor progress. Because they are local
to teams, champions can facilitate defect management goals,
such as tracking recurring issues to drive remediation [PT1.2]. The
BSIMM16 27

Engineering teams might have a different idea of what in-scope of security features [SFD1.1]. These controls can take the form of
software means relative to the security efforts they already microservices (e.g., authentication or other identity and access
have underway—if they’re working on one application, then that management) [SE2.5], common product libraries (e.g., encryption)
application is likely to be in their scope. When required to prioritize [SFD2.1], or even infrastructure security controls (e.g., controlling
specific applications’ components, we observe engineering teams scope of access to production secrets through vault technologies).
using the following as input:
Some engineering groups have taken steps to tackle the
• Teams conducting active new development or major prevention of certain classes of vulnerability in a wholesale
refactoring (velocity) manner [CMVM3.1], using development frameworks that preclude
them. Organizations will want to ask security-minded engineers
• Those services or data repositories to which specific
for their opinion about framework choices and empower them to
development or configuration requirements for security or
incorporate their understanding of security features and security
privacy apply [CP1.1, CP1.2] (regulation)
posture tradeoffs.
• Software that solves critical technical challenges or that
adopts key technologies (opportunity) UPGRADE INCIDENT RESPONSE
Prioritized software is then usually the target for test automation Ensuring that defined incident response processes include SSG
[ST2.5], vulnerability discovery tooling, or security features [SFD1.1]. representation [CMVM1.1] and determining whether an incident
has software security roots requires specific skills that are not
ENFORCE SECURITY BASICS EVERYWHERE
often found in traditional IT groups. The organization will want to
Commonly observed today regardless of SSG age are basic security work with engineering teams, especially DevOps engineers, to help
controls enforced in hosts and networks [SE1.2] and in cloud make the connections between those events and alerts raised in
environments [SE1.3]. A common strength for organizations that production and the associated artifacts, pipelines, repositories,
have good controls over the infrastructure assets they manage, and responsible teams. This traceability allows these groups to
these basics are accomplished through a combination of IT effectively prioritize security issues on which the SSG will focus.
provisioning controls, written policy, prebuilt and tested golden Feedback from the field on what is happening greatly enhances the
images, sensors and monitoring capabilities, server hardening and top N lists ([AM3.5, CR2.7]) that many organizations use to help
configuration standards, infrastructure-as-code, and entire groups establish priorities.
dedicated to patching. As firms migrate private infrastructure to
Security engineers who are in development teams and more
cloud environments, organizations must carefully reestablish their
familiar with application logic might be able to facilitate instructive
assurance-based controls to maintain and verify adherence to
monitoring and logging. They can coordinate with DevOps
security policy. To keep tabs on the growing number of virtual assets
engineers to generate in-application defenses that are tailored
created by engineering groups and their automation, organizations
for business logic and expected behavior, therefore, they are
often must deploy custom solutions [AM2.9] to overcome
likely more effective than, for example, Web Application Firewall
limitations in a cloud provider’s ability to meet desired policy.
(WAF) rules. Introducing such functionality will in turn provide
Governance and engineering teams often cooperate to build richer feedback and allow a more tailored response to application
in enforced security basics for infrastructure and cloud behavior [SE3.3].
environments, leveraging containers [SE2.5], infrastructure-as-code
Organizations deploying cloud-native applications using
[SE1.4], and orchestration [SE2.7]. Over time, these security basics
orchestration might respond to incidents (or to data indicating
expand to include internal development environments, toolchains,
imminent incidents) with an increase in logging, perhaps by
deployment automation, code repositories, and other important
adjusting traffic to the distribution of image types in production.
infrastructure.
Much of this is possible only with embedded security engineers
who are steeped in the business context of a development team
INTEGRATE DEFECT DISCOVERY AND PREVENTION
and have good relationships with that team’s DevOps engineers;
Initial defect discovery efforts tend to be one-off (by using
security champions can also be a good resource for these
centralized commercial tools [CR1.2]) and target the most critical
individuals. Under these circumstances, incident response moves
applications, with a plan to scale efforts over time. Scaling
at the speed of a well-practiced single team [CMVM1.4] rather than
prioritization might be selected for compliance or contractual
that of an interdepartmental playbook.
reasons or because it applies to a phase of the software lifecycle
(e.g., shift everywhere to do threat modeling at design time [AA1.1], REPEAT AND IMPROVE
composition analysis on software repositories [SE3.8], SAST
As noted earlier, working through activity growth for emerging and
during development [CR1.4], DAST in preproduction [ST1.4], and
maturing SSIs probably won’t happen in a straight line—there’ll be
penetration testing on deployed software [PT1.1, PT1.3]). The point
changes in priorities, resources, and responsibilities, along with
is to automate and scale the chosen defect discovery activities,
changes in attackers, attacks, technologies, and everything else.
but scaling through automation and integration must come
It’s necessary to take time periodically to determine how well
without disrupting CI/CD pipelines (e.g., due to tools having long
the SSI is performing against business objectives and adjust as
execution times), without generating large volumes of perceived
necessary.
false positives and without impeding delivery velocity (e.g., through
opaquely breaking builds or denying software promotion), except As a reminder, organizations rarely move their entire SSI from
under clear or agreed-upon circumstances. emerging to maturing to enabling all at once. Different parts of
the SSI will shift between emerging, maturing, and enabling a few
In addition to defect discovery, engineering teams might favor
times over the years, with different timing that SSG leaders will
prevention controls they can apply to software directly in the form
need to plan for.
BSIMM16 28

FOR AN ENABLING SSI: DATA-DRIVEN ACHIEVING SOFTWARE
IMPROVEMENTS
SECURITY SCALE—
Achieving software security scale—of expertise, portfolio coverage,
tool integration, vulnerability discovery accuracy, process
OF EXPERTISE,
consistency, etc.—remains a top priority. However, firms often
scale one or two capabilities (e.g., defect discovery, training) PORTFOLIO COVERAGE,
and fail to scale others (e.g., architecture analysis [AA], vendor
management). Given mature activities, there’s a treasure trove TOOL INTEGRATION,
of data to be harvested and included in KPI and KRI reporting
dashboards, but executives will start asking the very difficult VULNERABILITY DISCOVERY
questions: Are we getting better? Is our implementation working
well? Where are we lagging? How can we go faster with less ACCURACY, PROCESS
overhead? What’s our message to the board? The efficacy of an
CONSISTENCY, ETC.—
SSI will be supported by ongoing data collection and metrics
reporting that seeks to answer such questions [SM3.3].
REMAINS A TOP PRIORITY.
PROGRESS ISN’T A STRAIGHT LINE
As mentioned earlier, organizations don’t always progress from
emerging to maturing to enabling in one try or on a straight path,
PUSH FOR AGILE-FRIENDLY SSIs
some SSI capabilities might be enabling while others are still
In recent years, we’ve observed governance-oriented teams—often
emerging or maturing. Based on our experience, firms with some
out of necessity, to remain in sync with engineering teams—
portion of their SSI operating in an enabling state have likely been
evolving to become more Agile-friendly:
in existence for longer than three years. Although we don’t have
enough data to generalize enabling SSIs, we do see common • Putting “Sec” in DevOps is becoming a mission-critical
themes for those that strive to reach this state: objective. SSG leadership routinely partners with IT, cloud,
development, QA, and operations leadership to ensure that the
• Top N risk reduction. Everyone relentlessly identifies and
SSI mission aligns with DevOps values and principles.
closes top N weaknesses, placing emphasis on obtaining
visibility into all sources of vulnerability, whether in-house • SSG leaders realize they need in-house talent with coding
developed code, open source code [SR2.7], vendor code expertise to improve not only their credibility with engineering
[SR3.2], toolchains, or any associated environments and but also their understanding of modern software delivery
processes [SE1.2, SE1.3]. These top N weaknesses are most practices. Job descriptions for SSG roles now mention
useful when specific to the organization, evaluated at least experience and qualification requirements such as cloud,
annually, and tied to metrics to prioritize SSI efforts that mobile, containers, and orchestration security, as well
improve risk posture. as coding. We expect this list to grow as other topics
become more mainstream, such as architecture and testing
• Tool customization. Security leaders place a concerted
requirements around serverless computing and single-page
effort on tuning tools (e.g., customization for static analysis,
application approaches.
fuzzing, penetration testing) to improve integration, accuracy,
consistency, and depth of analysis [CR2.6, ST2.6, AM3.2, • To align better with DevOps values (e.g., agility, collaboration,
PT3.2]. Customization focuses not only on improving result responsiveness), SSG leaders are beginning to replace
fidelity and applicability across the portfolio but also on traditional people-driven activities with people-optional,
pipeline integration and timely execution, improving ease of pipeline-driven automated tasks. This often comes in the form
use for everyone. of automated security tool execution, bugs filed automatically
to defect notification channels, builds flagged for critical
• Feedback loops. Loops are created between SSDL activities
issues, and automated triggers to respond to real-time
to improve effectiveness as deliverables from activities ebb
operational events.
and flow with each other. For example, an expert in QA might
leverage AA results when creating security test cases [ST3.3]. • Scaling outreach and expertise through the implementation
Likewise, feedback from the field might be used to drive SSDL of an ever-growing security champions program is viewed as
improvement through enhancements to a hardening standard a short-term rather than long-term goal. Organizations report
[CMVM3.2]. The concept of routinely conducting blameless improved responsiveness and engagement as part of DevOps
postmortems to find root causes and drive remediation seems initiatives when they’ve localized security expertise in the
to be gaining ground in some firms. engineering teams. Champions are also becoming increasingly
sophisticated in building reusable artifacts (e.g., security
• Data-driven governance. The more mature groups instrument
sensors) in development and deployment streams to directly
everything to collect data that in turn becomes metrics for
support SSI activities.
measuring SSI efficiency and effectiveness against KRIs and
KPIs [SM3.3]. As an example, a metric such as defect density • SSG leaders are partnering with operations to implement
might be leveraged to track performance of individual business application-layer production monitoring and automated
units and application teams. Metrics choices are very specific mechanisms for responding to security events. There is a high
to each organization and also evolve over time. degree of interest in consuming real-time security events for
data collection and analysis to produce useful metrics.
BSIMM16 29

In summary, engineering teams have likely taken an enabling
approach from the beginning. Their security efforts are
contributions from engineers who deliver software early and
often, constantly improving it rather than relying on explicit
strategy backed by top-down policies. They make their software
available to everyone to prevent future issues and use evangelism
to encourage uptake. They review production failures and make
changes, often with automation, to their toolchains and processes.
That said, perceptions of business and technical risk between
corporate and engineering groups often differ in substantial
ways. Bringing the groups together to share responsibilities for
software security, as well as definitions of and goals for needed
risk management, while enabling broad stakeholder productivity is
a primary goal for any SSI.
BSIMM16 30

PART 4:
| B S | I M | M   |      |     |     |
| --- | --- | --- | ---- | --- | --- |
| PA  | RT  | I C | I PA | NT  | S   |

PART 4: BSIMM PARTICIPANTS pandemic and post-pandemic eras are still being seen as the large
pre-pandemic numbers age out of the report, while the leaner
post-pandemic numbers have yet to do so.
BSIMM participants comprise software security leaders and
team members from around the globe. They have a common PARTICIPANTS
mission to continuously improve their SSIs in light of changes The participating organizations fall across various verticals,
in the world around them. You can use the information they’ve including Cloud, Financial Services, FinTech, ISVs, Insurance, IoT,
provided to learn from their efforts. Healthcare, and Technology organizations (see Figure 7).
Unique in the software security industry, the BSIMM project has
This 2026 edition of the BSIMM report—BSIMM16—examines
grown from nine participating companies in 2008 to 111 in 2026,
anonymized data from the software security activities of 111
currently with about 3,700 software security group members
organizations. This diverse group spans multiple sizes of security
and almost 6,500 security champions. Today, the average age of
teams, development teams, and software portfolios, as well
participants’ SSIs is 5.6 years (see Table 5).
as regions, vertical markets, and security team ages. While
the numbers are smaller than in years past, the effects of the
5%
11% 4%
16%
4%
8%
18%
17%
14%
4%
3%
71% 25%
ISV Financial FinTech Tech Telecom
EMEA APAC North America
Cloud IoT Healthcare Insurance Other
Figure 7. BSIMM16 PARTICIPANTS. Participant percentages per tracked region and vertical.
BSIMM PARTICIPANT NUMBERS OVER TIME
BSIMM16 BSIMM15 BSIMM14 BSIMM13 BSIMM12 BSIMM11 BSIMM10 BSIMM1
FIRMS 111 121 130 130 128 130 122 9
SSG MEMBERS 3,722 3,428 3,527 3,342 2,837 1,801 1,596 370
SECURITY
6,498 7,703 7,427 8,508 6,448 6,656 6,298 710
CHAMPIONS
DEVELOPERS 226,247 259,326 267,731 408,999 398,544 490,167 468,500 67,950
APPLICATIONS 91,073 90,747 96,361 145,303 153,519 176,269 173,233 3,970
AVG. SSG AGE
5.62 5.44 5.24 5 4.41 4.32 4.53 5.32
(YEARS)
SSG
MEMBERS TO 5.63 / 100 4.4 / 100 3.87 / 100 3.01 / 100 2.59 / 100 2.01 / 100 1.37 / 100 1.13 / 100
DEVELOPERS
Table 5. BSIMM PARTICIPANT NUMBERS OVER TIME. The chart shows how the BSIMM study has changed over the years.
BSIMM16 32

ACKNOWLEDGEMENTS Zhao, Manik Virmani, Matt Chartrand, Melih Tas, Mike Fabian, Mike
Lyman, Nivedita Murthy, Rajiv Harish, Ravinder Reddy Amireddy,
Our thanks to the 111 executives, including those who wish to
Rehan Bashir, Sachin Shetty, Sam Schueller, Satish Swargam,
remain anonymous, from the SSIs we studied to create BSIMM16. Smith Kaneria, Stanislav Sivak, Stephen Gardner, Surya Uddhi
Nagaraj, Takeshi Ohmori, Thaddeus Bender, Thomas Madden, Tom
Our thanks also to the nearly 170 individuals who helped gather
the data for the BSIMM data pool over time. Stripling, Tony Blakemore, Uzear Ahmed, Vijay Sharma, Viplove
Jain, and Yasuhito Mori.
In particular, we thank Adam Brown, Aditi Gupta, Akhil Mittal,
We also thank David Johansson and Surya Uddhi Nagaraj for their
Akira Watanabe, Akshay Sawant, Alex Jupp, Alistair Nash, Anders
Stadum, Anil Gajawada, Aseem Lodha, Avi Sambira, Balaji  work managing the BSIMM tooling and data and for creating the
Padmanabhan, Ben Hutchison, Berta Rae, Bohuai Liu, Brendan  extracts used in this report. In addition, we thank Jennifer Stout
and Amy La Russa for their work on various aspects of this report.
Sheairs, Carlos Almeyda, Cem Nisanoglu, David Johansson,
Denis Sheridan, Derek Evans, Devaraj Munuswamy, Diya Ghosh,  BSIMM16 was authored by Jamie Boote, Ben Hutchison, Mike
Don Pollicino, Durai G, Eason Yu, Eli Erlikhman, Faheem Sultan,
Lyman, and Sam Schueller. Special thanks to Sammy Migues,
Grant Van Gorder, Iman Louis, Jacob Ewers, Jamie Boote, Jas  whose influences and words still exist throughout this document.
Alsuwailem, Jatin Virmani, John Tapp, Josh Brown, Kevin Nassery,
Kris Balarama, Lahiru Pinnaduwage, Lekshmi Nair, Leo Berrun, Li
| Airoha           | Intralinks        | QlikTech            |
| ---------------- | ----------------- | ------------------- |
| AON              | International AB  | Realtek             |
| Arlo             | iPipeline         | Reckitt             |
| Axway            | Johnson & Johnson | Sammons Financial   |
| Bell Network     | Landis+Gyr        | ServiceNow          |
| CIBC             | Lenovo            | SonicWall           |
| Citi             | MassMutual        | Synchrony Financial |
| Egis Technology  | MediaTek          | TD Ameritrade       |
| EQ Bank          | Medtronic         | Teradata            |
| Fidelity         | MiTAC             | U.S. Bank Unisoc    |
| Genetec          | Navient           | Vanguard            |
| HCA Healthcare   | NetApp            | Veritas             |
| Honeywell        | Oppo              | Vivo                |
| HUMAN Security   | Pegasystems       | ZoomInfo            |
| Inspur Software  | Phison            |                     |
THIS WORK IS LICENSED UNDER THE CREATIVE COMMONS Attribution-Share Alike 3.0 License. To view a copy of this license, visit http://creative-
commons.org/ licenses/by-sa/3.0/legalcode or send a letter to Creative Commons, 171 Second Street, Suite 300, San Francisco, California, 94105, USA.
BSIMM16 33

PART 5:
| Q U | I C | K G | U   | I D E TO  |     |
| --- | --- | --- | --- | --------- | --- |
| S S | I M | AT  | U   | R IT      | Y   |

PART 5: QUICK GUIDE TO SSI SHIFTING SECURITY EFFORTS EVERYWHERE IN THE
ENGINEERING LIFECYCLE
MATURITY
• Are you automating security decisions to remove time-
consuming manual review and moving toward a secure,
Twelve questions can help clarify where your SSI is today. auditable, governance-as-code-driven SDLC?
Combined with a detailed software security scorecard (see • Are you following a shift everywhere strategy to move from
below on how to measure your own program) and knowledge large, time-consuming security tests to smaller, faster, timelier,
about roles and responsibilities, you can use this information to pipeline-driven security tests conducted to improve engineering
plan strategic changes for your organization’s ongoing success. team performance?
• Are you managing supply chain risk through vendor software
assurance, governance-driven access and usage controls,
SSI maturity is a complex thing. Each organization will apply
maintenance standards, and collected provenance data?
different values to efforts and progress in people, process,
technology, and culture, but they will also evolve differently in their MEASURING YOUR SSI
vision for success as well as how they spend resources, grow the
• Do you routinely use telemetry from security testing, operations
program, and manage risk. This section provides an approach to
events, risk management processes, event postmortems, and
organizing, growing, and maturing an SSI that works for everyone.
other efforts to drive process and automation improvements
Refer to Part 3 for more details.
in your DevOps toolchain or governance improvements in your
policies and standards?
A BASELINE FOR SSI LEADERS
All program leaders require a detailed understanding of their • Does your SSI strategy include security efforts needed
efforts and whether those efforts align with business objectives. specifically for modern technologies, such as cloud, container,
A good start here is to understand whether organizational SSI orchestration, open source management, development pipeline,
efforts align well with changes in the software security landscape etc.?
driven by global events, digital transformation, and engineering • Are you actively experimenting with new technologies, such as
evolution, as well as with how software is made today. Use your AI and LLMs, that have the opportunity to integrate security and
answers to the questions below to determine whether it’s time engineering functions while also reducing engineering friction?
to invest in new growth—and if you don’t know all these answers,
Most organizations have already covered the basics of software
use the list to gather information from each SSI stakeholder
security policy, testing, and outreach, but it takes a concerted
responsible for aspects of software security risk management in
effort to scale an SSI to address changes in portfolio size,
your organization.
technology, infrastructure, regulation, laws, attackers, attacks, and
KEEPING PACE WITH CHANGE IN YOUR SOFTWARE more. Internal review of efforts vs. needs is always a good way to
move forward.
PORTFOLIO
• Do you maintain at least a near-current view of all your USING A BSIMM SCORECARD TO MAKE
software and development assets, including internal code,
PROGRESS
third-party code, open source, development environments and
A BSIMM scorecard is a management tool that allows your SSI and
toolchains, infrastructure-as-code, and other software assets?
SSG leadership to:
• Are you creating and using in your risk management processes
• Assess your level of maturity so you can evolve your software
SBOMs that detail all the components in the SSI’s software
security journey in stages, first building a strong emerging
portfolio?
foundation, then scaling and maturing the more complex
• Do you have a near-real-time view of your operations
activities over time
environments, along with a view into their aggregate attack
• Communicate your software security posture to customers,
surface and aggregate risk?
partners, executives, and regulators (a scorecard helps
CREATING THE DEVSECOPS CULTURE YOU NEED everyone understand where you are and where you want to go
in your journey when you’re explaining your strategic plan and
• Are you building bridges between the various software security
budgets)
stakeholders in your organization—governance, technical, audit,
vendor management, cloud, etc.—to align culture, approach, • See actual measurement data from the field, which helps in
technology stacks, and testing strategies? building a long-term plan for an SSI and in tracking progress
against that plan
• Have you scaled your security champions program across
your software portfolio, including skills specific to automation, In addition to being a lens on the state of software security, the
technology stacks, application architectures, cloud-native BSIMM scorecard serves as a measuring stick to determine where
development, and other important DevOps needs? your SSI currently stands relative to our participants, whether as a
• Are you delivering important security policy, standards, and whole or for specific verticals. A direct comparison of your efforts
guidelines as-code that run in engineering and operations to the BSIMM16 scorecard for the entire data pool (see Part 7)
toolchains? is probably the best first step. Follow the steps below to use the
BSIMM to create your own SSI scorecard (see Figure 8 for an
example).
BSIMM16 35

UNDERSTAND YOUR ORGANIZATIONAL For most organizations, a single aggregated scorecard covering
MANDATE the entire SSI will suffice to inform future planning. In some cases,
however, it will be beneficial to create individual scorecards for the
• Decide what the SSI is expected to accomplish. Who are the
SSG and for business units or application teams that have varying
executive sponsors, and what resources are they expected to
software security approaches or maturity levels.
provide? From a RACI perspective, who are the responsible and
accountable stakeholders? What metrics must be provided to Figure 8 depicts an example firm that performs 41 BSIMM16
executive management to demonstrate acceptable progress? activities (noted as 1s in its EXAMPLEFIRM scorecard columns,
e.g., SM1.1), including nine activities that are the most common in
• Set the proper scope for the SSI. At a high level, describe the
their respective practices (orange boxes, e.g., CP1.2). Note the firm
applicable software portfolio and the associated software
does not perform the most observed activities in the other three
ownership (e.g., risk managers). Ensure that you include all
practices (gray boxes, e.g., SM1.4) and should take some time
applications and related software in the SSG’s remit.
to determine whether these are necessary or useful to its overall
BUILD THE SCORECARD SSI. For example, [SM1.4] Implement security checkpoints and
associated governance might be critical for the organization, while
• Make a list of stakeholders to interview. No single person
[PT1.1] Use external penetration testers to find problems is being
knows everything about a modern SSI, so ensure that you
accomplished in-house; for [PT1.3] Use penetration testing tools
have broad coverage across the SSG, security champions,
internally, the company may decide external penetration testers
engineering, QA, operations, and security testing. As needed,
are not a priority at this time. The BSIMM16 FIRMS columns show
extend the stakeholder list to include teams from reliability,
the number of observations (currently out of 111) for each activity,
cloud, privacy, training, infrastructure, resilience, AI/ML, and
allowing the firm to understand the activity’s general popularity
others whose efforts have a direct impact on software security.
within the current data pool. If you want to evaluate your scorecard
• Understand the BSIMM. Review the BSIMM activities and gain
against a particular vertical, refer to Part 9.
an understanding of the practices, the individual activities, and
Once you have determined where you stand with activity efforts
the connected themes that run through them. For example, the
compared to your expectations, you can devise a plan for
activities for software security testing appear across multiple
improvement. Organizations almost always choose some hybrid of
BSIMM practices.
expanding their SSI with new activities and scaling some existing
• Interview everyone and consolidate the results. Keep interviews
activities across more of the software portfolio and stakeholder
brief and focused on the intersection of the interviewee’s role
teams.
and specific BSIMM activities. Ensure that you get the data and
artifacts that demonstrate the organization is sufficiently—in Note that there’s no inherent reason to adopt all activities in
both depth and breadth—performing each activity before you each practice. Prioritize the ones that make sense for your
award credit. organization today and set aside those that don’t—but revisit those
choices periodically. Once they’ve adopted an activity set, most
• Create your scorecard. Use a binary 1 or 0, a scale of low,
organizations strategically work on the depth, breadth, and cost-
medium, and high, or even a graduated scale such as a
effectiveness (e.g., via automation) of each activity in accordance
percentage to combine aspects of depth, breadth, and maturity.
with their view of the risk management efforts required in their
environments for their business objectives.
MAKE A STRATEGIC PLAN AND EXECUTE
• Compare your scorecard first to your stakeholders’ realistic To help refine the current and future activity prioritization for your
expectations and then also to what’s common in the data SSI, you can go beyond the BSIMM16 FIRMS data in Part 7 to
pool. Prioritize effort on the important gaps as well as those Figure 18 and analyze how SSIs evolve with remeasurements (see
gaps with a long lead time. See Part 3 for more details on how DATA ANALYSIS: LONGITUDINAL in Part 9) and with age (see DATA
to build an execution plan. Mark your calendar to revisit the ANALYSIS: SSG in Part 9). You can also examine what’s different
scorecard in 12 to 18 months, document your progress, and about your vertical or verticals (see DATA ANALYSIS: VERTICALS
create a new scorecard. AND PRACTICES in Part 9) and understand the impact of a
champions program (see DATA ANALYSIS: SECURITY CHAMPIONS
• Define and use metrics to gauge progress. Every program
in Part 9) on SSIs.
needs a barometer for success, and each organization finds
different things to be the best indicators for them. Whether
described as metrics, KPIs, KRIs, SLOs, or something else, use
what works best for you, your executive team, and your board
(with each likely needing different metrics).
BSIMM16 36

| GOVERNANCE |          |          | INTELLIGENCE |          |          | SSDL TOUCHPOINTS |          |          | DEPLOYMENT |          |          |
| ---------- | -------- | -------- | ------------ | -------- | -------- | ---------------- | -------- | -------- | ---------- | -------- | -------- |
|            | BSIMM16  |          |              | BSIMM16  |          |                  | BSIMM16  |          |            | BSIMM16  |          |
|            |          | EXAMPLE  |              |          | EXAMPLE  |                  |          | EXAMPLE  |            |          | EXAMPLE  |
ACTIVITY FIRMS (OUT  ACTIVITY FIRMS (OUT  ACTIVITY FIRMS (OUT  ACTIVITY FIRMS (OUT
|     | OF 111) | FIRM |     | OF 111) | FIRM |     | OF 111) | FIRM |     | OF 111) | FIRM |
| --- | ------- | ---- | --- | ------- | ---- | --- | ------- | ---- | --- | ------- | ---- |
STRATEGY & METRICS ATTACK MODELS ARCHITECTURE ANALYSIS PENETRATION TESTING
| [SM1.1]             | 84       | 1   | [AM1.2]             | 57       |     | [AA1.1]          | 89  | 1   | [PT1.1]         | 95         |     |
| ------------------- | -------- | --- | ------------------- | -------- | --- | ---------------- | --- | --- | --------------- | ---------- | --- |
| [SM1.3]             | 66       |     | [AM1.3]             | 44       | 1   | [AA1.2]          | 51  | 1   | [PT1.2]         | 87         | 1   |
| [SM1.4]             | 100      |     | [AM1.5]             | 78       |     | [AA1.4]          | 57  |     | [PT1.3]         | 67         | 1   |
| [SM1.7]             | 71       |     | [AM2.1]             | 20       |     | [AA2.1]          | 35  |     | [PT2.2]         | 40         |     |
| [SM2.1]             | 54       |     | [AM2.6]             | 16       | 1   | [AA2.2]          | 38  | 1   | [PT2.3]         | 56         |     |
| [SM2.3]             | 55       |     | [AM2.7]             | 18       | 1   | [AA2.4]          | 36  | 1   | [PT3.1]         | 25         | 1   |
| [SM2.6]             | 62       |     | [AM2.8]             | 26       |     | [AA3.1]          | 17  |     | [PT3.2]         | 25         |     |
| [SM2.7]             | 49       | 1   | [AM2.9]             | 22       |     | [AA3.2]          | 7   |     |                 |            |     |
| [SM3.1]             | 31       |     | [AM3.2]             | 5        |     | [AA3.3]          | 14  |     |                 |            |     |
| [SM3.2]             | 25       |     | [AM3.4]             | 9        |     |                  |     |     |                 |            |     |
| [SM3.3]             | 30       |     | [AM3.5]             | 12       |     |                  |     |     |                 |            |     |
| [SM3.4]             | 9        |     |                     |          |     |                  |     |     |                 |            |     |
| [SM3.5]             | 5        |     |                     |          |     |                  |     |     |                 |            |     |
|                     |          |     | SECURITY FEATURES   |          |     |                  |     |     |                 | SOFTWARE   |     |
| COMPLIANCE & POLICY |          |     |                     |          |     | CODE REVIEW      |     |     |                 |            |     |
|                     |          |     |                     | & DESIGN |     |                  |     |     | ENVIRONMENT     |            |     |
| [CP1.1]             | 88       | 1   | [SFD1.1]            | 85       | 1   | [CR1.2]          | 75  | 1   | [SE1.1]         | 73         |     |
| [CP1.2]             | 94       | 1   | [SFD1.2]            | 77       | 1   | [CR1.4]          | 95  | 1   | [SE1.2]         | 96         | 1   |
| [CP1.3]             | 92       | 1   | [SFD2.1]            | 44       |     | [CR1.5]          | 74  |     | [SE1.3]         | 79         | 1   |
| [CP2.1]             | 46       |     | [SFD2.2]            | 62       |     | [CR1.7]          | 47  |     | [SE1.4]         | 69         | 1   |
| [CP2.2]             | 56       |     | [SFD3.1]            | 16       |     | [CR2.6]          | 29  | 1   | [SE2.4]         | 52         |     |
| [CP2.3]             | 63       |     | [SFD3.2]            | 22       |     | [CR2.7]          | 19  |     | [SE2.5]         | 59         | 1   |
| [CP2.4]             | 61       |     | [SFD3.3]            | 11       |     | [CR2.8]          | 28  | 1   | [SE2.7]         | 40         | 1   |
| [CP2.5]             | 68       | 1   |                     |          |     | [CR3.2]          | 18  |     | [SE3.2]         | 25         |     |
| [CP3.1]             | 40       |     |                     |          |     | [CR3.3]          | 8   |     | [SE3.3]         | 22         |     |
| [CP3.2]             | 41       |     |                     |          |     | [CR3.4]          | 3   |     | [SE3.6]         | 31         |     |
| [CP3.3]             | 15       |     |                     |          |     | [CR3.5]          | 4   |     | [SE3.8]         | 8          |     |
|                     |          |     |                     |          |     |                  |     |     | [SE3.9]         | 13         |     |
|                     |          |     |                     |          |     |                  |     |     | [SE3.10]        | 6          |     |
|                     |          |     | STANDARDS &         |          |     |                  |     |     | CONFIG. MGMT.   |            |     |
|                     | TRAINING |     |                     |          |     | SECURITY TESTING |     |     |                 |            |     |
|                     |          |     | REQUIREMENTS        |          |     |                  |     |     | & VULN. MGMT.   |            |     |
| [T1.1]              | 61       | 1   | [SR1.1]             | 82       | 1   | [ST1.1]          | 93  | 1   | [CMVM1.1]       | 106        | 1   |
| [T1.7]              | 61       | 1   | [SR1.2]             | 88       | 1   | [ST1.3]          | 66  | 1   | [CMVM1.2]       | 76         |     |
| [T1.8]              | 52       |     | [SR1.3]             | 77       |     | [ST1.4]          | 47  |     | [CMVM1.3]       | 82         | 1   |
| [T2.5]              | 30       |     | [SR1.5]             | 88       | 1   | [ST2.4]          | 20  |     | [CMVM1.4]       | 86         |     |
| [T2.8]              | 25       | 1   | [SR2.2]             | 65       |     | [ST2.5]          | 30  |     | [CMVM2.3]       | 38         |     |
| [T2.9]              | 30       | 1   | [SR2.5]             | 62       | 1   | [ST2.6]          | 28  |     | [CMVM2.4]       | 53         |     |
| [T2.10]             | 21       |     | [SR2.7]             | 53       |     | [ST3.3]          | 15  |     | [CMVM3.1]       | 16         |     |
| [T2.11]             | 30       |     | [SR3.2]             | 17       |     | [ST3.4]          | 6   |     | [CMVM3.2]       | 27         |     |
| [T2.12]             | 45       |     | [SR3.3]             | 19       |     | [ST3.5]          | 9   |     | [CMVM3.3]       | 29         | 1   |
| [T3.1]              | 8        |     | [SR3.4]             | 26       |     | [ST3.6]          | 10  |     | [CMVM3.4]       | 34         | 1   |
| [T3.2]              | 21       |     | [SR3.5]             | 2        |     |                  |     |     | [CMVM3.5]       | 24         |     |
| [T3.6]              | 8        |     |                     |          |     |                  |     |     | [CMVM3.6]       | 5          |     |
|                     |          |     |                     |          |     |                  |     |     | [CMVM3.8]       | 3          |     |
Figure 8. BSIMM16 EXAMPLEFIRM SCORECARD. A scorecard helps everyone understand the software security efforts that are currently underway. It also helps
organizations make comparisons to participants and serves as a guide on where to focus next. By highlighting the most common activities (orange rows) and
where a firm is not doing the most common activities (gray-colored cells), the scorecard quickly shows what might be critical gaps in a firm’s program.
| BSIMM16 |     |     |     |     |     |     |     |     |     |     | 37  |
| ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

PART 6:
| S O  | F   | T   | WA  |     | R   | E    |
| ---- | --- | --- | --- | --- | --- | ---- |
| S E  | C   | U   | R   | IT  | Y   |      |
| I N  | IT  | I   | AT  | I   | V   | E    |
| BY T |     | H   | E   |     |     |      |
| N    | U M |     | B E | R   | S   |      |

PART 6: SOFTWARE SECURITY EXECUTIVE LEADERSHIP
INITIATIVE BY THE NUMBERS
Historically, security initiatives that achieve firm-wide impact
are sponsored by a senior executive who creates an SSG where
ROLES IN A SOFTWARE SECURITY software security governance and testing are distinctly separate
from software delivery (even when the groups have many shared
INITIATIVE
responsibilities). Security initiatives without that executive
sponsorship, by comparison, have historically had little lasting
An SSI requires thoughtful staffing with both full-time and impact across the firm. By identifying a senior executive and
dotted-line people. You can use the descriptions below to help putting them in charge of software security, the organization can
define roles and responsibilities that accommodate your needs address two “Management 101” concerns: accountability and
for execution and growth. empowerment.
In BSIMM-V, we saw CISOs as the nearest executive in 21 of 67
firms, which grew in BSIMM6 to 31 of 78, and again for BSIMM7
with 52 of 95. Since then, the percentage remained relatively flat,
even as BSIMM participation grew until this year, when there was a
significant drop, as shown in Figure 9.
60%
50%
40%
30%
20%
10%
0
BSI M M B V SI M M B 6 SI M M B 7 SI M M B 8 SI M M BS 9 I M M BS 10 I M M BS 1 I 1 M M B 1 S 2 I M M B 1 S 3 I M M B 1 S 4 I M M BS 15 I M M16
Figure 9. PERCENTAGE OF SSGs WITH A CISO AS THEIR NEAREST EXECUTIVE. Assuming new CISOs generally receive responsibilities for SSIs, this
data suggests that CISO role creation is also flattening or even declining, as this year’s data shows.
60%
50%
40%
30%
20%
10%
0%
CISO CTO CSO CIO COO CFO CRO CPO
BSIMM13 BSIMM14 BSIMM15 BSIMM16
Figure 10. NEAREST EXECUTIVE TO SSG. Although many SSGs have a CISO as their nearest executive, we see a variety of executives overseeing
software security efforts in the 111 BSIMM16 firms.
BSIMM16 39

If we look across all the executives nearest to SSG owners, not just SOFTWARE SECURITY GROUP
CISOs, we observe a large spread in the reporting path to executive
LEADERS
leadership for BSIMM12 through BSIMM16, as shown in Figure 10.
SSG leaders are individuals in charge of the day-to-day security
The dark purple columns show by percentage the closest SSG
efforts in the 111 SSIs we studied for BSIMM16, and they have a
leaders, while the other columns show the percentages for
variety of titles:
previous BSIMMs. For example, a CISO is the closest executive
in 49% of organizations (54 of 111) in the BSIMM16 data pool, • Product Security Lead
and that percentage ranged from 50% to 58% in BSIMM7 through
• Lead Security Architect
BSIMM15. Starting with the BSIMM13 data pool, we no longer see
SSGs reporting directly to CAO (assurance), CPO (privacy), and • SSG Chair
General Counsel roles and only rarely to CRO (risk) (1 out of 111 • Director Application Security Engineering
firms). Note that for BSIMM16, we added 16 firms and removed 26
• Director Application Security
others, which also affects analysis of reporting chains. Of course,
• Principal Security Architect
across various organizations, not all people with the same title
perform, prioritize, enforce, or otherwise provide resources for the • VP Security Compliance
same efforts in the same way.
• VP, Product Security
CISOs, in turn, report to different executives among the 111 • AVP Software Security Strategy Team
BSIMM16 firms. Figure 11 shows that CISOs report most
• Primary Security Officer
commonly to CIOs (18 of 54, or almost 33% of the time) and report
directly to the CEO about 22% of the time (12 of 54). • Director of Product Security (SSG Lead)
• Managing Director, SSG Lead
BOARD
2% • Cybersecurity Advisor
CFO
• Manager, Software Development, and Head of Product Security
COO
• Security Engineering Manager
4%
CIO • App Sec Lead
CRO
6%
• Application Security and Vulnerability Management Manager
4%
• Director Software Security
CSO
33%
• Director SSG
6%
• Application Security Director
• Product Security Manager
10% • Head of AppSec
• Chief Product Security Officer (VP)
TECH
When the SSG leader is an executive themselves, which happens
14% of the time (15 out of 111), they are CISOs almost 40% of the
10%
time (6 out of 15), with other titles being CTO, CPSO (Chief Product
Security Officer), and CSO. As shown in Figure 12, SSG leaders are
CTO 22% typically one or two hops from their nearest executive (e.g., a CxO
CEO or related technology organization title). In addition, we observed
that this nearest executive is usually a further two hops away from
the CEO.
CIO CEO CTO Tech CSO
CRO COO CFO Board
Figure 11. TO WHOM THE CISO REPORTS. For BSIMM16 participants,
the CISO reports to a variety of roles, with the most common being
the CIO, CTO, and a technology executive (e.g., head of engineering,
architecture, or software).
1.2 hops 1.9 hops
Figure 12. SSG LEADERSHIP REPORTING CHAINS. SSG leaders are
typically three or four hops away from the CEO.
BSIMM16 40

THE SSG ITSELF  Although no two of the 111 firms we examined had exactly the
same SSG structure, we did observe some commonalities. At the
Each of the 111 initiatives in BSIMM16 has an SSG—an
highest level, SSGs seem to come in five overlapping structures:
organizational group or person dedicated to software security. In
•  Organized to provide software security services
fact, without an SSG, successfully carrying out BSIMM activities
across a software portfolio is very unlikely, so the creation of  •  Organized around setting and verifying adherence to policy
such a group is a crucial first step. The SSG might start as a team  •  Designed to mirror business unit organizations
of one—just the SSG leader—and expand over time. The SSG
•  Organized with a hybrid policy and services approach
might be entirely a corporate team, entirely an engineering team,
•  Structured around managing a matrixed team of experts doing
or an appropriate hybrid. The team’s name might also have an
software security work across the development or engineering
appropriate organizational focus, such as application security
group or product security group, or perhaps DevSecOps. organizations
Some SSGs are highly distributed across a firm whereas others are  Table 6 shows SSG-related statistics across the 111 BSIMM16
firms, but note that large outliers affect the numbers this year. The
centralized. Even within the most distributed organizations, we find
that software security activities are almost always coordinated by  “Notes” column shows the effect of removing outliers, or the top
an SSG. 10 firms, for that SSG characteristic. When planning the size and
structure of your own SSG, consider the number of developers and
applications to determine what resources you need to scale the
SSI. Refer to DATA ANALYSIS: SSG in Part 9 for more details on
how SSGs evolve over time.
THE SOFTWARE SECURITY GROUP
| STATISTICS           | AVERAGE | MEDIAN | LARGEST | SMALLEST                              | NOTES |
| -------------------- | ------- | ------ | ------- | ------------------------------------- | ----- |
| SSG Size             | 33.5    | 10     | 892     | 1 Average drops to 25.7 (one outlier) |       |
| Number of Developers | 2,038.3 | 650    | 30,000  | 1                                     |       |
Average drops to 691.6 (one
| Number of Applications | 820.5 | 100 | 15,000 | 1   |     |
| ---------------------- | ----- | --- | ------ | --- | --- |
outlier)
| SSG Age | 5.6 | 4.5 | 23  | 0.1 |     |
| ------- | --- | --- | --- | --- | --- |
SSG Members-to-Developer Ratio (per  Average drops to 4.8 (one outlier)
|     | 5.6 | 1.8 | 100 | 0.02 |     |
| --- | --- | --- | --- | ---- | --- |
100 Developers)
SSG-to-Developer Ratio (650+
|     | 1.79 | 1.13 | 14.87 | 0.02 |     |
| --- | ---- | ---- | ----- | ---- | --- |
Developers) - 56 Firms
SSG-to-Developer Ratio (less than 650
|     | 9.54 | 3.33 | 100 | 0.33 |     |
| --- | ---- | ---- | --- | ---- | --- |
Developers) - 55 Firms
SSG Members to Applications 2.5 0.1 95 0.001 Average drops to 0.99 (two outliers)
SSG to Applications (650+ Developers)
|     | 2.25 | 0.07 | 95  | 0   |     |
| --- | ---- | ---- | --- | --- | --- |
- 56 Firms
SSG to Applications (less then 650
|     | 2.77 | 0.23 | 75  | 0   |     |
| --- | ---- | ---- | --- | --- | --- |
Developers) - 55 Firms
Champions-to-Developer Ratio (per 100  Average drops to 4.8 (two
|     | 5.9 | 1.2 | 102.2 | 0   |     |
| --- | --- | --- | ----- | --- | --- |
Developers) outliers)
Champions-to-Developer Ratio (650+  Only includes firms with
| Developers) -41 Firms (per 100  | 5.81 | 3   | 25.63 | 0.03 champions |     |
| ------------------------------- | ---- | --- | ----- | -------------- | --- |
Developers)
Champions-to-Developer Ratio (less  Only includes firms with
than 650 Developers) - 24 Firms (per 100  17.5 6.43 102.2 0.2
champions
Developers)
Average drops to 0.74 (two
| Champions to Applications | 1.6 | 0.03 | 52.5 | 0   |     |
| ------------------------- | --- | ---- | ---- | --- | --- |
outliers)
Champions-to-Applications Ratio (650+  Only includes firms with
|     | 2.07 | 0.22 | 52.5 | 0   |     |
| --- | ---- | ---- | ---- | --- | --- |
Developers) - 41 Firms champions
Champions-to-Applications Ratio (less  Only includes firms with
|     | 3.86 | 0.85 | 45  | 0.01 |     |
| --- | ---- | ---- | --- | ---- | --- |
than 650 Developers) - 24 Firms champions
Table 6. THE SOFTWARE SECURITY GROUP. We calculated the ratio of full-time SSG members and champions to developers and applications for the
entire data pool by averaging the individual ratio for each participating firm. In the “Notes” column, we show the impact of removing outliers in the data.
BSIMM16 41

SECURITY CHAMPIONS the feasibility and practicality of proposed software security changes
and improvements. Understanding how SSI governance changes
In addition to the SSG, many SSIs have identified individuals (often might affect project timelines and budgets helps the champions
developers, testers, architects, cloud and DevOps engineers, proactively identify potential frictions and minimize them.
and other SDLC roles) who are a driving force in improving
A successful security champions programs gets together regularly
software security but are (likely) not directly employed in the
to compare notes, learn new technologies, and expand stakeholder
SSG. We historically refer to this group as the satellite, while
understanding of the organization’s software security challenges.
many organizations today refer to them as their software security
Motivated individuals often share digital work products, such as
champions. Champions can enable an SSI to scale its efforts while
sensors, code, scripts, tools, and security features, rather than,
reducing dependency on the SSG team, and there appears to be
for example, getting together to discuss enacting a new policy.
a correlation between a higher BSIMM score and the presence of
Specifically, these proactive champions are working bottom-up
champions, as shown in Figure 13. Having security champions
and delivering software security features and awareness through
carry out software security activities removes SSG members from
implementation.
the engineering-critical path and empowers engineering teams to
own their software security deliverables and share responsibility For more information about security champions, refer to DATA
for software security objectives. ANALYSIS: SECURITY CHAMPIONS in Part 9.
Security champions are often chosen for software portfolio
coverage (with one or two members in each engineering group)
and sometimes for reasons such as technology stack coverage or
geographical reach. The champions can act as a sounding board for
BOTTOM 20% MIDDLE 60% TOP 20%
30% 55% 96%
of the bottom of the middle of the top 20%
20% of firms have 60% of firms have of firms have
champions champions champions
Figure 13. THE CHAMPIONS AND THE BSIMM SCORE. 96% of the top-scoring firms in the BSIMM16 data pool have security champions.
In contrast, only 30% of bottom-scoring firms have them.
BSIMM16 42

OTHER KEY STAKEHOLDERS • Executives and middle management, including business
owners and product managers, must understand how early
SSIs are truly cross-departmental efforts that involve a variety of investment in security design and analysis affects the degree
stakeholders: to which users will trust their products. Business requirements
• Builders, including developers, architects, and their managers, should explicitly address security needs, including security-
must practice security engineering, taking some responsibility related compliance. Any sizable business today depends
for both the definition of “secure enough” as well as ensuring on software to work, thus, software security is a business
that what’s delivered achieves the desired posture. An SSI necessity. Executives are also the group that must provide
requires collaboration between the SSG and these engineering resources for new efforts that directly improve software
teams to carry out the activities described in the BSIMM. security and must actively support digital transformation
efforts related to infrastructure- and governance-as-code.
• Testers typically conduct functional and feature testing, but
moving on to include security testing is very useful. Some • GRC, legal, and data privacy specialists form an integral part
testers are beginning to anticipate how software architectures of the software security effort in some firms, combining forces
and infrastructures can be attacked and are working to find an with security specialists when engaging with engineering. They
appropriate balance between automated and manual testing to might be responsible for analysis of contract terms, regulatory
ensure adequate security testing coverage. and compliance requirements including privacy regulations,
definition of privacy requirements, and tracking of PII and
• Operations teams must continue to design, defend, and
other regulated data categories. This has become increasingly
maintain resilient environments because software security
common in response to requirements such as GDPR, CCPA,
doesn’t end when software is “shipped.” In accelerating trends,
and other regulations.
development and operations are collapsing into one or more
DevOps teams, and the business functionality delivered • Procurement and vendor management need to communicate
is becoming very dynamic. This means that an increasing and enforce security requirements with vendors, including
amount of security effort, including infrastructure controls and those who supply on-premises products, custom software,
security configurations, is becoming software defined (and that and software-as-a-service (SaaS). Software supply chain
software should also be secure). vendors are increasingly subjected to software security SLAs
and reviews (such as the PCI SSF and NIST’s SSDF) to help
• Administrators must understand the distributed nature of
ensure that their products are the result of an SSDL. Of course,
modern systems, create and maintain secure configurations,
not all software (e.g., open source) comes from a vendor.
and practice the principle of least privilege, especially when it
Procurement and vendor management play a vital role but
comes to host, network, infrastructure, and cloud services for
aren’t the only stakeholders responsible for managing software
deployed applications.
supply chain risk.
BSIMM16 43

PART 7:
| T H | E B | S   | I M | M   |     |
| --- | --- | --- | --- | --- | --- |
| F R | A M | E W | O   | R   | K   |

PART 7: THE BSIMM
ONE DROPPED ACTIVITY
FRAMEWORK
In the history of the BSIMM, only one activity has been dropped
from the framework. Between BSIMM1 and BSIMM2, we
Most of the BSIMM will likely fit perfectly for your SSI, but some noticed that [CR1.3] Establish coding labs or office hours
parts might feel a little less applicable. Understanding the focused on review and [T1.3] Establish SSG office hours were
model allows you to both learn from others and ensure that your always scored together. Firms either got both points or neither,
program is right for your organization. but neither activity required the other, and they were effectively
the same, so CR1.3 was dropped in favor of T1.3.
We built the first version of the BSIMM 17 years ago (late 2008) as
follows: CORE KNOWLEDGE
• We relied on our own knowledge of software security practices
The BSIMM core knowledge encompasses the activities we have
to create the initial SSF.
directly observed in BSIMM participants. We organize that core
• We conducted a series of in-person interviews with nine knowledge into an SSF, represented in Table 7, which is organized
executives in charge of SSIs. From these interviews, we into four domains—Governance, Intelligence, SSDL Touchpoints,
identified a set of 110 software security activities that we and Deployment—with those domains containing the 128
organized according to the SSF. BSIMM16 activities.
• We then created scorecards for each of the nine initiatives that
From an executive perspective, you can view BSIMM activities as
showed which of the activities each initiative carried out. To
controls implemented in a software security risk management
validate our work, we asked each participating firm to review
framework. The implemented activities might function as
the SSF, practices, activities, and the scorecard we created for
preventive, detective, corrective, or compensating controls in
their initiative, making the necessary adjustments based on
your SSI, but positioning them as controls allows for easier
their feedback.
understanding of the BSIMM’s value by governance, risk,
Today, we continue to do BSIMM assessments with in-person compliance, legal, audit, and other risk management groups.
interviews whenever possible, which we’ve done with a total of 283
We divide activities into levels per practice based on the frequency
firms so far. Increasingly, we’ve assessed both the SSG and one
with which they’re observed in our participants. Doing this
or more business units as part of creating an aggregated SSI view
helps organizations quickly understand whether the activity
for a firm. We evolve the model by digging for new kinds of efforts
they’re contemplating is common or uncommon across other
during assessments, both as new participants join and as current
organizations. Level 1 activities (often straightforward and
participants are remeasured, then by adding new activities when
universally applicable) are those that are most observed across
warranted. Since 2008, we’ve added 19 activities and dropped one
the data pool of 111 firms, level 2 activities (often more difficult
original activity that was effectively a duplicate of another to give
to implement and requiring more coordination) are less frequently
us a total of 128 activities today. We also adjust the positioning of
observed, and level 3 activities (usually more difficult to implement
activities in the model practices according to their observation rates.
and not always applicable) are more rarely observed. Note that
new activities are added at level 3 because we don’t yet know how
common they are, so they start with zero observations.
DOMAINS
GOVERNANCE INTELLIGENCE SSDL TOUCHPOINTS DEPLOYMENT
Practices that help organize, Practices that result in collections Practices associated with Practices that interface with traditional
manage, and measure a of corporate knowledge used in analysis and assurance of network security and software
software security initiative. carrying out software security particular software development maintenance organizations. Software
Staff development is also a activities throughout the artifacts and processes. All configuration, maintenance, and other
central governance practice. organization. Collections include software security methodologies environment issues have direct impact
both proactive security guidance and include these practices. on software security.
organizational threat modeling.
PRACTICES
GOVERNANCE INTELLIGENCE SSDL TOUCHPOINTS DEPLOYMENT
1. Strategy & Metrics (SM) 4. Attack Models (AM) 7. Architecture Analysis (AA) 10. Penetration Testing (PT)
2. Compliance & Policy (CP) 5. Security Features & Design (SFD) 8. Code Review (CR) 11. Software Environment (SE)
3. Training (T) 6. Standards & Requirements (SR) 9. Security Testing (ST) 12. Configuration Management &
Vulnerability Management (CMVM)
Table 7. THE SOFTWARE SECURITY FRAMEWORK. Twelve practices align with the four high-level domains and contain the 128 BSIMM16 activities.
BSIMM16 45

UNDERSTANDING THE MODEL
GOVERNANCE
A domain, such as Governance, contains practices, such as
1. Strategy & Metrics (SM)
Strategy & Metrics, each of which contains activities that in turn
have a detailed description. Creating a scorecard (e.g., activity
2. Compliance & Policy (CP)
SM1.1 was observed and is marked with a “1”) informs decisions
| about strategic change (see Figure 14).  |     | 3. Training (T) |     |
| ---------------------------------------- | --- | --------------- | --- |
GOVERNANCE
STRATEGY & METRICS
[SM1.1] Publish process and evolve as necessary. [SM2.7] Create evangelism role and perform internal marketing.
[SM1.3] Educate executives on software security. [SM3.1] Use a software asset tracking application with portfolio
view.
[SM1.4] Implement security checkpoints and associated  [SM3.2] Make SSI efforts part of external marketing.
governance.
[SM1.7] Enforce security checkpoints and track exceptions. [SM3.3] Identify metrics and use them to drive resourcing.
[SM2.1] Publish data about software security internally and use it  [SM3.4] Integrate software-defined lifecycle governance.
to drive change.
[SM2.3] Create or grow a security champions program. [SM3.5] Integrate software supply chain risk management.
[SM2.6] Require security sign-off prior to software release.
| [SM2.7: 49] CREATE EVANGELISM ROLE AND  |          | GOVERNANCE |              |
| --------------------------------------- | -------- | ---------- | ------------ |
| PERFORM INTERNAL MARKETING.             |          | "BSIMM16   |              |
|                                         | ACTIVITY | FIRMS      | EXAMPLE FIRM |
(OUT OF 111)"
Build support for software security throughout the organization
via ongoing evangelism and ensure that everyone aligns on  STRATEGY & METRICS
security objectives. This internal marketing function, often  [SM1.1] 84 1
performed by a variety of stakeholder roles, keeps executives
|     | [SM1.3] | 66  |     |
| --- | ------- | --- | --- |
and others up to date on the magnitude of the software
|     | [SM1.4] | 100 |     |
| --- | ------- | --- | --- |
security problem and the elements of its solution. A champion
|     | [SM1.7] | 71  |     |
| --- | ------- | --- | --- |
or a scrum master familiar with security, for example, could
help teams adopt better software security practices as they  [SM2.1] 54
transform to Agile and DevOps methods. Similarly, a cloud
|     | [SM2.3] | 55  |     |
| --- | ------- | --- | --- |
expert could demonstrate the changes needed in security
|     | [SM2.6] | 62  |     |
| --- | ------- | --- | --- |
architecture and testing for serverless applications. Evangelists
can increase understanding and build credibility by giving  [SM2.7] 49 1
talks to internal groups (including executives), publishing  [SM3.1] 31
roadmaps, authoring technical papers for internal consumption,
|     | [SM3.2] | 25  |     |
| --- | ------- | --- | --- |
or creating a collection of papers, books, and other resources
|     | [SM3.3] | 30  |     |
| --- | ------- | --- | --- |
on an internal website (see [SR1.2]) and promoting its use.
|     | [SM3.4] | 9   |     |
| --- | ------- | --- | --- |
In turn, organizational feedback becomes a useful source of
| improvement ideas. | [SM3.5] | 5   |     |
| ------------------ | ------- | --- | --- |
Figure 14. THE PIECES OF THE BSIMM MODEL.
BSIMM16 46

DETAILED VIEW OF THE BSIMM DURING OUR
FRAMEWORK
ASSESSMENT EFFORTS
The BSIMM framework and data model evolve over time ACROSS HUNDREDS OF
to accurately represent actual software security practices.
Understanding these changes will help you set strategic ORGANIZATIONS, WE
directions for your own SSI.
MAKE QUALITATIVE
Here, we explore the BSIMM framework in more detail, including OBSERVATIONS ABOUT HOW
the methodology of how we created the model, how it evolved over
time, and how we updated it for BSIMM16. SSIs ARE EVOLVING AND
As a descriptive model, the only goal of the BSIMM is to observe
REPORT MANY OF THOSE AS
and report. We like to say we visited many restaurants to see
what was happening and observed that “there are three chicken INSIGHTS, ANALYSIS, AND
eggs in an omelet.” Note that the BSIMM does not extrapolate to
say, “all omelets must have three eggs,” “only chicken eggs make OTHER DISCUSSIONS IN
acceptable omelets,” “omelets must be eaten every day,” or any
other value judgments. We offer simple observations, simply THIS DOCUMENT.
reported.
Of course, during our assessment efforts across hundreds of
organizations, we also make qualitative observations about how
SSIs are evolving and report many of those as trends, insights,
THE DETAILED BSIMM SKELETON
analysis, and other topical discussions both in this document and
The detailed BSIMM skeleton provides a way to view the model
among BSIMM participants.
at a glance and is useful when assessing an SSI. The skeleton is
Our “just the facts” approach is hardly novel in science and shown in Figure 15 and contains the activity references organized
engineering, but in the realm of software security, it has not by levels, domains, and practices. More complete descriptions
previously been applied at this scale. Other work around SSI of the activities and examples are available in Part 8 of this
modeling has either described the experience of a single document.
organization or offered prescriptive guidance based on a
combination of personal experience and opinion.
BSIMM16 47

GOVERNANCE
|         | STRATEGY & METRICS             |         | COMPLIANCE & POLICY         |        | TRAINING                   |
| ------- | ------------------------------ | ------- | --------------------------- | ------ | -------------------------- |
|         | Publish process and evolve as  |         |                             |        | Conduct software security  |
| [SM1.1] |                                | [CP1.1] | Unify regulatory pressures. | [T1.1] |                            |
|         | necessary.                     |         |                             |        | awareness training.        |
Educate executives on software  Deliver on-demand individual
| [SM1.3] |           | [CP1.2] | Identify privacy obligations. | [T1.7] |           |
| ------- | --------- | ------- | ----------------------------- | ------ | --------- |
|         | security. |         |                               |        | training. |
Implement security checkpoints and  Include security resources in
| [SM1.4] |                        | [CP1.3] | Create policy. | [T1.8] |             |
| ------- | ---------------------- | ------- | -------------- | ------ | ----------- |
|         | associated governance. |         |                |        | onboarding. |
Enforce security checkpoints and  Enhance security champions through
| [SM1.7] |                   | [CP2.1] | Build a PII inventory. | [T2.5] |                      |
| ------- | ----------------- | ------- | ---------------------- | ------ | -------------------- |
|         | track exceptions. |         |                        |        | training and events. |
Publish data about software security  Require security sign-off for  Create and use material specific to
| [SM2.1] |     | [CP2.2] |     | [T2.8] |     |
| ------- | --- | ------- | --- | ------ | --- |
internally and use it to drive change. compliance-related risk. company history.
Create or grow a security champions  Implement and track controls for  Deliver role-specific advanced
| [SM2.3] |                                     | [CP2.3] |                                        | [T2.9]  |                                |
| ------- | ----------------------------------- | ------- | -------------------------------------- | ------- | ------------------------------ |
|         | program.                            |         | compliance.                            |         | curriculum.                    |
|         | Require security sign-off prior to  |         | Include software security SLAs in all  |         |                                |
| [SM2.6] |                                     | [CP2.4] |                                        | [T2.10] | Host software security events. |
|         | software release.                   |         | vendor contracts.                      |         |                                |
|         | Create evangelism role and perform  |         | Ensure executive awareness of          |         |                                |
| [SM2.7] |                                     | [CP2.5] |                                        | [T2.11] | Require an annual refresher.   |
|         | internal marketing.                 |         | compliance and privacy obligations.    |         |                                |
Use a software asset tracking  Document a software compliance  Provide expertise via open
| [SM3.1] |     | [CP3.1] |     | [T2.12] |     |
| ------- | --- | ------- | --- | ------- | --- |
application with portfolio view. story. collaboration channels.
Make SSI efforts part of external  Reward progression through
| [SM3.2] |            | [CP3.2] | Ensure compatible vendor policies. | [T3.1] |             |
| ------- | ---------- | ------- | ---------------------------------- | ------ | ----------- |
|         | marketing. |         |                                    |        | curriculum. |
Identify metrics and use them to  Drive feedback from software  Provide training for vendors and
| [SM3.3] |     | [CP3.3] |     | [T3.2] |     |
| ------- | --- | ------- | --- | ------ | --- |
drive resourcing. lifecycle data back to policy. outsourced workers.
Integrate software-defined lifecycle  Identify new security champions
| [SM3.4] |             |     |     | [T3.6] |                      |
| ------- | ----------- | --- | --- | ------ | -------------------- |
|         | governance. |     |     |        | through observation. |
Integrate software supply chain risk
[SM3.5]
management.
INTELLIGENCE
ATTACK MODELS SECURITY FEATURES & DESIGN STANDARDS & REQUIREMENTS
|         | Use a data classification scheme for  |          | Integrate and deliver security  |         |                            |
| ------- | ------------------------------------- | -------- | ------------------------------- | ------- | -------------------------- |
| [AM1.2] |                                       | [SFD1.1] |                                 | [SR1.1] | Create security standards. |
|         | software inventory.                   |          | features.                       |         |                            |
Application architecture teams
[AM1.3] Identify potential attackers. [SFD1.2] [SR1.2] Create a security portal.
engage with the SSG.
|         |                                     |          | Leverage secure-by-design             |         | Translate compliance constraints to  |
| ------- | ----------------------------------- | -------- | ------------------------------------- | ------- | ------------------------------------ |
| [AM1.5] | Gather and use attack intelligence. | [SFD2.1] |                                       | [SR1.3] |                                      |
|         |                                     |          | components and services.              |         | requirements.                        |
|         | Build attack patterns and abuse     |          | Create capability to solve difficult  |         |                                      |
| [AM2.1] |                                     | [SFD2.2] |                                       | [SR1.5] | Identify open source.                |
|         | cases tied to potential attackers.  |          | design problems.                      |         |                                      |
Form a review board to approve and
[AM2.6] Collect and publish attack stories. [SFD3.1] [SR2.2] Create a standards review process.
maintain secure design patterns.
|         | Build an internal forum to discuss   |          | Require use of approved security  |         |                           |
| ------- | ------------------------------------ | -------- | --------------------------------- | ------- | ------------------------- |
| [AM2.7] |                                      | [SFD3.2] |                                   | [SR2.5] | Create SLA boilerplate.   |
|         | attacks.                             |          | features and frameworks.          |         |                           |
|         | Have a research group that develops  |          | Find and publish secure design    |         |                           |
| [AM2.8] |                                      | [SFD3.3] |                                   | [SR2.7] | Control open source risk. |
|         | new attack methods.                  |          | patterns from the organization.   |         |                           |
[AM2.9] Monitor automated asset creation. [SR3.2] Communicate standards to vendors.
Create and use automation to mimic
| [AM3.2] |     |     |     | [SR3.3] | Use secure coding standards. |
| ------- | --- | --- | --- | ------- | ---------------------------- |
attackers.
Create technology-specific attack  Create standards for technology
| [AM3.4] |           |     |     | [SR3.4] |         |
| ------- | --------- | --- | --- | ------- | ------- |
|         | patterns. |     |     |         | stacks. |
Create standards controlling
Maintain and use a top N possible
| [AM3.5] |     |     |     | [SR3.5] | and guiding the adoption of new  |
| ------- | --- | --- | --- | ------- | -------------------------------- |
attacks list.
technologies.
BSIMM16 48

SSDL TOUCHPOINTS
| ARCHITECTURE ANALYSIS |     | CODE REVIEW |     | SECURITY TESTING |
| --------------------- | --- | ----------- | --- | ---------------- |
Perform edge/boundary value
[AA1.1] Perform security feature review. [CR1.2] Perform opportunistic code review. [ST1.1]
condition testing during QA.
Perform design review for high-risk  Drive tests with security
| [AA1.2] | [CR1.4] | Use automated code review tools. | [ST1.3] |     |
| ------- | ------- | -------------------------------- | ------- | --- |
applications. requirements and security features.
Use a risk methodology to rank  Make code review mandatory for all  Integrate opaque-box security tools
| [AA1.4]       | [CR1.5] |           | [ST1.4] |                      |
| ------------- | ------- | --------- | ------- | -------------------- |
| applications. |         | projects. |         | into the QA process. |
Perform architecture analysis using
[AA2.1] [CR1.7] Assign code review tool mentors. [ST2.4] Drive QA tests with AST results.
a defined process.
Standardize architectural  Use custom rules with automated  Include security tests in QA
| [AA2.2]                                      | [CR2.6] |                                   | [ST2.5] |                                     |
| -------------------------------------------- | ------- | --------------------------------- | ------- | ----------------------------------- |
| descriptions.                                |         | code review tools.                |         | automation.                         |
|                                              |         | Use a top N bugs list (real data  |         | Perform fuzz testing customized to  |
| [AA2.4] Have SSG lead design review efforts. | [CR2.7] |                                   | [ST2.6] |                                     |
|                                              |         | preferred).                       |         | application APIs.                   |
Have engineering teams lead AA  Use centralized defect reporting to  Drive tests with design review
| [AA3.1]  | [CR2.8] |                           | [ST3.3] |          |
| -------- | ------- | ------------------------- | ------- | -------- |
| process. |         | close the knowledge loop. |         | results. |
Drive analysis results into standard  Build a capability to combine AST
| [AA3.2] | [CR3.2] |     | [ST3.4] | Leverage code coverage analysis. |
| ------- | ------- | --- | ------- | -------------------------------- |
design patterns. results.
Make the SSG available as an AA  Begin to build and apply adversarial
| [AA3.3] | [CR3.3] | Create capability to eradicate bugs. | [ST3.5] |     |
| ------- | ------- | ------------------------------------ | ------- | --- |
resource or mentor. security tests (abuse cases).
Implement event-driven security
|     | [CR3.4] | Automate malicious code detection. | [ST3.6] |     |
| --- | ------- | ---------------------------------- | ------- | --- |
testing in automation.
|     | [CR3.5] | Enforce secure coding standards. |     |     |
| --- | ------- | -------------------------------- | --- | --- |
DEPLOYMENT
CONFIGURATION MANAGEMENT &
| PENETRATION TESTING | SOFTWARE ENVIRONMENT |     |     |     |
| ------------------- | -------------------- | --- | --- | --- |
VULNERABILITY MANAGEMENT
Use external penetration testers to  Use application input monitoring for  Create or interface with incident
| [PT1.1]        | [SE1.1] |                    | [CMVM1.1] |           |
| -------------- | ------- | ------------------ | --------- | --------- |
| find problems. |         | security purposes. |           | response. |
Identify software defects found in
Feed results to the defect  Ensure host and network security
| [PT1.2] | [SE1.2] |     | [CMVM1.2] | operations monitoring and feed  |
| ------- | ------- | --- | --------- | ------------------------------- |
management and mitigation system. basics are in place.
them back to engineering.
Use penetration testing tools  Track software defects found in
| [PT1.3] | [SE1.3] | Implement cloud security controls. | [CMVM1.3] |     |
| ------- | ------- | ---------------------------------- | --------- | --- |
internally. operations through the fix process.
Penetration testers use all available  Define secure deployment
| [PT2.2] | [SE1.4] |     | [CMVM1.4] | Have emergency response. |
| ------- | ------- | --- | --------- | ------------------------ |
information. parameters and configurations.
Schedule periodic penetration tests  Develop an operations software
| [PT2.3] | [SE2.4] | Protect code integrity. | [CMVM2.3] |     |
| ------- | ------- | ----------------------- | --------- | --- |
for application coverage. inventory.
Use external penetration testers to  Use application containers to  Streamline incoming responsible
| [PT3.1] | [SE2.5] |     | [CMVM2.4] |     |
| ------- | ------- | --- | --------- | --- |
perform deep-dive analysis. support security goals. vulnerability disclosure.
|     |     | Use orchestration for containers and  |     | Fix all occurrences of software  |
| --- | --- | ------------------------------------- | --- | -------------------------------- |
[PT3.2] Customize penetration testing tools. [SE2.7] [CMVM3.1]
|     |     | virtualized environments. |     | defects found in operations. |
| --- | --- | ------------------------- | --- | ---------------------------- |
Enhance the SSDL to prevent
|     | [SE3.2] | Use code protection. | [CMVM3.2] | software defects found in  |
| --- | ------- | -------------------- | --------- | -------------------------- |
operations.
Use application behavior monitoring
|     | [SE3.3] |     | [CMVM3.3] | Simulate software crises. |
| --- | ------- | --- | --------- | ------------------------- |
and diagnostics.
Create bills of materials for deployed
|     | [SE3.6] |     | [CMVM3.4] | Operate a bug bounty program. |
| --- | ------- | --- | --------- | ----------------------------- |
software.
|     |          | Perform application composition       |           | Automate verification of operational  |
| --- | -------- | ------------------------------------- | --------- | ------------------------------------- |
|     | [SE3.8]  |                                       | [CMVM3.5] |                                       |
|     |          | analysis on code repositories.        |           | infrastructure security.              |
|     |          | Protect integrity of development      |           | Publish risk data for deployable      |
|     | [SE3.9]  |                                       | [CMVM3.6] |                                       |
|     |          | toolchains.                           |           | artifacts.                            |
|     |          | Protect the integrity of development  |           | Do attack surface management for      |
|     | [SE3.10] |                                       | [CMVM3.8] |                                       |
|     |          | endpoints.                            |           | deployed applications.                |
Figure 15. THE DETAILED BSIMM SKELETON. Within the SSF, the 128 activities are organized into three
levels, across 12 practices, and within the four BSIMM domains.
BSIMM16 49

CREATING BSIMM16 FROM BSIMM15 champions through observation, both of which started as level
BSIMM16 includes updated activity descriptions, data from  1 activities. The BSIMM1 activity [AM1.1] Build and maintain a
firms in multiple vertical markets, and a longitudinal study. For  top N possible attacks list became [AM2.5] in BSIMM7 and then
[AM3.5] in BSIMM14 as observation rates declined relative to other
BSIMM16, we added 16 firms and removed 26, resulting in a data
Attack Model activities. [T1.4] Identify new security champions
pool of 111 firms.
through observation, also a BSIMM1 activity, became [T2.7] in
For the first time, there have been no changes to the BSIMM
BSIMM4 and [T3.6] in BSIMM8 as organizations adopted other
framework this year. Many activities saw significant growth in the
ways of identifying new security champion candidates. [T3.6]
last year but none to the extent that moving activities between
also demonstrates how activities evolve over time, changing from
levels seemed necessary. Some level 3 activities ([T3.2] Provide
Identify satellite through training to Identify new satellite members
training for vendors and outsourced workers and [CMVM 3.4]
through observation with BSIMM11, Identify new satellite members
Operate a bug bounty program) are coming close to the number of
(security champions) through observation with BSIMM13, and
observations for level 2 activities for those practices but are only
finally Identify new security champions through observation to
near activities that are slowly declining. Rather than rush to make
reflect both where the identifying was occurring as well as more
changes based on less than solid trends, the decision was made  common terminology in the industry.
to not move activities this year and let the trends develop further.
In addition, while some new activities were considered, the things  In BSIMM13, we had the first activity that migrated from level 3
that would have gone into them are largely covered in existing  to level 1—[SE1.3] Implement cloud security controls, which was
introduced in BSIMM9. While the relative growth of [SE2.5] Use
activities.
application containers to support security goals has slowed down,
As a result, we again have a total of 128 activities in BSIMM16.
it is one of the potential candidates to migrate from level 3 to level
To see of how the BSIMM functions as an observational model,  1 over the next couple of years. See Table 8 for the observation
consider the activities that are now [AM3.5] Maintain and use  growth in activities that were added since BSIMM7.
a top N possible attacks list and [T3.6] Identify new security
OBSERVATIONS
ACTIVITY BSIMM7 BSIMM8 BSIMM9 BSIMM10 BSIMM11 BSIMM12 BSIMM13 BSIMM14 BSIMM15 BSIMM16
| SE3.4 (now SE2.5) | 0 4 | 11  | 14  | 31  | 44  | 52  | 63  | 64  | 59  |
| ----------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SE3.5 (now SE2.7) |     | 0   | 5   | 22  | 33  | 42  | 47  | 42  | 40  |
| SE3.6             |     | 0   | 3   | 12  | 14  | 18  | 22  | 25  | 31  |
| SE3.7 (now SE1.3) |     | 0   | 9   | 36  | 59  | 79  | 92  | 87  | 79  |
| SM3.4             |     |     | 0   | 1   | 6   | 5   | 8   | 11  | 9   |
| AM3.3 (now        |     |     | 0   | 4   | 6   | 11  | 17  | 18  | 22  |
AM2.9)
| CMVM3.5       |     |     | 0   | 8   | 10  | 13  | 16  | 17  | 24  |
| ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ST3.6         |     |     |     | 0   | 2   | 3   | 6   | 8   | 10  |
| CMVM3.6       |     |     |     | 0   | 0   | 3   | 3   | 4   | 5   |
| CMVM3.7 (now  |     |     |     |     | 0   | 20  | 35  | 41  | 53  |
CMVM2.4)
| SM3.5   |     |     |     |     |     | 0   | 0   | 1   | 5   |
| ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SE3.8   |     |     |     |     |     | 0   | 2   | 3   | 8   |
| CMVM3.8 |     |     |     |     |     | 0   | 0   | 1   | 3   |
| SE3.9   |     |     |     |     |     |     | 0   | 3   | 13  |
| SR3.5   |     |     |     |     |     |     |     | 0   | 2   |
| SE3.10  |     |     |     |     |     |     |     | 0   | 6   |
Table 8. NEW ACTIVITIES. Some activities have seen exceptional growth in observation counts (highlighted in orange), likely demonstrating their
widespread utility. [SE3.7], highlighted in gray, is the first activity to migrate from level 3 (very uncommon) to level 1 (common)
| BSIMM16 |     |     |     |     |     |     |     |     | 50  |
| ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

MODEL CHANGES OVER TIME
WHERE DO OLD ACTIVITIES GO? ([SM2.3] Create or grow a security champions program). Second,
some activities don’t yet fit tightly with the evolving engineering
We continue to ponder the question, “Where do activities go when
culture, and the activity effort currently causes too much friction.
no one does them anymore?” We’ve noticed that the observation
For example, continuously going to engineering teams to find
rate for other seemingly useful activities has decreased
secure design patterns ([SFD3.3] Find and publish secure design
significantly in recent years:
patterns from the organization) might unacceptably delay key
• [CR3.5] Enforce secure coding standards declined from a development processes.
high of 55.6% of firms in BSIMM1 to a low of 0% of firms in
It might also be the case that evolving SSI and DevOps
BSIMM12, although it has climbed back to 3.6% with BSIMM16.
architectures are changing the way some activities are getting
• [T3.6] Identify new security champions through observation done. If an organization’s use of purpose-built architectures,
was observed in 11 of 51 firms in BSIMM4 but only in eight of development kits, and libraries is sufficiently consistent, perhaps
111 firms in BSIMM16. it’s less necessary to lean on prescriptive coding standards
• [SFD3.3] Find and publish secure design patterns from the ([CR3.5] Enforce secure coding standards) as a measure of
organization was observed in 14 of 51 firms in BSIMM4 but acceptable code.
only in 11 of 111 firms in BSIMM16. As a point of culture-driven contrast, we see significant increases
• [SR3.3] Use secure coding standards was observed in 23 of 78 in observation counts for activities such as [SE1.3] Implement
firms in BSIMM6 but only in 19 of 111 firms in BSIMM16. cloud security controls, [SE2.5] Use application containers to
support security goals, and [SE2.7] Use orchestration for containers
We believe there are two primary reasons why observations for
and virtualized environments, likely for similar reasons that we
some activities have decreased toward zero over time. First, some
see lower counts for the other activities above. The engineering
activities have become part of the culture and drive different
culture has shifted to be more self-service and to include increased
behavior—for example, choosing security champions members
telemetry that produces more data for everyone to use. We keep a
might become a more organic part of the SSDL without requiring
close watch on the BSIMM data pool and will make adjustments as
extra effort in identifying champions members ([T3.6] Identify
needed, which might include dropping an activity from the model.
new security champions through observation) to grow that team
Being a unique, real-world reflection of actual software security practices, the BSIMM naturally changes over time. While each release of the
BSIMM captures the current dataset and provides the most current guidance, reflection upon past changes can help clarify the ebb and flow of
specific activities. Table 9 shows the activity moves, adds, and deletes that have occurred since the BSIMM’s creation.
BSIMM16 51

CHANGES FOR BSIMM16 (128 ACTIVITIES) • No Changes
CHANGES FOR BSIMM15 (128 ACTIVITES) • [SM2.2] Enforce security checkpoints and track exceptions became [SM1.7]
• [SE2.2] Define secure deployment parameters and configurations became [SE1.4]
• [CMVM2.1] Have emergency response became [CMVM1.4]
• [CMVM3.7] Streamline incoming responsible vulnerability disclosure became [CMVM2.4]
• [SR3.5] Create standards controlling and guiding the adoption of new technologies was
added to the model
• [SE3.10] Protect the integrity of development endpoints was added to the model
CHANGES FOR BSIMM14 (126 ACTIVITIES) • [T3.5] Provide expertise via open collaboration channels became [T2.12]
• [AM2.2] Create technology-specific attack patterns became [AM3.4]
• [AM2.5] Maintain and use a top N possible attacks list became [AM3.5]
• [AM3.1] Have a research group that develops new attack methods became [AM2.8]
• [AM3.3] Monitor automated asset creation became [AM2.9]
• [SR2.4] Identify open source became [SR1.5]
• [CMVM2.2] Track software bugs found in operations through the fix process became
[CMVM1.3]
• [SE3.9] Protect integrity of SDLC toolchains was added to the model
CHANGES FOR BSIMM13 (125 ACTIVITIES) • [T3.3] Host software security events became [T2.10]
• [T3.4] Require an annual refresher became [T2.11]
• [SR3.1] Control open source risk became [SR2.7]
• [AA1.3] Have SSG lead design review efforts became [AA2.4]
• [CR1.6] Use centralized defect reporting to close the knowledge loop became [CR2.8]
• [SE2.6] Implement cloud security controls became [SE1.3]
• [SM3.5] Integrate software supply chain risk management added to the model
• [SE3.8] Perform application composition analysis on code repositories added to the
model
• [CMVM3.8] Do attack surface management for deployed applications added to the model
CHANGES FOR BSIMM12 (122 ACTIVITIES) • [SM1.2] Create evangelism role and perform internal marketing became [SM2.7]
• [T1.5] Deliver role-specific advanced curriculum became [T2.9]
• [ST2.1] Integrate black-box security tools into the QA process became [ST1.4]
• [SE3.5] Use orchestration for containers and virtualized environments became [SE2.7]
• [CMVM3.7] Streamline incoming responsible vulnerability disclosure added to the model
CHANGES FOR BSIMM11 (121 ACTIVITIES) • [T2.6] Include security resources in onboarding became [T1.8]
• [CR2.5] Assign tool mentors became [CR1.7]
• [SE3.4] Use application containers to support security goals became [SE2.5]
• [SE3.7] Ensure cloud security basics became [SE2.6]
• [ST3.6] Implement event-driven security testing in automation added to the model
• [CMVM3.6] Publish risk data for deployable artifacts added to the model
CHANGES FOR BSIMM10 (119 ACTIVITIES) • [T1.6] Create and use material specific to company history became [T2.8]
• [SR2.3] Create standards for technology stacks moves to become [SR3.4]
• [SM3.4] Integrate software-defined lifecycle governance added to the model
• [AM3.3] Monitor automated asset creation added to the model
• [CMVM3.5] Automate verification of operational infrastructure security added to the model
CHANGES FOR BSIMM9 (116 ACTIVITIES) • [SM2.5] Identify metrics and use them to drive resourcing became [SM3.3]
• [SR2.6] Use secure coding standards became [SR3.3]
• [SE3.5] Use orchestration for containers and virtualized environments added to the model
• [SE3.6] Enhance application inventory with operations bill of materials added to the model
• [SE3.7] Ensure cloud security basics added to the model
BSIMM16 52

CHANGES FOR BSIMM8 (113 ACTIVITIES) • [T2.7] Identify new satellite through training became [T3.6]
• [AA2.3] Make SSG available as AA resource or mentor became [AA3.3]
CHANGES FOR BSIMM7 (113 ACTIVITIES) • [AM1.1] Maintain and use a top N possible attacks list became [AM2.5]
• [AM1.4] Collect and publish attack stories became [AM2.6]
• [AM1.6] Build an internal forum to discuss attacks became [AM2.7]
• [CR1.1] Use a top N bugs list became [CR2.7]
• [CR2.2] Enforce coding standards became [CR3.5]
• [SE3.4] Use application containers to support security goals added to model
CHANGES FOR BSIMM6 (112 ACTIVITIES) • [SM1.6] Require security sign-off prior to software release became [SM2.6]
• [SR1.4] Use secure coding standards became [SR2.6]
• [ST3.1] Include security tests in QA automation became [ST2.5]
• [ST3.2] Perform fuzz testing customized to application APIs became [ST2.6]
CHANGES FOR BSIMM-V (112 ACTIVITIES) • [SFD2.3] Find and publish mature design patterns from the organization became [SFD3.3]
• [SR2.1] Communicate standards to vendors became [SR3.2]
• [CR3.1] Use automated tools with tailored rules became [CR2.6]
• [ST2.3] Begin to build and apply adversarial security tests (abuse cases) became [ST3.5]
• [CMVM3.4] Operate a bug bounty program added to model
CHANGES FOR BSIMM4 (111 ACTIVITIES) • [T2.1] Deliver role-specific advanced curriculum became [T1.5]
• [T2.2] Company history in training became [T1.6]
• [T2.4] Deliver on-demand individual training became [T1.7]
• [T1.2] Include security resources in onboarding became [T2.6]
• [T1.4] Identify new satellite members through training became [T2.7]
• [T1.3] Establish SSG office hours became [T3.5]
• [AM2.4] Build an internal forum to discuss attacks became [AM1.6]
• [CR2.3] Make code review mandatory for all projects became [CR1.5]
• [CR2.4] Use centralized reporting to close the knowledge loop became [CR1.6]
• [ST1.2] Share security results with QA became [ST2.4]
• [SE2.3] Use application behavior monitoring and diagnostics became [SE3.3]
• [CR3.4] Automate malicious code detection added to model
• [CMVM3.3] Simulate software crises added to model
CHANGES FOR BSIMM3 (109 ACTIVITIES) • [SM1.7] Identify metrics and use them to drive resourcing became [SM2.5]
• [SM2.4] Require security sign-off became [SM1.6]
• [AM2.3] Gather and use attack intelligence became [AM1.5]
• [ST2.2] Drive tests with security requirements and security features became [ST1.3]
• [PT2.1] Use pen testing tools internally became [PT1.3]
CHANGES FOR BSIMM2 (109 ACTIVITIES) • [T2.3] Require an annual refresher became [T3.4]
• [CR2.1] Use automated tools became [CR1.4]
• [SE2.1] Use code protection became [SE3.2]
• [SE3.1] Use code signing became [SE2.4]
• [CR1.3] removed from the model
CHANGES FOR BSIMM1 (110 ACTIVITIES) • Added 110 activities
Table 9. ACTIVITY CHANGES OVER TIME. This table allows for historical review of how BSIMM
activities have been added, moved, and deleted since inception.
BSIMM16 53

DATA: BSIMM16 To provide another view into this data, we created a box plot
chart by taking the percentage of activities observed in each
Every organization wants to do software security more practice and showing the distribution of those percentages for
effectively and efficiently. You can use this information to all 111 firms in the data pool (see Figure 16). Looking at the
understand what BSIMM participants are doing today and how score distributions provides more data than the simple average
those efforts have evolved over time, then plan your own SSI we used to use, for example, five practices see some companies
changes. doing 100% of the activities, Strategy & Metrics, Compliance
& Policy, Security Features & Design, Penetration Testing, and
Configuration Management and Vulnerability Management, while
The BSIMM data yields very interesting analytical results, as shown the interquartile range (the middle 50% of the scores) varies
throughout this document. Figure 18 shows the highest resolution across all five practices. Only two practices, Software Environment
observation data that is published, and organizations can use this and Configuration Management & Vulnerability Management,
information to note how often we observe each activity across all show all 111 firms doing at least something in those practices The
111 participants to help plan their next areas of focus. Activities other 10 practices all have at least one firm doing nothing in that
that are broadly popular will likely benefit your organization as well. practice. Looking at the median scores, Compliance & Policy and
Penetration Testing have the highest median scores, while Security
In Figure 18, we also identified the most common activity in each
Testing, QA, and other early phase testing have the lowest.
practice (highlighted in orange). To provide some perspective on
what “most common” means, although [T1.1] is the most common The range of observed scores in the current data pool is 12 for the
activity in the Training practice with 61 observations, Table 11 lower score and 101 for the higher score, indicating a wide range
shows that it isn’t in the top 20 activities across all practices. of SSI maturity levels in the BSIMM16 data.
READING A BOX PLOT
A box plot, also known as a box and whisker plot, provides a visual summary of a range of data. It shows the minimum and maximum, the
first quartile (bottom 25% of the values), third quartile (top 25% of the values), the interquartile range (the middle 50% of the values), and the
median.
The vertical axis is the percentage of activities in the
practice vs. how many were observed from that practice.
A firm scoring 5 activities from a practice with 10 activities This chart is for
total would score 50% the entire BSIMM
data pool “Earth”
Practice Scores Distribution for Earth (121)
100%
How the top 25%
90% of firms scored
80%
70% Box shows where
the middle 50% of
60% the firms scored
50%
Purple circle
40%
shows the
30% average score
20% White diamond
shows the
10%
median score
0%
Strategy & Compliance Training Attack Security Standards & Architecture Code Security How the bottom
Metrics & Policy Models Features Requirements Analysis Review Testing
& Design 25% of firms
scored
Median Average
25% of the values will fall between the first quartile and the minimum, 25% of the values will fall between the third quartile and the maximum,
and 50% will fall between the first and third quartiles. The median is the middle value in a set of numbers when they are sorted in ascending
or descending order.
BSIMM16 54

100%
90%
100%
80%
90%
70%
80%
60%
70%
50%
60%
40%
50%
30%
40%
20%
30%
10%
20%
0%
10% Strategy & Compliance Training Attack Security Standards & Architecture Code Security Penetration Software Configuration
Metrics & Policy Models Features Requirements Analysis Review Testing Testing Environment Management
0% & Design & Vulnerability
Strategy & Compliance Training Attack Security Standards & Architecture Code Security Penetration Software CMoannfaigguermateionnt
Metrics & Policy Models Features Requirements Analysis Review Testing Testing Environment Management
& Design & Vulnerability
Management
Median Average
Figure 16. ALL FIRMS SCORE DISTRIBUTION. This diagram shows the range of the normalized observations
Median Average
collectively reached in each practice by the 111 BSIMM16 firms.
AGE-BASED PROGRAM CHANGES
Figure 17 shows the distribution of scores of all 111 participating firms. To create this graph, we divided the scores into eight bins that are then
further divided by only one BSIMM assessment having been done (iteration 1), one reassessment (iteration 2), and two or more reassessments
done (iteration 3+). We also plotted the average age of the firms’ SSIs in each bin as a horizontal line. In general, firms where more BSIMM
activities were observed have older SSIs and are more likely to have performed multiple BSIMM measurements.
25
20
15
10
5
0
0–20 21–30 31–40 41–50 51–60 61–70 71–80 81–128
Assessment Iteration 1 Assessment Iteration 2 Assessment Iteration 3
Average Age
Figure 17. BSIMM SCORE DISTRIBUTION. Assessment scores most frequently fall into the 31 to 40 range in BSIMM16,
with an average SSG age of 4.8 years. In general, firms that mature and continue to use the BSIMM as a measurement tool over time
(e.g., iteration 2, iteration 3+) tend to have higher scores. NOTE: Firms that age out of the BSIMM data pool and then return a few years
later are reset to iteration 1, which can affect the iteration counts above.
BSIMM16 55

| GOVERNANCE |     | INTELLIGENCE | SSDL TOUCHPOINTS |     | DEPLOYMENT |     |
| ---------- | --- | ------------ | ---------------- | --- | ---------- | --- |
BSIMM16  BSIMM16  BSIMM16  BSIMM16  BSIMM16  BSIMM16  BSIMM16  BSIMM16
ACTIVITY FIRMS (OUT  FIRMS (PER- ACTIVITY FIRMS (OUT  FIRMS (PER- ACTIVITY FIRMS (OUT  FIRMS (PER- ACTIVITY FIRMS (OUT  FIRMS (PER-
OF 111) CENTAGE) OF 111) CENTAGE) OF 111) CENTAGE) OF 111) CENTAGE)
STRATEGY & METRICS ATTACK MODELS ARCHITECTURE ANALYSIS PENETRATION TESTING
[SM1.1] 84 75.68% [AM1.2] 57 51.35% [AA1.1] 89 80.18% [PT1.1] 95 85.59%
[SM1.3] 66 59.46% [AM1.3] 44 39.64% [AA1.2] 51 45.95% [PT1.2] 87 78.38%
[SM1.4] 100 90.09% [AM1.5] 78 70.27% [AA1.4] 57 51.35% [PT1.3] 67 60.36%
[SM1.7] 71 63.96% [AM2.1] 20 18.02% [AA2.1] 35 31.53% [PT2.2] 40 36.04%
[SM2.1] 54 48.65% [AM2.6] 16 14.41% [AA2.2] 38 34.23% [PT2.3] 56 50.45%
[SM2.3] 55 49.55% [AM2.7] 18 16.22% [AA2.4] 36 32.43% [PT3.1] 25 22.52%
[SM2.6] 62 55.86% [AM2.8] 26 23.42% [AA3.1] 17 15.32% [PT3.2] 25 22.52%
| [SM2.7] 49 | 44.14% [AM2.9] | 22 19.82% | [AA3.2] 7  | 6.31%  |     |     |
| ---------- | -------------- | --------- | ---------- | ------ | --- | --- |
| [SM3.1] 31 | 27.93% [AM3.2] | 5 4.50%   | [AA3.3] 14 | 12.61% |     |     |
| [SM3.2] 25 | 22.52% [AM3.4] | 9 8.11%   |            |        |     |     |
| [SM3.3] 30 | 27.03% [AM3.5] | 12 10.81% |            |        |     |     |
| [SM3.4] 9  | 8.11%          |           |            |        |     |     |
| [SM3.5] 5  | 4.50%          |           |            |        |     |     |
SECURITY FEATURES &
| COMPLIANCE & POLICY |     |     | CODE REVIEW |     | SOFTWARE ENVIRONMENT |     |
| ------------------- | --- | --- | ----------- | --- | -------------------- | --- |
DESIGN
[CP1.1] 88 79.28% [SFD1.1] 85 76.58% [CR1.2] 75 67.57% [SE1.1] 73 65.77%
[CP1.2] 94 84.68% [SFD1.2] 77 69.37% [CR1.4] 95 85.59% [SE1.2] 96 86.49%
[CP1.3] 92 82.88% [SFD2.1] 44 39.64% [CR1.5] 74 66.67% [SE1.3] 79 71.17%
[CP2.1] 46 41.44% [SFD2.2] 62 55.86% [CR1.7] 47 42.34% [SE1.4] 69 62.16%
[CP2.2] 56 50.45% [SFD3.1] 16 14.41% [CR2.6] 29 26.13% [SE2.4] 52 46.85%
[CP2.3] 63 56.76% [SFD3.2] 22 19.82% [CR2.7] 19 17.12% [SE2.5] 59 53.15%
[CP2.4] 61 54.95% [SFD3.3] 11 9.91% [CR2.8] 28 25.23% [SE2.7] 40 36.04%
| [CP2.5] 68 | 61.26% |               | [CR3.2] 18 | 16.22% | [SE3.2] 25             | 22.52% |
| ---------- | ------ | ------------- | ---------- | ------ | ---------------------- | ------ |
| [CP3.1] 40 | 36.04% |               | [CR3.3] 8  | 7.21%  | [SE3.3] 22             | 19.82% |
| [CP3.2] 41 | 36.94% |               | [CR3.4] 3  | 2.70%  | [SE3.6] 31             | 27.93% |
| [CP3.3] 15 | 13.51% |               | [CR3.5] 4  | 3.60%  | [SE3.8] 8              | 7.21%  |
|            |        |               |            |        | [SE3.9] 13             | 11.71% |
|            |        |               |            |        | [SE3.10] 6             | 5.41%  |
|            |        | STANDARDS &   |            |        | CONFIG. MGMT. & VULN.  |        |
TRAINING SECURITY TESTING
REQUIREMENTS MGMT.
[T1.1] 61 54.95% [SR1.1] 82 73.87% [ST1.1] 93 83.78% [CMVM1.1] 106 95.50%
[T1.7] 61 54.95% [SR1.2] 88 79.28% [ST1.3] 66 59.46% [CMVM1.2] 76 68.47%
[T1.8] 52 46.85% [SR1.3] 77 69.37% [ST1.4] 47 42.34% [CMVM1.3] 82 73.87%
[T2.5] 30 27.03% [SR1.5] 88 79.28% [ST2.4] 20 18.02% [CMVM1.4] 86 77.48%
[T2.8] 25 22.52% [SR2.2] 65 58.56% [ST2.5] 30 27.03% [CMVM2.3] 38 34.23%
[T2.9] 30 27.03% [SR2.5] 62 55.86% [ST2.6] 28 25.23% [CMVM2.4] 53 47.75%
[T2.10] 21 18.92% [SR2.7] 53 47.75% [ST3.3] 15 13.51% [CMVM3.1] 16 14.41%
[T2.11] 30 27.03% [SR3.2] 17 15.32% [ST3.4] 6 5.41% [CMVM3.2] 27 24.32%
[T2.12] 45 40.54% [SR3.3] 19 17.12% [ST3.5] 9 8.11% [CMVM3.3] 29 26.13%
[T3.1] 8 7.21% [SR3.4] 26 23.42% [ST3.6] 10 9.01% [CMVM3.4] 34 30.63%
| [T3.2] 21 | 18.92% [SR3.5] | 2 1.80% |     |     | [CMVM3.5] 24 | 21.62% |
| --------- | -------------- | ------- | --- | --- | ------------ | ------ |
| [T3.6] 8  | 7.21%          |         |     |     | [CMVM3.6] 5  | 4.50%  |
|           |                |         |     |     | [CMVM3.8] 3  | 2.70%  |
Figure 18. BSIMM16 SCORECARD. This scorecard shows how often we observed each of the BSIMM16 activities in the data pool of 111 firms.
| BSIMM16 |     |     |     |     |     | 56  |
| ------- | --- | --- | --- | --- | --- | --- |

COMMON ACTIVITIES AND ACTIVITY
BSIMM16 TOP 20 ACTIVITIES BY PERCENTAGE
CHANGES OVER TIME
|     |     |     | [CMVM1.1] | Create or interface with  | 95.5% |
| --- | --- | --- | --------- | ------------------------- | ----- |
The popular business book, The 7 Habits of Highly Effective  incident response.
People, explores the theory that successful individuals share
|     |     |     | [SM1.4] | Implement security  | 90.1% |
| --- | --- | --- | ------- | ------------------- | ----- |
common qualities in achieving their goals and that these qualities
checkpoints and associated
can be identified and applied by others. The same premise can  governance.
also be applied to SSIs. Table 10 lists the 20 most observed
|     |     |     | [SE1.2] | Ensure host and network  | 86.5% |
| --- | --- | --- | ------- | ------------------------ | ----- |
activities in the BSIMM16 data pool. The data suggests that if
security basics are in place.
your organization is working on its own SSI, you should consider
|     |     |     | [CR1.4] | Use automated code review  | 85.6% |
| --- | --- | --- | ------- | -------------------------- | ----- |
implementing these activities. As a reminder of how practices
tools.
and activity labeling works, activity [SM1.4] is from the Strategy
|     |     |     | [PT1.1] | Use external penetration  | 85.6% |
| --- | --- | --- | ------- | ------------------------- | ----- |
& Metrics practice, and it was observed in 90.1% of the 111  testers to find problems.
BSIMM16 participant organizations.
|     |     |     | [CP1.2] | Identify privacy obligations. | 84.7% |
| --- | --- | --- | ------- | ----------------------------- | ----- |
Instead of the top 20 activities overall, Table 11 shows the most
|     |     |     | [ST1.1] | Perform edge/boundary  | 83.8% |
| --- | --- | --- | ------- | ---------------------- | ----- |
common activity in each BSIMM practice. Although we can’t
value condition testing
directly conclude that these 12 activities are necessary for all  during QA.
SSIs, we can say with confidence that they’re commonly found in
|     |     |     | [CP1.3] | Create policy. | 82.9% |
| --- | --- | --- | ------- | -------------- | ----- |
initiatives whose efforts span all 12 practices. This suggests that if
|     |     |     | [AA1.1] | Perform security feature  | 80.2% |
| --- | --- | --- | ------- | ------------------------- | ----- |
an organization is working on an initiative of its own, its efforts will
review.
likely include the majority of these 12 activities over time. Simply
|     |     |     | [CP1.1] | Unify regulatory pressures. | 79.3% |
| --- | --- | --- | ------- | --------------------------- | ----- |
put, Table 10 and Table 11 can help you understand what most
firms are already doing and discover potential gaps in your own  [SR1.2] Create a security portal. 79.3%
| program.  |     |     | [SR1.5] | Identify open source. | 79.3% |
| --------- | --- | --- | ------- | --------------------- | ----- |
In addition to looking at the most common activities, we can also  [PT1.2] Feed results to the defect  78.4%
analyze the fastest-growing activity observation rates between  management and mitigation
system.
BSIMM15 and BSIMM16. Level 1 BSIMM activities are the most
common activities observed in each practice, and in BSIMM16, 20  [CMVM1.4] Have emergency response. 77.5%
of the level 1 activities still saw positive growth despite a decline in  [SFD1.1] Integrate and deliver  76.6%
the BSIMM data pool from 121 firms to 111.  security features.
|                                    |     |     | [SM1.1] | Publish process and evolve  | 75.7% |
| ---------------------------------- | --- | --- | ------- | --------------------------- | ----- |
| BSIMM16 TOP ACTIVITIES BY PRACTICE |     |     |         | as necessary.               |       |
[SM1.4] Implement security  90.1% [CMVM1.3] Track software defects  73.9%
|     | checkpoints and associated  |     |     | found in operations through  |     |
| --- | --------------------------- | --- | --- | ---------------------------- | --- |
|     | governance.                 |     |     | the fix process.             |     |
[CP1.2] Identify privacy obligations. 84.7% [SR1.1] Create security standards. 73.9%
[T1.1] Conduct software security  55.0% [SE1.3] Implement cloud security  71.2%
|         | awareness training.    |       |         | controls.              |       |
| ------- | ---------------------- | ----- | ------- | ---------------------- | ----- |
|         |                        |       | [AM1.5] | Gather and use attack  | 70.3% |
| [AM1.5] | Gather and use attack  | 70.3% |         |                        |       |
intelligence.
intelligence.
[SFD1.1] Integrate and deliver security  76.6% Table 10. TOP 20 ACTIVITIES BY OBSERVATION PERCENTAGE.
features. Shown here are the most observed activities in the BSIMM16 data pool
[SR1.2] Create a security portal. 79.3% of 111 firms. This frequent observation means that each activity has
broad applicability across a wide variety of SSIs.
| [AA1.1] | Perform security feature  | 80.2% |     |     |     |
| ------- | ------------------------- | ----- | --- | --- | --- |
review.
| [CR1.4] | Use automated code review  | 85.6% |     |     |     |
| ------- | -------------------------- | ----- | --- | --- | --- |
tools.
| [ST1.1] | Perform edge/boundary value  | 83.8% |     |     |     |
| ------- | ---------------------------- | ----- | --- | --- | --- |
condition testing during QA.
| [PT1.1] | Use external penetration  | 85.6% |     |     |     |
| ------- | ------------------------- | ----- | --- | --- | --- |
testers to find problems.
| [SE1.2] | Ensure host and network  | 86.5% |     |     |     |
| ------- | ------------------------ | ----- | --- | --- | --- |
security basics are in place.
| [CMVM1.1] | Create or interface with  | 95.5% |     |     |     |
| --------- | ------------------------- | ----- | --- | --- | --- |
incident response.
Table 11. MOST COMMON ACTIVITIES PER PRACTICE. This table
shows the most observed activity in each of the 12 BSIMM practices
for the entire data pool of 111.
BSIMM16 57

Another way to look at the growth of activities between BSIMM15  Finally, some extremely common activities continue to see growth,
and BSIMM16 is to look for trends, such as a high growth in  indicating that firms are still investing in foundational activities.
observation rates among common controls.  These extremely common activities are all level 1 activities and
observed at rates greater than the most common level 2 activities.
The greatest growth trends seen all grew at over 100%, but these
Remember that levels are determined by practice, so it is possible
were all level 3 activities and by definition the least common
to observe level 2 activities at greater rates in their practice than
activities seen, which gives them lots of room for growth. [SE3.9]
some level 1 activities in other practices (for example, [SR2.2] has
has the highest observation rate of the four, at 13 firms, but it is
been observed in 65 firms, while [T1.1], the most common activity
believed to actually be a fairly common activity that we have only
in the Training practices, has only been observed in 61 firms; see
been looking at since BSIMM14 was released, so we only have a
Figure 18). The six activities in Table 14 all continue to see growth,
few years’ data on it. The other three all have observation rates in
despite being very common.
the single digits (see Table 12).
VERY COMMON HIGH GROWTH
HIGH GROWTH ACTIVITIES
[SE3.9] Protect integrity of  1317.1% [AM1.5] Gather and use attack  10.4%
|         | development toolchains.    |        |         | intelligence.               |      |
| ------- | -------------------------- | ------ | ------- | --------------------------- | ---- |
|         |                            |        | [CR1.5] | Make code review mandatory  | 7.6% |
| [SM3.5] | Integrate software supply  | 445.0% |         |                             |      |
for all projects.
chain risk management.
|           |                    |        | [SM1.7] | Enforce security checkpoints  | 7.5% |
| --------- | ------------------ | ------ | ------- | ----------------------------- | ---- |
| [CMVM3.8] | Do attack surface  | 227.0% |         |                               |      |
and track exceptions.
management for deployed
|     | applications. |     | [CP1.3] | Create policy. | 6.7% |
| --- | ------------- | --- | ------- | -------------- | ---- |
[SE3.8] Perform application  190.7% [CMVM1.4] Have emergency response. 6.5%
composition analysis on code
|     |     |     | [SR1.1] | Create security standards. | 6.4% |
| --- | --- | --- | ------- | -------------------------- | ---- |
repositories.

Table 14. VERY COMMON ACTIVITIES THAT HAVE CONTUINUED TO
Table 12. FASTEST GROWING ACTIVITIES BY GROWTH PERCENTAGE.
SEE GROWTH.
Common activities also continue to grow, and among the activities
where at least half of the BSIMM16 data pool were observed doing
them, the six activities in Table 13 all saw strong growth.
COMMON HIGH GROWTH
| [PT2.3] | Schedule periodic penetration  | 19.7% |     |     |     |
| ------- | ------------------------------ | ----- | --- | --- | --- |
tests for application coverage.
| [AA1.4] | Use a risk methodology to  | 13.0% |     |     |     |
| ------- | -------------------------- | ----- | --- | --- | --- |
rank application.
| [CP2.4] | Include software security  | 10.8% |     |     |     |
| ------- | -------------------------- | ----- | --- | --- | --- |
SLAs in all vendor contracts.
| [AM1.5] | Gather and use attack  | 10.4% |     |     |     |
| ------- | ---------------------- | ----- | --- | --- | --- |
intelligence.
| [T1.7] | Deliver on-demand individual  | 9.0% |     |     |     |
| ------ | ----------------------------- | ---- | --- | --- | --- |
training.
| [SR2.5] | Create SLA boilerplate. | 9.0% |     |     |     |
| ------- | ----------------------- | ---- | --- | --- | --- |
Table 13. COMMON ACTIVITIES SEEING CONTINUED STRONG
GROWTH.
BSIMM16 58

PART 8:
| T H | E B | S   | I M | M   |
| --- | --- | --- | --- | --- |
| ACT | I V | IT  | I E | S   |

PART 8: THE BSIMM GOVERNANCE
ACTIVITIES
GOVERNANCE: STRATEGY & METRICS (SM)
The Strategy & Metrics practice encompasses planning, assigning
The BSIMM activities are the individual controls used to roles and responsibilities, identifying software security goals,
construct or improve an SSI. They range through people, determining budgets, and identifying metrics and software release
process, technology, and culture. You can use this information conditions.
to choose which controls to apply within your initiative, then
align your implementation strategy and metrics with your [SM1.1: 75.7%] PUBLISH PROCESS AND EVOLVE AS
desired outcomes. NECESSARY.
The process for addressing software security is defined, published
The BSIMM framework comprises four domains—Governance, internally, and broadcast to all stakeholders so that everyone
Intelligence, SSDL Touchpoints, and Deployment—and these knows the plan. Goals, roles, responsibilities, and activities
domains contain 12 practices, such as Strategy & Metrics, Attack are explicitly defined. Most organizations examine existing
Models, and Code Review, which themselves contain activities. methodologies, such as the NIST SSDF, Microsoft SDL, or Black
These activities are the BSIMM building blocks, the smallest unit Duck Touchpoints, then tailor them to meet their needs. Security
of software security granularity implemented to build SSIs. Rather activities will be adapted to software lifecycle processes (e.g.,
than prescriptively dictating a set of best practices, the BSIMM waterfall, Agile, CI/CD, DevOps), so activities will evolve with both
descriptively observes, quantifies, and documents the actual the organization and the security landscape. The process doesn’t
activities carried out in SSIs across diverse organizations. need to be publicly promoted outside the firm to have the desired
impact (see [SM3.2]). In addition to publishing the written process,
ACTIVITIES IN THE BSIMM some firms also automate parts (e.g., a testing strategy) as
governance-as-code (see [SM3.4]).
The BSIMM is a data-driven model that evolves over time. Over the
years, we have added, deleted, and adjusted the levels of various [SM1.3: 59.5%] EDUCATE EXECUTIVES ON
activities based on the data observed throughout the BSIMM’s SOFTWARE SECURITY.
evolution. When considering whether to add a new activity, we Executives are regularly shown the ways malicious actors attack
analyze whether the effort we’re observing is truly new to the software and the negative business impacts those attacks can
model or simply a variation on an existing activity. Similarly, for have on the organization. Go beyond reporting of open and
deciding whether to move an activity between levels within a closed defects to educate executives on the business risks,
practice, we use the results of an intra-level standard deviation including risks of adopting emerging engineering technologies and
analysis and the trend in observation counts. methodologies without security oversight. Demonstrate a worst-
Each activity has a unique label and name, e.g., activity [SM1.4] is case scenario in a controlled environment with the permission of
in the Strategy & Metrics practice and is named Implement security all involved (e.g., by showing attacks and their business impact).
checkpoints and associated governance. To preserve backward Presentation to the board can help garner resources for new or
compatibility, we make all changes by adding new activity labels to ongoing SSI efforts. Demonstrating the need for new skill-building
the model, even when an activity has simply changed levels within training in evolving areas, such as DevOps groups using cloud-
a practice (as an example, we would add a new CR#.# label for native technologies, can help convince leadership to accept SSG
both new and moved activities in the Code Review practice). recommendations when they might otherwise be ignored in favor
of faster release dates or other priorities. Bring in an outside expert
BSIMM activity levels distinguish the frequency with which
when necessary to bolster executive attention.
activities are observed in the participating organizations. As seen
in Part 7, frequently observed activities are designated level 1, with [SM1.4: 90.1%] IMPLEMENT SECURITY
less frequent and infrequently observed activities designated as CHECKPOINTS AND ASSOCIATED
levels 2 and 3, respectively. Using [SM1.4] as an example again, GOVERNANCE.
we see that it is a frequently observed activity in the Strategy &
The software security process includes checkpoints
Metrics practice. Note that the new activities we add to the model
(such as gates, release conditions, guardrails,
start with zero observations and are therefore always added at
milestones, etc.) at one or more points in a software lifecycle. The
level 3.
first two steps toward establishing security-specific checkpoint
conditions are to identify process locations that are compatible
with existing development practices and to then begin gathering
the information necessary, such as risk-ranking thresholds
or defect data, to make a go/no-go decision. Importantly, the
conditions need not be enforced at this stage, e.g., the SSG can
collect security testing results for each project prior to release,
Top 10 Activity Assists with then provide an informed opinion on what constitutes sufficient
in BSIMM15 Adopting AI/ML testing or acceptable test results without trying to stop a project
from moving forward (see [SM1.7]). Shorter release cycles might
To help understand the “Assists with Adopting” AI/ML activities, require creative approaches to collecting the right evidence and
see AI/ML and BSIMM16 in Part 3. rely heavily on automation. Socializing the conditions and then
BSIMM16 60
Adopting AI/ML Assists with

enforcing them once most project teams already know how to The champions can act as a sounding board for new projects
succeed is a gradual approach that motivates good behavior and, in new or fast-moving technology areas, can help combine
without introducing unnecessary friction. software security skills with domain knowledge that might be
under-represented in the SSG or engineering teams. Agile coaches,
[SM1.7: 64.0%] ENFORCE SECURITY CHECKPOINTS
scrum masters, and DevOps engineers can make particularly
AND TRACK EXCEPTIONS. useful champions members, especially for detecting and removing
Enforce security release conditions at each checkpoint (gate, process friction. In some environments, champions-led efforts are
guardrail, milestone, etc.) for every project, so that each project delivered via automation (e.g., as-code).
must either meet an established measure or follow a defined
[SM2.6: 55.9%] REQUIRE SECURITY SIGN-OFF PRIOR
process for obtaining an exception to move forward. Use internal
TO SOFTWARE RELEASE.
policies and standards, regulations, contractual agreements,
and other obligations to define release conditions, then track all The organization has an initiative-wide process for documenting
exceptions. Verifying conditions yields data that informs the KRIs accountability and accepting security risk by having a risk
and any other metrics used to govern the process. Automatically owner use SSG-approved criteria to sign off on the state of
giving software a passing grade or granting exceptions without due all software prior to release. The sign-off policy might also
consideration defeats the purpose of verifying conditions. Even require the accountable person to, e.g., acknowledge critical
seemingly innocuous software projects (e.g., small code changes, vulnerabilities that have not been mitigated or SSDL steps that
infrastructure access control changes, deployment blueprints) have been skipped. Informal or uninformed risk acceptance
must successfully satisfy the prescribed security conditions as they alone isn’t a security sign-off because the act of accepting risk
progress through the software lifecycle. Similarly, APIs, frameworks, is more effective when it’s formalized (e.g., with a signature, a
libraries, bespoke code, microservices, container configurations, form submission, or something similar) and captured for future
etc., are all software that must satisfy security release conditions. reference. Similarly, simply stating that certain projects don’t need
It’s possible, and often very useful, to have verified the conditions sign-off at all won’t achieve the desired risk management results.
both before and after the development process itself. In In some cases, however, the risk owner can provide the sign-off on
modern development environments, the verification process will a particular set of software project acceptance criteria, which are
increasingly become automated (see [SM3.4]). then implemented in automation to provide governance-as-code
(see [SM3.4]), but there must be an ongoing verification that the
[SM2.1: 48.6%] PUBLISH DATA ABOUT SOFTWARE
criteria remain accurate and the automation is working.
SECURITY INTERNALLY AND USE IT TO DRIVE
CHANGE. [SM2.7: 44.1%] CREATE EVANGELISM ROLE AND
PERFORM INTERNAL MARKETING.
To facilitate improvement, data is published internally about
the state of software security within the organization. Produce Build support for software security throughout the organization via
security or development dashboards with metrics for executives ongoing evangelism and ensure that everyone aligns on security
and software development management. Dashboards can be objectives. This internal marketing function, often performed by
part of pipeline toolchains to enable developer self-improvement. a variety of stakeholder roles, keeps executives and others up to
Sometimes, this published data won’t be shared with everyone date on the magnitude of the software security problem and the
in the firm but only with the stakeholders who are tasked to elements of its solution. A champion or a scrum master familiar
drive change. In other cases, open book management and data with security, for example, could help teams adopt better software
published to all stakeholders helps everyone know what’s going on. security practices as they transform to Agile and DevOps methods.
If the organization’s culture promotes internal competition between Similarly, a cloud expert could demonstrate the changes needed
groups, use this information to add a security dimension. Integrate in security architecture and testing for serverless applications.
automated security telemetry to gather measurements quickly and Evangelists can increase understanding and build credibility by
accurately to increase timeliness of security data in areas such as giving talks to internal groups (including executives), publishing
speed (e.g., time to fix) and quality (e.g., defect density). Publishing roadmaps, authoring technical papers for internal consumption,
data about new technologies (e.g., security and risk in cloud-native or creating a collection of papers, books, and other resources on
architectures) is important for identifying needed improvements. an internal website (see [SR1.2]) and promoting its use. In turn,
organizational feedback becomes a useful source of improvement
[SM2.3: 49.5%] CREATE OR GROW A SECURITY ideas.
CHAMPIONS PROGRAM.
[SM3.1: 27.9%] USE A SOFTWARE ASSET TRACKING
Form a collection of people scattered across the organization—
APPLICATION WITH PORTFOLIO VIEW.
often called security champions—who show an above-average
level of security interest or skill and who contribute software The SSG uses centralized tracking automation to chart the
security expertise to development, QA, and operations teams. progress of every piece of software and deployable artifact,
Forming this social network of advocates is a good step toward from creation to decommissioning, regardless of development
scaling security into software engineering. One way to build methodology. The automation records the security activities
the initial group is to track the people who stand out during scheduled, in progress, and completed, incorporating results from
introductory training courses (see [T3.6]). Another way is to ask SSDL activities even when they happen in a tight loop or during
for volunteers. In a more top-down approach, initial champions deployment. The combined inventory and security posture view
membership is assigned to ensure good coverage of development enables timely decision-making. The SSG uses the automation to
groups, but ongoing membership is based on actual performance. generate portfolio reports for multiple metrics and, in many cases,
BSIMM16 61

publishes this data at least among executives. As an initiative [SM3.5: 4.5%] INTEGRATE SOFTWARE
matures and activities become more distributed, the SSG uses the SUPPLY CHAIN RISK MANAGEMENT.
centralized reporting system to keep track of all the moving parts.
Organizational risk management processes ensure
that important software created by and entering the
[SM3.2: 22.5%] MAKE SSI EFFORTS PART OF
organization is managed through policy-driven access and usage
EXTERNAL MARKETING.
controls, maintenance standards (see [SE3.9]), and captured
To build external awareness, the SSG helps market the SSI
software provenance data (see [SE2.4]). Apply these processes to
beyond internal teams. The process of sharing details externally
external (see [SR2.7]), bespoke, and internally developed software
and inviting critique is used to bring new perspectives into the
(see [SE3.9]) to help ensure that deployed code has the expected
firm. Promoting the SSDL externally can turn security efforts into
components (see [SE3.8]). The lifecycle management for all
a market differentiator, and feedback from external marketing
software, from creation or importation through secure deployment,
can grow an SSI’s risk reduction exercises into a competitive
ensures that all access, usage, and modifications are done in
advantage. The SSG might provide details at external conferences
accordance with policy. This assurance is easier to implement
or trade shows. In some cases, a complete SSDL methodology can
at scale using automation in software lifecycle processes (see
be published and promoted outside the firm, and governance-as-
[SM3.4]).
code concepts can make interesting case studies.
GOVERNANCE: COMPLIANCE & POLICY (CP)
[SM3.3: 27.0%] IDENTIFY METRICS AND USE THEM
The Compliance & Policy practice is focused on identifying
TO DRIVE RESOURCING.
controls for compliance regimens such as PCI DSS and GDPR,
The SSG and its management identify metrics that define and developing contractual controls such as SLAs to help manage
measure SSI progress in quantitative terms. These metrics are COTS risk, setting organizational software security policy, and
reviewed on a regular basis and drive the initiative’s budgeting auditing against that policy.
and resource allocations, so simple counts and out-of-context
measurements won’t suffice here. On the technical side, one such [CP1.1: 79.3%] UNIFY REGULATORY
metric could be defect density, a reduction of which could be used PRESSURES.
to show a decreasing cost of remediation over time, assuming, of
Have a cross-functional team that understands
course, that testing depth has kept pace with software changes.
the constraints imposed on software security
Data for metrics is best collected early and often using event-
by regulatory or compliance drivers that are applicable to the
driven processes with telemetry rather than relying on calendar-
organization and its customers. The team takes a common
driven data collection. The key is to tie security results to business
approach that removes redundancy and conflicts to unify
objectives in a clear and obvious fashion to justify resourcing.
compliance requirements, such as from PCI security standards;
Because the concept of security is already tenuous to many
GLBA, SOX, and HIPAA in the US; or GDPR in the EU. A formal
businesspeople, make the tie-in explicit.
approach will map applicable portions of regulations to controls
(see [CP2.3]) applied to software to explain how the organization
[SM3.4: 8.1%] INTEGRATE SOFTWARE-DEFINED
complies. Existing business processes run by legal, product
LIFECYCLE GOVERNANCE.
management, or other risk and compliance groups outside the
Organizations begin replacing traditional document-, presentation-, SSG could serve as the regulatory focal point, with the SSG
and spreadsheet-based lifecycle management with software- providing software security knowledge. A unified set of software
based delivery platforms. For some software lifecycle phases, security guidance for meeting regulatory pressures ensures that
humans are no longer the primary drivers of progression from one compliance work is completed as efficiently as possible.
phase to the next. Instead, organizations rely on automation to
drive the management and delivery process with software such as [CP1.2: 84.7%] IDENTIFY PRIVACY
Spinnaker or GitHub, and humans participate asynchronously (and OBLIGATIONS.
often optionally). Automation often extends beyond the scope of
The SSG identifies privacy obligations stemming
CI/CD to include functional and nonfunctional aspects of delivery,
from regulation and customer expectations, then
such as health checks, cut-over on failure, rollback to known-good
translates these obligations into both software requirements
state, defect discovery and management, compliance verification,
and privacy best practices. The way software handles PII might
and a way to ensure adherence to policies and standards. Some
be explicitly regulated, but even if it isn’t, privacy is an important
organizations are also evolving their lifecycle management
topic. For example, if the organization processes credit card
approach by integrating their compliance and defect discovery
transactions, the SSG will help in identifying the privacy constraints
data, perhaps augmented by intelligence feeds and other external
that the PCI DSS places on the handling of cardholder data and
data, to begin moving from a series of point-in-time go/no-go
will inform all stakeholders (see [SR1.3]). Note that outsourcing
decisions (e.g., release conditions) to a future state of continuous
to hosted environments (e.g., the cloud) doesn’t relax privacy
accumulation of assurance data (see [CMVM3.6]).
obligations and can even increase the difficulty of recognizing
and meeting all associated needs. Also, note that firms creating
software products that process PII when deployed in customer
environments might meet this need by providing privacy controls
and guidance for their customers. Evolving consumer privacy
expectations, the proliferation of “software is in everything,” and
data scraping and correlation (e.g., social media) add additional
expectations and complexities for PII protection.
BSIMM16 62

[CP1.3: 82.9%] CREATE POLICY. automation to provide governance as-code, there must be ongoing
verification that the criteria remain accurate and the automation is
The SSG guides the organization by creating or
actually working.
contributing to software security policies that
satisfy internal, regulatory, and customer-driven
[CP2.3: 56.8%] IMPLEMENT AND TRACK CONTROLS
security requirements. This policy is what is permitted and denied
FOR COMPLIANCE.
at the initiative level—if it’s not mandatory and enforced, it’s not
policy. The policies include a unified approach for satisfying the The organization can demonstrate compliance with applicable
(potentially lengthy) list of security drivers at the governance requirements because its SSDL is aligned with the control
level so that project teams can avoid keeping up with the details statements that were developed by the SSG in collaboration with
involved in complying with all applicable regulations or other compliance stakeholders (see [CP1.1]). The SSG collaborates
mandates. Likewise, project teams won’t need to relearn customer with stakeholders to track controls, navigate problem areas, and
security requirements on their own. Architecture standards ensure that auditors and regulators are satisfied. The SSG can
and coding guidelines aren’t examples of policy, but policy that then remain in the background when the act of following the
prescribes and mandates their use for certain software categories SSDL automatically generates the desired compliance evidence
falls under this umbrella. In many cases, policy statements are predictably and reliably. Increasingly, the DevOps approach
translated into automation to provide governance-as-code. Even if embeds compliance controls in automation, such as in software-
not enforced by humans, policy that’s been automated must still be defined infrastructure and networks, rather than in human process
mandatory. In some cases, policy will be documented exclusively and manual intervention. A firm doing this properly can explicitly
as governance as-code (see [SM3.4]), often as tool configuration, associate satisfying its compliance concerns with following its
but it must still be readily readable, auditable, and editable by SSDL.
humans.
[CP2.4: 55.0%] INCLUDE SOFTWARE SECURITY SLAs
[CP2.1: 41.4%] BUILD A PII INVENTORY. IN ALL VENDOR CONTRACTS.
The organization identifies and tracks the kinds of PII processed Software vendor contracts include an SLA to ensure that the
or stored by each of its systems, along with their associated vendor’s security efforts align with the organization’s security
data repositories. In general, simply noting which applications and compliance story. Each new or renewed contract contains
process PII isn’t enough—the type of PII (e.g., PHI, PFI, PI) and provisions requiring the vendor to address software security and
where it’s stored are necessary so that the inventory can be easily deliver a product or service compatible with the organization’s
referenced in critical situations. This usually includes making a list security policy. In some cases, open source licensing concerns
of databases that would require customer notification if breached initiate the vendor management process, which can open the door
or a list to use in crisis simulations (see [CMVM3.3]). Build the PII for additional software security language in the SLA (see [SR2.5]).
inventory by starting with each individual application and noting Typical provisions set requirements for policy conformance,
its PII use or by starting with PII types and noting the applications incident management, training, defect management, and response
that touch each one. System architectures have evolved such times for addressing software security issues. Traditional IT
that PII will often flow into cloud-based service and endpoint security requirements and a simple agreement to allow penetration
device ecosystems, then come to rest there (e.g., content delivery testing or another defect discovery method aren’t sufficient here.
networks, workflow systems, mobile devices, IoT devices), making
[CP2.5: 61.3%] ENSURE EXECUTIVE AWARENESS OF
it tricky to keep an accurate PII inventory.
COMPLIANCE AND PRIVACY OBLIGATIONS.
[CP2.2: 50.5%] REQUIRE SECURITY SIGN-OFF FOR Gain buy-in around compliance and privacy obligations by
COMPLIANCE-RELATED RISK. providing executives with plain-language explanations of both
The organization has a formal compliance risk acceptance the organization’s compliance and privacy requirements and the
sign-off and accountability process that addresses all software potential consequences of failing to meet those requirements. For
development projects. In this process, the SSG acts as an advisor some organizations, explaining the direct cost and likely fallout
while the risk owner signs off on the software’s compliance state from a compliance failure or data breach can be an effective way
prior to release based on its adherence to documented criteria. The to broach the subject. For others, having an outside expert address
sign-off policy might also require the head of the business unit to, the board works because some executives value an outside
e.g., acknowledge compliance issues that haven’t been mitigated perspective more than an internal one. A sure sign of proper
or compliance-related SSDL steps that have been skipped, but executive buy-in is an acknowledgment of the need along with
sign-off is required even when no compliance-related risk is adequate allocation of resources to meet those obligations. Use
present. Sign-off is explicit and captured for future reference, with the sense of urgency that typically follows a compliance or privacy
any exceptions tracked, even in automated application lifecycle failure to build additional awareness and bootstrap new efforts.
methodologies. Note that an application without security defects
[CP3.1: 36.0%] DOCUMENT A SOFTWARE
might still be noncompliant, so clean security testing results
COMPLIANCE STORY.
are not a substitute for a compliance sign-off. Even in DevOps
organizations where engineers have the technical ability to release The SSG can demonstrate the organization’s up-to-date software
software, there is still a need for a deliberate risk acceptance step security compliance story on demand. A compliance story is a
even if the compliance criteria are embedded in automation (see collection of data, artifacts, policy controls, or other documentation
[SM3.4]). In cases where the risk owner signs off on a particular that shows the compliance state of the organization’s software
set of compliance acceptance criteria that are then implemented in and processes. Often, senior management, auditors, and
BSIMM16 63

regulators—whether government or other—will be satisfied with the members, security champions, an outside firm, the internal training
same kinds of reports that can be generated directly from various organization, or e-learning, but course content isn’t necessarily
tools. In some cases, particularly where organizations leverage tailored for a specific audience—developers, QA engineers, and
shared responsibility through cloud services, the organization project managers could attend the same “Introduction to Software
will require additional information from vendors about how that Security” course, for example. Augment this content with a tailored
vendor’s controls support organizational compliance needs. It approach that addresses the firm’s culture explicitly, which might
will often be necessary to normalize information that comes from include the process for building security in, avoiding common
disparate sources. mistakes, and technology topics such as CI/CD and DevSecOps.
Generic introductory courses that only cover basic IT or high-level
[CP3.2: 36.9%] ENSURE COMPATIBLE VENDOR
security concepts don’t generate satisfactory results. Likewise,
POLICIES. awareness training aimed only at developers and not at other roles
Ensure that vendor software security policies and SSDL in the organization is insufficient.
processes are compatible with internal policies. Vendors likely
[T1.7: 55.0%] DELIVER ON-DEMAND INDIVIDUAL
comprise a diverse group—cloud providers, middleware providers,
TRAINING.
virtualization providers, container and orchestration providers,
bespoke software creators, contractors, and many more—and each The organization lowers the burden on students and reduces
might be held to different policy requirements. Policy adherence the cost of delivering software security training by offering
enforcement might be through a point-in-time review (such as on-demand training for SSDL stakeholders. The most obvious
ensuring acceptance criteria), automated checks (such as those choice, e-learning, can be kept up to date through a subscription
applied to pull requests, committed artifacts like containers, or model, but an online curriculum must be engaging and relevant
similar), or convention and protocol (such as preventing services to students in various roles (e.g., developer, QA, cloud, ops) to
connection unless security settings are correct and expected achieve its intended purpose. Ineffective (e.g., aged, off-topic)
certificates are present). Evidence of vendor adherence could training or training that isn’t used won’t create any change. Hot
include results from SSDL activities, from manual tests or tests engineering topics like containerization and security orchestration,
built directly into automation or infrastructure, or from other and new training delivery styles such as gamification, will attract
software lifecycle instrumentation. For some policies or SSDL more interest than boring policy discussions. For developers, it’s
processes, vendor questionnaire responses and attestation alone possible to provide training directly through the IDE right when
might be sufficient. it’s needed, but in some cases, building a new skill (such as cloud
security or threat modeling) might be better suited for instructor-
[CP3.3: 13.5%] DRIVE FEEDBACK FROM SOFTWARE
led training, which can also be provided on demand.
LIFECYCLE DATA BACK TO POLICY.
[T1.8: 46.9%] INCLUDE SECURITY RESOURCES IN
Feed information from the software lifecycle into the policy
ONBOARDING.
creation and maintenance process to drive improvements, such
as in defect prevention and strengthening governance-as-code The process for bringing new hires into a software engineering
practices (see [SM3.4]). With this feedback as a routine process, organization requires timely completion of a training module
blind spots can be eliminated by mapping them to trends in SSDL about software security. While the generic new hire process
failures. Events such as the regular appearance of inadequate usually covers topics like picking a good password and avoiding
architecture analysis, recurring vulnerabilities, ignored security phishing, this orientation period is enhanced to cover topics such
release conditions, or the wrong vendor choice for carrying out as how to create, deploy, and operate secure code, the SSDL,
a penetration test can expose policy weakness (see [CP1.3]). security standards (see [SR1.1]), and internal security resources
As an example, lifecycle data including KPIs, OKRs, KRIs, SLIs, (see [SR1.2]). The objective is to ensure that new hires contribute
SLOs, or other organizational metrics can indicate where policies to the security culture as soon as possible. Although a generic
impose too much bureaucracy by introducing friction that prevents onboarding module is useful, it doesn’t take the place of a timely
engineering from meeting the expected delivery cadence. Rapid and more complete introductory software security course.
technology evolution might also create policy gaps that must be
[T2.5: 27.0%] ENHANCE SECURITY CHAMPIONS
addressed. Over time, policies become more practical and easier
to carry out (see [SM1.1]). Ultimately, policies are refined with THROUGH TRAINING AND EVENTS.
SSDL data to enhance and improve effectiveness. Strengthen the security champions network (see [SM2.3])
by inviting guest speakers or holding special events about
GOVERNANCE: TRAINING (T)
advanced software security topics. This effort is about providing
Training has always played a critical role in software security to the champions customized training (e.g., the latest software
because organizational stakeholders across GRC, legal, security techniques for DevOps or serverless technologies or
engineering, operations, and other groups often start with little on the implications of new policies and standards) so that it
security knowledge. can fulfill its assigned responsibilities—it’s not about inviting
champions members to routine brown bags or signing them
[T1.1: 55.0%] CONDUCT SOFTWARE SECURITY
up for standard computer-based training. Similarly, a standing
AWARENESS TRAINING.
conference call with voluntary attendance won’t get the desired
To promote a culture of software security throughout the results, which are as much about building camaraderie as they
organization, the SSG conducts periodic software security are about sharing knowledge and organizational efficiency.
awareness training. This training might be delivered via SSG Regular events build community and facilitate collaboration and
BSIMM16 64

collective problem-solving. Face-to-face meetings are by far the that the organization doesn’t lose focus due to turnover, evolving
most effective, even if they happen only once or twice a year and methodologies, or changing deployment models. The SSG might
even if some participants must attend by videoconferencing. In give an update on the security landscape and explain changes to
teams with many geographically dispersed and work-from-home policies and standards. A refresher could also be rolled out as part
members, simply turning on cameras and ensuring that everyone of a firmwide security day or in concert with an internal security
gets a chance to speak makes a substantial difference. conference. While one refresher module can be used for multiple
roles (see [T2.9]), coverage of new topics and changes to the
[T2.8: 22.5%] CREATE AND USE MATERIAL SPECIFIC
previous year’s content should result in a significant amount of
TO COMPANY HISTORY. fresh content.
To make a strong and lasting change in behavior, training includes
[T2.12: 40.5%] PROVIDE EXPERTISE VIA OPEN
material specific to the company’s history of software security
COLLABORATION CHANNELS.
challenges. When participants can see themselves in a problem,
they’re more likely to understand how the material is relevant Software security experts offer help to anyone in an open manner
to their work as well as when and how to apply what they’ve during regularly scheduled office hours or openly accessible
learned. One way to do this is to use noteworthy attacks on the channels on Slack, Jira, or similar. By acting as an informal
company’s software as examples in the training curriculum. Both resource for people who want to solve security problems, the SSG
successful and unsuccessful attacks, as well as notable results leverages teachable moments and emphasizes the carrot over the
from penetration tests, design review, and red team exercises, can stick approach to security best practices. Office hours might be
make good teachable moments. Stories from company history can hosted one afternoon per week by a senior SSG member, perhaps
help steer training in the right direction but only if those stories inviting briefings from product or application groups working on
are still relevant and not overly censored. This training should hard security problems. Slack and other messaging applications
cover platforms used by developers (developers orchestrating can capture questions 24x7, functioning as an office hours
containers probably won’t care about old virtualization problems) platform when appropriate subject matter experts are consistently
and problems relevant to languages in common use. part of the conversation and are ensuring that the answers
generated align with SSG expectations. An online approach has the
[T2.9: 27.0%] DELIVER ROLE-SPECIFIC ADVANCED
added benefit of discussions being recorded and searchable.
CURRICULUM.
[T3.1: 7.2%] REWARD PROGRESSION THROUGH
Software security training goes beyond building awareness (see
CURRICULUM.
[T1.1]) to enabling students to incorporate security practices into
their work. This training is tailored to cover the tools, technology Progression through the security curriculum brings personal
stacks, development methodologies, and issues that are most benefits, such as public acknowledgement or career advancement.
relevant to the students. An organization could offer tracks for The reward system can be formal and lead to a certification or
its engineers, for example, supplying one each for architects, an official mark in the human resources system, or it can be less
developers, operations, DevOps, site reliability engineers, and formal and include motivators such as documented praise at
testers. Tool-specific training is also commonly needed in such annual review time. Involving a corporate training department
a curriculum. While it might be more concise than engineering and human resources team can make the impact of improving
training, role-specific training is also necessary for many security skills on career progression more obvious, but the SSG
other stakeholders within an organization, including product should continue to monitor security knowledge in the firm and
management, executives, and others. In any case, the training not cede complete control or oversight. Coffee mugs and t-shirts
must be taken by a broad enough audience to build the collective can build morale, but it usually takes the possibility of real career
skillsets required. progression to change behavior.
[T2.10: 18.9%] HOST SOFTWARE SECURITY EVENTS. [T3.2: 18.9%] PROVIDE TRAINING FOR VENDORS
The organization hosts security events featuring external speakers AND OUTSOURCED WORKERS.
and content in order to strengthen its security culture. Good Vendors and outsourced workers receive appropriate software
examples of such events are Intel iSecCon and AWS re:Inforce, security training, comparable to the level of training given to
which invite all employees, feature external presenters, and focus employees. Spending time and effort helping suppliers get security
on helping engineering create, deploy, and operate better code. right at the outset is much easier than trying to determine what
Employees benefit from hearing outside perspectives, especially went wrong later, especially if the development team has moved
those related to fast-moving technology areas with software on to other projects. Training individual contractors is much more
security ramifications, and the organization benefits from putting natural than training entire outsourced firms and is a reasonable
its security credentials on display (see [SM3.2]). Events open place to start. It’s important that everyone who works on the firm’s
only to small, select groups or simply putting recordings on an software has an appropriate level of training that increases their
internal portal won’t result in the desired culture change across the capability of meeting the software security expectations for their
organization. role, regardless of their employment status. Of course, some
vendors and outsourced workers might have received adequate
[T2.11: 27.0%] REQUIRE AN ANNUAL REFRESHER.
training from their own firms, but that should always be verified.
Everyone involved in the SSDL is required to take an annual
software security refresher course. This course keeps the staff
up to date on the organization’s security approach and ensures
BSIMM16 65

[T3.6: 7.2%] IDENTIFY NEW SECURITY CHAMPIONS [AM1.5: 70.3%] GATHER AND USE ATTACK
THROUGH OBSERVATION. INTELLIGENCE.
Future security champions are recruited by noting people who The SSG ensures the organization stays ahead of
stand out during opportunities that show skill and enthusiasm, the curve by learning about new types of attacks and
such as training courses, office hours, capture-the-flag exercises, vulnerabilities, then adapts that information to the organization’s
hack-a-thons, etc., and then encouraging them to join the needs. Attack intelligence must be made actionable and useful for
champions. Pay particular attention to practitioners who are a variety of consumers, which might include developers, testers,
contributing things such as code, security configurations, or DevOps, security operations, and reliability engineers, among
defect discovery rules. The champions program often begins others. In many cases, a subscription to a commercial service can
as an assigned collection of people scattered across the provide a reasonable way of gathering basic attack intelligence
organization who show an above-average level of security related to applications, APIs, containerization, orchestration,
interest or advanced knowledge of new technology stacks and cloud environments, etc. Attending technical conferences and
development methodologies (see [SM2.3]). Identifying future monitoring attacker forums, then correlating that information
members proactively is a step toward creating a social network with what’s happening in the organization (perhaps by leveraging
that speeds the adoption of security into software development automation to mine operational logs and telemetry) helps everyone
and operations. A group of enthusiastic and skilled volunteers will learn more about emerging vulnerability exploitation.
be easier to lead than a group that is drafted.
[AM2.1: 18.0%] BUILD ATTACK PATTERNS AND
ABUSE CASES TIED TO POTENTIAL ATTACKERS.
INTELLIGENCE
The SSG works with stakeholders to build attack patterns and
INTELLIGENCE: ATTACK MODELS (AM) abuse cases tied to potential attackers (see [AM1.3]). Attack
patterns frequently contain details of the targeted asset, attackers,
Attack Models capture information used to think like an attacker,
goals, and the techniques used. These resources can be built
including threat modeling inputs, abuse cases, data classification,
from scratch or from standard sets, such as the MITRE ATT&CK
and technology-specific attack patterns.
framework, with the SSG adding to the pile based on its own attack
[AM1.2: 51.4%] USE A DATA CLASSIFICATION stories to prepare the organization for SSDL activities such as
SCHEME FOR SOFTWARE INVENTORY. design review and penetration testing. For example, a story about
an attack against a poorly designed cloud-native application could
Security stakeholders in an organization agree on a data
lead to a containerization attack pattern that drives a new type of
classification scheme and use it to inventory software, delivery
testing (see [ST3.5]). If a firm tracks the fraud and monetary costs
artifacts (e.g., containers), and associated persistent data stores
associated with specific attacks, this information can in turn be
according to the kinds of data processed or services called,
used to prioritize the process of building attack patterns and abuse
regardless of deployment model (e.g., on- or off-premises). Many
cases. Organizations will likely need to evolve both their attack
classification schemes are possible—one approach is to focus
pattern and abuse case creation prioritization and their content
on PII, for example. Depending on the scheme and the software
over time due to changing software architectures (e.g., zero trust,
involved, it could be easiest to first classify data repositories (see
cloud native, serverless), attackers, and technologies.
[CP2.1]), then derive classifications for applications according
to the repositories they use. Other approaches include data [AM2.6: 14.4%] COLLECT AND PUBLISH ATTACK
classification according to protection of intellectual property,
STORIES.
impact of disclosure, exposure to attack, relevance to GDPR, and
To maximize the benefit from lessons that don’t always come
geographic boundaries.
cheap, the SSG collects and publishes stories about attacks
[AM1.3: 39.6%] IDENTIFY POTENTIAL ATTACKERS. against the organization’s software. Both successful and
unsuccessful attacks can be noteworthy, and discussing historical
The SSG identifies potential attackers in order to understand and
information about software attacks has the added effect of
begin documenting their motivations and abilities. The outcome
grounding software security in a firm’s reality. This is particularly
of this periodic exercise could be a set of attacker profiles that
useful in training classes (see [T2.8]) to help counter a generic
includes outlines for categories of attackers and more detailed
approach that might be overly focused on other organizations’
descriptions for noteworthy individuals that are used in end-to-end
most common bug lists or outdated platform attacks. Hiding or
design review (see [AA1.2]). In some cases, a third-party vendor
overly sanitizing information about attacks from people building
might be contracted to provide this information. Specific and
new systems fails to garner any positive benefits from a negative
contextual attacker information is almost always more useful than
event.
generic information copied from someone else’s list. Moreover,
a list that simply divides the world into insiders and outsiders
[AM2.7: 16.2%] BUILD AN INTERNAL FORUM TO
won’t drive useful results. Identification of attackers should also
DISCUSS ATTACKS.
consider the organization’s evolving software supply chain, attack
The organization has an internal, interactive forum where the
surface, theoretical internal attackers, and contract staff.
SSG, champions, incident response, and others discuss attacks
and attack methods. The discussion serves to communicate
the attacker perspective to everyone, so it’s useful to include all
successful attacks here, regardless of attack source, such as
supply chain, internal, consultants, or bug bounty contributors.
BSIMM16 66

The SSG augments the forum with an internal communication technology stacks and coding languages evolve faster than
channel (see [T2.12]) that encourages subscribers to discuss vendors can innovate, creating tools and automation in-house
the latest information on publicly known incidents. Dissection might be the best way forward. In the DevOps world, these tools
of attacks and exploits that are relevant to a firm are particularly might be created by engineering and embedded directly into
helpful when they spur discussion of software, infrastructure, and toolchains and automation (see [ST3.6]).
other mitigations. Simply republishing items from public mailing
[AM3.4: 8.1%] CREATE TECHNOLOGY-
lists doesn’t achieve the same benefits as active and ongoing
discussions, nor does a closed discussion hidden from those SPECIFIC ATTACK PATTERNS.
creating code and configurations. Everyone should feel free to ask The SSG facilitates technology-specific attack pattern
questions and learn about vulnerabilities and exploits. creation by collecting and providing knowledge about
attacks relevant to the organization’s technologies. For example,
[AM2.8: 23.4%] HAVE A RESEARCH GROUP THAT
if the organization’s cloud software relies on a cloud vendor’s
DEVELOPS NEW ATTACK METHODS.
security apparatus (e.g., key and secrets management), the SSG
A research group works to identify and mitigate the impact of new or appropriate SMEs can help catalog the quirks of the crypto
classes of attacks and shares their knowledge with stakeholders. package and how it might be exploited. Attack patterns directly
Identification does not always require original research—the related to the security frontier (e.g., AI, serverless) can be useful
group might expand on an idea discovered by others. Doing this here as well. It’s often easiest to start with existing generalized
research in-house is especially important for early adopters of attack patterns to create the needed technology-specific ones,
new technologies and configurations so that they can discover but simply adding “for microservices” at the end of a generalized
potential weaknesses before attackers do. One approach is to pattern name, for example, won’t suffice.
create new attack methods that simulate persistent attackers
[AM3.5: 10.8%] MAINTAIN AND USE A TOP N
during goal-oriented red team exercises (see [PT3.1]). This isn’t a
penetration testing team finding new instances of known types of POSSIBLE ATTACKS LIST.
weaknesses, it’s a research group that innovates attack methods The SSG periodically digests the ever-growing list of applicable
and mitigation approaches. Example mitigation approaches attack types, creates a prioritized short list—the top N—and
include test cases, static analysis rules, attack patterns, standards, then uses the list to drive change. This initial list almost always
and policy changes. Some firms provide researchers time to follow combines input from multiple sources, both inside and outside the
through on their discoveries by using bug bounty programs or organization. Some organizations prioritize their list according to a
other means of coordinated disclosure (see [CMVM2.4]). Others perception of potential business loss while others might prioritize
allow researchers to publish their findings at conferences like DEF according to preventing successful attacks against their software.
CON to benefit everyone. The top N list doesn’t need to be updated with great frequency,
and attacks can be coarsely sorted. For example, the SSG might
[AM2.9: 19.8%] MONITOR AUTOMATED ASSET
brainstorm twice a year to create lists of attacks the organization
CREATION.
should be prepared to counter “now,” “soon,” and “someday.”
Implement technology controls that provide a continuously
updated view of the various network, machine, software, and INTELLIGENCE: SECURITY FEATURES &
related infrastructure assets being instantiated by engineering DESIGN (SFD)
teams. To help ensure proper coverage, the SSG works with The Security Features & Design practice is charged with creating
engineering teams (including potential shadow IT teams) to usable security patterns for major security controls (meeting the
understand orchestration, cloud configuration, and other self- standards defined in the Standards & Requirements practice),
service means of software delivery to ensure proper monitoring. building components and services for those controls, and
This monitoring requires a specialized effort—normal system, establishing collaboration during security design efforts.
network, and application logging and analysis won’t suffice.
Success might require a multi-pronged approach, including [SFD1.1: 76.6%] INTEGRATE AND DELIVER SECURITY
consuming orchestration and virtualization metadata, querying FEATURES.
cloud service provider APIs, and outside-in crawling and scraping.
Provide proactive guidance on preapproved security features for
engineering groups to use rather than each group implementing
[AM3.2: 4.5%] CREATE AND USE AUTOMATION TO
its own security features. Engineering groups benefit from
MIMIC ATTACKERS.
implementations that come preapproved, and the SSG benefits
The SSG arms engineers, testers, and incident response with by not having to repeatedly track down the kinds of subtle errors
automation to mimic what attackers are going to do. For example, that often creep into security features (e.g., authentication, role
a new attack method identified by an internal research group management, key management, logging, cryptography, protocols).
(see [AM2.8]) or a disclosing third party could require a new These security features might be discovered during SSDL
tool, so the SSG, perhaps through the security champions, could activities, created by the SSG or specialized development teams,
package the tool and distribute it to testers. The idea here is to or defined in configuration templates (e.g., cloud blueprints)
push attack capability past what typical commercial tools and and delivered via mechanisms such as SDKs, containers,
offerings encompass, then make that knowledge and technology microservices, and APIs. Generic security features often must
easy for others to use. Mimicking attackers, especially attack be tailored for specific platforms—for example, each mobile and
chains, almost always requires tailoring tools to a firm’s particular cloud platform might need its own means by which users are
technology stacks, infrastructure, and configurations. When authenticated and authorized, secrets are managed, and user
BSIMM16 67

actions are centrally logged and monitored. It’s implementing and [SFD3.1: 14.4%] FORM A REVIEW BOARD
disseminating these defined security features that generates real TO APPROVE AND MAINTAIN SECURE
progress, not simply making a list of them. DESIGN PATTERNS.
A review board formalizes the process of reaching
[SFD1.2: 69.4%] APPLICATION ARCHITECTURE
and maintaining consensus on security tradeoffs in design needs.
TEAMS ENGAGE WITH THE SSG.
Unlike a typical architecture committee focused on functions,
Application architecture teams take responsibility for security in
this group focuses on providing security guidance, preferably
the same way they take responsibility for performance, availability,
in the form of patterns, standards, features, or frameworks. It
scalability, and resiliency. One way to keep security from falling
also periodically reviews already published design guidance
out of these architecture discussions is to have secure design
(especially around authentication, authorization, and cryptography)
experts (from the SSG, a vendor, etc.) participate. Increasingly,
to ensure that design decisions don’t become stale or out of
architecture discussions include developers and site reliability
date. This review board helps control the chaos associated with
engineers who are governing all types of software components,
adoption of new technologies when development groups might
such as open source, APIs, containers, and cloud services. In
otherwise make decisions on their own without engaging the SSG
other cases, enterprise architecture teams have the knowledge to
or champions. Review board security guidance can also serve to
help the experts create secure designs that integrate properly into
inform outsourced software providers about security expectations
corporate design standards. Proactive engagement with experts
(see [CP3.2]).
is key to success here. In addition, it’s never safe for one team to
assume another team has addressed security requirements—even [SFD3.2: 19.8%] REQUIRE USE OF APPROVED
moving a well-known system to the cloud means reengaging the SECURITY FEATURES AND FRAMEWORKS.
experts.
Implementers must take their security features and frameworks
from an approved list or repository (see [SFD1.1], [SFD2.1],
[SFD2.1: 39.6%] LEVERAGE SECURE-BY-DESIGN
[SFD3.1]). There are two benefits to this activity—developers don’t
COMPONENTS AND SERVICES.
spend time reinventing existing capabilities, and review teams
Build or provide approved secure-by-design software components
don’t have to contend with finding the same old defects in new
and services for use by engineering teams. Prior to approving and
projects or when new platforms are adopted. Reusing proven
publishing secure-by-design software components and services,
components eases testing, code review, and threat modeling
including open source and cloud services, the SSG must carefully
(see [AA1.1]). Reuse is a major advantage of consistent software
assess them for security. This assessment process to declare
architecture and is particularly helpful for Agile development
a component secure-by-design is usually more rigorous and
and velocity maintenance in CI/CD pipelines. Packaging and
in-depth than that for typical projects. In addition to teaching by
applying required components, such as via containerization (see
example, these resilient and reusable building blocks aid important
[SE2.5]), makes it especially easy to reuse approved features and
efforts such as architecture analysis and code review by making
frameworks.
it easier to avoid mistakes. These components and services also
often have features (e.g., application identity, RBAC) that enable [SFD3.3: 9.9%] FIND AND PUBLISH SECURE DESIGN
uniform usage across disparate environments. Similarly, the PATTERNS FROM THE ORGANIZATION.
SSG might further take advantage of this defined list by tailoring
Foster centralized design reuse by collecting secure design
static analysis rules specifically for the components it offers (see
patterns (sometimes referred to as security blueprints) from
[CR2.6]).
across the organization and publishing them for everyone to use.
A section of the SSG website (see [SR1.2]) could promote positive
[SFD2.2: 55.9%] CREATE CAPABILITY TO SOLVE
elements identified during threat modeling or architecture analysis
DIFFICULT DESIGN PROBLEMS.
so that good ideas spread widely. This process is formalized—an
Contribute to building resilient architectures by solving design
ad hoc, accidental noticing isn’t sufficient. Common design
problems unaddressed by organizational security components
patterns accelerate development, so it’s important to use secure
or services, or by cloud service providers, thus minimizing the
design patterns, and not just for applications but for all software
negative impact that security has on other constraints, such as
assets (e.g., microservices, APIs, containers, infrastructure, and
feature velocity. Involving the SSG and secure design experts
automation).
in application refactoring or in the design of a new protocol,
microservice, or architecture feature (e.g., containerization) INTELLIGENCE: STANDARDS &
enables timely analysis of the security implications of existing
REQUIREMENTS (SR)
defenses and identifies elements to be improved. Designing for
The Standards & Requirements practice involves eliciting explicit
security early in the new project process is more efficient than
software security requirements from the organization, determining
analyzing an existing design for security and then refactoring
which COTS tools to recommend, building standards for major
when flaws are uncovered (see [AA1.1], [AA1.2], [AA2.1]). The SSG
security controls (such as authentication and input validation),
could also get involved in what would have historically been purely
creating security standards for technologies in use, and creating a
engineering discussions, as even rudimentary use of cloud-
standards review process.
native technologies (e.g., “Hello, world!”) requires proper use of
configurations and other capabilities that have direct implications
[SR1.1: 73.9%] CREATE SECURITY STANDARDS.
on security posture.
The organization meets the demand for security guidance by
creating standards that explain the required way to adhere to
BSIMM16 68

policy and carry out security-centric design, development, and code. Some software development pipeline platforms, container
operations. A standard might mandate how to perform identity- registries, and middleware platforms have begun to provide this
based application authentication or how to implement transport- visibility as metadata (e.g., SBOMs [SE3.6]) resulting from behind
level security, perhaps with the SSG ensuring the availability of the-scenes artifact scanning. Some organizations combine
a reference implementation. Standards often apply to software composition analysis results from multiple phases of the software
beyond the scope of an application’s code, including container lifecycle to get a more complete and accurate list of the open
construction, orchestration, infrastructure as-code, and cloud source being included in production software.
security configuration. Standards can be deployed in a variety of
[SR2.2: 56.6%] CREATE A STANDARDS REVIEW
ways to keep them actionable and relevant. For example, they can
be automated into development environments (such as an IDE or PROCESS.
toolchain) or explicitly linked to code examples and deployment Create a process to develop software security standards and
artifacts (e.g., containers). In any case, to be considered standards, ensure that all stakeholders have a chance to weigh in. This
they must be adopted and enforced. Standards for technology review process could operate by appointing a spokesperson for
stacks [SR3.4] and standards for incorporating new technologies any proposed security standard, putting the onus on the person
[SR3.5] can be expected to aid in the creation of these standards to demonstrate that the standard meets its goals and to get
but are not required. buy-in and approval from stakeholders. Enterprise architecture
or enterprise risk groups sometimes take on the responsibility of
[SR1.2: 79.3%] CREATE A SECURITY
creating and managing standards review processes. When the
PORTAL.
standards are implemented directly as software, the responsible
The organization has a well-known central location person might be a DevOps manager, release engineer, or whoever
for information about software security. Typically, owns the associated deployment artifact (e.g., the orchestration
this is an internal website maintained by the SSG and security code). Common triggers for standards review processes include
champions that people refer to for current information on periodic updates, security incidents, major vulnerabilities
security policies, standards, and requirements, as well as for discovered, adoption of new technologies, acquisition, etc.
other resources (such as training). An interactive portal is better
[SR2.5: 55.9%] CREATE SLA BOILERPLATE.
than a static portal with guideline documents that rarely change.
Organizations often supplement these materials with mailing The SSG works with the legal department to create standard
lists, chat channels (see [T2.12]), and face-to-face meetings. SLA boilerplate for use in contracts with vendors and outsource
Development teams are increasingly putting software security providers, including cloud providers, to require software security
knowledge directly into toolchains and automation that are outside efforts on their part. The legal department might also leverage
the organization (e.g., GitHub), but that does not remove the need the boilerplate to help prevent compliance and privacy problems.
for SSG-led knowledge management. Under the agreement, vendors and outsource providers must
meet company-mandated software security SLAs (see [CP2.4]).
[SR1.3: 69.4%] TRANSLATE COMPLIANCE
Boilerplate language might call for objective third-party insight
CONSTRAINTS TO REQUIREMENTS. into software security efforts, such as SSDF gap analysis (https://
Compliance constraints are translated into security requirements csrc.nist.gov/Projects/ssdf), BSIMMsc measurements, or BSIMM
for individual projects and communicated to the engineering scores.
teams. This is a linchpin in the organization’s compliance
[SR2.7: 47.8%] CONTROL OPEN SOURCE RISK.
strategy—by representing compliance constraints explicitly
with requirements and informing stakeholders, the organization The organization has control over its exposure to the risks that
demonstrates that compliance is a manageable task. For example, come along with using open source components and all the
if the organization builds software that processes credit card involved dependencies, including dependencies integrated at
transactions, PCI DSS compliance plays a role during the security runtime. Controlling exposure usually includes multiple efforts,
requirements phase. In other cases, technology standards built with one example being responding to known vulnerabilities in
for international interoperability can include security guidance on identified open source (see [SR1.5]). The use of open source
compliance needs. Representing these standards as requirements could also be restricted to predefined projects or to a short list of
also helps with traceability and visibility in the event of an audit. It’s versions that have been through an approved security screening
particularly useful to codify the requirements into reusable code process, have had unacceptable vulnerabilities remediated, and
(see [SFD2.1]) or artifact deployment specifications (see [SE1.4]). are made available only through approved internal repositories and
containers. For some use cases, policy might preclude any use of
[SR1.5: 79.3%] IDENTIFY OPEN SOURCE. open source. The legal department often spearheads additional
Identify open source components and dependencies open source controls due to license compliance objectives and
included in the organization’s code repositories the viral license problem associated with GPL code. SSGs that
and built software, then review them to understand partner with and educate the legal department can help move
their security posture. Organizations use a variety of tools and an organization to improve its open source risk management
metadata provided by delivery pipelines to discover old versions practices, which must be applied across the software portfolio to
of open source components with known vulnerabilities or that be effective.
their software relies on multiple versions of the same component.
Scale efforts by using automated tools to find open source,
whether whole components or perhaps large chunks of borrowed
BSIMM16 69

[SR3.2: 15.3%] COMMUNICATE STANDARDS TO [SR3.5: 1.8%] CREATE STANDARDS
VENDORS. CONTROLLING AND GUIDING THE
Work with vendors to educate them and promote the organization’s ADOPTION OF NEW TECHNOLOGIES.
security standards. A healthy relationship with a vendor often The SSG is involved in efforts to provide internal
starts with contract language (see [CP2.4]), but the SSG should practices for technologies so new that industry best practices have
engage with vendors, discuss vendor security practices, not yet been codified. Involving the SSG in exploration efforts to
and explain in simple terms (rather than legalese) what the understand and plan for new technology minimizes the negative
organization expects. Any time a vendor adopts the organization’s impacts that insecure implementations will have by proactively
security standards, it’s a clear sign of progress. Note that accounting for potential security pitfalls. The SSG’s involvement
standards implemented as security features or infrastructure can result in updates to policies and standards [SR1.1], new
configuration could be a requirement to services integration with security requirements for technology stacks [SR3.4], secure-by-
a vendor (see [SFD1.1], [SE1.4]). When the firm’s SSDL is publicly design components and services [SFD2.1, SFD3.2], or coding
available, communication regarding software security expectations guidelines [SR3.3]. The SSG must be involved in proactive efforts
is easier. Likewise, sharing internal practices and measures can surrounding the adoption of new technologies rather than merely
make expectations clear. retroactively securing existing integrations [SFD2.2] or updating
policy and standards in response to changing regulations [CP1.1]
[SR3.3: 17.1%] USE SECURE CODING STANDARDS.
or emerging threat intelligence [AM1.5]. This effort helps control
Developers use secure coding standards to avoid the most the chaos associated with adoption of new technologies (such
obvious bugs and as ground rules for code review. These as the rise of AI and LLMs) when development groups might
standards are necessarily specific to a programming language, and otherwise make decisions on their own without engaging the SSG
they can address the use of popular frameworks, APIs, libraries, or champions. It is all about ensuring that security is considered
and infrastructure automation. Secure coding standards can also from the beginning instead of having to be bolted on after the fact.
be for low- or no-code platforms (e.g., Microsoft Power Apps,
Salesforce Lightning). While enforcement isn’t the point at this SDLC TOUCHPOINTS
stage (see [CR3.5]), violation of standards is a teachable moment
for all stakeholders. Other useful coding standards topics include
SDLC TOUCHPOINTS: ARCHITECTURE
proper use of cloud APIs, use of approved cryptography, memory
ANALYSIS (AA)
sanitization, banned functions, open source use, and many
Architecture analysis encompasses capturing software
others. If the organization already has coding standards for other
architecture in concise diagrams, applying lists of risks and
purposes (e.g., style), its secure coding standards should build
threats, adopting a process for review (such as Microsoft Threat
upon them. A clear set of secure coding standards is a good way
Modeling [STRIDE] or Architecture Risk Analysis [ARA]), building an
to guide both manual and automated code review, as well as to
assessment and remediation plan for the organization, and using a
provide relevant examples for security training. Some groups might
risk methodology to rank applications.
choose to integrate their secure coding standards directly into
automation. Socializing the benefits of following standards is also
[AA1.1: 80.2%] PERFORM SECURITY
a good first step to gaining widespread acceptance (see [SM2.7]).
FEATURE REVIEW.
[SR3.4: 23.4%] CREATE STANDARDS FOR Security-aware reviewers identify application security
TECHNOLOGY STACKS. features, review these features against application
security requirements and runtime parameters, and determine if
The organization standardizes on the use of specific technology
each feature can adequately perform its intended function—usually
stacks, which translates into a reduced workload because teams
collectively referred to as threat modeling. The goal is to quickly
don’t have to explore new technology risks for every new project.
identify missing security features and requirements, or bad
The organization might create a secure base configuration
deployment configuration (authentication, access control, use
(commonly in the form of golden images, Terraform definitions,
of cryptography, etc.), and address them. For example, threat
etc.) for each technology stack, further reducing the amount of
modeling would identify both a system that was subject to
work required to use the stack safely. In cloud environments,
escalation of privilege attacks because of broken access control
hardened configurations likely include up-to-date security patches,
as well as a mobile application that incorrectly puts PII in local
configurations, and services, such as logging and monitoring. In
storage. Use of the firm’s secure-by-design components often
traditional on-premises IT deployments, a stack might include an
streamlines this process (see [SFD2.1]). Many modern applications
operating system, a database, an application server, and a runtime
are no longer simply “3-tier” but instead involve components
environment (e.g., a MEAN stack). Standards for secure use of
architected to interact across a variety of tiers—browser/endpoint,
reusable technologies, such as containers, microservices, or
embedded, web, microservices, orchestration engines, deployment
orchestration code, means that getting security right in one place
pipelines, third-party SaaS, etc. Some of these environments might
positively impacts the security posture of all downstream efforts
provide robust security feature sets, whereas others might have
(see [SE2.5]).
key capability gaps that require careful analysis, so organizations
should consider the applicability and correct use of security
features across all tiers that constitute the architecture and
operational environment.
BSIMM16 70

[AA1.2: 46.0%] PERFORM DESIGN REVIEW FOR [AA2.2: 34.2%] STANDARDIZE ARCHITECTURAL
HIGH-RISK APPLICATIONS. DESCRIPTIONS.
Perform a design review to determine whether the security Threat modeling, design review, or AA processes use an agreed
features and deployment configurations are resistant to attack upon format (e.g., diagramming language and icons, not simply a
in an attempt to break the design. The goal is to extend the more text description) to describe architecture, including a means for
formulaic approach of a security feature review (see [AA1.1]) to representing data flow. Standardizing architecture descriptions
model application behavior in the context of real-world attackers between those who generate the models and those who analyze
and attacks. Reviewers must have some experience beyond simple and annotate them makes analysis more tractable and scalable.
threat modeling to include performing detailed design reviews High-level network diagrams, data flow, and authorization flows
and breaking the design under consideration. Rather than security are always useful, but the model should also go into detail about
feature guidance, a design review should produce a set of flaws how the software itself is structured. A standard architecture
and a plan to mitigate them. An organization can use consultants description can be enhanced to provide an explicit picture of
to do this work, but it should participate actively. A review focused information assets that require protection, including useful
only on whether a software project has performed the right metadata. Standardized icons that are consistently used in
process steps won’t generate useful results about flaws. Note diagrams, templates, and dry-erase board squiggles are especially
that a sufficiently robust design review process can’t be executed useful, too.
at CI/CD speed, so organizations should focus on a few high-risk
[AA2.4: 32.4%] HAVE SSG LEAD DESIGN REVIEW
applications to start (see [AA1.4]).
EFFORTS.
[AA1.4: 51.4%] USE A RISK METHODOLOGY TO RANK
The SSG takes a lead role in performing design review (see
APPLICATIONS.
[AA1.2]) to uncover flaws. Breaking down an architecture is enough
Use a defined risk methodology to collect information about each of an art that the SSG, or other reviewers outside the application
application in order to assign a risk classification and associated team, must be proficient, and proficiency requires practice. This
prioritization. It is important to use this information in prioritizing practice might then enable, e.g., champions to take the day-to-day
what applications or projects are in scope for testing, including lead while the SSG maintains leadership around knowledge and
security feature and design reviews. Information collection can be process. The SSG can’t be successful on its own either—it will
implemented via questionnaire or similar method, whether manual likely need help from architects or implementers to understand
or automated. Information needed for classification might include, the design. With a clear design in hand, the SSG might be able
“Which programming languages is the application written in?” or to carry out a detailed review with a minimum of interaction with
“Who uses the application?” or “Is the application’s deployment the project team. Approaches to design review evolve over time,
software orchestrated?” Typically, a qualified member of the so don’t expect to set a process and use it forever. Outsourcing
application team provides the information, but the process should design review might be necessary, but it’s also an opportunity to
be short enough to take only a few minutes. The SSG can then use participate and learn.
the answers to categorize the application as, e.g., high, medium,
[AA3.1: 15.3%] HAVE ENGINEERING TEAMS LEAD AA
or low risk. Because a risk questionnaire can be easy to game, it’s
important to put into place some spot-checking for validity and PROCESS.
accuracy—an overreliance on self-reporting can render this activity Engineering teams lead AA to uncover technical flaws and
useless. document business risk. This effort requires a well-understood
and well-documented process (see [AA2.1]). But even with a
[AA2.1: 31.5%] PERFORM ARCHITECTURE ANALYSIS
good process, consistency is difficult to attain because breaking
USING A DEFINED PROCESS.
architecture requires experience, so provide architects with SSG
Define and use a process for AA that extends the design review or outside expertise in an advisory capacity. Engineering teams
(see [AA1.2]) to also document business risk in addition to performing AA might normally have responsibilities such as
technical flaws. The goal is to identify application design flaws development, DevOps, cloud security, operations security, security
as well as the associated risk (e.g., impact of exploitation), such architecture, or a variety of similar roles. The process is more
as through frequency or probability analysis, to more completely useful if the AA team is different from the design team.
inform stakeholder risk management efforts. The AA process
[AA3.2: 6.3%] DRIVE ANALYSIS RESULTS INTO
includes a standardized approach for thinking about attacks,
vulnerabilities, and various security properties. The process is STANDARD DESIGN PATTERNS.
defined well enough that people outside the SSG can carry it out. Failures identified during threat modeling, design review, or AA
It’s important to document both the architecture under review are fed back to security and engineering teams so that similar
and any security flaws uncovered, as well as risk information mistakes can be prevented in the future through improved design
that people can understand and use. Microsoft Threat Modeling, patterns, whether local to a team or formally approved for everyone
Versprite PASTA, and Black Duck ARA are examples of such a (see [SFD3.1]). This typically requires a root-cause analysis
process, although these will likely need to be tailored to a given process that determines the origin of security flaws, searches for
environment. In some cases, performing AA and documenting what should have prevented the flaw, and makes the necessary
business risk is done by different teams working together in a improvements in documented security design patterns. Note that
single process. Uncalibrated or ad hoc AA approaches don’t count security design patterns can interact in surprising ways that break
as a defined process. security, so apply analysis processes even when vetted design
patterns are in standard use. For cloud services, providers have
BSIMM16 71

learned a lot about how their platforms and services fail to resist small changes, or to conduct full analysis by scanning the entire
attack and have codified this experience into patterns for secure codebase, this service should be explicitly connected to a larger
use. Organizations that heavily rely on these services might base SSDL defect management process applied during software
their application layer patterns on those building blocks provided development. This effort is not useful when done just to “check the
by the cloud service provider (for example, AWS CloudFormation security box” on the path to deployment.
and Azure Blueprints) when making their own.
[CR1.5: 66.7%] MAKE CODE REVIEW
[AA3.3: 12.6%] MAKE THE SSG AVAILABLE AS AN AA MANDATORY FOR ALL PROJECTS.
RESOURCE OR MENTOR.
A security-focused code review is mandatory for
To build organizational AA capability, the SSG advertises experts all software projects, with a lack of code review
as resources or mentors for teams using the AA process (see or unacceptable results stopping a release, slowing it down, or
[AA2.1]). This effort might enable, e.g., security champions, site causing it to be recalled. While all projects must undergo code
reliability engineers, DevSecOps engineers, and others to take review, the process might be different for different kinds of
the lead while the SSG offers advice. As one example, mentors projects. The review for low-risk projects might rely more heavily
help tailor AA process inputs (such as design or attack patterns) on automation (see [CR1.4]), for example, whereas high-risk
to make them more actionable for specific technology stacks. projects might have no upper bound on the amount of time spent
This reusable guidance helps protect the team’s time so they can by reviewers. Having a minimum acceptable standard forces
focus on the problems that require creative solutions rather than projects that don’t pass to be fixed and reevaluated. A code review
enumerating known bad habits. While the SSG might answer AA tool with nearly all the rules turned off (so it can run at CI/CD
questions during office hours (see [T2.12]), they will often assign automation speeds, for example) won’t provide sufficient defect
a mentor to work with a team, perhaps comprising both security- coverage. Similarly, peer code review or tools focused on quality
aware engineers and risk analysts, for the duration of the analysis. and style won’t provide useful security results.
In the case of high-risk software, the SSG should play a more
[CR1.7: 42.3%] ASSIGN CODE REVIEW TOOL
active mentorship role in applying the AA process.
MENTORS.
SDLC TOUCHPOINTS: CODE REVIEW (CR)
Mentors show developers how to get the most out of code review
The Code Review practice includes use of code review tools (e.g., tools, including configuration, triage, and remediation. Security
static analysis), development of tailored rules, customized profiles champions, DevOps and site reliability engineers, and SSG
for tool use by different roles (e.g., developers vs. auditors), members often make good mentors. Mentors could use office
manual analysis, and tracking and measuring results. hours or other outreach to help developers establish the right
configuration and get started on interpreting and remediating
[CR1.2: 67.6%] PERFORM OPPORTUNISTIC CODE
results. Alternatively, mentors might work with a development
REVIEW.
team for the duration of the first review they perform. Centralized
Perform code review for high-risk applications in an opportunistic use of a tool can be distributed into the development organization
fashion. For example, organizations can follow up a design or toolchains over time through the use of tool mentors, but
review with a code review looking for security issues in source providing installation instructions and URLs to centralized tool
code and dependencies and perhaps also in deployment artifact downloads isn’t the same as mentoring. Increasingly, mentorship
configuration (e.g., containers) and automation metadata (e.g., extends to code review tools associated with deployment
infrastructure-as-code). This informal targeting often evolves into artifacts (e.g., container security) and infrastructure (e.g., cloud
a systematic approach (see [CR1.4]). Manual code review could be configuration). While AI is becoming useful to augment human
augmented with the use of specific tools and services, but it has code review guidance, it likely doesn’t have the context necessary
to be part of a proactive process. When new technologies pop up, to replace it.
new approaches to code review might become necessary.
[CR2.6: 26.1%] USE CUSTOM RULES WITH
[CR1.4: 85.6%] USE AUTOMATED CODE AUTOMATED CODE REVIEW TOOLS.
REVIEW TOOLS.
Create and use custom rules in code review tools to help uncover
Incorporate static analysis into the code review security defects specific to the organization’s coding standards
process to make the review more efficient and or to the framework-based or cloud-provided middleware the
consistent. Automation won’t replace human judgment, but it organization uses. The same group that provides tool mentoring
does bring definition to the review process and security expertise (see [CR1.7]) will likely spearhead this customization. Custom
to reviewers who typically aren’t security experts. Note that a rules are often explicitly tied to proper usage of technology stacks
specific tool might not cover an entire portfolio, especially when in a positive sense and avoidance of errors commonly encountered
new languages are involved, so additional local effort might be in a firm’s codebase in a negative sense. Custom rules are also
useful. Some organizations might progress to automating tool use an easy way to check for adherence to coding standards (see
by instrumenting static analysis into source code management [CR3.5]). To reduce the workload for everyone, many organizations
workflows (e.g., pull requests) and delivery pipeline workflows also create rules to remove repeated false positives and to turn off
(build, package, and deploy) to make the review more efficient, checks that aren’t relevant.
consistent, and aligned with release cadence. Whether use
of automated tools is to review a portion of the source code
incrementally, such as a developer committing new code or
BSIMM16 72

[CR2.7: 17.1%] USE A TOP N BUGS LIST (REAL DATA scripting bug when a specific example is found—it means going
PREFERRED). after that specific example everywhere. A firm with only a handful
of software applications built on a single technology stack
Maintain a living list of the most important kinds of bugs the
will have an easier time with this activity than firms with many
organization wants to eliminate from its code and use it to drive
large applications built on a diverse set of technology stacks.
change. Many organizations start with a generic list pulled from
A new development framework or library, rules in RASP or a
public sources, but broad-based lists such as the OWASP Top
next-generation firewall, or cloud configuration tools that provide
10 rarely reflect an organization’s bug priorities. Build a valuable
guardrails can often help in (but not replace) eradication efforts.
list by using real data gathered from code review (see [CR2.8]),
testing (see [PT1.2]), software composition analysis (see [SE3.8]),
[CR3.4: 2.7%] AUTOMATE MALICIOUS CODE
and actual incidents (see [CMVM1.1]), then prioritize it for
DETECTION.
prevention efforts. Simply sorting the day’s bug data by number
Use automated code review to identify malicious code written
of occurrences won’t produce a satisfactory list because the data
by in-house developers or outsource providers. Examples of
changes so often. To increase interest, the SSG can periodically
malicious code include backdoors, logic bombs, time bombs,
publish a “most wanted” report after updating the list. One
nefarious communication channels, obfuscated program logic,
potential pitfall with a top N list is that it tends to include only
and dynamic code injection. Although out-of-the-box automation
known problems. Of course, just building the list won’t accomplish
might identify some generic malicious-looking constructs, custom
anything—everyone has to use it to find and fix bugs.
rules for the static analysis tools used to codify acceptable and
[CR2.8: 25.2%] USE CENTRALIZED DEFECT unacceptable patterns in the organization’s codebase will likely
REPORTING TO CLOSE THE KNOWLEDGE LOOP. become a necessity. Manual review for malicious code is a good
start but insufficient to complete this activity at scale. While not all
The defects found during code review are tracked in a centralized
backdoors or similar code were meant to be malicious when they
repository that makes it possible to do both summary and trend
were written (e.g., a developer’s feature to bypass authentication
reporting for the organization. Reported defects drive engineering
during testing), such things tend to stay in deployed code and
improvements such as enhancing processes, updating standards,
should be treated as malicious until proven otherwise. Discovering
adopting reusable frameworks, etc. For example, code review
some types of malicious code will require dynamic testing
information is usually incorporated into a CISO-level dashboard
techniques.
that can include feeds from other security testing efforts (e.g.,
penetration testing, composition analysis, threat modeling).
[CR3.5: 3.6%] ENFORCE SECURE CODING
Given the historical code review data, the SSG can also use the
STANDARDS.
reports to demonstrate progress (see [SM3.3]) or drive the training
A violation of secure coding standards is sufficient grounds for
curriculum. Individual bugs make excellent training examples (see
rejecting a piece of code. This rejection can take one or more
[T2.8]). Some organizations have moved toward analyzing this
forms, such as denying a pull request, breaking a build, failing
data and using the results to drive automation (see [ST3.6]).
quality assurance, removing from production, or moving the
[CR3.2: 16.2%] BUILD A CAPABILITY TO COMBINE code into a different development workstream where repairs
AST RESULTS. or exceptions can be worked out. The enforced portions of an
organization’s secure coding standards (see [SR3.3]) often start
Combine application security testing (AST) results so that multiple
out as a simple list of banned functions or required frameworks.
testing techniques feed into one reporting and remediation
Code review against standards must be objective—it shouldn’t
process. In addition to code review, testing techniques often
become a debate about whether the noncompliant code is
include dynamic analysis, software composition analysis,
exploitable. In some cases, coding standards are specific to
container scanning, cloud services configuration review, etc.
language constructs and enforced with tools (e.g., codified into
The SSG might write scripts or acquire software to gather data
SAST rules). In other cases, published coding standards are
automatically and combine the results into a format that can
specific to technology stacks and enforced during the code review
be consumed by a single downstream review and reporting
process or by using automation. Standards can be positive (“do
solution. The tricky part of this activity is normalizing vulnerability
it this way”) or negative (“do not use this API”), but they must be
information from disparate sources that might use conflicting
enforced.
terminology or scoring. In some cases, using a standardized
taxonomy (e.g., a CWE-like approach) can help with normalization.
SDLC TOUCHPOINTS: SECURITY
Combining multiple sources helps drive better-informed risk
TESTING (ST)
mitigation decisions and identify engineering improvements.
The Security Testing practice is concerned with prerelease
[CR3.3: 7.2%] CREATE CAPABILITY TO ERADICATE defect discovery as well as integrating security into standard
BUGS. QA processes. The practice includes the use of opaque-box AST
When a security bug is found during code review (see [CR1.2], tools (including fuzz testing) as a smoke test in QA, risk-driven
[CR1.4]), the organization searches for and then fixes all crystal-box test suites, application of the attack model, and code
occurrences of the bug, not just the instance originally discovered. coverage analysis. Security testing focuses on vulnerabilities in
Searching with custom rules (see [CR2.6]) makes it possible construction.
to eradicate the specific bug entirely without waiting for every
project to reach the code review portion of its lifecycle. This
doesn’t mean finding every instance of every kind of cross-site
BSIMM16 73

[ST1.1: 83.8%] PERFORM EDGE/ organization benefits from an improved ability to create security
BOUNDARY VALUE CONDITION TESTING tests tailored to the organization’s code.
DURING QA.
[ST2.5: 27.0%] INCLUDE SECURITY TESTS IN QA
QA efforts go beyond functional testing to perform
AUTOMATION.
basic adversarial tests and probe simple edge cases and boundary
Security tests are included in an automation framework and run
conditions, with no particular attacker skills required. When QA
alongside functional, performance, and other QA test suites.
pushes past standard functional testing that uses expected input,
Executing this automation framework can be triggered manually
it begins to move toward thinking like an adversary. Boundary
or through additional automation (e.g., as part of pipeline tooling).
value testing, whether automated or manual, can lead naturally
When test creators who understand the software create security
to the notion of an attacker probing the edges on purpose (e.g.,
tests, they can uncover more specialized or more relevant
determining what happens when someone enters the wrong
defects than commercial tools might (see [ST1.4]). Security tests
password over and over).
might be derived from typical failures of security features (see
[ST1.3: 59.5%] DRIVE TESTS WITH SECURITY [SFD1.1]), from creative tweaks of functional and developer tests,
REQUIREMENTS AND SECURITY FEATURES. or even from guidance provided by penetration testers on how to
reproduce an issue. Tests that are performed manually or out-of-
QA targets declarative security mechanisms with tests derived
band likely will not provide timely feedback.
from security requirements and features. A test could try to access
administrative functionality as an unprivileged user, for example, or
[ST2.6: 25.2%] PERFORM FUZZ TESTING
verify that a user account becomes locked after some number of
CUSTOMIZED TO APPLICATION APIS.
failed authentication attempts. For the most part, security features
QA efforts include running a customized fuzzing framework
can be tested in a fashion similar to other software features—
against APIs critical to the organization. An API might be software
security mechanisms such as account lockout, transaction
that allows two applications to communicate or even software that
limitations, entitlements, etc., are tested with both expected
allows a human to interact with an application (e.g., a webform).
and unexpected input as derived from security requirements.
Testers could begin from scratch or use an existing fuzzing toolkit,
Software security isn’t security software, but testing security
but the necessary customization often goes beyond creating
features is an easy way to get started. New software architectures
custom protocol descriptions or file format templates to giving
and deployment automation, such as with container and cloud
the fuzzing framework a built-in understanding of application
infrastructure orchestration, might require novel test approaches.
interfaces and business logic. Test harnesses developed explicitly
[ST1.4: 42.3%] INTEGRATE OPAQUE-BOX SECURITY for specific applications make good places to integrate fuzz
TOOLS INTO THE QA PROCESS. testing.
The organization uses one or more opaque-box security testing
[ST3.3: 13.5%] DRIVE TESTS WITH DESIGN REVIEW
tools as part of the QA process. Such tools are valuable because
RESULTS.
they encapsulate an attacker’s perspective, albeit generically.
Use design review or architecture analysis results to direct QA
Traditional dynamic analysis scanners are relevant for web
test creation. For example, if the results of attempting to break
applications, while similar tools exist for cloud environments,
a design determine that “the security of the system hinges on
containers, mobile applications, embedded systems, APIs, etc. In
the transactions being atomic and not being interrupted partway
some situations, other groups might collaborate with the SSG to
through,” then torn transactions will become a primary target in
apply the tools, e.g., a testing team could run the tool but come
adversarial testing. Adversarial tests like these can be developed
to the SSG for help with interpreting the results. When testing is
according to a risk profile, with high-risk flaws at the top of the list.
integrated into Agile development approaches, opaque-box tools
Security defect data shared with QA (see [ST2.4]) can help focus
might be hooked into internal toolchains, provided by cloud-based
test creation on areas of potential vulnerability that can, in turn,
toolchains, or used directly by engineering. Regardless of who runs
help prove the existence of identified high-risk flaws.
the opaque-box tool, the testing should be properly integrated into
a QA cycle of the SSDL and will often include both authenticated
[ST3.4: 5.4%] LEVERAGE CODE COVERAGE
and unauthenticated reviews.
ANALYSIS.
[ST2.4: 18.0%] DRIVE QA TESTS WITH AST RESULTS. Testers measure the code coverage of their application security
testing to identify code that isn’t being exercised and then adjust
Share results from application security testing, such as penetration
test cases to incrementally improve coverage. AST can include
testing, threat modeling, composition analysis, code reviews,
automated testing (see [ST2.5], [ST2.6]) and manual testing (see
etc., with QA teams to evangelize the security mindset. Using
[ST1.1], [ST1.3]). In turn, code coverage analysis drives increased
security defects as the basis for a conversation about common
security testing depth. Coverage analysis is easier when using
attack patterns or the underlying causes for them allows QA
standard measurements, such as function coverage, line coverage,
teams to generalize this information into new test approaches.
or multiple condition coverage. The point is to measure how
Organizations that leverage software pipeline platforms such as
broadly the test cases cover the security requirements, which is
GitHub, or CI/CD platforms such as the Atlassian stack, can benefit
not the same as measuring how broadly the test cases exercise
from teams receiving various testing results automatically, which
the code.
should then facilitate timely stakeholder conversations—emailing
security reports to QA teams will not generate the desired
results. Over time, QA teams learn the security mindset, and the
BSIMM16 74

[ST3.5: 8.1%] BEGIN TO BUILD AND APPLY development and operations responding via a defect management
ADVERSARIAL SECURITY TESTS (ABUSE CASES). and release process. In addition to application vulnerabilities,
also track results from testing other software such as containers
QA teams incorporate test cases based on abuse cases
and infrastructure configuration. Properly done, this exercise
(see [AM2.1]) as testers move beyond verifying functionality
demonstrates the organization’s ability to improve the state of
and take on the attacker’s perspective. One way to do this
security and emphasizes the importance of not just identifying but
is to systematically attempt to replicate incidents from the
actually fixing security problems. One way to ensure attention is
organization’s history. Abuse and misuse cases based on the
to add a security flag to the bug-tracking and defect management
attacker’s perspective can also be derived from security policies,
system. The organization might leverage developer workflow
attack intelligence, standards, and the organization’s top N attacks
or social tooling (e.g., JIRA or Slack) to communicate change
list (see [AM3.5]). This effort turns the corner in QA from testing
requests, but these requests are still tracked explicitly as part of a
features to attempting to break the software under test.
vulnerability management process.
[ST3.6: 9.0%] IMPLEMENT EVENT-DRIVEN SECURITY
[PT1.3: 60.4%] USE PENETRATION TESTING TOOLS
TESTING IN AUTOMATION.
INTERNALLY.
The SSG guides implementation of automation for continuous,
The organization creates an internal penetration testing capability
event-driven application security testing. An event here is simply a
that uses tools as part of an established process. Execution can
noteworthy occurrence, such as dropping new code in a repository,
rest with the SSG or be part of a specialized team elsewhere in
a pull request, a build request, or a push to deployment. Event-
the organization, with the tools complementing manual efforts
driven testing implemented in pipeline automation (rather than
to improve the efficiency and repeatability of the testing process.
testing only in production) typically moves the testing closer to
The tools used will usually include off-the-shelf products built
the conditions driving the testing requirement (whether shift left
specifically for application penetration testing, network penetration
toward design or shift right toward operations), repeats the testing
tools that specifically understand the application layer, container
as often as the event is triggered, and helps ensure that the right
and cloud configuration testing tools, and custom scripts.
testing is executed for a given set of conditions. Success with this
Free-time or crisis-driven efforts aren’t the same as an internal
approach depends on the broad use of sensors (e.g., agents, bots)
capability.
that monitor engineering processes, execute contextual rules, and
provide telemetry to automation that initiates the specified testing
[PT2.2: 36.0%] PENETRATION TESTERS USE ALL
whenever event conditions are met. More mature configurations
AVAILABLE INFORMATION.
typically include risk-driven conditions (e.g., size of change,
Penetration testers, whether internal or external, routinely
provenance, function, team).
make use of artifacts created throughout the SSDL to do more
comprehensive analysis and find more problems. Example
DEPLOYMENT
artifacts include design documents, architecture analysis results,
misuse and abuse cases, code review results, cloud environment
DEPLOYMENT: PENETRATION
and other deployment configurations, and source code if
TESTING (PT) applicable. Focusing on high-risk applications is a good way to
The Penetration Testing practice involves standard outside-in start. Note that having access to SSDL artifacts is not the same as
testing of the sort carried out by security specialists. Penetration using them.
testing focuses on vulnerabilities in preproduction and production
code, providing direct feeds to defect management and mitigation. [PT2.3: 50.5%] SCHEDULE PERIODIC PENETRATION
TESTS FOR APPLICATION COVERAGE.
[PT1.1: 85.6%] USE EXTERNAL
All applications are tested periodically, which could be tied to
PENETRATION TESTERS TO FIND
a calendar or a release cycle. High-risk applications could get
PROBLEMS.
a penetration test at least once per year, for example, even if
External penetration testers are used to demonstrate there have not been substantive code changes, while other
that the organization’s software needs help. Finding critical applications might receive different kinds of security testing on
vulnerabilities in high-profile applications provides the evidence a similar schedule. Any security testing performed must focus
that executives often require. Over time, the focus of penetration on discovering vulnerabilities, not just checking a process or
testing moves from trying to determine if the code is broken in compliance box. This testing serves as a sanity check and helps
some areas to a sanity check done before shipping or on a periodic ensure that yesterday’s software isn’t vulnerable to today’s attacks.
basis. In addition to breaking code, this sanity check can also be The testing can also help maintain the security of software
an effective way to ensure that vulnerability prevention techniques configurations and environments, especially for containers and
are both used and effective. External penetration testers who bring components in the cloud. One important aspect of periodic
a new set of experiences and skills to the problem are the most security testing across the portfolio is to make sure that the
useful. problems identified are actually fixed. Software that isn’t an
application, such as automation created for CI/CD, infrastructure-
[PT1.2: 78.4%] FEED RESULTS TO THE DEFECT as-code, etc., deserves some security testing as well.
MANAGEMENT AND MITIGATION SYSTEM.
All penetration testing results are fed back to engineering through
established defect management or mitigation channels, with
BSIMM16 75

[PT3.1: 22.5%] USE EXTERNAL PENETRATION [SE1.2: 86.5%] ENSURE HOST AND
TESTERS TO PERFORM DEEP-DIVE ANALYSIS. NETWORK SECURITY BASICS ARE IN
The SSG uses external penetration testers to do a deep-dive PLACE.
analysis on critical software systems or technologies and The organization provides a solid foundation for its
to introduce fresh thinking. One way to do this is to simulate software in operation by ensuring that host (whether bare metal or
persistent attackers using goal-oriented red team exercises. virtual machine) and network security basics are in place across
These testers are domain experts and specialists who keep the its data centers and networks and that these basics remain in
organization up to speed with the latest version of the attacker’s place during new releases. Host and network security basics must
perspective and have a track record for breaking the type of account for evolving network perimeters, increased connectivity
software being tested. When attacking the organization’s software, and data sharing, software-defined networking, and increasing
these testers also demonstrate a creative approach that provides dependence on vendors (e.g., content delivery, load balancing,
useful knowledge to the people designing, implementing, and and content inspection services). In addition to securing your
hardening new systems. Creating new types of attacks from production environment, the organization should consider securing
threat intelligence and abuse cases typically requires extended their development endpoints [SE3.10] and tool chains [SE3.9].
timelines, which is essential when it comes to new technologies, Doing software security before getting host and network security
and prevents checklist-driven approaches that look only for known in place is like putting on shoes before putting on socks.
types of problems.
[SE1.3: 71.2%] IMPLEMENT CLOUD SECURITY
[PT3.2: 22.5%] CUSTOMIZE PENETRATION TESTING CONTROLS.
TOOLS.
Organizations ensure that cloud security controls are in place and
Build a capability to create penetration testing tools, or to adapt working for both public and private clouds. Industry best practices
publicly available ones, to attack the organization’s software more are a good starting point for local policy and standards to drive
efficiently and comprehensively. Creating penetration testing controls and configurations. Of course, cloud-based assets often
tools requires a deep understanding of attacks (see [AM2.1], have public-facing services that create an attack surface (e.g.,
[AM2.8]) and technology stacks (see [AM3.4]). Customizing cloud-based storage) that is different from the one in a private data
existing tools goes beyond configuration changes and extends tool center, so these assets require customized security configuration
functionality to find new issues. Tools will improve the efficiency and administration. In the increasingly software-defined world,
of the penetration testing process without sacrificing the depth of the SSG has to help everyone explicitly configure cloud-specific
problems that the SSG can identify. Automation can be particularly security features and controls (e.g., through cloud provider
valuable in organizations using Agile methodologies because administration consoles) comparable to those built with cables
it helps teams go faster. Tools that can be tailored are always and physical hardware in private data centers. Detailed knowledge
preferable to generic tools. Success here is often dependent on about cloud provider shared responsibility security models is
both the depth and scope of tests enabled through customized always necessary to ensure that the right cloud security controls
tools. remain in place.
DEPLOYMENT: SOFTWARE [SE1.4: 62.1%] DEFINE SECURE DEPLOYMENT
ENVIRONMENT (SE) PARAMETERS AND CONFIGURATIONS.
The Software Environment practice deals with OS and platform Create deployment automation or installation guides (e.g.,
patching (including in the cloud), WAFs (web application firewalls), standard operating procedures) to help teams and customers
installation and configuration documentation, containerization, install and configure software securely. Software here includes
orchestration, application monitoring, change management, and applications, products, scripts, images, firmware, and other
code signing. forms of code. Deployment automation usually includes a
clearly described configuration for software artifacts and
[SE1.1: 65.8%] USE APPLICATION INPUT the infrastructure-as-code (e.g., Terraform, CloudFormation,
MONITORING FOR SECURITY PURPOSES. ARM templates, Helm Charts) necessary to deploy them,
The organization monitors input to the software that it runs in including details on COTS, open source, vendor, and cloud
order to spot attacks. Monitoring systems that write log files services components. All deployment automation should be
are useful only if humans or bots periodically review the logs understandable by humans, not just by machines, especially when
and take action. For web applications, RASP or a WAF can do distributed to customers. Where deployment automation is not
this monitoring, while other kinds of software likely require other applicable, customers or deployment teams need installation
approaches, such as custom runtime instrumentation. Software guides that include hardening guidance and secure configurations.
and technology stacks, such as mobile and IoT, likely require their
[SE2.4: 46.9%] PROTECT CODE INTEGRITY.
own input monitoring solutions. Serverless and containerized
software can require interaction with vendor software to get the Use code protection mechanisms (e.g., code signing) that
appropriate logs and monitoring data. Cloud deployments and allow the organization to attest to the provenance, integrity,
platform-as-a-service usage can add another level of difficulty to and authorization of important code. While legacy and mobile
the monitoring, collection, and aggregation approach. platforms accomplished this with point-in-time code signing and
permissions activity, protecting modern containerized software
demands actions in various lifecycle phases. Organizations
can use build systems to verify sources and manifests of
BSIMM16 76

dependencies, creating their own cryptographic attestation of [SE3.3: 19.8%] USE APPLICATION BEHAVIOR
both. Packaging and deployment systems can sign and verify MONITORING AND DIAGNOSTICS.
binary packages, including code, configuration, metadata, code
The organization monitors production software to look for
identity, and authorization to release material. In some cases,
misbehavior or signs of attack. Go beyond host and network
organizations allow only code from their own registries to execute
monitoring to look for software-specific problems, such as
in certain environments. Protecting code integrity can also include
indications of malicious behavior, fraud, and related issues.
securing development infrastructure, using permissions and peer
Application-level intrusion detection and anomaly detection
review to govern code contributions, and limiting code access to
systems might focus on an application’s interaction with the
help protect integrity (see [SE3.9]).
operating system (through system calls) or with the kinds of data
that an application consumes, originates, and manipulates. Signs
[SE2.5: 53.2%] USE APPLICATION CONTAINERS TO
that an application isn’t behaving as expected will be specific to
SUPPORT SECURITY GOALS.
the software business logic and its environment, so one-size-fits-
The organization uses application containers to support its
all solutions probably won’t generate satisfactory results. In some
software security goals. Simply deploying containers isn’t
types of environments (e.g., platform-as a-service), some of this
sufficient to gain security benefits, but their planned use can
data and the associated predictive analytics might come from a
support a tighter coupling of applications with their dependencies,
vendor.
immutability, integrity (see [SE2.4]), and some isolation benefits
without the overhead of deploying a full operating system on a [SE3.6: 27.9%] CREATE BILLS OF MATERIALS FOR
virtual machine. Containers are a convenient place for security DEPLOYED SOFTWARE.
controls to be applied and updated consistently (see [SFD3.2]), and
Create a BOM detailing the components, dependencies, and other
while they are useful in development and test environments, their
metadata for important production software. Use this BOM to
use in production provides the needed security benefits.
help the organization tighten its security posture, i.e., to react with
agility as attackers and attacks evolve, compliance requirements
[SE2.7: 36.0%] USE ORCHESTRATION FOR
change, and the number of items to patch grows quite large.
CONTAINERS AND VIRTUALIZED ENVIRONMENTS.
Knowing where all the components live in running software—and
The organization uses automation to scale service, container,
whether they’re in private data centers, in clouds, or sold as box
and virtualized environments in a disciplined way. Orchestration
products (see [CMVM2.3])—allows for timely response when
processes take advantage of built-in and add-on security
unfortunate events occur.
features (see [SFD2.1]), such as hardening against drift, secrets
management, RBAC, and rollbacks, to ensure that each deployed [SE3.8: 7.2%] PERFORM APPLICATION
workload meets predetermined security requirements. Setting COMPOSITION ANALYSIS ON CODE REPOSITORIES.
security behaviors in aggregate allows for rapid change when the
Use composition analysis results to augment software asset
need arises. Orchestration platforms are themselves software
inventory information with data on all components comprising
that becomes part of your production environment, which in turn
important applications. Beyond open source (see [SR1.5]),
requires hardening and security patching and configuration—in
inventory information (see [SM3.1]) includes component and
other words, if you use Kubernetes, make sure you patch
dependency information for internally developed (first-party),
Kubernetes.
commissioned code (second-party), and external (third-party)
software, whether that software exists as source code or binary.
[SE3.2: 22.5%] USE CODE PROTECTION.
One common way of documenting this information is to build
To protect intellectual property and make exploit development
SBOMs. Doing this manually is probably not an option—keeping up
harder, the organization erects barriers to reverse engineering its
with software changes likely requires toolchain integration rather
software (e.g., anti-tamper, debug protection, anti-piracy features,
than carrying this out as a point-in-time activity. This information is
runtime integrity). For some software, obfuscation techniques
extremely useful in supply chain security efforts (see [SM3.5]).
could be applied as part of the production build and release
process. In other cases, these protections could be applied at the [SE3.9: 11.7%] PROTECT INTEGRITY OF
software-defined network or software orchestration layer when DEVELOPMENT TOOLCHAINS.
applications are being dynamically regenerated post-deployment.
The organization ensures the integrity of software it builds
Code protection is particularly important for widely distributed
and integrates by maintaining and securing all development
code, such as mobile applications and JavaScript distributed
infrastructure and preventing unauthorized changes to source
to browsers. On some platforms, employing Data Execution
code and other software lifecycle artifacts. Development
Prevention (DEP), Safe Structured Exception Handling (SafeSEH),
infrastructure includes code and artifact repositories, build
and Address Space Layout Randomization (ASLR) can be a good
pipelines, and deployment automation. Secure the development
start at making exploit development more difficult, but be aware
infrastructure by safely handling and storing secrets, following
that yesterday’s protection mechanisms might not hold up to
pipeline configuration requirements, patching tools and
today’s attacks.
build environments, limiting access to pipeline settings, and
auditing changes to configurations. Preventing unauthorized
changes typically includes enforcing least privilege access to
code repositories and requiring approval for code commits.
Automatically granting access for all project team members isn’t
sufficient to adequately protect software integrity.
BSIMM16 77

[SE3.10: 5.4%] PROTECT THE INTEGRITY OF [CMVM1.3: 73.9%] TRACK SOFTWARE DEFECTS
DEVELOPMENT ENDPOINTS. FOUND IN OPERATIONS THROUGH THE FIX
The organization maintains the integrity of the software it PROCESS.
builds by applying security basics to the workstations used by Defects found in operations (see [CMVM1.2]) are entered into
development stakeholders who interact with the development established defect management systems and tracked through the
toolchain. Development endpoints are the workstations used fix process. This tracking ability could come in the form of a two-
for writing source code, configuring the development toolchain, way bridge between defect finders and defect fixers or possibly
testing the software’s functionality, or modifying data in the code through intermediaries (e.g., the vulnerability management team),
or artifact repositories. Organizations can protect development but make sure the loop is closed completely. Defects can appear
endpoints by limiting or monitoring privileged actions, ensuring in all types of deployable artifacts, deployment automation, and
that the operating system and antivirus definitions are up to date, infrastructure configuration. Setting a security flag in the defect
vetting installed software, or by providing a separate, secured tracking system can help facilitate tracking.
workstation for development that is not used for administrative
tasks. Establishing and applying a development endpoint security [CMVM1.4: 77.5%] HAVE EMERGENCY RESPONSE.
baseline allows for stakeholders to perform the technical tasks The organization can make quick code and configuration
required by software development, but also provides another layer changes when software (e.g., application, API, microservice,
of defense to the development toolchain [SE3.9]. infrastructure) is under attack. An emergency response team
works in conjunction with stakeholders such as application
DEPLOYMENT: CONFIGURATION
owners, engineering, operations, and the SSG to study the code
MANAGEMENT & VULNERABILITY and the attack, find a resolution, and fix the production code (e.g.,
MANAGEMENT (CMVM) push a patch into production, rollback to a known-good state,
deploy a new container). Often, the emergency response team is
The Configuration Management & Vulnerability Management
the engineering team itself. A well-defined process is a must here,
practice concerns itself with operations processes, patching
a process that has never been used might not actually work.
and updating applications, version control, defect tracking and
remediation, and incident handling.
[CMVM2.3: 34.2%] DEVELOP AN OPERATIONS
SOFTWARE INVENTORY.
[CMVM1.1: 95.5%] CREATE OR INTERFACE
WITH INCIDENT RESPONSE. The organization has a map of its software deployments
and related containerization, orchestration, and deployment
The SSG is prepared to respond to an event or alert
automation code, along with the respective owners. If a software
and is regularly included in the incident response
asset needs to be changed or decommissioned, operations
process, either by creating its own incident response capability
or DevOps teams can reliably identify both the stakeholders
or by regularly interfacing with the organization’s existing team.
and all the places where the change needs to occur. Common
A standing meeting between the SSG and the incident response
components can be noted so that when an error occurs in one
team keeps information flowing in both directions. Having
application, other applications sharing the same components
prebuilt communication channels with critical vendors (e.g., ISP,
can be fixed as well. Building an accurate representation of
monitoring, IaaS, SaaS, PaaS) is also very important.
an inventory will likely involve enumerating at least the source
[CMVM1.2: 68.5%] IDENTIFY SOFTWARE DEFECTS code, the open source incorporated both during the build and
FOUND IN OPERATIONS MONITORING AND FEED during dynamic production updates, the orchestration software
THEM BACK TO ENGINEERING. incorporated into production images, and any service discovery or
invocation that occurs in production.
Defects identified in production through operations monitoring are
fed back to development and used to change engineering behavior. [CMVM2.4: 47.8%] STREAMLINE INCOMING
Useful sources of production defects include incidents, bug bounty
RESPONSIBLE VULNERABILITY DISCLOSURE.
(see [CMVM3.4]), responsible disclosure (see [CMVM2.4]), SIEMs,
Provide external bug reporters with a line of communication to
production logs, customer feedback, and telemetry from cloud
internal security experts through a low-friction, public entry point.
security posture monitoring, container configuration monitoring,
These experts work with bug reporters to invoke any necessary
RASP, and similar technologies. Entering production defect data
organizational responses and to coordinate with external
into an existing bug-tracking system (perhaps by making use of
entities throughout the defect management lifecycle. Successful
a special security flag) can close the information loop and make
disclosure processes require insight from internal stakeholders,
sure that security issues get fixed. In addition, it’s important to
such as legal, marketing, and public relations roles, to simplify
capture lessons learned from production defects and use these
and expedite decision-making during software security crises
lessons to change the organization’s behavior. In the best of cases,
(see [CMVM3.3]). Although bug bounties might be important
processes in the SSDL can be improved based on operations data
to motivate some researchers (see [CMVM3.4]), proper public
(see [CMVM3.2]).
attribution and a low-friction reporting process is often sufficient
motivation for researchers to participate in a coordinated
disclosure. Most organizations will use a combination of easy-
to-find landing pages, common email addresses (security@), and
embedded product documentation when appropriate (security.txt)
as an entry point for external reporters to invoke this process.
BSIMM16 78

[CMVM3.1: 14.4%] FIX ALL OCCURRENCES OF critical services warrant higher payouts). Ad hoc or short-
SOFTWARE DEFECTS FOUND IN OPERATIONS. duration activities, such as capture-the-flag contests or informal
crowdsourced efforts, don’t constitute a bug bounty program.
When a security defect is found in operations (see [CMVM1.2]),
the organization searches for and fixes all occurrences of the
[CMVM3.5: 21.6%] AUTOMATE VERIFICATION OF
defect in operations, not just the one originally reported. Doing this
OPERATIONAL INFRASTRUCTURE SECURITY.
proactively requires the ability to reexamine the entire operations
The SSG works with engineering teams to verify with automation
software inventory (see [CMVM2.3]) when new kinds of defects
the security properties (e.g., adherence to agreed upon security
come to light. One way to approach reexamination is to create a
hardening) of infrastructure generated from controlled self-
ruleset that generalizes deployed defects into something that can
service processes. Engineers use self-service processes to
be scanned for via automated code review. In some environments,
create networks, storage, containers, and machine instances,
addressing a defect might involve removing it from production
to orchestrate deployments, and to perform other tasks that
immediately and making the actual fix in some priority order before
were once IT’s sole responsibility. In facilitating verification, the
redeployment. Use of orchestration can greatly simplify deploying
organization uses machine-readable policies and configuration
the fix for all occurrences of a software defect (see [SE2.7]).
standards (see [SE1.4]) to automatically detect issues and report
[CMVM3.2: 24.3%] ENHANCE THE SSDL TO PREVENT on infrastructure that does not meet expectations. In some cases,
SOFTWARE DEFECTS FOUND IN OPERATIONS. the automation makes changes to running environments to bring
them into compliance, but in many cases, organizations use a
Experience from operations leads to changes in the SSDL (see
single policy to manage automation in different environments,
[SM1.1]), which can in turn be strengthened to prevent the
such as in multi- and hybrid-cloud environments.
reintroduction of defects. To make this process systematic, the
incident response postmortem includes a feedback-to-SSDL
[CMVM3.6: 4.5%] PUBLISH RISK DATA FOR
step. The outcomes of the postmortem might result in changes
DEPLOYABLE ARTIFACTS.
such as to tool-based policy rulesets in a CI/CD pipeline and
The organization collects and publishes risk information about
adjustments to automated deployment configuration (see [SE1.4]).
the applications, services, APIs, containers, and other software it
This works best when root-cause analysis pinpoints where in the
deploys. Whether captured through manual processes or telemetry
software lifecycle an error could have been introduced or slipped
automation, published information extends beyond basic software
by uncaught (e.g., a defect escape). DevOps engineers might have
security (see [SM2.1]) and inventory data (see [CMVM2.3])
an easier time with this because all the players are likely involved
to include risk information. This information usually includes
in the discussion and the solution. An ad hoc approach to SSDL
constituency of the software (e.g., BOMs [SE3.6]), provenance data
improvement isn’t sufficient for prevention.
about what group created it and how, and the risks associated
[CMVM3.3: 26.1%] SIMULATE SOFTWARE CRISES. with known vulnerabilities, deployment models, security controls,
or other security characteristics intrinsic to each artifact. This
The SSG simulates high-impact software security crises to
approach stimulates cross-functional coordination and helps
ensure that software incident detection and response capabilities
stakeholders take informed risk management action. Making a list
minimize damage. Simulations could test for the ability to identify
of risks that aren’t used for decision support won’t achieve useful
and mitigate specific threats or could begin with the assumption
results.
that a critical system or service is already compromised and
evaluate the organization’s ability to respond. Planned chaos
[CMVM3.8: 2.7%] DO ATTACK SURFACE
engineering can be effective at triggering unexpected conditions
MANAGEMENT FOR DEPLOYED APPLICATIONS.
during simulations. The exercises must include attacks or other
software security crises at the appropriate software layer to Operations standards and procedures proactively minimize
generate useful results (e.g., at the application layer for web application attack surfaces by using attack intelligence and
applications and at lower layers for IoT devices). When simulations application weakness data to limit vulnerable conditions. Finding
model successful attacks, an important question to consider is the and fixing software defects in operations is important (see
time required for cleanup. Regardless, simulations must focus on [CMVM1.2]) but so is finding and fixing errors in cloud security
security-relevant software failure, not on natural disasters or other models, VPNs, segmentation, security configurations for networks,
types of emergency response drills. Organizations that are highly hosts, and applications, etc., to limit the ability to successfully
dependent on vendor infrastructure (e.g., cloud service providers, attack deployed applications. Combining attack intelligence (see
SaaS, PaaS) and security features will naturally include those [AM1.5]) with information about software assets (see [AM2.9]) and
things in crisis simulations. a continuous view of application weaknesses helps ensure that
attack surface management keeps pace with attacker methods.
[CMVM3.4: 30.6%] OPERATE A BUG BOUNTY SBOMs (see [SE3.6]) are also an important information source
PROGRAM. when doing attack surface management in a crisis.
The organization solicits vulnerability reports from external
researchers and pays a bounty for each verified and accepted
vulnerability received. Payouts typically follow a sliding scale linked
to multiple factors, such as vulnerability type (e.g., remote code
execution is worth $10,000 vs. CSRF is worth $750), exploitability
(demonstrable exploits command much higher payouts), or
specific service and software versions (widely deployed or
BSIMM16 79

PART 9:
| W      | H AT C | A   | N T | H E  |
| ------ | ------ | --- | --- | ---- |
| DATA T |        | E L | L U | S    |

PART 9: WHAT CAN THE DATA This section analyzes how SSIs evolve over time by analyzing SSG
age, SSG score, and other relevant data.
TELL US
The BSIMM started out looking at the recognized leaders in
software security, so the average and median scores started
DATA ANALYSIS: SSG
out relatively high. Over the next several years, firms with less
CHARACTERISTICS experience in software security entered the data pool, and the
average and median scores dropped as could be expected. The
BSIMM12 BSIMM13 BSIMM14 BSIMM15
“decline” continued until BSIMM8, as can somewhat be seen in
SSGs are the primary implementers of an SSI, responsible for
Figure 19.
governance, enablement, productivity, and continuous growth.
You can use this information to put your SSI and SSG on a
growth path.
50
40
30
20
10
0
BSIMM6 BSIMM7 BSIMM8 BSIMM9 BSIMM10 BSIMM11 BSIMM12 BSIMM13 BSIMM14 BSIMM15 BSIMM16
Average Score Median Score
Figure 19. AVERAGE AND MEDIAN BSIMM PARTICIPANT SCORES. Adding firms with less experience decreased the average score from BSIMM7
through BSIMM8, even as remeasurements have shown that individual firm maturity increases over time.
In BSIMM9, the avBeSraIMgeM 1a2n d t h eB SmIMeMdi1a3n s c o BrSeIsM sMta1r4t e d t oB SinIMcMre1a5se. We saw the largest increase in BSIMM13, when the average and median
scores increased by 4.1 and 3, respectively. One reason for this change in average data pool score appears to be the mix of firms using the
BSIMM as part of their SSI journey. For example, Figure 20 shows how the SSG age of firms entering the BSIMM data pool changed over time. In
BSIMM16, and in concert with the increase in average scores seen for BSIMM13, BSIMM14, and BSIMM15 in Figure 20, we saw a significantly
higher average and median SSG age of new firms vs. what was seen in previous years.
10
8
6
4
2
0
BSIMM6 BSIMM7 BSIMM8 BSIMM9 BSIMM10 BSIMM11 BSIMM12 BSIMM13 BSIMM14 BSIMM15 BSIMM16
Average SSG Age Median SSG Age
Figure 20. AVERAGE AND MEDIAN SSG AGE FOR NEW FIRMS ENTERING THE BSIMM DATA POOL. The median SSG age of firms entering BSIMM7
through BSIMM8 was declining and so did the average BSIMM score, while outliers in BSIMM7 and BSIMM8 resulted in a high average SSG age. Starting
with BSIMM9, the median age of firms entering the BSIMM was higher again, which tracks with the increase of average BSIMM scores.
BSIMM16 81

BSIMM12 BSIMM13 BSIMM14 BSIMM15
25
20
15
10
5
0
BSIMM6 BSIMM7 BSIMM8 BSIMM9 BSIMM10 BSIMM11 BSIMM12 BSIMM13 BSIMM14 BSIMM15 BSIMM16
Figure 21. NUMBER OF FIRMS AGED OUT OF THE BSIMM DATA POOL.
BSIMM12 BSIMM13 BSIMM14 BSIMM15
Given their importance to overall SSI efforts, we also closely monitor champions trends. Many firms with no champions continue to exist
in the data pool, which causes the overall median champions size to be nine (46 of 111 firms had no champions at the time of their current
assessment). The median champion size is 45 for the firms with champions programs (see Figure 22).
60 100
50
AVERAGE
40 CHAMPIONS
SIZE
30
45
20
10
MEDIAN
CHAMPIONS
0
Average SSG Size Median SSG Size Average SSG Age Average Score SIZE
Champions No Champions
Figure 22. STATISTICS FOR FIRMS WITH AND WITHOUT CHAMPIONS. This data appears to validate the notion that having more people, both
centralized and distributed into engineering teams, helps SSIs achieve higher scores. For the 65 BSIMM16 firms with champions at their last assessment
time, the average champions size was 100, with a median of 45. We present the average and median SSG size to remove the impact of a few significant
outliers.
BSIMM16 82

DATA ANALYSIS: SECURITY  A security champions program is an effective way to address the
CHAMPIONS people and culture portions of the people, process, technology,
and culture view of an SSI’s scope. Firms typically rely on their
security champions to lead the ground-level security push among
A security champions program allows an SSI and SSG to  developers, architects, QA, operations, and other stakeholders
scale their reach throughout the organization and harmonize
such as cloud and site reliability. A strong security champions
everyone’s approach to software security. You can use this
program enables an SSI to scale people-driven activities, tune
information to help justify your own outreach program.
automated activities, and prioritize remediation tracking activities
within an organization. In Figure 23, the orange line shows that
firms can achieve higher scores even with a lower ratio of SSG
to developers (e.g., the bottom 20% have an average SSG-to-
A security championsB SpIrMoMgr1a2m      i s    BaSnI MorMg1a3n  i z  e   d B eSfIMfoMrt1 t4o     d  e   pBuStIMizMe 15
developer ratio of 6.8 while the top 20% have an average SSG-to-
BSIMM12         BSIMM13         BSIMM14         BSIMM15
members of the development community into being software  developer ratio of 2.7). One way these firms are able to scale is
security leaders for their geographies, application teams, or  by increasing the ratio of champions to developers, as shown by
technology groups. Once they are inducted into the program, the  the teal bars (e.g., the bottom 20% have an average champions-
SSI provides the champions with training, support, and the access  to-developer ratio of 4.6 while the top 20% have an average
needed to answer security questions. champions-to-developer ratio of 12.3).
| 15  |     |     |     | 90  |
| --- | --- | --- | --- | --- |
| 15  |     |     |     | 90  |
80
80
12
70
| 12  |     |     |     | 70  |
| --- | --- | --- | --- | --- |
60
| 9   |     |     |     | 60  |
| --- | --- | --- | --- | --- |
| 9   |     |     |     | 50  |
50
40
| 6   |     |     |     | 40  |
| --- | --- | --- | --- | --- |
6
30
30
| 3   |     |     |     | 20  |
| --- | --- | --- | --- | --- |
20
3
10
10
| 0          |                  |               |         | 0   |
| ---------- | ---------------- | ------------- | ------- | --- |
| 0          | Bottom 20%       | Middle 60%    | Top 20% | 0   |
|            | Bottom 20%       | Middle 60%    | Top 20% |     |
| SSG to Dev | Champions to Dev | Average Score |         |     |
| SSG to Dev | Champions to Dev | Average Score |         |     |
Figure 23. AVERAGE RATIO OF SSG AND CHAMPIONS SIZE TO DEVELOPERS FOR THREE SCORE BUCKETS. There is a strong correlation between
BSIMM12         BSIMM13         BSIMM14         BSIMM15
BSIMM12         BSIMsMec1u3r  i t y     c BhSaImMpMio14n s  ’   s  u  BpSpIoMrMt a1n5d overall BSIMM score (scale on the right).
While the presence of a champions program doesn’t guarantee a high number of activity observations, there is a correlation that appears when
grouping BSIMM firms by scores. Nearly 96% of firms in the highest-scoring group have a champions program as compared to 30% in the
lowest-scoring group. Figure 24 shows the score increases from an average of 22.4 activities in the lowest-scoring group (shown on the orange
line), up to an average of 76.9 activities in the highest-scoring group (shown here as the top 20%).
100
90
| 100 |     |     |     | 90  |
| --- | --- | --- | --- | --- |
80
80
80
70
| 80  |     |     |     | 70  |
| --- | --- | --- | --- | --- |
60
| 60  |     |     |     | 60  |
| --- | --- | --- | --- | --- |
| 60  |     |     |     | 50  |
50
40
| 40  |     |     |     | 40  |
| --- | --- | --- | --- | --- |
| 40  |     |     |     | 30  |
30
| 20  |     |     |     | 20  |
| --- | --- | --- | --- | --- |
20
20
10
10
| 0                         |               |            |         | 0   |
| ------------------------- | ------------- | ---------- | ------- | --- |
|                           | Bottom 20%    | Middle 60% | Top 20% |     |
| 0                         |               |            |         | 0   |
|                           | Bottom 20%    | Middle 60% | Top 20% |     |
| % of Firms with Champions | Average Score |            |         |     |
| % of Firms with Champions | Average Score |            |         |     |
Figure 24. PERCENTAGE OF FIRMS THAT HAVE A CHAMPIONS PROGRAM, ORGANIZED IN THREE BUCKETS BY BSIMM SCORE. Presence of a
champions program and average score (scale on the right) appear to be correlated, but we don’t have enough data to say which is the cause and which is
the effect. Here we see, for example, that in the bottom-scoring 20% (about seven firms) of the 65 (out of 111) firms with champions, the average score
was just over 23 compared to an average score of over 80 for the top-scoring 20% with champions.
BSIMM16 83

When separating firms into groups with and without champions,  Standards & Requirements, the firms with champions also spend
the activity observation rate increases in nearly every practice (see  consistently more effort on defect discovery in the Code Review,
Figure 25). While the biggest differences between the two spiders  Security Testing, and Penetration Testing practices.
are in Strategy & Metrics, Training, Architecture Analysis, andS trategy & Metrics
70%
Configuration Management &
Compliance & Policy
|     | Vulnerability Management |     | St6r0a%tegy & Metrics |     |     |     |     |
| --- | ------------------------ | --- | --------------------- | --- | --- | --- | --- |
5700%%
Configuration Management &
Compliance & Policy
| SofVtwualnreer Eabnviliirtyo nMmaennatgement |     |     | '6400%% |     | Training |     |     |
| -------------------------------------------- | --- | --- | ------- | --- | -------- | --- | --- |
3500%%
2'400%%
| Software Environment |     |     |     |     | Training |     |     |
| -------------------- | --- | --- | --- | --- | -------- | --- | --- |
1300%%
|     | Penetration Testing |     | 200%% |     | Attack Models |     |     |
| --- | ------------------- | --- | ----- | --- | ------------- | --- | --- |
10%
|     | Penetration Testing |             | 0%  |                          | Attack Models              |     |     |
| --- | ------------------- | ----------- | --- | ------------------------ | -------------------------- | --- | --- |
|     | Security Testing    |             |     |                          | Security Features & Design |     |     |
|     | Security Testing    |             |     |                          | Security Features & Design |     |     |
|     |                     | Code Review |     | Standards & Requirements |                            |     |     |
Architecture Analysis
|     |     | Code Review |     | Standards & Requirements |     |     |     |
| --- | --- | ----------- | --- | ------------------------ | --- | --- | --- |
Architecture Analysis
|     |     |     | Champions | No Champions |     |     |     |
| --- | --- | --- | --------- | ------------ | --- | --- | --- |
Figure 25. COMPARING FIRMS WITH AND WITHOUT CHAMPCIhOaNmS.p Tiohnes presenceN oof  aC chhaammppiioonnss program seems to correlate strongly with an increase
in program maturity as evidenced by increased scores by practice on a percentage scale.
Figure 26 shows that as SSIs get older, they have higher average  to look at the average ratio of SSG size to number of developers,
scores and are more likely to have a champions program, so is  shown in Figure 26, which might indicate that there is a correlation
the presence of champions the reason for higher scores or the  between SSI reach and the size of the security champions team.
consequence of older SSIs? One way to answer this question is
30 100%
90%
25
80%
70%
20
60%
15 50%
40%
10
30%
20%
5
10%
0 0%
| 0 –20     | 21 –30       | 31 –40 | 41 –50                    | 51 –60 | 61 –70      | 71 –80 | 81 –128 |
| --------- | ------------ | ------ | ------------------------- | ------ | ----------- | ------ | ------- |
| Champions | No Champions |        | Percentage with Champions |        | Average Age |        |         |
 Figure 26. BSIMM SCORE DISTRIBUTION RELATIVE TO CHAMPIONS SIZE AND SSG AGE. Older SSIs (light purple line) not only tend to have a higher
BSIMM score (buckets 0-20, 21-30, etc.), they are also more likely to have a champions program (gold line).
BSIMM16 84

90% OF FIRMS IN THE An important use of the BSIMM data is to help everyone see how
different groups of organizations approach the implementation
HIGHEST-SCORING GROUP of software security activities. Do certain groups focus more on
governance than testing? Or perhaps architecture and secure-by-
HAVE A CHAMPIONS design components vs. operational maintenance? What about
training? Or vendor management? While it seems true that “every
PROGRAM, COMPARED
company is becoming a software company,” different verticals still
have their own priorities. The BSIMM data helps us to observe and
TO 22% IN THE LOWEST-
analyze this.
SCORING GROUP. BSIMM16 currently reports eight verticals where there is sufficient
data to keep that data reasonably anonymous:
• Financial
• Financial Technology (FinTech)
Eighty-four percent of the 38 BSIMM16 firms that have been
• Independent Software Vendor (ISV)
assessed more than once have a champions program, while 55%
• Technology (Tech)
of the firms on their first assessment do not. Many firms that are
new to software security take some time to identify and develop a • Healthcare
champions program. This data suggests that as an SSI matures,
• Internet of Things (IoT)
its activities become distributed and institutionalized into the
• Cloud
organizational structure, perhaps even into engineering automation
as well, requiring an expanded champions program to provide • Insurance
expertise and be the local voice of the SSG.
Table 15 shows how the representation of different verticals has
grown and evolved over the history of the BSIMM. Financial, ISV,
DATA ANALYSIS: VERTICALS AND
and Technology firms were early adopters of the BSIMM. Several
PRACTICES firms fall into more than one vertical, so the numbers in Table 15
do not add up to the 111 firms in the BSIMM16 data pool, nor to
the number of firms in the previous BSIMM data pools. There are
While every company is a software company these days,
several other verticals we track, and when there are sufficient firms
there are differences in SSI implementations. You can use this
in those verticals, we will begin to or resume reporting on those
information on how vertical markets approach software security
verticals.
to inform your own strategy.
BSIMM16 85

BSIMM VERTICAL PARTCIPANTS OVER TIME
INTERNET
|     | FINANCIAL | FINTECH | ISV TECH | HEALTHCARE |     | CLOUD | INSURANCE |
| --- | --------- | ------- | -------- | ---------- | --- | ----- | --------- |
OF THINGS
| BSIMM16 | 31  | 7   | 29 45 | 8   | 15  | 25  | 8   |
| ------- | --- | --- | ----- | --- | --- | --- | --- |
| BSIMM15 | 35  | 9   | 32 43 | 9   | 19  | 26  | 14  |
| BSIMM14 | 43  | 12  | 33 39 | 10  | 21  | 32  | 15  |
| BSIMM13 | 44  | 15  | 38 33 | 11  | 19  | 35  | 15  |
| BSIMM12 | 38  | 21  | 42 28 | 14  | 18  | 26  | 13  |
| BSIMM11 | 42  | 21  | 46 27 | 14  | 17  | 30  | 14  |
| BSIMM10 | 57  |     | 43 20 | 16  | 13  | 20  | 11  |
| BSIMM9  | 50  |     | 42 22 | 19  | 16  | 17  | 10  |
|         | 47  |     | 38 16 | 17  | 12  | 16  | 11  |
BSIMM8
| BSIMM7  | 42  |     | 30 14 | 15  | 12  | 15  | 10  |
| ------- | --- | --- | ----- | --- | --- | --- | --- |
| BSIMM6  | 33  |     | 27 17 | 10  | 13  |     |     |
| BSIMM-V | 26  |     | 25 14 |     |     |     |     |
| BSIMM4  | 19  |     | 19 13 |     |     |     |     |
| BSIMM3  | 17  |     | 15 10 |     |     |     |     |
| BSIMM2  | 12  |     | 7 7   |     |     |     |     |
| BSIMM1  | 4   |     | 4 2   |     |     |     |     |
Table 15. BSIMM VERTICALS OVER TIME. The BSIMM data pool has grown over the years as shown by growth in vertical representation. Remember that
a firm can appear in more than one vertical. Note also that FinTech became a separate vertical from Financial in BSIMM11.
In five of the verticals—Cloud, IoT, FinTech, Insurance, and
COMPLIANCE & POLICY
This year, Compliance & Policy overtook Penetration Testing when  Healthcare—every firm is doing at least some of the Compliance
& Policy activities, however, only IoT has firms doing 100% of the
comparing the percentage of activities observed within practices,
activities in the practice. Technology has firms doing 100% of the
with a median score of 54% observed for the entire data pool. This
trend continues across most of the eight verticals and the Top 10  activities, but it also has firms doing none of the activities in the
practice.
and Top 25 firms. Across the verticals, it achieves a high of 63% of
the IoT firms and a low of 44% for Healthcare. The Top 10 firms are
doing 91% of the activities and the Top 25 80% (see Figure 27).
BSIMM16 86

100%
90%
80%
70%
60%
50%
40%
100% 30%
90%
20%
80%
10%
70%
0%
60% Earth Tech Cloud IoT FinTech ISV Financial Insurance Healthcare Top 10 Top 25
50% Median Value
40%
30%
20%
10%
0%
Earth Tech Cloud IoT FinTech ISV 100%Financial Insurance Healthcare Top 10 Top 25
Figure 27. SCORING RAN9G0E%S FOR COMPLIANCE & POLICY.
Median Value
80%
70%
PENETRATION TESTING 60%
Penetration Testing shows the second highest median value of all 12 practices, with a median score of 51% observed for the entire data pool
50%
(see Figure 28).
40%
100% 30%
90%
20%
80%
10%
70%
0%
60% Earth Tech Cloud IoT FinTech ISV Financial Insurance Healthcare Top 10 Top 25
50% Median Value
40%
30%
20%
10%
0%
Earth Tech Cloud IoT FinTech ISV Financial Insurance Healthcare Top 10 Top 25
Median Value
Figure 28. SCORING RANGES FOR PENETRATION TESTING.
The FinTech vertical achieves the high-water mark with a median The standout is the FinTech vertical, where all seven of the firms
score of 69% of the activities in the practice, and Healthcare shows are doing at least 28.6% of the activities in the practice, and the
the lowest median score at 34%. The Top 10 firms’ median score is interquartile range—the middle 50% of the scores—is significantly
94% of the activities, and the Top 25’s median score is 83% of the higher than all the other verticals. PCI DSS is likely a major driver
activities. This is not surprising as penetration testing is one of the for the FinTech vertical, although the Financial vertical has not
earliest recognized ways of finding vulnerabilities in software and adopted as many Penetration Testing activities as their FinTech
is required by a number of regulations like PCI DSS. peers and instead are similar to most of the other verticals and the
entire BSIMM16 data pool.
BSIMM16 87

100%
ARCHITECTURE ANALYSIS 90% Somewhat surprisingly, across all eight verticals, neither the
The practice with perhaps the greatest difference between median Top 10 firms nor the Top 25 firms are performing all 100% of
80%
values is Architecture Analysis, with the highest median score of the Architecture Analysis activities, which means that no firm in
46.7% (IoT) and lowest score of 23.6% (Insurance). Across all eight 70% the BSIMM16 data pool is doing 100% of the activities. Only the
verticals, the median scores and interquartile ranges for other Insurance vertical has all its firms (eight) doing at least some of
verticals show wide variance, indicating there is a difference in 60% the activities in the practice. Interestingly, it also has the lowest
how valuable different industries view the activities in this practice median score among all the verticals.
50%
(see Figure 29).
40%
100% 30%
90%
20%
80%
10%
70%
0%
60% Earth Tech Cloud IoT FinTech ISV Financial Insurance Healthcare Top 10 Top 25
50% Median Value
40%
30%
20%
10%
0%
Earth Tech Cloud IoT FinTech ISV 100%Financial Insurance Healthcare Top 10 Top 25
Figure 29. SCORMEe RdiAanN VGaE9 luS0 e %FOR ARCHITECTURE ANALYSIS.
80%
ATTACK MODELS 70%
The Attack Models practice shows the lowest range of scores and median scores of the 12 practices. Financial and FinTech show the highest
60%
overall scores, with good median scores as well, but Insurance beats them out with the highest medians score at 33% of the activities. Once
again, nobody is doing all the activities within the practice, and Tech5,0 I%oT, FinTech, ISV, and Financial all have firms doing nothing with Attack
Models (see Figure 30).
40%
100% 30%
90%
20%
80%
10%
70%
0%
60% Earth Tech Cloud IoT FinTech ISV Financial Insurance Healthcare Top 10 Top 25
50% Median Value
40%
30%
20%
10%
0%
Earth Tech Cloud IoT FinTech ISV Financial Insurance Healthcare Top 10 Top 25
Figure 30. SMCeOdiRanE VRaAluNeGES FOR ATTACK MODELS.
BSIMM16 88

Few of the activities in Attack Models lend themselves to  100% Figure 31, Figure 32, and Figure 33 show the score distributions for
automation and tend to be hands-on efforts by SMEs. These  the Tech, IoT, and ISV verticals, respectively, all of which are likely
90%
relatively low scores mirror the general trends in seeing activities  to see their products going into a customer’s environment outside
that allow automation increase in observation rates while SME- the control of the firm that produced the product. While there are
80%
driven activities are seeing a relative decline.  some differences, the score distributions look remarkably similar,
|     |     |     |     |     | 70% | especially in the interquartile range area where 50% of the scores  |     |     |     |
| --- | --- | --- | --- | --- | --- | ------------------------------------------------------------------- | --- | --- | --- |
IOT, TECH, ISV, AND FINTECH fall very similarly in each practice. These similarities suggest that
Besides looking at individual practices, looking at all 12 practices’  60% the three verticals see the priorities between the 12 practices in
score distributions by vertical can provide some interesting  roughly the same way.
50%
insights.
40%
100%
30%
90%
20%
80%
| 70% |     |     |     |     | 10% |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
60%
0%
50% Earth Tech Cloud IoT FinTech ISV Financial Insurance Healthcare Top 10 Top 25
40%
Median Value
30%
20%
10%
0%
| & c e | Training | k   | s   |   & | r e | w Security Testing | io n | re  | n   |
| ----- | -------- | --- | --- | --- | --- | ------------------ | ---- | --- | --- |
gy   rics a n licy ac s tu re ign d s  nts tu s Code Revie t ting w a ent t i o t
Strate mpli o Att d e l urity Fea s a r e Archite c1 0 ly 0si % Penetra f t m r a e n ty
| M e t P |     | M o | D e | n d m     | n a   |     | e s | S o n | g u e m l i ent   |
| ------- | --- | --- | --- | --------- | ----- | --- | --- | ----- | ----------------- |
| Co &    |     |     | &   | S ta ir e | A     |     | T   | ir o  | Con f i a g a b i |
|         |     |     |     | q u       |       |     |     | n v   | a n e r e m       |
|         |     | e   | c   | R e       | 9 0 % |     |     | E     | M u l n a g       |
|         |     | S   |     |           |       |     |     |       |   V a n           |
& M
80%
|     |     |     |     | Figure 31.M SeCdiOaRn EV 7 | aDl 0 uI%SeTRIBUTIONS FOR TECH. |     |     |     |     |
| --- | --- | --- | --- | -------------------------- | ------------------------------- | --- | --- | --- | --- |
60%
50%
40%
| 100% |     |     |     |     | 30% |     |     |     |     |
| ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
90%
20%
80%
10%
70%
| 60% |     |     |     |     | 0%  |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Earth Tech Cloud IoT FinTech ISV Financial Insurance Healthcare Top 10 Top 25
50%
40%
Median Value
30%
20%
10%
0%
gy   & c e Training ac k   re s   s  & tu r e Code Revie w Security Testing io n a re o n
Strate rics a n licy Att e l s tu ign r d nts c sis Penetra t ting w ent a t i n t
e t mpli o o d urity Fea e s d a m e Archite a ly s o f t m u r m e ty
| M Co &   P |     | M   |   D | ta n e | A n |     | T e | S o n | f i g g e b i l i ent |
| ---------- | --- | --- | --- | ------ | --- | --- | --- | ----- | --------------------- |
|            |     |     | &   | S u ir |     |     |     | v ir  | Con n a r a m         |
|            |     |     | c   | e q    |     |     |     | E n   | M a n e g e           |
|            |     | S e |     | R      |     |     |     |       | V u l n a             |
|            |     |     |     |        |     |     |     |       | &   M a               |
Median Value
Figure 32. SCORE DISTRIBUTIONS FOR IOT.
BSIMM16 89

100%
90%
80%
70%
60%
50%
40%
| 100% |     |     |     | 30% |     |     |     |     |
| ---- | --- | --- | --- | --- | --- | --- | --- | --- |
90%
20%
80%
10%
70%
| 60% |     |     |     | 0%  |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
Earth Tech Cloud IoT FinTech ISV Financial Insurance Healthcare Top 10 Top 25
50%
40%
Median Value
30%
20%
10%
0%
| & e      | Training |      |      | & e                | w Security Testing | n   | re  |     |
| -------- | -------- | ---- | ---- | ------------------ | ------------------ | --- | --- | --- |
| gy   n c |          | ac k | re s | s  tu r Code Revie |                    | io  | a   | o n |
Strate rics mpli a licy Att e l s tu ign r d nts c sis Penetra t ting t w ent a t i n t
e t P o o d urity Fea e s d a m e Archite a ly s o f m u r m e ty
| M Co &   |     | M   |   D | ta n e A n |     | T e | S o n | f i g g e b i l i ent |
| -------- | --- | --- | --- | ---------- | --- | --- | ----- | --------------------- |
|          |     |     | &   | S u ir     |     |     | v ir  | Con n a r a m         |
|          |     |     | c   | e q        |     |     | E n   | M a n e g e           |
|          |     | S e |     | R          |     |     |       | V u l n a             |
|          |     |     |     |            |     |     |       | &   M a               |
Figure 33. SCORE DISTRIBUTION FOR ISV.
|     |     |     |     | Median Value |     |     |     |     |
| --- | --- | --- | --- | ------------ | --- | --- | --- | --- |
Isolating the comparison to just the median scores shows similarities in scores in an even clearer way (see Figure 34). The median scores
across all 12 practices are very close.
70%
60%
50%

40%
30%
20%
10%
0%
Tech                   IoT                     ISV

Figure 34. MEDIAN SCORES FOR TECH, IOT, AND ISV VERTICALS.
To illustrate different priorities, consider the FinTech vertical in Figure 35. The score differences show a different set of priorities than Tech, IoT,
and ISV.
BSIMM16 90

100%
90%
80%
70%
60%
50%
40%
100% 30%
90%
20%
80%
70% 10%
60%
0%
50% Earth Tech Cloud IoT FinTech ISV Financial Insurance Healthcare Top 10 Top 25
40%
Median Value
30%
20%
10%
0%
Strate M gy e t & rics Co mpli & a n P c o e licy Training Att M ac o k d S e e l c s urity Fea & tu D re e s s ign S R ta e n q d u a ir r e d m s e & nts Archite A c n tu a r ly e sis Code Revie w Security Testing Penetra T t e io s n ting E S n o v f ir t o w n a m re ent Con M f & i a g n u V a r u a g M l t n e i a o e m n r n a e a b n g i t e l i m ty ent
Figure 35. SCORE DISTRIBUTIONS FOR FINTECH.
Median Value
Comparing the median scores, Figure 36 shows some similar priorities between FinTech, Tech, IoT, and ISV verticals but greater variability that
seen between just Tech, IoT, and ISV. FinTech shows higher interest in Strategy & Metrics, Code Review, and Penetration Testing.
70%
60%
50%
40%
30%
20%
10%
0%
Tech IoT ISV FinTech
Figure 36. MEDIAN SCORES FOR TECH, IOT, ISV, AND FINTECH VERTICALS.
BSIMM16 91

100%
90%
80%
70%
60%
FINTECH AND FINANCIAL
On the surface, FinTech and Financial might have similar priorities i5n0 s%oftware security, but that does not appear to be the case, as seen in
Figure 35 and Figure 37.
40%
100% 30%
90%
20%
80%
70% 10%
60%
0%
50% Earth Tech Cloud IoT FinTech ISV Financial Insurance Healthcare Top 10 Top 25
40%
Median Value
30%
20%
10%
0%
Strate M gy e t & rics Co mpli & a n P c o e licy Training Att M ac o k d S e e l c s urity Fea & tu D re e s s ign S R ta e n q d u a ir r e d m s e & nts Archite A c n tu a r ly e sis Code Revie w Security Testing Penetra T t e io s n ting E S n o v f ir t o w n a m re ent Con M f & i a g n u V a r u a g M l t n e i a o e m n r n a e a b n g i t e l i m ty ent
Figure 37. SCORE DISTRIBUTIONS FOR FINANCIAL.
Median Value
FinTech has more firms doing 100% of some practices, such as Strategy & Metrics, Security Features & Design, and Penetration Testing, while
Financial has firms achieving 100% only in Penetration Testing. FinTech has firms doing something in eight of the 12 practices, Strategy &
Metrics, Compliance & Policy, Training, Standards & Requirements, Code Review, Penetration Testing, Software Environment, and Configuration
Management & Vulnerability Management, while Financial only achieves this in four: Standards & Requirements, Code Review, Software
Environment, and Configuration Management & Vulnerability Management.
70%
60%
50%
40%
30%
20%
10%
0%
FinTech Financial
Figure 38. MEDIAN SCORE COMPARISONS FOR FINTECH AND FINANCIAL.
The median scores of the FinTech and Financial verticals (see Figure 38) show some different priorities. In general, this is perhaps largely
indicative of the fact that FinTech software is in use by other firms and has to meet broad financial industry requirements, while Financial
software is more typically in-house. When providing software to others to use, more due diligence is required to make the software robust, while
in-house software can be directly taken care of by the firm itself, allowing for somewhat more leeway.
BSIMM16 92

DATA ANALYSIS: A LOOK AT THE TOP 10S
Each year we present the “Top 10” activities (see Table 1) without much discussion. We use quotes around “Top 10” because, as Table 16
below shows, there are sometimes more than 10 items in the list. The lists are built by sorting the observation counts from highest to lowest
and identifying the observation count for the 10th activity on the list. That score then becomes the cutoff, and every activity above that score is
included—this allows for ties, meaning it does not arbitrarily cut the list off at 10 items.
| EARTH (111) | TECH (45) | CLOUD (25) | IOT (15) | FINTECH (7) |
| ----------- | --------- | ---------- | -------- | ----------- |
ACTIVITY OBS ACTIVITY OBS ACTIVITY OBS ACTIVITY OBS ACTIVITY OBS
[CMVM1.1] 106 [CMVM1.1] 43 [CMVM1.1] 24 [CMVM1.1] 15 [CMVM1.1] 7
| [SM1.4] 100 | [SM1.4] 42   | [PT1.1] 24  | [CP1.2] 15   | [CP1.2] 7 |
| ----------- | ------------ | ----------- | ------------ | --------- |
| [SE1.2] 96  | [AA1.1] 41   | [SM1.4] 24  | [SE1.2] 15   | [CR1.4] 7 |
| [CR1.4] 95  | [CR1.4] 41   | [SE1.2] 23  | [SM1.1] 15   | [PT1.1] 7 |
| [PT1.1] 95  | [SFD1.1] 41  | [PT1.2] 22  | [ST1.1] 15   | [PT1.2] 7 |
| [CP1.2] 94  | [SM1.1] 40   | [CP1.2] 21  | [AA1.1] 14   | [SE1.2] 7 |
| [ST1.1] 93  | [ST1.1] 40   | [SR1.5] 21  | [CMVM1.3] 14 | [SE2.5] 7 |
| [CP1.3] 92  | [CMVM1.3] 39 | [ST1.1] 21  | [CP1.3] 14   | [SM2.3] 7 |
| [AA1.1] 89  | [CP1.3] 39   | [AM1.5] 20  | [SR1.2] 14   | [SR1.5] 7 |
| [CP1.1] 88  | [SE1.2] 39   | [SFD1.2] 20 | [CMVM1.2] 13 | [AA1.1] 6 |
| [SR1.2] 88  | [SR1.2] 39   |             | [CP1.1] 13   | [AA1.4] 6 |
| [SR1.5] 88  |              |             | [SFD1.2] 13  | [AM1.2] 6 |
|             |              |             | [SM1.4] 13   | [CR1.2] 6 |
|             |              |             | [SR1.1] 13   | [SE1.3] 6 |
|             |              |             | [SR1.5] 13   | [SE2.7] 6 |
[SFD1.1] 6
[SM1.4] 6
[SR1.3] 6
[SR2.7] 6
| FINANCIAL (31) | ISV (29)     | INSURANCE (8) | HEALTHCARE (8) |     |
| -------------- | ------------ | ------------- | -------------- | --- |
| ACTIVITY OBS   | ACTIVITY OBS | ACTIVITY OBS  | ACTIVITY OBS   |     |
| [CMVM1.1] 30   | [AA1.1] 28   | [AM1.2] 8     | [AM1.5] 8      |     |
| [CP1.2] 29     | [CMVM1.1] 28 | [CP1.2] 8     | [CMVM1.1] 8    |     |
| [SM1.4] 29     | [CR1.4] 27   | [SE1.2] 8     | [ST1.1] 8      |     |
| [PT1.1] 28     | [SR1.5] 27   | [CMVM1.1] 7   | [CP1.1] 7      |     |
| [CP1.1] 27     | [PT1.1] 26   | [CP1.3] 7     | [CP1.2] 7      |     |
| [CP1.3] 27     | [PT1.2] 26   | [CR1.4] 7     | [CR1.4] 7      |     |
| [CR1.4] 27     | [CP1.1] 25   | [PT1.1] 7     | [PT1.1] 7      |     |
| [SE1.2] 27     | [CP1.2] 25   | [SE1.3] 7     | [SE1.1] 7      |     |
| [SE1.1] 26     | [SM1.4] 25   | [SE2.5] 7     | [SE1.2] 7      |     |
| [SR1.3] 26     | [SR1.2] 25   | [AA1.1] 6     | [SE1.3] 7      |     |
|                |              | [AM1.5] 6     | [SM1.4] 7      |     |
|                |              | [CP1.1] 6     | [SR1.2] 7      |     |
|                |              | [SR1.1] 6     | [SR1.5] 7      |     |
|                |              | [SR1.2] 6     |                |     |
|                |              | [SR1.3] 6     |                |     |
|                |              | [SR2.2] 6     |                |     |
Table 16. THE “TOP 10” ACROSS ALL VERTICALS.
BSIMM16 93

To aid in reading the chart, we include the activity names in Table 17. [CMVM1.1] COLLABORATION WITH
CYBERSECURITY OPERATIONS IS
ACTIVITY NAME
NUMBER ONE?
| [AA1.1] | Perform security feature review. |     |
| ------- | -------------------------------- | --- |
One thing that jumps out is that [CMVM1.1] Create or interface
| [AA1.4] | Use a risk methodology to rank applications. |     |
| ------- | -------------------------------------------- | --- |
with incident response is almost universally the #1 activity or tied
[AM1.2] Use a data classification scheme for  at #1, except for the Insurance vertical, where it is tied at #2. Ask
software inventory.
most software security professionals what the most important
[AM1.5] Gather and use attack intelligence. activity is for secure software, and few, if any, would say Create
or interface with incident response, so why is it almost always
| [CMVM1.1] | Create or interface with incident response. |     |
| --------- | ------------------------------------------- | --- |
#1? The simple answer is that it is something that most software
| [CMVM1.2] | Identify software defects found in operations  |     |
| --------- | ---------------------------------------------- | --- |
security programs inherit from general cybersecurity programs—
monitoring and feed them back to  most companies realize quickly that they must be able to handle
engineering. incidents, then set up an incident response capability to do so. For
[CMVM1.3] Track software defects found in operations  software security programs, [CMVM1.1] requires “little more” than
through the fix process. coordination with the broader cybersecurity response team. This
coordination ensures that incident response teams can respond to
| [CP1.1] | Unify regulatory pressures. |     |
| ------- | --------------------------- | --- |
attacks on an organization’s custom software as well as they can
| [CP1.2] | Identify privacy obligations. |     |
| ------- | ----------------------------- | --- |
for all other attacks. Building these connections is relatively easy
[CP1.3] Create policy. compared to other software security activities, and most firms do
so (106 out of 111).
| [CR1.2] | Perform opportunistic code review. |     |
| ------- | ---------------------------------- | --- |
| [CR1.4] | Use automated code review tools.   |     |
[SM1.4] SECURITY CHECKPOINTS ARE
[PT1.1] Use external penetration testers to find  IMPORTANT RELEASE CRITERIA
problems. [SM1.4] Implement security checkpoints and associated
governance is another very common activity that occurs in the
| [PT1.2] | Feed results to the defect management and  |     |
| ------- | ------------------------------------------ | --- |
mitigation system. “Top 10” across the board for every vertical except Insurance,
but even there, if we expand to the “Top 20” activities, it is tied
| [SE1.1] | Use application input monitoring for security  |     |
| ------- | ---------------------------------------------- | --- |
with many other activities as the 4th most observed activity, just
purposes.
missing out on Insurance’s “Top 10.” Creation of some sort of
| [SE1.2] | Ensure host and network security basics are  |     |
| ------- | -------------------------------------------- | --- |
security checkpoints or gates and providing governance around
in place. how software proceeds through these gates or is stopped is
[SE1.3] Implement cloud security controls. almost always seen as a good thing.
| [SE2.5] | Use application containers to support  |     |
| ------- | -------------------------------------- | --- |
[SE1.2] BASIC NETWORK AND SERVER
security goals.
HARDENING IS SEEN AS CRITICAL WHEN
| [SE2.7] | Use orchestration for containers and  |     |
| ------- | ------------------------------------- | --- |
YOU HOST SOFTWARE
virtualized environments.
[SE1.2] Ensure host and network security basics are in place
| [SFD1.1] | Integrate and deliver security features. |     |
| -------- | ---------------------------------------- | --- |
provides a good example of how different verticals have different
| [SFD1.2] | Application architecture teams engage with  |     |
| -------- | ------------------------------------------- | --- |
priorities. [SE1.2] is in the “Top 10” for every vertical except ISV, but
the SSG. this makes sense: [SE1.2] is all about the operating environment
for the software we create, and ISVs, except when they are SaaS
| [SM1.1] | Publish process and evolve as necessary. |     |
| ------- | ---------------------------------------- | --- |
[SM1.4] Implement security checkpoints and  providers, are not responsible for the operating environment
of their software—their customers are. And while Tech and
associated governance.
IoT verticals also ship products that operate in a customer’s
[SM2.3] Create or grow a security champions  environment, their products are physical devices themselves, and
program.
the firms have some responsibilities for their internal operating
| [SR1.1] | Create security standards. | environment. |
| ------- | -------------------------- | ------------ |
[SR1.2] Create a security portal. Despite ISVs having little responsibility for the operating
[SR1.3] Translate compliance constraints to  environment of their software, [SE1.2] just misses the “Top 10”
|         | requirements.                          | cutoff but is still a high-priority activity. |
| ------- | -------------------------------------- | --------------------------------------------- |
| [SR1.5] | Identify open source.                  |                                               |
| [SR2.2] | Create a standards review process.     |                                               |
| [SR2.7] | Control open source risk.              |                                               |
| [ST1.1] | Perform edge/boundary value condition  |                                               |
testing during QA.
Table 17. “TOP 10” ACTIVITY NUMBERS AND NAMES.
BSIMM16 94

[CP1.3] SOFTWARE SECURITY POLICY IS A can be diluted with acquisitions, and this can, at least temporarily,
CRITICAL FOUNDATION FOR MOST reduce the policy’s effectiveness.
[CP1.3] Create policy is perhaps surprising in that it does not Finally, some smaller firms find they can operate just fine without
appear in the “Top 10” across the board, i.e., it is not in the “Top 10” governance and the policies that go with it. Good people doing
for Cloud, FinTech, ISV, or Healthcare, but it does make the “Top the right things according to industry best practices can be
20” for Cloud, ISV, and Healthcare. This may seem surprising since reasonably effective for a time, but unfortunately, this does not
many would consider having policies around software security to last or scale, and as the firm grows, informal processes become
be a foundational activity, and they are not wrong, but there are a more of a hinderance than an enabler. Eventually, firms must begin
couple of things at play here. the process of transitioning into more defined and repeatable
processes. Many undertake a BSIMM assessment to facilitate
First is that the BSIMM always scores [CP1.3] from the perspective
this transition, and these emerging programs (see Part 3) have an
that a policy that is not enforced is not a policy. Having a written
impact on the observation rates of many activities, [CP1.3] among
policy that people can and do ignore negates its purpose. The
them.
software security lead may not yet have the influence or authority
necessary to enforce a software security policy—the written policy
[PT1.1] PENETRATION TESTING OF
may exist, but if they lack the power and influence to enforce it,
DEVICES IS A CHALLENGE
there effectively is no policy. This is a struggle that many software
security professionals will recognize if they have been in the [PT1.1] Use external penetration testers to find problems is not
business for any length of time. universally in the “Top 10.” Tech and IoT do not have [PT1.1] or its
companion [PT1.3] Use penetration testing tools internally in their
Another common cause for lack of enforcement is that many firms
“Top 10” lists, although [PT1.1] does make those verticals’ “Top
grow through acquisitions, and integrating these acquisitions into
20” lists. This reflects the reality that penetration testing devices,
an existing program can be a challenge. The enforcement of policy
which are typically what the Tech and IoT verticals produce, have
significant differences from penetration testing things like web
applications and APIs. It is a different skillset that often requires
more time than a basic web application penetration test.
About Black Duck
Black Duck® meets the board-level risks of modern software with True Scale Application Security, ensuring
uncompromised trust in software for the regulated, AI-powered world. Only Black Duck solutions free organizations
from tradeoffs between speed, accuracy, and compliance at scale while eliminating security, regulatory, and licensing
risks. Whether in the cloud or on premises, Black Duck is the only choice for securing mission-critical software
everywhere code happens. With Black Duck, security leaders can make smarter decisions and unleash business
innovation with confidence. Learn more at www.blackduck.com .
©2026 Black Duck Software, Inc. All rights reserved. Black Duck is a trademark of Black Duck Software, Inc. in the United States and other countries. All other names
mentioned herein are trademarks or registered trademarks of their respective owners. January 2026
BSIMM16 95

<!-- CONVERSION_METADATA: {"source": "https://github.com/jacobdjwilson/awesome-annual-security-reports", "date": "2026-08-12", "model": "gemini-3.5-flash-lite"} -->
