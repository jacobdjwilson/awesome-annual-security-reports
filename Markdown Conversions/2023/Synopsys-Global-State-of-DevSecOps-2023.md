# Global State of DevSecOps 2023
Strategies, Tools, and Practices Impacting Software Security

## Table of Contents
- [Overview](#overview)
- [About the Synopsys 2023 DevSecOps report](#about-the-synopsys-2023-devsecops-report)
- [On DevOps and DevSecOps](#on-devops-and-devsecops)
- [Benefits of automation](#benefits-of-automation)
- [The growing use of ASOC/ASPM in DevSecOps](#the-growing-use-of-asocaspm-in-devsecops)
- [Key Findings from the Synopsys 2023 DevSecOps Survey](#key-findings-from-the-synopsys-2023-devsecops-survey)
- [The State of DevSecOps in 2023](#the-state-of-devsecops-in-2023)
- [Lessons Learned](#lessons-learned)
- [Survey Demographics](#survey-demographics)
- [Appendix](#appendix)

# Overview
## About the Synopsys 2023 DevSecOps report
In early 2023, the Synopsys Cybersecurity Research Center (CyRC) and Censuswide, an international market research consultancy, conducted a survey of 1,000 IT professionals who identified security as part of their role or responsibilities. The group includes developers, AppSec professionals, DevOps engineers, CISOs, and experts who work in various roles in technology, cybersecurity, and application/software development. Participants came from the U.S., U.K., France, Finland, Germany, China, Singapore, and Japan.

Respondents from all industries and all company sizes were eligible to participate. One of the challenges faced while developing the survey is that the term “DevSecOps” embraces several disciplines, many of which have unique personas. The goal was to include a broad spectrum of professionals including “hands-on” developers who write the code and people at the CISO level, but targeting those whose work involved some aspect of software security.

## On DevOps and DevSecOps
Achieving the key tenets of DevOps—accelerated development, continuous delivery, pipeline resilience, scalability, and end-to-end transparency—requires a concerted effort from contributors in development, security, and operations.

An extension of the DevOps methodology, DevSecOps is designed to instill a culture of security across teams and address security early and consistently in DevOps environments. By integrating security practices into the software development life cycle (SDLC) and CI pipelines, DevSecOps aims to shift security from a separate, standalone phase to an integral part of the development life cycle.

DevSecOps has gained significant traction in every organization involved with software development. According to the SANS 2023 DevSecOps survey, DevSecOps is now clearly seen as a business-critical practice and a risk management concern. But historically, security and development teams have found themselves at odds when trying to introduce security into their processes, often a consequence of bringing legacy application security testing (AST) into the SDLC. Common complaints include AST tools’ complexity and high learning curves, slow performance, and “noisy” results causing DevOps “friction”—that is, anything in the software creation process that prevents developers from easily and quickly building code.

The majority of the respondents cited their general unhappiness with the AST tools they have in use
![Chart showing the following: 35% Tool(s) do not prioritize resolution based on exposure, exploitability, and criticality. 34% Too slow to fit into rapid release cycles/continuous deployment. 33% Inaccuracy/unreliability. 33% Cost vs. ROI]

## Benefits of automation
A core tenet of DevOps is to automate manual processes within each stage of the SDLC. Automation is a fundamental requirement before any organization can implement continuous integration or continuous deployment to develop and deliver code faster.

Successful DevSecOps requires the interplay of integration and automation, governed by standards and policies. This allows security teams to trust that security interests are being covered, and allows DevOps teams to keep working and trust that there won’t be unpredictable breakdowns in the pipeline.

Unlike manual testing, automated security tests can be executed quickly and consistently, allowing developers to identify issues early in the development process without impacting delivery schedules or productivity.

### Consistency
Automated tests ensure that security checks are consistently applied to every build and deployment. Manual testing might lead to variations in testing procedures and coverage.

### Scalability
As software grows in complexity, manual testing becomes impractical. Automated tests can easily scale to handle a large number of tests across various components.

### Continuous integration and continuous deployment (CI/CD)
Automated testing is crucial in CI/CD pipelines, where rapid and frequent code changes are deployed. Automated tests validate changes quickly and prevent faulty code from reaching production.

### Continuous improvement
Automated testing provides data and insights that help teams improve security practices over time. Patterns of vulnerabilities can be analyzed and addressed systematically.

### Documentation
Automated tests document the testing process, making it easier to track and audit security measures and compliance requirements.

### Reduction of human error
Manual testing can be error-prone due to fatigue or oversight. Automated tests follow predefined scripts, reducing the risk of human error.

### Time and cost savings
Identifying and fixing security issues late in the development process or in production can be time-consuming and costly. Automated testing minimizes these expenses.

### Improved developer experience
Automated application security testing enhances the developer experience by offering proactive, integrated, and educational solutions to address security concerns. This ultimately leads to more secure software and a more efficient development process.

## The growing use of ASOC/ASPM in DevSecOps
This report examines the characteristics of organizations at various stages of DevSecOps maturity and the security tools/practices the organizations employ. Based on the survey results, we offer prescriptive recommendations to those striving to attain a higher level of security maturity.

An interesting data point seen in the findings is the growing use of application security orchestration and correlation (ASOC), now more commonly referred to as application security posture management (ASPM). According to Gartner, ASPM should be a priority for any organization that uses multiple development and security tools.

ASPM solutions continuously manage application risks through the detection, correlation, and prioritization of security issues from development to deployment. ASPM tools ingest data from multiple sources and then correlate and analyze findings for easier interpretation, triage, and remediation.

ASPM also acts as a management and orchestration layer for security tools, enabling controls and the enforcement of security policies. And by providing a consolidated perspective of application security findings, ASPM offers a comprehensive view of security and risk status across an entire application or system.

Given that the majority of the 1,000 survey respondents cited their general unhappiness with the AST tools they have in use—criticisms included that those tools don’t prioritize remediation based on business needs (35%) and they can’t consolidate/correlate results for issue resolution (29%)—it’s little wonder that the use of ASOC/ASPM is growing rapidly.

28%
Reported that their organization used an ASOC tool

## Key Findings from the Synopsys 2023 DevSecOps Survey
### The majority of DevOps teams have adopted some level of DevSecOps
A total of 91% of respondents reported that they incorporate some measure of DevSecOps activities into their software development pipelines. It’s safe to say that adoption of the DevSecOps methodology is now an established part of software development.

### Organizations with a more mature security program have personnel focused on security
Twenty-nine percent of survey respondents noted that a cross-functional DevSecOps team—a collaborative group from development, security, and operations—was an important factor in a security program’s success. Personnel focused on security, working with developers/software engineers and/or QA and testing, are likely to be on the front lines of security testing in organizations with mature security programs.

### There are many barriers to effectively implementing DevSecOps
Over 33% of respondents pointed to inadequate security training as a major roadblock. This was closely followed by a shortage of security personnel (31%), lack of transparency into development/operations work (31%), and continuously changing priorities (30%).

### Over a third of respondents said that integrating automated security testing into build/deploy workflows was key to a security program’s success
Other critical factors included enforcing security/compliance policies through infrastructure-as-code, developing security champions in dev and ops teams, and improving communications across dev, ops, and security teams.

### Dealing with critical vulnerabilities late in the SDLC dramatically impacts the bottom line
More than 80% of respondents said that critical vulnerability/security issues in deployed software impacted their delivery schedules in some form during 2022-23.

Twenty-eight percent of respondents said their organizations take as much as three weeks to patch critical security risks/vulnerabilities in deployed applications; another 20% said it can take up to a month

These figures are especially disturbing because vulnerabilities are being exploited faster than ever. The latest studies show that well over half of reported vulnerabilities are exploited within a week of disclosure.

### Over 70% said automated scanning of code for vulnerabilities or coding flaws is a useful security measure, with 34% calling automated AST “very useful”
Automated scanning of code for security vulnerabilities and other defects led the “usefulness of tool/processes” category, followed closely by “defining security requirements as part of SDLC requirements stage” and “formal measurement of a software security program through models such as BSIMM and SAMM.”

### Nearly all respondents agreed that AST tools don’t align with their business needs
The majority of the 1,000 respondents cited as major problems a variety of issues with AST tools—including that those tools don’t prioritize remediation based on business needs (35%) and they can’t consolidate/correlate results for issue resolution (29%).

### Fifty-two percent of security professionals are already actively using AI in their DevSecOps practices, but more than three-quarters are concerned about issues with AI use
The survey results indicate that AI, machine learning, natural language processing, and neural networks are in active use by security teams. However, the growing use of generative AI tools such as AI-powered coding suggestions are spawning questions—in some cases, even lawsuits—around IP ownership, copyright, and licensing of the AI-generated code.

## The State of DevSecOps in 2023
### DevSecOps adoption
Over a third of the 1,000 respondents characterized their security initiatives at a Level 3 stage of maturity, in which security processes are documented, repeatable, and standardized across the organization. Twenty-five percent felt that they had attained Level 4, with security processes also logged, monitored, and measured.

With a total of 91% of respondents reporting that they have applied some type of DevSecOps activities into their software development pipelines, adoption of DevSecOps appears to have become an established part of DevOps.

![Chart showing the following: Level I: Security processes are unstructured/disorganized. 8.5%. Level II: Security processes are documented and repeatable for specific team. 24.1%. Level III: Level II processes and procedures are standardized across organization. A proactive security culture is endorsed and communicated by leadership. 34.3%. Level IV: Security processes and controls are logged, managed, and monitored. 24.5%. Level V: Security processes are continuously analyzed and improved. 8.5%.]
Figure A How would you best describe the maturity of your current software security program/initiative?

### Implementation of security practices indicate a higher level of maturity
Another measurement of DevSecOps maturity can be seen in Figure B, indicative that the respondents have adopted a broad set of security practices, ranging from continuous monitoring and measurement (30%) to automated testing (28%).

The leading practice, security risk management, cited by 358 respondents (35.1%), involves integrating security considerations at every stage of the development process to identify, assess, and mitigate potential security risks associated with a software application. Applied within the SDLC, overall security risk management entails
- Requirement analysis. Identifying security requirements and constraints early in the SDLC and defining security objectives.
- Design. Incorporating security principles into the system architecture and design to ensure an application’s design includes appropriate safeguards against common vulnerabilities.
- Development. Implementing secure coding practices and adhering to coding standards that address security concerns. Using integrated security testing tools such as static application security testing (SAST) and software composition analysis (SCA) to catch vulnerabilities as code is written and open source or third-party dependencies are brought in.
- Testing. Performing various types of security testing, such as SAST, dynamic application security testing (DAST), SCA, and penetration testing to identify vulnerabilities in the application.
- Deployment. Securely configuring the environment where the application will run. Implementing access controls, network security, and proper authentication and authorization mechanisms.
- Monitoring and measurement. Continuously monitoring the application in production for security incidents and anomalies. Implementing logging and monitoring solutions to detect and respond to potential breaches. This was cited by 30% of survey respondents as a major security practice in their organization.
- Response and remediation. Creating an incident response plan to address security incidents quickly and effectively. Remediating risks detected during the testing phase.
- Transparency and security enablement. Establishing clear standards, criteria, policies, and reporting of security risks and risk tolerance.
- Training. Providing training to development teams on secure coding practices, common vulnerabilities, and security best practices. This empowers developers to proactively address security concerns. Unfortunately, 34% of our survey respondents cited “inadequate/ineffective security training for developers/engineers” as one of the major blocks to implementing DevSecOps effectively at their organization.
- Continuous improvement. Regularly reviewing and improving the security processes and practices within the SDLC.

![Chart showing the following: Continuous monitoring and measurement 29.9%, Security risk management 35.1%, Configuration management 29.6%, Threat data and responses 29.3%, Continuous deployment 29.1%, Automated deployment 28.6%, Continuous testing 28.5%, Continuous integration 28.2%, Application security orchestration and correlation 28.4%, Automated testing 27.9%, Infrastructure-as-code 27.6%]
Figure B What practices does your organization follow? (Select all that apply)

### Measuring a security program
Nearly 70% of respondents said that measuring their security programs through an assessment tool such as Building Security In Maturity Model (BSIMM) was a useful exercise, with over a third calling such assessments “very useful.”

An outside assessment of a security posture allows organizations to analyze and benchmark their software security program against other organizations and industry peers. Tools such as BSIMM provide an objective, data-driven analysis on which to base decisions of resources, time, budget, and priorities. Comparing other software security programs with your own can guide the strategy for your efforts, whether you’re in the early stages of implementing a security program or want to ensure that your existing program can address changing business and security needs.

If you’re in charge of, or beginning to build, a software security program, understanding AppSec trends among your peer organizations can help you plan strategic improvements to your own security efforts. If you’re running a security program from the technical side, you can use the information garnered by a BSIMM or Software Assurance Maturity Model (SAMM) assessment to define tactical improvements for people and processes—for example, by building a Security Champions program.

In fact, according to the BSIMM report, one of the first initiatives that many software security groups undertake is identifying people who are a driving force in software security but not directly connected to a software security group. Collectively referred to as “software security champions,” these people can enable and emphasize software security efforts. Security champions in engineering teams, for instance, can encourage engineers to own the security of their software deliverables. Developing a Security Champions program was cited by 33% of survey respondents as a key factor to a security program’s success.

33%
Consider developing security champions in Dev and Ops teams a significant factor in their security program's success

![Chart showing the following: Useful (Net) 69.4%, Not that useful 18.1%, Very useful 33.6%, Not at all useful 8.4%, Somewhat useful 35.8%, Not useful (Net) 26.5%]
Figure C Usefulness of formal measurement of your software security through models such as BSIMM, SAMM, etc.

### The importance of cross-functional teams for DevSecOps success
Twenty-nine percent of survey respondents noted that a cross-functional DevSecOps team—a collaborative group from development, security, and operations—was an important key to a security program’s success (see Appendix Q16). Personnel with a focus on security, working with developers/software engineers and/or QA and testing teams (whether formally in DevSecOps groups or otherwise) are likely to be on the front lines of security testing in organizations in more mature security programs.

Monolithic, stove-piped security teams that stepped in to test shortly before or after deployment have gone the way of the dodo. In today’s software development environment, security testing is the responsibility of the entire engineering team, including QA, dev, and ops, and most will have had a hand in building security into their software at different stages of the SDLC.

Thirty-three percent of respondents mentioned that external consultants also conducted security tests for their organizations. Best practices advise that organizations should conduct security audits regularly. It can be invaluable to contract third-party auditors or penetration testers to conduct such tests in order to gain an unbiased view of an organization’s security posture.

![Chart showing the following: Internal security team 46.0%, Developers/software engineers 45.1%, QA/test teams 37.6%, Cross-functional DevSecOps teams 35.5%, External consultants 32.9%]
Figure D Who is responsible for conducting security testing in your organization? (Select all that apply)

### Combining manual and automated testing for the best results
The survey results indicate that the majority of respondents feel combining manual and automated security testing provides a more comprehensive approach to assessing the security of business-critical applications. As important as automated testing is for consistency, scalability, and time and cost-savings, the human factor adds a layer of insight and adaptability essential for identifying complex and subtle security issues. For example, the very nature of DAST as “black box” testing (that is, without knowledge of an application’s internal structure) requires developer and security experts to verify and triage findings.

Similarly, the fact that 44% of respondents include external pen testing as a key element of their security testing demonstrates the value of penetration testing as a complement to internal testing. Often required to comply with industry regulations and standards, external pen testing brings added benefits such as an unbiased viewpoint of your security posture, as well as accurate simulation of potential threats and vulnerabilities that external adversaries might exploit.

![Chart showing the following: Combination of both manual and automated assessments 52.6%, External pen testing 44.2%, Automated assessments and testing 43.7%, Manual assessments and/or tests (excluding pen testing) 43.0%, Unknown/unsure 0.2%]
Figure E How do you assess or test the security of your business-critical applications? (Select all that apply)

### Key performance indicators
Respondents were asked to pick the top three key performance indicators (KPIs) used to measure the success of their DevSecOps program. Overall reduction of open security vulnerabilities was cited by 295 respondents (29%), closely followed by the 28% (288 respondents) who referenced a reduction of security-related discoveries late in the SDLC as a crucial KPI. Rounding out the top three KPIs was issue resolution time, noted by 28% (281 respondents).

As the survey results demonstrate, time, productivity, and costs are the three commonalities among the top KPIs and the challenges organizations face in implementing a secure SDLC. Or, in other words, the three major questions those involved with DevSecOps face are
- How can we reduce the number of vulnerabilities/issues we encounter?
- What can we do to move vulnerability discovery earlier in the SDLC?
- How can we reduce the time it takes to resolve issues to both reduce build delays and improve developer productivity?

![Chart showing the following: Number of open security vulnerabilities 29.0%, Reduction of security-related discoveries late in the development process 28.3%, Issue resolution time 27.6%, Reduction in hours spent resolving security issues 27.4%, Compliance KPIs (percentage of audits passed, etc.) 23.8%, Reduction in security-related build delays 27.0%, Customer ticket volume 22.8%, Reduction in security-failed builds 24.4%, Defect escape rate 22.3%, There are no major KPIs we use to measure the success of our DevSecOps activities 1.1%]
Figure F What are the major KPIs you use to measure the success of your DevSecOps activities? (Select up to 3)

### Which AST tools are in use? How useful are they?
The survey results show that successful DevSecOps strategies use a full security toolset—including dynamic application security testing (DAST), interactive application security testing (IAST), static application security testing (SAST), and software composition analysis (SCA) tools—to address code quality and security flaws throughout the software development life cycle.

SAST was found to be the leading AST tool used by respondents, with 72% finding it useful. It was closely followed by IAST (69%), SCA (68%), and DAST (67%). SAST and DAST use different testing approaches that work most effectively in different phases of the SDLC. SAST is critical for uncovering and eliminating vulnerabilities in proprietary software early in the SDLC, before the application is deployed. DAST, on the other hand, is used after deployment to spot issues that manifest at runtime, such as authentication and network configuration flaws. Combining some of the features of both SAST and DAST, IAST is used to detect critical security flaws that may not be identified by other types of tests.

SCA is used to identify and manage open source security and license risk, a critical need in modern software development, especially considering that over three-quarters of the code in any given application is likely to be open source. And since many organizations use packaged software procured from independent software vendors, as well as Internet of Things (IoT) devices and embedded firmware, many will also need some form of SCA binary analysis in their AST toolbox.

![Chart showing the following: Automated scanning of code for security vulnerabilities and other defects (SAST) Useful (Net) 71.5%, Open source/third-party dependency analysis (SCA) Useful (Net) 67.6%, Dynamic application security testing (DAST) Useful (Net) 67.1%, Interactive application security testing (IAST) Useful (Net) 68.5%]
Figure G How useful, if at all, are the following application security tools used in your organization?

### When to test? When to patch? What’s the impact on our schedules?
The frequency of application security testing depends on several factors, including the business criticality of the application, the industry, and the threat landscape. For highly critical applications, assessments should be performed regularly, as reflected in our survey results (Figure H). Most respondent organizations run vulnerability scans on business-critical applications an average of two to three days a week.

On first blush, the survey results showing that 28% of organizations take up to three weeks to patch critical vulnerabilities (Figure I) may seem concerning, but there are other factors to consider. There is a myth that the proverbial developer can fix each and every vulnerability, but no one can rationally expect developers to dig into vulnerabilities that haven’t been prioritized for resolution. It’s worth noting that 31% of respondents cited “lack of transparency into development/operations work,” while another 29% identified “organizational silos between development, operations, security” as major barriers in implementing DevSecOps (Figure K). Both are indicative of issues with the communication of risk from security to development and the need for rapid alerting and automation with security policies.

In any case, patch priorities need to align with the business importance of the asset being patched, the criticality of the asset, and the risk of exploitation. That last is of high importance. Studies show that well over half of reported vulnerabilities are exploited within a week of disclosure.

![Chart showing the following: Every day 7.1%, Once a month 7.2%, 4 to 6 days a week 17.2%, Once every 2 months 7.5%, 2 to 3 days a week 20.4%, Once every 3 to 5 months 6.4%, Once a week 17.0%, Once every 6 to 11 months 4.4%, Less than once a year, please specify 0%, Once every 2 to 3 weeks 11.1%, Once a year 1.7%, Never 0.2%]
Figure H On average, how often, if at all, do you assess or test the security of your business-critical applications?

![Chart showing the following: Up to one week, please specify in days 4.6%, Over two months, up to four months 5.5%, Over one week, up to two weeks 26.4%, Over four months, up to six months 4.7%, Unsure 2.2%, Over two weeks, up to three weeks 28.3%, Over six months, please specify in months 0%, Over three weeks, up to one month 19.9%, Over one month, up to two months 8.4%]
Figure I On average, how long does it take for your organization to patch/resolve critical security risks/vulnerabilities for applications already deployed/in use?

With that in mind, organizations need to prioritize their efforts based on Common Vulnerability Scoring System (CVSS) scores and Common Weakness Enumeration (CWE) information, as well as the availability of exploits, not only on “day zero” of a vulnerability disclosure but over the life cycle of the application.

CVSS scores are an industry standard for assessing the severity of a vulnerability. Vulnerabilities in the National Vulnerability Database (NVD) have a base score that aids in calculating severity and can be used as a factor for prioritizing remediation. The CVSS score provides an overall base score that takes both exploitability and impact into account.

Temporal scores consider metrics that change over time owing to events that are external to the vulnerability. Remediation levels (Is there an official fix available?) and report confidence (Is the report confirmed?) can help temper the overall CVSS score to an appropriate level of risk.

CWE information lists software or hardware weaknesses that have security ramifications. A CWE tells developers which weakness could be exploited if an exploit is available. This information can help security and development teams understand where to focus developer security training, which additional security controls to implement across the SDLC and into production, and adds one more mechanism for assessing risk severity. For example, a development team may prioritize a SQL injection differently than a buffer overflow or denial of service, given the context of the data the application touches, where it is deployed, and other environmental and security factors.

The existence of an exploit will raise the risk score and help teams prioritize the highest-risk vulnerabilities for remediation. Understanding whether there is an existing patch, mitigating factor, or compensating controls is another key piece of information to examine once you have assessed the overall risk. If you have two medium-risk vulnerabilities without exploits available, for example, the final determination of which to fix first might come down to whether either has a patch or workaround available.

Critical security or vulnerability issues in deployed applications tend to cascade downhill, not only through their potential of disrupting an organization’s (or its customers’) business operations, but also their impact on the entire SDLC, as shown in Figure J.

Issues that might have been minor fixes if they had been caught early in development could mutate into “all hands on deck” firedrills in deployed applications. Automated security testing tools, integrated into IDEs and CI pipelines, can identify vulnerabilities and weaknesses in the code as soon as—or even before—it’s committed, enabling developers to address issues before they propagate downstream.

![Chart showing the following: No impact (Net) 18.9%, No impact at all 1.8%, Not much of an impact 17.2%, A little impact 42.7%, A large impact 38.4%, Impact (Net) 81.1%]
Figure J How much of an impact, if at all, has addressing a critical security/vulnerability issue had on your organization’s software delivery schedule within the past year (2022-2023)?

### Challenges to effective DevSecOps
The shortage of cybersecurity personnel is a significant challenge for DevSecOps, with many organizations unable to fill critical cybersecurity positions, as reflected in Figure K. According to some studies, there are 3.5 million unfilled cybersecurity jobs around the world.

As the demand for trained cybersecurity professionals grows, the scarcity of supply is driving up wages for skilled practitioners, pricing out many government entities and SMBs. But, as the top response indicates, inadequate security training for developers/engineers remains the biggest challenge.

One strategy that has shown to be effective to address these issues is the development of a Security Champions program, a collection of people across the organization who show an above-average level of security interest or skill and who are already contributing software security expertise to development, QA, and operations teams. Security champions can act as a sounding board for new projects, and in new or fast-moving technology areas, help combine software security skills with domain knowledge that might be under-represented in security or engineering teams. Agile coaches, scrum masters, and DevOps engineers can make particularly useful security champions, especially for detecting and removing process friction.

![Chart showing the following: Inadequate/ineffective security training for developers/engineers 33.9%, Shortage of application security personnel/skills 31.4%, Lack of transparency into development/operations work 31.3%, Continuously changing requirements and priorities 30.4%, Organizational silos between development, operations, security 29.1%, Insufficient budget/funding for security programs and tools 29.4%, Lack of coding skills in security teams 29.0%]
Figure K What are the challenges/barriers in implementing DevSecOps at your organization? (Select all that apply)

![Chart showing the following: Tool(s) do not prioritize resolution based on exposure, exploitability, and criticality 34.7%, No way to consolidate/correlate results from different tools 29.0%, Too slow to fit into rapid release cycles/continuous deployment 34.1%, There are no major issues 3.1%, Cost vs. ROI 33.5%, Inaccuracy/unreliability 33.1%, High number of false positives 32.2%]
Figure L What are the major issues with the application security testing tools used in your organization? (Select up to 3)

As noted earlier in this report, AST tools such as SAST, DAST, IAST, and SCA are all widely used by respondents, but effectively aligning those tools to business needs remains a challenge (Figure L).

Many respondents complained that the security testing tools they use do not prioritize resolution based on such factors as exposure, exploitability, and criticality; are too slow to fit into continuous deployment release cycles; and are inaccurate and unreliable.

With no way to consolidate or correlate results from different security tests, security and DevOps teams spend too much time determining what needs to be fixed first—probably one of the reasons why nearly three-quarters of respondents noted that their organizations can take anywhere from two weeks to a month to patch known critical vulnerabilities (Figure I).

Failure to patch quickly affects the bottom line. More than 80% of respondents said that dealing with critical vulnerabilities or related security issues of deployed software impacted their delivery schedules during 2022-23 (Figure J).

The problems of fragmented AST tools and slow remediation are precisely what application security orchestration and correlation (ASOC) and application security posture management (ASPM) are designed to address. Gartner notes that ASOC/ASPM acts as a management layer to orchestrate multiple AST tools, automatically correlating and contextualizing findings to accelerate and focus remediation.

By ingesting results from diverse sources and providing a unified view of risk across the application landscape, ASOC/ASPM enables data-driven prioritization based on business context like criticality and facilitates faster patching of the highest-risk vulnerabilities. By providing visibility into production environments, ASOC/ASPM closes the gap between lengthy remediation times for deployed applications and the reality that most exploits appear within days.

### Promises and pitfalls of AI
These survey results demonstrate that AI use is already deeply embedded in many organizations’ software security initiatives, with over 50% of respondents indicating that they are actively using AI in their DevSecOps practices. Fifty-four percent expect AI to improve the efficiency and accuracy of their security measures. Forty-eight percent hope that AI will help reduce manual review of security testing.

This makes sense when you consider the major advantages AI could potentially provide for DevSecOps. AppSec teams are constantly caught between the need to perform complete and consistent security testing and the need to keep pace with development teams using DevOps methodologies and CI pipelines. When deadlines are tight, it’s easy for developers to skip key security risk–assessment procedures.

Survey respondents cited “improve accuracy and efficiency of security measures” (54%) and “reduce the need for manual review and analysis of security data” (48%) as two major benefits they anticipate from introducing AI into the secure SDLC.

Note that respondents also said, however, that they expected AI to “increase the complexity and technical requirements of software security,” perhaps anticipating that at some future point, the only entities capable of adequately reviewing AI-generated code may be AI itself.

![Chart showing the following: Yes, we are actively using AI tools 52.5%, No, we are open to the use of AI tools, but have not yet implemented them 36.5%, No, we have not implemented AI tools, and have no plans to do so 11.0%, No (Net) 47.5%]
Figure M Are you currently using any AI tools to enhance your software security measures?

![Chart showing the following: Improve efficiency and accuracy of security measures 53.7%, Reduce the need for manual review and analysis of security data 48.4%, Increase the complexity and technical requirements of software security 52.0%, Have no significant impact 0.9%]
Figure N How do you expect the use of AI tools to impact your DevSecOps processes and workflows? (Select all that apply)

Implementing AI in DevSecOps comes with additional challenges, such as ensuring data quality and addressing security and privacy concerns. As AI tools are more integrated into the DevOps pipeline, they will almost certainly become key targets for security threats. The handling of sensitive data used for AI training can raise privacy issues as well.

One scenario that illustrates potential risks of AI in action is the use of AI-assisted coding, which is generating questions around ownership, copyright, and licensing of the AI-created code.

In late 2022, a class-action lawsuit was filed against GitHub, Microsoft, and OpenAI, claiming that GitHub Copilot—a cloud-based AI tool that offers developers autocomplete-style suggestions as they code—violates both copyright law and software licensing requirements, as well as the rights of the developers whose open source code the Copilot service is trained on. The lawsuit further claims that the code suggested by Copilot uses licensed materials without attribution, copyright notice, or adherence to the original licensing terms.

![Chart showing the following: Threat detection and prevention 45.1%, Vulnerability scanning and testing 44.2%, Identity and access management 42.0%, Compliance and regulation management 41.6%]
Figure O What specific areas of software security do you believe AI tools could be most effective in enhancing?

Large language model–based generative AI chatbots such as ChatGPT and Google Bard also have the problem of randomly producing “hallucinations,” false responses that may seem credible and confident but are not true—in lay terms, a “lie.”

AI hallucinations are a clear danger to software supply chain security. Researchers have found that ChatGPT may recommend a hallucinatory nonexistent code library or package. A malicious actor could create a package with the same name, fill it with malicious code, and then distribute it to unsuspecting developers who follow the AI’s recommendations. This could be a game-changer for cybercriminals, allowing them to sidestep more traditional and easily detectable techniques such as typosquatting or masquerading. In fact, the researchers discovered malicious packages created through ChatGPT’s hallucinatory recommendations already on popular package installers like PyPI and npm.

That threat isn’t theoretical; it’s real and happening right now. Whether defending against supply chain attacks originating from AI hallucinations or malicious actors, it’s crucial to know your code’s origin, authenticate developers and maintainers, and only download from reliable vendors or sources.

![Chart showing the following: Not concerned (Net) 7.2%, Not concerned at all 1.2%, Neutral/undecided 16.2%, Not very concerned 6.0%, Somewhat concerned 51.3%, Very concerned 25.4%, Concerned (Net) 76.6%]
Figure P How concerned, if at all, are you about potential bias or errors in AI-based security solutions?

## Lessons Learned
While most organizations have largely adopted some level of DevSecOps practices, they continue to face barriers to its effective implementation. Two major problem areas emerged from the survey.
- Integrating and aligning the results of multiple application security testing (AST) tools to meet business priorities
- Reducing the time needed to resolve critical vulnerabilities

Twenty-eight percent of respondents said their organizations take as much as three weeks to patch critical security