# 2024 The State of Open Source Report

## Table of Contents
- [How frequently does your organization ship code?](#how-frequently-does-your-organization-ship-code)
- [Section 1: Slowing progress in OSS security efforts and signs of AppSec exhaustion](#section-1-slowing-progress-in-oss-security-efforts-and-signs-of-appsec-exhaustion)
- [Signs of Application Security Exhaustion](#signs-of-application-security-exhaustion)
- [Clear Declines in Resources Dedicated to Supply Chain Security](#clear-declines-in-resources-dedicated-to-supply-chain-security)
- [Less than a day](#less-than-a-day)
- [52% Fail to Meet Stated SLAs for High-Severity Vulnerability Fixes](#52-fail-to-meet-stated-slas-for-high-severity-vulnerability-fixes)
- [Teams Auditing Code Less Frequently and Less Continuously](#teams-auditing-code-less-frequently-and-less-continuously)
- [Big Increase In Using Tools That Analyze Package Security](#big-increase-in-using-tools-that-analyze-package-security)
- [Section 2: Supply Chain Security Remains Immature](#section-2-supply-chain-security-remains-immature)
- [How have you or your organization been impacted by an open source or supply chain security vulnerability in the past year?](#how-have-you-or-your-organization-been-impacted-by-an-open-source-or-supply-chain-security-vulnerability-in-the-past-year)
- [What security practices do you use?](#what-security-practices-do-you-use)
- [Where are security tools integrated?](#where-are-security-tools-integrated)
- [LankeofeMa ur yeaiieSopt s na oie ieR skeVulihrab yeAialys s](#lankeofema-ur-yeaiiesopt-s-na-oie-ie-r-skevulihrab-ye-aialys-s)
- [Shn oie3:eCoi iuhieM splanhieCoifihinhe ie theShnur yeofeAQOghihra hieCoih](#shn-oie3-ecoi-iuhie-m-splanhie-coifihinhe-ie-theshnur-yeofe-aqo-ghihra-hie-coih)
- [Comparison of Critical/High Severity Time-to-Fix in OSS](#comparison-of-criticalhigh-severity-time-to-fix-in-oss)
- [Section 4: Evidence of General Open Source Security Progress](#section-4-evidence-of-general-open-source-security-progress)
- [Conclusion](#conclusion)
- [Methodology](#methodology)

The official report URL is: https://snyk.io/blog/2024-open-source-security-report-slowing-progress-and-new-challenges-for/

# 2024 The State of Open Source Report

## How frequently does your organization ship code?

**Dependency Tracking and Code Ship Frequency Unchanged**

The percentage of respondents that track all dependencies rather than just direct only increased slightly year-over-year. Roughly one-quarter of respondents still only track direct dependencies. Nearly 5% don’t track open source dependencies at all, although the majority of those who do not track do run software composition analysis (SCA). This implies that tracking may not be systematic but they do check dependencies and open source components.

No change in code ship frequency means we find ourselves at a plateau with existing DevOps and deploy methodologies and that organizations are hitting a wall. In theory, reduced friction from improved tooling and Developer Experience should facilitate faster code iteration. In practice, this does not appear to be happening, likely due to AppSec exhaustion.

**Does your company track which open source libraries your applications are using?**

*   **2023:**
    *   We track direct dependencies only: 25.5%
    *   We track all our dependencies — direct and indirect: 66.8%
    *   No, we don’t: 5.7%
    *   Not sure: 2%
*   **2024:**
    *   We track direct dependencies only: 24.6%
    *   We track all our dependencies — direct and indirect: 67.7%
    *   No, we don’t: 4.6%
    *   Not sure: 1.1%

**Code Ship Frequency**

*   **2023:**
    *   Daily: 33.2%
    *   Weekly: 41.3%
    *   Monthly: 13.1%
    *   Quarterly: 3.5%
    *   Don’t know: 0.1%
*   **2024:**
    *   Daily: 29.5%
    *   Weekly: 52%
    *   Monthly: 14.8%
    *   Quarterly: 3.1%
    *   Don’t know: 0.2%

---

## Section 1: Slowing progress in OSS security efforts and signs of AppSec exhaustion

There are signs of slowing progress in OSS security efforts and in DevOps efforts more broadly. Across many questions about supply chain security, we saw either little change year-over-year or surprising declines in adoption and usage.

### Signs of Application Security Exhaustion

Signs of application security (AppSec) “exhaustion” are growing, with teams overwhelmed by AppSec requirements and struggling to adopt them. None of the eight AppSec methods surveyed exceeded 70% usage — even SCA (69.7%) and SAST (59.5%) fell short. Four methods — license scanning, secrets scanning, supply chain security, and dependency analysis — were below 50%, with license and secrets scanning under 40%. Year-over-year respondents reported declines in usage of several application security processes. These declines run counter to numerous reports that highlight a significant overall increase in application security tool spending, which likely represents that organizations that have advanced in their use of these tools are expanding their use.

**Which of the following application security processes does your organization apply?**

*   Software Composition Analysis (SCA):
    *   2023: 65.6%
    *   2024: 69.7%
*   Static Code Analysis / Static Application Security Testing (SAST):
    *   2023: 62.1%
    *   2024: 59.5%
*   Dependency Analysis:
    *   2023: 51.4%
    *   2024: 49.6%
*   License Scanning:
    *   2023: 40.4%
    *   2024: 38.9%
*   Secrets Scanning:
    *   2023: 34.6%
    *   2024: 32.1%
*   Configuration Checks:
    *   2023: 58.4%
    *   2024: 53.5%
*   None of the above:
    *   2023: 3.5%
    *   2024: 0.4%

### Clear Declines in Resources Dedicated to Supply Chain Security

Compared to our research last year, we saw a marked decrease in proactive security measures from 2023 to 2024. The percentage of organizations implementing new tooling and practices to address supply chain vulnerabilities dropped from 60.9% in 2023 to 49.6% in 2024. Similarly, those investing in training their development teams on supply chain vulnerabilities decreased from 53.2% to 35.4% even though more than 40% of respondents indicated that they had to patch or replace vulnerable or malicious packages or build components. These reductions suggest that organizations may be feeling overwhelmed or fatigued by the continuous pressure of supply chain security demands, leading to reduced commitment to preventive actions. This may indicate fatigue, as some may opt to disengage rather than continually invest in complex and evolving security requirements.

**How have you or your organization been impacted by an open source or supply chain security vulnerability in the past year?**

*   We had to patch or replace one or more open sources libraries that were vulnerable or malicious:
    *   2023: 60.9%
    *   2024: 49.6%
*   We had to patch or replace one or more build components that were vulnerable or malicious:
    *   2023: 53.2%
    *   2024: 35.4%
*   We implemented new tooling and practices to better handle supply chain vulnerabilities:
    *   2023: 45.4%
    *   2024: 42.7%
*   We trained our development team to help them better understand supply chain vulnerabilities:
    *   2023: 12.4%
    *   2024: 12.6%
*   We have not been impacted by open source software supply chain vulnerabilities in the past year:
    *   2023: 0%
    *   2024: 0%

### Less than a day

*   Less than a day: 21.7%
*   Less than a week: 52.4%
*   Less than a month: 18.1%
*   More than a month: 6.6%
*   Never: 9.7%
*   Rarely: 36.9%
*   Sometimes: 37.2%
*   Don’t have one: 1.1%
*   Don’t know: 1.3%

### 52% Fail to Meet Stated SLAs for High-Severity Vulnerability Fixes

Widespread failure to meet vulnerability mitigation SLAs further highlights AppSec fatigue. Teams struggle to meet these goals, suggesting unrealistic expectations. While 74% have SLAs of a week or less, and 25% a day or less, 52% regularly miss these targets, and 14.8% frequently fail to meet them.

**What is your SLA policy for fixing high-severity vulnerabilities?**

*   Less than a day: 25%
*   Less than a week: 49%
*   Less than a month: 18%
*   More than a month: 6%
*   Don't have one: 1%
*   Don't know: 1%

**How often do you break your vulnerability SLA?**

*   Frequently: 14.8%
*   Regularly: 37.2%
*   Rarely: 36.9%
*   Never: 9.7%
*   Don't know: 1.3%

### Teams Auditing Code Less Frequently and Less Continuously

Between 2023 and 2024, there was a noticeable shift toward less frequent code auditing among teams. The percentage of teams auditing code weekly increased from 29% in 2023 to 36.9% in 2024, while continuous auditing through automation decreased from 27% to 22.3%. Additionally, monthly audits saw an increase from 10.1% to 14.6%, indicating a trend toward less frequent and less continuous auditing practices.

**How Often Do You Audit Your Code?**

*   Continuously through automation:
    *   2023: 27%
    *   2024: 22.3%
*   Daily:
    *   2023: 28%
    *   2024: 22.3%
*   Weekly:
    *   2023: 29%
    *   2024: 36.9%
*   Monthly:
    *   2023: 10.1%
    *   2024: 14.6%
*   Less frequently:
    *   2023: 4%
    *   2024: 2.7%
*   Don't know:
    *   2023: 2%
    *   2024: 1.1%

### Big Increase In Using Tools That Analyze Package Security

Reliance on tools for package security rose 22.3% YoY, with an 11% drop in manual approaches like checking registry information. This shift may reflect either a proactive move toward automation or a need to manage OSS-related security burdens as teams rely increasingly on tools for package safety analysis.

**How do you check the safety of the open source packages used by your software?**

*   I use the information in the registry or package manager:
    *   2023: 65.8%
    *   2024: 63.7%
*   I use a tool that analyzes package security:
    *   2023: 40.8%
    *   2024: 63.7%
*   I look at repository ratings or package download statistics:
    *   2023: 54%
    *   2024: 48.8%
*   I look at the frequency of releases/commits/etc.:
    *   2023: 42.5%
    *   2024: 57.5%
*   I check that the project has an active, responsive community:
    *   2023: 44.2%
    *   2024: 44.5%
*   I check that the project has a responsible disclosure policy (e.g., a SECURITY.md):
    *   2023: 34.2%
    *   2024: 33.4%
*   I check the OpenSSF security scorecard or similar security health scorecards:
    *   2023: 3%
    *   2024: 0.9%
*   I don't check the safety of open source packages:
    *   2023: 0%
    *   2024: 0%

---

## Section 2: Supply Chain Security Remains Immature

Security practices in OSS supply chains lack maturity, with most measures under-adopted and inadequate to meet evolving threats.

Open source supply chain security remains lightly adopted, with no practice used by more than two-thirds of organizations. SBOM monitoring leads at 62%, and only software pipeline security also surpasses 50% usage. Just 44% verify SBOMs pre-deployment, 41% check for signed artifacts, and only around 20% use protections like reproducible builds or branch protection. This leaves build pipelines vulnerable, as many rely on outdated scanning and lag in adopting cloud-native security.

**Which supply chain security practices does your organization follow?**

*   SBOM creation: 43.8%
*   SBOM monitoring: 62.4%
*   SBOM enrichment: 47.4%
*   Package attestation/verification: 47.6%
*   Artifact signing: 36.7%
*   SBOM verification pre-deploy: 44.9%
*   Software pipeline security: 57.5%
*   Reproducible builds: 23.7%
*   Branch protection: 20.7%

**How have you or your organization been impacted by an open source or supply chain security vulnerability in the past year?**

*   We implemented new tooling and practices to better handle supply chain vulnerabilities:
    *   2023: 60.9%
    *   2024: 49.6%
*   We trained our development team to help them better understand supply chain vulnerabilities:
    *   2023: 53.2%
    *   2024: 35.4%

**What security practices do you use?**

*   Software Composition Analysis (SCA):
    *   2023: 65.6%
    *   2024: 69.7%
*   Static Code Analysis / Static Application Security Testing (SAST):
    *   2023: 62.1%
    *   2024: 59.5%
*   Secrets scanning:
    *   2023: 34.6%
    *   2024: 32.1%
*   Dynamic Application Security Tools (DAST):
    *   2023: 29%
    *   2024: 55.5%
*   Infrastructure as Code scanning (IaC):
    *   2023: 50.4%
    *   2024: 33.6%
*   Container image scanning:
    *   2023: 27.7%
    *   2024: 35.7%
*   Reproducible builds:
    *   2023: 20.7%
    *   2024: 20.7%
*   None of the above:
    *   2023: 0.7%
    *   2024: 0.4%

Despite the maturity of SCA and Static Application Security Testing (SAST), adoption is still just over 60%, with container scanning surprisingly low at 35%. Reproducible builds and secrets scanning are around 20%, although supply chain vulnerabilities continue impacting both code and build components. As seen in the previous section, between 2023 and 2024, new tooling adoption went from 61% to 50%, while security training went from 53% to 35%, even as vulnerabilities rose. In 2024, 45% replaced compromised build components, and 42% swapped vulnerable OSS libraries.

**Where are security tools integrated?**

*   IDE:
    *   2023: 40.7%
    *   2024: 40.8%
*   CLI:
    *   2023: 23.7%
    *   2024: 27.5%
*   Build System:
    *   2023: 54%
    *   2024: 65.6%
*   Pre-Commit Checks:
    *   2023: 33.6%
    *   2024: 41.5%
*   Code Repository:
    *   2023: 56%
    *   2024: 66.3%
*   CI/CD pipeline:
    *   2023: 38.7%
    *   2024: 45%
*   Don’t know:
    *   2023: 0.4%
    *   2024: 4%

### LankeofeMa ur yeaiieSopt s na oie ieR skeVulihrab yeAialys s

When determining how severe a vulnerability risk is, the most widely used approaches are traditional scoring systems (CVSS, exploit prediction scoring system (EPSS)). Far less widely used are measures that reflect the actual risk of a vulnerability to an organization (reachability, deployment status, business context). Teams are still struggling to adopt more relevant vulnerability severity rating systems. This implies that they are still struggling to effectively triage vulnerabilities and build risk models that accurately reflect the true business risk of vulnerabilities.

**What factors do you use to determine the severity of a vulnerability?**

*   CVSS severity as supplied by Mitre, etc (Critical, High, Medium, Low): 47.8%
*   Internally calculated CVSS score: 47.8%
*   Exploit prediction scoring system: 43.1%
*   Social media / hacking site chatter: 38.7%
*   Exploit maturity: 35.8%
*   Package health measures (maintenance, popularity, etc): 39.4%
*   Reachability: 33.8%
*   Package age: 25.9%
*   Business context (mission critical, sensitive data access, etc): 35%
*   Deployment status: 25.2%

---

### Shn oie3:eCoi iuhieM splanhieCoifihinhe ie theShnur yeofeAQOghihra hieCoih

High confidence in AI for secure code persists, despite evidence of vulnerabilities, signaling a need for better education on AI risks.

Respondents continued to hold high levels of misplaced confidence in the ability of AI tools to generate secure code. Despite 77.9% of respondents believing AI has improved code security (up slightly from 76.5% last year), Snyk’s research shows frequent, serious vulnerabilities in AI-generated code. Meanwhile, 56.7% remain concerned about vulnerabilities introduced by AI — a modest decline in worry, with 38.1% now expressing little or no concern. This disconnect highlights an education gap, as many organizations may be overly trusting of AI's security capabilities. On the positive side, 84.1% of respondents apply the same scrutiny to open source components recommended by AI as they do to human-suggested components, reflecting a mature approach. However, confidence in AI's security contributions remains unaligned with actual risks, emphasizing the need for consistent oversight to prevent a false sense of security as AI adoption grows.

**Respondents said AI improved code security and did not introduce vulnerabilities**

*   Yes: 77.9%
*   No: 11.6%
*   Don’t know: 11.5%

**Are you concerned that using AI coding tools will introduce security vulnerabilities into your applications?**

*   Yes: 56.7%
*   No: 34.5%
*   Don’t know: 6%
*   N/A: 2.7%

**Are you concerned that using AI coding tools will introduce open source licensing and copyright problems into your stack?**

*   Yes: 84.1%
*   No: 11.5%
*   Don’t know: 4.4%

**Do you apply the same scrutiny to open source packages and libraries suggested by AI as those suggested by humans?**

*   Yes: 84.1%
*   No: 11.5%
*   Don’t know: 4.4%

**How many vulnerabilities has AI introduced into your code?**

*   A lot: 40.8%
*   A moderate amount: 32.7%
*   Very few: 13.7%
*   None: 3.7%
*   Don’t know: 6.7%

---

### Comparison of Critical/High Severity Time-to-Fix in OSS

Even as we see evidence of AppSec exhaustion and slow adoption of supply chain security practices, the open source software (OSS) community has made significant progress in a critical measure reducing the time it takes to fix high and critical severity vulnerabilities present in open source software projects. Over recent years, OSS has consistently shortened its "time-to-fix" for critical bugs, outpacing proprietary software in responsiveness. OSS is also improving time-to-fix across open source projects across popular languages from 2022-2023 and 2023-2024, with a clear reduction in resolution times. These improvements underscore the community's dedication to enhancing security and responsiveness, demonstrating the effectiveness of collaborative, transparent approaches in addressing vulnerabilities quickly at the level of project and project code.

**Time-to-Fix of High/Critical Severity Bugs: OSS vs Proprietary**

*   **OSS:**
    *   2019: 296 days
    *   2020: 287 days
    *   2021: 283 days
    *   2022: 246 days
    *   2023: 220 days
    *   2024: 189 days
*   **Proprietary:**
    *   2019: 137 days
    *   2020: 274 days
    *   2021: 173 days
    *   2022: 154 days
    *   2023: 112 days
    *   2024: 122 days

**Time-to-Fix of High/Critical Severity Bugs: OSS vs Proprietary (by language/ecosystem)**

*   **swift:**
    *   2022-2023: 437 days
    *   2023-2024: 79 days
*   **python:**
    *   2022-2023: 91 days
    *   2023-2024: 68 days
*   **js:**
    *   2022-2023: 166 days
    *   2023-2024: 136 days
*   **java:**
    *   2022-2023: 138 days
    *   2023-2024: 129 days
*   **go:**
    *   2022-2023: 32 days
    *   2023-2024: 33 days
*   **elixir:**
    *   2022-2023: 30 days
    *   2023-2024: 38 days
*   **dotnet:**
    *   2022-2023: 23 days
    *   2023-2024: 59 days
*   **cpp:**
    *   2022-2023: 21 days
    *   2023-2024: 16 days
*   **alpine:**
    *   2022-2023: 7 days
    *   2023-2024: 9 days

---

## Section 4: Evidence of General Open Source Security Progress

The OSS community has significantly reduced time-to-fix for critical and high severity vulnerabilities in open source projects and continues to outperform proprietary software in response times based on vulnerability database findings.

---

## Conclusion

### Room for Improvement in Supply Chain, AppSec with Progress in General OSS Code

The findings from our 2024 research paint a concerning picture of an industry struggling to maintain momentum in security practices while facing evolving challenges. The observed "AppSec exhaustion" phenomenon, evidenced by declining engagement in security measures and widespread failure to meet vulnerability management goals, suggests that current approaches to security may be unsustainable. Encouragingly, we did identify signs of ongoing improvement in the underlying foundations of open source software, with projects turning critical fixes around more quickly and the open source community continuing to distance itself from proprietary code in terms of speed of fixes.

The immaturity of supply chain security practices, combined with decreasing investment in proactive security measures, creates a particularly vulnerable environment. This vulnerability is potentially exacerbated by the industry's overreliance on AI-generated code security. While AI tools offer promising capabilities for code generation, the disconnect between perceived and actual security risks — with 77.9% of respondents expressing confidence despite evidence of serious vulnerabilities — suggests a dangerous trend that could lead to significant security oversights.

Moving forward, organizations need to:

*   Reassess their approach to security to prevent burnout and ensure sustainable practices.
*   Improve prioritization in vulnerability management and other supply chain risk management tasks.
*   Prioritize the adoption of fundamental supply chain security measures and deploy newer supply chain security measures to improve security posture.
*   Include more holistic risk analysis as part of SCA determination to ensure security teams can focus more time on risks that matter.
*   Take a more cautious and measured approach to AI-generated code, implementing rigorous security reviews rather than assuming inherent security.
*   Establish clear guidelines for validating and testing AI-generated code, treating it with the same or greater scrutiny as human-written code.

These findings suggest that the industry must find new ways to balance security requirements with team capacity while maintaining vigilance against emerging threats, including those potentially introduced by overreliance on AI tools. Without addressing these challenges and adjusting attitudes toward AI-generated code security, organizations risk falling further behind in their security posture as threats continue to evolve.

## Methodology

We surveyed 453 technologists across application development and security. We used many of the same questions we had asked in the 2023 State of Open Source Security in 2023 and compared to the past results, where applicable. Respondents were located in the United States of America, Canada, and the United Kingdom. The question types included binary responses (only one answer allowed), multi-picks (choose all that apply), and ratings on a scale of 1 to 4, with 1 being *most concerning*. Respondents came from a wide variety of sectors, including automotive, business services, communications, education, energy and utilities, entertainment/media, financial services, government, and SaaS technology.