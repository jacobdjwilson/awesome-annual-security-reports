# Insights and Trends in Software Security Testing from Black Duck Global State of DevSecOps 2024

[blackduck.com](blackduck.com)

## Table of Contents
- [Executive Summary](#executive-summary)
- [About Black Duck](#about-black-duck)
- [Findings Overview](#findings-overview)
    - [AI-assisted development soars but securing AI-generated code lags far behind](#ai-assisted-development-soars-but-securing-ai-generated-code-lags-far-behind)
    - [Parallels between securing AI-generated code and securing open source](#parallels-between-securing-ai-generated-code-and-securing-open-source)
    - [An increased focus on software security testing](#an-increased-focus-on-software-security-testing)
    - [Too much noise, too many tools](#too-much-noise-too-many-tools)
    - [Looking ahead](#looking-ahead)
- [A Deep Dive into the State of DevSecOps in 2024](#a-deep-dive-into-the-state-of-devsecops-in-2024)
    - [Three priorities are driving security testing](#three-priorities-are-driving-security-testing)
        - [Protecting sensitive information](#protecting-sensitive-information)
        - [Adhering to best practices](#adhering-to-best-practices)
        - [Automating and ensuring ease of test configuration](#automating-and-ensuring-ease-of-test-configuration)
    - [Trending toward centralization](#trending-toward-centralization)
    - [A struggle to attain full security coverage](#a-struggle-to-attain-full-security-coverage)
    - [Who determines when security tests are run](#who-determines-when-security-tests-are-run)
    - [A tool proliferation challenge](#a-tool-proliferation-challenge)
    - [The noise factor](#the-noise-factor)
    - [Role-based differences](#role-based-differences)
    - [The AI revolution in security testing](#the-ai-revolution-in-security-testing)
    - [Worldwide AI adoption](#worldwide-ai-adoption)
    - [Most respondents not confident they’re securing AI-generated code](#most-respondents-not-confident-theyre-securing-ai-generated-code)
    - [Interpreting and acting on security test results](#interpreting-and-acting-on-security-test-results)
        - [Role-based differences](#role-based-differences-1)
        - [Geographical differences](#geographical-differences)
        - [Different approaches to parsing and cleansing results](#different-approaches-to-parsing-and-cleansing-results)
- [From interpretation to action](#from-interpretation-to-action)
    - [Constant security testing vs. development speed tension](#constant-security-testing-vs-development-speed-tension)
    - [Role-based differences](#role-based-differences-2)
    - [How remediation is accomplished](#how-remediation-is-accomplished)
    - [Prioritizing issues for remediation](#prioritizing-issues-for-remediation)
    - [What happens when security issues are discovered](#what-happens-when-security-issues-are-discovered)
    - [How developers are informed of issues](#how-developers-are-informed-of-issues)
- [Conclusion](#conclusion)
- [Appendix](#appendix)

---

## Executive Summary

It is a time of radical change in software development, with organizations in every industry recognizing the need for robust, efficient security processes that can keep pace with new development practices, such as AI-assisted coding.

The findings in the “Global State of DevSecOps 2024” report are based on a comprehensive survey that Black Duck® commissioned from Censuswide, an international market research consultancy. More than 1,000 software developers, application security (AppSec) professionals, CISOs, and DevOps engineers across multiple countries and industries were included in the survey.

This report provides critical insights into the current state of DevSecOps practices and AppSec testing. It delivers a comprehensive analysis of trends, challenges, and opportunities, and it offers actionable insights for organizations seeking to enhance their DevSecOps practices.

## About Black Duck

Formerly the Synopsys Software Integrity Group, Black Duck offers the most comprehensive, powerful, and trusted portfolio of AppSec solutions in the industry. We have an unmatched track record of helping organizations secure their software quickly, integrate security efficiently in their development environments, and safely innovate with new technologies.

[blackduck.com](blackduck.com) | 2

## Findings Overview

### AI-assisted development soars but securing AI-generated code lags far behind

One of the most striking discoveries in this report is that the AI revolution is already over—and AI won, at least when it comes to integrating AI into software development processes. The adoption of AI in software development has gone beyond a tipping point, with over 90% of the respondents to our survey using AI assistance in some capacity.

### Parallels between securing AI-generated code and securing open source

The rapid adoption of AI-assisted coding by software development teams shares several similarities with the historic rise of open source software use. Both movements disrupted traditional software development practices. Open source challenged proprietary software models, and AI-assisted coding is transforming how code is written and reviewed.

But just as with open source use, bringing AI-assisted coding tools into software development presents unique intellectual property (IP), licensing, and security challenges that need careful management by development teams. For example, both unmanaged open source and AI-generated code can create ambiguity about IP ownership and licensing—especially when the AI model uses datasets that might include open source or other third-party code without attribution.

AI-assisted coding tools also have the potential to introduce security vulnerabilities into codebases. One researcher flatly concludes that “autogenerated code cannot be blindly trusted, and still requires a security review to avoid introducing software vulnerabilities.”

There are clear challenges in managing and securing AI-generated code. Our survey found that organizations are at different stages of implementing policies and controls around AI tool usage, reflecting the nascent nature of this trend.

> Although 85% of respondents to our survey say they have some measures in place to address the challenges posed by AI-generated code, less than a quarter were very confident in their policies and processes for testing such code.

Here is the breakdown.

*   24% VERY CONFIDENT
*   20% SLIGHTLY CONFIDENT
*   41% MODERATELY CONFIDENT
*   6% NOT AT ALL CONFIDENT

### An increased focus on software security testing

Test coverage is substantial but not universal, with 57% of respondents testing between 41% to 80% of their projects, branches, and repositories, suggesting opportunities for expanding security test coverage.

Our findings show that organizations are prioritizing security testing based on the sensitivity of information handled (37% of respondents), while also emphasizing industry best practices (36%) and increasing use of automated security testing (35%).

Configuration of security tests is becoming more centralized, with 55% of respondents using centralized interfaces for test configuration. And although their execution is becoming more automated, the persistence of nonautomated activities documented in this report indicates substantial room for improvement. A significant percentage of respondents still uses manual processes in their application security testing and remediation workflows. The exact amount varies depending on which manual process we look at, but it ranges from about 15% to 43% of respondents.

[blackduck.com](blackduck.com) | 3

### Too much noise, too many tools

A slight majority of respondents find security test results at least “somewhat easy” (52%) to understand and act upon, while another 20% deem their results “extremely easy” to understand. However, this perception varies across roles, industries, and geographies.

The findings also reveal a critical challenge with “noise” in security testing results; that is, output that is considered irrelevant or not worth acting upon. Noise is often caused by a high number of false positives or a large volume of duplicative true positives in results. Sixty percent of respondents reported that they consider over 20% of their results as noise, impacting efficiency and decision-making processes.

Despite a broader trend of integrating security into development processes, 61% of respondents report that security testing moderately or severely slows down development. The tension between security and development speed remains a critical challenge for every industry.

The fact that 82% of organizations use between 6 and 20 security testing tools is certainly a factor, with a broad proliferation of tools contributing to the high levels of noise reported by respondents. Multiple tools may detect the same issues, leading to duplicative results. Or different tools may provide conflicting results for the same code or application. Each tool may generate its own false positives, which compounds as more tools are used.

With so many tools in use, organizations are struggling to effectively integrate and correlate results across platforms and pipelines, leading to difficulty distinguishing between genuine issues and false positives, as well as challenges in prioritizing issues across different tools’ outputs.

### Looking ahead

Several key trends are shaping the path of DevSecOps.

*   Increased automation of security testing and remediation processes
*   A need for policies concerning the use of AI-assisted development tools
*   Enhanced focus on reducing noise in security test results to improve efficiency
*   The evolution of cross-functional collaboration in security decision-making

Organizations have significant opportunities to improve their DevSecOps practices by leveraging automation, enhancing the clarity of security test results, developing robust policies for AI-assisted development, and fostering better cross-functional collaboration.

As the landscape continues to evolve, organizations must stay agile, adapting their AppSec processes to meet emerging challenges. The most successful will be those that can effectively balance rigorous security practices with the speed and innovation demands of modern software development.

[blackduck.com](blackduck.com) | 4

## A Deep Dive into the State of DevSecOps in 2024

Our survey of over 1,000 security professionals reveals a state of flux, with organizations striving to balance security measures with the demands of rapid development cycles. This section delves into the current state of AppSec testing and highlights key trends, challenges, and opportunities that define the testing landscape in 2024.

**Q1.** Which of the following criteria does your organization consider when determining which application security tests to run and when they are run?

*   Sensitivity of information accessed/transmitted by the application 37%
*   General best practices recommended by third-party organizations (e.g., OWASP) 36%
*   Ease-of-configuration or automation of the security tests 35%

### Three priorities are driving security testing

Our results reveal that respondents to our survey have a clear set of priorities for effective security testing. Protecting sensitive information is a key mandate for security teams. Development teams value efficiency through automation and closed feedback loops, and implementing best practices for resilient pipelines is fundamental to operations teams.

#### Protecting sensitive information

The foremost consideration, cited by 37% of respondents, is protecting the sensitive information accessed or transmitted by the application. Taking a risk-based approach as these organizations are doing reflects a mature understanding of the impact potential breaches can have across different parts of an application ecosystem.

In a recent analysis of 1,300 customer applications, Black Duck found sensitive data exposure issues affecting 86% of those customers, accounting for over 30,000 vulnerabilities, including 4,800 critical-risk instances. Sensitive data exposure is one of the most common and serious security issues across industries. To address these vulnerabilities, organizations need to implement strong encryption practices, use up-to-date security protocols, and ensure that sensitive data is properly protected both when it’s being transmitted and when it’s stored.

Our data shows that organizations in sectors such as Application/ Software, Banking/Finance, Healthcare, and Government are particularly attuned to this priority, given the highly sensitive nature of the data they handle.

#### Adhering to best practices

Thirty-six percent of organizations rely on the best practices recommended by third-party organizations like OWASP. Adherence to established guidelines ensures a baseline of security across diverse development environments. However, it also raises questions about the adaptability of these standards in the face of rapidly evolving threats.

> Industry standards may have difficulty adapting in the face of rapidly evolving threats. For example, OWASP standards have yet to address the unique security challenges posed by AI-generated code.

[blackduck.com](blackduck.com) | 5

#### Automating and ensuring ease of test configuration

The emphasis on automation and ease of test configuration, prioritized by 35% of respondents, underscores the growing integration of security into DevOps processes. This move toward DevSecOps reflects the recognition that security must be woven into the fabric of the development life cycle rather than treating it as an afterthought.

### Trending toward centralization

**Q2.** Which statement best describes your process of configuring and running application security tests across your SDLC or CI pipeline?

*   Testing tools provided by the same vendor are configured using a centralized interface and automatically run with policies 30%
*   All tests are configured using a centralized interface and automatically run with policies 26%

The top responses to the survey’s Question 2 reveal a clear trend toward centralization in tool configuration for efficiency and consistency. Thirty percent of respondents reported using a vendor’s interface to configure tests from that vendor, while 26% reported using a centralized interface for all tests, regardless of vendor.

Centralizing security tools allows for a unified management interface, which simplifies the monitoring and configuration of security measures. This reduces the complexity associated with managing multiple disparate systems, facilitates integration at each stage of the pipeline, and ensures that security policies are consistently applied across the organization. With a centralized system, security efforts can be more easily coordinated, reducing the likelihood of gaps or overlaps in security coverage. A centralized, holistic approach enhances the ability to detect and respond to threats across the entire IT infrastructure.

Centralized management also allows better visibility into an application’s security profile, enabling more effective identification and mitigation of vulnerabilities. Further, it facilitates the collection and analysis of security data, which is crucial for proactive threat detection and response.

Overall, centralization and vendor consolidation in security testing can significantly enhance an organization’s ability to protect its digital assets by simplifying management, improving coordination, and potentially reducing costs.

### A struggle to attain full security coverage

**Q3.** Which of the following statements best describes the manner in which new projects, branches, or repositories are added to your application security testing queue?

*   All are added to the test queue manually (e.g., declared by dev team, selected by security team) 29%
*   All are added to the test queue automatically (e.g., detected by testing tools) 38%
*   Most are added to the test queue automatically; a few are added manually 22%
*   Most are added to the test queue manually; a few are added automatically 6%
*   I am not familiar with how items are added to the security testing queue 4%

[blackduck.com](blackduck.com) | 6

**Q4.** Approximately what percentage of your projects, branches, and repositories are included in your application security testing queue?

| Percentage of projects, branches, and repositories included in testing queue | Percentage of respondents |
| :-------------------------------------------------------------------------- | :-----------------------: |
| 41%–60%                                                                     |            37%            |
| 61%–80%                                                                     |            21%            |

Despite the emphasis on comprehensive security, many organizations struggle to achieve full coverage, as the responses to Questions 3 and 4 demonstrate. Nearly 30% of respondents still add new projects, branches, or repositories to their application security testing queue manually. Six percent use mostly manual processes with some automation. In other words, about 35% of organizations are still heavily reliant on manual intervention in their security testing queue management.

While there are varying perceptions of the extent to which security testing impacts development workflows, survey results show a clear correlation between the perceived impact on testing and manual processes. For example, 50% of those that say application security testing slows down the process also say that most projects are added to the test queue manually.

However, 38% of respondents report that they are taking full advantage of automated processes to include all projects in test queues, and another 22% report mostly using automated processes. This means that 60% of organizations are leveraging automation to a significant degree in their security testing workflows.

Thirty-seven percent of respondents include only 41% to 60% of their projects, branches, and repositories in their testing queue. Twenty-one percent achieve 61% to 80% coverage.

This coverage gap presents significant risk, potentially leaving critical parts of an organization’s application ecosystem untested. While counterintuitive, some respondents noted slightly higher-than-average coverage despite using manual processes to add projects to the test queue. This may simply be the level of coverage being perceived as higher due to the greater level of effort to test each project.

### Who determines when security tests are run

**Q5.** Which of the following teams/departments determine which application security tests are performed, when, and on which projects?

*   Security 44%
*   Development/software engineering 42%
*   DevOps 37%
*   Quality assurance 34%
*   Compliance 28%
*   Cross-functional groups 21%
*   Legal 19%
*   None of the above 1%

The responses to Question 5 offer valuable insights into how organizations are structuring their application security testing decisions. This data paints a picture of organizations increasingly treating security as a shared responsibility, integrated into various stages of the software development life cycle.

The close percentages for security (44%) and development/ software engineering (42%) suggest a trend toward shared responsibility for security testing. This aligns well with DevSecOps principles, indicating that security is becoming more integrated into the development process.

At 37%, DevOps teams play a significant role in security testing decisions. This further supports the trend toward integrating security throughout the development life cycle. At 34%, QA teams are also heavily involved,

> About 35% of organizations are still heavily reliant on manual intervention in their security testing queue management.

[blackduck.com](blackduck.com) | 7

suggesting that many organizations view security as an integral part of overall software quality.

The involvement of compliance (28%) and legal (19%) teams indicates that regulatory and legal requirements are significant factors in security testing decisions for many organizations.

Twenty-one percent of respondents indicate that cross-functional groups are involved in these decisions, showing a trend toward collaborative, multidisciplinary approaches to security. With only 1% selecting “None of the above,” it’s clear that the majority of organizations have specific teams or processes in place for determining security testing.

The distribution across teams suggests a relatively mature approach to security in many organizations, moving away from security as solely the responsibility of a dedicated security team. These results align with broader industry trends toward DevSecOps and “shift-everywhere” security practices, as described in the “Building Security in Maturity Model” report, where security is integrated earlier and more continuously in the development process.

### A tool proliferation challenge

**Q6.** Approximately how many application security testing tools does your organization use?

| Number of security testing tools | Percentage of respondents |
| :-----------------------------: | :-----------------------: |
|              6–10              |            34%            |
|             11–15              |            33%            |
|             16–20              |            15%            |
|              Total              |            82%            |

One of the most striking findings from our survey is the sheer number of security testing tools in use, as shown by the responses to Question 6. Eighty-two percent of organizations use between 6 and 20 security testing tools.

A proliferation of tools, although intended to provide comprehensive coverage, introduces significant complexity in integration, results interpretation, and overall management. It correlates strongly with another key challenge—noise in security testing results.

### The noise factor

**Q9.** Approximately what percentage of security test results are noise? For example: duplicative results, false positives, conflicting with other tests/tools.

| Percentage of noise in findings | Percentage of respondents |
| :-----------------------------: | :-----------------------: |
|            21%–40%             |            30%            |
|            41%–60%             |            30%            |
|              Total              |            60%            |

Question 9 uncovers a significant hurdle in effective security testing: the high level of noise in results. A total of 60% of respondents reported that between 21% and 60% of their security test results are noise. A high noise level can significantly impact the effectiveness of security efforts and lead to efficiency loss, as teams must spend time filtering out irrelevant findings. It can also lead to alert fatigue and genuine threats being overlooked, as well as resource misallocation due to organizations directing too much of their security efforts toward noncritical issues.

### Role-based differences

There is a perception among security personnel of a high percentage of noise within security test results. This is likely because security teams are commonly tasked with managing security tests, as they sit toward the top of the review funnel. These teams present dev/engineering teams with cleansed and prioritized results, which in turn results in those teams skewing toward lower perceived noise.

Likewise, 17% of dev/engineering personnel feel they don’t have enough visibility into security tests to identify noise in results. This is in stark

> 82% of organizations use between 6 and 20 security testing tools.

[blackduck.com](blackduck.com) | 8

contrast to CISOs, CTOs/CPOs, and AppSec professionals; only 1% of respondents in those roles cite a lack of visibility when detecting noisy results. One core tenet of efficient DevSecOps is adequate visibility into software artifacts and associated risks across all teams. Inadequate visibility can slow down issue detection, prioritization, and remediation, and leave pipelines prone to breakdowns and software open to attack.

### The AI revolution in security testing

**Q14.** Are your developers using AI, generative, or transformational tools to write code and modify projects?

| Response                                                              | Percentage |
| :-------------------------------------------------------------------- | :---------: |
| Yes (Net)                                                             |     91%     |
| Yes, all developers are permitted to, and do, use these tools          |     27%     |
| Yes, but only certain developers/teams are permitted to, and do, use these tools |     43%     |
| Yes, while we do not allow the use of these tools, we are aware that some developers use them |     21%     |

Over 90% of organizations are using AI tools in some capacity for software development. The distribution of responses to Question 14 illustrates a seemingly phased adoption curve. Twenty-seven percent of respondents note that all developers are permitted to use AI, generative, or transformational tools in their work, while 43% permit only certain developers or teams to use such tools, and 21% forbid their use alongside an awareness that such tools are, in fact, being used by their developers.

### Worldwide AI adoption

**Q14.** Are your developers using AI, generative, or transformational tools to write code and modify projects (by region)?

| Region      | Yes (Net) | Yes, all developers are permitted to, and do, use these tools | Yes, but only certain developers/teams are permitted to, and do, use these tools | Yes, while we do not allow the use of these tools, we are aware that some developers use them | No, developers are not permitted to, and do not, use these tools | I do not have enough visibility into development processes to know if these tools are used |
| :---------- | :-------: | :----------------------------------------------------------: | :-------------------------------------------------------------------------------: | :------------------------------------------------------------------------------------: | :--------------------------------------------------------------------------------: | :--------------------------------------------------------------------------------: |
| U.K.        |    94%    |                             30%                              |                                      39%                                       |                                         26%                                         |                                4%                                 |                                2%                                 |
| U.S.        |    97%    |                             26%                              |                                      46%                                       |                                         26%                                         |                                2%                                 |                                2%                                 |
| France      |    92%    |                             26%                              |                                      41%                                       |                                         25%                                         |                                6%                                 |                                2%                                 |
| Germany     |    94%    |                             20%                              |                                      50%                                       |                                         24%                                         |                                6%                                 |                                1%                                 |
| Finland     |    93%    |                             27%                              |                                      51%                                       |                                         14%                                         |                                5%                                 |                                2%                                 |
| China       |    97%    |                             35%                              |                                      50%                                       |                                         12%                                         |                                3%                                 |                                0%                                 |
| Singapore   |    96%    |                             37%                              |                                      37%                                       |                                         22%                                         |                                2%                                 |                                2%                                 |
| Japan       |    60%    |                             26%                              |                                      45%                                       |                                         25%                                         |                                3%                                 |                                1%                                 |

The regional responses to Question 14 demonstrate that AI adoption in software development is not only a phenomenon—it is a global phenomenon, with slight variations in results probably reflecting differences in technological infrastructure, regulatory environments, or cultural attitudes toward AI.

[blackduck.com](blackduck.com) | 9

Similar numbers play out by industry sector, with over 90% adoption reported across the Technology, Cybersecurity, FinTech, Education, Banking/Financial, Healthcare, Media, Insurance, Transportation, and Utilities sectors. Even lagging sectors, such as Nonprofit, report at least 50% adoption. Perhaps unsurprisingly, the larger the organization, the more likely it has significantly adopted some facet of AI in its software development.

This trend is reshaping the security testing landscape and also introduces new challenges, particularly in securing AI-generated code and managing potential biases or vulnerabilities that AI systems might introduce, as the responses to Question 15 show.

**Q15.** How confident are you that you have the processes in place to manage and secure AI-generated code?

| Response                                                              | Percentage |
| :-------------------------------------------------------------------- | :---------: |
| Confident (Net)                                                       |     85%     |
| Very confident we have the policies and automated testing in place     |     24%     |
| Moderately confident we have the policies and automated testing in place |     41%     |
| Slightly confident we have the policies and automated testing in place  |     20%     |
| Not at all confident we have the policies and automated testing in place |      6%     |
| This is not a priority at this time, as using AI-generated code is against company policies |      4%     |
| I do not have enough visibility into our processes to manage and secure AI-generated code |      5%     |

### Most respondents not confident they’re securing AI-generated code

While the net confidence level of respondents to Question 15 may seem high at first blush, a deeper dive into the responses show that 41% of respondents are only moderately confident that they have the policies and automated testing in place to adequately vet AI-generated code, while 20% are only slightly confident and 6% are not at all confident—a total 67% of respondents altogether showing concern about managing and securing AI-generated code.

This distribution suggests that even though their development teams are adopting AI tools, many organizations are still in the process of putting policies and tools into place to manage the unique challenges posed by AI-generated code. Ensuring the reliability and security of that code remains a significant challenge. As one example, AI tools trained on public open source codebases could introduce potential IP, copyright, and license issues into the code they produce, particularly if that code is used in proprietary software.

**Figure 1.** Developers’ AI usage (permitted or not) correlated against moderate to high confidence in security controls

*Image Description: A stacked bar chart showing the distribution of confidence levels in security controls for AI-generated code, broken down by different levels of AI usage permission. The x-axis represents four groups of organizations: those that forbid AI use, those that permit all developers to use AI, those that permit only certain developers/teams to use AI, and those that do not allow AI use but are aware that some developers use it. The y-axis represents the percentage of respondents. The bars are segmented to show the percentage of respondents in each group who are very confident, moderately confident, slightly confident, not at all confident, or who do not prioritize AI security.*

In Figure 1, starting from the left, less than 5% of organizations forbid developers from using AI to write code or modify projects. Perhaps this group’s moderate and high confidence in their preparedness derives from their prohibition of the use of AI, or perhaps there are other access controls that preclude access to AI resources.

The second group, 27% of respondents, reports a strong awareness that AI is being used. Eighty-one percent have moderate or high confidence in their security preparedness (22% of overall responses). These respondents are readily leveraging AI tools and confident that they have the controls in place to mitigate consequent risks.

The third and fourth groups are in the midst of an AI evolution, with moderate to high confidence in their security preparedness and a seemingly phased approach to AI-enabled development.

[blackduck.com](blackduck.com) | 10

**Figure 2.** Developers’ AI usage (permitted or not) correlated against low to slight confidence in security controls

*Image Description: A stacked bar chart showing the distribution of confidence levels in security controls for AI-generated code, broken down by different levels of AI usage permission. The x-axis represents four groups of organizations: those that forbid AI use, those that permit all developers to use AI, those that permit only certain developers/teams to use AI, and those that do not allow AI use but are aware that some developers use it. The y-axis represents the percentage of respondents. The bars are segmented to show the percentage of respondents in each group who are very confident, moderately confident, slightly confident, not at all confident, or who do not prioritize AI security.*

### AI and code snippets

A common practice of developers is to use “snippets” (small extracts from larger pieces of code) in software, a problem now exacerbated by the use of AI coding assistants. Although code might include only a snippet of open source, users of the software must still comply with any license associated with the snippet.

Even one noncompliant license in software can result in legal reviews, freezes in merger and acquisition transactions, loss of intellectual property rights, time-consuming remediation efforts, and delays in getting a product to market.

Black Duck’s 2024 OSSRA report relates that over half—53%—of the applications examined contained open source with license conflicts, exposing those applications’ owners to potential IP ownership questions.

In Figure 2, we can see some dissonance between respondents’ use of AI-generated code and AI-assisted development, and the steps they’re taking to safeguard their intellectual property and mitigate security risks.

Starting from the left, the less than 5% that forbids the use of AI tools altogether exhibits slight or nonexistent confidence in security preparedness, with nearly 42% of this group claiming a lack of priority. Consequently, their choice to disallow AI-enabled development may stem from this lagging organizational approach to securing AI-generated code.

The rightmost group highlights a greater exposure to risk, where automated testing of AI-generated code is a notably lower priority despite an awareness of the use of AI-assisted development.

The group second from right illustrates a seemingly phased adoption of AI-enabled development and security controls, with limited permission being granted, perhaps based upon a slight confidence in preparedness.

Most concerning is the group second from left, which has some development teams that are using AI with permission, despite a clear lack of confidence in their preparations to mitigate risks.

[blackduck.com](blackduck.com) | 11

## Interpreting and acting on security test results

The effectiveness of application security testing hinges not just on the execution of tests, but also on the ability to interpret results and take appropriate action. This section examines the current state of result interpretation and remediation based on our survey results, highlighting both progress and persistent challenges in the field.

**Q7.** Which statement best describes the clarity and actionability of the results of your application security tests?

### Role-based differences

Our analysis suggests that CISOs, CTOs/CPOs, and AppSec professionals generally reported higher levels of ease in understanding and acting upon security test results compared to other roles (Question 7). For example, 37% of CISOs, 23% of CTO/CPOs, and 21% of AppSec professionals found security test results “extremely easy” to understand and to act upon. In contrast, only 14% of DevOps and dev/engineering personnel found these tasks extremely easy. This may be due to senior-level personnel having more experience or better interpretative tools at their command than workers in the trenches. Unfortunately, those workers are usually the ones on the front line of security testing and the ones whose efforts are being hampered by the lack of clarity in testing results.

**Q7** Which statement best describes the clarity and actionability of the results of your application security tests (by regional)?

### Geographical differences

Notable variations were observed across countries. For example, 88% of respondents in China found testing results easy to understand, compared to 55% in the U.S. and 51% in Japan. These regional disparities suggest differences in tool adoption, security culture, or regulatory environments across countries.

| Region      | Regard results as easy to interpret and act on |
| :---------- | :-------------------------------------------: |
| Singapore   |                      72%                      |
| U.K.        |                      88%                      |
| U.S.        |                      83%                      |
| China       |                      82%                      |
| Germany     |                      76%                      |
| Finland     |                      73%                      |
| France      |                      71%                      |
| Japan       |                      55%                      |

| Role                      | Security test results are extremely easy to understand and to act upon |
| :------------------------ | :------------------------------------------------------------------: |
| All respondents           |                                20%                                 |
| CISO                      |                                37%                                 |
| CTO/CPO                   |                                23%                                 |
| AppSec                    |                                21%                                 |
| DevOps and dev/engineering |                                14%                                 |

[blackduck.com](blackduck.com) | 12

### Different approaches to parsing and cleansing results

**Q8.** Which statement best describes your approach to parsing and cleansing the results of application security tests?

*   Results generated by all tools are manually parsed and cleansed 38%
*   We can automatically parse and cleanse results from some testing tools; the remainder are manually parsed and cleansed 28%
*   Results generated by all tools are automatically parsed and cleansed 25%

#### Automated vs. manual review

As illustrated in Figure 3, it is possible to associate ease of interpretation and action with the method of parsing and cleansing data. The resulting insight reveals a clear benefit to establishing automated mechanisms for parsing and cleansing security test data, whether the benefit comes from accelerated review or more consistent elimination of noise before human consumption. Of those that manually parse and cleanse test results, 22% find those results somewhat or extremely difficult to understand and act upon. Of those that use automated means, only 10% find the same difficulty.

Conversely, 90% of those that use automated methods to parse and cleanse data find the results of security tests somewhat or extremely easy to understand and act upon, while only 77% report the same ease by doing so manually. Notably, when examining those with hybrid approaches to reviewing test results, we see a “worst of both worlds” experience, with 35% citing difficulty understanding and acting on results, and only 64% finding it easy to do so.

The process of parsing and cleansing security test results reveals a spectrum of approaches (Question 8). For example, 38% of respondents manually parse and cleanse results from all tools. Twenty-five percent report fully automated parsing and cleansing of results. Twenty-eight percent use a combination of automated and manual parsing and cleansing.

The prevalence of manual and hybrid approaches (66% combined) indicates a significant opportunity for increased automation and normalization in results processing. However, the challenge lies in balancing automation with the need for human expertise in interpreting complex security contexts.

**Figure 3.** Impact of review method on understanding results