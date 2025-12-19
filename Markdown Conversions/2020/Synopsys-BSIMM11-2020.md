BSIMM11 AUTHORS

Created by Sammy Migues, John Steven, and Mike Ware

Sammy Migues
Principal Scientist at Synopsys
Sammy works primarily with senior managers on entrepreneurial innovation, practical business solutions, and business
process optimization. At Synopsys, he started the internal knowledge management program as well as commercial
offerings for CBT and ILT software security training, smart grid security, and the management consulting practice for
software security initiative creation and improvement, metrics, and DevSecOps transformation. Migues is also a creator
and the maintainer of the BSIMM, the only study of its kind to capture the actual software security practices in nearly
200 firms around the world.

John Steven
Founding Principal of Aedify Security
John provides strategic consulting to software security initiatives and serves as technical advisor to application security
and cloud security vendors. John is also CTO of ZeroNorth. For two decades, John led technical direction at Cigital.
He founded Cigital spin-off Codiscope as its CTO in 2015. Both firms were acquired by Synopsys in 2016, where John
served as Senior Director of Security Technology and Applied Research. A BSIMM author and trusted advisor to security
executives, John is keenly interested in enabling software-defined security governance, using his unparalleled experience
with a broad range of security tools and techniques to build mature security initiatives.

Mike Ware
Sr. Director of Technology at Synopsys
Mike leads the consulting technology practices for Synopsys within the Software Integrity Group (SIG), based in the
Eastern Panhandle of WV. Having undertaken leadership roles in both client management and technology thought
leadership since 2008, Mike has led the implementation of our client’s largest software security initiatives. A BSIMM
co-author, Mike focuses on relentlessly understanding the business and technology drivers for software security as an
industry and innovating SIG’s portfolio of software security capabilities and solutions.

BSIMM LICENSE

This work is licensed under the Creative Commons Attribution-Share Alike 3.0 License. To view a copy of this license,visit http://creativecommons.
org/licenses/by-sa/3.0/legalcode or send a letter to Creative Commons, 171 Second Street, Suite 300, San Francisco, California, 94105, USA.

PAGE 2   |   BUILDING SECURITY IN MATURITY MODEL (BSIMM) – VERSION 11

EXECUTIVE SUMMARY

The BSIMM is the result of a multiyear study of real-world software security initiatives (SSIs). We present BSIMM11 as
built directly out of data observed in 130 firms. These firms are listed in the Acknowledgments section.

The BSIMM is primarily a measuring stick for software security. The best way to use it is to compare and contrast your
own initiative with the data about what other organizations are doing. The BSIMM also functions as a roadmap for an SSI.
You can identify your own goals and objectives, then refer to the BSIMM to determine which additional activities make
sense for you.

The purpose of the BSIMM is to quantify the activities carried out by various kinds of SSIs across many organizations.
Because these initiatives use different methodologies and different terminology, the BSIMM requires a framework that
allows us to describe any initiative in a uniform way. Our software security framework (SSF) and activity descriptions
provide a common vocabulary for explaining the salient elements of an SSI, thereby allowing us to compare initiatives
that use different terms, operate at different scales, exist in different parts of the organizational chart, operate in different
vertical markets, or create different work products.

We understand that not all organizations need to achieve the same security goals, but we believe all organizations can
benefit from using a common measuring stick. The BSIMM is not a traditional maturity model where a set of activities are
repeated at multiple levels of depth and breadth—do something at level 1, do it more at level 2, do it better at level 3, and
so on. Instead, the BSIMM comprises a set of unique activities, with activity levels used only to distinguish the relative
frequency with which the activities are observed in organizations. Frequently observed activities are designated as level 1,
less frequently observed activities are designated level 2, and infrequently observed activities are designated level 3. Table
A shows the natural groupings of activities.

In the rapidly changing software security field, understanding what most, some, and few other organizations are doing
in their SSIs can directly inform your own strategy.

We hold the scorecards for individual firms in confidence, but we publish aggregate data describing the number of times
we have observed each activity (see the BSIMM11 Scorecard in Part Two). We also publish observations about subsets
(such as industry verticals) when our sample size for the subset is large enough to guarantee anonymity.

NATURAL GROUPINGS OF ACTIVITIES

LEVEL 1

SOFTWARE ENVIRONMENT (SE)

OBSERVATIONS

Activities in this practice

observed most frequently

[SE1.1] Use application input monitoring.

[SE1.2] Ensure host and network security basics are in place.

73

121

LEVEL 2

SOFTWARE ENVIRONMENT (SE)

OBSERVATIONS

[SE2.2] Define secure deployment parameters and configurations.

Activities in this practice

observed relatively frequently

[SE2.4] Protect code integrity.

[SE2.5] Use application containers.

[SE2.6] Ensure cloud security basics.

39

33

31

36

LEVEL 3

SOFTWARE ENVIRONMENT (SE)

OBSERVATIONS

Activities in this practice

observed least frequently

or are newly added

[SE3.2] Use code protection.

[SE3.3] Use application behavior monitoring and diagnostics.

[SE3.5] Use orchestration for containers and virtualized environments.

[SE3.6] Enhance application inventory with operations bill of materials.

13

7

22

12

Table A. Natural Groupings of Activities. The observation rate leads to natural groupings of activities into those seen most often, often, and least often.

BUILDING SECURITY IN MATURITY MODEL (BSIMM) – VERSION 11   |   PAGE 3

KEY TAKEAWAYS FOR BSIMM11

This annual BSIMM report presents observed quantitative data on actual software security practices across 130
organizations. You will see these numbers throughout the document relative to software security activities, vertical
markets, champions programs, reporting lines, change over time, and much more. Each year, we gather these data through
hundreds of interviews with the individuals directly involved in making software security happen in their organizations.

During these interviews, we also learn what organizations think regarding how their software security initiatives (SSIs)
operate today and how they might need to operate in the future. We express that qualitative data throughout this
document as, for example, a guide to starting and maturing an initiative, as themes across many initiatives, and as
real-world examples within activity descriptions.

Below, we summarize some of that data as BSIMM11’s key takeaways.

1.  Engineering-led software security efforts are having success contributing to DevOps value streams in pursuit of resiliency.
•  CI/CD instrumentation and operations orchestration have become a normal part of the approach to software security

for some organizations and are influencing how SSIs are organized, designed, and executed. As an example, increasingly,
we see SSIs report through technology groups (20 of 130 firms) or to a CTO (21 of 130 firms) up to the CEO.
•  Engineering-led firms are changing how software security groups find internal talent and use it to scale their depth
and breadth. For instance, the satellite role (e.g., champion) is evolving rapidly in firms embracing DevOps and
DevSecOps to recruit members from cloud and related security-oriented roles and increasingly have them apply
their expertise as code for everyone’s benefit.

•  Some centralized software security groups (SSGs) are building bridges with the talent aggregating within cloud

security and digital transformation teams, as well as within forward-looking development teams. This might reflect a
shift to SSG members delivering secure application functionality in places along the value stream rather than simply
putting in place governance as defect discovery.

•  Cloud service providers offer a shared responsibility model that makes SSIs contend with what is effectively

compulsory outsourcing of at least parts of security architecture, feature provisioning, and other SSI practice areas
that are traditionally done 100% locally. Ensuring proper risk management across all cloud provider resources for all
engineering teams is a key concern.

2.  Software-defined security governance is no longer just aspirational.

•  Digital transformation initiatives are incorporating security activities into their efforts to provide some manner of
CI/CD-pipeline-as-a-service and more broadly make software delivery self-service for development teams. In so
doing, previously high-friction security activities conducted by the SSG out-of-band and at gates are becoming
more transparent and are increasingly applied by default as part of pipeline execution. Some have made significant
progress on a goal of governance-as-code.

•  The three activities added for BSIMM10 described a clear arc—software-defined lifecycle governance,

software-assisted monitoring of software-defined asset creation, and automated verification of software-defined
infrastructure—which shows that some organizations are actively working on ways to speed up security to match the
speed with which the business delivers functionality to market. BSIMM11 captures the continued evolution of this
arc with the addition of activities for implementing event-driven security testing [ST3.6] and publishing risk data for
deployable artifacts [CMVM3.6].

•  Assigning repetitive analysis and procedural tasks to bots, sensors, and other automation is increasingly the way

organizations choose to address people and skills shortages, as well as cadence management problems. For example,
converting to algorithms the decision-making on what security tools to run when often removes a variety of human
processes from the application lifecycle.

3.  Security is becoming part of a quality practice, which is being recognized as part of reliability, all in pursuit of resilience.
•  Many activities that were traditionally siloed and expert-driven are evolving into a set of technologies and processes

that provide needed insight to a target audience and do so in cadence. As a technology example, there are now
SAST tools ranging from fast-running open source that target specific single-language issues to full-program
behavioral analysis tools with much longer execution cycles. While results from the former often support the quality
and reliability goals in development, it is usually the latter that are able to support the security and resilience goals in
the governance cycles.

PAGE 4   |   BUILDING SECURITY IN MATURITY MODEL (BSIMM) – VERSION 11

•  Engineering groups are building capabilities focused on inventorying software, cataloging its components, and

capturing the means by which it was built, configured, and deployed. Rather than attempting to find all problems
before deployment, for example, many DevOps groups continue to optimize by knowing what is running where and
by creating capabilities to restart or re-deploy patched or misbehaving software, which focuses on groundwork for
resilience in response to a variety of drivers—security telemetry included.

•  Because they’re often free, easy to find, and easy to use, engineering-led cultures tend to start with open source
or “freemium” security tools to accomplish various in-band automated code review and testing activities. The
organization’s larger, commercial security testing tools that execute over extended periods typically continue to get
used at checkpoints relevant to governance groups, with those tests usually being out-of-band of CI/CD pipelines
due to the time taken to execute and the friction introduced.

•  Rapidly evolving cloud and platform security features, as well as branching strategies, deployment strategies,

•

site reliability approaches, and so on, are making it easier for some engineering teams to align more closely with
resilience as a primary goal for their software rather than simply security or quality.
In the software world, many organizations now have engineers for security, quality, reliability, and resilience
(in addition to the traditional core, infrastructure, network, and other types of engineers). These roles each have
their own objectives, timelines, cultures, and guardrails, as well as their own group of people telling them what
they’ve done wrong without necessarily collaborating broadly on what works best for everyone. No one can boil the
ocean and manage all this change at once, necessitating bridge-building and prioritization in pursuit of organizational
success over group goals.

4.  “Shift Left” is becoming “Shift Everywhere.”

•  Although shift left has been promoted as doing some security testing during development, that is a large

simplification of what we meant. More accurately today, some secure software development lifecycles (SSDLs) seek
to conduct an activity as quickly as possible with the highest fidelity as soon as the artifacts on which that activity
depend are made available. Sometimes, that’s to the left of where you’re doing things today, but often times, it’s
to the right. In addition, technology trends naturally require shifting right to produce rapid and accurate telemetry
from modern languages, frameworks, and software orchestration.

•  Established practices such as secure code review are leveraging enhanced source code management features to allow
review during multiple phases. For example, shift left to initial code commits and shift right to augment metadata
offered as part of pull requests sent to repository maintainers when code is finished and tested. These options reflect a
desire to present results both where they can be achieved the soonest and where they will be most impactful.

•  Some organizations evaluating defect discovery tools and services are showing a growing preference for continuous

event-based security telemetry throughout a value stream rather than a single point-in-time analysis.

•  Those organizations attempting to maintain accurate software inventory data are discovering the need to align

efforts across source code content management, the build process, the deployment process, and the operations
environment, where inventory granularity and content will likely be different with each view and will also change
frequently. Such organizations are struggling to maintain the effectiveness of their existing inventory efforts while
also adapting to new software lifecycles, software architecture changes and any underlying software, deployment,
and cloud technologies changes happening in response to the engineering self-service trends and the digital
transformation sea change.

Of course, other large trends demand attention and perhaps haven’t yet shown their true impact on software security.
In particular, and anecdotally, the current world and political climate has caused significant changes in software
security processes, technology, and resourcing. As one point, we hear stories of a significant slow-down in hiring in
many organizations and a mandate to get both this year’s and next year’s goals done with existing staff and technology.
Primarily, we see this implemented as a significant acceleration in process automation, in applying some manner of
intelligence through sensors to prevent people from becoming process blockers, and in the start of a cultural acceptance
that going faster means not everything (e.g., not all desired security testing) can be done in-band of the delivery
lifecycle before deployment.

BUILDING SECURITY IN MATURITY MODEL (BSIMM) – VERSION 11   |   PAGE 5

ACKNOWLEDGMENTS

Our thanks to the 130 executives from the SSIs we studied from around the world to create BSIMM11, including
those who choose to remain anonymous.

Adobe
Aetna
Alibaba
Ally Bank
Autodesk
Axway
Bank of America
Bell
BMO Financial Group
Black Duck Software
Black Knight Financial Services
Box
Canadian Imperial Bank of
Commerce
City National Bank
Cisco
Citigroup
Dahua
Depository Trust & Clearing
Corporation
Eli Lilly
Equifax
Experian

F-Secure
Fannie Mae
Freddie Mac
General Electric
Genetec
Global Payments
HCA Healthcare
Highmark Health Solutions
Honeywell
Horizon Healthcare Services, Inc.
HSBC
iPipeline
Johnson & Johnson
JPMorgan Chase & Co.
Lenovo
MassMutual
McKesson
Medtronic
Morningstar
Navient
Navy Federal Credit Union
NCR

NEC Platforms
NetApp
NewsCorp
NVIDIA
PayPal
Pegasystems
Principal Financial Group
Royal Bank of Canada
SambaSafety
ServiceNow
Synopsys
TD Ameritrade
The Home Depot
The Vanguard Group
Trainline
Trane
U.S. Bank
Veritas
Verizon
Verizon Media
Wells Fargo
Zendesk

Our thanks also to the nearly 120 individuals who helped gather the data for the BSIMM.

In particular, we thank Matthew Chartrand, Sagar Dongre, Michael Doyle, Eli Erlikhman, Jacob Ewers, Stephen Gardner,
Iman Louis, Daniel Lyon, Alistair Nash, Kevin Nassery, Donald Pollicino, and Denis Sheridan. In addition, we give a special
thank you to Kathy Clark-Fisher, whose behind-the-scenes work keeps the BSIMM science project, conferences, and
community on track.

Data for the BSIMM were captured by Synopsys. BSIMM10 and BSIMM11 were authored by Sammy Migues, Mike
Ware, and John Steven. BSIMM4–BSIMM9 were authored by Gary McGraw, Ph.D., Sammy Migues, and Jacob West.
BSIMM1–BSIMM3 were authored by Gary McGraw, Ph.D., Brian Chess, Ph.D., and Sammy Migues.

PAGE 6   |   BUILDING SECURITY IN MATURITY MODEL (BSIMM) – VERSION 11

BSIMM11 TABLE OF CONTENTS

PART TWO: BSIMM11
The BSIMM11 Framework ........................................... 39

The BSIMM11 Skeleton ...............................................40

What BSIMM11 Tells Us .............................................. 44

BSIMM11 and Industry Verticals Analysis .................. 47

Emerging Trends in BSIMM11 ...................................... 51
•  Activity Trends ............................................................. 51
        Trend: Governance as Code
        Trend: Continuous Defect Discovery
        Trend: Continuous Activity
        Trend: Security as Resilience and Quality
•  Data Trends ................................................................. 55

PART THREE: ACTIVITIES
Governance .................................................................. 59
•  Governance: Strategy & Metrics (SM) ................... 59
•  Governance: Compliance & Policy (CP) ................. 62
•  Governance: Training (T) ........................................... 64

Intelligence ....................................................................67
•  Intelligence: Attack Models (AM) ............................67
•  Intelligence: Security Features & Design (SFD) .... 69
•  Intelligence: Standards & Requirements (SR) ..........71

SSDL Touchpoints ........................................................73
•  SSDL Touchpoints: Architecture Analysis (AA) .....73
•  SSDL Touchpoints: Code Review (CR) ...................75
•  SSDL Touchpoints: Security Testing (ST) ................77

Deployment ...................................................................79
•  Deployment: Penetration Testing (PT).....................79
•  Deployment: Software Environment (SE) ..............80
•  Deployment: Configuration Management &

Vulnerability Management (CMVM) ...................... 82

Executive Summary .................................................... 3
•  Key Takeaways for BSIMM11 ...................................... 4
Acknowledgments ...................................................... 6

PART ONE: BACKGROUND
BSIMM History ......................................................... 9
The Model .................................................................. 9
Creating BSIMM11 from BSIMM10 ......................... 10
Roles in a Software Security Initiative....................... 12
•  Executive Leadership .................................................. 12
•  BSIMM Terminology................................................... 14
•  Software Security Group (SSG) ................................ 15
•  Satellite..........................................................................17
•  Everybody Else ............................................................ 18
Measuring Your Firm with the BSIMM .................... 20
Using the BSIMM to Start or Improve an SSI ...........22
•  SSI Phases ................................................................... 22
•  Traditional SSI Approaches ....................................... 23
•  The New Wave in Engineering Culture .................... 24
•  Convergence as a Goal .............................................. 26
•  A Description of Two Journeys ................................. 28
•  The Governance-Led Journey ................................... 29
•  Governance-Led Culture .......................................... 29

    Leadership

        Inventory Software
        Select In-Scope Software
        Ensure Host and Network Security Basics
        Do Defect Discovery
        Engage Development
        Select Security Controls
•  Maturing Governance-Led SSIs ...............................30
        Document and Socialize the SSDL
        Balance Detective and Preventive Controls
        Support Incident Response and Feedback
        to Development
•  Optimizing Governance-Led SSIs ............................ 32
        Progress Isn’t a Straight Line
        Push for Agile-Friendly SSIs
•  The Engineering-Led Journey ................................... 33
    •  Emerging Engineering-Led Culture ......................... 33

        Inventory Software
        Select In-Scope Software
        Ensure Host and Network Security Basics
        Choose Application Controls
•  Maturing Engineering-Led Efforts ........................... 36
        Upgrade Incident Response
        Do Defect Discovery
        Document the SSDL

    •  Optimizing Engineering-Led Efforts ........................ 38

BUILDING SECURITY IN MATURITY MODEL (BSIMM) – VERSION 11   |   PAGE 7

BSIMM11 LIST OF FIGURES
Figure 1. AllFirms vs. ExampleFirm Spider Chart ................... 22
Figure 2. SSG Evolution ............................................................ 25
Figure 3. BSIMM11 Participating Firms ...................................44
Figure 4. AllFirms Spider Chart ............................................... 46
Figure 5. Cloud vs. Internet of Things vs. Tech

Spider Chart ......................................................................... 47

Figure 6. Financial vs. Healthcare vs. Insurance

Spider Chart .........................................................................48
Figure 7. Tech vs. Healthcare Spider Chart ............................. 49
Figure 8. AllFirms vs. Retail Spider Chart ...............................50
Figure 9. Financial vs. FinTech Spider Chart ............................5 1
Figure 10. Round 1 Firms vs. Round 2 Firms

Spider Chart ......................................................................... 88

Figure 11. Round 1 Firms vs. Round 3 Firms

Spider Chart .......................................................................... 91
Figure 12. BSIMM Score Distribution ................................... 100

APPENDIX
Building a Model for Software Security ................................... 85
The BSIMM as a Longitudinal Study ........................................ 87
Charts, Graphs, and Scorecards ............................................... 92
Comparing Verticals ................................................................. 101
121 BSIMM Activities at a Glance .......................................... 105
Model Changes over Time .........................................................112

BSIMM11 LIST OF TABLES
Table A. Natural Groupings of Activities ....................................3
Table 1. New Activities ................................................................. 11
Table 2. The Software Security Group .......................................17
Table 3. BSIMM11 ExampleFirm Scorecard ............................. 21
Table 4. BSIMM11 Scorecard .................................................... 45
Table 5. Most Common Activities per Practice .......................57
Table 6. Top 20 Activities by Observation Count ................... 58
Table 7. BSIMM Numbers Over Time ..................................... 86
Table 8. BSIMM11 Reassessments Scorecard
  Round 1 vs. Round 2............................................................. 87
Table 9. BSIMM11 Reassessments Scorecard
  Round 1 vs. Round 3 ............................................................90
Table 10. BSIMM11 Skeleton ..................................................... 92
Table 11. Vertical Comparison Scorecard ................................ 101
Table 12. Activity Changes Over Time .....................................112

PAGE 8   |   BUILDING SECURITY IN MATURITY MODEL (BSIMM) – VERSION 11

PART ONE: BACKGROUND

The BSIMM is now in its eleventh iteration. In this section, we talk about its history and the underlying model, as well as
the changes we made for BSIMM11. We describe the roles we typically see in an SSI and some related terminology. We
conclude this section with guidance on how to use the BSIMM to start, mature, and measure your own SSI.

BSIMM HISTORY

We built the first version of the BSIMM a little over a decade ago (Fall 2008) as follows:

•  We relied on our own knowledge of software security practices to create the SSF (found in Part Two).

•  We conducted a series of in-person interviews with nine executives in charge of SSIs. From these interviews,

we identified a set of common activities, which we organized according to the SSF.

•  We then created scorecards for each of the nine initiatives that showed which activities the initiatives carry
out. To validate our work, we asked each participating firm to review the framework, the practices, and the
scorecard we created for their initiative.

Today, we continue to evolve the model by looking for new activities as participants are added and as current participants
are remeasured. We also adjust the model according to observation rates for each of the activities.

THE MODEL

The BSIMM is a data-driven model that evolves over time. We have added, deleted, and adjusted the levels of various
activities based on the data observed as the project has evolved. To preserve backwards compatibility, we make all changes
by adding new activity labels to the model, even when an activity has simply changed levels (e.g., we add a new CRx.x
label for both new and moved activities in the Code Review practice). When considering whether to add a new activity,
we analyze whether the effort we’re observing is truly new to the model or simply a variation on an existing activity. When
considering whether to move an activity between levels, we use the results of an intralevel standard deviation analysis and
the trend in observation counts.

Whenever possible, we use an in-person interview technique to conduct BSIMM assessments, done with a total of 211
firms so far. In addition, we conducted assessments for 10 organizations that have rejoined the community after once
aging out. In 50 cases, we assessed the software security group (SSG) and one or more business units as part of creating
the corporate SSI view.

For most organizations, we create a single aggregated scorecard, whereas in others, we create individual scorecards for the
SSG and each business unit assessed. However, each firm is represented by only one set of data in the model published
here. (“Table 7. BSIMM Numbers Over Time” in the appendix shows changes in the data pool over time.)

As a descriptive model, the only goal of the BSIMM is to observe and report. We like to say we visited a neighborhood to
see what was happening and observed that “there are robot vacuum cleaners in X of the Y houses we visited.” Note that
the BSIMM does not say, “all houses must have robot vacuum cleaners,” “robots are the only acceptable kind of vacuum
cleaners,” “vacuum cleaners must be used every day,” or any other value judgements. We offer simple observations
simply reported.

BUILDING SECURITY IN MATURITY MODEL (BSIMM) – VERSION 11   |   PAGE 9

Of course, during our assessment efforts across hundreds
of organizations, we also make qualitative observations about
how SSIs are evolving and report many of those as key
takeaways, themes, and other topical discussions in
this document.

Our “just the facts” approach is hardly novel in science and
engineering, but in the realm of software security, it has not
previously been applied at this scale. Other work around
modeling SSIs has either described the experience of a single
organization or offered prescriptive guidance based purely on
a combination of personal experience and opinion.

CREATING BSIMM11 FROM
BSIMM10

Our ‘just the facts’ approach

is hardly novel in science and

engineering, but in the realm

of software security, it has

not previously been applied

at this scale.

BSIMM11 includes updated activity descriptions, data from 130 firms in multiple vertical markets, and a longitudinal
study. For BSIMM11, we added 27 firms and removed 19, resulting in a data pool of 130 firms. In addition, 14 firms
conducted reassessments to update their scorecards, and we assessed additional business units for five firms.

We used the resulting observation counts to refine activity placement in the framework, which resulted in moving four activities
to different levels. In addition, we added two newly observed activities, resulting in a total of 121 activities in BSIMM11.

Changes made for BSIMM11

•  [T2.6 Include security resources in onboarding] became T1.8.

•  [CR2.5 Assign tool mentors] became CR1.7.

•  [SE3.4 Use application containers] became SE2.5.

•  [SE3.7 Ensure cloud security basics] became SE2.6.

•  [ST3.6 Implement event-driven security testing in automation] added to the model.

•  [CMVM3.6 Publish risk data for deployable artifacts] added to the model.

We also carefully considered but did not adjust [CMVM2.2 Track software bugs found in operations through the fix process]
at this time; we will do so if the observation rate continues to increase. Similarly, we considered and did not adjust [ST2.1
Integrate black-box security tools into the QA process] but will do so if the observation rate continues to increase.

As concrete examples of how the BSIMM functions as an observational model, consider the activities that are now
SM3.3 and SR3.3, which both started as level 1 activities. The BSIMM1 activity [SM1.5 Identify metrics and use them
to drive budgets] became SM2.5 in BSIMM3 and is now SM3.3 due to its observation rate remaining fairly static while
other activities became observed much more frequently. Similarly, the BSIMM1 activity [SR1.4 Use coding standards]
became SR2.6 in BSIMM6 and is now SR3.3 as its observation rate has decreased. To date, no activity has migrated from
level 3 to level 1, but we see significant observation increases in recently added cloud- and DevOps-related activities.

PAGE 10   |   BUILDING SECURITY IN MATURITY MODEL (BSIMM) – VERSION 11

ACTIVITY

BSIMM7
OBSERVATIONS

BSIMM8
OBSERVATIONS

BSIMM9
OBSERVATIONS

BSIMM10
OBSERVATIONS

BSIMM11
OBSERVATIONS

NEW ACTIVITIES

SE3.4 (now SE2.5)

0

4

SE3.5

SE3.6

SE3.7 (now SE2.6)

SM3.4

AM3.3

CMVM3.5

ST3.6

CMVM3.6

11

0

0

0

14

5

3

9

0

0

0

31

22

12

36

1

4

8

0

0

Table 1. New Activities. Some of the most recently added activities have seen exceptional growth in observation counts, perhaps
demonstrating their widespread utility.

We noted in BSIMM7 that, for the first time, an activity ([AA3.2 Drive analysis results into standard architecture
patterns]) was not observed in the current dataset, and there were no new observations of AA3.2 for BSIMM8. AA3.2
did have two observations in BSIMM9 and one observation in both BSIMM10 and BSIMM11; there are currently no
activities with zero observations (except for the two just added).

Where Do Old Activities Go?
We continue to ponder the question, “Where do activities go when no one does them anymore?” In addition to
SR3.3 mentioned above, we’ve noticed that the observation rate for other seemingly useful activities has decreased
significantly in recent years:

•  [T3.6 Identify new satellite members through observation] – observed in 11 of 51 firms in BSIMM4 and 1

of 130 firms in BSIMM11.

•  [AA3.3 Make the SSG available as an AA resource or mentor] – observed in 20 of 67 firms in BSIMM-V

and 6 of 130 firms in BSIMM11.

•  [CR3.5 Enforce coding standards] – observed in 13 of 51 firms in BSIMM4 and 12 of 130 firms in BSIMM11.

We believe there are two primary reasons why observations for some activities decrease toward zero over time. First,
some activities become part of the culture and drive different behavior. For example, the SSG may not need to
select satellite members if there is a good stream of qualified volunteers from the engineering groups. Second, some
activities don’t yet fit tightly with the evolving culture, and doing it currently causes too much friction. For example,
continuously going to the SSG for design discussions might unacceptably delay key value streams.

It may also be the case that evolving SSI and DevOps architectures are changing the way some activities are
getting done. For example, if an organization’s use of purpose-built architectures, development kits, and libraries
is sufficiently consistent, perhaps it’s less necessary to lean on prescriptive coding standards as a measure of
acceptable code.

BUILDING SECURITY IN MATURITY MODEL (BSIMM) – VERSION 11   |   PAGE 11

Just as a point of culture-driven contrast, we see significant increases in observation counts for activities such as
[SE2.5 Use application containers], [SE3.5 Use orchestration for containers and virtualized environments], and
[SM2.1 Publish data about software security internally] likely for similar reasons that we see lower counts for the
activities above. The culture has shifted to be more self-service in engineering and to increased telemetry that
produces more data for everyone.

We, of course, keep a close watch on the BSIMM data pool and will make adjustments if and when the time comes, which
might include dropping an activity from the model.

Fifty-three of the current participating firms have been
through at least two assessments, allowing us to study how
their initiatives have changed over time. Twenty-one firms
have undertaken three BSIMM assessments, nine have done
four, and two have had five assessments.

BSIMM10 was our first study to formally reflect software
security changes driven by engineering-led efforts, meaning
efforts originating bottom-up in the development and
operations teams (often while they evolve into a DevOps
group) rather than originating top-down from a centralized
SSG. These results showed up here in the form of new
activities, in new examples of the way existing activities are
conducted, as well as in discussion of the paths organizations
might follow to maturation over time. We expanded that
analysis for BSIMM11.

It’s clear that—within

engineering-led initiatives

particularly—there’s a trend

toward collecting event-driven

security telemetry in addition

to or even rather than

conducting point-in-time

BSIMM11 also includes a brief “Trends” section that describes
shifts in SSI behavior affecting activity implementation
across multiple practices. Larger in scope than an activity, or
even a capability that combines activities within a workflow,
we believe these trends inform the way that initiatives execute groups of activities within their evolving culture. For
example, it’s clear that—within engineering-led initiatives particularly—there’s a trend toward collecting event-driven
security telemetry in addition to or even rather than conducting point-in-time scans that produce reports. This trend
fundamentally changes the way organizations interpret and implement multiple activities within the Governance, SSDL
Touchpoints, and Deployment domains.

scans that produce reports.

ROLES IN A SOFTWARE SECURITY INITIATIVE

Determining the right activities to focus on and clarifying who is responsible for their implementation are important parts
of making any SSI work.

EXECUTIVE LEADERSHIP
Historically, security initiatives that achieve firm-wide impact are sponsored by a senior executive who creates an SSG
where software security testing and operations are distinctly separate from software delivery. The BSIMM empowers
these individuals to garner resources and provide political support while maturing their groups. Those security initiatives
born within engineering and led solely by development management, by comparison, have historically had little lasting
impact firm-wide. Likewise, initiatives spearheaded by resources from an existing network security group usually run into
serious trouble when it comes time to interface with development groups.

PAGE 12   |