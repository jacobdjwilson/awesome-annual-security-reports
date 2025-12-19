## PART 1: EXECUTIVE SUMMARY

### TRENDS AND INSIGHTS

These BSIMM trends and insights are a distillation of software security lessons learned across 130 organizations that collectively have 11,850 security professionals helping about 410,000 developers do good security work on about 145,000 applications. Use this information to inform your own strategy for improvement.

Trends describe shifts in SSI behavior that affect activity implementation across multiple areas. Larger in scope than an activity, or even a capability that combines multiple activities within a workflow, we believe these trends show the way organizations are executing groups of activities within their evolving culture. For example, there’s a clear trend toward collecting event-driven security telemetry in addition to (or sometimes even rather than) conducting point-in-time security scans that produce reports people must review. Over time, we’ve seen a trend in testing being applied earlier in the software lifecycle (“shift left”), followed by trends in additional testing (e.g., composition analysis) and in testing automation (e.g., as checkpoints in the software development lifecycle [SDLC]).

Refer to Part 2 later in this document for more Trends and Insights.

### Why We Do Software Security

Software security leaders continue to face pressure to increase the size, scope, depth, and complexity of their SSIs. From government mandates to regulatory changes, technology shifts, budget and hiring constraints, attacker successes, and marketplace demands, software security leaders must do more with less, and do it better. In short, expanded software security governance is a necessity in any modern SSI.

However, governance done with people and checklists alone doesn’t scale very far. A trend today is governance-as-code, where security leaders provide their mandatory requirements (e.g., policies and standards) as checks or guardrails (i.e., as code) in the engineering infrastructure, enabling scaling automatically.

There has been much media, insurance, and executive attention on security issues found in third-party code. This has led to a trend in software supply chain risk management to track and secure external software that’s integrated into internal software and systems. To track this trend, BSIMM13 includes a new activity for integrating supply chain risk management.

Open source software is now a common part of nearly every development effort, which has led to a significant increase in efforts around identifying open source and controlling open source risk, whose observation rate—the rate at which we observed this effort in the BSIMM community—grew by nearly 35% from BSIMM12 to BSIMM13. Balancing the cost savings from open source use with the risk incurred is becoming an important governance objective. In some cases, it’s possible to control some risk associated with third-party software through contractual terms. We’ve recently seen a 15% increase in efforts around creating service-level agreement (SLA) boilerplate for software security responsibilities and including these SLAs in vendor contracts.

Finally, software security and the responsibility for security leaders to keep their organizations safe are growing in new ways. Beyond just scaling with software portfolio size, software security is becoming intertwined with cloud security, infrastructure security, container security, orchestration security, site reliability, and much more. These adjacent security disciplines can both support and undermine even the best software security program. We see a trend in bridge-building between these various groups for the purpose of defining and using mutually beneficial security solutions.

### Where We Do Software Security

Not so long ago, most organizations were attempting to manage software security risk by doing some testing just before releasing software to production. It quickly became evident that this approach wasn’t working and couldn’t scale even if it was. The movement to “shift left” in the SDLC put testing earlier, to happen while the code was being written. This was much more scalable and kept uncountable security defects from ever making it to production code. However, such testing—usually static analysis with a tool—was still a time-consuming gate that simply moved the friction between security and engineering from the day before release to production to the day before release to build.

Today, the trend continues toward “shift everywhere,” an approach to embedding software security testing throughout the software lifecycle in both development and operations. The move to more testing done more often, usually using smaller tests that run faster, enables the governance-as-code approach that organizations need. Facilitating shift everywhere is a trend to translating risk numbers into decisions where we see more than 25% growth in activities related to combining security testing results to improve decision-making, striving for data-driven change in software security processes, and using metrics to drive resourcing.

As another aspect of shift everywhere, organizations are trending toward distributing testing into engineering workflows—including security tests in QA functional testing automation has grown by almost 50%. There has also been steady growth in use of automated tools, integrating security tools into the QA process, and defining secure deployment parameters and configurations.

Some labor-intensive security testing has been on a downward trend. For example, using secure coding guidance and enforcing secure coding standards have declined for several years. In the past year, however, we’ve seen a significant spike in both the usage and enforcement aspects, presumably because it’s become much easier to enforce coding standards with automated testing rather than with peer code review processes that take up too much valuable development time.

### How We Do Software Security

For such a complicated endeavor, software development and its associated security governance was also simple: write some code, build it, then apply all the security testing there was time for. Development then fixed the worst security defects discovered, and some of the remainder became requirements for the next release. Today, important aspects of software security are embedded throughout people, process, technology, and culture.

Doing testing at a single SDLC gate became unacceptably inadequate over time, and today we see a trend toward continuous defect discovery, especially testing that can be automated into lifecycle tooling. For example, effort in the BSIMM Code Review and Security Testing practices each grew at almost twice the rate of effort in the Penetration Testing and Architecture Analysis practices. There is also continued growth in monitoring automated asset creation, with over half the total observations occurring in the past year.

Doing good software security requires accurate and comprehensive knowledge of software assets beyond compiling the list of software developed in-house. A rapidly growing trend is to go beyond a simple application list and to track all components within all deployed code. Here, we’ve seen a nearly 30% growth in efforts related to creating software bills of materials (SBOMs), which improve the software inventory and help with incident response.

Good software security also requires a trained workforce. The trend in providing software security training for vendors and outsourced software workers increased steadily for years but recently dropped by 30%. It’s possible organizations have found other ways to ensure that software suppliers have adequate software security programs, perhaps through a combination of attestations, reviews, and contractual agreements.

We’ve seen a nearly 30% growth in efforts related to creating software bills of materials (SBOMs), which improve the software inventory and help with incident response.

Data turned into decision support knowledge is the lifeblood of a risk management program. Organizations are, for example, leveraging operational data about security defects to look for and fix all occurrences of important defects found in operations, with a recent growth of 175% in this effort. They are also using this decision support knowledge to improve the SDLC based on issues found in operations, which has grown by 70%, and using SDLC knowledge to improve policy, which has grown by over 80%. This, and other useful knowledge, is also beginning to be turned into code when possible. Efforts to define secure deployment parameters and configurations (and to use application containers to support security goals) grew by nearly 20%, and the use of orchestration for containers grew by nearly 30%.

Once again, labor-intensive efforts are hard to staff, making them hard to scale. Security champions—a team of people skilled in various aspects of software security—are a good way to ensure that evangelism, training, and governance reaches all parts of the organization. There has recently been a 15% increase in the number of firms that have a security champions group. Note also that there has been a continuous trend over the years in organizations with a champions group scoring higher than organizations without, currently at about 35% (13 points) higher on average for BSIMM13.

### WELCOME TO BSIMM13

If you’re in charge of an SSI, understanding the BSIMM model and its use by the community will help you plan strategic improvements. If you’re running technical aspects of an initiative, you can use the how-to guide (in Part 4) and activity descriptions (in Part 6) to help define tactical improvements to people, process, technology, and culture.

Each BSIMM annual report is the result of studying real-world SSIs, which some organizations refer to as their application security program or product security program, or as their DevSecOps effort. Each year, a variety of firms in different industry verticals use the BSIMM to create a software security scorecard for their programs that they then use to manage their SSI improvements. Here, we present BSIMM13 as built directly out of the data we observed in 130 firms.

In the rapidly changing software security field, it’s important to understand what other organizations are doing in their SSIs. Comparing the efforts of hundreds of companies to your own will directly inform your strategy for your own software security efforts.

The BSIMM core knowledge is the activities we directly observed in the community—the group of firms that participate in using the BSIMM as part of their SSI management. Each community member has their own unique SSI with an emphasis on the build-security-in activities important to their business objectives, but they collectively use the activities captured here. We organize that core knowledge into a software security framework (SSF), represented in Figure 7. The SSF is organized into four domains—Governance, Intelligence, SSDL Touchpoints, and Deployment—with those domains currently embracing 125 activities. The Governance domain, for example, includes activities that fall under the organization, management, and measurement practices of an SSI.

Descriptions of the BSIMM domains, practices, and activities can be found at www.bsimm.com/framework.html.

From an executive perspective, you can view BSIMM activities as controls implemented in a software security risk management framework. The implemented activities might function as preventive, detective, corrective, or compensating controls. Positioning the activities as controls allows for easier understanding of the BSIMM’s value by governance, risk, compliance, legal, audit, and other risk management groups.

### BSIMM Terminology

Nomenclature has always been a problem in computer security, and software security is no exception. Several terms used in the BSIMM have particular meaning for us. The following list highlights some of the most important terms used throughout this document:

*   **Activity.** Actions or efforts carried out or facilitated by the SSG as part of a practice. Activities are divided into three levels in the BSIMM based on observation rates.
*   **Capability.** A set of BSIMM activities spanning one or more practices working together to serve a cohesive security function.
*   **Champions.** Interested and engaged developers, cloud security engineers, deployment engineers, architects, software managers, testers, and people in similar roles who have an active interest in software security and contribute to the security posture of the organization and its software.
*   **Community.** The group of firms in the current data pool.
*   **Data pool.** The collection of assessment data from the current community.
*   **Domain.** One of the four categories the framework is divided into, i.e., Governance, Intelligence, SSDL Touchpoints, and Deployment.
*   **Practice.** A grouping of BSIMM activities. The SSF is organized into 12 practices, three in each of four domains.
*   **Satellite.** A group of individuals, often called security champions, that is organized and leveraged by an SSG.
*   **Secure SDL (SSDL).** Any software lifecycle with integrated software security checkpoints and activities.
*   **Software security framework (SSF).** The basic structure underlying the BSIMM, comprising 12 practices divided into four domains.
*   **Software security group (SSG).** The internal group charged with carrying out and facilitating software security. The group’s name might also have an appropriate organizational focus, such as application security group or product security group.
*   **Software security initiative (SSI).** An organization-wide program to instill, measure, manage, and evolve software security activities in a coordinated fashion. Also referred to in some organizations as an application security program, product security program, or perhaps as a DevSecOps program.

### BSIMM13 DATA HIGHLIGHTS

Use the information in this section to answer common questions about BSIMM data, such as, “What are some community statistics?,” “Which activities are most firms doing?,” and “How are software security efforts changing over time?”

Activities are the building blocks and smallest unit of granularity that are implemented across organizations to build SSIs. Rather than dictating a set of prescriptive activities, the purpose of the BSIMM is to descriptively observe and quantify the actual activities carried out by various kinds of SSIs across many organizations.

The BSIMM is an observational model that reflects current software security efforts, so we adjust it annually to keep it current. For BSIMM13, we’ve made the following changes to the model based on what we see in the BSIMM community:

*   We moved activities related to controlling open source risk, implementing cloud security controls, hosting software security events, and requiring an annual training refresher because we now see them more frequently.
*   We moved activities related to security experts leading design review efforts and using centralized defect reporting for targeted training because they’re growing much more slowly than other common activities in their practice areas.
*   We added the following activities because we are beginning to see them more in the community:
    *   Integrate software supply chain risk management
    *   Perform application composition analysis on code repositories
    *   Do attack surface management for deployed applications

Unique in the software security industry, the BSIMM project has grown from nine participating companies in 2008 to 130 in 2022, now with nearly 3,350 software security group (SSG) members and over 8,500 satellite members (aka security champions). The average age of the participants’ SSIs is 5.0 years. The BSIMM project shows consistent growth even as participants enter and leave the community over time—we added 27 firms for BSIMM13 and dropped 25 whose data hadn’t been refreshed.

This 2022 edition of the BSIMM report—BSIMM13—examines anonymized data from the software security activities of 130 organizations across various verticals, including cloud, financial services, financial technology (FinTech), independent software vendors (ISVS), insurance, Internet of Things (IoT), healthcare, and technology organizations.

The popular business book, The 7 Habits of Highly Effective People, explores the theory that successful individuals share common qualities in achieving their goals and that these qualities can be identified and applied by others. The same premise can be applied to SSIs. Listed in

### BSIMM13 TOP 10 ACTIVITIES

| PERCENT | DESCRIPTION                                                              |
| :------ | :----------------------------------------------------------------------- |
| 90.0%   | Implement security checkpoints and associated governance.                |
| 88.5%   | Ensure host and network security basics are in place.                    |
| 88.5%   | Identify privacy obligations.                                            |
| 87.7%   | Create or interface with incident response.                              |
| 87.7%   | Use external penetration testers to find problems.                       |
| 86.9%   | Perform security feature review.                                         |
| 83.1%   | Perform edge/boundary value condition testing during QA.                 |
| 82.3%   | Use automated code review tools.                                         |
| 80.0%   | Integrate and deliver security features.                                 |
| 79.2%   | Translate compliance constraints to requirements.                        |

TABLE 1. TOP ACTIVITIES BY OBSERVATION PERCENTAGE. The most frequently observed activities in BSIMM13 are likely important to all SSIs.

### BSIMM13 TOP 10 ACTIVITIES GROWTH BY COUNT

| INCREASE | DESCRIPTION                                                              |
| :------- | :----------------------------------------------------------------------- |
| 20       | Streamline incoming responsible vulnerability disclosure.                |
| 20       | Implement cloud security controls.                                       |
| 18       | Control open source risk.                                                |
| 18       | Identify open source.                                                    |
| 16       | Create a standards review process.                                       |
| 15       | Gather and use attack intelligence.                                      |
| 13       | Provide expertise via open collaboration channels.                       |
| 13       | Make code review mandatory for all projects.                             |
| 13       | Create a security portal.                                                |
| 11       | Schedule periodic penetration tests for application coverage.            |

TABLE 2. TOP ACTIVITIES BY RECENT GROWTH IN OBSERVATION COUNT. These activities had the largest growth in BSIMM13, out of 44 firms measured during the last 12 months, which means they are likely important to your program now or will be soon.

Table 1 are the 10 most observed activities in the BSIMM13 data pool. The data suggests that if your organization is working on its own SSI, you should consider implementing these activities.

Table 2 shows some activities that have experienced exceptionally high growth over the past 12 months. Not surprisingly, some of these activities, such as control open source risk and identify open source, are mentioned in the Trends and Insights section. In addition, the activity introduced in BSIMM12, streamline incoming responsible vulnerability disclosure, has the largest increase in observation count. Note that for some of the activities in Table 2, the growth in observation is a new change. For example, the activities make code review mandatory for all projects, create a security portal, and provide expertise via open collaboration channels saw virtually no growth in the previous three years but all saw a significant jump in observation rates in the last 12 months. While one year of new data is not sufficient to establish a trend, it is worth paying attention to and considering for your program.

### CALL TO ACTION

Use the information in this section to prioritize improvements in your SSI and perhaps also in the SSIs of your most important software suppliers and partners.

Every SSI has room for improvement, whether it’s improving scale, effectiveness, depth, risk management, the framework of deployed activities, resourcing, or anything similar. The following suggestions represent the broad efforts we see happening in the BSIMM community, and various parts are likely right for your program as well.

#### Plan Your Journey

*   Take stock of your SSI. It’s important to periodically look at your program through a different lens, and the BSIMM enables that. Use the guidance in Part 4 to create your own SSI scorecard and compare it to your expectations.
*   Create a vision and strategic plan. Use the activity descriptions in Part 6 when creating a prioritized action plan for business areas where your current SSI efforts fall short. Typical investment areas include risk management, digital transformation, technical debt removal, technology insertion, and process improvement.

#### Get a Handle on What You Have

*   Inventory all your code. It’s likely that you’ll need specialized automation to keep track of all the code you write and all the code elsewhere in the organization. A simple application inventory will be useful for some things, such as naming risk managers, but you’ll quickly need specialized inventories such as BOMs, API and microservices lists, code that is subject to specific compliance needs, and much more.
*   Automate, automate, automate. Search for ways to eliminate error-prone manual processes and reduce friction between governance and engineering groups, including automating security decisions. This will require some policy-as-code effort and tools integration, and maybe even bringing development skills into the SSG.
*   Gather all the data. As more processes become code and more policy and standards become machine-readable, day-to-day development and operations will generate significantly more telemetry about what’s happening and why. Use this data to ensure that everything’s working as expected.

#### Pay Attention to the Latest Trends

*   Innovate in digital transformation. Encourage your SSG and other security stakeholders to experiment with ways to deliver security value directly into engineering processes, especially where current security testing tools don’t always keep up with engineering changes, such as with serverless architectures, single-page applications, API security, and zero trust.
*   Secure the software supply chain. Nearly every organization today uses third-party code and provides code as a third party to other organizations. While producing SBOMs is easy, the management of software, SBOMs, vendors, and vulnerability information is much more complicated.
*   Expand software security into adjacencies. Even perfect software can have its security undermined by mistakes elsewhere in the organization. Make explicit ties between the SSI and other security stakeholders working in areas such as container security, orchestration security, cloud security, infrastructure security, and site reliability.

In summary, the data shows that new SSIs—from just started to 18 months old—are typically doing about 33 BSIMM activities. These organizations are also beginning to scale these activities across their software portfolio, deal with all the change going on around them, and evolve their risk management strategy.

Here are some suggestions on reading through this BSIMM report:

*   If you’re experienced with the BSIMM, or if you need some content to help make your case with executive management, then Part 2: Trends and Insights are probably what you’re looking for.
*   If this is your first time with the BSIMM, we recommend first reading Part 5 for context and then returning here to decide what to read next.
*   If you’re starting an SSI or an SSG, or looking to mature an existing program, start with Part 4: Quick Guide to SSI Maturity, then move to Appendix B: How to Build or Upgrade an SSI, and then read through the activities in Part 6.
*   If you want to get right into the types of software security controls organizations are using in their SSIs, or if you are working on building out capabilities, then read Part 6: The BSIMM Activities.
*   If you want to see a summary of the BSIMM13 data, review Appendix D.
*   If you want to look at our analysis of the BSIMM data, review Appendices E though H.
*   If you’d like to see a brief case study, the Case Studies section has you covered.

## THE BSIMM SKELETON

The BSIMM skeleton provides a way to view activities at a glance, which is useful when thinking about your own SSI. The skeleton is shown in Figure 1, organized by domains and practices. More complete descriptions of the activities and examples are available in Part 6 of this document.

Use this skeleton to understand the software security activities included in BSIMM13. A list of software security controls can be a very helpful guide, and the BSIMM project has worked since 2008 to ensure that its content matches real-world efforts.

### GOVERNANCE

#### STRATEGY & METRICS

*   Publish process and evolve as necessary.
*   Educate executives on software security.
*   Implement security checkpoints and associated governance.
*   Publish data about software security internally and use it to drive change.
*   Enforce security checkpoints and track exceptions.
*   Create or grow a satellite (security champions).
*   Require security sign-off prior to software release.
*   Create evangelism role and perform internal marketing.
*   Use a software asset tracking application with portfolio view.
*   Make SSI efforts part of external marketing.
*   Identify metrics and use them to drive resourcing.
*   Integrate software-defined lifecycle governance.
*   Integrate software supply chain risk management.

#### COMPLIANCE & POLICY

*   Unify regulatory pressures.
*   Identify privacy obligations.
*   Create policy.
*   Build a PII inventory.
*   Require security sign-off for compliance-related risk.
*   Implement and track controls for compliance.
*   Include software security SLAs in all vendor contracts.
*   Ensure executive awareness of compliance and privacy obligations.
*   Document a software compliance story.
*   Ensure compatible vendor policies.
*   Drive feedback from software lifecycle data back to policy.

#### TRAINING

*   Conduct software security awareness training.
*   Deliver on-demand individual training.
*   Include security resources in onboarding.
*   Enhance satellite (security champions) through training and events.
*   Create and use material specific to company history.
*   Deliver role-specific advanced curriculum.
*   Host software security events.
*   Require an annual refresher.
*   Reward progression through curriculum.
*   Provide training for vendors and outsourced workers.
*   Provide expertise via open collaboration channels.
*   Identify new satellite members (security champions) through observation.

### INTELLIGENCE

#### ATTACK MODELS

*   Use a data classification scheme for software inventory.
*   Identify potential attackers.
*   Gather and use attack intelligence.
*   Build attack patterns and abuse cases tied to potential attackers.
*   Create technology-specific attack patterns.
*   Maintain and use a top N possible attacks list.
*   Collect and publish attack stories.
*   Build an internal forum to discuss attacks.
*   Have a research group that develops new attack methods.
*   Create and use automation to mimic attackers.
*   Monitor automated asset creation.

#### SECURITY FEATURES & DESIGN

*   Integrate and deliver security features.
*   Application architecture teams engage with the SSG.
*   Leverage secure-by-design components and services.
*   Create capability to solve difficult design problems.
*   Form a review board or central committee to approve and maintain secure design patterns.
*   Require use of approved security features and frameworks.
*   Find and publish secure design patterns from the organization.

#### STANDARDS & REQUIREMENTS

*   Create security standards.
*   Create a security portal.
*   Translate compliance constraints to requirements.
*   Create a standards review process.
*   Identify open source.
*   Create SLA boilerplate.
*   Control open source risk.
*   Communicate standards to vendors.
*   Use secure coding standards.
*   Create standards for technology stacks.

### SSDL TOUCHPOINTS

#### ARCHITECTURE ANALYSIS

*   Perform security feature review.
*   Perform design review for high-risk applications.
*   Use a risk methodology to rank applications.
*   Perform architecture analysis using a defined process.
*   Standardize architectural descriptions.
*   Have SSG lead design review efforts.
*   Have engineering teams lead AA process.
*   Drive analysis results into standard architecture patterns.
*   Make the SSG available as an AA resource or mentor.

#### CODE REVIEW

*   Perform opportunistic code review.
*   Use automated code review tools.
*   Make code review mandatory for all projects.
*   Assign code review tool mentors.
*   Use custom rules with automated code review tools.
*   Use a top N bugs list (real data preferred).
*   Use centralized defect reporting to close the knowledge loop.
*   Build a capability to combine AST results.
*   Create capability to eradicate bugs.
*   Automate malicious code detection.
*   Enforce secure coding standards.

#### SECURITY TESTING

*   Perform edge/boundary value condition testing during QA.
*   Drive tests with security requirements and security features.
*   Integrate opaque-box security tools into the QA process.
*   Drive QA tests with AST results.
*   Include security tests in QA automation.
*   Perform fuzz testing customized to application APIs.
*   Drive tests with design review results.
*   Leverage code coverage analysis.
*   Begin to build and apply adversarial security tests (abuse cases).
*   Implement event-driven security testing in automation.

### DEPLOYMENT

#### PENETRATION TESTING

*   Use external penetration testers to find problems.
*   Feed results to the defect management and mitigation system.
*   Use penetration testing tools internally.
*   Penetration testers use all available information.
*   Schedule periodic penetration tests for application coverage.
*   Use external penetration testers to perform deep-dive analysis.
*   Customize penetration testing tools.

#### SOFTWARE ENVIRONMENT

*   Use application input monitoring.
*   Ensure host and network security basics are in place.
*   Implement cloud security controls.
*   Define secure deployment parameters and configurations.
*   Protect code integrity.
*   Use application containers to support security goals.
*   Use orchestration for containers and virtualized environments.
*   Use code protection.
*   Use application behavior monitoring and diagnostics.
*   Create bills of materials for deployed software.
*   Perform application composition analysis on code repositories.

#### CONFIGURATION MANAGEMENT & VULNERABILITY MANAGEMENT

*   Create or interface with incident response.
*   Identify software defects found in operations monitoring and feed them back to development.
*   Have emergency response.
*   Track software bugs found in operations through the fix process.
*   Develop an operations software inventory.
*   Fix all occurrences of software bugs found in operations.
*   Enhance the SSDL to prevent software bugs found in operations.
*   Simulate software crises.
*   Operate a bug bounty program.
*   Automate verification of operational infrastructure security.
*   Publish risk data for deployable artifacts.
*   Streamline incoming responsible vulnerability disclosure.
*   Do attack surface management for deployed applications.

## PART 2: TRENDS AND INSIGHTS

### Where do we get the data, and why should you participate?

BSIMM data originates in interviews conducted with member firms during a BSIMM assessment. Through these in-depth conversations, assessors look for the existence of BSIMM activities and assign credit for activities that are performed with sufficient coverage across the organization, formality to be repeatable and consistent, and depth to be effective at managing associated risk. After each assessment, the observation data is anonymized and added to the BSIMM data pool, where statistical analysis is performed to highlight trends in how firms secure their software. You can use this information to understand what others are doing to then inform your own strategy.

Businesses have seen drivers, pressures, and threats come from nearly every direction. Ransomware attacks have put pressure on supply chains and manufacturing sectors. Industries are facing new regulations or having to re-adapt to old ones as cryptocurrencies go mainstream and interact with currency and banks. The US government has made cybersecurity a priority and is releasing executive orders to put it on industry’s radar. The outbreak of war is bringing hacktivism back after a relatively quiet period. Of course, there have also been new software languages and technology stacks, massive shifts to the cloud, and over two years of working from home.

These and other external drivers are being met by organizational transformations facilitated by new technologies, expanded processes, changes in the security culture, and increased supply chain security efforts.

### SHIFT EVERYWHERE

Starting more than 15 years ago, the “shift left” trend drove firms to focus on moving security testing earlier in the development process, starting with doing SAST during development. Much more recently, “shift everywhere” extends this trend into making security testing continuous throughout the software lifecycle. This means that smaller, faster, pipeline-driven security tests are conducted as soon as there is an artifact to test. These tests are often smaller and context-specific, such as validating the use of a required library during a pull request, rather than waiting until a build cycle or a penetration test—and these tests can happen anywhere from design to production. A shift everywhere approach is useful for more than just testing for vulnerabilities in a timely fashion; it also facilitates automating governance checks and measuring risk in various parts of the software lifecycle. For example, shifting right into production might entail using automated tests to continuously verify that only those APIs with proper documentation are allowed to receive certain traffic.

#### Translating Risk Numbers into Decisions

BSIMM13 data shows an increase in firms that collect and combine data from various sources throughout the SDLC to support security decisions. There was more than 25% average growth in related activities such as build a capability to combine AST results, publish data about software security internally and drive change, and identify metrics and use them to drive resourcing. Collecting and combining data is an important step in shaping risk-based secure SDLC governance and is also a necessary step in governance-as-code efforts.

#### Continuous Defect Discovery

Firms are increasing adoption of automated defect discovery approaches that favor continuous monitoring and reporting over expert-intensive point-in-time defect discovery. For example, effort in the Code Review and Security Testing practices each grew at almost twice the rate of the effort in the Penetration Testing and Architecture Analysis practices. There is also continued growth in monitoring automated asset creation, with over half the total observations occurring in the past year. Shifting everywhere in the SDLC with integrated tooling is an important step in increasing governance while minimizing friction with engineering processes.

#### Governance-as-Code

Firms are augmenting their implementations of governance-as-code by integrating off-the-shelf CI/CD pipeline solutions with their custom automation or in-house solutions. In some cases, decisions about what to test and when are being implemented in the same commercial software that runs integration tests and software pushes. These automation approaches enable the translation of software security standards and policy into human-readable configuration code or simplified code that conducts software vulnerability discovery.

### SOFTWARE SUPPLY CHAIN RISK MANAGEMENT

Increased media attention on critical vulnerabilities discovered in third-party libraries and on supply chain instability caused by global events has increased executive attention on software risk that doesn’t originate in the firm’s own SDLC. Efforts to manage software supply chain risk are focusing on tracking and securing software that is integrated into in-house-built software and ensuring that software suppliers follow best practices.

After observing increased efforts around controlling risk associated with software brought into the firm, BSIMM13 added the integrate supply chain risk management activity. This activity captures efforts to manage risk through governance-driven access and usage controls, maintenance standards, and provenance data. Because software supply chain risk can be introduced at any point in the lifecycle of internally built or bespoke software, firms are moving to automated solutions to ensure that all access, usage, and modifications are done in accordance with policy everywhere in the software lifecycle.

#### Software Bill of Materials

An SBOM is a machine-readable listing of all the components included in a set of software and aids in identifying which software components could include a publicly disclosed security vulnerability. Firms are adding SBOM generation to their security capabilities to both aid in managing the risk posed by vulnerabilities discovered in the open source they use and to improve their ability to respond promptly to disclosed vulnerabilities. This usefulness likely drove the 30% growth of create bills of materials for deployed software. This new effort also contributed to the addition of a new activity for BSIMM13: perform application composition analysis on code repositories.

#### Open Source Software

Firms are getting better at managing the risk associated with integrating open source software into their own applications. Increased media coverage of vulnerabilities found in open source libraries is bringing added executive attention to this area, and the availability of software composition analysis tooling is continuing to fuel year-over-year growth of the identify open source and control open source risk activities, which grew by nearly 35%. Firms won’t be able to get ahead of critical vulnerabilities in their open source libraries without building a comprehensive approach to managing this risk.

#### Vendor Management

Firms are increasing pressure on vendors by communicating and imposing software security standards on the supplied software. Observations of the communicate standards to vendors and ensure compatible vendor policies activities grew by over 50% in BSIMM13. Organizations are also increasing their use of standard SLA terms in contracts with vendors and outsource providers to ensure that third-party software won’t jeopardize compliance with their software security standards. The create SLA boilerplate and include software security SLAs in all vendor contracts activities are continuing to grow year-over-year and saw a 15% increase in observations. Ensuring that vendor-supplied software is held to the same security standards as internally built software is essential to managing risk across the entire software portfolio.

#### Training for Outsourced Workers

Not all trends happen in a positive direction. The activity with the largest drop in observation rates in BSIMM13 is provide training for vendors and outsourced workers. The observations for this activity grew steadily over the lifetime of the BSIMM. In BSIMM13, however, the observation rate fell by 30%. Of the 44 firms measured between BSIMM12 and BSIMM13, only two were providing training to vendors and outsourced workers, and the overall BSIMM13 measurement fell to 16 observations as data aged out of the BSIMM13 data pool. This fall in observations might also be linked to growth in the create SLA boilerplate and include software security SLAs in all vendor contracts activities, where organizations might specify training requirements that contracted firms are expected to provide their development teams.

### SECURITY INTEGRATION INTO DEVELOPER TOOLCHAINS

Developers and software vendors continue to make progress in integrating security options into CI/CD pipelines and toolchains. These integrations provide faster and tighter processes that reduce friction, improve coverage, and make the shift everywhere concept a reality.

In the early days of application security, firms found vulnerabilities everywhere they looked—in production, in pre-release products, and in news reports about their software. Shift left was a call to move testing efforts earlier into the development lifecycle to find and fix software vulnerabilities before they could be taken advantage of in production. For a waterfall development structure, shift left meant examining designs during the design phase, testing code when that code was being built, and testing applications as soon as they could run. This view had to evolve and adapt as Agile sprints meant, for example,
