Application
Cloud
Security
Security
Market
Market
Repor t
Repor t

Table of Contents
Executive Summary 3
2026 Application Security Survey Results 4
Application Security Timeline 11
The Current State of Application Security 16
Emerging Categories 28
Buyer’s Guides 36
Conclusion 44
Vendor Spotlights 46

Executive Summary
Whether you call it application security, product security, or DevSecOps, securing software is
complicated. Today, practitioners are expected to manage a growing set of scanners, reduce
large vulnerability backlogs, coordinate remediation across teams, and participate in
architecture and threat modeling, often with limited headcount and little tolerance for noise.
AI is adding to this complexity, amplifying both the risks and opportunities in application security.
AI assisted coding is reshaping how applications are built, deployed, and maintained. In parallel,
the capabilities of platforms themselves are evolving with AI: features from autofix workflows, to
false positive analysis, to scanning itself, are all radically changing product expectations.
This report is designed to help practitioners and buyers navigate the current application
security landscape. It covers the transitions in application security over time, from waterfall
development to DevOps to emerging AI code generation workflows. The report then breaks
down every subcategory of scanner, the development of modern features, as well as how AI
capabilities are changing functionalities we use today. We conclude with actionable buyer
guidance that spans across SMB, mid-market, and enterprise environments.
Key Takeaways
Application security has largely consolidated into platform players. The capability
differences have more to do with user, integration and developer experiences than pure
scanning functionalities.
AI-native static analysis and business logic detection are the most immediately
meaningful changes in Application Security detection capabilities. These new scanners
are capable of detecting entirely new categories of vulnerabilities which have traditionally
been reserved for manual review.
Application security evaluations should focus on usability and backlog reduction more
than specific scanner functionalities. Tool evaluations should be guided by the time to fix
an issue, rather than the number of issues detected.
ASPM as “management without scanning” has largely collapsed into broader vulnerability
management and exposure programs. ASPM is shifting into continuous threat exposure
management, or universal vulnerability management.
Securing AI-generated code is still an open market with unclear best practices. General
approaches involve giving organizational context to agents, and having secure code
reviews in pipelines, but this field is rapidly changing.
Supply chain security is expanding towards malware, package health, and secure-by-default
consumption patterns. CVE detection alone is not enough for modern supply chain security.
Application Security Market Report 2026 3

2026
APPLICATION
SECURITY
SURVEY
RESULTS

Survey Results
The application security survey spanned organizations from tens of developers to thousands. In
many ways, they reflected the reality of application security being a discipline in crisis - as teams
were split in their priorities, what they wanted out of a tool, and where they saw the industry going.
The key results were:
Developer experience is the most important deciding factor for new tools, followed by
false positive rates
AI pentesting is the most desired emerging capability
The top concern for 2026 is speed and security of AI generated code
Enterprise Doesn’t Always Use More Tools
Number of Developers
>1000
<1000
<100
<3 <5 <10
Median Number of Tools
Contrary to popular belief, the survey data indicated that smaller teams can actually use more
tools than enterprises, largely because they lean more heavily into open source offerings that
they orchestrate themselves. Enterprises, by contrast, tend to manage fewer tools overall, but
at a much larger scale. They are also more likely to rely on a smaller set of paid tools for specific
purposes, such as supply chain security, SAST, and DAST.
Application Security Market Report 2026 5

This data helps explain why ASPM, as a standalone management category, struggled to
survive. Enterprises with distributed scanning tools and capabilities never intended to
centralize everything under a single ASPM layer, and third-party integrations often served as a
stopgap rather than a durable, long-term strategy for tool orchestration. As we argued in our
Cloud report, ASPM is now evolving into the broader CTEM category, which approaches
vulnerability management in a more holistic way.
Developer Experience Matters
Ranked choice voting was completed for several key application security features. The results
are listed below in order of how practitioners voted.
The top 6 application security features:
1 Developer Experience
2 Least False Positives
3 Integrations
4 Most True Positives
5 Remediation Guidance
6 Reporting
The survey results are clear: practitioners are looking for tools that create the least friction with
their development teams. Poor developer experiences and high false positive rates are what
create friction with other teams, and are the top priorities teams have when assessing tools.
This is where user experience matters more than individual scanner finding quality.
Ultimately, practitioners want their security tools to feel invisible to the developer, having them
only be helpful nudges in the right direction rather than trying to find as many potential issues
as possible. This is why reachability analysis has become a critical component of application
security tools.
Application Security Market Report 2026 6

Core Application Security is SCA + SAST + Secrets
I expect my application security tool to provide:
SAST 51%
SCA 52%
Secrets 49%
DAST 9%
IaC 35%
Containers 8%
ADR 0%
CSPM 8%
No Bundling 46%
As much as security platforms, finance teams, and analysts alike see the value of bundled
application security offerings, the majority of practitioners still view only SCA, SAST, and
Secrets as part of a core application security offering. The other half of practitioners sometimes
included IaC scanning, DAST, and containers, or preferred to have no bundling at all.
While there are clear benefits from implementation and budgeting perspectives for having an
all-in-one solution, the core application security stack remain SAST, SCA, and Secrets scanning.
The SOC is Handling Runtime and WAF
Cloud
5% App
5%
What team handles runtime SOC
application security incidents? 42% Developers
17%
(e.g. WAF, Fraud, IR, or API abuse)
Product
Security
31%
Application Security Market Report 2026 7

Increasingly, security operations teams are being tasked with handling runtime application
security alerts, though ownership remains mixed. Cloud and product security teams are also
responsible for these alerts in many organizations, and in some cases developers are involved
as well. It is worth highlighting that these management functions no longer sit with traditional
network security teams, and have instead shifted toward broader security operations and
cloud teams.
This speaks to the growing importance of application-layer visibility for security operations
teams, as they are increasingly expected to handle more contextual and technical alerts.
The AI Features That Matter
Which AI feature are you the
most excited about?
Application security practitioners are ready to adopt the latest AI features - from prioritization
to static code analysis. The relatively low number of “none” responses is surprising, because it
suggests that practitioners in this area are less skeptical about AI’s ability to transform day to
day workflows than in other categories. Seeing the power of AI code generation directly makes
practitioners in this category more open to AI adoption.
While most AI features garnered similar levels of excitement, AI pentesting pulled a slight lead,
indicating that teams are excited about being able to make continuous pentesting a reality.
Overall it's clear that AI is transforming the capabilities of existing testing methodologies and
teams are ready for it.
Application Security Market Report 2026 8

The Gap is Runtime Context
My current application security tool needs to have:
A Better API 23%
More Integrations 11%
More CI/CD Customization 23%
Better IDE Experience 23%
AI SAST 14%
Better Cloud and Runtime Context 56%
Detection and Response 35%
AI Pentesting 27%
AI may be driving industry excitement, but usability remains the primary focus for immediate feature
enhancements. Specifically, better APIs, IDE state tracking, and integration experiences were highly
requested from practitioners. The most requested feature by far was better cloud and runtime
context, because teams want to better prioritize and determine the truth of a particular finding.
When reviewing the results alongside the preference to separate runtime and code
experiences, this finding highlights the need for strong integration between tools managed by
different teams to support vulnerability triage, false positive analysis, and delivering fixes.
Open Source or Not - Results Matter More
How do you feel about your
vendor using open source
scanners?
Application Security Market Report 2026 9

In 2026, practitioners care about end results more than a vendor's underlying scanning engine.
Historically, application security practitioners were split about the value of open source
scanning engines. About half of practitioners thought they were better than closed source,
because passionate developers for every coding language could add to the rule sets, keeping
them modern and useful. On the other hand, many other practitioners committed to closed
source engines, counting on vendors to do a more thorough job than open source communities.
In the time since, practitioners have come to better appreciate open source software, as well as
understand that the underlying scanning engine doesn’t matter as much as the rules that are
being applied to it. Most of the time, having customized and editable scanning rules matters
more than the engine that is searching the code for the patterns.
Application Security Priorities
What team handles runtime
What’s your top 2026
application security incidents?
application security concern?
Three concerns stood out most for 2026 priorities: Securing AI generated code, supply chain
malware, and getting budget. With a combined 84% of responses, AI generated code and
supply chain malware remain top of mind for security teams going into next year. These
categories have increased in priority in light of a steady stream of supply chain attacks,
combined with the rapid adoption of AI coding tools.
While teams recognize the need to move quickly, they increasingly require tools that enable
them to trust the results they’re seeing.
Application Security Market Report 2026 10

APPLICATION
SECURITY TIMELINE
Application security can be divided into four eras: waterfall, agile, platform, and AI. Each era
was introduced to address distinct concerns, many of which persist today, even as application
security has rapidly matured over the past decade.
| Waterfall | Agile     | Platform  | AI          |
| --------- | --------- | --------- | ----------- |
| 2000-2015 | 2015-2019 | 2019-2023 | 2023-Future |

hosted source code management software. Alongside this shift, the ability to scan code in
Early Application Security
pipeline created the fundamental promise of the “shift left” movement, an attempt to find
and fix vulnerabilities in code before they were deployed.
Before 2010, application security was a very different practice in terms of scope, market size, and day
Shifting left brought a utopian vision of application security - developers organically fixing
to day operations. For the most part, before the proliferation of cloud, DevOps, and B2B SaaS,
every vulnerability out of the overflow of their hearts. On the plus side, potential
application security was meaningfully practiced only by the largest software distributors. Companies
vulnerabilities were identified earlier in development, and teams got new insights into what
like Microsoft, Cisco, and IBM were the largest consumers and builders of application security services,
actually made up their software. On the negative side, developers were bombarded with
as they had real financial obligations to protect the consumers of their software. During this period,
confusing false positives, left spinning their wheels with pipelines blocked over nothing.
OWASP served as a volunteer-led consortium, guiding and developing best practices in real-time.
Nonetheless, the idea of getting findings directly to developers as they’re coding became
One primary challenge was developing scaling scanning solutions, primarily for static languages the driving force of application security.
like C and Java. Early solutions were built to support waterfall development workflows, where
annual software updates were compiled, uploaded to a platform, and a multi-hour (or multi-day)
scan would be kicked off. Then, security teams would work with developers to remediate any
discoveries before releasing major software versions.
While the workflow is not as common, the capabilities of these older scanners still serve a key
function for enterprises supporting legacy software. Older scanning engines also tend to be more
mature, offering styles of analysis and customization that many newer companies have ignored in
favor of targeting more cloud native development languages and deployment styles. Especially
for static languages, these years of research and development can’t be cloned overnight.
The Shift to Agile
The 2010s saw a massive change in how software was delivered:
Dynamic languages like Javascript and Python massively increased in adoption
The adoption of cloud hosted Git and CI/CD pipelines, alongside DevOps practices
The shift to agile development practices
Massive adoption of open source packages in software development
Shift to microservice driven development, APIs and containerization
These changes introduced a new wave of development and observability tools, from GitHub
to DataDog. At the same time, solutions like WhiteSource (now Mend), Sonatype, and Snyk
emerged, addressing both the growing importance of open source vulnerabilities and the
need for faster scan times.
These Software Composition Analysis (SCA) tools saw rapid adoption because existing
platforms did not yet support SCA capabilities, and didn’t integrate natively with cloud
Application Security Market Report 2026 12

hosted source code management software. Alongside this shift, the ability to scan code in
pipeline created the fundamental promise of the “shift left” movement, an attempt to find
and fix vulnerabilities in code before they were deployed.
Shifting left brought a utopian vision of application security - developers organically fixing
every vulnerability out of the overflow of their hearts. On the plus side, potential
vulnerabilities were identified earlier in development, and teams got new insights into what
actually made up their software. On the negative side, developers were bombarded with
confusing false positives, left spinning their wheels with pipelines blocked over nothing.
Nonetheless, the idea of getting findings directly to developers as they’re coding became
the driving force of application security.
Platform Timeline
2015 2019 2020 2021
SCA Container IaC SAST
The Market Transition to Platforms
As application security tools became more integrated with developer workflows, it was unrealistic
to have developers managing numerous scanners. Snyk was the first incumbent player to define
the modern application security platform as they expanded from in pipeline SCA scanning to
containers, IaC, and SAST. These scanners existed in other tools, but surfaced results in ways that
were detached from the developer experience. Snyk treated everything in a repository as code,
surfacing results directly to developers in near real-time, and into the workflows they were used to.
Snyk’s expansion into a platform was part of a broader shift in application security. Enterprise
incumbents like Checkmarx and Veracode began speeding up their scanning engines for in
pipeline scans, and building unified cloud hosted offerings. While these established players
were consolidating their capabilities, many startups emerged to disrupt the market.
These changes introduced a new wave of development and observability tools, from GitHub
Several application platform startups like Aikido and Arnica focused on orchestrating and
to DataDog. At the same time, solutions like WhiteSource (now Mend), Sonatype, and Snyk
consolidating different tools, often using a combination of open and closed source scanners.
emerged, addressing both the growing importance of open source vulnerabilities and the
Another set of startups like Apiiro, Cycode, and Legit started from the opposite direction -
need for faster scan times.
giving teams the ability to manage their different scanners and get visibility into their pipelines.
The end vision for most of these tools however was the same: creating an all in one application
These Software Composition Analysis (SCA) tools saw rapid adoption because existing
security platform.
platforms did not yet support SCA capabilities, and didn’t integrate natively with cloud
Application Security Market Report 2026 13

Types of Scanners Ways to Implement Outcomes for Teams
Each Scanner Type
Why Traditional ASPM Failed
The application security platform space has grown particularly confused around the term
Application Security Posture Management (ASPM) and the capabilities a platform should
deliver. Existing definitions from other analyst firms often fall short, typically describing ASPM
as little more than a tool for managing and orchestrating scan results.
However, most products that manage third party results also introduced their own scanners
over time. Because these scanners often used powerful open source foundations, it has
become rare for teams to run thorough detection bake-offs between scanners themselves,
such as trying to compare the capabilities of 8 different scanners directly within a one month
trial period. To add to the confusion, numerous platforms launched “ASPM” solutions that were
little more than dashboards for managing their own tools.
In our last report, we explained that pure play ASPM solutions are better relegated to the realm
of CTEM, as larger vendors went on acquisition sprees to create vulnerability management
platforms for every kind of vulnerability. The desire to create a code to cloud picture of a
vulnerability has made application security a clear requirement of larger vulnerability
management providers. Meanwhile, the advent of AI coding has completely transformed the
needs of application security platforms.
As early as last year, code to cloud correlation was the defining feature of application security
platforms, as the capability is essential for accurately prioritizing and assigning vulnerabilities
in modern systems. However, tools for securing AI assisted development have since become
the critical feature for application security buyers. The challenge for buyers and vendors alike is
that there’s no defined best practices for AI security development. While some vendors are
offering helpful tools, like defining security practices in rules files, we are a long way away from
understanding the right kinds of scanners and workflows that will be used at scale.
Application Security Market Report 2026 14

Moving Towards an AI Future
Securing AI generated code has created a totally new set of technical requirements - MCP
servers, rule file management, context management - all data that sits outside of the repository
itself. Combined with rapid developments in AI scanning capabilities, it’s no longer true that the
scanners are commoditized.
While application and cloud security will unify towards product security,
the rapid adoption of AI code generation tools has steamrolled this
simplified vision for the future.
There’s never been a more exciting time to be an application security practitioner, and a more
uncertain time to be a vendor. New use cases are emerging everyday, requiring rapid pivoting
of underlying capabilities, such as focusing on developer endpoints rather than pipeline based
code scanning. The most promising approaches bring organizational context directly into the
agent’s context window, enabling developers to avoid preventable mistakes, like building a
custom encryption engine or dealing with complicated library version choices.
The risk AI code generation presents for vendors also creates an opportunity. Just as Snyk’s
growth was due to rapidly accommodating new workflows, AI code generation is transforming
how code is built and deployed. A new paradigm for secure code generation is needed, and
someone’s going to win this next wave of the market. The challenge for emerging vendors is
that OpenAI and Anthropic have a good chance to capitalize on the opportunity themselves;
however, this is what people assumed would happen with cloud providers, who failed to
deploy security features fast enough to win adoption.
Our prediction is that the new AI driven SDLC will create another application security unicorn,
the company that will adapt most quickly to the new workflows of software development.
Application Security Market Report 2026 15

THE CURRENT STATE
OF APPLICATION
SECURITY

SAST
Feature Development
Large Monorepos Fast Incremental Scans Function Reachability
AI Development
AI Autofix AI False Positive Judgements AI Based Logic Detections
Despite the commoditization of core scanners, they still generate more noise than value. On the
one hand, Static Application Security Testing (SAST) is a check the box feature, but on the other,
scaling a SAST program requires a lot of customization and false positive management. As with
code generation, AI is fundamentally changing the benefits of SAST scanning, making results
more novel and actionable.
Before exploring the exciting developments of AI SAST, it’s important to understand that for
large enterprises, legacy scanners are still used due to their support of:
Large compiled binaries
Complex static languages with substantial technical debt
Large monorepos for core services
The shift to rapid in-pipeline scanning was essential for supporting flexible microservice driven
development, but is why some large enterprises still use multiple SAST scanners - some for their
modern services, and others for their older systems.
Over the last 5 years, the debate around SAST mostly centered on if a company was “just an
open source wrapper” or not. It’s becoming increasingly clear that buyers should prioritize the
quality of the output, rather than the details of the scan engine.
To understand how to evaluate competing SAST vendors, it’s important to know what SAST
actually consists of. In practice, SAST is a combination of two core functionalities:
An Abstract Syntax Tree (AST) - a way to query specific patterns in code.
Rules that use the AST to look for potential security vulnerabilities.
Application Security Market Report 2026 17

In other words, it’s not the engine that matters, but how it’s used, and how customizable it is.
Companies that take open source rules without enriching them will have noisy and inefficient
scanners, while those who properly customize will have the best.
The emergence of AI-driven SAST has offered practitioners a massive advancement in
scanning and prioritization capabilities. Early advances in AI SAST help rule out false positives
and discover logic and misconfiguration vulnerabilities, opening new possibilities for static
code analysis. These tools surface the kinds of issues traditionally found only through manual
reviews or pentests. At the same time, they introduce new challenges around de-duplicating
findings, scan performance, and incorporating organizational context.
Despite these new challenges, AI based static analysis is the 10x differentiator the static
analysis category has needed - the results are a generational improvement that cannot be
ignored. That being said, the user experience of SAST tools is also changing, as in-pipeline
scanning becomes more about AI code reviews than pure scanning.
Organizations should prioritize modernizing their in-pipeline code review process to rely more
on AI based analysis, while investing in the business logic capabilities of AI based scanners.
Post-AI startups, like Corgea and Zeropath, are the leaders in these capabilities, while many
incumbents are rolling out their own versions of AI scanning.
Application Security Market Report 2026 18

DAST and API Security
Feature Development
Web Crawler API Fuzzing AI Pentesting
The first wave of dynamic application testing solutions focused primarily on crawling an
application’s webpages, injecting various payloads, and reading responses to see if they were
successful. These early solutions offered a scalable way to test applications after they were
deployed, and were also adopted by pentesters and red teamers as part of their toolkit.
Application Security Market Report 2026 19

With microservice development, a new line of API first testing solutions emerged. These
solutions were split between “API Security” solutions, which functioned more as runtime based
API specific WAFs, and API testing solutions that excelled at fuzzing API endpoints directly
when provided API spec files. These solutions have continued to mature, generating specs
themselves, and improving their scanning performance. Solutions like Escape and Stackhawk
are especially strong at running meaningful testing of API endpoints, and focused providers in
this area are worth exploring for teams with modern API first architectures.
Like it has for SAST, AI is rapidly transforming the nature of pentesting, Dynamic Application
Security Testing (DAST), and bug bounty programs, offering autonomous crawling and
assessments of public facing endpoints. To give two examples of AI Pentesting, one is Wiz’s
dynamic payloads for testing public exposures. This is a lightweight solution that tries to test
for exploitability from outside the environment - much like a traditional DAST, but with more
flexibility. A second example is Aikido’s approach, where you provide the platform with
different user accounts in order to validate authorization issues in runtime, and watch as the
agents attempt different attacks.
AI DAST vs. AI Pentesting
AI Pentesting: gives agents a variety of tools to enumerate endpoints
AI DAST: runs application contextual payloads to look for business logic flaws
Both AI Pentesting and AI DAST offer similar results with different implementations
Both discover an organization’s public endpoints, moving towards Attack Surface
Management
Choosing an approach in this category ultimately depends on the outcomes an organization is
seeking. DAST generally delivers more consistent results with greater clarity, while AI-based
pentesting tends to uncover more unique vulnerabilities, often at the expense of consistency.
Over time, these categories will converge and the distinction made in our report is intended to
clarify differences in approach rather than to imply a hard boundary. This is why in our images
we highlight both the AI pentesting approach, and those who have built substantial AI
capabilities into their tooling.
Application Security Market Report 2026 20

Secrets
Feature Development
Validation
Secrets Detection Governance
& Pre-Commit Hooks
Of all the tools in an application security arsenal, secret scanning remains the most binary - it’s
either a top priority, or a very low one. On the one hand, detecting secrets has always been a
relatively commoditized offering, as strong open source options have existed, as well as the
more obvious regex use cases for implementation. Some tools like Snyk combined secret
detection with their SAST engine, never marketing it as a separate capability; others like
GitGuardian invested heavily in the capabilities, building a platform around them, alongside
building robust libraries of secret types.
In 2018, GitHub entered the secrets scanning market, and did so in a way that makes it
difficult for competitors to provide as simple a deployment. Once a secret is pushed to a
repository, dealing with it becomes a major pain. For scenarios where a team can’t
seamlessly rotate a secret, they need to take the risky action of removing the secret from the
repo, as well as the commit history, and force pushing their branch upstream - overwriting
the entire history of the repository.
This is why pre-commit hooks, wherein a secret can be detected and blocked before it’s sent to
the upstream repository, is the essential feature of a secret scanner. The challenge is in
deploying these endpoint capabilities across developer laptops. While many companies offer
pre-commit hooks, GitHub’s advantage is baking these capabilities directly into their own
hooks, allowing them to be deployed without additional efforts.
Dedicated platforms like GitGuardian and Trufflehog have innovated by expanding their
validation and detection capabilities outside of developer commits in source code. These
additional capabilities take their secret scanning offerings across other platforms like Slack or
Google Drive, and do more granular validation of the permissions of the leaked keys. These
developments are turning the platforms into more non-human identity security providers than
traditional scanners.
Application Security Market Report 2026 21

Software Supply Chain
Most vendors support some
amount of static function level
reachability, here are some
technical considerations:
Without a CLI, doing this with static
languages is incomplete
Doing this analysis means an
increased scan time, it’s used for
prioritization, not pipeline
Expect different results based on
language, CVE coverage and
provider
The proliferation of open source software combined with an executive order mandating
Software Bill of Materials (SBOMs) led to an explosion of supply chain security vendors. This has
caused software supply chain security to become one of the most crowded markets in all of
application security. Early on, differentiation largely came down to how tools performed scans,
and what languages they supported. Some vendors, like Snyk, focused on code-level analysis
through package files, while others relied on binary scanning, giving more depth insights but at
the cost of speed and ease of adoption.
The code scanning approach proved to be the better user experience, but numerous other
possibilities exist in supply chain security more broadly. First, the categories of malware
detection and package health detection have always lingered as niche use cases (despite their
risk being so large), with most startups focusing on these areas facing acquisitions over the last
ten years. Only this year, with attacks like Shai Hulud having a massive impact, malware
detection has become a mainstream necessity of Software Composition Analysis (SCA) tooling.
Application Security Market Report 2026 22

Reachability has proven to be an essential feature of SCA platforms, helping reduce massive
vulnerability backlogs by providing evidence of exploitability. In brief, reachability analysis
attempts to determine whether a vulnerability is actually exploitable within a given
environment. At a basic level, this is commonly done by checking whether the vulnerable code
is used by the application or whether it is accessible to attackers. You can read more in depth
about the types of reachability analysis in our series on reachability.
While several vendors offer strong reachability analysis capabilities, the feature
itself is difficult for organizations to evaluate because vendor databases and
methodologies are proprietary. Dedicated SCA providers tend to offer
stronger support but effectiveness depends heavily on the languages and
architectures they support.
The core problem of SCA has always been that updating open source software is hard. If
patching software was easy and automatic, vulnerability scanning wouldn’t need to exist at all.
Today, many vendors understand the core problem, and are building the solutions to help.
With the rise of AI, new approaches have entered the market, particularly breaking change
analysis and backporting patches. Breaking change analysis is one of the most promising
approaches to aiding the patching process - it utilizes function level reachability to lookup
function changes between versions, and suggests the required changes needed to patch.
Even as AI makes software changes easier, backporting patches will continue to have a role in
large enterprises, where patching certain systems brings unacceptable risk. The trade-off is
that it has the potential to create divergent supply chain problems, and may introduce
additional risk if the vendor patch wasn’t completed correctly
Ultimately, AI coding tools are also developing to assist with the patching process, helping
developers use the latest versions of software packages by looking up the versions before
using them. Similarly, they’re getting better at looking up the relevant changes to migrate
between versions. We’re finally moving towards a future where patching becomes easy enough
to actually help drive vulnerability backlogs down.
Application Security Market Report 2026 23

Cloud and Infrastructure
Feature Development
Container Scanning Application Mapping Runtime Reachability
When tools start scanning containers, they open Pandora's box of complexity. Once you scan a
container, you’re quickly involved in its entire lifecycle - scanning the Dockerfile, the build
process, the container registry, and the running container. Additionally, many teams don’t
realize they’re getting duplicative results from their container scanner and their SCA scanner,
adding another layer of confusion.
The responsibility of scanning containers has landed squarely on the cloud security side of the
fence; however, typically application security tools do a better job of delivering the results to
the teams that can actually do the fixing. This tension has led most large application security
providers to provide container scanning in some form or another as part of their platform.
Infrastructure as code has the same problem, landing as an infrastructure team responsibility,
but being more native to an application security integration workflow. This functionality is
generally the most underbaked, because while basic scanning is widely accessible in open
source tooling, making it work for your environment requires a high degree of customization.
Scaling IaC analysis quickly leads to high levels of complexity, as building drift detection and
support for custom modules become must-have capabilities. Other tools also include basic
CSPM scanning as part of their platform in order to function as an all in one platform for
smaller companies.
All in all, cloud security capabilities have long faced an awkward overlap with application
security. On one hand, for organizations that are heavily invested in infrastructure as code and
have strong deployment guardrails, an application-security-first approach works well. However,
many companies operate in far more cobbled-together cloud environments, consisting of a mix
of manually deployed and infrastructure-as-code-managed assets. These organizations tend to
value the runtime monitoring capabilities of cloud security providers more than treating
everything as code. Nonetheless, having these capabilities closely tied together creates many
benefits to prioritization, drift detection, and contextualizing findings.
Application Security Market Report 2026 24

Management Tools
In our cloud security report, we made it clear that vulnerability management solutions are
consolidating under CTEM functionalities. ASPM vendors, as traditional analyst firms described
them, were a transitional tool for consolidating the findings of different application scanners.
Consolidating findings across containers and SCA scanners was important, but the broader
de-duplication and contextual project has more to do with infrastructure than code.
The threat exposure management category (vulnerability management 2.0) remains top of mind
for security leaders entering 2026, but they don’t necessarily expect their application security
scanner to be that same tool. Developer experience and finding quality remain paramount, with
broader vulnerability management goals typically owned by different teams.
Even as the market shifts toward more unified exposure and vulnerability management tools,
there can be meaningful benefits having an orchestration layer on top of your application
security scanners. For organizations with tens of thousands of GitHub repositories, monitoring
pipeline coverage, understanding which applications map to which teams, and orchestrating
scanning tools are massive challenges.
Tools in this category take different approaches to solving these enterprise problems. Some, like
Apiiro, focus on a more application-centric model. Others, such as Phoenix Security, lean more
heavily into cloud and container-centric views. Legit Security emphasizes CI/CD coverage, while
Palo Alto Networks brings a cloud-centric perspective through its broader platform. Each of
these approaches deliver value for large organizations that need clear visibility into security
coverage across sprawling development environments.
Application Security Market Report 2026 25

It’s also worth discussing the impact runtime technologies are having on improving on the
Runtime Technologies
concept of WAF more broadly. There are several approaches out there, each with pros and cons,
but each valuable additions to a WAF centric approach. One approach pioneered by Impart
Security focuses on providing an eBPF-based WAF, which can be easier to manage and enables
more contextual rule creation than traditional WAFs. Another approach comes from Miggo,
which applies its function-level reachability capabilities to generate more precise WAF rules. The
company has published extensively on this approach in the context of the React-to-Shell
vulnerability. A third approach from those like Raven and Oligo utilize preventative security
capabilities inside applications themselves to stop novel attacks.
This report focuses specifically on function-level capabilities for prioritization at runtime. For a
broader discussion on the importance of CADR and how these capabilities fit into achieving
best-in-class cloud runtime detection, see our Cloud Security report.
The shift left and secure by design movements promised perfect software, but the reality was
large backlogs of vulnerabilities that get explained away rather than fixed. While prioritization
and code scanning techniques have improved, runtime remains the source of truth for assessing
exploitability and implementing protection. Runtime oriented solutions provide the best
possible prioritization and protection organizations can get.
For reachability analysis, ADR providers have built extensive libraries of vulnerable function
executions that they monitor for at runtime. If a vulnerable function is executing, teams can have
high confidence that an exploit is possible. While the functionality might not seem that different
at first glance, runtime function level reachability is a necessary improvement for modern
programs. When every finding is interesting, and developers can see exactly how the
vulnerability is working, it creates a level of trust and interoperability that older tools haven’t
been able to achieve. Based on the usage of tools such as Oligo, Raven, and Kodem, these
capabilities can meaningfully improve prioritization across both code and operating system
packages.
As much as prioritization is helpful, organizations will never hit zero vulnerabilities, or be
perfectly protected against zero days. React2Shell was a great example of this, as vendors and
attackers raced to play WAF wack-a-mole with each new exploit. This is the true purpose of ADR
- helping to protect against ongoing attacks in real time, without needing to sit by and pray that
you, or the open source community, get a patch out in time.
Application Security Market Report 2026 26

It’s also worth discussing the impact runtime technologies are having on improving on the
concept of WAF more broadly. There are several approaches out there, each with pros and cons,
but each valuable additions to a WAF centric approach. One approach pioneered by Impart
Security focuses on providing an eBPF-based WAF, which can be easier to manage and enables
more contextual rule creation than traditional WAFs. Another approach comes from Miggo,
which applies its function-level reachability capabilities to generate more precise WAF rules. The
company has published extensively on this approach in the context of the React-to-Shell
vulnerability. A third approach from those like Raven and Oligo utilize preventative security
capabilities inside applications themselves to stop novel attacks.
This report focuses specifically on function-level capabilities for prioritization at runtime. For a
broader discussion on the importance of CADR and how these capabilities fit into achieving
best-in-class cloud runtime detection, see our Cloud Security report.
The shift left and secure by design movements promised perfect software, but the reality was
large backlogs of vulnerabilities that get explained away rather than fixed. While prioritization
and code scanning techniques have improved, runtime remains the source of truth for assessing
exploitability and implementing protection. Runtime oriented solutions provide the best
possible prioritization and protection organizations can get.
For reachability analysis, ADR providers have built extensive libraries of vulnerable function
executions that they monitor for at runtime. If a vulnerable function is executing, teams can have
high confidence that an exploit is possible. While the functionality might not seem that different
at first glance, runtime function level reachability is a necessary improvement for modern
programs. When every finding is interesting, and developers can see exactly how the
vulnerability is working, it creates a level of trust and interoperability that older tools haven’t
been able to achieve. Based on the usage of tools such as Oligo, Raven, and Kodem, these
capabilities can meaningfully improve prioritization across both code and operating system
packages.
As much as prioritization is helpful, organizations will never hit zero vulnerabilities, or be
perfectly protected against zero days. React2Shell was a great example of this, as vendors and
attackers raced to play WAF wack-a-mole with each new exploit. This is the true purpose of ADR
- helping to protect against ongoing attacks in real time, without needing to sit by and pray that
you, or the open source community, get a patch out in time.
Application Security Market Report 2026 27

EMERGING
CATEGORIES

AI Code Guardrails
Numerous Application Security Providers Numerous AI Security Providers
It’s tempting for some to picture an AI utopia, where all generated code is perfectly crafted
and tested, but the fact of the matter is that (for now) AI generated code is definitively insecure.
Whether it’s the numerous research papers demonstrating it, or anecdotal evidence, AI can be
too aggressive at delivering what developers ask for, no matter the security concerns.
The foundation model companies, from OpenAI to Anthropic, have strong incentives to make
their code generation process as secure and effective as possible, but the reality just isn’t there
yet. Combined with the accelerated risk of using more open source AI plugins in the form of
MCP servers and IDE extensions, developer endpoints have become more exposed than ever.
Application Security Market Report 2026 29

In response to the rapid adoption of AI generated code, application security companies have
taken different approaches to securing the process. First, I’ve seen some strong initial results
from providers like Backslash and Corridor, building in security rules to add to the agent’s
context window. These providers allow security teams to monitor for malicious rules files, while
also deploying rules files enforcing best practices, or secure architecture considerations
specific to the repository. This approach is aimed at making AI generated code more secure by
default.
Another approach taken by some providers with a lot of cloud context, such as OX and Apiiro,
is to give coding agents access to broader application context via MCP. This goes beyond the
scanner invocation some teams are doing with MCP by instead giving agents helpful context
about the overall environment. This helps agents automatically understand coding practices
that are adopted across the organization, while sneaking in patches for older vulnerabilities
along the way.
Finally, insights into developer endpoints are more important than ever as CISOs seek to
enforce policies instituted by AI governance committees. This includes initiatives to control
what models are approved, alongside AI code assistance tools. These solutions give teams the
ability to control what MCPs and other tools are allowed in the organization. Snyk has recently
moved in this direction, alongside providers like Koi which we wrote about here.
A sign of how rapidly this space is developing is that when we completed an in-depth report of
AI autofixing last year, there were only a few startups in the space of creating AI generated
fixes. Since then, many companies now offer and focus on AI autofixing. However, this entire
approach has become antiquated by code assistants with MCP workflows generating much
better fixes than any company’s "proprietary fix engine.”
These guardrail approaches offer promising initial results, but the future remains unclear of the
best approach to securing AI generated code. With many vendors focusing on runtime testing
instead of the guardrail approaches, it’s too early to tell which comes out on top.
Application Security Market Report 2026 30

Second, backporting patches can help in large enterprise environments because major version
Secure Supply Chain upgrades have the potential to introduce more risk than they eliminate. These upgrades often
involve major architectural changes. To mitigate the risk associated with upgrading, some vendors
backport security patches to older versions of software. This approach can meaningfully reduce risk
with minimal operational disruption but scalability and long-term support will remain as challenges.
Third, secure package registries hosted by vendors offer mixed benefits. Although scanning
packages for security issues before approving new versions can be helpful, there are simpler
solutions, such as introducing a new version cooldown or version pinning. At the same time,
popular ecosystems like npm are gradually introducing stronger authentication mechanisms to
reduce the risk of maintainer account takeovers.
Secure Supply Chain tools are most effective in highly regulated environments with legacy systems
that are difficult to patch, or where compliance requirements place heavy emphasis on vulnerability
counts. Regardless of the approach used, it is always worth noting that regularly rebuilding and
redeploying your software remains the only reliable way to maintain a low-CVE environment.
An emerging category of Secure Supply Chain tools focuses on securing the supply chain at
the source by providing mechanisms to make open source libraries safer before they are
imported into your environment. There are three main approaches to creating a secure by
default open source consumption model:
Reducing the attack surface of container images by minimizing them.
Backporting patches for newly discovered vulnerabilities into older versions, allowing teams
to avoid the disruption of major upgrades.
Hosting a package registry where libraries are scanned before they’re imported to reduce
exposure to supply chain takeovers.
First, minimal container images are a strong defense-in-depth initiative for teams looking to
reduce their attack surface. However, they can be challenging for developers to adopt. Even in
relatively small applications, migrating to minimal images can introduce unexpected issues, as
many applications implicitly rely on packages that are no longer present.
Vendors have tried to address these challenges with minimal image adoption in several ways:
Custom image builders
Debian-based images
Minimizing existing images instead of requiring a full transition
If you’re considering moving to minimal images, first be sure to rebuild your images nightly.
Rebuilding images will apply more security benefits than any major migration to minimal images,
and even if teams move to minimal images, they’ll need to rebuild them regularly for patching.
Application Security Market Report 2026 31

Second, backporting patches can help in large enterprise environments because major version
upgrades have the potential to introduce more risk than they eliminate. These upgrades often
involve major architectural changes. To mitigate the risk associated with upgrading, some vendors
backport security patches to older versions of software. This approach can meaningfully reduce risk
with minimal operational disruption but scalability and long-term support will remain as challenges.
Third, secure package registries hosted by vendors offer mixed benefits. Although scanning
packages for security issues before approving new versions can be helpful, there are simpler
solutions, such as introducing a new version cooldown or version pinning. At the same time,
popular ecosystems like npm are gradually introducing stronger authentication mechanisms to
reduce the risk of maintainer account takeovers.
Secure Supply Chain tools are most effective in highly regulated environments with legacy systems
that are difficult to patch, or where compliance requirements place heavy emphasis on vulnerability
counts. Regardless of the approach used, it is always worth noting that regularly rebuilding and
redeploying your software remains the only reliable way to maintain a low-CVE environment.
Developer PAM
Governing developer access to infrastructure has long been overlooked: how their credentials
are rotated, how just-in-time privilege workflows are enforced, and how NHI’s are managed.
Many legacy Privileged Access Management (PAM) tools were designed around Windows-based
infrastructure, focusing on laptop access, remote desktop, and database connectivity. Modern
development environments, however, require access to Kubernetes clusters, cloud
environments, and more recently, AI agent tooling. This shift has expanded the attack surface of
developer accounts that are often poorly monitored and insufficiently controlled.
The tools highlighted above focus on providing developers with secure access to a wide range
of resources while delivering several additional benefits, from just-in-time access to real-time
visibility. In many organizations, platform teams have built distributed homegrown systems to
manage access, which leads to sprawling permission models that are difficult for security teams
to audit and understand. PAM tools excel at restoring control and consistent visibility without
disrupting developer workflows.
If you’re considering moving to minimal images, first be sure to rebuild your images nightly.
From a developer perspective, tools in the PAM category make access management far more
Rebuilding images will apply more security benefits than any major migration to minimal images,
streamlined than maintaining a collection of long-lived SSH keys or custom tooling.
and even if teams move to minimal images, they’ll need to rebuild them regularly for patching.
Application Security Market Report 2026 32

sophistication of these capabilities varies significantly, resulting in a major impact on backlog
Code Quality reduction and remediation outcomes. Based on our testing with more AI-native tools such as
Zeropath and Corgea, a substantial number of false positives were tuned out across both SCA
and SAST findings.
On the remediation side, the expansion of these capabilities into SCA is exciting. While prioritization
alone is already a challenge in SCA scanning, remediation has always been the true bottleneck in
the category. If everything is fully patched, prioritization efforts become far less critical.
Newer startups like Aisle, Backline, and Konvu have made meaningful progress generating end
to end patches for SCA vulnerabilities. These tools go well beyond the basic approach of opening
Code quality and code security often cause confusion, as they should address closely related
pull requests that simply bump dependency versions, instead completing major framework and
concerns. In theory, checking code for security issues is very similar to checking code for quality
library upgrades directly for users, while also analyzing existing findings for true positives.
issues. But these tools have historically been built for different personas, leading to different
noise-to-signal ratios across each category and disconnected workflows.
AI prioritization and remediation continues to be one of the fastest-moving segments in
application security. As frontier models improve at generating and fixing code on their own,
Unifying code quality and code security can consolidate tooling and integration needs. The primary
security tools are increasingly evolving into contextual layers that guide those models toward
benefits are the ability to manage a single scanner across development pipelines, and having a single
higher-quality, safer code changes.
source of truth for developers to track rules, findings, and remediation priorities. This consolidation
reduces operational overhead while making it clearer what needs to be fixed and when.
The most important capability of a code quality tool is the ability to measure code coverage,
specifically the percentage of code functions that have tests written for them. Like security posture,
code coverage tends to drift over time, with developers struggling to consistently meet quality
standards in the same way they can fall short on security requirements. This struggle highlights the
shared challenge both code quality and code security tools are intended to address.
Many tools in the code quality and code security categories are now blending AI-driven code
review rules across both quality and security, giving teams a unified AI pull request reviewer.
From the experience of using AI code quality reviews from both Aikido and Corgea, their ability
to catch common issues in AI-generated applications, including authentication flaws and
always-true conditional statements is impressive.
AI Prioritization and Remediation
Last year, we released a report that objectively tested different approaches to AI remediation for
static code analysis. Since then, autofix capabilities have become widespread across many code
security platforms. However, the capability itself has largely been replaced by frontier models
and tools like Claude Code, driven by the superiority of dedicated AI agents, rules, and
workflows that can deploy large-scale, contextual fixes across entire codebases.
Although many providers now offer both AI-driven prioritization and remediation, the
Application Security Market Report 2026 33

sophistication of these capabilities varies significantly, resulting in a major impact on backlog Another capability that’s particularly valuable is significant change tracking ability. This enables
reduction and remediation outcomes. Based on our testing with more AI-native tools such as teams to gain visibility into major architectural or code changes that often happen without
Zeropath and Corgea, a substantial number of false positives were tuned out across both SCA security being aware. Combining significant changes tracking with organizational context gives
and SAST findings. security teams real insight into the riskiest changes happening in their applications.
On the remediation side, the expansion of these capabilities into SCA is exciting. While prioritization
alone is already a challenge in SCA scanning, remediation has always been the true bottleneck in
the category. If everything is fully patched, prioritization efforts become far less critical.
Newer startups like Aisle, Backline, and Konvu have made meaningful progress generating end
to end patches for SCA vulnerabilities. These tools go well beyond the basic approach of opening
pull requests that simply bump dependency versions, instead completing major framework and
library upgrades directly for users, while also analyzing existing findings for true positives.
AI prioritization and remediation continues to be one of the fastest-moving segments in
application security. As frontier models improve at generating and fixing code on their own,
security tools are increasingly evolving into contextual layers that guide those models toward
higher-quality, safer code changes.
Threat Modeling and Design Review
Of all the emerging tools in application security, continuous threat modeling and design review
is the most exciting area, both for the immediate value they provide and for their long-term
impact on AI-driven code generation. These tools work typically by integrating with existing
knowledge bases and source code to build an overall threat model of an application. From
there, they continuously monitor changes to deliver ongoing design reviews and updated threat
Last year, we released a report that objectively tested different approaches to AI remediation for
models as new systems are deployed.
static code analysis. Since then, autofix capabilities have become widespread across many code
security platforms. However, the capability itself has largely been replaced by frontier models Having a clear architectural view gives these tools a strong advantage when providing context to
and tools like Claude Code, driven by the superiority of dedicated AI agents, rules, and AI agents, which often struggle to understand an organization’s broader application
workflows that can deploy large-scale, contextual fixes across entire codebases. architecture. These guardrails can then be applied directly to new code generation, allowing
teams to enforce organizational standards consistently across their codebase.
Although many providers now offer both AI-driven prioritization and remediation, the
Application Security Market Report 2026 34

Another capability that’s particularly valuable is significant change tracking ability. This enables
teams to gain visibility into major architectural or code changes that often happen without
security being aware. Combining significant changes tracking with organizational context gives
security teams real insight into the riskiest changes happening in their applications.
AI Application Protection
Guardrails & Gateways Model Discovery & AI-BOM
Prompts, Tools & MCP Discovery
Red Teaming
Static Runtime
It is still too early to tell whether a dedicated vendor will be required to do AI application
security, but dedicated startups are offering capabilities that go beyond larger platforms.
Several of the tools covered in this report offer baseline AI Application Protection capabilities
such as model discovery, basic AI red teaming, and other posture-oriented methods for
identifying how an organization is using AI.
As a team prioritizes runtime protection, conversation guardrails, and MCP gateways, the
likelihood of needing a dedicated AI security provider increases. This is where tools like Pillar
and Operant are clearly differentiated, as they provide both runtime protection and granular
visibility into AI-driven applications, alongside a more robust mapping of AI application
architectures.
Setting aside the hype, AI red teaming is largely another form of DAST, where inputs are injected
into a different type of system and outputs are evaluated, often by another LLM, for
Of all the emerging tools in application security, continuous threat modeling and design review inappropriate or unsafe behavior. Similarly, AI BOMs and model discovery often resemble
is the most exciting area, both for the immediate value they provide and for their long-term extensions of SCA scanning, as models are frequently packaged as Python or JavaScript
impact on AI-driven code generation. These tools work typically by integrating with existing libraries. That said, the maturity of these capabilities varies widely across providers.
knowledge bases and source code to build an overall threat model of an application. From
One area that is especially compelling about ADR and CADR-style providers is their ability to
there, they continuously monitor changes to deliver ongoing design reviews and updated threat
secure AI applications from inside the running application itself. While many tools rely on
models as new systems are deployed.
observing inputs and outputs to infer how a model reached a particular outcome, ADR operates
Having a clear architectural view gives these tools a strong advantage when providing context to within the application, allowing it to observe chains of thought and tool calls far more natively.
AI agents, which often struggle to understand an organization’s broader application
We will cover the AI Application Security market in more detail later this year, but more details
architecture. These guardrails can then be applied directly to new code generation, allowing
are available in the 2025 AI Security report.
teams to enforce organizational standards consistently across their codebase.
Application Security Market Report 2026 35

BUYER’S GUIDE
Picking the right tool varies and depends on individual tech
stacks and priorities. The Latio Buyer's Guides exist to provide
clear and actionable considerations when searching for the
best available tools.

SMB and Mid-market Buyer’s Guide
Application Security Market Report 2026 37

SMB and Mid-market
Infrastructure Vulnerability Scanning
Application Security SCA SAST Secrets
Runtime Solution EDR XDR MDR CADR SIEM
Mid-market organizations require certain core scanning capabilities from their application
security tooling due to how their environments are structured.
Typically, mid-market organizations have one tool in place for infrastructure, one for application
security, and one for runtime protection. Beyond these core tools, mid-market organizations
may consider additional capabilities like:
Having a separate MDM solution for device management
A compliance automation solution for achieving SOC 2
Depending on the type of business and infrastructure, they may prioritize only infrastructure
or only application scanning.
If you’re a company looking for a scalable application security tool, you probably care about:
Reducing developer work as much as possible
Not wasting time on false positives
Having a workflow that’s consolidated around cloud hosted products
Not using too many tools
Spending the least amount of money as possible
Companies in this position will want to consolidate as many features into one application
security tool as possible to save on management overhead.
Application Security Market Report 2026 38

The two key questions to answer in order to confidently guide your tool choice are:
Do you want a separate platform for cloud security? While most of our survey respondents
wanted separate tools, they’re not always needed right away, or at all, depending on your
specific architecture. There are benefits to consolidating these tools, but they’re often
separate disciplines.
Do you want DAST included? DAST is one of the easiest compliance checkbox tools in your
arsenal, so it’s suggested, but many organizations make this a later priority in favor of the
immediate value provided by static analysis.
Of these companies, it’s worth noting Aikido, JIT, Arnica, and Socket have free account
offerings and friendly pricing structures. Also worth noting are Semgrep’s open source tooling,
and GitHub’s value through included or open source offerings.
Once core application security scanners are acquired, teams often consider DAST. It’s
important to understand that vendor approaches to DAST vary because:
DAST is included in many infrastructure security tools at a very low cost
DAST’s value has been de-emphasized by “DAST is dead” - old school scanners
that lack API context
Valuable API testing is difficult to build and maintain
While traditional DAST scanning has lost its value, meaningful API testing is an important part
of a mature security program. We recommend that teams introduce a DAST that is API driven
to support modern architectures, as older DAST scanners will provide little to no additional
value in these environments.
There are two key trends that SMB and Mid-Market companies should be conscious of when
thinking about tech stack structuring. The first is the shift from traditional in-pipeline scanning
to in-pipeline code review, whether through AI code quality or code security tools. This
approach can satisfy a large number of compliance requirements, while also giving developers
a more unified experience that goes beyond traditional vulnerability management models
The second trend is pairing strong static scanning with an equally strong runtime offering,
which is where the CADR category becomes particularly relevant. By combining an all-in-one
application security testing platform with robust runtime protection, mid-market companies
can achieve an extremely strong security posture. An all-in-one application security scanner
with strong AI detection capabilities, combined with a meaningful application runtime solution
is our mid-market security stack of choice.
Application Security Market Report 2026 39

Enterprise Buyer’s Guide
Application Security Market Report 2026 40

Additional Enterprise Coverage Guide
Application Security Market Report 2026 41

The most effective reductions in false positives continue to come from combining runtime
Enterprise
function-level reachability with cloud context. We’ve written previously about the potential
unlocked by this combination, but it is difficult to fully appreciate without hands-on experience.
When using these tools, every vulnerability investigation becomes genuinely interesting,
Choosing a Platform
reshaping how teams think about risk after years of being overwhelmed by noise.
Application security in large enterprises looks significantly different due to the high number of
legacy applications, diverse coding languages, deployment models, and development teams
that have built and managed their own pipeline solutions over time. Organizations with these
distributed environments often also have strict compliance requirements and long-standing
vendor relationships, which require customizations of SBOMs and multiple scanning types as
binaries are built and deployed.
These enterprises differ fundamentally from cloud-native startups and SaaS companies, where
standardized developer platforms are core to the organization. They typically operate on more
unified cloud-native architectures, with deployment processes built from the ground up or fully
migrated using consistent, standardized approaches.
The first step of our buyer’s guide is intended to highlight this distinction between sprawling
developer environments and fully modernized ones. On one side, there are vendors that support
a wide range of testing methods and workflow requirements, designed for large enterprises and
their often complex compliance needs. On the other side are vendors that function well as
all-in-one application security solutions, either through deep customization, strong extensibility
into existing platforms, or broad coverage of the many use cases enterprises require.
Additionally, the vendors listed in the cloud native architecture section are not meant to be
exhaustive. Nearly every company shown in the mid-market diagram can fit into an enterprise
stack, with different trade-offs depending on organizational priorities.
Approaches to False Positive Reduction
Vulnerability prioritization and reduction is a massive challenge on its own for large enterprises.
For this reason, static function-level reachability and AI-driven prioritization are important
differentiators, but their maturity varies widely by vendor and language, and often depends on
proprietary vulnerability databases that are difficult to assess externally. In general, static
reachability requires longer CLI-based scans to produce strong results, particularly for statically
typed languages.
Vendors have also taken different approaches to AI prioritization. Some build deep, proprietary
indexes of customer codebases and run sophisticated prioritization logic, while others rely on far
more superficial techniques, such as prompting general-purpose LLMs with a finding and its
surrounding code.
Application Security Market Report 2026 42

The most effective reductions in false positives continue to come from combining runtime
function-level reachability with cloud context. We’ve written previously about the potential
At the same time, developing AI coding guardrails are also a major concern for enterprises, as
unlocked by this combination, but it is difficult to fully appreciate without hands-on experience.
they aggressively encourage developers to adopt AI-assisted coding. The vendors highlighted in
When using these tools, every vulnerability investigation becomes genuinely interesting,
this category have all taken meaningful steps toward providing management capabilities and
reshaping how teams think about risk after years of being overwhelmed by noise.
guardrails for AI coding agents. That said, it is still early for this category, as frontier AI solutions
are evolving so quickly that it can be difficult to determine what best-practice security
architectures should look like.
Best in Class Solutions
On top of those points, continuous threat modeling and design review remain significant
challenges for both security and compliance teams, making this a smart investment for
Once a broad approach to vulnerability discovery and prioritization is in place, several additional
organizations looking to reduce friction in these processes. While many teams attempt to build
options for expanding your security program are possible. The first is the traditional ASPM
these capabilities in-house, vendors typically have an easier time integrating with the third-party
category, which focuses primarily on vulnerability management. These tools work well for
tooling required to operate at scale.
organizations with large, distributed teams that need visibility into what is and is not covered
across their existing scanner ecosystem.
Finally, robust runtime protection in cloud environments continues to be a major gap for many
enterprises, as legacy EDR solutions provide little meaningful coverage in containerized
The second option is adopting a dedicated software supply chain security provider. These tools
environments. By extending protection into the application layer, newer providers have made
typically offer more advanced reachability and license management, at the cost of introducing
substantial progress in delivering effective runtime detection and protection for enterprise
an additional vendor. In many cases, however, they deliver enough additional value, such as
applications. When combined with strong false-positive reduction for vulnerabilities, CADR
runtime protection, SBOM management, or developer autofix capabilities, to justify their place
remains a clear choice for modern enterprise cloud workloads.
as standalone offerings.
The final option is investing in a dedicated dynamic scanning solution. While many application
security platforms offer some dynamic scanning capabilities, these offerings are maturing due to
acquisitions in the space. For teams that prioritize API-first scanning and modern web
architectures, a standalone dynamic scanner is often still worth the investment.
Investing in Emerging Capabilities
For some teams, investing in point solutions that address emerging capabilities, or selecting a
platform based on strong support for a specific capability, can be sound decisions, depending
Vulnerability prioritization and reduction is a massive challenge on its own for large enterprises.
on organizational focuses. For example, open source supply chain attacks disproportionately
For this reason, static function-level reachability and AI-driven prioritization are important
target crypto businesses, making upstream malware detection and secure package registries
differentiators, but their maturity varies widely by vendor and language, and often depends on
especially important selection criteria for teams operating in that space.
proprietary vulnerability databases that are difficult to assess externally. In general, static
reachability requires longer CLI-based scans to produce strong results, particularly for statically
Beyond supply chain risks, investments in application security scanning are introducing new
typed languages.
considerations for how enterprises evaluate tools. A key consideration is business logic
detections, one of the most impactful application security scanning developments available
Vendors have also taken different approaches to AI prioritization. Some build deep, proprietary
today. These tools unlock entirely new categories of findings, and typically provide strong false
indexes of customer codebases and run sophisticated prioritization logic, while others rely on far
positive reduction methodologies as well.
more superficial techniques, such as prompting general-purpose LLMs with a finding and its
surrounding code.
Application Security Market Report 2026 43

At the same time, developing AI coding guardrails are also a major concern for enterprises, as
they aggressively encourage developers to adopt AI-assisted coding. The vendors highlighted in
this category have all taken meaningful steps toward providing management capabilities and
guardrails for AI coding agents. That said, it is still early for this category, as frontier AI solutions
are evolving so quickly that it can be difficult to determine what best-practice security
architectures should look like.
On top of those points, continuous threat modeling and design review remain significant
challenges for both security and compliance teams, making this a smart investment for
organizations looking to reduce friction in these processes. While many teams attempt to build
these capabilities in-house, vendors typically have an easier time integrating with the third-party
tooling required to operate at scale.
Finally, robust runtime protection in cloud environments continues to be a major gap for many
enterprises, as legacy EDR solutions provide little meaningful coverage in containerized
environments. By extending protection into the application layer, newer providers have made
substantial progress in delivering effective runtime detection and protection for enterprise
applications. When combined with strong false-positive reduction for vulnerabilities, CADR
remains a clear choice for modern enterprise cloud workloads.
Concluding Thoughts
Application security is a discipline in crisis. Developer workflows are changing rapidly and the
reality is that we are in a period of transition. Traditional scanning methodologies still have a
place, but things are quickly evolving.
For some teams, investing in point solutions that address emerging capabilities, or selecting a
There are bold promises from nearly every vendor around securing AI-generated code, but in
platform based on strong support for a specific capability, can be sound decisions, depending
practice much of the heavy lifting is still being done by frontier models. In the meantime, there
on organizational focuses. For example, open source supply chain attacks disproportionately
are also exciting developments that are helping teams reduce backlogs and uncover more
target crypto businesses, making upstream malware detection and secure package registries
meaningful vulnerabilities.
especially important selection criteria for teams operating in that space.
For all the approaches to securing AI-generated code, the real security benefits are still
Beyond supply chain risks, investments in application security scanning are introducing new
emerging. Looking ahead to practitioner tool roadmaps for the coming year, robust runtime
considerations for how enterprises evaluate tools. A key consideration is business logic
protection remains a key priority, as the AI-driven SDLC is still taking shape. By this time next
detections, one of the most impactful application security scanning developments available
year, it should be much clearer what this new SDLC looks like, and which vendors are doing the
today. These tools unlock entirely new categories of findings, and typically provide strong false
best job securing it.
positive reduction methodologies as well.
Application Security Market Report 2026 44

Application Security Vendor Map
The below map indicates the vendors focused on specific categories of scanning, versus which
provide bundled options. This is designed to help organizations think through coverage, but it
doesn't indicate scanner maturity.
Application Security Market Report 2026 45

VENDOR
SPOTLIGHTS
All vendors were given the opportunity to
spotlight their product by having the Latio
team author a dedicated page explaining
why they were awarded in this report.

Wiz has quickly evolved beyond cloud security to become a leader in the application security market as
well. While its core code-to-cloud capabilities remain as strong as ever, the ability to ingest findings
from other tools has also made Wiz a centralized vulnerability management platform. At the same time,
they have rapidly built and expanded their in-house scanning capabilities to a level that now rivals
many dedicated application security providers.
Beyond the scanning capabilities themselves, Wiz continues to lead in contextualizing and prioritizing
findings across the SDLC. Whether issues are tied to infrastructure resources or source code
repositories, the Wiz graph provides an elegant way to visualize relationships and drive remediation
workflows. This ensures the most relevant issues are routed to the right place with context on what
needs to be fixed and why.
On the runtime side, Wiz has significantly matured its attack surface management capabilities to
include AI-driven penetration testing, along with API discovery and runtime function-level reachability.
Bringing all of this data together in a single platform positions Wiz as the most complete code-to-cloud
offering on the market, giving both security and engineering teams a single place to reduce risk and
prioritize.
The Benefits of Wiz
Centralized Visibility Developer Context End-To-End Coverage
Manage application and cloud Provide actionable context through Combine static, runtime, and attack
security findings across code, graph-based relationships that link surface insights for comprehensive
infrastructure, and third-party tools. vulnerabilities to real-world impact. code-to-cloud visibility.

GitHub Advanced Security has quickly become a strong competitor across traditional application security categories,
particularly secret scanning, SAST, and SCA. While many tools attempt to be “developer-friendly,” GitHub is the only
platform developers actually love, adopt, and use on their own! This organic expansion into security significantly
increases developer adoption, and empowers them to directly customize workflows without friction. The result: tools
are actually operationalized, preventing leaks and security incidents, and reducing risk across application portfolios
of all sizes.
On the scanning side, GitHub has implemented leading features such as incremental scans, code quality scanning
and out of the box push protection for secrets. GitHub has also invested in scalable remediation workflows —
combining security campaigns with GitHub Copilot to make the remediation process as seamless and automated as
possible. Copilot is one of the few AI coding tools broadly trusted for enterprise development, and its ability to
generate large volumes of remediation pull requests materially accelerates vulnerability fixes.
GitHub is also embedding security directly into the code generation process by scanning code as it is produced by AI
agents. This adds an additional layer of protection during AI adoption itself. Combined with GitHub’s close
integration with Microsoft Defender for Cloud to analyze and establish runtime risk, GitHub stands out as a strong
option for enterprises looking to scale AI-driven development without compromising security.
The Benefits of GitHub
Native Developer Deep Rule Customization AI-Driven Remediation
Experience
Enables teams to write, extend, and Uses Copilot agents and campaigns to
maintain custom security logic with accelerate fixes at enterprise scale.
Built directly into developer
CodeQL.
workflows developers already trust
and use daily.

Datadog’s Application Security offering covers the full set of scanning capabilities teams expect,
alongside leading runtime protection features. On the static analysis side, Datadog supports multiple
implementation models, ranging from IDE through to runtime scanning. After integrating source code
repositories, teams can track and manage SAST, SCA, Code Quality, Secrets, and IaC findings across
their environments, with flexibility in how scans are configured and maintained.
Datadog’s leading agentic capabilities deliver benefits for application security workflows by giving
teams accurate remediation guidance and prioritization. These features pair well with Datadog’s
broader Bits AI Agents offering, helping to prioritize and remediate security issues.
The value of their scanning capabilities is amplified by Datadog’s access to runtime telemetry. By
correlating static findings with runtime behavior and threat detection signals, teams gain deeper
visibility into how applications actually operate in production. Beyond scanning and detection,
Datadog has contributed to research focused on areas such as malicious IDE extensions and software
supply chain threats. From leading threat research to scanning capabilities, Datadog is a complete
application security platform.
The Benefits of Datadog
Work With Developers Runtime Context Detection Engineering
Let developers work with the tools Correlate security findings with Benefit from ongoing detection
they’re already the most real-world application behavior using research across cloud and application
comfortable with. native telemetry. attack surfaces.

Since their founding in 2022, Aikido has evolved from a simple bundled application security offering
into a platform with leading capabilities across several categories. From robust SAST customization, to
open-source malware research, to leading innovations in AI Pentesting, Aikido focuses on delivering
features that matter most, improving developer experience while also strengthening real-world
security outcomes.
From a scanning perspective, Aikido provides strong reachability analysis, flexible SAST customization,
and a highly robust autofix architecture. These capabilities are designed to reduce developer noise
through a large set of handcrafted and sensible mitigations for some of the most common vulnerability
classes. When combined with the Zen runtime module and cloud capabilities, Aikido is able to add
meaningful organizational and runtime context, helping teams significantly reduce false positives -
expanding even to proactive protection.
Aikido has also been at the forefront of several emerging capabilities: AI penetration testing, attack
surface management, code quality analysis, and AI code security. The platform is a strong offering for
companies of any size looking to improve their developer experience, false positive rates, and adoption
of the latest technologies.
The Benefits of Aikido
Scalable Pricing Contextual Prioritization AI-Driven Coverage
Aikido provides clear pricing and Improve prioritization with runtime Apply AI-based scanning for both
bundling options for companies of and organizational context, alongside security and code quality use cases.
every size. strong reachability capabilities

Palo Alto Networks Cortex Cloud is a strong fit for security teams looking for integrated scanning or to extract more
value from their existing tools while also adding robust ASPM, software supply chain and cloud security capabilities.
With Cortex Cloud, teams can build a clearer picture of how vulnerabilities enter their environment and where
exploitable paths could lead to real-world impact.
Cortex Cloud natively supports IaC, SCA and secret scanning, alongside the broader set of ASPM, software supply
chain and cloud security capabilities expected from a CNAPP platform. In addition, it can ingest results through
native integrations with a wide range of third-party scanners, allowing organizations to improve prioritization without
disrupting their existing development tools and processes.
As with other areas of Cortex Cloud, its primary strength lies in the Command Center experience bringing together
context from across the application lifecycle to make findings actionable. Teams can also assess security coverage
across their codebase and gain visibility into any gaps. The AI Guardrails automatically suggest policies tailored to
your environment to stop new risks before they reach production.
The flexibility and configurability of Palo Alto Networks application security capabilities make Cortex Cloud a
compelling option for AppSec teams seeking preventing vulnerabilities getting to production, better prioritization
and supply chain.
The Benefits of Palo Alto Networks Cortex Cloud:
Prevention-First Unified Visibility AI Prioritization and
Remediation
Enforce AI generated policies that Centralize findings from native and
target and block risks based on your third-party scanners to improve
Enables prioritization, coverage
overall infrastructure context. prioritization, analyze coverage gaps,
analysis, and remediation from a
and accelerate remediation from a
single interface.
single interface.

Semgrep is one of the most developer-oriented platforms on the market. They pioneered making security
scanning accessible with their open source engine, which remains highly distributed and relied on by
organizations of all sizes. Semgrep has expanded to offer the cloud-native integrations along with robust
SCA and secret detection capabilities that practitioners expect from a modern application security platform.
Semgrep has also architected AI-driven detection, prioritization and remediation in ways that work
consistently for enterprise environments. The engineering thoughtfulness behind these features
delivers a set of AI capabilities that teams can adopt with confidence - whether detecting business logic
flaws with AI SAST, or driving remediation with autofixes. Beyond AI, Semgrep’s secret detection
remains a standout feature, particularly due to its semantic analysis approach, which goes well beyond
traditional pattern searching methods.
Semgrep is especially well suited for developer-first organizations that encourage teams to actively
optimize and maintain the scanning engine they’re using. The maturity of the scanning engine, combined
with the flexibility of its rule customization, makes Semgrep an enterprise ready application testing
solution. At the same time, its distributed and open source roots also make it a strong fit for mid-market
organizations that often begin their journey with the open source offering before expanding further.
The Benefits of Semgrep
Developer Native Customize Everything Enterprise-Ready AI
Remediation
Deliver a truly developer-first security Reduce noise with semantic analysis
experience with fast, local, and and highly customizable rule sets.
Utilize AI-driven prioritization and
CI-friendly scanning.
remediation with confidence in large
environments.

Invicti has long been known for its robust DAST solutions, which have enabled organizations of all sizes to
perform in-depth testing of running applications. The platform has remained competitive in the dynamic
testing space by expanding AI capabilities from their Acunetix and Netsparker lineage and has more
recently expanded into a broader AppSec platform strategy with its acquisition of ASPM from Kondukto.
Today, Invicti provides a comprehensive set of dynamic testing features, alongside API and LLM
discovery, LLM integration testing, and developer-oriented API testing and scanning. Recent
enhancements include AI-assisted testing aimed at identifying business logic issues and improving scan
context. These additions to the platform expand coverage and reduce false positives, improving
everything from initial integration to scan quality.
With the integration of its orchestration capabilities, Invicti can now coordinate existing scanners,
deploy open-source scanners, or Invicti-supplied static AST tools across development environments.
This allows the platform to extend beyond standalone DAST into broader application security
workflows. As a result, Invicti is well suited for mid size enterprises looking for all-in-one AppSec
platforms, or for enterprises that prioritize a dedicated DAST solution and want flexibility in how they
manage and evolve their existing application security tooling.
The Benefits of Invicti
Discover Undocumented API and AI-Assisted Tool Orchestration
API and LLM Testing
Coordinate existing and open-source
scanners to support broader
Multi-layered approach to discovery, Test APIs and leverage AI-based
application security workflows.
including during scans, source code techniques to improve context and
analysis, gateway integrations, and identify complex issues.
network traffic analysis.

Corgea has built a strong AI-first approach to application security, using AI across vulnerability discovery,
prioritization, and remediation. While many vendors claim to use AI for better prioritization, Corgea has
delivered real differentiation in how effective these capabilities are across each of those areas.
As AI coding becomes more common, developer expectations for security tools are rising, both in
terms of the relevance of findings and how teams interact with them. Corgea’s AI-driven SAST engine
consistently surfaces findings that are practical and meaningful. I have seen firsthand the value of these
discoveries, particularly in identifying business logic flaws that lead to real-world attacks, rather than
the typical volume of low-value false positives produced by traditional tools.
On the workflow side, the Corgea team has invested heavily in modern, AI-first developer experiences.
Developers can interact directly with pull request comments through chat-based workflows that feel
natural and intuitive. This creates reviews that resemble thoughtful, informed security feedback rather
than rigid pipeline blocks that disrupt development.
Overall, Corgea is one of the more exciting companies in application security as AI reshapes what is
possible across detection, prioritization, and remediation.
The Benefits of Corgea:
AI-Driven Discovery Relevant Prioritization Developer-Native Reviews
Identifies meaningful vulnerabilities, Uses AI context to reduce noise and Delivers conversational, PR-based
including business logic flaws, that surface issues that pose real security feedback that aligns with modern
traditional scanners often miss. risk. developer workflows.

Snyk pioneered the modern DevSecOps experience by giving developers immediate access to security findings
across their code base. Most recently, Evo by Snyk brings many of the capabilities of dedicated AI security tools
into the context of Snyk’s broader ecosystem, creating a developer first approach to securing AI-Native
applications, while giving security engineers visibility into the new wave of AI tools.
Snyk’s newest capabilities give teams visibility into developer endpoints, including which MCPs and coding agents
are in use, and the ability to track and enforce standards across those endpoints. This visibility forms the foundation
for enforcing guardrails on AI generated code. Using Snyk’s MCP for agents, coding tools can retrieve additional
security context to generate higher-quality code by default and to produce more effective remediations.
The broader Snyk platform remains a flexible option for organizations managing a wide range of languages,
frameworks, and deployment models at enterprise scale. Across its product lines, Snyk has built a robust and
continually evolving knowledge base of vulnerabilities and findings that support consistent security outcomes
across diverse environments. These capabilities combined with AI capabilities help enterprises looking to safely
adopt AI tooling.
Overall, Snyk continues to be a strong choice for enterprises seeking a mature DevSecOps platform, while
actively preparing for widespread adoption of AI-assisted code generation.
The Benefits of Snyk
AI-Aware Guardrails Developer Endpoint Enterprise Platform
Visibility
Applies security standards directly to Supports broad language coverage
AI-driven code generation workflows. and scalable security management
Tracks agents, tools, and usage
across teams.
patterns to enforce consistent
security controls.

It is increasingly clear that AI coding will play a major role in the future of software development. While AI-generated
code introduces new risks, it also introduces new opportunities to secure code by default, in ways that shift-left always
promised but rarely delivered. Corridor is a leader in improving the quality of AI-generated code by giving security
teams visibility, governance, and guardrails before and after code is created.
Corridor begins by learning an organization’s codebase and environment to understand which security controls
should be applied alongside existing standards. It uses AI agents to generate security context and guardrails
automatically, drawing upon both pre-generated packs as well as building custom context based upon a customer’s
codebase and documentation. It then integrates directly into the most popular AI coding tools at both the planning
and code generation stages.
Corridor enables agents to make better decisions around libraries, frameworks, and coding patterns that align with
the organization’s security postures and scans code as it is created to prevent flaws at the source. Corridor also
provides a pull-request reviewer as a final check to make sure code is secure and compliant before it is merged.
When these capabilities are unified, the platform delivers an end-to-end improvement over traditional scanning
approaches. Organizational context is used both to secure code as it is generated and to provide developers with
more meaningful, actionable feedback.
The Benefits of Corridor
Secure-By-Default Contextual Code Reviews Deep AI Tooling Integration
Generation
Replaces noisy findings with AI-driven Native tool integration allows
reviews that understand code intent developers to scan code and fix vulns
Applies organizational security
and usage. from their coding agent.
standards directly within AI code
generation workflows.

While most vendors are just beginning to apply AI to enterprise-scale security problems, Konvu was
built from the ground up to address SCA backlogs for security teams. The platform delivers two key
outcomes: vulnerability prioritization and remediation, and is well positioned to solve both effectively.
Security teams have long struggled to make SCA backlogs shrink instead of grow. One common
approach is reachability analysis - there are multiple types of reachability, and most vendors support
only a subset of them. Another approach is AI-driven code analysis which introduces another powerful
layer of false-positive reduction. Konvu stands out by combining all aspects of reachability with
AI-based prioritization, resulting in some of the most robust false-positive reduction on the market.
Beyond prioritization, remediation is a critical part of the SCA challenge. Many security engineers have
experienced the false promise of automated pull requests that simply bump dependency versions
without addressing real migration complexity. Konvu goes significantly further by delivering complete,
end-to-end patches for major version upgrades, making complex dependency migrations far more
achievable for engineering teams.
The Benefits of Konvu
No Rip and Replace Agentic Triage Evidence Backed Decisions
Konvu plugs into your existing Konvu’s agents run exploitability Every outcome comes with clear
scanners and pushes decisions back analysis in the customer’s context, reasoning and supporting evidence
where teams already work, no new executing a CVE specific investigation so AppSec and developers can trust
dashboard needed. plan with reproducible checks. the results, and keep an audit trail.

Cycode is one of the most comprehensive application security platforms on the market, spanning
software supply chain security, application security testing, and posture management. Cycode can
function as an all-in-one application security solution, or as a unifying risk-based platform for
vulnerabilities across Cycode and third-party scanners, depending on an organization's needs.
Cycode’s core strength has long been its context intelligence graph - combining data across code,
infrastructure, and security findings. This graph allows teams to quickly correlate signals to prioritize
exploitable vulnerabilities based on risk and codify why, how, and by whom security decisions and
actions are made throughout the vulnerability lifecycle.
More recently, the team has focused on extending the context intelligence graph to orchestrate AI
agents. By providing agents with contextual intelligence, Cycode enables them to emulate security
decisions, such as contextual blocking and targeted remediation campaigns. This approach equips
security teams to scale alongside developer AI usage.
Whether an organization is looking to replace individual application security testing tools or orchestrate
and manage a diverse set of existing scanners, Cycode remains a leading option in the market.
The Benefits of Cycode:
Comprehensive Coverage Contextual Risk Graph AI-Enhanced Orchestration
Spans supply chain, testing, and Maps findings to ownership, Uses rich context to drive smarter
posture management within a single exploitability, and impact across the blocking, prioritization, and
platform. codebase. remediation campaigns.

Upwind Security was the first platform to meaningfully combine API security capabilities with those of a traditional
CNAPP. By leveraging deep runtime, application, and layer 7 data, Upwind delivers API discovery, dynamic testing of
APIs and AI/LLM risks, vulnerability prioritization, and can even serve as a replacement for standalone API security
tools. Upwind is unique in pairing these features with the standard suite of CNAPP capabilities, especially agentless
scanning, CSPM, and vulnerability management.
Upwind’s dynamic testing capabilities are especially strong and exceed what most traditional vulnerability solutions
offer today. By collecting network logs directly, the platform deploys contextual tests that reflect real application and
network flows, alongside comprehensive API fuzzing and API spec generation. This approach gives teams visibility
into how applications actually behave in production, rather than relying on static assumptions.
Among CNAPP providers, Upwind has invested the most heavily in runtime function-level reachability. This capability
enables more accurate prioritization, and significant false-positive reduction. These function-level insights also
extend into Upwind’s Cloud Application Detection & Response (CADR) capabilities, creating a cross-layer runtime
protection platform that combines cloud, application, and network security into single detection events.
Overall, Upwind remains a deeply runtime-focused CNAPP, built from the ground up to deliver traditional CSPM
capabilities alongside advanced runtime security technologies. These capabilities make it a great selection for teams
looking to get the most value out of their cloud security solution.
The Benefits of Upwind:
Better Detections, Faster Improved Dynamic Testing Function-Level
Response Prioritization
Use real network and application data
Combine cloud, workload, and API to drive more accurate API testing Reduce alert volume by prioritizing
data to fully detect threats from start that’s contextual to your environment. only the vulnerabilities that matter
to finish, and give teams the context most, focusing on what’s executing in
they need to respond. your environment.

Legit Security is frequently a reference point for enterprises looking for an application security posture management
tool. They were the first to make me aware of the ASPM category, and when I saw the product, the solution
immediately made sense for those dealing with the “too many scanners” problem. Development teams at large
enterprises frequently manage their own pipelines and tools, leading to sprawling and uncertain scanning coverage.
Legit steps in to provide teams with a strong mapping of their deployment pipelines, cloud-based or on-premise, and
assigns risk and coverage scores as code moves through to deployment.
Within the last few years, Legit has expanded well beyond providing a pure management layer. The platform now
includes scanning capabilities like SAST and SCA, API reachability, and significant change tracking. For management
and consolidation use cases, these additions have meaningfully increased the overall value of the solution.
With the recent launch of VibeGuard, Legit Security is on the front lines of addressing challenges with AI code
generation. VibeGuard covers critical capabilities, starting with securing AI code generation tools - IDE’s, MCPs, and rules
- preventing attacks like prompt injection and unapproved secret access. It then helps to secure code as it’s generated by
fetching organizational and security context, allowing teams to enforce security standards on AI generated code.
Together, these capabilities form a holistic, modern platform that is particularly well suited for enterprise environments.
The Benefits of Legit Security
Gain Visibility Across Enforce Governance for Track Changes Across
Deployment Pipelines AI-Generated Code Enterprise Environments
Track and monitor workflows to Embed AI Governance into Teams can assess overall coverage and
maintain oversight across dispersed development flows, securing end to security posture across their tooling,
development teams, gaining a end developer usage from code while using Legit to close gaps across
complete coverage map of your SDLC. generation to ensure secure MCP traditional scanners and emerging
usage. AI-driven coding workflows.

Clover Security is a leader in the emerging category of AI threat modeling and design review, which has the potential to
reshape the entire application security industry. Clover’s ability to generate ongoing security design reviews unlocks
two key capabilities. First, it significantly accelerates and improves the quality of threat modeling across an organization.
Second, it enables the enforcement of security controls from AI code generation, to pull requests, to deployment.
First, Clover integrates with existing knowledge bases and developer productivity platforms to build baseline
contextual awareness of an organization’s environment. This allows the platform to prioritize incoming projects while
gathering the information needed to support effective threat modeling and design review. Clover then uses this
context to help security teams accelerate the often overwhelming and time-intensive processes of conducting design
reviews for new systems.
Second, Clover acts as a continuous enforcement layer for the decisions made during design review. By supplying
developers and AI agents with organizational security context, it enables secure-by-default code generation and
ensures that security intent is carried through to implementation. Clover brings your organizational security policies,
such as architecture and authentication requirements, into every prompt or pull request, enabling catching issues like
business logic flaws as early as possible.
By combining these capabilities together, Clover provides a new kind of end to end application security platform -
one that helps you design an effective security program, and implement it across the SDLC.
The Benefits of Clover Security
Continuous Threat Context-Aware Design and Secure-By-Default
Modeling Code Reviews Enforcement
Improves coverage and consistency Uses organizational knowledge to Carries security intent from AI coding
by making threat modeling an deliver more accurate and relevant through deployment without manual
ongoing process. security guidance. intervention.

Enterprise vulnerability management programs fail because scanners rarely answer the three questions
that drive remediation: who owns it, where is it running, and what is the fastest, lowest-impact fix. For
organizations that prioritize actionable attribution and operate in regulated industries, many platforms
overlook the customization details required to operationalize remediation. Phoenix Security has
consistently stood out for its attention to enterprise-level details that make vulnerability management
work at scale.
One of Phoenix’s primary differentiators is its ability to align asset attribution, code-to-cloud correlation,
and reachability analysis with business goals, regardless of which scanning tools feed into the platform.
This allows teams to maximize the value of their existing scanners rather than being forced to adopt
entirely new ones. These benefits extend to providing AI prioritization and remediation.
Phoenix’s attribution model is designed for distributed enterprises where ownership changes, services
are ephemeral, and data resides across multiple systems. Phoenix supports PYRUS CMDB-as-code
patterns and integrates with enterprise sources of truth to ensure accurate ownership. Phoenix also uses
AI across the platform, from vulnerability enrichment to remediation. These features make Phoenix a
strong option for enterprises seeking a scalable, configurable vulnerability management solution.
The Benefits of Phoenix Security:
Attribution at Enterprise Tool-Agnostic Reachability AI Prioritization and
Scale Remediation
Reduce false positives by applying
native provenance, lineage, and
Phoenix’s attribution CMDB enables Phoenix’s AI systems analyze threat
reachability analysis on top of
teams to manage asset ownership intelligence data to predict the threat
existing scanners, drastically
across their entire lifecycle types most likely to lead to
reducing vulnerability counts.
programmatically. exploitation, and provide precise
remediation guidance.

Contrast Security has long delivered some of the most robust application security protections available. The company
pioneered a runtime-oriented approach to application security through Interactive Application Security Testing
(IAST) and has since expanded into Application Detection and Response (ADR), bringing the power of its runtime
engine directly to security operations teams.
As application attacks continue to increase year over year, public-facing applications have become a primary attack
surface. Security operations teams have struggled to act on application-level alerts due to limited visibility and a lack
of understanding of how applications actually behave. Contrast addresses this challenge by providing deep,
runtime-level insight into application behavior.
Beyond visibility, Contrast delivers detection, testing, and response capabilities directly at runtime. Through deep
application instrumentation, the platform observes payloads, attack paths, and execution behavior in production,
correlating this telemetry in the Contrast Graph to give security teams the context they need to respond to attacks
with confidence.
Contrast provides testing and remediation by determining which vulnerabilities are truly reachable and
uncovering novel exploits in live applications, rather than relying solely on historical CVE data. For teams
prioritizing a runtime-first approach across application security and SecOps, Contrast is a compelling option.
The Benefits of Contrast Security
Runtime Application High-Fidelity Detection Reachability-Driven SCA
Visibility and Protection
Identifies exploitable vulnerabilities
across custom code and open-source
Provides deep insight into how Surfaces precise payloads and attack
dependencies based on runtime
applications behave in real paths to support confident
reachability.
production environments. investigation and response.

Raven has built a leading Application Detection Response (ADR) solution for companies to protect critical
applications. Raven unlocks the missing piece of workload protection for software teams by preventing malicious
deviations, whether a CVE exists or not. In an age where attackers are leveraging AI to automate exploitation, having
a prevention solution for CVE-less threats is more valuable than ever. Using deep application inspection at runtime,
Raven is able to tie functions that execute back to the original code that produced them, and prevent libraries from
executing attacker manipulated paths.
With ADR, developers get the insights they need to separate action from noise by contextualizing alerts to an
application’s environment, and security is able to prevent attacks, known and unknown, so patching isn’t done under
fire. Under the barrage of open source and AI assisted exploits, teams need better ways to protect themselves
besides waiting for a patch to be released.
Raven helps with incident response and vulnerability management by offering teams the critical application layer
insights they’ve been missing. They do this with low overhead, offering out of the box performance dashboarding
with common developer tools. Beyond insights alone, Raven even offers an elegant proactive protection solution by
permissioning libraries into known categories of system calls, enabling true zero day protection.
For enterprises looking to bring their applications into their security program, and mitigate advanced attacks, Raven
is a great solution.
The Benefits of Raven
Prevent Attacks Eliminate Vulnerabilities Simple Deployment
As application layer attacks continue to Respond only to known vulnerable Deploy an extremely efficient sensor
increase, prevent the latest attacks function executions, prioritizing what in minutes to immediately reduce your
while giving your team time to patch, matters. vulnerability counts by 99% and stop
while keeping your application running. malicious code before it executes.

Checkmarx has done an impressive job delivering the power of a modern, cloud-driven, AI-focused DevSecOps
platform without sacrificing the depth or precision of its historically robust scanning engines. For organizations
looking to modernize application security at scale, the Checkmarx One platform offers strong coverage across
scanning categories without compromising core capabilities.
Checkmarx has been steadily raising the bar on platform depth and precision by including features such as container
image layer analysis, detailed customization of SAST findings, custom query development, and an IDE experience for
agentic development lifecycles. These capabilities have been rolled out across a broad set of languages at enterprise
scale, giving customers access to modern application security workflows without losing depth.
One of Checkmarx’s long-standing strengths has been the level of customization it provides for enterprise application
security teams. Its highly configurable scanning engines allow teams to enforce organization-specific requirements
across large and complex codebases, aligning security controls with existing standards and threat models.
Checkmarx also delivers a strong management layer for application security teams, enabling centralized rule and risk
management across diverse applications. This approach allows organizations to enforce consistent security standards
while still accounting for the unique needs of individual applications.
The Benefits of Checkmarx:
Enterprise-Grade Modern DevSecOps Centralized Risk
Customization Platform Management
Enforces organization-specific Delivers cloud-native AI-assisted Manages rules and risk consistently
security standards across large and workflows without sacrificing across applications and teams.
complex codebases. scanning depth or precision.

GitGuardian has matured into far more than a secret scanning tool. The detection engine is built and optimized
for scanning at internet scale. It leverages a deterministic rules engine to identify secrets, paired with AI to filter
false positives and increase context. This distinction matters because understanding whether a secret has been
leaked publicly or exposed elsewhere is what determines risk and allows teams to prioritize.
By expanding detection beyond source code, GitGuardian delivers additional value through identifying secrets across
other platforms such as Slack and workforce tooling. This broader visibility enables teams to take a more comprehensive
data loss prevention (DLP) approach to secrets management, instead of narrowly focusing on code repositories.
Risk assessment in GitGuardian tests the validity of credentials while simultaneously connecting with IdPs and
applications to enumerate identities and their permissions. By cross-referencing these with identified secrets, the
platform provides a precise understanding of the potential blast radius. It also identifies which workloads actively
consume them, minimizing the risk of breaking production applications.
These capabilities make GitGuardian a more holistic non-human identity security solution, providing both proactive
and reactive identity security controls across the organization.
The Benefits of GitGuardian
Broader Secrets Detection Remediation Context Non-Human Identity
Coverage
Identify exposed secrets across code Assess potential impact by
repositories, collaboration tools, and understanding permissions, active Support proactive and reactive controls
public sources, taking advantage of a usage and exposure, allowing teams for secrets and machine identities across
highly tuned hybrid detection engine. to remediate based on severity. the organization, including detection
and response with HoneyTokens.

Category Innovators
AI Code
Supply Chain
Runtime
AI Platform AI Pentesting
Secrets Security DAST
API Security Developer Experience

Definitions
Platform Leader
Leaders in this category are built to be the only application security platform teams need. This
means including all core application security scanning capabilities alongside cloud and runtime
context features for prioritization and team context. Leaders in this category have made large
investments in the latest scanning features, without sacrificing the overall platform.
Testing Leader
This category represents the companies who meet the diverse requirements of enterprise use
cases - meaning support for the wide variety of languages, scan types, and reporting that these
companies need. They also have robust hosting, customization, and tertiary support services.
Management Leader
Leaders in this category are built for integrating with numerous scanners to drive workflows
with rich application context, creating an orchestration platform for remediating vulnerabilities.
While they often provide their own scanning tools as well, the strengths of these platforms are
in their ability to consolidate data across massive environments, creating unified remediation
workflows.
AI Code Innovator
This award is for companies investing in new technology for securing AI generated code by
both securing employee workstations against MCP supply chain and rule injection attacks, and
giving AI coding agents the context they need to deploy secure code. These emerging tools
are designed to work with AI coding development tools to create secure code by default.

Supply Chain Innovator
Companies in this category have innovated in specific ways for teams with supply chain
security concerns. Vendors in this category are highlighted for their investments in legal
analysis, malware detection, package health, prioritization, or autopatching capabilities.
Runtime Innovator
Innovators in this category excel at protecting applications against runtime threats. This
category is about representing tools that don’t merely detect ongoing application attacks, but
also offer various threat mitigation capabilities, allowing enterprises to respond in seconds to
the latest application attacks.
Category Innovator
These awards acknowledge companies who are especially innovating within either a specific
category, emerging capability, or set of features.

Ever wonder: Am I using the right security tools for my business, or am I
building the right product for the market?
Everyday companies are making decisions based on the information that is
available to them, which is often incomplete and based on vibes rather than
usage.
That’s where Latio comes in.
Founded in 2023 by James Berthoty, Latio was built to solve a critical problem
James was facing: there was no reliable, credible way to evaluate a vendor's
capabilities until after an agreement was signed. Latio exists to make the
buying and building processes better by getting accurate information to the
most relevant teams.(cid:31)
We focus on the product, the practitioner, and the market rather than slides
and hype cycles. We believe the greatest predictor of a great security tool and
program is finding the right product fit for both vendors and buyers.
We are creating a future where every decision is based on tests, market
insights, experience, and hard work, where it’s easy to find the right product
you’re looking for.
Our mission is to help every team find the right security product. So we test
every product, to make it easier for you to pick the right one.
A special thank you to everyone who has supported this mission, without you,
none of this would be possible.
Learn more:
(cid:31) latio.com (cid:30) Schedule a product briefing
(cid:30) Schedule a security program sync (cid:31) Follow us

The only analyst firm that tests products,
so you can find the right one.
Latio Tech, Inc. All Rights Reserved.

<!-- CONVERSION_METADATA: {"source": "https://github.com/jacobdjwilson/awesome-annual-security-reports", "date": "2026-08-27", "model": "gemini-3.5-flash-lite"} -->
