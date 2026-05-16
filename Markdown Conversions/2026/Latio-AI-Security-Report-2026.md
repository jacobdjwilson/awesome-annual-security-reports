# AI-Security-Report

## Table of Contents
- [Executive Summary](#executive-summary)
- [2026 Application Security Survey Results](#2026-application-security-survey-results)
- [Application Security Timeline](#application-security-timeline)
- [The Current State of Application Security](#the-current-state-of-application-security)
- [Emerging Categories](#emerging-categories)
- [Buyer’s Guides](#buyer’s-guides)
- [Conclusion](#conclusion)
- [Vendor Spotlights](#vendor-spotlights)

---

## Executive Summary

Whether you call it application security, product security, or DevSecOps, securing software is complicated. Today, practitioners are expected to manage a growing set of scanners, reduce large vulnerability backlogs, coordinate remediation across teams, and participate in architecture and threat modeling, often with limited headcount and little tolerance for noise.

AI is adding to this complexity, amplifying both the risks and opportunities in application security. AI assisted coding is reshaping how applications are built, deployed, and maintained. In parallel, the capabilities of platforms themselves are evolving with AI: features from autofix workflows, to false positive analysis, to scanning itself, are all radically changing product expectations.

This report is designed to help practitioners and buyers navigate the current application security landscape. It covers the transitions in application security over time, from waterfall development to DevOps to emerging AI code generation workflows. The report then breaks down every subcategory of scanner, the development of modern features, as well as how AI capabilities are changing functionalities we use today. We conclude with actionable buyer guidance that spans across SMB, mid-market, and enterprise environments.

### Key Takeaways

- **Application security has largely consolidated into platform players.** The capability differences have more to do with user, integration and developer experiences than pure scanning functionalities.
- **AI-native static analysis and business logic detection** are the most immediately meaningful changes in Application Security detection capabilities. These new scanners are capable of detecting entirely new categories of vulnerabilities which have traditionally been reserved for manual review.
- **Application security evaluations should focus on usability and backlog reduction** more than specific scanner functionalities. Tool evaluations should be guided by the time to fix an issue, rather than the number of issues detected.
- **ASPM as “management without scanning” has largely collapsed** into broader vulnerability management and exposure programs. ASPM is shifting into continuous threat exposure management, or universal vulnerability management.
- **Securing AI-generated code is still an open market** with unclear best practices. General approaches involve giving organizational context to agents, and having secure code reviews in pipelines, but this field is rapidly changing.
- **Supply chain security is expanding** towards malware, package health, and secure-by-default consumption patterns. CVE detection alone is not enough for modern supply chain security.

---

## 2026 Application Security Survey Results

The application security survey spanned organizations from tens of developers to thousands. In many ways, they reflected the reality of application security being a discipline in crisis - as teams were split in their priorities, what they wanted out of a tool, and where they saw the industry going.

The key results were:
- Developer experience is the most important deciding factor for new tools, followed by false positive rates
- AI pentesting is the most desired emerging capability
- The top concern for 2026 is speed and security of AI generated code

### Enterprise Doesn’t Always Use More Tools

![Chart showing median number of tools vs number of developers]

Contrary to popular belief, the survey data indicated that smaller teams can actually use more tools than enterprises, largely because they lean more heavily into open source offerings that they orchestrate themselves. Enterprises, by contrast, tend to manage fewer tools overall, but at a much larger scale. They are also more likely to rely on a smaller set of paid tools for specific purposes, such as supply chain security, SAST, and DAST.

This data helps explain why ASPM, as a standalone management category, struggled to survive. Enterprises with distributed scanning tools and capabilities never intended to centralize everything under a single ASPM layer, and third-party integrations often served as a stopgap rather than a durable, long-term strategy for tool orchestration. As we argued in our Cloud report, ASPM is now evolving into the broader CTEM category, which approaches vulnerability management in a more holistic way.

### Developer Experience Matters

Ranked choice voting was completed for several key application security features. The top 6 application security features:

1. Developer Experience
2. Least False Positives
3. Integrations
4. Most True Positives
5. Remediation Guidance
6. Reporting

The survey results are clear: practitioners are looking for tools that create the least friction with their development teams. Poor developer experiences and high false positive rates are what create friction with other teams, and are the top priorities teams have when assessing tools. This is where user experience matters more than individual scanner finding quality.

### Core Application Security is SCA + SAST + Secrets

![Chart showing percentage of practitioners expecting specific tool bundles]

As much as security platforms, finance teams, and analysts alike see the value of bundled application security offerings, the majority of practitioners still view only SCA, SAST, and Secrets as part of a core application security offering. The other half of practitioners sometimes included IaC scanning, DAST, and containers, or preferred to have no bundling at all.

### The SOC is Handling Runtime and WAF

![Chart showing team ownership of runtime application security incidents]

Increasingly, security operations teams are being tasked with handling runtime application security alerts, though ownership remains mixed. Cloud and product security teams are also responsible for these alerts in many organizations, and in some cases developers are involved as well. It is worth highlighting that these management functions no longer sit with traditional network security teams, and have instead shifted toward broader security operations and cloud teams.

### The AI Features That Matter

Application security practitioners are ready to adopt the latest AI features - from prioritization to static code analysis. The relatively low number of “none” responses is surprising, because it suggests that practitioners in this area are less skeptical about AI’s ability to transform day to day workflows than in other categories. Seeing the power of AI code generation directly makes practitioners in this category more open to AI adoption.

### The Gap is Runtime Context

AI may be driving industry excitement, but usability remains the primary focus for immediate feature enhancements. Specifically, better APIs, IDE state tracking, and integration experiences were highly requested from practitioners. The most requested feature by far was better cloud and runtime context, because teams want to better prioritize and determine the truth of a particular finding.

### Open Source or Not - Results Matter More

In 2026, practitioners care about end results more than a vendor's underlying scanning engine. Historically, application security practitioners were split about the value of open source scanning engines. In the time since, practitioners have come to better appreciate open source software, as well as understand that the underlying scanning engine doesn’t matter as much as the rules that are being applied to it.

### Application Security Priorities

Three concerns stood out most for 2026 priorities: Securing AI generated code, supply chain malware, and getting budget. With a combined 84% of responses, AI generated code and supply chain malware remain top of mind for security teams going into next year.

---

## Application Security Timeline

Application security can be divided into four eras: waterfall, agile, platform, and AI. Each era was introduced to address distinct concerns, many of which persist today, even as application security has rapidly matured over the past decade.

### Early Application Security (2000-2015)
Before 2010, application security was a very different practice in terms of scope, market size, and day to day operations. One primary challenge was developing scaling scanning solutions, primarily for static languages like C and Java. Early solutions were built to support waterfall development workflows, where annual software updates were compiled, uploaded to a platform, and a multi-hour (or multi-day) scan would be kicked off.

### The Shift to Agile (2015-2019)
The 2010s saw a massive change in how software was delivered:
- Dynamic languages like Javascript and Python massively increased in adoption
- The adoption of cloud hosted Git and CI/CD pipelines, alongside DevOps practices
- The shift to agile development practices
- Massive adoption of open source packages in software development
- Shift to microservice driven development, APIs and containerization

These changes introduced a new wave of development and observability tools. Solutions like WhiteSource (now Mend), Sonatype, and Snyk emerged, addressing both the growing importance of open source vulnerabilities and the need for faster scan times.

### The Market Transition to Platforms (2019-2023)
As application security tools became more integrated with developer workflows, it was unrealistic to have developers managing numerous scanners. Snyk was the first incumbent player to define the modern application security platform as they expanded from in pipeline SCA scanning to containers, IaC, and SAST.

### Moving Towards an AI Future (2023-Future)
Securing AI generated code has created a totally new set of technical requirements - MCP servers, rule file management, context management - all data that sits outside of the repository itself. Combined with rapid developments in AI scanning capabilities, it’s no longer true that the scanners are commoditized.

---

## The Current State of Application Security

### SAST
Despite the commoditization of core scanners, they still generate more noise than value. In practice, SAST is a combination of two core functionalities:
1. An Abstract Syntax Tree (AST) - a way to query specific patterns in code.
2. Rules that use the AST to look for potential security vulnerabilities.

The emergence of AI-driven SAST has offered practitioners a massive advancement in scanning and prioritization capabilities. Early advances in AI SAST help rule out false positives and discover logic and misconfiguration vulnerabilities, opening new possibilities for static code analysis.

### DAST and API Security
The first wave of dynamic application testing solutions focused primarily on crawling an application’s webpages, injecting various payloads, and reading responses. With microservice development, a new line of API first testing solutions emerged. Like it has for SAST, AI is rapidly transforming the nature of pentesting, DAST, and bug bounty programs, offering autonomous crawling and assessments of public facing endpoints.

### Secrets
Of all the tools in an application security arsenal, secret scanning remains the most binary - it’s either a top priority, or a very low one. This is why pre-commit hooks, wherein a secret can be detected and blocked before it’s sent to the upstream repository, is the essential feature of a secret scanner.

### Software Supply Chain
The proliferation of open source software combined with an executive order mandating Software Bill of Materials (SBOMs) led to an explosion of supply chain security vendors. Reachability has proven to be an essential feature of SCA platforms, helping reduce massive vulnerability backlogs by providing evidence of exploitability.

### Cloud and Infrastructure
When tools start scanning containers, they open Pandora's box of complexity. The responsibility of scanning containers has landed squarely on the cloud security side of the fence; however, typically application security tools do a better job of delivering the results to the teams that can actually do the fixing.

### Management Tools
ASPM vendors, as traditional analyst firms described them, were a transitional tool for consolidating the findings of different application scanners. The threat exposure management category (vulnerability management 2.0) remains top of mind for security leaders entering 2026.

### Runtime Technologies
The shift left and secure by design movements promised perfect software, but the reality was large backlogs of vulnerabilities that get explained away rather than fixed. Runtime oriented solutions provide the best possible prioritization and protection organizations can get.

---

## Emerging Categories

### AI Code Guardrails
It’s tempting for some to picture an AI utopia, where all generated code is perfectly crafted and tested, but the fact of the matter is that (for now) AI generated code is definitively insecure. In response, application security companies have taken different approaches to securing the process, such as building in security rules to add to the agent’s context window.

### Secure Supply Chain
An emerging category of Secure Supply Chain tools focuses on securing the supply chain at the source by providing mechanisms to make open source libraries safer before they are imported into your environment.

### Developer PAM
Governing developer access to infrastructure has long been overlooked: how their credentials are rotated, how just-in-time privilege workflows are enforced, and how NHI’s are managed. PAM tools excel at restoring control and consistent visibility without disrupting developer workflows.

### Code Quality
Unifying code quality and code security can consolidate tooling and integration needs. The primary benefits are the ability to manage a single scanner across development pipelines, and having a single source of truth for developers to track rules, findings, and remediation priorities.

### AI Prioritization and Remediation
AI prioritization and remediation continues to be one of the fastest-moving segments in application security. As frontier models improve at generating and fixing code on their own, security tools are increasingly evolving into contextual layers that guide those models toward higher-quality, safer code changes.

### Threat Modeling and Design Review
Of all the emerging tools in application security, continuous threat modeling and design review is the most exciting area. These tools work typically by integrating with existing knowledge bases and source code to build an overall threat model of an application.

### AI Application Protection
It is still too early to tell whether a dedicated vendor will be required to do AI application security, but dedicated startups are offering capabilities that go beyond larger platforms.

---

## Conclusion
The application security landscape is undergoing a profound transformation driven by AI. While the core scanners (SAST, SCA, Secrets) remain foundational, their value is increasingly defined by their integration, developer experience, and ability to leverage AI for prioritization and remediation. Organizations that focus on reducing friction and providing actionable, contextual insights will be best positioned to secure their software in this new era.

---

## Vendor Spotlights
[Content omitted as per original document structure]

---

ifying how an organization is using AI.

As a team prioritizes runtime protection, conversation guardrails, and MCP gateways, the
likelihood of needing a dedicated AI security provider increases. This is where tools like Pillar
and Operant are clearly differentiated, as they provide both runtime protection and granular
visibility into AI-driven applications, alongside a more robust mapping of AI application
architectures.

Setting aside the hype, AI red teaming is largely another form of DAST, where inputs are injected
into a different type of system and outputs are evaluated, often by another LLM, for
inappropriate or unsafe behavior. Similarly, AI BOMs and model discovery often resemble
extensions of SCA scanning, as models are frequently packaged as Python or JavaScript
libraries. That said, the maturity of these capabilities varies widely across providers.

One area that is especially compelling about ADR and CADR-style providers is their ability to
secure AI applications from inside the running application itself. While many tools rely on
observing inputs and outputs to infer how a model reached a particular outcome, ADR operates
within the application, allowing it to observe chains of thought and tool calls far more natively.

We will cover the AI Application Security market in more detail later this year, but more details
are available in the 2025 AI Security report.

Application Security Market Report 2026

35

Of all the emerging tools in application security, continuous threat modeling and design review

is the most exciting area, both for the immediate value they provide and for their long-term

impact on AI-driven code generation. These tools work typically by integrating with existing

knowledge bases and source code to build an overall threat model of an application. From

there, they continuously monitor changes to deliver ongoing design reviews and updated threat

models as new systems are deployed.

Having a clear architectural view gives these tools a strong advantage when providing context to

AI agents, which often struggle to understand an organization’s broader application

architecture. These guardrails can then be applied directly to new code generation, allowing

teams to enforce organizational standards consistently across their codebase.

BUYER’S GUIDE

Picking the right tool varies and depends on individual tech
stacks and priorities. The Latio Buyer's Guides exist to provide
clear and actionable considerations when searching for the
best available tools.

SMB and Mid-market Buyer’s Guide

Application Security Market Report 2026

37

SMB and Mid-market

Infrastructure Vulnerability Scanning

Application Security

SCA

SAST

Secrets

Runtime Solution

EDR

XDR

MDR

CADR

SIEM

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
Having a workﬂow that’s consolidated around cloud hosted products
Not using too many tools

Spending the least amount of money as possible

Companies in this position will want to consolidate as many features into one application
security tool as possible to save on management overhead.

Application Security Market Report 2026

38

The two key questions to answer in order to conﬁdently guide your tool choice are:

Do you want a separate platform for cloud security? While most of our survey respondents
wanted separate tools, they’re not always needed right away, or at all, depending on your
speciﬁc architecture. There are beneﬁts to consolidating these tools, but they’re often
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

Valuable API testing is difﬁcult to build and maintain

While traditional DAST scanning has lost its value, meaningful API testing is an important part
of a mature security program. We recommend that teams introduce a DAST that is API driven
to support modern architectures, as older DAST scanners will provide little to no additional
value in these environments.

There are two key trends that SMB and Mid-Market companies should be conscious of when
thinking about tech stack structuring. The ﬁrst is the shift from traditional in-pipeline scanning
to in-pipeline code review, whether through AI code quality or code security tools. This
approach can satisfy a large number of compliance requirements, while also giving developers
a more uniﬁed experience that goes beyond traditional vulnerability management models

The second trend is pairing strong static scanning with an equally strong runtime offering,
which is where the CADR category becomes particularly relevant. By combining an all-in-one
application security testing platform with robust runtime protection, mid-market companies
can achieve an extremely strong security posture. An all-in-one application security scanner
with strong AI detection capabilities, combined with a meaningful application runtime solution
is our mid-market security stack of choice.

Application Security Market Report 2026

39

Enterprise Buyer’s Guide

Application Security Market Report 2026

40

Additional Enterprise Coverage Guide

Application Security Market Report 2026

41

The most effective reductions in false positives continue to come from combining runtime

function-level reachability with cloud context. We’ve written previously about the potential

unlocked by this combination, but it is difﬁcult to fully appreciate without hands-on experience.

When using these tools, every vulnerability investigation becomes genuinely interesting,

reshaping how teams think about risk after years of being overwhelmed by noise.

Enterprise

Choosing a Platform

Application security in large enterprises looks signiﬁcantly different due to the high number of
legacy applications, diverse coding languages, deployment models, and development teams
that have built and managed their own pipeline solutions over time. Organizations with these
distributed environments often also have strict compliance requirements and long-standing
vendor relationships, which require customizations of SBOMs and multiple scanning types as
binaries are built and deployed.

These enterprises differ fundamentally from cloud-native startups and SaaS companies, where
standardized developer platforms are core to the organization. They typically operate on more
uniﬁed cloud-native architectures, with deployment processes built from the ground up or fully
migrated using consistent, standardized approaches.

The ﬁrst step of our buyer’s guide is intended to highlight this distinction between sprawling
developer environments and fully modernized ones. On one side, there are vendors that support
a wide range of testing methods and workﬂow requirements, designed for large enterprises and
their often complex compliance needs. On the other side are vendors that function well as
all-in-one application security solutions, either through deep customization, strong extensibility
into existing platforms, or broad coverage of the many use cases enterprises require.

Additionally, the vendors listed in the cloud native architecture section are not meant to be
exhaustive. Nearly every company shown in the mid-market diagram can ﬁt into an enterprise
stack, with different trade-offs depending on organizational priorities.

Approaches to False Positive Reduction

Vulnerability prioritization and reduction is a massive challenge on its own for large enterprises.
For this reason, static function-level reachability and AI-driven prioritization are important
differentiators, but their maturity varies widely by vendor and language, and often depends on
proprietary vulnerability databases that are difﬁcult to assess externally. In general, static
reachability requires longer CLI-based scans to produce strong results, particularly for statically
typed languages.

Vendors have also taken different approaches to AI prioritization. Some build deep, proprietary
indexes of customer codebases and run sophisticated prioritization logic, while others rely on far
more superﬁcial techniques, such as prompting general-purpose LLMs with a ﬁnding and its
surrounding code.

Application Security Market Report 2026

42

At the same time, developing AI coding guardrails are also a major concern for enterprises, as

they aggressively encourage developers to adopt AI-assisted coding. The vendors highlighted in

this category have all taken meaningful steps toward providing management capabilities and

guardrails for AI coding agents. That said, it is still early for this category, as frontier AI solutions

are evolving so quickly that it can be difﬁcult to determine what best-practice security

architectures should look like.

On top of those points, continuous threat modeling and design review remain signiﬁcant

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

The most effective reductions in false positives continue to come from combining runtime
function-level reachability with cloud context. We’ve written previously about the potential
unlocked by this combination, but it is difﬁcult to fully appreciate without hands-on experience.
When using these tools, every vulnerability investigation becomes genuinely interesting,
reshaping how teams think about risk after years of being overwhelmed by noise.

Best in Class Solutions

Once a broad approach to vulnerability discovery and prioritization is in place, several additional
options for expanding your security program are possible. The ﬁrst is the traditional ASPM
category, which focuses primarily on vulnerability management. These tools work well for
organizations with large, distributed teams that need visibility into what is and is not covered
across their existing scanner ecosystem.

The second option is adopting a dedicated software supply chain security provider. These tools
typically offer more advanced reachability and license management, at the cost of introducing
an additional vendor. In many cases, however, they deliver enough additional value, such as
runtime protection, SBOM management, or developer autoﬁx capabilities, to justify their place
as standalone offerings.

The ﬁnal option is investing in a dedicated dynamic scanning solution. While many application
security platforms offer some dynamic scanning capabilities, these offerings are maturing due to
acquisitions in the space. For teams that prioritize API-ﬁrst scanning and modern web
architectures, a standalone dynamic scanner is often still worth the investment.

Investing in Emerging Capabilities

For some teams, investing in point solutions that address emerging capabilities, or selecting a
platform based on strong support for a speciﬁc capability, can be sound decisions, depending
on organizational focuses. For example, open source supply chain attacks disproportionately
target crypto businesses, making upstream malware detection and secure package registries
especially important selection criteria for teams operating in that space.

Beyond supply chain risks, investments in application security scanning are introducing new
considerations for how enterprises evaluate tools. A key consideration is business logic
detections, one of the most impactful application security scanning developments available
today. These tools unlock entirely new categories of ﬁndings, and typically provide strong false
positive reduction methodologies as well.

Application Security Market Report 2026

43

Vulnerability prioritization and reduction is a massive challenge on its own for large enterprises.

For this reason, static function-level reachability and AI-driven prioritization are important

differentiators, but their maturity varies widely by vendor and language, and often depends on

proprietary vulnerability databases that are difﬁcult to assess externally. In general, static

reachability requires longer CLI-based scans to produce strong results, particularly for statically

typed languages.

surrounding code.

Vendors have also taken different approaches to AI prioritization. Some build deep, proprietary

indexes of customer codebases and run sophisticated prioritization logic, while others rely on far

more superﬁcial techniques, such as prompting general-purpose LLMs with a ﬁnding and its

At the same time, developing AI coding guardrails are also a major concern for enterprises, as
they aggressively encourage developers to adopt AI-assisted coding. The vendors highlighted in
this category have all taken meaningful steps toward providing management capabilities and
guardrails for AI coding agents. That said, it is still early for this category, as frontier AI solutions
are evolving so quickly that it can be difﬁcult to determine what best-practice security
architectures should look like.

On top of those points, continuous threat modeling and design review remain signiﬁcant
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

Application security is a discipline in crisis. Developer workﬂows are changing rapidly and the
reality is that we are in a period of transition. Traditional scanning methodologies still have a
place, but things are quickly evolving.

There are bold promises from nearly every vendor around securing AI-generated code, but in
practice much of the heavy lifting is still being done by frontier models. In the meantime, there
are also exciting developments that are helping teams reduce backlogs and uncover more
meaningful vulnerabilities.

For all the approaches to securing AI-generated code, the real security beneﬁts are still
emerging. Looking ahead to practitioner tool roadmaps for the coming year, robust runtime
protection remains a key priority, as the AI-driven SDLC is still taking shape. By this time next
year, it should be much clearer what this new SDLC looks like, and which vendors are doing the
best job securing it.

Application Security Market Report 2026

44

For some teams, investing in point solutions that address emerging capabilities, or selecting a

platform based on strong support for a speciﬁc capability, can be sound decisions, depending

on organizational focuses. For example, open source supply chain attacks disproportionately

target crypto businesses, making upstream malware detection and secure package registries

especially important selection criteria for teams operating in that space.

Beyond supply chain risks, investments in application security scanning are introducing new

considerations for how enterprises evaluate tools. A key consideration is business logic

detections, one of the most impactful application security scanning developments available

today. These tools unlock entirely new categories of ﬁndings, and typically provide strong false

positive reduction methodologies as well.

Application Security Vendor Map

The below map indicates the vendors focused on speciﬁc categories of scanning, versus which
provide bundled options. This is designed to help organizations think through coverage, but it
doesn't indicate scanner maturity.

Application Security Market Report 2026

45

VENDOR
SPOTLIGHTS

All vendors were given the opportunity to
spotlight their product by having the Latio
team author a dedicated page explaining
why they were awarded in this report.

Wiz has quickly evolved beyond cloud security to become a leader in the application security market as
well. While its core code-to-cloud capabilities remain as strong as ever, the ability to ingest ﬁndings
from other tools has also made Wiz a centralized vulnerability management platform. At the same time,
they have rapidly built and expanded their in-house scanning capabilities to a level that now rivals
many dedicated application security providers.

Beyond the scanning capabilities themselves, Wiz continues to lead in contextualizing and prioritizing
ﬁndings across the SDLC. Whether issues are tied to infrastructure resources or source code
repositories, the Wiz graph provides an elegant way to visualize relationships and drive remediation
workﬂows. This ensures the most relevant issues are routed to the right place with context on what
needs to be ﬁxed and why.

On the runtime side, Wiz has signiﬁcantly matured its attack surface management capabilities to
include AI-driven penetration testing, along with API discovery and runtime function-level reachability.
Bringing all of this data together in a single platform positions Wiz as the most complete code-to-cloud
offering on the market, giving both security and engineering teams a single place to reduce risk and
prioritize.

The Beneﬁts of Wiz

Centralized Visibility

Developer Context

End-To-End Coverage

Manage application and cloud
security ﬁndings across code,
infrastructure, and third-party tools.

Provide actionable context through
graph-based relationships that link
vulnerabilities to real-world impact.

Combine static, runtime, and attack
surface insights for comprehensive
code-to-cloud visibility.

GitHub Advanced Security has quickly become a strong competitor across traditional application security categories,
particularly secret scanning, SAST, and SCA. While many tools attempt to be “developer-friendly,” GitHub is the only
platform developers actually love, adopt, and use on their own! This organic expansion into security signiﬁcantly
increases developer adoption, and empowers them to directly customize workﬂows without friction. The result: tools
are actually operationalized, preventing leaks and security incidents, and reducing risk across application portfolios
of all sizes.

On the scanning side, GitHub has implemented leading features such as incremental scans, code quality scanning
and out of the box push protection for secrets. GitHub has also invested in scalable remediation workﬂows —
combining security campaigns with GitHub Copilot to make the remediation process as seamless and automated as
possible. Copilot is one of the few AI coding tools broadly trusted for enterprise development, and its ability to
generate large volumes of remediation pull requests materially accelerates vulnerability ﬁxes.

GitHub is also embedding security directly into the code generation process by scanning code as it is produced by AI
agents. This adds an additional layer of protection during AI adoption itself. Combined with GitHub’s close
integration with Microsoft Defender for Cloud to analyze and establish runtime risk, GitHub stands out as a strong
option for enterprises looking to scale AI-driven development without compromising security.

The Beneﬁts of GitHub

Native Developer
Experience

Built directly into developer
workﬂows developers already trust
and use daily.

Deep Rule Customization

AI-Driven Remediation

Enables teams to write, extend, and
maintain custom security logic with
CodeQL.

Uses Copilot agents and campaigns to
accelerate ﬁxes at enterprise scale.

Datadog’s Application Security offering covers the full set of scanning capabilities teams expect,
alongside leading runtime protection features. On the static analysis side, Datadog supports multiple
implementation models, ranging from IDE through to runtime scanning. After integrating source code
repositories, teams can track and manage SAST, SCA, Code Quality, Secrets, and IaC ﬁndings across
their environments, with ﬂexibility in how scans are conﬁgured and maintained.

Datadog’s leading agentic capabilities deliver beneﬁts for application security workﬂows by giving
teams accurate remediation guidance and prioritization. These features pair well with Datadog’s
broader Bits AI Agents offering, helping to prioritize and remediate security issues.

The value of their scanning capabilities is ampliﬁed by Datadog’s access to runtime telemetry. By
correlating static ﬁndings with runtime behavior and threat detection signals, teams gain deeper
visibility into how applications actually operate in production. Beyond scanning and detection,
Datadog has contributed to research focused on areas such as malicious IDE extensions and software
supply chain threats. From leading threat research to scanning capabilities, Datadog is a complete
application security platform.

The Beneﬁts of Datadog

Work With Developers

Runtime Context

Detection Engineering

Let developers work with the tools
they’re already the most
comfortable with.

Correlate security ﬁndings with
real-world application behavior using
native telemetry.

Beneﬁt from ongoing detection
research across cloud and application
attack surfaces.

Since their founding in 2022, Aikido has evolved from a simple bundled application security offering
into a platform with leading capabilities across several categories. From robust SAST customization, to
open-source malware research, to leading innovations in AI Pentesting, Aikido focuses on delivering
features that matter most, improving developer experience while also strengthening real-world
security outcomes.

From a scanning perspective, Aikido provides strong reachability analysis, ﬂexible SAST customization,
and a highly robust autoﬁx architecture. These capabilities are designed to reduce developer noise
through a large set of handcrafted and sensible mitigations for some of the most common vulnerability
classes. When combined with the Zen runtime module and cloud capabilities, Aikido is able to add
meaningful organizational and runtime context, helping teams signiﬁcantly reduce false positives -
expanding even to proactive protection.

Aikido has also been at the forefront of several emerging capabilities: AI penetration testing, attack
surface management, code quality analysis, and AI code security. The platform is a strong offering for
companies of any size looking to improve their developer experience, false positive rates, and adoption
of the latest technologies.

The Beneﬁts of Aikido

Scalable Pricing

Contextual Prioritization

AI-Driven Coverage

Aikido provides clear pricing and
bundling options for companies of
every size.

Improve prioritization with runtime
and organizational context, alongside
strong reachability capabilities

Apply AI-based scanning for both
security and code quality use cases.

Palo Alto Networks Cortex Cloud is a strong ﬁt for security teams looking for integrated scanning or to extract more
value from their existing tools while also adding robust ASPM, software supply chain and cloud security capabilities.
With Cortex Cloud, teams can build a clearer picture of how vulnerabilities enter their environment and where
exploitable paths could lead to real-world impact.

Cortex Cloud natively supports IaC, SCA and secret scanning, alongside the broader set of ASPM, software supply
chain and cloud security capabilities expected from a CNAPP platform. In addition, it can ingest results through
native integrations with a wide range of third-party scanners, allowing organizations to improve prioritization without
disrupting their existing development tools and processes.

As with other areas of Cortex Cloud, its primary strength lies in the Command Center experience bringing together
context from across the application lifecycle to make ﬁndings actionable. Teams can also assess security coverage
across their codebase and gain visibility into any gaps. The AI Guardrails automatically suggest policies tailored to
your environment to stop new risks before they reach production.

The ﬂexibility and conﬁgurability of Palo Alto Networks application security capabilities make Cortex Cloud a
compelling option for AppSec teams seeking preventing vulnerabilities getting to production, better prioritization
and supply chain.

The Beneﬁts of Palo Alto Networks Cortex Cloud:

Prevention-First

Uniﬁed Visibility

Enforce AI generated policies that
target and block risks based on your
overall infrastructure context.

Centralize ﬁndings from native and
third-party scanners to improve
prioritization, analyze coverage gaps,
and accelerate remediation from a
single interface.

AI Prioritization and
Remediation

Enables prioritization, coverage
analysis, and remediation from a
single interface.

Semgrep is one of the most developer-oriented platforms on the market. They pioneered making security
scanning accessible with their open source engine, which remains highly distributed and relied on by
organizations of all sizes. Semgrep has expanded to offer the cloud-native integrations along with robust
SCA and secret detection capabilities that practitioners expect from a modern application security platform.

Semgrep has also architected AI-driven detection, prioritization and remediation in ways that work
consistently for enterprise environments. The engineering thoughtfulness behind these features
delivers a set of AI capabilities that teams can adopt with conﬁdence - whether detecting business logic
ﬂaws with AI SAST, or driving remediation with autoﬁxes. Beyond AI, Semgrep’s secret detection
remains a standout feature, particularly due to its semantic analysis approach, which goes well beyond
traditional pattern searching methods.

Semgrep is especially well suited for developer-ﬁrst organizations that encourage teams to actively
optimize and maintain the scanning engine they’re using. The maturity of the scanning engine, combined
with the ﬂexibility of its rule customization, makes Semgrep an enterprise ready application testing
solution. At the same time, its distributed and open source roots also make it a strong ﬁt for mid-market
organizations that often begin their journey with the open source offering before expanding further.

The Beneﬁts of Semgrep

Developer Native

Customize Everything

Deliver a truly developer-ﬁrst security
experience with fast, local, and
CI-friendly scanning.

Reduce noise with semantic analysis
and highly customizable rule sets.

Enterprise-Ready AI
Remediation

Utilize AI-driven prioritization and
remediation with conﬁdence in large
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
workﬂows. As a result, Invicti is well suited for mid size enterprises looking for all-in-one AppSec
platforms, or for enterprises that prioritize a dedicated DAST solution and want ﬂexibility in how they
manage and evolve their existing application security tooling.

The Beneﬁts of Invicti

Discover Undocumented
API and LLM

API and AI-Assisted
Testing

Multi-layered approach to discovery,
including during scans, source code
analysis, gateway integrations, and
network trafﬁc analysis.

Test APIs and leverage AI-based
techniques to improve context and
identify complex issues.

Tool Orchestration

Coordinate existing and open-source
scanners to support broader
application security workﬂows.

Corgea has built a strong AI-ﬁrst approach to application security, using AI across vulnerability discovery,
prioritization, and remediation. While many vendors claim to use AI for better prioritization, Corgea has
delivered real differentiation in how effective these capabilities are across each of those areas.

As AI coding becomes more common, developer expectations for security tools are rising, both in
terms of the relevance of ﬁndings and how teams interact with them. Corgea’s AI-driven SAST engine
consistently surfaces ﬁndings that are practical and meaningful. I have seen ﬁrsthand the value of these
discoveries, particularly in identifying business logic ﬂaws that lead to real-world attacks, rather than
the typical volume of low-value false positives produced by traditional tools.

On the workﬂow side, the Corgea team has invested heavily in modern, AI-ﬁrst developer experiences.
Developers can interact directly with pull request comments through chat-based workﬂows that feel
natural and intuitive. This creates reviews that resemble thoughtful, informed security feedback rather
than rigid pipeline blocks that disrupt development.

Overall, Corgea is one of the more exciting companies in application security as AI reshapes what is
possible across detection, prioritization, and remediation.

The Beneﬁts of Corgea:

AI-Driven Discovery

Relevant Prioritization

Developer-Native Reviews

Identiﬁes meaningful vulnerabilities,
including business logic ﬂaws, that
traditional scanners often miss.

Uses AI context to reduce noise and
surface issues that pose real security
risk.

Delivers conversational, PR-based
feedback that aligns with modern
developer workﬂows.

Snyk pioneered the modern DevSecOps experience by giving developers immediate access to security ﬁndings
across their code base. Most recently, Evo by Snyk brings many of the capabilities of dedicated AI security tools
into the context of Snyk’s broader ecosystem, creating a developer ﬁrst approach to securing AI-Native
applications, while giving security engineers visibility into the new wave of AI tools.

Snyk’s newest capabilities give teams visibility into developer endpoints, including which MCPs and coding agents
are in use, and the ability to track and enforce standards across those endpoints. This visibility forms the foundation
for enforcing guardrails on AI generated code. Using Snyk’s MCP for agents, coding tools can retrieve additional
security context to generate higher-quality code by default and to produce more effective remediations.

The broader Snyk platform remains a ﬂexible option for organizations managing a wide range of languages,
frameworks, and deployment models at enterprise scale. Across its product lines, Snyk has built a robust and
continually evolving knowledge base of vulnerabilities and ﬁndings that support consistent security outcomes
across diverse environments. These capabilities combined with AI capabilities help enterprises looking to safely
adopt AI tooling.

Overall, Snyk continues to be a strong choice for enterprises seeking a mature DevSecOps platform, while
actively preparing for widespread adoption of AI-assisted code generation.

The Beneﬁts of Snyk

AI-Aware Guardrails

Applies security standards directly to
AI-driven code generation workﬂows.

Developer Endpoint
Visibility

Tracks agents, tools, and usage
patterns to enforce consistent
security controls.

Enterprise Platform

Supports broad language coverage
and scalable security management
across teams.

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
the organization’s security postures and scans code as it is created to prevent ﬂaws at the source. Corridor also
provides a pull-request reviewer as a ﬁnal check to make sure code is secure and compliant before it is merged.

When these capabilities are uniﬁed, the platform delivers an end-to-end improvement over traditional scanning
approaches. Organizational context is used both to secure code as it is generated and to provide developers with
more meaningful, actionable feedback.

The Beneﬁts of Corridor

Secure-By-Default
Generation

Applies organizational security
standards directly within AI code
generation workﬂows.

Contextual Code Reviews

Deep AI Tooling Integration

Replaces noisy ﬁndings with AI-driven
reviews that understand code intent
and usage.

Native tool integration allows
developers to scan code and ﬁx vulns
from their coding agent.

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
without addressing real migration complexity. Konvu goes signiﬁcantly further by delivering complete,
end-to-end patches for major version upgrades, making complex dependency migrations far more
achievable for engineering teams.

The Beneﬁts of Konvu

No Rip and Replace

Agentic Triage

Konvu plugs into your existing
scanners and pushes decisions back
where teams already work, no new
dashboard needed.

Konvu’s agents run exploitability
analysis in the customer’s context,
executing a CVE speciﬁc investigation
plan with reproducible checks.

Evidence Backed Decisions

Every outcome comes with clear
reasoning and supporting evidence
so AppSec and developers can trust
the results, and keep an audit trail.

Cycode is one of the most comprehensive application security platforms on the market, spanning
software supply chain security, application security testing, and posture management. Cycode can
function as an all-in-one application security solution, or as a unifying risk-based platform for
vulnerabilities across Cycode and third-party scanners, depending on an organization's needs.

Cycode’s core strength has long been its context intelligence graph - combining data across code,
infrastructure, and security ﬁndings. This graph allows teams to quickly correlate signals to prioritize
exploitable vulnerabilities based on risk and codify why, how, and by whom security decisions and
actions are made throughout the vulnerability lifecycle.

More recently, the team has focused on extending the context intelligence graph to orchestrate AI
agents. By providing agents with contextual intelligence, Cycode enables them to emulate security
decisions, such as contextual blocking and targeted remediation campaigns. This approach equips
security teams to scale alongside developer AI usage.

Whether an organization is looking to replace individual application security testing tools or orchestrate
and manage a diverse set of existing scanners, Cycode remains a leading option in the market.

The Beneﬁts of Cycode:

Comprehensive Coverage

Contextual Risk Graph

AI-Enhanced Orchestration

Spans supply chain, testing, and
posture management within a single
platform.

Maps ﬁndings to ownership,
exploitability, and impact across the
codebase.

Uses rich context to drive smarter
blocking, prioritization, and
remediation campaigns.

Upwind Security was the ﬁrst platform to meaningfully combine API security capabilities with those of a traditional
CNAPP. By leveraging deep runtime, application, and layer 7 data, Upwind delivers API discovery, dynamic testing of
APIs and AI/LLM risks, vulnerability prioritization, and can even serve as a replacement for standalone API security
tools. Upwind is unique in pairing these features with the standard suite of CNAPP capabilities, especially agentless
scanning, CSPM, and vulnerability management.

Upwind’s dynamic testing capabilities are especially strong and exceed what most traditional vulnerability solutions
offer today. By collecting network logs directly, the platform deploys contextual tests that reﬂect real application and
network ﬂows, alongside comprehensive API fuzzing and API spec generation. This approach gives teams visibility
into how applications actually behave in production, rather than relying on static assumptions.

Among CNAPP providers, Upwind has invested the most heavily in runtime function-level reachability. This capability
enables more accurate prioritization, and signiﬁcant false-positive reduction. These function-level insights also
extend into Upwind’s Cloud Application Detection & Response (CADR) capabilities, creating a cross-layer runtime
protection platform that combines cloud, application, and network security into single detection events.

Overall, Upwind remains a deeply runtime-focused CNAPP, built from the ground up to deliver traditional CSPM
capabilities alongside advanced runtime security technologies. These capabilities make it a great selection for teams
looking to get the most value out of their cloud security solution.

The Beneﬁts of Upwind:

Better Detections, Faster
Response

Combine cloud, workload, and API
data to fully detect threats from start
to ﬁnish, and give teams the context
they need to respond.

Improved Dynamic Testing

Use real network and application data
to drive more accurate API testing
that’s contextual to your environment.

Function-Level
Prioritization

Reduce alert volume by prioritizing
only the vulnerabilities that matter
most, focusing on what’s executing in
your environment.

Legit Security is frequently a reference point for enterprises looking for an application security posture management
tool. They were the ﬁrst to make me aware of the ASPM category, and when I saw the product, the solution
immediately made sense for those dealing with the “too many scanners” problem. Development teams at large
enterprises frequently manage their own pipelines and tools, leading to sprawling and uncertain scanning coverage.
Legit steps in to provide teams with a strong mapping of their deployment pipelines, cloud-based or on-premise, and
assigns risk and coverage scores as code moves through to deployment.

Within the last few years, Legit has expanded well beyond providing a pure management layer. The platform now
includes scanning capabilities like SAST and SCA, API reachability, and signiﬁcant change tracking. For management
and consolidation use cases, these additions have meaningfully increased the overall value of the solution.

With the recent launch of VibeGuard, Legit Security is on the front lines of addressing challenges with AI code
generation. VibeGuard covers critical capabilities, starting with securing AI code generation tools - IDE’s, MCPs, and rules
- preventing attacks like prompt injection and unapproved secret access. It then helps to secure code as it’s generated by
fetching organizational and security context, allowing teams to enforce security standards on AI generated code.

Together, these capabilities form a holistic, modern platform that is particularly well suited for enterprise environments.

The Beneﬁts of Legit Security

Gain Visibility Across
Deployment Pipelines

Enforce Governance for
AI-Generated Code

Track Changes Across
Enterprise Environments

Track and monitor workﬂows to
maintain oversight across dispersed
development teams, gaining a
complete coverage map of your SDLC.

Embed AI Governance into
development ﬂows, securing end to
end developer usage from code
generation to ensure secure MCP
usage.

Teams can assess overall coverage and
security posture across their tooling,
while using Legit to close gaps across
traditional scanners and emerging
AI-driven coding workﬂows.

Clover Security is a leader in the emerging category of AI threat modeling and design review, which has the potential to
reshape the entire application security industry. Clover’s ability to generate ongoing security design reviews unlocks
two key capabilities. First, it signiﬁcantly accelerates and improves the quality of threat modeling across an organization.
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
business logic ﬂaws as early as possible.

By combining these capabilities together, Clover provides a new kind of end to end application security platform -
one that helps you design an effective security program, and implement it across the SDLC.

The Beneﬁts of Clover Security

Continuous Threat
Modeling

Context-Aware Design and
Code Reviews

Secure-By-Default
Enforcement

Improves coverage and consistency
by making threat modeling an
ongoing process.

Uses organizational knowledge to
deliver more accurate and relevant
security guidance.

Carries security intent from AI coding
through deployment without manual
intervention.

Enterprise vulnerability management programs fail because scanners rarely answer the three questions
that drive remediation: who owns it, where is it running, and what is the fastest, lowest-impact ﬁx. For
organizations that prioritize actionable attribution and operate in regulated industries, many platforms
overlook the customization details required to operationalize remediation. Phoenix Security has
consistently stood out for its attention to enterprise-level details that make vulnerability management
work at scale.

One of Phoenix’s primary differentiators is its ability to align asset attribution, code-to-cloud correlation,
and reachability analysis with business goals, regardless of which scanning tools feed into the platform.
This allows teams to maximize the value of their existing scanners rather than being forced to adopt
entirely new ones. These beneﬁts extend to providing AI prioritization and remediation.

Phoenix’s attribution model is designed for distributed enterprises where ownership changes, services
are ephemeral, and data resides across multiple systems. Phoenix supports PYRUS CMDB-as-code
patterns and integrates with enterprise sources of truth to ensure accurate ownership. Phoenix also uses
AI across the platform, from vulnerability enrichment to remediation. These features make Phoenix a
strong option for enterprises seeking a scalable, conﬁgurable vulnerability management solution.

The Beneﬁts of Phoenix Security:

Attribution at Enterprise
Scale

Phoenix’s attribution CMDB enables
teams to manage asset ownership
across their entire lifecycle
programmatically.

Tool-Agnostic Reachability

Reduce false positives by applying
native provenance, lineage, and
reachability analysis on top of
existing scanners, drastically
reducing vulnerability counts.

AI Prioritization and
Remediation

Phoenix’s AI systems analyze threat
intelligence data to predict the threat
types most likely to lead to
exploitation, and provide precise
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
with conﬁdence.

Contrast provides testing and remediation by determining which vulnerabilities are truly reachable and
uncovering novel exploits in live applications, rather than relying solely on historical CVE data. For teams
prioritizing a runtime-ﬁrst approach across application security and SecOps, Contrast is a compelling option.

The Beneﬁts of Contrast Security

Runtime Application
Visibility

Provides deep insight into how
applications behave in real
production environments.

High-Fidelity Detection
and Protection

Surfaces precise payloads and attack
paths to support conﬁdent
investigation and response.

Reachability-Driven SCA

Identiﬁes exploitable vulnerabilities
across custom code and open-source
dependencies based on runtime
reachability.

Raven has built a leading Application Detection Response (ADR) solution for companies to protect critical
applications. Raven unlocks the missing piece of workload protection for software teams by preventing malicious
deviations, whether a CVE exists or not. In an age where attackers are leveraging AI to automate exploitation, having
a prevention solution for CVE-less threats is more valuable than ever. Using deep application inspection at runtime,
Raven is able to tie functions that execute back to the original code that produced them, and prevent libraries from
executing attacker manipulated paths.

With ADR, developers get the insights they need to separate action from noise by contextualizing alerts to an
application’s environment, and security is able to prevent attacks, known and unknown, so patching isn’t done under
ﬁre. Under the barrage of open source and AI assisted exploits, teams need better ways to protect themselves
besides waiting for a patch to be released.

Raven helps with incident response and vulnerability management by offering teams the critical application layer
insights they’ve been missing. They do this with low overhead, offering out of the box performance dashboarding
with common developer tools. Beyond insights alone, Raven even offers an elegant proactive protection solution by
permissioning libraries into known categories of system calls, enabling true zero day protection.

For enterprises looking to bring their applications into their security program, and mitigate advanced attacks, Raven
is a great solution.

The Beneﬁts of Raven

Prevent Attacks

Eliminate Vulnerabilities

Simple Deployment

As application layer attacks continue to
increase, prevent the latest attacks
while giving your team time to patch,
while keeping your application running.

Respond only to known vulnerable
function executions, prioritizing what
matters.

Deploy an extremely efﬁcient sensor
in minutes to immediately reduce your
vulnerability counts by 99% and stop
malicious code before it executes.

Checkmarx has done an impressive job delivering the power of a modern, cloud-driven, AI-focused DevSecOps
platform without sacriﬁcing the depth or precision of its historically robust scanning engines. For organizations
looking to modernize application security at scale, the Checkmarx One platform offers strong coverage across
scanning categories without compromising core capabilities.

Checkmarx has been steadily raising the bar on platform depth and precision by including features such as container
image layer analysis, detailed customization of SAST ﬁndings, custom query development, and an IDE experience for
agentic development lifecycles. These capabilities have been rolled out across a broad set of languages at enterprise
scale, giving customers access to modern application security workﬂows without losing depth.

One of Checkmarx’s long-standing strengths has been the level of customization it provides for enterprise application
security teams. Its highly conﬁgurable scanning engines allow teams to enforce organization-speciﬁc requirements
across large and complex codebases, aligning security controls with existing standards and threat models.

Checkmarx also delivers a strong management layer for application security teams, enabling centralized rule and risk
management across diverse applications. This approach allows organizations to enforce consistent security standards
while still accounting for the unique needs of individual applications.

The Beneﬁts of Checkmarx:

Enterprise-Grade
Customization

Modern DevSecOps
Platform

Centralized Risk
Management

Enforces organization-speciﬁc
security standards across large and
complex codebases.

Delivers cloud-native AI-assisted
workﬂows without sacriﬁcing
scanning depth or precision.

Manages rules and risk consistently
across applications and teams.

GitGuardian has matured into far more than a secret scanning tool. The detection engine is built and optimized
for scanning at internet scale. It leverages a deterministic rules engine to identify secrets, paired with AI to ﬁlter
false positives and increase context. This distinction matters because understanding whether a secret has been
leaked publicly or exposed elsewhere is what determines risk and allows teams to prioritize.

By expanding detection beyond source code, GitGuardian delivers additional value through identifying secrets across
other platforms such as Slack and workforce tooling. This broader visibility enables teams to take a more comprehensive
data loss prevention (DLP) approach to secrets management, instead of narrowly focusing on code repositories.

Risk assessment in GitGuardian tests the validity of credentials while simultaneously connecting with IdPs and
applications to enumerate identities and their permissions. By cross-referencing these with identiﬁed secrets, the
platform provides a precise understanding of the potential blast radius. It also identiﬁes which workloads actively
consume them, minimizing the risk of breaking production applications.

These capabilities make GitGuardian a more holistic non-human identity security solution, providing both proactive
and reactive identity security controls across the organization.

The Beneﬁts of GitGuardian

Broader Secrets Detection

Remediation Context

Identify exposed secrets across code
repositories, collaboration tools, and
public sources, taking advantage of a
highly tuned hybrid detection engine.

Assess potential impact by
understanding permissions, active
usage and exposure, allowing teams
to remediate based on severity.

Non-Human Identity
Coverage

Support proactive and reactive controls
for secrets and machine identities across
the organization, including detection
and response with HoneyTokens.

Category Innovators

AI Code

Supply Chain

Runtime

AI Platform

AI Pentesting

Secrets Security

DAST

API Security

Developer Experience

Deﬁnitions

Platform Leader

Leaders in this category are built to be the only application security platform teams need. This
means including all core application security scanning capabilities alongside cloud and runtime
context features for prioritization and team context. Leaders in this category have made large
investments in the latest scanning features, without sacriﬁcing the overall platform.

Testing Leader

This category represents the companies who meet the diverse requirements of enterprise use
cases - meaning support for the wide variety of languages, scan types, and reporting that these
companies need. They also have robust hosting, customization, and tertiary support services.

Management Leader

Leaders in this category are built for integrating with numerous scanners to drive workﬂows
with rich application context, creating an orchestration platform for remediating vulnerabilities.
While they often provide their own scanning tools as well, the strengths of these platforms are
in their ability to consolidate data across massive environments, creating uniﬁed remediation
workﬂows.

AI Code Innovator

This award is for companies investing in new technology for securing AI generated code by
both securing employee workstations against MCP supply chain and rule injection attacks, and
giving AI coding agents the context they need to deploy secure code. These emerging tools
are designed to work with AI coding development tools to create secure code by default.

Supply Chain Innovator

Companies in this category have innovated in speciﬁc ways for teams with supply chain
security concerns. Vendors in this category are highlighted for their investments in legal
analysis, malware detection, package health, prioritization, or autopatching capabilities.

Runtime Innovator

Innovators in this category excel at protecting applications against runtime threats. This
category is about representing tools that don’t merely detect ongoing application attacks, but
also offer various threat mitigation capabilities, allowing enterprises to respond in seconds to
the latest application attacks.

Category Innovator

These awards acknowledge companies who are especially innovating within either a speciﬁc
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
program is ﬁnding the right product ﬁt for both vendors and buyers.

We are creating a future where every decision is based on tests, market
insights, experience, and hard work, where it’s easy to ﬁnd the right product
you’re looking for.

Our mission is to help every team ﬁnd the right security product. So we test
every product, to make it easier for you to pick the right one.

A special thank you to everyone who has supported this mission, without you,
none of this would be possible.

Learn more:

(cid:31)

(cid:30)

latio.com

Schedule a security program sync

(cid:30)

(cid:31)

Schedule a product brieﬁng

Follow us

The only analyst ﬁrm that tests products,
so you can ﬁnd the right one.

Latio Tech, Inc. All Rights Reserved.