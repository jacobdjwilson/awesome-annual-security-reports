# DEVSECOPS PRACTICES AND OPEN SOURCE MANAGEMENT IN 2020

A SURVEY OF 1,500 IT PROFESSIONALS

## Table of Contents
- [Introduction](#introduction)
- [Section 1: Survey Highlights](#section-1-survey-highlights)
  - [DevOps and the secure SDLC](#devops-and-the-secure-sdlc)
  - [DevSecOps tools](#devsecops-tools)
  - [Open source selection and governance](#open-source-selection-and-governance)
  - [Open source security and patching](#open-source-security-and-patching)
  - [Open source project sustainability](#open-source-project-sustainability)
  - [Conclusion: Developing security in depth for the SDLC](#conclusion-developing-security-in-depth-for-the-sdlc)
- [Section 2: Full Survey Results](#section-2-full-survey-results)
  - [Respondent demographics](#respondent-demographics)
  - [Questions](#questions)

---

## Introduction

In August 2020, the Synopsys Cybersecurity Research Center (CyRC) and Censuswide, an international market research consultancy, conducted a survey of 1,500 IT professionals with DevSecOps as part of their role and who work in cyber security, software development, software engineering, and web development.

The group was recruited to take part in an online survey focused on DevSecOps practices and open source use. Participants came from the United States, the United Kingdom, Finland, Germany, China, Singapore, and Japan, with at least 50 respondents from each country. The survey is part of CyRC’s ongoing research into cyber security practices and is intended as a complement to Synopsys’ annual Open Source Security and Risk Analysis (OSSRA) report.

As the 2020 OSSRA report[^1] details, almost 100% of the 1,200+ audited codebases in that report contained open source components or libraries, with open source making up 70% of the codebases themselves. Gartner’s report, “Market Guide for Software Composition Analysis,”[^2] relates that due to the prevalence of open source in modern software development, corporate interest in software composition analysis (SCA) tools used to manage open source is growing rapidly, with inquiries to the analyst firm on the topic increasing nearly 40% from 2019 to 2020.

While the OSSRA report provides an in-depth snapshot of the current state of open source security, compliance, and code quality risk, this survey reports on the tools organizations in the business of building software are employing to integrate open source management into their DevOps practice. The survey also explores the strategies being used to address open source license compliance, vulnerability management, and the growing issue of legacy open source in commercial code.

Section 1 of this report details the highlights of these survey findings, and Section 2 includes full survey results.

---

## Section 1: Survey Highlights

### DevOps and the secure SDLC
One of CyRC’s areas of interest in conducting this survey was to investigate the prevalence of DevSecOps—the practice of integrating security into every stage of the DevOps pipeline—across industry verticals and throughout organizations around the world. While we expected to find evidence of a DevSecOps trend, our results point to a more mature adoption of DevSecOps among respondents than anticipated.

Thirty-three percent of the respondents noted that their organizations are well on their way to a mature deployment of DevSecOps. An additional 30% reported that they are making measurable strides toward maturity. With a combined 63% of respondents reporting that they are incorporating some measure of DevSecOps activities into their software development pipelines, it’s safe to say that adoption of the DevSecOps methodology is an important, rapidly growing trend.

![Figure 1: How mature is the adoption of DevSecOps practices within your team?]

Synopsys’ 2020 Building Security in Maturity Model (BSIMM) report,[^3] which looks at the current state of application security across a large number of organizations, notes that “the idea of baking security into all phases of a DevOps life cycle is quickly becoming the norm. But organizations are adopting this approach in their own ways and at their own pace.”

Tellingly, 42% of respondents to our survey have a dedicated security team. Also known as a software security group (SSG), this team’s responsibility may include acquiring, creating, deploying, and managing secure software. Having an SSG is another indicator of maturity in an organization’s software security practices, according to the Synopsys BSIMM report as well as other benchmarking tools for software security initiatives.

![Figure 2: Who, if anyone, is responsible for application security in your organization?]

### DevSecOps tools
Figure 3 indicates that many organizations in the business of building software need to increase their investments in software composition analysis (SCA) and interactive application security testing (IAST), which enable security automation at the development phase. Successful DevSecOps strategies entail a full security toolset—including dynamic application security testing (DAST), IAST, static analysis security testing (SAST), and SCA tools—to fully address code quality and security flaws early in the software development life cycle (SDLC).

SCA tools are employed by 38% of the respondent organizations. SCA products analyze applications throughout the entire SDLC to detect open source software. These tools typically produce an inventory, or Bill of Materials (BOM), of all open source in the codebase, the versions of that open source, the download locations for each project and all dependencies, the libraries the code calls to, and the libraries those dependencies themselves link to.

SCA tools also advise of known open source vulnerabilities found in the code, available security patches, and the license(s) used to distribute the respective open source packages. Comprehensive SCA solutions also monitor the BOM to provide customers with early notification of new vulnerabilities, and even deliver upgrade/patch guidance.

Of note is that the tool with the highest adoption rate is still only utilized by 45% of respondents, indicating that there is no universally adopted application security tool.

![Figure 3: Which, if any, of the following security tools does your team currently use?]

### Open source selection and governance
The survey results indicate that most respondents’ organizations are at a relatively high level of maturity when it comes to how they select open source and how they ensure that their policies on open source use are being followed. An overwhelming percentage—72%—have a published policy on open source use. The majority of those policies define acceptable open source licenses; 55% prescribe patching/updating requirements, and close to half define open source components that are acceptable for use.

![Figure 4: Does your organization have a published policy for open source use?]
![Figure 5: Which, if any, of the following requirements are true for your policy on open source use?]

A large majority (64%) of the respondents’ organizations also have a specific individual or board of governors charged with open source oversight and whose responsibilities include developing open source governance processes, setting use policies, and defining acceptable open source components for organizational use.

![Figure 6: Do you have an open source governance board or specific individual charged with open source governance?]
![Figure 7: What criteria is used in the vetting process for a new open source component?]

### Open source security and patching
Somewhat troubling were the results in the respondents’ answers to the question of patching. Over half—51%—say it takes 2 to 3 weeks for their organization to apply an open source patch, with 24% noting that it can take up to a month, even when the patch addresses a critical issue.

Parsing the results by country, it appears that the United States is being most heavily impacted by unpatched open source components. Over half of respondent organizations in the U.S. have had their software delivery schedule affected in the past year because of addressing a critical open source patch, compared to 40% globally.

![Figure 8: When a critical open source vulnerability is identified by your organization, on average, how long does it take for your teams to provide a fix?]
![Figure 9: Has addressing a critical open source patch impacted your software delivery schedule within the past year?]

The media comes under regular—sometimes deserved—criticism from the open source community for exaggerating security incidents and the risk of open source use. However, most coverage notes that the risk comes from the unmanaged use of open source, with reported incidents usually involving unpatched or outdated components, or the lack of an up-to-date software inventory, one of the primary causes behind the Equifax data breach.[^4]

![Figure 10: Has media coverage of an open source issue ever caused your organization to do any of the following?]

### Open source project sustainability
As shown in the highlighted section from Figure 5, 47% of respondents’ organizations define standards around the age of open source components, an acknowledgement of a growing problem in the open source community—project sustainability.

There’s no guarantee that the people behind any given open source project will continue maintaining the code. In fact, of the 1,200+ codebases examined for the 2020 OSSRA report, 88% contained open source components that had no development activity in the last two years.[^5]

All software ages. As it ages, it loses support. With open source, the number of developers working to ensure updates—including feature improvements, as well as security and stability updates—decreases over time. The component becomes more likely to break without the support needed to provide fixes. At some point, as that open source component ages and the number of people who handle bug reports and code reviews diminishes, the component becomes increasingly likely to open a codebase to exploit.

### Conclusion: Developing security in depth for the SDLC
Organizations are producing and deploying software applications faster than ever before. Ensuring that developers are on board with security practices is even more critical to improving their efficiency. The Forrester report, “The State of Application Security, 2020" notes, “To meet developer needs, security pros must integrate application security testing tools into the CI/CD pipeline and enable scans to run automatically on check-in, build, and integration while also enabling autoremediation to make mitigating security flaws quick and painless.”[^6]

---

## Section 2: Full Survey Results

### Respondent demographics
- **Age**: 16-24 (5%), 25-34 (38%), 35-44 (34%), 45-54 (15%), 55+ (8%)
- **Gender**: Male (71%), Female (28%), Prefer not to say (1%)
- **Job Title**: Software development (52%), Software engineering (21%), Cyber security (21%), Web development (7%)
- **Company Size**: 1-9 (3%), 10-49 (9%), 50-99 (20%), 100-249 (27%), 250-500 (15%), 500+ (27%)
- **Geography**: North America (17%), Europe (18%), Asia (65%)

### Questions

#### General
- **What types of applications does your team usually create or manage?**
  - Web services: 51%
  - Mobile applications: 48%
  - Software libraries provided to third parties: 44%
  - Packaged commercial software: 42%
  - Firmware for embedded systems: 38%
- **How mature is the adoption of DevSecOps practices within your team?**
  - Mature or deployed widely: 33%
  - Limited to specific projects: 30%
  - Still researching: 11%
  - Not investigating: 10%
  - Immature/pilot: 10%
  - Not sure: 6%

#### Security and patching
- **Who is responsible for application security?**
  - Security team: 42%
  - Development: 29%
  - Shared: 18%
  - Operations: 9%
- **Which security tools does your team currently use?**
  - Web application firewall: 45%
  - SCA: 38%
  - DAST: 37%
  - Intrusion/detection: 37%
  - RASP: 34%
  - SAST: 33%
  - IAST: 33%

#### Selection, use, and governance
- **Does your organization have a published policy for open source use?**
  - Yes: 72%
  - No: 28%
- **Do you have an open source governance board?**
  - Yes: 64%
  - No: 36%

---

[^1]: Synopsys Cybersecurity Research Center, “2020 Open Source Security and Risk Analysis Report,” Synopsys, May 2020.
[^2]: Dale Gardner, “Market Guide for Software Composition Analysis,” Gartner, August 2020.
[^3]: Sammy Migues, John Steven, and Mike Ware, “Building Security in Maturity Model,” Synopsys, 2020.
[^4]: Permanent Subcommittee on Investigations, How Equifax Neglected Cybersecurity and Suffered a Devastating Data Breach, Committee on Homeland Security and Governmental Affairs, U.S. Senate, accessed September 12, 2020.
[^5]: Synopsys Cybersecurity Research Center, “2020 Open Source Security and Risk Analysis Report,” Synopsys, May 2020.
[^6]: Sandy Carielli, “The State Of Application Security, 2020,” Forrester, May 2020.