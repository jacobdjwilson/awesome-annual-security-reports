# State of Open Source Security 2024

## Table of Contents
- [Section 1: Slowing progress in OSS security efforts and signs of AppSec exhaustion](#section-1-slowing-progress-in-oss-security-efforts-and-signs-of-appsec-exhaustion)
- [Section 2: Supply Chain Security Remains Immature](#section-2-supply-chain-security-remains-immature)
- [Section 3: Confidence in AI-Generated Code Outpaces Reality](#section-3-confidence-in-ai-generated-code-outpaces-reality)
- [Section 4: Evidence of General Open Source Security Progress](#section-4-evidence-of-general-open-source-security-progress)
- [Conclusion](#conclusion)
- [Methodology](#methodology)

---

## Section 1: Slowing progress in OSS security efforts and signs of AppSec exhaustion

There are signs of slowing progress in OSS security efforts and in DevOps efforts more broadly. Across many questions about supply chain security, we saw either little change year-over-year or surprising declines in adoption and usage.

### Dependency Tracking and Code Ship Frequency Unchanged
The percentage of respondents that track all dependencies rather than just direct only increased slightly year-over-year. Roughly one-quarter of respondents still only track direct dependencies. Nearly 5% don’t track open source dependencies at all, although the majority of those who do not track do run software composition analysis (SCA). This implies that tracking may not be systematic but they do check dependencies and open source components. No change in code ship frequency means we find ourselves at a plateau with existing DevOps and deploy methodologies and that organizations are hitting a wall. In theory, reduced friction from improved tooling and Developer Experience should facilitate faster code iteration. In practice, this does not appear to be happening, likely due to AppSec exhaustion.

![Chart: Does your company track which open source libraries your applications are using?]
![Chart: How frequently does your organization ship code?]

### Signs of Application Security Exhaustion
Signs of application security (AppSec) “exhaustion” are growing, with teams overwhelmed by AppSec requirements and struggling to adopt them. None of the eight AppSec methods surveyed exceeded 70% usage — even SCA (69.7%) and SAST (59.5%) fell short. Four methods — license scanning, secrets scanning, supply chain security, and dependency analysis — were below 50%, with license and secrets scanning under 40%. Year-over-year respondents reported declines in usage of several application security processes.

![Chart: Which of the following application security processes does your organization apply?]

### Clear Declines in Resources Dedicated to Supply Chain Security
Compared to our research last year, we saw a marked decrease in proactive security measures from 2023 to 2024. The percentage of organizations implementing new tooling and practices to address supply chain vulnerabilities dropped from 60.9% in 2023 to 49.6% in 2024. Similarly, those investing in training their development teams on supply chain vulnerabilities decreased from 53.2% to 35.4%.

![Chart: How have you or your organization been impacted by an open source or supply chain security vulnerability in the past year?]

### 52% Fail to Meet Stated SLAs for High-Severity Vulnerability Fixes
Widespread failure to meet vulnerability mitigation SLAs further highlights AppSec fatigue. Teams struggle to meet these goals, suggesting unrealistic expectations. While 74% have SLAs of a week or less, and 25% a day or less, 52% regularly miss these targets, and 14.8% frequently fail to meet them.

![Chart: What is your SLA policy for fixing high-severity vulnerabilities?]
![Chart: How often do you break your vulnerability SLA?]

### Teams Auditing Code Less Frequently and Less Continuously
Between 2023 and 2024, there was a noticeable shift toward less frequent code auditing among teams. The percentage of teams auditing code weekly increased from 29% in 2023 to 36.9% in 2024, while continuous auditing through automation decreased from 27% to 22.3%.

![Chart: How Often Do You Audit Your Code?]

### Big Increase In Using Tools That Analyze Package Security
Reliance on tools for package security rose 22.3% YoY, with an 11% drop in manual approaches like checking registry information.

![Chart: How do you check the safety of the open source packages used by your software?]

---

## Section 2: Supply Chain Security Remains Immature

Open source supply chain security remains lightly adopted, with no practice used by more than two-thirds of organizations. SBOM monitoring leads at 62%, and only software pipeline security also surpasses 50% usage.

![Chart: Which supply chain security practices does your organization follow?]
![Chart: Where are security tools integrated?]

---

## Section 3: Confidence in AI-Generated Code Outpaces Reality

High confidence in AI for secure code persists, despite evidence of vulnerabilities, signaling a need for better education on AI risks.

Respondents continued to hold high levels of misplaced confidence in the ability of AI tools to generate secure code. Despite 77.9% of respondents believing AI has improved code security, Snyk’s research shows frequent, serious vulnerabilities in AI-generated code. Meanwhile, 56.2% remain concerned about vulnerabilities introduced by AI.

![Chart: What factors do you use to determine the severity of a vulnerability?]
![Chart: Has the use of AI code suggestion tools improved your organization’s code security?]
![Chart: Are you concerned that using AI coding tools will introduce security vulnerabilities into your applications?]
![Chart: Are you concerned that using AI coding tools will introduce open source licensing and copyright problems into your stack?]
![Chart: Do you apply the same scrutiny to open source packages and libraries suggested by AI as those suggested by humans?]
![Chart: How many vulnerabilities has AI introduced into your code?]

---

## Section 4: Evidence of General Open Source Security Progress

The OSS community has significantly reduced time-to-fix for critical and high severity vulnerabilities in open source projects and continues to outperform proprietary software in response times based on vulnerability database findings.

![Chart: Time-to-Fix of High/Critical Severity Bugs: OSS vs Proprietary]

---

## Conclusion

The findings from our 2024 research paint a concerning picture of an industry struggling to maintain momentum in security practices while facing evolving challenges. The observed "AppSec exhaustion" phenomenon suggests that current approaches to security may be unsustainable.

**Moving forward, organizations need to:**
- Reassess their approach to security to prevent burnout and ensure sustainable practices.
- Improve prioritization in vulnerability management and other supply chain risk management tasks.
- Prioritize the adoption of fundamental supply chain security measures and deploy newer supply chain security measures to improve security posture.
- Include more holistic risk analysis as part of severity determination to ensure security teams can focus more time on risks that matter.
- Take a more cautious and measured approach to AI-generated code, implementing rigorous security reviews rather than assuming inherent security.
- Establish clear guidelines for validating and testing AI-generated code, treating it with the same or greater scrutiny as human-written code.

---

## Methodology
We surveyed 453 technologists across application development and security. We used many of the same questions we had asked in the 2023 State of Open Source Security and compared to the past results, where applicable. Respondents were located in the United States of America, Canada, and the United Kingdom. The question types included binary responses, multi-picks, and ratings on a scale. Respondents came from a wide variety of sectors, including automotive, business services, communications, education, energy and utilities, entertainment/media, financial services, government, and SaaS technology.

© 2024 Snyk Limited