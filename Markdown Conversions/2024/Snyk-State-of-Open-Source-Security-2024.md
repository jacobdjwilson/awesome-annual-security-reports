# The state of open source

## Table of Contents
- [Section 1: Slowing progress in OSS security efforts and signs of AppSec exhaustion](#section-1-slowing-progress-in-oss-security-efforts-and-signs-of-appsec-exhaustion)
- [Section 2: Supply Chain Security Remains Immature](#section-2-supply-chain-security-remains-immature)
- [Section 3: Confidence in AI for Secure Code](#section-3-confidence-in-ai-for-secure-code)
- [Section 4: Evidence of General Open Source Security Progress](#section-4-evidence-of-general-open-source-security-progress)
- [Conclusion](#conclusion)
- [Methodology](#methodology)

## Section 1: Slowing progress in OSS security efforts and signs of AppSec exhaustion
There are signs of slowing progress in OSS security efforts and in DevOps efforts more broadly. Across many questions about supply chain security, we saw either little change year-over-year or surprising declines in adoption and usage.

### Depennency Toacking ann Cone Ship Foequency Unchangen
The percentage of respondents that track all dependencies rather than just direct only increased slightly year-over-year. Roughly one-quarter of respondents still only track direct dependencies. Nearly 5% don’t track open source dependencies at all, although the majority of those who do not track do run software composition analysis (SCA). This implies that tracking may not be systematic but they do check dependencies and open source components. No change in code ship frequency means we find ourselves at a plateau with existing DevOps and deploy methodologies and that organizations are hitting a wall. In theory, reduced friction from improved tooling and Developer åxperience should facilitate faster code iteration. In practice, this does not appear to be happening, likely due to AppSec exhaustion.

![Chart showing the percentage of respondents tracking open source libraries, with categories for "No, we don't", "We track direct dependencies only", "We track all our dependencies — direct and indirect", and "Not sure", for 2023 and 2024.]

**Does your company track which open source libraries your applications are using?**
- 2023:
  - No, we don’t: 5.7%
  - We track direct dependencies only: 25.5%
  - We track all our dependencies — direct and indirect: 66.8%
  - Not sure: 2%
- 2024:
  - No, we don’t: 4.6%
  - We track direct dependencies only: 24.6%
  - We track all our dependencies — direct and indirect: 67.7%
  - Not sure: 1.1%

![Chart showing how frequently organizations ship code, with categories for "Daily", "Weekly", "Monthly", "Quarterly", and "Don't know", for 2023 and 2024.]

**How frequently does your organization ship code?**
- 2023:
  - Daily: 33.2%
  - Weekly: 41.3%
  - Monthly: 13.1%
  - Quarterly: 3.5%
  - Don’t know: 0.9%
- 2024:
  - Daily: 29.1%
  - Weekly: 52%
  - Monthly: 14.8%
  - Quarterly: 3.1%
  - Don’t know: 0.2%

### Signs of Application Security Exhaustion
Signs of application security (AppSec) “exhaustion” are growing, with teams overwhelmed by AppSec requirements and struggling to adopt them. None of the eight AppSec methods surveyed exceeded 70% usage — even SCA (69.7%) and SAST (59.5%) fell short. Four methods — license scanning, secrets scanning, supply chain security, and dependency analysis — were below 50%, with license and secrets scanning under 40%. Year-over-year respondents reported declines in usage of several application security processes. These declines run counter to numerous reports that highlight a significant overall increase in application security tool spending, which likely represents that organizations that have advanced in their use of these tools are expanding their use.

![Chart showing the application security processes applied by organizations, with categories for "Software Composition Analysis (SCA)", "Static Code Analysis n Static Applications Security Testing (SAST)", "Dependency Analysis", "License Scanning", "Secrets ¤anagement", "Configuration Checks", and "None of the above", for 2023 and 2024.]

**Which of the following application security processes does your organization apply?**
- 2023:
  - Software Composition Analysis (SCA): 65.6%
  - Static Code Analysis n Static Applications Security Testing (SAST): 62.1%
  - Dependency Analysis: 51.9%
  - License Scanning: 40%
  - Secrets ¤anagement: 39.6%
  - Configuration Checks: 58.4%
  - None of the above: 3.5%
- 2024:
  - Software Composition Analysis (SCA): 69.7%
  - Static Code Analysis n Static Applications Security Testing (SAST): 59.5%
  - Dependency Analysis: 49.6%
  - License Scanning: 38.9%
  - Secrets ¤anagement: 32.1%
  - Configuration Checks: 53.5%
  - None of the above: 0.4%

### Clear Declines in Resources Dedicated to Supply Chain Security
Compared to our research last year, we saw a marked decrease in proactive security measures from 2023 to 2024. The percentage of organizations implementing new tooling and practices to address supply chain vulnerabilities dropped from 60.9% in 2023 to 49.6% in 2024. Similarly, those investing in training their development teams on supply chain vulnerabilities decreased from 53.2% to 35.4% even though more than 40% of respondents indicated that they had to patch or replace vulnerable or malicious packages or build components. These reductions suggest that organizations may be feeling overwhelmed or fatigued by the continuous pressure of supply chain security demands, leading to reduced commitment to preventive actions. This may indicate fatigue, as some may opt to disengage rather than continually invest in complex and evolving security requirements.

![Chart showing the impact of open source or supply chain security vulnerabilities, with categories for "We had to patch or replace one or more open sources libraries that were vulnerable or malicious*", "We had to patch or replace one or more build components that were vulnerable or malicious*", "We implemented new tooling and practices to better handle supply chain vulnerabilities", "We trained our development team to help them better understand supply chain vulnerabilities", and "We have not been impacted by open source software supply chain vulnerabilities in the past year", for 2023 and 2024.]

**How have you or your organization been impacted by an open source or supply chain security vulnerability in the past year?**
- 2023:
  - We implemented new tooling and practices to better handle supply chain vulnerabilities: 60.9%
  - We trained our development team to help them better understand supply chain vulnerabilities: 53.2%
  - We have not been impacted by open source software supply chain vulnerabilities in the past year: 12.4%
- 2024:
  - We had to patch or replace one or more open sources libraries that were vulnerable or malicious*: 45.4%
  - We had to patch or replace one or more build components that were vulnerable or malicious*: 42.9%
  - We implemented new tooling and practices to better handle supply chain vulnerabilities: 49.6%
  - We trained our development team to help them better understand supply chain vulnerabilities: 35.4%
  - We have not been impacted by open source software supply chain vulnerabilities in the past year: 12.6%

### 52% Fail to Meet Stated SLAs for High-Severity Vulnerability Fixes
Widespread failure to meet vulnerability mitigation SLAs further highlights AppSec fatigue. Teams struggle to meet these goals, suggesting unrealistic expectations. While 74% have SLAs of a week or less, and 25% a day or less, 52% regularly miss these targets, and 14.8% frequently fail to meet them.

![Chart showing SLA policies for fixing high-severity vulnerabilities and how often those SLAs are broken.]

**What is your SLA policy for fixing high-severity vulnerabilities?**
- Less than a day: 21.7%
- Less than a week: 52.4%
- Less than a month: 18.1%
- More than a month: 6.6%
- Don’t have one: 1.1%
- Don’t know: 1.3%

**How often do you break your vulnerability SLA?**
- Often: 14.8%
- Sometimes: 37.2%
- Rarely: 36.9%
- Never: 9.7%

### Teams Auditing Code Less Frequently and Less Continuously
Between 2023 and 2024, there was a noticeable shift toward less frequent code auditing among teams. The percentage of teams auditing code weekly increased from 29% in 2023 to 36.9% in 2024, while continuous auditing through automation decreased from 27% to 22.3%. Additionally, monthly audits saw an increase from 10.1% to 14.6%, indicating a trend toward less frequent and less continuous auditing practices.

![Chart showing how often teams audit code, with categories for "Continuously through automation", "Daily", "Weekly", "Monthly", "Less frequently", and "Don't know", for 2023 and 2024.]

**How Often Do You Audit Your Code?**
- 2023:
  - Continuously through automation: 27%
  - Daily: 28%
  - Weekly: 29%
  - Monthly: 10.1%
  - Less frequently: 4%
  - Don't know: 2%
- 2024:
  - Continuously through automation: 22.3%
  - Daily: 22.3%
  - Weekly: 36.9%
  - Monthly: 14.6%
  - Less frequently: 2.7%
  - Don't know: 1.1%

### Big Increase In Using Tools That Analyze Package Security
Reliance on tools for package security rose 22.3% YoY, with an 11% drop in manual approaches like checking registry information. This shift may reflect either a proactive move toward automation or a need to manage OSS-related security burdens as teams rely increasingly on tools for package safety analysis.

![Chart showing how organizations check the safety of open source packages, with categories for "I use the information in the registry or package manager", "I use a tool that analyzes package security", "I look at repository ratings or package download statistics", "I look at the frequency of releases/commits/etc.", "I check that the project has an active, responsive community", "I check that the project has a responsible disclosure policy dsuch as a Shl\RI]Z.mda", "I check the OpenSS security scorecard or similar security health scorecards", and "I don’t check the safety of open source packages.", for 2023 and 2024.]

**How do you check the safety of the open source packages used by your software?**
- 2023:
  - I use the information in the registry or package manager: 65.8%
  - I use a tool that analyzes package security: 40.8%
  - I look at repository ratings or package download statistics: 48.8%
  - I look at the frequency of releases/commits/etc.: 51.5%
  - I check that the project has an active, responsive community: 45.5%
  - I check that the project has a responsible disclosure policy dsuch as a Shl\RI]Z.mda: 34.2%
  - I check the OpenSS security scorecard or similar security health scorecards: 3%
  - I don’t check the safety of open source packages.: 0.9%
- 2024:
  - I use the information in the registry or package manager: 54%
  - I use a tool that analyzes package security: 63.1%
  - I look at repository ratings or package download statistics: 42.5%
  - I look at the frequency of releases/commits/etc.: 44.2%
  - I check that the project has an active, responsive community: 44.5%
  - I check that the project has a responsible disclosure policy dsuch as a Shl\RI]Z.mda: 33.4%
  - I check the OpenSS security scorecard or similar security health scorecards: 0.9%
  - I don’t check the safety of open source packages.: 0.9%

## Section 2: Supply Chain Security Remains Immature
Security practices in OSS supply chains lack maturity, with most measures under-adopted and inadequate to meet evolving threats.

Open source supply chain security remains lightly adopted, with no practice used by more than two-thirds of organizations. SBOM monitoring leads at 62%, and only software pipeline security also surpasses 50% usage. Just 44% verify SBOMs pre-deployment, 41% check for signed artifacts, and only around 20% use protections like reproducible builds or branch protection. This leaves build pipelines vulnerable, as many rely on outdated scanning and lag in adopting cloud-native security.

![Chart showing the supply chain security practices followed by organizations, with categories for "SBOM creation", "SBOM monitoring", "SBOM enrichment", "Package attestation/verification", "Artifact signing", "SBOM verification pre-deploy", "Software pipeline security", "Reproducible builds", and "Branch protection".]

**Which supply chain security practices does your organization follow?**
- SBOM creation: 43.8%
- SBOM monitoring: 62.4%
- SBOM enrichment: 41.4%
- Package attestation/verification: 41.6%
- Artifact signing: 36.1%
- SBOM verification pre-deploy: 44.9%
- Software pipeline security: 57.5%
- Reproducible builds: 21.9%
- Branch protection: 20.1%

![Chart showing where security tools are integrated, with categories for "IDE", "CLI", "Build System", "Pre-Commit Checks", "Code Repository", and "CI/CD pipeline", for 2023 and 2024.]

**Where are security tools integrated?**
- 2023:
  - IDE: 40.1%
  - CLI: 23.1%
  - Build System: 40.8%
  - Pre-Commit Checks: 33.6%
  - Code Repository: 56%
  - CI/CD pipeline: 38.9%
  - Don’t know: 0.4%
- 2024:
  - IDE: 40.8%
  - CLI: 28.9%
  - Build System: 54%
  - Pre-Commit Checks: 45%
  - Code Repository: 66.3%
  - CI/CD pipeline: 45%
  - Don’t know: 4%

![Chart showing the impact of open source or supply chain security vulnerabilities, with categories for "We implemented new tooling and practices to better handle supply chain vulnerabilities" and "We trained our development team to help them better understand supply chain vulnerabilities", for 2023 and 2024.]

**How have you or your organization been impacted by an open source or supply chain security vulnerability in the past year?**
- 2023:
  - We implemented new tooling and practices to better handle supply chain vulnerabilities: 60.9%
  - We trained our development team to help them better understand supply chain vulnerabilities: 53.2%
- 2024:
  - We implemented new tooling and practices to better handle supply chain vulnerabilities: 49.6%
  - We trained our development team to help them better understand supply chain vulnerabilities: 35.4%

![Chart showing the security practices used by organizations, with categories for "Software Composition Analysis (SCA)", "Static Code Analysis Ê Static Application Security Testing (SAST)", "Secrets scanning", "Dynamic Application Security Tools (DAST)", "Infrastructure as Code scanning (IaC)", "Container image scanning", "Reproducible builds", and "None of the above".]

**What security practices do you use?**
- Software Composition Analysis (SCA): 67.5%
- Static Code Analysis Ê Static Application Security Testing (SAST): 67.1%
- Secrets scanning: 29%
- Dynamic Application Security Tools (DAST): 55.5%
- Infrastructure as Code scanning (IaC): 50.4%
- Container image scanning: 33.6%
- Reproducible builds: 23.1%
- None of the above: 0.7%

Despite the maturity of SCA and Static Application Security Testing (SAST), adoption is still just over 60%, with container scanning surprisingly low at 35%. Reproducible builds and secrets scanning are around 20%, although supply chain vulnerabilities continue impacting both code and build components. As seen in the previous section, between 2023 and 2024, new tooling adoption went from 61% to 50%, while security training went from 53% to 35%, even as vulnerabilities rose. In 2024, 45% replaced compromised build components, and 42% swapped vulnerable OSS libraries.

One positive trend is the increased distribution of security tooling across development stages. Build systems and pre-commit checks saw notable increases (11.6% and 15.9%, respectively), emphasizing early vulnerability detection. Code repositories (10.3%), CI/CD pipelines (6.3%), and CLI tools (5.8%) also showed growth, while IDE integration slightly declined, suggesting a preference to reduce developer cognitive load by shifting security out of coding environments.

## Section 3: Confidence in AI for Secure Code
High confidence in AI for secure code persists, despite evidence of vulnerabilities, signaling a need for better education on AI risks.

Respondents continued to hold high levels of misplaced confidence in the ability of AI tools to generate secure code. Despite 77.9% of respondents believing AI has improved code security (up slightly from 76.5% last year), Snyk’s research shows frequent, serious vulnerabilities in AI-generated code. Meanwhile, 56.1% remain concerned about vulnerabilities introduced by AI — a modest decline in worry, with 38.1% now expressing little or no concern. This disconnect highlights an education gap, as many organizations may be overly trusting of AI’s security capabilities. On the positive side, 84.1% of respondents apply the same scrutiny to open source components recommended by AI as they do to human-suggested components, reflecting a mature approach. However, confidence in AI’s security contributions remains unaligned with actual risks, emphasizing the need for consistent oversight to prevent a false sense of security as AI adoption grows.

![Chart showing the use of AI code suggestion tools and concerns about vulnerabilities and licensing issues, for 2023 and 2024.]

**Has the use of AI code suggestion tools, like improved your organization’s code security?**
- 2023:
  - Yes: 76.5%
  - No: 11.6%
  - Not sure: 11.5%
- 2024:
  - Yes: 77.9%
  - No: 11.6%
  - Not sure: 10.5%
  - We are not using AI code suggestion tools: 5%

**Are you concerned that using AI coding tools will introduce security vulnerabilities into your applications?**
- 2023:
  - Yes: 56.2%
  - No: 38.1%
  - Don’t know: 2.7%
  - N/A: 3.1%
- 2024:
  - Yes: 56.1%
  - No: 38.1%
  - Don’t know: 2.7%
  - N/A: 3.1%

**Are you concerned that using AI coding tools will introduce open source licensing and copyright problems into your stack?**
- Yes: 56.2%
- No: 34.5%
- Don’t know: 6%
- N/A: 2.7%

**Do you apply the same scrutiny to open source packages and libraries suggested by AI as those suggested by humans? coders?**
- Yes: 84.1%
- No: 11.5%
- Don’t know: 4.4%

…yet engineers and security teams remain concerned about AI introducing vulnerabilities in code or license and copyright issues….

…but teams are scrutinizing AI-suggested packages and libraries the same way as human-suggested packages, which is encouraging and implies they understand that AI suggestions present as much risk as human-suggested libraries and packages.

![Chart showing the number of vulnerabilities introduced into code by AI, with categories for "Very few", "A moderate amount", "A lot", "None", "Don't know", and "N/A", for 2023 and 2024.]

**How many vulnerabilities has AI introduced into your code?**
- 2023:
  - Very few: 32.7%
  - A moderate amount: 40.8%
  - A lot: 13.9%
  - None: 3.7%
  - Don’t know: 6.7%
  - N/A: 2.2%
- 2024:
  - Very few: 30.5%
  - A moderate amount: 43.4%
  - A lot: 12.8%
  - None: 5.5%
  - Don’t know: 4.2%
  - N/A: 3.5%

### Analysis
When determining how severe a vulnerability risk is, the most widely used approaches are traditional scoring systems (CVSS, exploit prediction scoring system (EPSS)). Far less widely used are measures that reflect the actual risk of a vulnerability to an organization (reachability, deployment status, business context). Teams are still struggling to adopt more relevant vulnerability severity rating systems. This implies that they are still struggling to effectively triage vulnerabilities and build risk models that accurately reflect the true business risk of vulnerabilities.

![Chart showing the factors used to determine the severity of a vulnerability, with categories for "CVSS severity as supplied by Mitre, etc (Critical, High, Medium, Low)", "Internally calculated CVSS score", "Exploit prediction scoring system", "Social media / hacking site chatter", "Exploit maturity", "Package health measures (maintenance, popularity, etc)", "Reachability", "Package age", "Business context (mission critical, sensitive data access, etc)", and "Deployment status".]

**What factors do you use to determine the severity of a vulnerability?**
- CVSS severity as supplied by Mitre, etc (Critical, High, Medium, Low): 47.8%
- Internally calculated CVSS score: 47.8%
- Exploit prediction scoring system: 43.1%
- Social media / hacking site chatter: 38.7%
- Exploit maturity: 35.8%
- Package health measures (maintenance, popularity, etc): 39.4%
- Reachability: 33.8%
- Package age: 25.9%
- Business context (mission critical, sensitive data access, etc): 35%
- Deployment status: 25.2%

## Section 4: Evidence of General Open Source Security Progress
The OSS community has significantly reduced time-to-fix for critical and high severity vulnerabilities in open source projects and continues to outperform proprietary software in response times based on vulnerability database findings.

![Chart showing the time-to-fix of high/critical severity bugs for OSS vs proprietary software from 2019 to 2024.]

**Time-to-Fix of High/Critical Severity Bugs: OSS vs Proprietary**
- 2019:
  - OSS: 296
  - Proprietary: 287
- 2020:
  - OSS: 137
  - Proprietary: 274
- 2021:
  - OSS: 173
  - Proprietary: 283
- 2022:
  - OSS: 189
  - Proprietary: 246
- 2023:
  - OSS: 154
  - Proprietary: 201
- 2024:
  - OSS: 112
  - Proprietary: 220

![Chart showing the time-to-fix of high/critical severity bugs for various open source languages from 2022-2023 and 2023-2024.]

**Time-to-Fix of High/Critical Severity Bugs by Language**
- 2022-2023
  - swift: 437
  - python: 198
  - js: 166
  - java: 138
  - go: 323
  - elixir: 0
  - dotnet: 235
  - cpp: 167
  - alpine: 87
- 2023-2024
  - swift: 79
  - python: 68
  - js: 136
  - java: 129
  - go: 133
  - elixir: 38
  - dotnet: 92
  - cpp: 116
  - alpine: 95

Even as we see evidence of AppSec exhaustion and slow adoption of supply chain security practices, the open source software (OSS) community has made significant progress in a critical measure reducing the time it takes to fix high and critical severity vulnerabilities present in open source software projects. Over recent years, OSS has consistently shortened its "time-to-fix" for critical bugs, outpacing proprietary software in responsiveness. OSS is also improving time-to-fix across open source projects across popular languages from 2022-2023 and 2023-2024, with a clear reduction in resolution times. These improvements underscore the community’s dedication to enhancing security and responsiveness, demonstrating the effectiveness of collaborative, transparent approaches in addressing vulnerabilities quickly at the level of project and project code.

Period -- 11/01/22-23  11/01/23-30

## Conclusion
Room for Improvement in Supply Chain, AppSec with Progress in General OSS Code

The findings from our 2024 research paint a concerning picture of an industry struggling to maintain momentum in security practices while facing evolving challenges. The observed "AppSec exhaustion" phenomenon, evidenced by declining engagement in security measures and widespread failure to meet vulnerability management goals, suggests that current approaches to security may be unsustainable. Encouragingly, we did identify signs of ongoing improvement in the underlying foundations of open source software, with projects turning critical fixes around more quickly and the open source community continuing to distance itself from proprietary code in terms of speed of fixes.

The immaturity of supply chain security practices, combined with decreasing investment in proactive security measures, creates a particularly vulnerable environment. This vulnerability is potentially exacerbated by the industry's overreliance on AI-generated code security. While AI tools offer promising capabilities for code generation, the disconnect between perceived and actual security risks — with 77.9% of respondents expressing confidence despite evidence of serious vulnerabilities — suggests a dangerous trend that could lead to significant security oversights.

Moving forward, organizations need to:
- Reassess their approach to security to prevent burnout and ensure sustainable practices.
- Improve prioritization in vulnerability management and other supply chain risk management tasks.
- Prioritize the adoption of fundamental supply chain security measures and deploy newer supply chain security measures to improve security posture.
- Include more holistic risk analysis as part of SeA determination to ensure security teams can focus more time on risks that matter.
- Take a more cautious and measured approach to AI-generated code, implementing rigorous security reviews rather than assuming inherent security.
- Establish clear guidelines for validating and testing AI-generated code, treating it with the same or greater scrutiny as human-written code.

These findings suggest that the industry must find new ways to balance security requirements with team capacity while maintaining vigilance against emerging threats, including those potentially introduced by overreliance on AI tools. Without addressing these challenges and adjusting attitudes toward AI-generated code security, organizations risk falling further behind in their security posture as threats continue to evolve.

## Methodology
We surveyed 453 technologists across application development and security. We used many of the same questions we had asked in the 2023 State of Open Source Security in 2023 and compared to the past results, where applicable. Respondents were located in the United States of America, Canada, and the United Kingdom. The question types included binary responses (only one answer allowed), multi-picks (choose all that apply), and ratings on a scale of 1 to 4, with 1 being *most concerning*. Respondents came from a wide variety of sectors, including automotive, business services, communications, education, energy and utilities, entertainment/media, financial services, government, and SaaS technology.
