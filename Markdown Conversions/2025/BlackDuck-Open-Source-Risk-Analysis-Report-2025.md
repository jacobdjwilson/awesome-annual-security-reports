# 2025 Open Source Security and Risk Analysis Report

## Table of Contents
- [Welcome to the 2025 OSSRA Report](#welcome-to-the-2025-ossra-report)
  - [Who Should Read This Report](#who-should-read-this-report)
  - [What You’ll Learn and Why It Matters](#what-youll-learn-and-why-it-matters)
  - [About This Report’s Data and Black Duck Audits](#about-this-reports-data-and-black-duck-audits)
- [Our Findings at a Glance](#our-findings-at-a-glance)
- [Looking at Open Source Risk and Vulnerabilities](#looking-at-open-source-risk-and-vulnerabilities)
  - [Software Security Begins with Visibility into Your Code](#software-security-begins-with-visibility-into-your-code)
  - [Understanding Risk Management and Gaining Visibility into Your Code](#understanding-risk-management-and-gaining-visibility-into-your-code)
  - [Enhancing Software Security and Transparency with SCA and SBOMs](#enhancing-software-security-and-transparency-with-sca-and-sboms)
  - [Analyzing the Impact of a Vulnerability](#analyzing-the-impact-of-a-vulnerability)
  - [Log4j and Equifax: Two Lessons on the Need for Visibility into Your Code](#log4j-and-equifax-two-lessons-on-the-need-for-visibility-into-your-code)
  - [The Top High- and Critical-Risk Vulnerabilities](#the-top-high--and-critical-risk-vulnerabilities)
  - [What the Data Tells Us](#what-the-data-tells-us)
  - [Industry-Specific Insights](#industry-specific-insights)
- [Open Source Licensing](#open-source-licensing)
  - [How Conflicts, Variants, and Lack of Licenses Create Risk](#how-conflicts-variants-and-lack-of-licenses-create-risk)
  - [The Impact of Transitive Dependencies on License Conflicts](#the-impact-of-transitive-dependencies-on-license-conflicts)
  - [The Top 10 Open Source Licenses of 2024](#the-top-10-open-source-licenses-of-2024)
  - [What Are Permissive, Weak Copyleft, and Reciprocal Open Source Licenses?](#what-are-permissive-weak-copyleft-and-reciprocal-open-source-licenses)
  - [How to Manage Open Source License Risk with SCA](#how-to-manage-open-source-license-risk-with-sca)
  - [Industry Perspectives on License Conflicts](#industry-perspectives-on-license-conflicts)
  - [If You Anticipate an M&A](#if-you-anticipate-an-ma)
- [Maintenance and Operational Factors Impacting Risk](#maintenance-and-operational-factors-impacting-risk)
- [Conclusion: The More Things Change](#conclusion-the-more-things-change)
  - [Key Recommendations](#key-recommendations)

---

## Welcome to the 2025 OSSRA Report

Open source software (OSS) has revolutionized application development, providing a vast repository of prebuilt components that offer numerous benefits such as cost savings, flexibility, and scalability. However, with all those benefits comes risks that every organization using open source needs to be prepared to acknowledge and address.

The 2025 “Open Source Security and Risk Analysis” (OSSRA) report details key findings from Black Duck® audit data, including security vulnerabilities, licensing issues, component maintenance, and industry trends. Our analysis shows that open source is ubiquitous, and that it can introduce significant risk unless properly identified and managed.

> “He will win who has prepared himself.”
> —Sun Tzu

### Who Should Read This Report

The findings of this report will be beneficial for a variety of readers, particularly those involved in securing the software supply chain, as well as those directly involved in software development, security and risk management, and merger and acquisition (M&A) activities.

Developers will gain insights into the types of vulnerabilities that we found prevalent in open source software, such as _cross-site scripting (XSS)_ and _denial-of-service (DoS)_ vulnerabilities. For example, the OSSRA report highlights the importance of following input validation and sanitization techniques, which can help developers build more-secure applications.

Further, this report identifies the most common open source components containing vulnerabilities, which will aid developers in making informed decisions when selecting open source libraries and frameworks. For example, development teams should be aware that our data shows that jQuery, jackson-databind, and the Spring Framework often include vulnerabilities that require regular management and patching.

OSSRA 2025 also emphasizes the risks associated with using out-of-date components and the need for all organizations to implement a process for timely updates. As one example, **90%** of audited codebases were found to have open source components more than four years out-of-date. Outdated components magnify security risk, provide attackers with an expanded attack surface, and create compliance and compatibility issues. The presence of older open source also suggests that developers are not taking advantage of software improvements and are relying on code that is no longer being maintained.

Readers with a security focus can leverage the data presented in OSSRA 2025 to improve their vulnerability management processes. For example, the report identifies the top common vulnerabilities and exposures (CVEs) found in our audits, as well as their relationship to common software weaknesses (CWEs).

Risk management professionals can use OSSRA data to inform their strategic decisions about open source software adoption and risk mitigation. The ability to compare vulnerability percentages and other metrics across industries can help risk managers pinpoint areas where their organization is performing well or needs improvement.

The OSSRA data, primarily derived from analysis of M&A targets’ code, provides key insights for professionals involved in merger and acquisition transactions into the kinds of issues they may be taking on in their own transactions, such as common open source license conflicts, the security posture of the target company, and potential operational challenges that could impact the target’s IP value.

### What You’ll Learn and Why It Matters

There’s much more open source in your software than you think: **Ninety-seven percent** of the codebases we evaluated contained open source, with an average **911 OSS components** found per application. From an industry perspective, the percentages ranged from **100%** in the Computer Hardware and Semiconductors, EdTech, and Internet and Mobile Apps sectors, to a “low” of **79%** for Manufacturing, Industrials, and Robotics.

Open source codebases are getting bigger and more complicated: Our data shows that the number of open source files in an average application has tripled in just the last four years. One of the reasons behind this is the use of “_transitive dependencies_”—open source libraries that other software components rely on to function. Open source frequently uses other open source. Our audits found that **64%** of open source components identified in our scans were transitive dependencies, most nearly impossible to locate or track without using an automated tool. Finding all instances of a transitive dependency can be like searching for a needle in a haystack when you lack an up-to-date inventory of third-party code.

Where all this open source is coming from: Our audits show that the majority of open source is being downloaded from package manager repositories. Over 280,000 of the nearly 1 million OSS components found in our audits originated from one such repository—npm, a massive public database of JavaScript packages.

Whether you think of open source as “free” or not, it comes at a cost: The odds are better than **