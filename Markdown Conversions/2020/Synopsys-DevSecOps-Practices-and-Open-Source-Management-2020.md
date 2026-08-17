DEVSECOPS PRACTICES
AND OPEN SOURCE
MANAGEMENT IN 2020
A SURVEY OF 1,500 IT PROFESSIONALS

TABLE OF CONTENTS
Introduction ................................................................................................................................................................................2
Section 1: Survey Highlights ......................................................................................................................................................4
DevOps and the secure SDLC ......................................................................................................................................................................................................5
DevSecOps tools ............................................................................................................................................................................................................................7
Open source selection and governance.....................................................................................................................................................................................8
Open source security and patching ..........................................................................................................................................................................................10
Open source project sustainability............................................................................................................................................................................................12
Conclusion: Developing security in depth for the SDLC ........................................................................................................................................................13
Section 2: Full Survey Results .................................................................................................................................................15
Respondent demographics ........................................................................................................................................................................................................16
Questions .......................................................................................................................................................................................................................................18
DEVSECOPS PRACTICES AND OPEN SOURCE MANAGEMENT IN 2020 | synopsys.com | 1

INTRODUCTION
DEVSECOPS PRACTICES AND OPEN SOURCE MANAGEMENT IN 2020 || ssyynnooppssyyss..ccoomm || 22

In August 2020, the Synopsys Cybersecurity Research Center The group was recruited to take part in an online survey
(CyRC) and Censuswide, an international market research focused on DevSecOps practices and open source use.
consultancy, conducted a survey of 1,500 IT professionals Participants came from the United States, the United
with DevSecOps as part of their role and who work in cyber Kingdom, Finland, Germany, China, Singapore, and Japan,
security, software development, software engineering, and with at least 50 respondents from each country. The survey is
web development. part of CyRC’s ongoing research into cyber security practices
and is intended as a complement to Synopsys’ annual Open
Source Security and Risk Analysis (OSSRA) report.
As the 2020 OSSRA report1 details, almost 100% of the 1,200+
This survey reports on
audited codebases in that report contained open source
components or libraries, with open source making up 70% of
the tools organizations in
the codebases themselves. Gartner’s report, “Market Guide
for Software Composition Analysis,”2 relates that due to the
the business of building prevalence of open source in modern software development,
corporate interest in software composition analysis (SCA)
tools used to manage open source is growing rapidly, with
software are employing to
inquiries to the analyst firm on the topic increasing nearly 40%
from 2019 to 2020.
integrate open source
While the OSSRA report provides an in-depth snapshot of the
current state of open source security, compliance, and code
management into their quality risk, this survey reports on the tools organizations in the
business of building software are employing to integrate open
source management into their DevOps practice. The survey
DevOps practice.
also explores the strategies being used to address open source
license compliance, vulnerability management, and the growing
issue of legacy open source in commercial code.
Section 1 of this report details the highlights of these survey
findings, and Section 2 includes full survey results.
DEVSECOPS PRACTICES AND OPEN SOURCE MANAGEMENT IN 2020 | synopsys.com | 3

Section 1
SURVEY HIGHLIGHTS
DEVSECOPS PRACTICES AND OPEN SOURCE MANAGEMENT IN 2020 || ssyynnooppssyyss..ccoomm || 44

DevOps and the secure SDLC How mature is the adoption of DevSecOps practices within
your team?
One of CyRC’s areas of interest in conducting this survey was
to investigate the prevalence of DevSecOps—the practice of Mature or deployed widely within our business
integrating security into every stage of the DevOps pipeline— Limited to use within specific projects, but expanding
across industry verticals and throughout organizations We’re still researching how to apply it
around the world. While we expected to find evidence of a We aren’t investigating DevSecOps practices at this time
DevSecOps trend, our results point to a more mature adoption Immature or running pilot programs
of DevSecOps among respondents than anticipated. Not sure
Thirty-three percent of the respondents noted that their
organizations are well on their way to a mature deployment 6%
of DevSecOps. An additional 30% reported that they are
making measurable strides toward maturity. With a combined 10% 33%
63% of respondents reporting that they are incorporating
some measure of DevSecOps activities into their software
development pipelines, it’s safe to say that adoption of the
10%
DevSecOps methodology is an important, rapidly growing
trend.
11%
30%
Figure 1
DEVSECOPS PRACTICES AND OPEN SOURCE MANAGEMENT IN 2020 | synopsys.com | 5

Synopsys’ 2020 Building Security in Maturity Model (BSIMM) Who, if anyone, is responsible for application security in
report,3 which looks at the current state of application security your organization?
across a large number of organizations, notes that “the idea
of baking security into all phases of a DevOps life cycle is
42% Security team
quickly becoming the norm. But organizations are adopting
this approach in their own ways and at their own pace.”
29% Development
Tellingly, 42% of respondents to our survey have a dedicated
security team. Also known as a software security group (SSG),
18% Shared by one or more team
this team’s responsibility may include acquiring, creating,
deploying, and managing secure software. Having an SSG
is another indicator of maturity in an organization’s software 9% Operations
security practices, according to the Synopsys BSIMM report as
Figure 2
well as other benchmarking tools for software security initiatives.
42% of respondents have a dedicated
security team whose responsibility may
include acquiring, creating, deploying, and
managing secure software.
DEVSECOPS PRACTICES AND OPEN SOURCE MANAGEMENT IN 2020 | synopsys.com | 6

DevSecOps tools Which, if any, of the following security tools does your team
currently use?
Figure 3 indicates that many organizations in the business
of building software need to increase their investments in
software composition analysis (SCA) and interactive application 45% Web application firewall
security testing (IAST), which enable security automation at the
development phase. Successful DevSecOps strategies entail 38% Software composition analysis (SCA)
a full security toolset—including dynamic application security
testing (DAST), IAST, static analysis security testing (SAST),
37% Dynamic application security testing (DAST)
and SCA tools—to fully address code quality and security flaws
early in the software development life cycle (SDLC).
37% Intrusion/detection protection system
SCA tools are employed by 38% of the respondent
organizations. SCA products analyze applications throughout
the entire SDLC to detect open source software. These tools 34% Runtime application self-protection (RASP)
typically produce an inventory, or Bill of Materials (BOM), of
all open source in the codebase, the versions of that open 33% Static analysis security testing (SAST)
source, the download locations for each project and all
dependencies, the libraries the code calls to, and the libraries
33% Interactive application security testing (IAST)
those dependencies themselves link to.
SCA tools also advise of known open source vulnerabilities
27% Penetration testing
found in the code, available security patches, and the
license(s) used to distribute the respective open source
packages. Comprehensive SCA solutions also monitor the 23% Protocol or API fuzzing
BOM to provide customers with early notification of new
vulnerabilities, and even deliver upgrade/patch guidance.
21% Container security
Of note is that the tool with the highest adoption rate is still
only utilized by 45% of respondents, indicating that there is no
7% None of the above
universally adopted application security tool.
Figure 3
DEVSECOPS PRACTICES AND OPEN SOURCE MANAGEMENT IN 2020 | synopsys.com | 7

Open source selection and Does your organization have a published policy for open
source use?
governance
The survey results indicate that most respondents’
72% Yes 28% No
organizations are at a relatively high level of maturity when it
Figure 4
comes to how they select open source and how they ensure
that their policies on open source use are being followed. An
overwhelming percentage—72%—have a published policy
on open source use. The majority of those policies define
Which, if any, of the following requirements are true for your
acceptable open source licenses; 55% prescribe patching/
policy on open source use? (Select all that apply)
updating requirements, and close to half define open source
components that are acceptable for use.
62% Defines acceptable open source licenses
An interesting question arises when correlating these
results and the results shown in Figure 3. While only 38%
of respondent companies use an SCA tool, 72% have a 55% Prescribes patch or update requirements
published policy for open source use.
Without an automated tool, are 34% of the respondents’ 49% Provides a whitelist or blacklist of components
companies employing manual processes to manage open
source? Are they depending on a developer honor system
that policies are being followed? The survey results indicate 47% Includes a manual review process from groups outside your
team
that—as Gartner’s 2020 report “Market Guide for Software
Composition Analysis” also relates—corporate adoption of
47% Includes standards around the age of components
SCA tools is still at a relatively early stage. On the other hand,
Gartner also relates that interest in SCA is growing rapidly,
Figure 5
with inquiries to the analyst firm on the topic increasing nearly
40% from 2019 to 2020.
DEVSECOPS PRACTICES AND OPEN SOURCE MANAGEMENT IN 2020 | synopsys.com | 8

A large majority (64%) of the respondents’ organizations also Do you have an open source governance board or specific
have a specific individual or board of governors charged with individual charged with open source governance?
open source oversight and whose responsibilities include
developing open source governance processes, setting use
64% Yes 36% No
policies, and defining acceptable open source components
for organizational use (see Section 2—survey question, Which, Figure 6
if any, of the following are true for the governance board/
individual?).
Security and a component’s vulnerability to exploit was top- What criteria is used in the vetting process for a new open
of-mind to 50% of respondents, and the #1 selection criterion source component? (Select all that apply)
when vetting a new open source component. Completeness
of a component’s implementation, frequency of releases/
50% Research on known vulnerabilities
patches, license restrictions, and community viability were
also cited as important considerations in the decision
process. 45% Completeness of component’s implementation
Forty-four percent of respondents noted that their team’s
familiarity or involvement with the component’s development
44% Development team’s familiarity with the component or its
or with its community (28%) were important factors in their community
decision. Both are welcome percentages to see, as one of the
factors leading to open source’s successful adoption is the
44% Frequency of releases/patches
volunteer communities improving and updating code.
40% Research on license restrictions
34% Viability of community
28% One of our team members is directly engaged with the
community
Figure 7
DEVSECOPS PRACTICES AND OPEN SOURCE MANAGEMENT IN 2020 | synopsys.com | 9

Open source security and patching When a critical open source vulnerability is identified by
your organization, on average, how long does it take for
Somewhat troubling were the results in the respondents’
your teams to provide a fix?
answers to the question of patching. Over half—51%—say
it takes 2 to 3 weeks for their organization to apply an open
51% In 2-3 weeks
source patch, with 24% noting that it can take up to a month,
even when the patch addresses a critical issue.
Parsing the results by country, it appears that the United 24% In a month
States is being most heavily impacted by unpatched open
source components. Over half of respondent organizations
16% Within a week
in the U.S. have had their software delivery schedule affected
in the past year because of addressing a critical open source
patch, compared to 40% globally. 5% We have not had to address a critical open source vulnerability
Based on the survey results, many organizations—especially
in the U.S.—would be well-advised to explore accelerating their
5% Not sure
time-to-patch schedules. When a vulnerability is disclosed,
you’re in a race with attackers. For example, in March 2017, Figure 8
a critical vulnerability in the Apache Struts open source
framework was publicly disclosed. Security researchers
observed a high number of exploitation attempts almost
Has addressing a critical open source patch impacted your
immediately after disclosure. In fact, on the same day as
software delivery schedule within the past year?
the disclosure, information about how to exploit the Apache
Struts flaw was posted to several websites popular with
Global
hackers.
40% Yes 53% No 7% Not in the
Thousands of organizations were attacked, and even though
past year
many applied the patch to their systems immediately, the
United States
attacks kept coming. All it took to create the conditions for a
breach was for one department at one firm to miss patching
52% Yes 42% No 6% Not in the
a version of Struts containing the vulnerability—and that past year
breach happened at a company called Equifax. Figure 9
DEVSECOPS PRACTICES AND OPEN SOURCE MANAGEMENT IN 2020 | synopsys.com | 10

The media comes under regular—sometimes deserved— Has media coverage of an open source issue ever caused your
criticism from the open source community for exaggerating organization to do any of the following? (Select all that apply)
security incidents and the risk of open source use.
However, most coverage notes that the risk comes from
46% Place more stringent controls on open source usage
the unmanaged use of open source, with reported incidents
usually involving unpatched or outdated components, or the
lack of an up-to-date software inventory, one of the primary 45% Put open source management tools in place to address
risk (i.e., SCA)
causes behind the Equifax data breach.4
Our survey results demonstrate that media coverage of open
36% Use different open source components
source issues definitely affects how organizations manage
their open source use. Forty-six percent of respondents noted
that media coverage had prompted their organization to apply 33% Use commercial components in place of open source
more stringent controls on open source usage.
10% No open source issue reported by the media has impacted us
10% None of the above
Figure 10
46% of respondents noted that coverage of open
source issues definitely has an effect on how
their organizations manage open source.
DEVSECOPS PRACTICES AND OPEN SOURCE MANAGEMENT IN 2020 | synopsys.com | 11

Open source project sustainability Which, if any, of the following requirements are true for your
policy on open source use?
As shown in the highlighted section from Figure 5, 47% of
respondents’ organizations define standards around the
62% Defines acceptable open source licenses
age of open source components, an acknowledgement of
a growing problem in the open source community—project
sustainability.
55% Prescribes patch or update requirements
There’s no guarantee that the people behind any given open
source project will continue maintaining the code. In fact,
of the 1,200+ codebases examined for the 2020 OSSRA 49% Provides a whitelist or blacklist of components
report, 88% contained open source components that had no
development activity in the last two years.5
47% Includes a manual review process from groups outside your
All software ages. As it ages, it loses support. With open team
source, the number of developers working to ensure
updates—including feature improvements, as well as security 47% Includes standards around the age of components
and stability updates—decreases over time. The component
Figure 5
becomes more likely to break without the support needed to
provide fixes. At some point, as that open source component
ages and the number of people who handle bug reports
and code reviews diminishes, the component becomes
increasingly likely to open a codebase to exploit.
Without policies in place to identify and manage the risks
that legacy open source can create, organizations open
themselves up to the possibility of issues in their software.
DEVSECOPS PRACTICES AND OPEN SOURCE MANAGEMENT IN 2020 | synopsys.com | 12

Conclusion: Developing security in Taking the steps toward a more secure SDLC
If the findings in this report mirror your organization’s current
depth for the SDLC
software development environment and you’re looking toward
Organizations are producing and deploying software applications a more secure SDLC, an objective analysis of the maturity
faster than ever before. Ensuring that developers are on board level of your software security efforts can be an invaluable
with security practices is even more critical to improving their first step.
efficiency. The Forrester report, “The State of Application
A benchmarking tool such as the Building Security in Maturity
Security, 2020" notes, “To meet developer needs, security pros
Model (BSIMM) report is designed to help CISOs and security
must integrate application security testing tools into the CI/
leaders objectively measure existing security practices and
CD pipeline and enable scans to run automatically on check-
identify areas for improvement within their organization.
in, build, and integration while also enabling autoremediation
The BSIMM gives an objective, data-driven view into your
to make mitigating security flaws quick and painless.”
current software security initiative and includes key areas
we’ve reviewed in this report, such as patching third-party
components used in software development, test automation,
“Firms must move
and the impact of DevSecOps practices.
Armed with the results of an independent assessment of your
faster at pushing
current practices, you can develop a strategy to improve your
security practices in a structured and cost-efficient manner. If
prerelease testing
you’re looking for a software security roadmap, the Synopsys
Managed Services team has developed a series of Maturity
earlier in the SDLC.” Action Plans (MAPs) that can help chart a path to goals
ranging from developing an overall DevSecOps culture to
implementing more-targeted activities such as cloud security.
—Forrester report, “The State of Application Security, 2020”6
Avoiding application security testing pain
As the responses to the DevSecOps tools question indicate,
there is no shortage of application security tools and
techniques. But for many teams, each tool represents a pain
point within their development workflow—and that can slow
development efforts.
DEVSECOPS PRACTICES AND OPEN SOURCE MANAGEMENT IN 2020 | synopsys.com | 13

To ease some of that pain, vendors have focused on security updates probably won’t be tied to the same sprint
integrating their tools within CI/CD pipelines. While this can cycle or release interval used by a proprietary coding team.
help with tool deployment, it doesn’t really address the pain Default settings for a given open source component may not
felt by development teams. With over 50% of U.S. respondents align to an organization’s security policies.
and 40% of respondents worldwide indicating that addressing
Identifying risks associated with open source requires
an open source vulnerability impacted their delivery schedules,
an accurate understanding of all the open source used
it’s clear that unpatched vulnerabilities are a major source of
in an application, including the open source embedded
developer pain. But so too are tools that slow down or generate
within commercial libraries. This is the role that SCA
additional work for development teams.
tools like Synopsys Black Duck® provide—starting with a
Contextual information is key to addressing security pain. comprehensive software Bill of Materials (BOM). An accurate,
For example, if a developer can see in their IDE that a feature up-to-date software BOM of open source components allows
won’t pass a security policy check, they can adjust the you to pinpoint vulnerable components quickly and prioritize
implementation to meet the policy. Empowering developers remediation efforts appropriately.
in this way is one objective of the Synopsys Code Sight™ IDE
As noted in the survey results, many organizations—
plugin. Code Sight provides both SAST and SCA information to
especially those in the United States—should accelerate their
developers, so they can find and fix open source and proprietary
time-to-patch schedules. Over half say that it currently takes
security defects as they code. And it does so in manner familiar
two to three weeks to apply a patch. A production-grade
to anyone who has used an IDE syntax checker.
SCA solution is the key to reducing patching timelines from
Context is also an attribute of runtime validation technologies. weeks to days by providing continuous monitoring for new
Using Seeker®, Synopsys’ IAST tool, to test an application vulnerabilities and giving guidance on mitigation.
provides actionable value to a security-minded development
team. Armed with data flows and call graphs targeting the
vulnerability, development teams can quickly remediate an
References
issue—and Seeker automatically confirms that the issue has
1. Synopsys Cybersecurity Research Center, “2020 Open Source Security and Risk Analysis Report,”
been resolved. Synopsys, May 2020.
2. Dale Gardner, “Market Guide for Software Composition Analysis,” Gartner, August 2020.
3. Sammy Migues, John Steven, and Mike Ware, “Building Security in Maturity Model,” Synopsys, 2020.
Know your risks
4. Permanent Subcommittee on Investigations, How Equifax Neglected Cybersecurity and Suffered a
Devastating Data Breach, Committee on Homeland Security and Governmental Affairs, U.S. Senate,
It’s important to remember that security practices employed
accessed September 12, 2020.
by an open source development team are likely different than 5. Synopsys Cybersecurity Research Center, “2020 Open Source Security and Risk Analysis Report,”
Synopsys, May 2020.
those of an internal team creating custom code. Open source
6. Sandy Carielli, “The State Of Application Security, 2020,” Forrester, May 2020.
DEVSECOPS PRACTICES AND OPEN SOURCE MANAGEMENT IN 2020 | synopsys.com | 14

Section 2
FULL SURVEY RESULTS
DEVSECOPS PRACTICES AND OPEN SOURCE MANAGEMENT IN 2020 || ssyynnooppssyyss..ccoomm || 1155

Respondent demographics
| 8%    |     | 5%    | 7%              |     |     |
| ----- | --- | ----- | --------------- | --- | --- |
| 55+   |     | 16-24 | Web development |     |     |
| 15%   |     |       | 21%             |     |     |
| 45-54 |     |       | Software        |     |     |
engineering
|     | Age | 38%   |     | Job title | 52%       |
| --- | --- | ----- | --- | --------- | --------- |
|     |     | 25-34 |     |           | Software  |
development
| 34%          |     |     | 21%            |     |     |
| ------------ | --- | --- | -------------- | --- | --- |
| 35-44        |     |     | Cyber security |     |     |
| 1%           |     |     |                |     | 3%  |
| Prefer  not  |     |     |                |     | 1-9 |
to say
9%
|     |     |     | 27%  |          | 10-49 |
| --- | --- | --- | ---- | -------- | ----- |
| 28% |     |     | 500+ |          |       |
|     |     |     |      | Company  | 20%   |
Female
|     | Gender | 71% |     |     |     |
| --- | ------ | --- | --- | --- | --- |
50-99
size
Male
15%
|     |     |     | 250-500 |     | 27% |
| --- | --- | --- | ------- | --- | --- |
100-249
      |  synopsys.com  |  16
DEVSECOPS PRACTICES AND OPEN SOURCE MANAGEMENT IN 2020

Respondents geographically
| 17% | 18% | 65% |
| --- | --- | --- |
North America (United States) Europe (Finland, Germany, U.K.) Asia (China, Japan, Singapore)
      |  synopsys.com  |  17
DEVSECOPS PRACTICES AND OPEN SOURCE MANAGEMENT IN 2020

Questions When selecting a new component or application, where
does your organization usually look? (Please select best
General match)
What types of applications does your team usually create or Mixture of both commercial and open source vendors ..............................34%
manage? (Select all that apply) Open source code repository (e.g., GitHub) ..................................................22%
Web services .......................................................................................................51% Commercial software vendors ........................................................................20%
Mobile applications ............................................................................................48% Vendor-supported open source component (e.g., Red Hat) ......................19%
Software libraries provided to third parties ...................................................44% We never select a new component or application .........................................5%
Packaged commercial software ......................................................................42% Other, please specify ......................................................................................0.60%
Firmware for embedded systems such as IoT, medical, or automotive..38%
Other (please describe) .......................................................................................4%
In your opinion, where does open source risk rank in your
organization compared to other AppSec risks
How mature is the adoption of DevSecOps practices within (e.g., proprietary code defects)?
your team? Equal to .................................................................................................................51%
Mature or deployed widely within our business ...........................................33% Higher ...................................................................................................................29%
Limited to use within specific projects, but expanding ...............................30% Lower ....................................................................................................................14%
We’re still researching how to apply it ............................................................11% Not sure ..................................................................................................................5%
We aren’t investigating DevSecOps practices at this time .........................10% Not applicable .......................................................................................................2%
Immature or running pilot programs ..............................................................10%
Not sure .....................................................................................................6%
Security and patching
Who, if anyone, is responsible for application security in
your organization?
Security team ......................................................................................................42%
Development .......................................................................................................29%
Shared by one or more team ............................................................................18%
Operations ..............................................................................................................9%
No one ....................................................................................................................1%
Other, please specify ......................................................................................0.20%
DEVSECOPS PRACTICES AND OPEN SOURCE MANAGEMENT IN 2020 | synopsys.com | 18

How is your team primarily informed of vulnerabilities or What, if anything, is your team’s primary source for open
weaknesses in the applications or services you create or source component security information?
manage? Software composition analysis (SCA) tool ....................................................33%
Alerts from security teams ...............................................................................27% Corporate software asset management tools ..............................................16%
Notification from security tools .......................................................................25% Internet (forums, mailing lists, etc.) ................................................................13%
Periodic audits ....................................................................................................14% NVD (or country-specific equivalent) ..............................................................11%
Customer support ..............................................................................................10% Package management tool ..............................................................................10%
Diligence review during procurement ...............................................................9% Threat intelligence feeds .....................................................................................8%
Our team is not informed in any specific way about vulnerabilities or News media ...........................................................................................................4%
weaknesses in our applications or services ...................................................6%
We don’t have a primary source of information for open source
External security researchers or bug bounties ...............................................5% component security information .......................................................................4%
Media coverage .....................................................................................................4% Other, please specify ......................................................................................0.44%
Other, please specify ......................................................................................0.27%
When an open source component's patch is issued, on
Which, if any, of the following security tools does your team average, how quickly does your organization apply the
currently use? (Select all that apply) patch?
Web application firewall ....................................................................................45% Within a week, please specify in days ............................................................13%
Software composition analysis (SCA) ............................................................38% In 2–3 weeks .......................................................................................................53%
Dynamic application security testing (DAST) ...............................................37% In a month ............................................................................................................23%
Intrusion/detection protection system ..........................................................37% Longer than a month .....................................................................................0.80%
Runtime application self-protection (RASP)..................................................34% Not sure ..................................................................................................................7%
Static analysis security testing (SAST) ..........................................................33% We have no open source component patching policy ..................................3%
Interactive application security testing (IAST) ..............................................33%
Penetration testing .............................................................................................27%
Has an unpatched open source component resulted in a
Protocol or API fuzzing ......................................................................................23%
security incident within your organization within the past
Container security ..............................................................................................21%
year?
None of the above ................................................................................................7%
Yes .........................................................................................................................29%
No/Unknown .......................................................................................................65%
Prefer not to say ......................................................................................6%
DEVSECOPS PRACTICES AND OPEN SOURCE MANAGEMENT IN 2020 | synopsys.com | 19

Has addressing a critical open source patch impacted your In your opinion, is the patching process for open source
software delivery schedule within the past year? components faster or slower than applying patches of the
Yes .........................................................................................................................40% commercial software you use?
No ..........................................................................................................................53% Faster ....................................................................................................................37%
We haven’t had to address a critical open source patch within the past Slower ...................................................................................................................24%
year ..........................................................................................................................7% About the same...................................................................................................33%
Not sure ..................................................................................................................6%
Has media coverage of an open source issue ever caused
your organization to do any of the following? (Select all that
In your opinion, where in the software development life
apply)
cycle (SDLC) is open source vulnerability management best
Place more stringent controls on open source usage ................................46% suited?
Put open source management tools in place to address risk (i.e., SCA) ...45% Development .......................................................................................................42%
Use different open source components ........................................................36% Testing ..................................................................................................................42%
Use commercial components in place of open source ..............................33% Deployment ..........................................................................................................12%
No open source issue reported by the media has impacted us ...............10% Not sure ..................................................................................................................3%
None of the above ..............................................................................................10% Other, please specify ......................................................................................0.51%
When a critical open source vulnerability is identified by
Selection, use, and governance
your organization, on average, how long does it take for
How are open source components selected within your
your teams to provide a fix?
organization? (Select all that apply)
Within a week ......................................................................................................16%
Developers can select open source components based on approved
In 2–3 weeks .......................................................................................................51% license types and their meeting security policies ........................................51%
In a month ............................................................................................................24% Developers must use preapproved components but can request that new
Longer than a month, please specify in months ......................................0.29% components be added to approval lists .........................................................47%
We have not had to address a critical open source vulnerability ................5% Developers have the freedom to select any component providing it is
currently patched and up to date ....................................................................37%
Not sure ..................................................................................................................5%
Developers can select any open source component without restriction 27%
Not sure ..................................................................................................................4%
DEVSECOPS PRACTICES AND OPEN SOURCE MANAGEMENT IN 2020 | synopsys.com | 20

What criteria is used in the vetting process for a new open What is the primary method used by your team to track
source component? (Select all that apply) open source usage in your apps?
Research on known vulnerabilities..................................................................50% SCA tool ................................................................................................................39%
Completeness of component’s implementation ..........................................45% Package managers ............................................................................................25%
Development team’s familiarity with the component or its community ..44% Individual developer tracks (through spreadsheet or other method) .......20%
Frequency of releases/patches .......................................................................44% N/A – We don’t use open source components ..............................................9%
Research on license restrictions .....................................................................40% We don’t track open source usage in our apps ..............................................8%
Viability of community .......................................................................................34% Other method, please specify ......................................................................0.53%
One of our team members is directly engaged with the community .......28%
Our team doesn’t usually vet open source components ..............................4%
Does your organization have a published policy for open
Other (please specify) ....................................................................................0.51%
source use?
Yes .........................................................................................................................72%
Which team manages the approval process for a new open
No ..........................................................................................................................28%
source component? Note: The following are from respondents who
answered “Yes” to “Developers must use preapproved components but can
request that new components be added to approval lists.” Which, if any, of the following requirements are true for your
Security team ......................................................................................................45% policy on open source use? (Select all that apply)
Development team .............................................................................................28% Defines acceptable open source licenses .....................................................62%
Operations team .................................................................................................15% Prescribes patch or update requirements .....................................................55%
Legal/Compliance team ....................................................................................11% Provides a whitelist or blacklist of components ..........................................49%
No particular team .........................................................................................0.77% Includes a manual review process from groups outside your team ........47%
Includes standards around the age of components ...................................47%
None of the above ..........................................................................................0.41%
Do you have an open source governance board or specific
individual charged with open source governance?
Yes .........................................................................................................................64%
No ..........................................................................................................................36%
DEVSECOPS PRACTICES AND OPEN SOURCE MANAGEMENT IN 2020 | synopsys.com | 21

Which, if any, of the following are true for the governance License compliance
board/individual? (Select all that apply)
How important is open source license compliance to your
Develops open source management processes ..........................................60% organization?
Sets policies and handles exceptions concerning open source usage ...58% Very important ....................................................................................................45%
Can whitelist specific open source components .........................................49% Somewhat important .........................................................................................48%
Provides training for the organization ............................................................46% Not very important ...............................................................................................6%
Can blacklist specific open source components .........................................45% Not at all important ........................................................................................0.80%
None of the above ..........................................................................................0.34%
Who has primary responsibility in your organization to verify
license compliance?
Open source project contributions
Security team ......................................................................................................38%
Does your organization have a published policy for its
Development .......................................................................................................28%
developers to make open source contributions?
Legal ......................................................................................................................17%
Yes .........................................................................................................................65%
Operations ............................................................................................................14%
No ..........................................................................................................................35%
We don’t verify license compliance ...................................................................1%
Other, please specify ......................................................................................0.44%
Which, if any, of the following is true for your open source
contribution policy? (Select all that apply)
Requires internal review of all potential code contributions ......................59%
Allows developers to agree to contributor license agreements ................55%
Requires registration of supported projects with HR or Legal ..................50%
Allows team members to support external users of the project ..............49%
None of the above ..........................................................................................0.78%
DEVSECOPS PRACTICES AND OPEN SOURCE MANAGEMENT IN 2020 | synopsys.com | 22

The Synopsys difference
Synopsys helps development teams build secure, high-quality software, minimizing risks while maximizing speed and
productivity. Synopsys, a recognized leader in application security, provides static analysis, software composition analysis, and
dynamic analysis solutions that enable teams to quickly find and fix vulnerabilities and defects in proprietary code, open source
components, and application behavior. With a combination of industry-leading tools, services, and expertise, only Synopsys helps
organizations optimize security and quality in DevSecOps and throughout the software development life cycle.
About CyRC
The Synopsys Cybersecurity Research Center (CyRC) works to accelerate access to information around the
identification, severity, exploitation, mitigation, and defense against software vulnerabilities. Operating within the
greater Synopsys mission of making the software that powers our lives safer and of the highest quality, CyRC helps
CyRC
increase awareness of issues by publishing research supporting strong cyber security practices.
For more information, go to www.synopsys.com/software.
Synopsys, Inc. Contact us:
185 Berry Street, Suite 6500 U.S. Sales: 800.873.8193
San Francisco, CA 94107 USA International Sales: +1 415.321.5237
Email: sig-info@synopsys.com
©2020 Synopsys, Inc. All rights reserved. Synopsys is a trademark of Synopsys, Inc. in the United States and other countries. A list of Synopsys trademarks is available at www.synopsys.com/copyright.html . All other names
mentioned herein are trademarks or registered trademarks of their respective owners. November 2020
DEVSECOPS PRACTICES AND OPEN SOURCE MANAGEMENT IN 2020 | synopsys.com | 23