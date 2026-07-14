# The 2025 State of Open Source in Financial Services

## Table of Contents
- [Foreword](#foreword)
- [Executive summary](#executive-summary)
- [Introduction](#introduction)
- [GitHub metrics show the scope of open source activity in financial services](#github-metrics-show-the-scope-of-open-source-activity-in-financial-services)
- [Survey and interview findings](#survey-and-interview-findings)
- [Measuring the industry’s open source maturity and strategy](#measuring-the-industrys-open-source-maturity-and-strategy)
- [Strategic maturity](#strategic-maturity)
- [From consumption to contribution through policy and practice](#from-consumption-to-contribution-through-policy-and-practice)
- [What are the barriers and challenges holding the sector back?](#what-are-the-barriers-and-challenges-holding-the-sector-back)
- [Community as the accelerator to value and impact](#community-as-the-accelerator-to-value-and-impact)
- [Community drives value](#community-drives-value)
- [Opportunities across the stack](#opportunities-across-the-stack)
- [Measuring business value and ROI](#measuring-business-value-and-roi)
- [The growing value of AI](#the-growing-value-of-ai)
- [Growing investment](#growing-investment)
- [Emerging ROI](#emerging-roi)
- [The increasing role of open source](#the-increasing-role-of-open-source)
- [Business impact](#business-impact)
- [Tackling adoption challenges](#tackling-adoption-challenges)
- [Conclusions and actionable insights](#conclusions-and-actionable-insights)
- [Methodology](#methodology)
- [Resources](#resources)
- [Acknowledgments](#acknowledgments)
- [Appendix A](#appendix-a)
- [Appendix B](#appendix-b)

---

## Foreword
As I reflect on my discussions with hundreds of clients worldwide over the last year, it’s clear that the future of banking is being reshaped by open source systems. Today, banks’ technology stacks are highly complex, dominated by costly and inefficient legacy systems. Within these systems lies a mix of both strategic capabilities and necessary foundational elements.

Strategic elements, such as mobile banking apps, marketing and relationship manager tools, and pricing strategies, are unique to each bank and serve as drivers of competitive differentiation. Necessary components—including risk and regulatory compliance, reporting, basic payment services, common data models, and simple operational functions, such as physical cash management systems—provide little to no differentiation. The question for the global banking industry is: why do we collectively spend so much money on so many things for so little differentiation? This is the foundation of open source thinking—why do things individually that we could do better collectively?

By sharing the development and maintenance costs of these necessary systems, banks can eliminate redundant efforts and expenses. The capital markets sector has already recognized the benefits of this through its need to standardize data structures to facilitate trading and settlement. Extending this approach to retail and commercial banking could yield exponentially greater benefits globally, particularly in areas where standardized protocols and shared code can be leveraged.

The Linux operating system exemplifies the transformative power of open source. Linux is rapidly becoming the dominant compute engine for the banking industry, whether on-premises (on-prem) or in the cloud. And open source technologies are increasingly prevalent across all levels of the technology stack, including databases, development tools, security components, and now agentic management. Some banks have gone all-in: notably, innovative banks such as Nubank, a Brazilian digital bank offering low-cost financing through a user-friendly app, have adopted 100% open source models.

FINOS has played a pivotal role in fostering collaboration and innovation within financial services through open source software, standards, and best practices. This year’s State of Open Source in Financial Services Research report examines consumption patterns, contribution dynamics, governance structures, and cultural aspects, as well as the fast-evolving intersection of open source and generative AI (GenAI). It tackles ROI expectations for GenAI and examines the policies that either unlock or limit contributions to open source.

In banking’s next chapter, open source and AI are on the same runway for reinvention. Based on our analysis, we believe GenAI will impact nearly 75% of the work in today’s banks—changing nearly everything we do. Yet, the greatest impact may very well be in accelerating the move to open source. GenAI is already revolutionizing legacy system modernization by decoding and translating outdated code into modern languages, acting as a Rosetta Stone of sorts. Once decoded, the bridge to an open source–first bank is just a few steps away. The old banking world will increasingly look more like the Nubank world.

The banking industry has historically thrived on collaboration and shared interests. Since the establishment of the Society for Worldwide Interbank Financial Communication (SWIFT), The Clearing House, Visa, and Mastercard, the industry has benefited from collective efforts. Banks rely on shared standards, such as Wi-Fi, to drive their infrastructure. Similarly, sharing the code that underpins these standards can yield significant benefits. The real opportunity lies in extending this collaborative approach further up the technology stack. As banks operate in an interconnected world, encompassing trading, payments, and underwriting, among other functions, sharing open source code can foster a more cohesive and efficient ecosystem.

In conclusion, I am confident that the future of banking is open source. As the industry continues to evolve, embracing open source will be crucial for banks to remain competitive, efficient, and innovative. I commend FINOS for its efforts in driving this change and embracing the art of the possible. I look forward to seeing the continued adoption and innovation in open source within the financial services sector.

**Mike Abbott**
Accenture

---

## Executive summary

### Organizational maturity: from playbooks to strategic practice
Financial services firms are steadily advancing in their open source maturity, evolving from unstructured adoption to strategic engagement. Nearly half of organizations now report having an open source program office (OSPO) or equivalent, and consumption is almost universally permitted (97%), reflecting a recognition that open source software (OSS) is critical for the industry. Contribution policies are becoming more permissive, with just 2% of firms saying contributions are not allowed, and organizations are allocating more time for engineers to participate upstream. However, policies are still applied inconsistently, due in part to unclear ROI and legal/licensing concerns, leading to uneven participation and costly outcomes, such as internal forks. Some risk management practices also lack maturity. While 52% of respondents cite security vulnerabilities as their top concern and 37% point to supply chain attacks, only 43% are actively producing software bills of materials (SBOMs).

> **KEY TAKEAWAY**
> The foundations for maturity are now firmly in place. Closing the gap between awareness and execution will require firms to further strengthen consumption and supply chain management, increase contribution enablement more broadly across the organization, and engage committed leadership that recognizes the strategic value of OSS and adequately champions and resources it.

### Stronger together: community at the core of impact and value
Community is the engine of open source value. When diverse communities of adopters, contributors, and maintainers come together, they multiply benefits by improving quality, resilience, and long-term sustainability. Commercial models, from managed services to venture capital (VC)-backed offerings, reinforce this ecosystem, with evidence showing that healthier communities correlate directly with stronger valuations and growth. Respondents identified AI (49%) and cloud technologies (39%) as the most important open source technologies for the industry’s future, underscoring the centrality of collaboration in fast-evolving domains. Beyond technology, 51% pointed to industry standards as the area where open source can deliver the greatest value, reducing duplication, enabling interoperability, and helping companies tackle shared challenges. While cost savings are significant, the true value extends into innovation, collaboration, and talent development, making open source a long-term strategic asset.

> **KEY TAKEAWAY**
> Community participation is no longer optional. Organizations must prioritize engagement, contribution, and collaboration with the open source communities important to them, not just to reduce risk but to realize the full value of open source.

### Unlocking AI value: navigating momentum and maturity
AI is emerging as one of the most valuable open source technologies in financial services. For the third year in a row, respondents identified AI as the most valuable open source technology for the industry’s future (49%), with top opportunities identified across standards (56%), open models (54%), and frameworks (52%). This reflects a rapid shift from early risk aversion to large-scale adoption, positioning GenAI as a foundational technology. The returns are beginning to materialize: 18% of firms already report measurable ROI, and another 22% expect to see returns within the next year. Respondents also pointed to enhanced developer productivity (49%) as the area where GenAI will have the greatest impact. Yet, challenges remain. The most significant barrier is no longer governance but skills, with 46% citing capability gaps as the biggest obstacle. This underscores the importance of investment not only in technology but also in talent development to realize AI’s full potential.

> **KEY TAKEAWAY**
> Financial services firms must pair increasing investment in AI with deliberate talent and skills strategies while embracing open approaches that balance innovation with resilience.

---

## Introduction
Why are banks all-in on open source? This report, the fifth in a series of annual financial services industry studies into open source software (OSS) and ecosystems, provides concrete evidence to help answer this question.

The insights from our research activities to date have grounded the work that many of us do within and beyond FINOS, informing organizational strategies, policies, and approaches across the sector. Whether exposing gaps or pointing to new opportunities, the data has consistently informed decision-making. By pursuing empirical evidence from industry experts, practitioners, and executives, we have been able to trace the clear progression of open source in financial services from early readiness to adoption to demonstrable ROI. This year’s findings show just how far the industry has come, with 87% of respondents seeing open source as critical to their organization’s future and 84% believing that it’s essential to the overall sector.

Organizations are recognizing the cost savings of open source adoption, alongside benefits in software quality (93%), lower licensing costs (87%), and business value creation (89%). What began as a cost play has matured into a value play, with open source directly contributing to speed to market, regulatory success, and the ability to attract and retain technical talent. Projects such as GitProxy, FDC3, and other community-driven initiatives have become part of the production backbone of the world’s leading financial institutions.

Maturity also shows in governance. Half of organizations now have a defined open source strategy, with nearly half implementing OSPOs. As centers of internal open source competence, these offices coordinate policies, streamline contributions, mitigate risk, and ensure that open source engagement links to enterprise goals. Larger organizations, in particular, are demonstrating higher engagement across all open source activities, showing that scale and maturity go hand in hand.

Contribution practices are shifting, too. Survey data reveals that nearly half of developers are spending more time contributing to open source than they did a year ago. Motivations range from giving back to the community (33%) to influencing critical projects (29%) to reducing technical debt (28%). These drivers reflect not only altruism but also strategic alignment with business needs. At the same time, barriers persist. Concerns over unclear ROI (48%) and legal complexity (48%) remain common, underscoring the importance of clear frameworks, standards, leadership, and knowledge translation.

In 2025, no discussion of technology in finance is complete without AI. Open source is already shaping the future of GenAI in the sector, from models to frameworks to standards. Nearly half (49%) of respondent organizations believe that AI will first deliver value in internal developer productivity, with ROI horizons of two to five years. Some (18%) are already realizing returns. Open ecosystems are key here, accelerating innovation while keeping costs in check.

Ultimately, the momentum is undeniable. Banks are all-in on open source because the data shows bottom-line benefits: better code, lower costs, stronger compliance, faster delivery, and a more resilient talent pipeline. However, equally important are the bonds formed across the industry. It is the strength of the relationships among industry peers, forged through open source collaboration in FINOS and across the industry around shared challenges and purpose, that creates better technologies for all.

---

## GitHub metrics show the scope of open source activity in financial services
In this section, we explore GitHub commit activity, finding that:
- Financial services engagement in open source remains steady, with unique financial services users rising to 9,354, representing modest growth year-on-year.
- Activity is concentrated in institution-hosted projects, with much of the observed contribution coming from repositories directly hosted by financial services organizations.
- Python dominates as the language of choice, accounting for ~18% of contributions, while traditional financial services languages, such as Java (7%) and C# (3%), rank lower.

However, despite these challenges, we observe interesting patterns in the available data. GitHub provided the analysis in this section using a list of the FINOS-supplied email domains of over 400 of the largest financial services institutions (by revenue and/or assets under management), as well as those financial services organizations known to this group to be active or interested in open source. Data was included for GitHub users who made commits to any public repository with a primary email that matched an email domain in a FINOS-provided list or any users who were members of an organization that had a billing email with a domain in that same list.

In this section, we explore the open source activities of financial services organizations through publicly available data from GitHub. It is challenging to capture the full extent of open source interactions because, as we highlighted in last year’s report, policies and restrictions often push developers to use their personal accounts when interacting with GitHub.

This year, as shown in **TABLE 1**, we found that 9,354 employees from financial services organizations contributed to around 36,056 repositories, making a total of 774,732 commits. Looking at **FIGURE 1**, which shows the number of users and commits for the past five years, we can see that this year there has only been modest growth in each. Much of the activity we observe is related to projects (repositories) directly hosted by financial institutions, which is possibly a limiting factor. If financial services organizations move to a more permissive contribution model, we may see activity rise once again.

### TABLE 1: GitHub repositories with a financial services email domain
| Year | Unique repositories with financial services commits | Unique financial services users | Total commits by financial services users |
| :--- | :--- | :--- | :--- |
| 2025 | 36,056 | 9,354 | 774,732 |
| 2024 | 35,788 | 9,247 | 751,259 |
| 2023 | 36,634 | 9,009 | 595,860 |
| 2022 | 36,107 | 8,552 | 535,974 |
| 2021 | 25,280 | 6,857 | 429,258 |

![2021-2025 GITHUB DATA]

Of these ~36,000 repositories, the following have the greatest number of unique contributors, with each having ten or more (financial services) contributors:
- **oxcaml/oxcaml**— Jane Street’s production OCaml compiler for performance-oriented programming
- **man-group/ArcticDB**— a high-performance, serverless DataFrame database
- **fidelity-contributions/open-telemetry-opentelemetry-python-contrib**— a fork for Fidelity’s contributions to open-telemetry/opentelemetry-python-contrib
- **transferwise/tw-tasks-executor**— service cluster-wide asynchronous tasks executor
- **deckhouse/deckhouse**— a platform for managing Kubernetes clusters
- **Point72/csp**— a high-performance reactive stream processing library
- **finos/architecture-as-code**— a specification that enables software architects to define, validate, and visualize system architectures in a standardized, machine-readable format
- **bloomberg/blazingmq**— a distributed message queueing platform with a focus on efficiency and reliability
- **seb-oss/green**— an open source design system built by SEB

This is a relatively diverse set of projects, including design systems and UI components, compiler and IDE technology, databases, messaging, streaming, and observability frameworks.

### FIGURE 1: Growth of financial services users and commit activity within GitHub
![Line chart showing growth of unique financial services users and total commits from 2021 to 2025]

### FIGURE 2: Primary language of GitHub repositories with financial services committer activity
![Bar chart showing Python (18%) as the top language, followed by TypeScript, Go, OCaml, Java (7%), JavaScript, C++, C# (3%), Rust, Shell, Jupyter Notebook, HTML, Nix, Swift, Kotlin, and Dockerfile]

### FIGURE 3: Keyword frequency for GitHub repositories with financial services committers
![Word cloud visualization showing keywords like kubernetes, security, ai, machine-learning, hacktoberfest, and finance]

With this data, we observe the following trends regarding the types of projects that financial services organizations contribute to:
- **Cloud native and infrastructure**: The most frequent keywords in this dataset include kubernetes, kubernetes-security, and policy-as-code, together with other infrastructure-as-code-related keywords. This shows that financial services contributors are heavily engaged in container orchestration but with a strong tilt toward security and compliance.
- **Data, AI, and machine learning (ML)**: AI keywords include machine-learning, ai, llm, and data-science, together with Jupyter and JupyterLab, indicating an interest in AI/ML-related projects and interactive research and analytics.
- **Security and compliance**: Keywords include security, pod-security-policy, cryptography, and owasp, reflecting the sector’s need to maintain regulatory compliance and secure infrastructure.
- **Finance-specific open source**: Finally, we see domain-specific keywords, including finance, trading, algorithm-trading, and quantitative-finance. Although these are present, they have a smaller share of contributions. This suggests organizations are more focused on enabling technologies (cloud, security, and DevOps) than domain-specific tooling.
- **hacktoberfest**: The most frequently cited keyword is nothing to do with a specific technology or problem domain. Instead, it indicates a willingness to participate in Hacktoberfest, an annual event which encourages open source contribution. This reflects the continued and varied efforts involved in encouraging active participation and contributions to open source.

---

## Survey and interview findings

### Measuring the industry’s open source maturity and strategy
In this section, we find that:
- **Formalization is accelerating**: Nearly half of firms now report having an OSPO or equivalent structure in place, and 50% have defined an open source strategy, signaling a clear move from ad hoc adoption toward structured approaches.
- **Governance is advancing, but unevenly**: While most organizations now permit OSS consumption (97%) and many have evaluation processes, gaps remain in ensuring consistent policies, education, and alignment, leaving some firms at an early stage.
- **Organizations recognize risk but undermanage it**: Despite rising concern about vulnerabilities and attacks, fewer than half of organizations actively use SBOMs, highlighting a gap between awareness and action.
- **Contribution remains constrained**: Cultural and structural barriers still limit upstream engagement, stemming from unclear ROI, legal and licensing concerns, and governance challenges.
- **Leadership and influence matter**: CTOs, OSPOs, and developers play critical roles in shaping open source strategy, and their support and leadership help overcome cultural and compliance hurdles.

### Strategic maturity
Across the financial services industry, we’re witnessing new levels of maturity on a number of levels, illustrated by the extent and type of open source contributions.

Open source adoption in financial services has continued to mature, with organizations now shifting their focus from foundational questions of whether to use open source toward a more strategic emphasis to how to operationalize, govern, and maximize its value. The 2025 survey findings show that maturity increasingly includes formalized strategies, leadership support, and external collaboration as firms move beyond ad hoc adoption toward structured approaches that embed open source into business and technology priorities.

As **FIGURE 4** shows, 47% of respondents in 2025 reported the presence of an OSPO or equivalent initiative, with financial institutions leading fintechs in adoption (55% vs. 38%). Alongside this, half of all respondents (50%) state that their organizations now have a defined open source strategy, demonstrating that firms are increasingly aligning open source practices with business priorities and risk frameworks.

### FIGURE 4: OSS engagement across organizations
| Action | Total | Financial institution | Fintech or other |
| :--- | :--- | :--- | :--- |
| Implemented an OSPO or similar open source initiative | 47% | 55% | 38% |
| Defined a clear and visible open source strategy | 50% | 51% | 38% |
| Defined a public position on open source | 34% | 43% | 48% |
| Joined or associated with open source organizations | 45% | 53% | 48% |
| Funded open source | 37% | 49% | 43% |
| None of the above | 14% | 3% | 9% |
| Don’t know or not sure | 3% | 8% | 5% |

Organizational maturity is also reflected in how firms communicate their open source posture externally. In the survey, 38% of organizations overall report having a defined public position on open source, with fintechs slightly ahead of financial institutions (43% vs. 34%). Similarly, participation in open source organizations is rising, with 45% of financial institutions and 53% of fintechs reporting engagement. These actions not only strengthen transparency and credibility but also extend firms’ influence in shaping open source across the industry. According to RBC Capital Markets managing director Elspeth Minty, participation in open source has reached new heights as team members assume prominent leadership roles within the FINOS board and community more broadly. “We’ve seen a real evolution—from just consuming open source to feeling confident in how we contribute back, and that extends to participating in governance.”[^1]

Direct financial support for open source is another critical marker of maturity. This year, 43% of respondents overall indicate that their organizations provide funding through foundation memberships, sponsorships, or contributor programs. Fintechs (49%) are more likely than financial institutions (37%) to make these investments, signaling a growing recognition that sustainability requires active stewardship of shared technologies.

Maturity also extends past governance to leading in the development of innovative projects. For James McLeod, open source lead at NatWest, organizational maturity among banks in open source is more evident today than in days past. He says, “I do see maturity increasing in open source within financial services, as banks are starting to take the lead on projects rather than tech vendors taking the lead and then inviting the banks in.”[^2] When firms enable and encourage collaboration (a sign of open source maturity), it not only increases their influence but also inspires employees. As Mimi Flynn, software engineer and open source advocate at Morgan Stanley, explains, “Having opportunities to contribute to external projects is still motivating and inspiring. It also reinforces why hands-on coding remains so important.”[^3]

Despite encouraging progress, challenges remain, as 14% of financial institutions and 3% of fintech respondents report that their organizations have not yet taken any of the listed maturity actions. A further 3% of financial institutions and 8% of fintechs are unsure of their firm’s approach. These figures highlight ongoing cultural and organizational barriers, suggesting that while leading firms are advancing quickly, a meaningful segment of the sector has yet to begin its maturity journey in open source.

### From consumption to contribution through policy and practice
Implementing appropriate policies, processes, and tools to manage open source selection, usage, and contribution is foundational for increasing open source maturity and unlocking its value and benefits. However, having to write open source policies for the first time can be a barrier to both using and contributing to open source, especially for new organizations just beginning their journeys. Organizations such as FINOS have made this first step easier. As NatWest open source lead James McLeod reflects, “Because other banks within the FINOS membership have published their open source policies, we’ve been able to learn from their approach.”[^4]

This year’s data on consumption policies (**FIGURE 5**) shows that the industry is more openly encouraging open source consumption than ever before, and only 1% now say that it’s not permitted.

This shows a wider recognition of what those close to open source in the industry have known for years, that every organization is using open source (even if 1% still say it’s not permitted). As Brian Fox, CTO at Sonatype, who has been working in this space for nearly 30 years, explains, “There were cases in the early days where the leadership didn’t understand how much open source was being used. They would tell us they weren’t using open source. What I think they meant was major open source systems like Linux, Open Office, or Firefox, not understanding that open source was being used to actually build their own applications.”[^5]

### FIGURE 5: Policy on OSS use in organizations
![Bar chart showing 55% of organizations openly encourage OSS use, 22% permit it under limited circumstances, 16% have no clear policy, 1% say it is not permitted, and 14% are up to each development team]

### FIGURE 6: Practices around OSS use
![Bar chart showing 46% have a formal review process, 42% have internal manuals/guidelines, and 42% have tooling and automation]

The importance of carefully selecting and managing OSS cannot be overstated. Without visibility, organizations risk exposure to unknown vulnerabilities, untracked dependencies, shadow code, licensing noncompliance, abandoned code, and package hijacking, all of which can lead to security breaches, reputational damage, increased technical debt, and fines.

Managing these risks begins with ensuring you have adequate policies and processes to understand what OSS is in use within your organization. As Dietmar Fauser, chief information officer (CIO) at Symphony, shared, “We keep a close eye on the tendencies of adoption levels to ensure that we are not alone when we use something. And we make conscious choices, not just letting open source sneak in because the developer found it cool to use a library.”[^6] As is the case for many fintechs, OSS is deeply strategic for Symphony, which uses open source or enterprise-supported OSS at the core of what they are doing and at all levels from the front end to deep database technology in the back end. Given how deeply embedded OSS is across the industry, organizations should manage it with the same level of governance and process that they apply to proprietary and licensed software, including understanding and addressing any specific risks.

The industry is waking up to the reality of OSS supply chain risk, but recognition hasn’t yet translated into the systematic actions necessary to close the gap. Matt Barrett, CEO of Adaptive, very succinctly points out, “There’s growing discomfort and awareness that OSS supply chain risks need better management, even for internally hosted systems. But recognizing the risk doesn’t always translate into budget or action. We’re not yet seeing the kind of top-down mandates that drive real change.”[^7]

Our survey results largely support Mr. Barrett’s assertion (**FIGURE 7**). They show that 52% of respondents are concerned about security vulnerabilities, yet only 37% are worried about supply chain attacks. As shown in **FIGURE 8**, fewer than half of the organizations report actively producing (43%), requiring (34%), integrating (30%), attesting to (29%), or consuming (28%) SBOMs. A significant number of individuals indicated that they don’t know whether their organizations are undertaking these practices at all, a gap that further underscores the need for increased resources and focus. The silver lining is that an almost equal number of respondents report that their organizations are beginning to adopt these SBOM processes, indicating that growing awareness is starting to translate into action.

### FIGURE 7: Organizational concerns about open source
![Chart showing 52% concerned about security vulnerabilities and 37% concerned about supply chain attacks]

### FIGURE 8: SBOM adoption levels
![Chart showing adoption levels for producing, requiring, integrating, managing, and consuming SBOMs]

One technology leader at a large asset management firm highlights another value to producing SBOMs: “Having an SBOM is essential for understanding your stack, even if you’re not contributing to open source. You really have to do this. But once you have that visibility, it also helps identify where you should be contributing. If you’re using something like OpenTofu every day, it makes sense to be part of that community. That’s part of the cultural shift: moving from broad, disconnected use to contributing to the tools you rely on most.”[^8]

Contribution policies remain mixed and nuanced in the industry. There is a general, albeit modest, shift toward permitting contribution, with only 2% reporting that they do not permit contribution. However, how and when organizations permit contribution continues to vary significantly from year to year (**FIGURE 9**). Our respondents also report that their organizations allocated more time over the previous year (48%) for them to contribute to open source. This suggests that while firms are beginning to allocate more time for open source work, inconsistent policies and practices still create uncertainty. Until contribution is governed by clearer, more consistent frameworks, participation will remain uneven and fragmented across the industry.

### FIGURE 9: OSS contribution policies from 2022 to 2025
![Line chart showing trends in contribution policies over four years]

One unintended consequence of restrictive contribution policies is the creation of unintentional forks. Forking is a natural part of open source, but when forks are maintained independently without a clear strategy, they drive up costs, increase technical debt, duplicate effort, and introduce security risks. Survey data (**FIGURE 10**) shows that forks occur in multiple forms: intentional, independently maintained forks (where there is a large discrepancy between financial institutions at 46% and fintechs at 34%); unintentional, unmaintained forks; and even cases where multiple teams within the same organization independently maintain internal forks of the same software (20%).

A practical way to reduce fork-related risks while policies and processes mature is to prioritize contributions in the areas most critical to your organization. This requires careful evaluation of open source consumption and alignment with strategic initiatives; maturing policies and processes should go hand in hand with creating opportunities for contribution. This will help organizations avoid unnecessary forks while strengthening the upstream projects they rely on.

Elspeth Minty reinforces this point, naming a specific FINOS project, which captures collective best practices to streamline contribution across financial services. She says, “One of my favorite FINOS projects is git-proxy because it’s a fantastic example of how open source should work. It takes all the accumulated knowledge, best practice, and experience from all these big financial firms, including RBC, and distills it down into this piece of code that we can all use.”[^9]

### FIGURE 10: Forking practices in organizations
![Chart showing various types of internal forks: Maintained (41%), Reactive (31%), Unmaintained (25%), Duplicate (20%), Shadow (19%)]

Policies work best when everyone knows them. Breaking down responses by respondents’ familiarity with open source, we see several discrepancies in the knowledge of policies and processes between those who are very familiar with their organization’s approach to open source and those who are familiar or somewhat familiar (**FIGURE 11**). While not surprising, it is a clear reminder that it is necessary for organizations to ensure that they clearly and continually inform employees about policies, processes, tools, and resources related to open source.

### FIGURE 11: Knowledge discrepancies in OSS policies across familiarity levels
![Chart showing higher awareness of policies among those very familiar with open source compared to those less familiar]

### What are the barriers and challenges holding the sector back?
Open source adoption in financial services has matured, yet firms continue to face significant barriers that limit their ability to fully realize its value. As we’ve discussed, security and compliance remain pressing obstacles, with nearly half of respondents citing concerns over vulnerabilities, supply chain attacks, and regulatory obligations. While tooling such as SBOMs and secure dependency management is gaining traction, the gap between confidence and reality persists.

Confidence in identifying and remediating vulnerable OSS components highlights this disconnect. **FIGURE 12** shows that just over half of respondents (53%) reported being somewhat confident, and only 23% felt extremely confident. Meanwhile, nearly one in five expressed low confidence or uncertainty. These results show that even as security practices expand, many organizations lack the consistent operational maturity to address vulnerabilities at scale. The challenge is compounded by resource constraints, smaller firms in particular report difficulty balancing innovation with the overhead of risk management and compliance.

### FIGURE 12: Confidence in the ability to identify and remediate OSS vulnerabilities
![Chart showing 23% extremely confident, 53% somewhat confident, 16% not very confident, 2% not at all confident, 5% don't know]

Cultural and structural barriers further complicate open source engagement. As shown in **FIGURE 13**, nearly half of respondents agreed that the lack of a clear ROI (48%) and legal or licensing concerns (48%) limit their ability to contribute upstream. Policy gaps, fear of leaking intellectual property (IP), and technology constraints reinforce this hesitancy. Developers also report inconsistent organizational support, with some firms permitting contributions only under restrictive conditions. This not only limits collaboration but also adds technical debt when patches cannot be upstreamed. New governance challenges are emerging as friction points as firms attempt to extend traditional oversight models to cover rapidly evolving technologies.

“The biggest barrier has been the perception that open source is somehow riskier or less professional than proprietary approaches. To overcome that, we’ve focused on education, clear policies, and celebrating early wins. When teams see successful examples in action, it starts to shift the narrative.”
— Mark Paulsen, Head of OSPO, TD Bank[^10]

### FIGURE 13: Barriers to open source contribution
![Chart showing top barriers: Lack of clear ROI (48%), Legal/licensing concerns (48%), Lack of policy/training (43%)]

### FIGURE 14: Roles with the most influence on open source direction
![Chart showing influence levels of CTO (69%), OSPO (63%), Developer (60%), CISO (57%), CIO (55%)]

Finally, leadership and influence play a critical role in shaping open source strategy. **FIGURE 14** shows that respondents identified CTOs (69%), OSPOs or open source–specific roles (63%), and developers (60%) as the most influential stakeholders, followed by CISOs and CIOs. By contrast, external regulators, audit functions, and HR were seen as less impactful. This concentration of influence underscores the importance of executive sponsorship and dedicated OSPO resources in overcoming cultural and compliance hurdles. Without them, progress risks being slowed by fragmented governance and limited budgets. Addressing these barriers, through stronger education, clearer contribution frameworks, and modernized risk oversight, will be essential for enabling financial institutions to fully capture the benefits of open source.

---

## Community as the accelerator to value and impact

### Community drives value
At its core, open source is about collaboration and community. The most successful and valuable open source projects and standards benefit from a diverse, active group of adopters, contributors, and maintainers who provide varied insights, a high degree of scrutiny, and redundancy that increases the longevity and utility of projects. Ultimately, the richer and more engaged the community, the greater the value open source can deliver.

This year’s survey data in **FIGURE 15** reinforces that point. Among financial services organizations, the top motivations for contributing to open source ranged from giving back to the community and attracting talent to influencing the direction of projects and reducing technical debt. A senior technology leader explains how these motivations are connected, “From a talent perspective, open source contribution has become very important. People want to contribute to something bigger than themselves, and they want to work in organizations that support that. When you consider that 90% of your software stack runs on open source, it becomes clear that open source needs to be part of how you run your business and part of your strategy.”[^11]

### FIGURE 15: Top motivations for contributing to open source
![Chart showing top motivations: Give back (33%), Influence direction (29%), Lower risk/debt (28%), Attract/retain talent (27%)]

“You can influence the roadmap at the commit level so you’re not completely downstream of a tech vendor.”[^12]

Eddie Knight, OSPO lead at Sonatype, also explains how community is important for building secure software: “Trust comes from more than secure code; it comes from knowing how to work with the projects you rely on. If enterprises can’t reach maintainers and maintainers can’t show the security work they’ve done, even the best processes won’t translate into confidence.”[^13]

Thriving open source communities rely on dynamic ecosystems of individuals and organizations, each playing vital roles. As we’ve discussed, not all organizations are in a position to contribute code back to the open source projects they use, so communities are also essential for connecting open source consumers with maintainers, offering access to expert support and services, and enabling sustainable commercial models built around OSS.

---

[^1]: Interview with Elspeth Minty, July 9, 2025.
[^2]: Interview with James McLeod, July 29, 2025.
[^3]: Interview with Mimi Flynn, July 7, 2025.
[^4]: Interview with James McLeod, July 29, 2025.
[^5]: Interview with Brian Fox, August 11, 2025.
[^6]: Interview with Dietmar Fauser, June 24, 2025.
[^7]: Interview with Matt Barrett, July 7, 2025.
[^8]: Interview with technology leader, June 26, 2025.
[^9]: Interview with Elspeth Minty, July 9, 2025.
[^10]: Interview with Mark Paulsen, July 1, 2025.
[^11]: Interview with technology leader, June 26, 2025.
[^12]: Interview with technology leader, June 26, 2025.
[^13]: Interview with Eddie Knight, July 15, 2025.

---

erational overhead and benefit from production-
tested reliability. As Dietmar Fauser describes, “We have a
fundamental policy that says if there are managed services
Engaging in open source communities, particularly in areas
available, by a good partner and at an acceptable price, we
where organizations are large consumers of open source, is
go for it. We are not a large firm, so this helps us reduce the
also important. Many individuals we spoke with discussed
number of people we need to operate the platform. You get
the importance of knowing your community and getting
the operational benefits of people doing this at scale, and
involved, as it takes time to build trust, earn a role as a
you get the versions of the open source libraries that are
maintainer, influence the direction of a project, or even simply
typically tested in relatively real production-type setups.”17
to de-risk your reliance on open source components. James
McLeod of NatWest articulates the value of participants
Other financial institutions turn to consultancies or fintechs
influencing the technical direction of projects. He says, “The
that can contribute on their behalf, co-create new projects or
strategic influence of open source projects is definitely
standards, build custom solutions from existing open source
starting to be realized. Even if you can’t reduce the cost, you
code, or provide ongoing support for open source initiatives.
15 Interview with James McLeod, July 29, 2025.
16 Interview with Eddie Knight, August 11, 2025.
17 Interview with Dietmar Fauser, June 24, 2025. THE 2025 STATE OF OPEN SOURCE IN FINANCIAL SERVICES 26

As Matt Barrett of Adaptive explains, “Some firms are looking
for production-ready capabilities with SLAs and support,
essentially a productized form of open source. That’s one
place where commercial value around open source exists.”18 In Their Words: The Value of Community Events
Community events provide numerous benefits to
We are also seeing increasing value from VC-backed COSS, the open source community at all levels of maturity,
as The State of Commercial Open Source 202519 reports, including offering knowledge sharing and education,
drawing on 25 years of venture data from 800 VC-backed building trust and relationships, and providing practical
startups. Taking us back to the value of community, research hands-on experiences.
in the report “demonstrates a direct and strengthening link
between the health of an OSS community and the financial “We use something called ‘jams’ to drive contribution
success (valuation and venture capital funding) of the and community. It’s one way we bring together people
company built around it.” who are all working on the same project, even if they’re
on opposite sides of the organization. It creates a space
Success requires participation at all levels, from all areas, to share what we’re doing, learn from each other, and
and a goal of ensuring that everyone involved can find build connections. It’s not just about the code; it’s about
value. Community participation is not altruistic; it’s core creating those threads that strengthen both our internal
to the competitiveness, resilience, and long-term success community and our influence in the wider open source
of the open source projects and standards. Mark Paulsen ecosystem.”21
summarizes this well: “Long term, I’d love to see open source
woven into the fabric of everything we do, from product “Community events are important for us, for both
development to community engagement. It’s not just about engagement and validation. Developers show up and tell
code. It’s about building trust, transparency, and shared us they’re running Aeron in production, which we might
purpose with our peers and the broader ecosystem.”20 not otherwise know. And when our clients attend and
see the broader ecosystem and activity, it reinforces that
they’re making the right bet. It turns open source into
something real and investable.”22
“Events are extremely valuable. There’s definitely a
strong desire for people to attend them now, as more
and more engineers are allowed to go.”23
18 Interview with Matt Barrett, July 7, 2025.
19 https://www.linuxfoundation.org/research/2025-state-of-commercial-open-source
20 Interview with Mark Paulsen, July 1, 2025.
21 Interview with technology leader, June 26, 2025.
22 Interview with Matt Barrett, July 7, 2025.
23 Interview with James McLeod, July 29, 2025. THE 2025 STATE OF OPEN SOURCE IN FINANCIAL SERVICES 27

Opportunities across the stack Looking first at open source technologies (FIGURE 16), AI
has been in the top three since the inception of our survey
In our survey, we explore where respondents believe open and has ranked in the top spot for the last three years. We
source is most valuable to the industry, approaching this look at AI growth, opportunities, and challenges later in the
from two slightly different angles: asking about specific open report.
source technologies and in which areas collaboration can
deliver the most value.
FIGURE 16
Top open source technologies for the industry
Which open source technologies do you feel are the most valuable to the future of the financial services industry?
50% 52%
49%
49%
Greater familiarity with
45%
open source corresponds
with higher value recognition
for cloud, bringing it close
40% to AI
39%
35%
30%
25%
20%
15%
2023 2024 2025 AI Cloud
Overall Very familiar with their organization's OSS approach
AI Cloud Cybersecurity Advanced Analytics
2023-2025 FINOS SURVEYS, Q36, Q14, Q16, SAMPLE SIZE = 324, 249, 209, TOTAL MENTIONS = 861, 683, 571, FULL DATA IN APPENDIX A7
2025 FINOS SURVEY, Q16 BY Q3, SAMPLE SIZE = 209, TOTAL MENTIONS = 571, FULL DATA IN APPENDIX A8
THE 2025 STATE OF OPEN SOURCE IN FINANCIAL SERVICES 28

Cloud (and associated technologies) has also consistently this fragmentation by providing a unified, cloud-agnostic
ranked in the top three, and respondents who are very control framework. It is backed by major financial institutions,
familiar with their open source policies ranked AI and including Citi, Morgan Stanley, BMO, and LSEG, and foremost
the cloud almost equally (52% and 49%, respectively) cloud providers, such as Microsoft, Google Cloud, and AWS.
(FIGURE 16). The importance of AI and the cloud to the The project recently announced an integration with the
industry is reinforced by the GitHub data presented earlier, open source AI governance framework27 to help ensure that
which shows that the most common keywords in open source emerging AI-related risks and controls are incorporated,
projects with financial services contributors were cloud- giving firms a sustainable way to strengthen security, reduce
related, followed by AI-related. duplication, and scale compliance across both cloud and AI
services.
Accenture’s research report “Top 10 banking trends in 2025
and beyond”24 predicts that “open-source systems—on-prem Turning to specific areas of collaboration, FIGURE 17 shows
and in the cloud—will become the foundation of banking that 51% agree that the industry can derive the greatest
infrastructure, driving innovation, reducing costs, and value from collaboration on industry standards. They are
enhancing security.” The report encourages organizations critically important across the financial services industry, and,
to “adopt a cloud-first mindset. Standardize your operations as Elspeth Minty says, “Standards just make things easier.
to work seamlessly across both on-prem and cloud If we’re all producing data and sending it to each other in a
environments.” consistent way, it just becomes easier for everyone in the
industry to deal with it.”28
Financial institutions often use multiple cloud providers and
environments to address operational resilience, data security,
data residency, and regulatory reporting requirements. The
FIGURE 17
2024 CNCF survey25 confirms this trend across industries,
Greatest value from open source collaboration
with 78% of respondents using multiple cloud service
providers (CSPs). Further, the majority (59%) use a mix of In which areas can the financial services industry derive the greatest
on-prem data centers and public clouds. value from open source collaboration? (select up to three responses)
Industry standards (e.g., trade
For financial institutions, working with multiple CSPs means
lifecycle modeling, cloud controls, 51%
recreating the same security and compliance artifacts again climate risk measures, digital assets)
and again. While different CSPs may offer similar features, AI toolchain: tools,
33%
each has its own proprietary controls and processes. This datasets, frameworks
fragmentation can result in duplicative effort, higher costs,
Regulation and legal
32%
and increased compliance risk. One area where the industry compliance
is working together to tackle this challenge is the open
source Common Cloud Controls project,26 which tackles 2025 FINOS SURVEY, Q17, SAMPLE SIZE = 209, TOTAL MENTIONS = 523, TOP 3
SHOWN, FULL DATA IN APPENDIX A9
24 https://www.accenture.com/us-en/insights/banking/top-10-trends-banking-2025
25 https://www.linuxfoundation.org/hubfs/Research%20Reports/cncf_annual_survey24_031225a.pdf?hsLang=en
26 https://github.com/finos/common-cloud-controls
27 https://github.com/finos/ai-governance-framework
28 Interview with Elspeth Minty, July 9, 2025. THE 2025 STATE OF OPEN SOURCE IN FINANCIAL SERVICES 29

For this reason, the financial services industry has relied on The industry is also recognizing the value of moving to
standards for centuries to improve operations, reduce errors, truly open standards. As Paul Hands, CTO of Parallel 51 and
increase interoperability, and accelerate transactions. In Document Risk Solutions, explains, “CDM becoming open
the 19th century, inventions such as the ticker tape (1867) source made a real difference. It stopped being someone
enabled uniform, democratized reporting of stock prices. else’s model and became something we could work with and
The telex networks of the 1920s and 1930s were the original contribute to. That shift was key to us deciding to invest time
electronic communication method for banking, paving the and effort.”30 Engaging additional community participants
way for SWIFT to create a shared, encrypted network with also expedites expansion into new areas and segments, such
standardized message formats and protocols in the 1970s. as the CDM expanding to tokenized assets and physical risk.
Collaborative efforts continued to build on existing standards
and deliver new ones, including the FIX Protocol (1987) Among the examples of industry standards that respondents
for electronic trading, ISO 20022 (2004) (a modern global cited as a value point in the survey are climate-risk measures.
financial messaging standard), PCI DSS (2004) for secure Managing risk of all kinds is important to financial services
card payments, and XBRL (2000s) for financial reporting. organizations, but climate-risk measures improve fund
managers’ ability to make portfolio management and other
This long tradition of financial standards continues, with types of investment and underwriting decisions in the face of
open standards in financial services advancing in numerous physical and market risk from adverse weather events. The
domains where consistency, interoperability, and shared insurance industry, in particular, has had to face challenges
perspectives deliver real business value. Open source adapting to damages from floods, wildfires, and windstorms.
standards address a range of opportunities, including
financial desktop interoperability (e.g., FDC3 for financial In this context, the “value in standards” opportunity lies in
desktops), data and reporting (e.g., CDM for trade lifecycle improved climate risk modeling to achieve more resilient
management and regulatory processes), and DevOps and financial markets—an equal benefit to all. According to
infrastructure practices that standardize deployment and Steven Tebbe of OS-Climate, “We’re building the neutral,
operational tooling. CALM (the Common Architecture open source infrastructure that allows markets, regulators,
Language Model) is part of this evolution, moving and civil society to engage with climate-related data and
architecture off whiteboards and into code. As Matthew Bain, analytics in a transparent, scalable, and actionable way. We’re
a Distinguished Engineer at Morgan Stanley, explains, “Our the plumbing, the foundation for a better understanding
intent was to make architecture an integral, concrete part of climate-linked financial risk.” He adds, “Acknowledging
of the SDLC, something that drives developer productivity, the reality of physical climate risk is no longer optional—it’s
lowers friction in the development cycle, and reduces risk by a fiduciary imperative. The scale and complexity of these
enabling measurable controls.”29 risks make this project not just important, but essential. No
institution can afford to navigate this landscape alone.”31
29 Email with Matthew Bain, September 8, 2025.
30 Interview with Paul Hands, July 3, 2025.
31 Interview with Steven Tebbe, July 17, 2025. THE 2025 STATE OF OPEN SOURCE IN FINANCIAL SERVICES 30

One-third of respondents also identified regulation and
legal compliance as a top area for collaboration (FIGURE
FIGURE 18
17). While the industry may be recognizing the importance
OSS value to organizations and
of mutualizing regulatory risk, there’s still a long way to go.
the financial services industry
From Elspeth Minty’s perspective, “The work that has been
done with the regulatory industry bodies, including the open
reg tech projects, is fantastic, but it’s still only a small part of
Industry standards (e.g., trade
lifecycle modewlinhga, tc lonuede cdosn ttrool sb, e done.”32 84%
climate risk measures, digital assets)
YAeIt ,t odoelcshpaiint:e t otohlse, re being plenty of work to accomplish as an
agree that open source is valuable to the future of the
datasets, frameworks
industry, there is immediate value to be realized for open financial services industry.
source participants. Organizations no longer have to take
on certain challenges in isolation, nor must they reinvent the
87%
wheel at every turn. As James McLeod of NatWest describes,
“Some of the problems that we’re trying to solve have already
agree that open source is valuable to the future of their
been solved, so we don’t have to start from scratch.”33 organization.
Measuring business value and ROI
2025 FINOS SURVEY, Q14, Q13, SAMPLE SIZE = 209, % OF “AGREE”, FULL DATA IN
APPENDIX A10-A11
As shown in FIGURE 18, respondents continue to affirm
the value of open source for financial services, with 84%
agreeing it benefits the industry overall and 87% recognizing
value within their own organizations. Larger firms see this FIGURE 19 shows the breadth of benefits OSS delivers to the
even more strongly, with over 95% agreeing it benefits respondents’ organizations. They see open source improving
the industry (APPENDIX B3) and 96% agreeing it benefits software quality, delivering business value, lowering costs,
their organization (APPENDIX B4). This widespread speeding up software delivery, and reducing vendor lock-in.
acknowledgement reflects the many ways open source As Elspeth Minty acknowledges, “One of the benefits of
delivers value, some of which we’ve already discussed. These open source is that you’re not necessarily tied into a single
include knowledge sharing, collaboration, collective problem- vendor”34
solving, and the ability to influence technical direction.
32 Interview with Elspeth Minty, July 9, 2025.
33 Interview with James McLeod, July 29, 2025.
34 Interview with Elspeth Minty, July 9, 2025. THE 2025 STATE OF OPEN SOURCE IN FINANCIAL SERVICES 31

FIGURE 19
Benefits of OSS use
How often does using OSS deliver the following benefits in your organization? (select one response per row)
Lower cost of software
| Improved software  |                       |                        | Improved productivity  |
| ------------------ | --------------------- | ---------------------- | ---------------------- |
| 1                  | 2 ownership (license  | 3 Business value (59%) | 4                      |
| quality (63%)      |                       |                        | (58%)                  |
costs) (62%)
Makes the organization
Faster development Less vendor lock-in  Improved collaboration
| 5                    | 6     | 7 a better place to work  | 8     |
| -------------------- | ----- | ------------------------- | ----- |
| time to market (51%) | (50%) |                           | (49%) |
(50%)
| Improved security  | Lower cost of IT  | Facilitates innovation  |     |
| ------------------ | ----------------- | ----------------------- | --- |
| 9                  | 10                | 11                      |     |
| (48%)              | operations (48%)  | (46%)                   |     |
2025 FINOS SURVEY, Q23, SAMPLE SIZE = 202, % OF “OFTEN”, FULL DATA IN APPENDIX A12
Talent is another recurring theme in the ROI of open source.  potential employees: “Open source certainly increases the
Elspeth Minty explains that business value can be derived  organization’s reach within the engineering community, and
from open source through the ease of sourcing expert talent.  this enables us to demonstrate not only who we are but what
According to Minty, “Open source provides an opportunity  values we uphold when it comes to engineering.”37
for us to hire knowledgeable people with transferable skills.
We can more readily source talent by looking at the quality  The industry widely recognizes the benefits that open source
of that individual’s open source contributions but also be  delivers, but quantifying the dollar value of those savings
able to find them from job boards at open source events and  remains challenging. While 18% of survey respondents
then retain them.”35 Mimi Flynn from Morgan Stanley builds  reported saving more than $1,000,000 annually from
on this point: “Leveraging open source makes it so much  using open source (FIGURE 20), nearly one-third were
easier to attract talented engineers who already know the  unsure about their savings, a figure that rises to 45% among
platforms we use. With proprietary software, training takes  larger organizations. Improving visibility into consumption,
longer, and onboarding costs are higher.”36 James McLeod  supported by OSPOs that consolidate insight across teams,
shares the value in publicizing an organization’s culture to  can help close this gap, but the true value of open source
35 Interview with Elspeth Minty, July 9, 2025.
36 Interview with Mimi Flynn, July 7, 2025.
37 Interview with James McLeod, July 29, 2025. THE 2025 STATE OF OPEN SOURCE IN FINANCIAL SERVICES  32

extends far beyond cost savings. As one technology leader Still, quantifying the full business value of open source is
explains, “We’re consuming certain capabilities from the complex and remains a limiting factor in financial services
open source world that we now want to contribute to organizations reaching open source maturity, as we’ve
because they underpin a lot of the software we run internally. previously discussed. Efforts continue in this area, such as
Open source is no longer just a cost-saving mechanism; it’s a the study “The Value of Open Source Software,”39 which
route to innovation and a strategic asset.”38 estimates the annual demand-side (usage) value of open
source globally across all industries at $8.8 trillion. And even
this, according to the authors, underestimates the full value.
FIGURE 20
The growing value of AI
Cost savings from using OSS
In this section, we find that:
What is your organization’s estimated annual cost savings from using
• Adoption has shifted from caution to commitment.
OSS? (select one)
Financial services firms are moving from initial bans of
GenAI to significant investment.
• Returns remain uneven, but optimism is rising. While only
Less than $100,000 5%
a minority of prototypes make it to production, nearly 40%
of survey respondents either already report ROI or expect
to see it within the next year.
$100,000 to $500,000 17% • Open source is becoming a strategic priority. Momentum
is building around open-weight models, with firms
seeking flexibility, reduced vendor lock-in, and greater
customization.
$500,000 to $1 million 29%
• Skills are now the critical barrier. Firms see capability
gaps, not governance, as the biggest challenge to
adoption, highlighting the need for new expertise and
More than $1 million 18%
reskilling strategies to fully unlock the technology’s value.
Growing investment
Don’t know or not sure 32%
GenAI is a relatively new technology that has rapidly
reshaped the technology landscape. Its potential first
became apparent with the release of GPT-3 in 2020, but
2025 FINOS SURVEY, Q15, SAMPLE SIZE = 209 it was the launch of ChatGPT in 2022 that propelled the
38 Interview with technology leader, June 26, 2025.
39 https://www.hbs.edu/faculty/Pages/item.aspx?num=65230 THE 2025 STATE OF OPEN SOURCE IN FINANCIAL SERVICES 33

technology into mainstream adoption. Initial reactions survey respondents have consistently identified AI as the
within financial services were cautious, with many firms even most valuable open source technology for the future of
imposing outright bans on its use amid concerns over data their industry over the past three years, with sentiment
security and compliance.40 strengthening each year (see FIGURE 21). This rising
expectation of value is mirrored in the scale of investment
Over the past two years, however, that caution has given financial services organizations are now making in generative
way to growing optimism and significant investment. Our AI.
Examples span both external partnerships and internal
innovation. NatWest, for instance, has partnered with OpenAI
FIGURE 21
to enhance its Cora chatbot,41 while BBVA was highlighted
Most valuable open source technologies
as a collaborator during the global launch of GPT-5.42 At
the same time, leading institutions are building their own
Which open source technologies do you feel are the most valuable to the
future of the financial services industry? solutions: JPMorgan Chase has developed IndexGPT to
support investment decision-making;43 Goldman Sachs is
rolling out a custom large language model (LLM)-based
50% AI
assistant across its bankers, traders, and asset managers;44
and Citi has deployed similar tools to more than 140,000
Cloud/ employees across eight countries.45 These developments
40%
containerization
illustrate the rapid shift from risk aversion to large-scale
Cybersecurity
adoption, positioning GenAI as a foundational technology
30% within financial services.
Analytics
Databases CI/CD and DevOps
20% Edge computing
Operating
systems
10%
0%
2023 2024 2025
2023-2025 FINOS SURVEYS, Q36, Q14, Q16, SAMPLE SIZE = 324, 249, 209, TOTAL
MENTIONS = 861, 683, 571, FULL DATA IN APPENDIX A7
40 https://www.businessinsider.com/chatgpt-companies-issued-bans-restrictions-openai-ai-amazon-apple-2023-7
41 https://www.reuters.com/technology/natwest-seals-milestone-uk-banking-collaboration-with-openai-2025-03-20/
42 https://www.bbva.com/en/innovation/openai-highlights-its-collaboration-with-bbva-in-the-global-launch-of-gpt-5/
43 https://www.forbes.com/sites/janakirammsv/2024/07/30/jpmorgan-chase-leads-ai-revolution-in-finance-with-launch-of-llm-suite/
44 https://www.reuters.com/business/goldman-sachs-launches-ai-assistant-firmwide-memo-shows-2025-06-23/
45 https://www.reuters.com/technology/artificial-intelligence/citigroup-rolls-out-artificial-intelligence-tools-employees-eight-
countries-2024-12-04/ THE 2025 STATE OF OPEN SOURCE IN FINANCIAL SERVICES 34

Emerging ROI
While investment in GenAI is accelerating, businesses and Our own survey responses, however, suggest a more
independent studies continue to report mixed success optimistic outlook within financial services. FIGURE 22
in realizing returns. Gartner, for example, has found that shows that 18% of respondents already report achieving a
only 41% of GenAI prototypes make it into production,46 measurable ROI, and a further 22% expect to realize ROI
highlighting the challenges of scaling from experimentation within the next year. This indicates that, while industry-wide
to reliable products that deliver a return. This has prompted challenges persist, financial services firms may be positioning
some analysts to describe a growing “GenAI divide”47 where themselves at the forefront of translating GenAI adoption
many organizations demonstrate high levels of adoption but into tangible value.
relatively low levels of actual transformation.
The increasing role of open source
Open source AI has gained significant momentum over
FIGURE 22 the past year, with a wave of high-profile model releases,
Expected date to realize ROI from GenAI advances in AI frameworks, growing industry adoption, and
policy initiatives that support open development.
When do you expect your organization to realize a ROI from generative
AI? (select one)
Several landmark releases have underscored this progress.
Meta launched LLaMA 3, continuing its investment in the
open model ecosystem, while Mistral introduced its 141B
18% 22% 44% 2% 14% parameter model, which it optimized for multilingual natural
language processing, mathematics, and coding tasks.
In a notable shift, even OpenAI released its first open-
weight models in August 2025, an important signal of the
We are already seeing ROI In 2 to 5 years
broader trend toward open source, or at least open-weight,
Within the next year We do not expect to see ROI approaches across the industry.
Don’t know or not sure
The appetite for open source is clear. A recent a16z survey48
found that 46% of business leaders “strongly prefer” open
2025 FINOS SURVEY, Q21, SAMPLE SIZE = 209 source models, with the leading motivations being greater
control, flexibility, and opportunities for customization.
Together, these developments highlight the growing role
of open source in shaping the future AI landscape and its
relevance for financial services firms seeking transparency,
adaptability, and long-term resilience.
46 https://www.gartner.com/en/documents/6587902
47 https://mlq.ai/media/quarterly_decks/v0.1_State_of_AI_in_Business_2025_Report.pdf
48 https://a16z.com/generative-ai-enterprise-2024/ THE 2025 STATE OF OPEN SOURCE IN FINANCIAL SERVICES 35

debated, more comprehensive analyses tend to converge on
“APIs work well for us, but we’re conscious of the risks— an estimated productivity uplift of around 20%. Together,
around cost, long-term viability, and vendor lock-in. We’d these findings point to a future in which GenAI becomes a
pervasive force in reshaping how software development is
like to have open source alternatives ready so we’re not
carried out.
entirely dependent on a single provider.” 49
- Paul Hands, CTO, Parallel 51 and Document Risk Solutions
FIGURE 23
Business impact Areas where GenAI will have the biggest impact
In which area do you think GenAI will have the biggest impact? (select one)
There has been widespread reporting that GenAI will have
its most significant impact, both positive and negative, on
knowledge work. Early studies, such as Goldman Sachs’s
report on the economic impact of GenAI,50 highlighted 2%
computer and mathematical roles among the job categories
most at risk from automation.
23%
Internal developer productivity
Advances in model capability are already reinforcing this
Business process automation
view. On SWE-bench, an evaluation framework that measures 49%
Creating new, or enhancing,
model performance against real-world software engineering
client-facing services
tasks, pass rates have risen dramatically: from around 20% a
Don’t know or not sure
year ago to more than 50% for several leading models today.
26%
This rapid improvement suggests that the influence of GenAI
on software engineering is accelerating.
Our survey respondents echoed this sentiment, with 49%
identifying enhanced developer productivity as the area
where GenAI will have the greatest impact (see FIGURE 23). 2025 FINOS SURVEY, Q19, SAMPLE SIZE = 209
While the true extent of these productivity gains remains
“AI is raising the bar for developer productivity, but it’s not removing humans from the loop—especially in financial services.
The industry still demands rigor and accountability, and that’s not something you can hand over to a machine just yet.” 51
- Ranadip Chatterjee, Solutions Architect—Global Solutions & Industries (FSI), at a technology company
49 Interview with Paul Hands, July 5, 2025.
50 https://www.gspublishing.com/content/research/en/reports/2023/03/27/d64e052b-0f6e-45d7-967b-d7be35fabd16.html
51 Interview with Ranadip Chatterjee, July 14, 2025. The views expressed in this document are personal. THE 2025 STATE OF OPEN SOURCE IN FINANCIAL SERVICES 36

Tackling adoption challenges However, our survey highlights a different picture. The most
frequently cited barrier is not technology itself but a lack of
As discussed earlier, many organizations are struggling skills (see FIGURE 24). This represents a notable shift from
to move GenAI projects into production and generate last year’s survey, where insufficient governance processes
meaningful ROI. Given the nascent nature of the technology, were seen as the main obstacle. Encouragingly, the industry
it would be easy to attribute these challenges purely to issues is beginning to address the issue through community-led
of technical maturity. initiatives, such as the FINOS AI Governance Framework,52
which provides practical guidance on responsible and
compliant adoption.
FIGURE 24
The challenge of skills is multifaceted. Developing and
Barriers to the use of GenAI
deploying AI systems requires expertise in emerging areas
such as prompt engineering and data engineering, alongside
My organization’s use of GenAI is limited by, or we do not use GenAI
due to: (select one response per row) the adoption of new processes capable of handling the
inherent non-determinism of GenAI. This skills gap is not
50%
unique to financial services. A recent McKinsey report53 on
A lack of A lack of the state of AI found that while organizations are actively
governance in-house
process skills hiring across a wide range of AI-related roles, they are also
making significant investments in reskilling their existing
workforce. This dual approach underscores the scale of the
Data and transformation necessary to fully capture the benefits of
40%
legacy tech A lack of
GenAI.
business case
A lack of tech
maturity
A lack of ideas/
30% applications
20%
2024 2025
2024-2025 FINOS SURVEY, Q16, Q18 SAMPLE SIZE = 249, 209, FULL DATA IN
APPENDIX A13
52 https://air-governance-framework.finos.org/
53 https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai THE 2025 STATE OF OPEN SOURCE IN FINANCIAL SERVICES 37

Conclusions and actionable insights
The 2025 data shows that the industry is operationalizing and innovation come from active participation in upstream
open source, capturing hard savings, improving software projects, not passive consumption. Firms must commit to
quality, and building the muscle to collaborate at scale. Yet, sustained involvement in the communities that underpin
value realization remains uneven where governance, security their most critical technologies.
operations, and contribution pathways are under-resourced.
• Support sustainable ecosystems. Commercial models,
funding commitments, and dedicated individual
Financial services institutions are no longer debating the role
contributors are all integral to the long-term health of a
of open source; they are now challenged with embedding
robust open source ecosystem for financial services.
it strategically across the enterprise, ensuring governance,
and aligning contributions with broader business priorities. • Drive and adopt open standards. Organizations should
Organizations should: prioritize engagement in collaborative standards that
reduce duplication, strengthen interoperability, increase
• Invest in cultural and structural enablers. Secure
operational efficiency, and cut costs across shared
leadership sponsorship, establish or empower OSPOs,
domains.
and build internal education programs to normalize
contribution and strengthen trust across communities. • Make the community part of the talent strategy.
Organizations should showcase values through
• Strengthen secure consumption. Adopt and scale
contribution and participation, using open source as
consumption practices that comprehensively manage
a magnet for attracting, retaining, and developing
all open source and increase SBOM practices to improve
engineering talent.
visibility and mitigate supply chain risks.
• Evolve contribution practices. Move beyond ad hoc AI is both the fastest moving and most strategically
permissions toward consistent frameworks that reduce significant open source technology for financial services.
costly forks, ensure contributions flow back upstream, and Adoption has shifted from hesitation to investment,
pave the way for increased collaboration and value. positioning GenAI as a foundational enabler of productivity,
customer experience, and innovation. Yet, challenges remain
Open source community and collaboration are the in scaling prototypes into production-ready systems and
accelerators of value in financial services. Firms that finding individuals with the skill sets that can make this
approach open source as a shared endeavor, balancing happen. Organizations should:
business priorities with community stewardship, will be in the
• Invest in skills at scale. Pair external hiring with structured
best position to capture both near-term efficiency gains and
reskilling programs in areas such as prompt engineering,
long-term strategic advantages. Organizations should:
data engineering, and secure deployment practices.
• Deepen community engagement. Influence, resilience,
THE 2025 STATE OF OPEN SOURCE IN FINANCIAL SERVICES 38

• Prioritize open approaches. Adopt open-weight models Bottom line: Financial services is all-in on open source
that reduce lock-in, increase transparency, and allow firms because it delivers better code, lower costs, stronger
to tailor solutions to their needs. compliance, faster delivery, and improved talent
pipelines. The firms that will pull ahead now are those that
• Adopt responsible governance frameworks. Use
professionalize OSS management, commit to cross-industry
approaches such as the FINOS AI Governance Framework
standards, and treat AI as an open platform with measurable
to balance innovation with compliance and risk
returns.
management.
• Measure impact deliberately. Tie investments in AI to
clear productivity, ROI, and resilience outcomes rather
than experimentation alone.
THE 2025 STATE OF OPEN SOURCE IN FINANCIAL SERVICES 39

Methodology
This research report draws on survey data, industry data, and The data from the 2021, 2022, 2023, and 2024 studies, and
insights culminating from a series of qualitative interviews. this 2025 survey, is openly available on data.world. Like last
We invited senior IT and business leaders fluent in open year, this 2025 survey primarily focused on both end-user
source technologies, communities, and challenges to share organizations and fintech vendors. End-user organizations
their insights. are primarily consumers of IT products and services, whereas
fintech vendors are primarily producers of IT products and
In-depth interviews services. This 2025 survey made comparisons between 2021,
2022, 2023, 2024, and 2025 questions where possible.
We recorded so that transcripts could be produced. Such
transcripts were strictly controlled and used only for
Percentage values in charts may not add up to 100% due to
purposes of this report. If a recording was not permitted,
rounding.
then detailed notes were taken. Questions were also shared
for completion via email. Unless quotes were given explicit
Screening criteria
approval by the named individuals and/or their organizations,
sources were anonymized. The qualified sample size analyzed for the 2025 survey
was 209. This sample size reflects those respondents who
About the survey passed various screening and filtering criteria, including the
following:
From May to July of 2025, FINOS and its research partners
fielded a worldwide survey of qualified individuals within • A respondent had to be employed full-time, part-time or
(or providing services to) the financial services industry on be self-employed.
various questions related to organizational open source
• A respondent had to be employed by or working closely
consumption, contribution, opportunities, and challenges.
with the financial services industry.
The quantitative survey was designed to engage key • A respondent had to be somewhat familiar, very familiar,
stakeholders at the intersection of open source and financial or extremely familiar with their organization’s approach to
institutions, including developers, IT leaders, executive open source.
management, security, legal, compliance, and procurement.
• A respondent had to self-identify as a real person.
This was combined with distillation and benchmarking of
previous work conducted by the Linux Foundation and
The margin of error for this sample size (N = 209) is +/- 5.7%
FINOS. The survey was distributed and promoted across
with 90% confidence.
research partner social media channels, websites, newsletters
and via direct email campaigns. The survey sample also
included qualified responses from a third-party panel
provider.
THE 2025 STATE OF OPEN SOURCE IN FINANCIAL SERVICES 40

Year-over-year comparisons the comparative results. Therefore, when performing year-
over-year comparisons, we excluded DKNS responses and
Comparisons were made between data collected in 2021,
recalculated percentages so that we had a normalized basis
2022, 2023, 2024, and 2025, question and response design
for comparing the remaining percentage values.
permitting. Respondents had to answer nearly all questions
in the survey. However, there were situations when a
Demographics
respondent was unable to answer a question because it
was outside the scope of their role or experience. For this FIGURE 25 presents demographic data from the survey. This
reason, a “Don’t know or not sure” (DKNS) response was was a worldwide study, with 30% of respondents residing
presented to the respondent. The share of DKNS responses in North America, 30% in Europe, and 31% in Asia-Pacific.
in a question influences the percentage values of the We show the company size data (number of employees) in
remaining responses. Generally, we present the percentage the second panel and aggregate it into four categories. We
of respondents who answer DKNS as a valid response to each included all company sizes in the survey sample, but when we
question. used this variable for segmentation, we decided to exclude
organizations with fewer than 250 employees due to data
One exception is when we are performing year-over- reliability concerns. The third panel classifies the organization
year comparisons. Differences in the percentage of DKNS of the respondents and shows that 53% of respondents work
responses between questions year-over-year would skew in financial institutions, and 30% are employed in the fintech /
financial services sector.
FIGURE 25
Selected demographics from the 2025 FINOS State of Open Source in Financial Services Survey
Please select the geographic region in which Please estimate how many employees the organi- What option best describes the organization
you reside. (select one) zation you work for has worldwide. (select one) you work for? (select one)
North America 30% 1 to 249 13% Financial
53%
institution
Europe 30% 250 to 999 33%
Fintech /
Financial 30%
Asia-Pacific 31% 1,000 to 9,999 28% services vendor
Other 8% 10,000 or more 27% Other 17%
2025 FINOS SURVEY, Q6, Q10, Q7, SAMPLE SIZE = 209
THE 2025 STATE OF OPEN SOURCE IN FINANCIAL SERVICES 41

Resources
Reports: • Open Source Consumption Manifesto
• The State of Commercial Open Source 2025 • Releasing Internal Code into a New Open Source Project
• The Top 10 Banking Trends in 2025 and Beyond • Marketing Open Source Code
• The 2025 State of OSPOs and OSS Initiatives • A Beginner’s Guide to Open Source Software
Development (Free Training)
• Open Source as Europe’s Strategic Advantage 2025
• Open Source Program Office 101 (Free Training)
• 2025 Open Source Security and Risk Analysis Report
• Automating Supply Chain Security: SBOMs and
• 2024 State of Open Source in Financial Services Report
Signatures (Free Training)
• 2023 State of Open Source in Financial Services Report
• Developing Secure Software (Free Training)
• 2022 State of Open Source in Financial Services Report
• Introduction to the Common Domain Model
• 2024 State of the Software Supply Chain (Free Training)
• A Deep Dive into Open Source Program Offices: • Introduction to FDC3 (Free Training)
Structure, Roles, Responsibilities, and Challenges
Open Source Project Catalogs
• A Guide to Open Source Software for Procurement
Professionals • FINOS
• Addressing Cybersecurity Challenges in Open Source • Linux Foundation
Software
• Apache Foundation
• The Case for Confidential Computing
• Eclipse Foundation
• GitProxy Case Study
Guides & Training:
• Open Source Body of Knowledge
• Open Source Maturity Model in Financial Services
• Using Open Source Code
THE 2025 STATE OF OPEN SOURCE IN FINANCIAL SERVICES 42

Acknowledgments
This report and the research behind it would not have been possible without the contributions of many individuals. Beginning
with the research team partners, the authors wish to thank the entire FINOS and Linux Foundation teams, including Gabriele
Columbro, Jane Gavronsky, Aaron Griswold, Win Morgan, Kendall Perez, Anna Hermansen, Mia Chaszeyka along with Philip
Holleran at GitHub. Together, this group facilitated various aspects of the research and supported interview outreach.
We would like to thank Adaptive and Symphony for helping to distribute the survey and all our interviewees, whose rich
insights feature prominently throughout this report.
Finally, thanks to all who continue to contribute to open source in the financial services industry.
THE 2025 STATE OF OPEN SOURCE IN FINANCIAL SERVICES 43

Appendix A
| A1: What practices does your  |     | A2: Which open source issues  |     |
| ----------------------------- | --- | ----------------------------- | --- |
organization follow regarding the use  are you most concerned about?
of OSS? (select all that apply) (select up to three responses)
We have a formal review process for  Security vulnerabilities in OSS components 52%
46%
evaluating OSS components
|     |     | Lack of ongoing maintenance or support | 48% |
| --- | --- | -------------------------------------- | --- |
We have internal manuals, checklists,
42%
| or guidelines for using OSS |     | Supply chain attacks | 37% |
| --------------------------- | --- | -------------------- | --- |
We have tooling (e.g., license checkers,  Licensing, IP, or compliance risks 36%
| security scanning) and automation to  | 42% |     |     |
| ------------------------------------- | --- | --- | --- |
implement OSS policies and processes
|     |     | Fragmented or immature ecosystems | 34% |
| --- | --- | --------------------------------- | --- |
We require developer training on
|                             | 36% | “Rug pull” (change from permissive to  |     |
| --------------------------- | --- | -------------------------------------- | --- |
| secure software development |     |                                        | 33% |
restrictive or non-open license)
We recommend developer training
|     | 29% | Other (please specify) | 1%  |
| --- | --- | ---------------------- | --- |
on secure software development
|     |     | Don’t know or not sure | 0%  |
| --- | --- | ---------------------- | --- |
We engage with outside professionals to
| determine what OSS components  | 26% |     |     |
| ------------------------------ | --- | --- | --- |
2025 FINOS SURVEY, Q27, SAMPLE SIZE = 209,
we should use
TOTAL MENTIONS = 505
Our OSPO works with developers to
19%
ensure its policies are followed
| None of the above      | 5%  |     |     |
| ---------------------- | --- | --- | --- |
| Don’t know or not sure | 5%  |     |     |
2025 FINOS SURVEY, Q24, SAMPLE SIZE = 202,
TOTAL MENTIONS = 504
THE 2025 STATE OF OPEN SOURCE IN FINANCIAL SERVICES  44

| A3: To what extent is the use  |           |     | A4: What practices does your   |           |     |
| ------------------------------ | --------- | --- | ------------------------------ | --------- | --- |
| of OSS permitted in your       |           |     | organization follow regarding  |           |     |
| organization?                  |           |     | the use of OSS? (select all    |           |     |
|                                | Somewhat  |     |                                | Somewhat  |     |
(select one)— segmented by  Very  that apply)— segmented by  Very
|     | familiar  |     |     | familiar  |     |
| --- | --------- | --- | --- | --------- | --- |
the following question: What  familiar the following question: What  familiar
|                                    | + Familiar |     |                                    | + Familiar |     |
| ---------------------------------- | ---------- | --- | ---------------------------------- | ---------- | --- |
| is your level of familiarity with  |            |     | is your level of familiarity with  |            |     |
| your organization’s approach       |            |     | your organization’s approach       |            |     |
| to open source? (select one)       |            |     | to open source? (select one)       |            |     |
| Not permitted                      | 2%         | 1%  | We have a formal review            |            |     |
|                                    |            |     | process for evaluating             | 48%        | 44% |
OSS components
Permitted under limited
|     | 28% | 18% |     |     |     |
| --- | --- | --- | --- | --- | --- |
circumstances
We have internal manuals,
| Openly encouraged | 37% | 65% | checklists, or guidelines  | 31% | 49% |
| ----------------- | --- | --- | -------------------------- | --- | --- |
for using OSS
Use is up to each
|                  | 26% | 15% |                                 |     |     |
| ---------------- | --- | --- | ------------------------------- | --- | --- |
| development team |     |     | We have tooling (e.g., license  |     |     |
checkers, security scanning)
|     |     |     |     | 25% | 52% |
| --- | --- | --- | --- | --- | --- |
and automation to implement
| No clear policy | 4%  | 1%  |     |     |     |
| --------------- | --- | --- | --- | --- | --- |
OSS policies and processes
| Don’t know or not sure | 4%  | 1%  |     |     |     |
| ---------------------- | --- | --- | --- | --- | --- |
We require developer training
|     |     |     |     | 30% | 39% |
| --- | --- | --- | --- | --- | --- |
on secure software development
2025 FINOS SURVEY, Q22 BY Q3, SAMPLE SIZE = 209
We recommend developer
|     |     |     | training on secure  | 30% | 28% |
| --- | --- | --- | ------------------- | --- | --- |
software development
We engage with outside
professionals to determine
|     |     |     |     | 26% | 26% |
| --- | --- | --- | --- | --- | --- |
what OSS components
we should use
Our OSPO works with
|     |     |     | developers to ensure its  | 9%  | 26% |
| --- | --- | --- | ------------------------- | --- | --- |
policies are followed
|     |     |     | None of the above      | 1%  | 8%  |
| --- | --- | --- | ---------------------- | --- | --- |
|     |     |     | Don’t know or not sure | 12% | 2%  |
2025 FINOS SURVEY, Q24 BY Q3, SAMPLE SIZE = 202,
TOTAL MENTIONS = 504
THE 2025 STATE OF OPEN SOURCE IN FINANCIAL SERVICES  45

A5: What statement is closest to your organization’s policy on
contributing to open source projects? (select one)— segmented  Somewhat familiar
Very familiar
| by the following question: What is your level of familiarity with  |     | + Familiar |     |     |
| ------------------------------------------------------------------ | --- | ---------- | --- | --- |
your organization’s approach to open source? (select one)
| Not permitted                                    |     | 2%  |     | 2%  |
| ------------------------------------------------ | --- | --- | --- | --- |
| No clear policy                                  |     | 17% |     | 6%  |
| Permitted under some conditions                  |     | 40% |     | 20% |
| Up to each development team                      |     | 20% |     | 28% |
| Permitted if required by the open source license |     | 6%  |     | 17% |
| Openly encouraged                                |     | 7%  |     | 25% |
| Don’t know or not sure                           |     | 7%  |     | 1%  |
2025 FINOS SURVEY, Q29 BY Q3, SAMPLE SIZE = 209
Don’t
A6: I feel that my organization’s willingness to contribute to
|     | Agree | Neutral | Disagree | know or  |
| --- | ----- | ------- | -------- | -------- |
open source is limited by: (select one response per row)
not sure
Technology constraints and challenges to upstream OS contributions 34% 37% 18% 10%
| A fear of leaking IP                   | 41% | 29% | 17% | 13% |
| -------------------------------------- | --- | --- | --- | --- |
| A lack of policy or training materials | 43% | 27% | 20% | 11% |
| Legal or licensing concerns            | 48% | 24% | 16% | 11% |
| A lack of clear ROI                    | 48% | 24% | 19% | 8%  |
2025 FINOS SURVEY, Q33, SAMPLE SIZE = 202
THE 2025 STATE OF OPEN SOURCE IN FINANCIAL SERVICES  46

A7: Which open source technologies do you feel are the most valuable to the
|     | 2025 | 2024 | 2023 |
| --- | ---- | ---- | ---- |
future of the financial services industry? (select up to three responses)
| Advanced analytics and data science        | 23% | 24% | 27% |
| ------------------------------------------ | --- | --- | --- |
| Artificial intelligence / Machine learning | 49% | 45% | 35% |
Augmented / virtual reality, 3D simulation, graphics
|                | 15% | 19% | 10% |
| -------------- | --- | --- | --- |
| Blockchain     | 19% | 16% | 12% |
| CI/CD & DevOps | 21% | 20% | 15% |
Cloud / container technologies (including Kubernetes) 39% 29% 34%
Cybersecurity
|                              | 20% | 32% | 35% |
| ---------------------------- | --- | --- | --- |
| Database and data management | 12% | 21% | 23% |
| DevOps / GitOps / DevSecOps  | 14% | 13% | 14% |
| Edge computing               | 5%  | 9%  | 5%  |
Industry standards
|                                              | 10% | 8%  | 8%  |
| -------------------------------------------- | --- | --- | --- |
| IoT & Embedded                               | 0%  | 4%  | 4%  |
| Networking technologies (5G, SDN, NFV, etc.) | 2%  | 4%  | 8%  |
| Open data / open models                      | 12% | 8%  | 0%  |
Open hardware
|                                 | 2%  | 2%  | 2%  |
| ------------------------------- | --- | --- | --- |
| Operating systems (e.g., Linux) | 16% | 9%  | 5%  |
| Storage technologies            | 2%  | 4%  | 4%  |
| Web & application development   | 11% | 6%  | 13% |
2023-2025 FINOS SURVEYS, Q36, Q14, Q16, SAMPLE SIZE = 324, 249, 209, TOTAL MENTIONS = 861, 683, 571
THE 2025 STATE OF OPEN SOURCE IN FINANCIAL SERVICES  47

A8: Which open source technologies do you feel are the most valuable to
Somewhat
the future of the financial services industry? (select up to three responses)— Very
|     | Total | familiar  |     |
| --- | ----- | --------- | --- |
segmented by the following question: What is your level of familiarity  familiar
+ Familiar
with your organization’s approach to open source? (select one)
| Artificial intelligence / Machine learning | 49% | 44% | 52% |
| ------------------------------------------ | --- | --- | --- |
Cloud / container technologies (including Kubernetes) 39% 24% 49%
| Advanced analytics and data science | 23% | 26% | 21% |
| ----------------------------------- | --- | --- | --- |
| CI/CD & DevOps                      | 21% | 30% | 15% |
| Cybersecurity                       | 20% | 20% | 20% |
| Blockchain                          | 19% | 26% | 15% |
| Operating systems (e.g., Linux)     | 16% | 13% | 17% |
Augmented / virtual reality, 3D simulation, graphics 15% 16% 15%
| DevOps / GitOps / DevSecOps                  | 14% | 11% | 16% |
| -------------------------------------------- | --- | --- | --- |
| Database and data management                 | 12% | 11% | 13% |
| Open data / open models                      | 12% | 11% | 13% |
| Web & application development                | 11% | 16% | 7%  |
| Industry standards                           | 10% | 9%  | 10% |
| Edge computing                               | 5%  | 1%  | 8%  |
| Networking technologies (5G, SDN, NFV, etc.) | 2%  | 4%  | 2%  |
| Open hardware                                | 2%  | 1%  | 3%  |
| Storage technologies                         | 2%  | 1%  | 2%  |
| IoT & Embedded                               | 0%  | 0%  | 1%  |
THE 2025 STATE OF OPEN SOURCE IN FINANCIAL SERVICES  48

A8: Which open source technologies do you feel are the most valuable to
Somewhat
the future of the financial services industry? (select up to three responses)— Very
|     | Total | familiar  |     |
| --- | ----- | --------- | --- |
segmented by the following question: What is your level of familiarity  familiar
+ Familiar
with your organization’s approach to open source? (select one)
| Other (please specify) | 0%  | 0%  | 1%  |
| ---------------------- | --- | --- | --- |
| Don't know or not sure | 0%  | 0%  | 0%  |
2025 FINOS SURVEY, Q16 BY Q3, SAMPLE SIZE = 209, TOTAL MENTIONS = 571
A9: In which areas can the financial services industry derive the greatest value
from open source collaboration? (select up to three responses)
Industry standards (e.g., trade lifecycle modeling, cloud controls, climate risk measures, digital assets) 51%
| AI toolchain: tools, datasets, frameworks |     |     | 33% |
| ----------------------------------------- | --- | --- | --- |
| Regulation and legal compliance           |     |     | 32% |
| LLMs (for finance)                        |     |     | 29% |
| Open data / data sharing                  |     |     | 29% |
| Precompetitive AI / ML models             |     |     | 26% |
| Core banking (operations) platform        |     |     | 25% |
| Digital identity                          |     |     | 22% |
| Other (please specify)                    |     |     | 0%  |
| Don’t know or not sure                    |     |     | 3%  |
2025 FINOS SURVEY, Q17, SAMPLE SIZE = 209, TOTAL MENTIONS = 523
THE 2025 STATE OF OPEN SOURCE IN FINANCIAL SERVICES  49

A10: Do you agree or disagree that open  A11: Do you agree or disagree that
source is valuable to the future of the  open source is valuable to the future
financial services industry? (select one)  of your organization? (select one)
| Agree                  | 84% | Agree                  |     |     | 87% |
| ---------------------- | --- | ---------------------- | --- | --- | --- |
| Neutral                | 15% | Neutral                |     |     | 11% |
| Disagree               | 0%  | Disagree               |     |     | 0%  |
| Don’t know or not sure | 1%  | Don’t know or not sure |     |     | 1%  |
2025 FINOS SURVEY, Q14, SAMPLE SIZE = 209 2025 FINOS SURVEY, Q13, SAMPLE SIZE = 209
Don’t
A12: How often does using OSS deliver the following benefits
|     |     | Often | Sometimes | Rarely | know or  |
| --- | --- | ----- | --------- | ------ | -------- |
in your organization? (select one response per row)
not sure
Facilitates innovation
|                             |     | 46% | 38% | 5%  | 10% |
| --------------------------- | --- | --- | --- | --- | --- |
| Improved security           |     | 48% | 32% | 9%  | 11% |
| Lower cost of IT operations |     | 48% | 35% | 6%  | 11% |
| Improved collaboration      |     | 49% | 36% | 6%  | 8%  |
Less vendor lock-in
|                                               |     | 50% | 37% | 5%  | 7%  |
| --------------------------------------------- | --- | --- | --- | --- | --- |
| Makes the organization a better place to work |     | 50% | 36% | 3%  | 10% |
| Faster development time to market             |     | 51% | 37% | 3%  | 8%  |
| Improved productivity                         |     | 58% | 30% | 3%  | 8%  |
Business value
|     |     | 59% | 30% | 3%  | 7%  |
| --- | --- | --- | --- | --- | --- |
Lower cost of software ownership (license costs) 62% 25% 6% 7%
| Improved software quality |     | 63% | 30% | 1%  | 6%  |
| ------------------------- | --- | --- | --- | --- | --- |
2025 FINOS SURVEY, Q23, SAMPLE SIZE = 202
THE 2025 STATE OF OPEN SOURCE IN FINANCIAL SERVICES  50

A13: My organization’s use of generative AI (GenAI) is limited by,
|     | 2025 | 2024 |
| --- | ---- | ---- |
or we do not use GenAI due to:
| A lack of suitable internal governance processes | 43% | 45% |
| ------------------------------------------------ | --- | --- |
The immaturity of this technology
|                                  | 34% | 36% |
| -------------------------------- | --- | --- |
| A lack of in-house skills        | 46% | 39% |
| Data and / or legacy technology  | 39% | 40% |
| A lack of ideas and applications | 32% | 33% |
A lack of business case and clear ROI
|                                   | 39% | 39% |
| --------------------------------- | --- | --- |
| A lack of leadership or ownership | 32% | 33% |
2024-2025 FINOS SURVEY, Q16, Q18 SAMPLE SIZE = 249, 209
Appendix B
B1: Over the last year, the time your organization has allocated for
you to contribute to open source has: (select one)
| Decreased              |     | 4%  |
| ---------------------- | --- | --- |
| Stayed the same        |     | 37% |
| Increased              |     | 48% |
| Don’t know or not sure |     | 12% |
2025 FINOS SURVEY, Q30, SAMPLE SIZE = 197
THE 2025 STATE OF OPEN SOURCE IN FINANCIAL SERVICES  51

B2: Which of the following practices occur in your organization if OSS is modified to
|     |     | Financial  | Fintech  |
| --- | --- | ---------- | -------- |
meet internal needs? (select all that apply)— segmented by the following question:
|     |     | institution | or other |
| --- | --- | ----------- | -------- |
What option best describes the organization you work for? (select one)
Maintained fork – Intentionally created and actively maintained
|     |     | 46% | 34% |
| --- | --- | --- | --- |
version separate from the upstream project
Unmaintained fork – Intentionally created but no longer maintained or updated 25% 24%
Reactive fork – Initially created unintentionally (e.g., due to immediate
|     |     | 30% | 32% |
| --- | --- | --- | --- |
needs or constraints) but later identified and maintained internally
Duplicate forks across teams – The same open source project is
|     |     | 20% | 19% |
| --- | --- | --- | --- |
maintained separately by multiple internal teams
Shadow fork – Introduced without approval or tracking (e.g., directly copied into a codebase) 19% 19%
No internal forks – OSS is not modified, or modifications are contributed back to the project 17% 16%
| Don’t know or not sure |     | 11% | 21% |
| ---------------------- | --- | --- | --- |
2025 FINOS SURVEY, Q28 BY Q7, SAMPLE SIZE = 202, TOTAL MENTIONS = 337
B3: Do you agree or disagree that open source is valuable to the future of the
|     | 250 to  | 1,000 to  | 10,000  |
| --- | ------- | --------- | ------- |
financial services industry? (select one)— segmented by Please estimate how
|     | 999 | 9,999 | or more |
| --- | --- | ----- | ------- |
many employees the organization you work for has worldwide. (select one)
| Disagree               | 0%  | 0%  | 0%  |
| ---------------------- | --- | --- | --- |
| Neutral                | 16% | 24% | 5%  |
| Agree                  | 82% | 74% | 95% |
| Don’t know or not sure | 1%  | 2%  | 0%  |
2025 FINOS SURVEY, Q14 BY Q10, SAMPLE SIZE = 182
THE 2025 STATE OF OPEN SOURCE IN FINANCIAL SERVICES  52

B4: Do you agree or disagree that open source is valuable to the future of your
|     |     |     | 250 to  | 1,000 to  | 10,000  |
| --- | --- | --- | ------- | --------- | ------- |
organization? (select one)— segmented by the following: Please estimate how
|     |     |     | 999 | 9,999 | or more |
| --- | --- | --- | --- | ----- | ------- |
many employees the organization you work for has worldwide. (select one)
| Disagree               |     |     | 1%  | 0%  | 0%  |
| ---------------------- | --- | --- | --- | --- | --- |
| Neutral                |     |     | 10% | 14% | 4%  |
| Agree                  |     |     | 87% | 83% | 96% |
| Don’t know or not sure |     |     | 1%  | 3%  | 0%  |
2025 FINOS SURVEY, Q13 BY Q10, SAMPLE SIZE = 182
B5: Which of the following actions has your  B6: In which areas do you believe
open source will have the greatest
organization engaged in regarding OSS?
(select all that apply)— filtered for large  impact on AI development and
(>10k employees) financial institutions adoption? (select all that apply)
Standards (e.g. model cards,
Implemented an OSPO or similar
|                        | 64% |                          |     |     | 56% |
| ---------------------- | --- | ------------------------ | --- | --- | --- |
| open source initiative |     | a definition of open AI) |     |     |     |
Defined a clear and visible  Open source and free-to-use models 54%
62%
open source strategy
|                                          |     | Frameworks and libraries (e.g. agent toolkits) |     |     | 52% |
| ---------------------------------------- | --- | ---------------------------------------------- | --- | --- | --- |
| Defined a public position on open source | 44% |                                                |     |     |     |
Test frameworks (e.g. prompt
45%
| Joined or associated with open  |     | engineering, systems testing) |     |     |     |
| ------------------------------- | --- | ----------------------------- | --- | --- | --- |
67%
source organizations
Governance frameworks (e.g.
32%
| Funded open source (via foundation  |     | risk catalogues, controls) |     |     |     |
| ----------------------------------- | --- | -------------------------- | --- | --- | --- |
membership, sponsorship of
56%
individual developers, donations,
|     |     | Other (please specify) |     |     | 1%  |
| --- | --- | ---------------------- | --- | --- | --- |
FOSS Contributor Funds, etc.)
Don't know or not sure
2%
| None of the above | 15% |     |     |     |     |
| ----------------- | --- | --- | --- | --- | --- |
2025 FINOS SURVEY, Q20, SAMPLE SIZE = 209,
| Don’t know or not sure | 3%  | TOTAL MENTIONS = 508 |     |     |     |
| ---------------------- | --- | -------------------- | --- | --- | --- |
2025 FINOS SURVEY, Q11, SAMPLE SIZE = 39, TOTAL MENTIONS = 121
THE 2025 STATE OF OPEN SOURCE IN FINANCIAL SERVICES  53

B7: What is your organization’s estimated annual cost savings from using OSS?
(select one) —filtered for large organizations (>10k employees)
Less than $100,000 2%
$100,000 to $500,000 4%
$500,000 to $1 million 13%
More than $1 million 38%
Don’t know or not sure 45%
2025 FINOS SURVEY, Q15 BY Q10, SAMPLE SIZE = 56
THE 2025 STATE OF OPEN SOURCE IN FINANCIAL SERVICES 54

At Scott Logic, we love difficult. Our 450 U.K.-based consultants collaborate
The Fintech Open Source Foundation (FINOS) is a nonprofit whose mission is with some of the world’s biggest enterprises, providing a pragmatic approach
to foster the adoption of open source software, standards, and collaborative to software development and delivering measurable value through insightful
development practices in financial services. As part of the Linux Foundation, technology advice. Our mission is to help our clients envision, design, build,
FINOS provides a regulatory-compliant platform for developers from and run the software applications that meet their needs and deliver the unique
competing organizations to collaborate on innovative projects that transform services their customers demand.
business operations. With over 100 members spanning major financial
institutions, fintechs, and technology consultancies, FINOS is at the forefront
of driving open source innovation in finance.
GitHub is the world’s most widely adopted Copilot-powered developer platform
to build, scale, and deliver secure software. Over 150 million developers,
including more than 90% of the Fortune 100 companies, use GitHub to
collaborate and more than 77,000 organizations have adopted GitHub Copilot.
Founded in 2021, Linux Foundation Research explores the growing scale
of open source collaboration, providing insight into emerging technology
trends, best practices, and the global impact of open source projects.
Through leveraging project databases and networks, and a commitment
to best practices in quantitative and qualitative methodologies, Linux
twitter.com/finosfoundation
Foundation Research is creating the go-to library for open source insights
for the benefit of organizations the world over. www.linkedin.com/company/finosfoundation
www.youtube.com/c/FINOS
github.com/finos
Copyright © 2025 FINOS
This report is licensed under the Creative Commons
Attribution-NoDerivatives 4.0 International Public License.
To reference this work, please cite as follows: Hilary Carter, Tosha Ellison, Colin
Eberhardt, Brittany Istenes, and Adrienn Lawson, “The 2025 State of Open Source in
Financial Services,” foreword by Michael Abbott, The Linux Foundation, October 2025.