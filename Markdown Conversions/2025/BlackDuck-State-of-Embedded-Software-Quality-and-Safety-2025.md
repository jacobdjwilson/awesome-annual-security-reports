# The State of Embedded Software Quality and Safety 2025

## Table of Contents
- [Unprecedented Change for Embedded Software](#unprecedented-change-for-embedded-software)
- [Why You Should Read This Report](#why-you-should-read-this-report)
- [Executive Summary](#executive-summary)
- [The AI Revolution in Embedded Systems](#the-ai-revolution-in-embedded-systems)
- [The Governance Gap: Confidence Lags Behind Adoption](#the-governance-gap-confidence-lags-behind-adoption)
- [The Maturation of Software Supply Chain Management](#the-maturation-of-software-supply-chain-management)
- [The People and Processes of Modern Embedded Development](#the-people-and-processes-of-modern-embedded-development)
- [Recommendations and Outlook](#recommendations-and-outlook)
- [How Black Duck Can Help](#how-black-duck-can-help)
- [Appendix A: Full Survey Questions](#appendix-a-full-survey-questions)

---

## Unprecedented Change for Embedded Software

The world of embedded software is changing at a faster pace than ever before. Our research drills into this new reality and finds two major stories unfolding at once. The first is the story of artificial intelligence—a massive adoption of AI tools but paired with dangerously lagging governance. The second is the story of the software supply chain becoming a core business function with the maturation of Software Bills of Materials (SBOMs) into a mainstream commercial requirement.

This report is a guide to understanding those two stories as well as the current state of embedded software development. We surveyed 785 professionals in the trenches—the developers, managers, and security pros who build the embedded software that runs our world—to give you a real, data-driven look at what’s happening.

## Why You Should Read This Report

“The State of Embedded Software Quality and Safety 2025” report is a field guide to the realities of embedded development. Whether you’re managing the budget or writing the code, the data presented here is directly relevant to your work.

### For Executive Leaders
This report is about risk and competitive advantages. Our findings on “shadow AI” and the governance gap aren’t technical problems; they are unmanaged business risks that create legal exposure and threaten your intellectual property. The data on SBOMs becoming a commercial requirement is a clear signal about what it now takes to win and keep customers. And the insights into the changing skillset of developers can directly inform your hiring, training, and strategic planning. This report gives you the information you need to ask the right questions from your technical teams and make informed decisions about where to invest.

### For Hands-on Coders
This report is about your job and your skills. The data showing Python overtaking C++ is a headline you can’t ignore; it’s a strong indicator of what coding skills are increasingly in demand. The findings on memory-safe languages and the “shift-everywhere” approach to security show how the definition of “good code” is changing. And the data on the manager/engineer perception gap is validation that the pressure you’re feeling is real. Use this report to understand the trends shaping your career and advocate for the tools and processes you need to do your job effectively and securely.

### Survey Methodology
This report is designed to give you a clear, data-backed understanding of the current state of the embedded software industry. We break down the key trends, the real-world challenges, and the strategic shifts separating the leaders from the laggards. Our goal is to give you the insights you need to make smart decisions in a landscape that’s changing by the minute.

The data comes from a comprehensive survey conducted by the international market research firm Censuswide in June 2025. We collected responses to 16 key questions from 785 professionals who live and breathe embedded software every day. Throughout the report you’ll see markers such as this: [Q12]. A marker indicates that the data preceding it was derived from one of those 16 questions.

## Executive Summary

For the C-suite, the takeaway from our data is simple: The ground beneath your feet is shifting. The tools your teams use, the skills they need, and the risks they face are being completely redefined. The AI revolution and the formalization of supply chain security are your new operational reality. Ignoring these evolving changes is not an option if you care about your competitive position, your IP, or your products’ security.

### Top Six Key Findings
- **The Stakes Are High**: The top concern among our respondents around software being released with defects was the possible safety/environment impact (19.62%) [Q2].
- **AI Is Everywhere, but the Guardrails Are Missing**: AI adoption is in full swing. A staggering 89.3% of respondents say their companies are already using AI coding assistants, and 96.1% note that their companies are building open source AI models directly into their products [Q10, Q11].
- **SBOMs Aren’t Just for Regulators Anymore**: SBOMs are no longer a checkbox for government contracts; they are a commercial demand. Over 70% of organizations now must produce an SBOM [Q15].
- **The Embedded Developer Is a New Breed**: The job description for an embedded developer is being rewritten. While C languages are still the cornerstone of embedded systems, it’s increasingly about memory-safe languages, with 80.4% of companies having already adopted them [Q9].
- **“Shadow AI” Is the Threat You May Not Be Tracking Sufficiently**: A significant 18% of companies know their developers are using AI tools against company policy [Q10].
- **Your Managers and Engineers Are Living in Different Realities**: While over 85% of VPs and directors are optimistic about on-time, on-quality releases, only 64% of the hands-on developers share that sentiment [Q7].

> "If you can’t show what’s in your software, you’re at a competitive disadvantage."

## The AI Revolution in Embedded Systems

Of all the changes sweeping the industry, one stands out as the most disruptive: artificial intelligence. Developers are adopting AI tools at a breakneck pace, but the rules and safeguards needed to manage this new power are dangerously behind.

- **It’s Ubiquitous**: A stunning 89.3% of companies are already using AI-powered coding assistants [Q10].
- **It’s Built-in**: 96.1% of companies are using open source AI models in the software they ship [Q11].
- **It’s Unsanctioned; the Shadow AI Problem**: 18% of companies know their developers are using AI tools against official policy [Q10].

## The Governance Gap: Confidence Lags Behind Adoption

AI risk management is a new, significant category of business risk that most companies are only beginning to grapple with.

- **The Security Oversights**: More than one in five companies (21.1%) aren’t sure their AI-generated code is safe [Q12].
- **The Ticking Time Bomb of IP Risk**: Nearly 20% of organizations admit that they’re not confident they can manage the open source license risks that come with AI-generated code [Q13].
- **The Confidence Chasm Between Security and Dev**: Over 44% of embedded software engineers feel unequipped to handle the license risks from AI, while only about 14% of their counterparts in product security share that lack of confidence [Q13].

## The Maturation of Software Supply Chain Management

What was once a niche security concern has become a mainstream business requirement.

- **SCA Is Now SOP**: Software composition analysis (SCA) is now a standard practice, with scans happening at every stage of the pipeline [Q3].
- **License Compliance Is No Longer an Afterthought**: More than half of all companies are actively scanning for license obligations in their main components (51.0%) and in code snippets (54.4%) [Q5].
- **SBOMs Become a Commercial Imperative**: 70.8% of companies now say that producing an SBOM is a requirement for their business [Q15]. The single biggest driver is "customer or partner requirements" (39.4%) [Q15].

## The People and Processes of Modern Embedded Development

- **Navigating Speed vs. Quality**: Nearly 40% of all respondents admit they are only “mostly successful” because they “sometimes need to compromise” on quality to hit a deadline [Q7].
- **The Manager/Engineer Reality Gap**: 86% of CTOs feel their projects are successful, while only 56% of hands-on embedded software engineers agree [Q7].
- **The Fragmented Compliance Landscape**: No single public standard dominates. The most common source of authority is a company’s own “internal coding standards” (22.2%) [Q14].

## Recommendations and Outlook

### Actionable Recommendations
- **For Technical Leaders**: Treat AI assistants like talented, unreliable interns. Demand better, integrated tooling (SAST/SCA).
- **For Managers**: Write your AI policy immediately. Invest in training for memory-safe languages. Stop treating security like a cost center.
- **For Security Professionals**: Audit your tools for AI-readiness. Update your threat models to include AI-specific risks. Weaponize the SBOM as a strategic asset.

### Future Outlook
By 2026, we expect to see a boom in AI governance tools. The skills gap between developers who can master these new tools and those who can’t will widen. Finally, the SBOM will cease to be a “nice to have” and will become a standard, non-negotiable line item in most B2B contracts.

## How Black Duck Can Help

Black Duck offers a comprehensive portfolio of application security solutions to address these challenges:
- **Black Duck® SCA**: Provides deep analysis of code, snippet analysis to mitigate IP/license risk, and dynamic SBOM management.
- **Coverity® Static Analysis**: Analyzes AI-generated code for critical defects and vulnerabilities, supporting MISRA and CERT C/C++ standards.
- **Polaris™ Platform**: Provides a single, correlated source of truth to bridge the gap between management and engineering, offering centralized visibility and role-based views.

## Appendix A: Full Survey Questions

*(Note: The original document contains detailed tables for 16 survey questions. Below is a summary of the data provided in the text.)*

- **[Q2] Largest concern if software is released with defects**: Impact on safety or the environment (19.62%).
- **[Q7] Success in releasing on time/meeting standards**: 62.5% of VPs report success vs. 55.6% of engineers.
- **[Q8] Biggest challenge to eliminating defects**: Complexity of software/hardware/systems (18.73%).
- **[Q10] AI assistant usage**: 38.98% (certain teams), 32.36% (all developers), 18% (shadow AI).
- **[Q15] SBOM requirements**: 39.4% (customer/partner), 31.5% (industry regulation).

---

making it hard to focus on resolving defects and developers use them
17 .58%
vulnerabilities No, developers are not permitted to, and do not, use these tools 7 .26%
It’s not a priority to eliminate all critical issues 14 .65% I do not have enough visibility into development processes to know if
3 .44%
Insufficient testing or tools to identify issues 14 .39% these tools are used
Lack of secure coding skills 12 .74%
I don’t have visibility into challenges regarding coding defects 3 .82%
9 . Are your developers writing code (or planning to begin writing code) using
one or more “memory safe” programming languages (e .g ., Rust, Go, C#,
Swift, Java, or Python)?
We’re already writing code in a memory safe language on new projects,
42 .80%
and transitioning existing C++ projects to a memory safe alternative
We’re already writing code in a memory safe language on new projects
37 .58%
only
We’re planning to begin writing code in a memory safe programming
13 .50%
language in the near future
I don’t have visibility into plans around programming languages 3 .18%
No, we have no plans to write code using a memory safe language 2 .93%
Some developers are permitted
to use AI assistants [39.0%]
All developers are permitted to
use AI assistants [32.3%]
Used against company policy
("Shadow AI") [18.0%]
BLACKDUCK .COM | 23

11 .  Are you using any open source AI models (e .g ., from Hugging Face) in the  12 .  How confident are you that you have the processes and tools in place to
software you build?  ensure AI-generated code doesn’t introduce security vulnerabilities or other
|                                        |         | issues?  |
| -------------------------------------- | ------- | -------- |
| Yes, for data processing and cleaning  | 37 .32% |          |
Yes, for computer vision (e .g ., image recognition)  35 .92% Moderately confident we have sufficient policies and testing in place  40 .13%
Yes, for process automation  34 .78% Very confident we have sufficient policies and comprehensive testing in
33 .76%
| Yes, for natural language processing  | 32 .10% | place  |
| ------------------------------------- | ------- | ------ |
Slightly confident we have sufficient policies and testing in place  15 .29%
| Yes, for embedding pretrained models  | 31 .72% |     |
| ------------------------------------- | ------- | --- |
Yes, for training custom models  30 .45% Not at all confident we have sufficient policies and testing in place  5 .86%
Yes, for predictive analytics  30 .45% I do not have enough visibility into our processes to manage and secure
3 .31%
AI-generated code
| I don’t have visibility into usage of open source AI models  | 2 .93% |     |
| ------------------------------------------------------------ | ------ | --- |
This is not a priority at this time, as using AI-generated code is against
| No, we are not currently using open source AI models  | 1 .02% |     |
| ----------------------------------------------------- | ------ | --- |
1 .66%
company policies
73.9%  21.1%
Confident Not Confident
40.1%
Moderately Confident
33.8%
Very Confident
15.3%
Slightly Confident
5.9%
Not at All Confident
BLACKDUCK .COM  |  24

13 . How confident are you in your ability to ensure AI-powered code assistants 15 . Is your business required to produce a Software Bill of Materials (SBOM) to
don’t introduce open source code subject to license obligations that could meet customer requirements or industry regulations?
put your IP at risk?
Yes, we currently produce SBOMs to meet customer or partner
39 .36%
Very confident we have the policies and tools in place to identify all open requirements
39 .75%
source components and code snippets Yes, we currently produce SBOMs to comply with an industry regulation 31 .46%
Moderately confident we have the policies and tools in place to identify all No, but we do produce SBOMs for a different reason 13 .76%
38 .85%
open source components and code snippets No, we don’t currently produce SBOMs, but are planning to in the future 7 .90%
Slightly confident we have the policies and tools in place to identify all No, we have no requirement to produce SBOMs 4 .20%
14 .27%
open source components and code snippets
I do not have enough visibility into our SBOM process 3 .31%
Not at all confident we have the policies and tools in place to identify all
4 .08%
open source components and code snippets
16 . How confident are you in your company’s ability to produce a complete and
I do not have enough visibility into the policies and tools to identify all
3 .06%
accurate Software Bill of Materials (SBOM)?
open source code in our software
Moderately confident we have tools in place to produce an SBOM, but
14 . What standards or regulations must your software adhere to before it’s 40 .25%
aren’t sure of its accuracy
released?
Very confident we have the knowledge and tools in place to produce an
40 .13%
accurate SBOM
CERT C/C++/Java 24 .46%
Not confident we are unsure of what’s required to build an accurate SBOM 11 .08%
Internal coding standards 22 .17%
Not a requirement to produce an SBOM at this time 4 .84%
MISRA C/C++ 22 .04%
I do not have enough visibility into our SBOM process 3 .69%
ISO 26262 21 .15%
ISO/SAE 21434 20 .89%
OWASP Top 10 19 .62%
EU Cyber Resilience Act 19 .11%
CWE Top 25 18 .47%
FDA Regulations 18 .34%
DO-326A/ED-202A 18 .22%
AUTOSAR 18 .09%
IEC 62443 17 .07%
DO-178C 15 .16%
DISA STIG 14 .52%
PCI DSS 14 .01%
BLACKDUCK .COM | 25

APPENDIX B: DETAILED RESPONDENT
DEMOGRAPHICS
Respondents by Country Respondents by Select Job Titles Respondents by Company  Respondents by Industry
|           |     |                                |     | Size (Number of Employees) |     | Sector                       |     |
| --------- | --- | ------------------------------ | --- | -------------------------- | --- | ---------------------------- | --- |
| U .S .    | 125 | Chief Technology Officer (CTO) | 58  |                            |     |                              |     |
|           |     | VP of Engineering              | 8   |                            |     | Application/Software         | 144 |
| U .K .    | 104 |                                |     | 1–9                        | 51  |                              |     |
|           |     | VP of Software Development     | 23  |                            |     | Cybersecurity                | 132 |
|           |     |                                |     | 10–49                      | 92  |                              |     |
| France    | 104 |                                |     |                            |     |                              |     |
|           |     |                                |     |                            |     | Technology                   | 122 |
|           |     | Director of Software           | 9   |                            |     |                              |     |
| Germany   | 100 |                                |     | 50–99                      | 136 |                              |     |
|           |     | Head of Embedded Software      | 11  |                            |     | Healthcare                   | 72  |
|           |     |                                |     | 100–249                    | 219 |                              |     |
| Japan     | 100 |                                |     |                            |     |                              |     |
|           |     | Embedded Software Engineer     | 9   |                            |     | Systems Engineer, Functional | 71  |
|           |     |                                |     | 250–500                    | 167 |                              |     |
| Singapore | 100 |                                |     |                            |     | Manufacturing                | 63  |
|           |     | Embedded Systems Developer     | 14  |                            |     |                              |     |
China 100 Senior Firmware Engineer 8 More than 500 120 Automotive 61
|         |     | Product Security Engineer    | 69  |     |     | MedTech               | 44  |
| ------- | --- | ---------------------------- | --- | --- | --- | --------------------- | --- |
| Finland | 52  |                              |     |     |     |                       |     |
|         |     |                              |     |     |     | Government            | 43  |
|         |     | Embedded Security Engineer   | 68  |     |     |                       |     |
|         |     | Cybersecurity Engineer       | 29  |     |     | Transportation        | 38  |
|         |     | Functional Safety Manager    | 20  |     |     | Telecommunication/ISP | 37  |
|         |     |                              |     |     |     | Utilities             | 26  |
|         |     | Functional Safety Engineer   | 9   |     |     |                       |     |
|         |     | Quality Manager              | 19  |     |     |                       |     |
|         |     | AI/ML Engineer               | 30  |     |     |                       |     |
|         |     | Technical AI Product Manager | 41  |     |     |                       |     |
BLACKDUCK .COM  |  26

ABOUT BLACK DUCK
Black Duck® meets the board-level risks of modern software with True Scale Application
Security, ensuring uncompromised trust in software for the regulated, AI-powered world .
Only Black Duck solutions free organizations from tradeoffs between speed, accuracy, and
compliance at scale while eliminating security, regulatory, and licensing risks . Whether in the
cloud or on premises, Black Duck is the only choice for securing mission-critical software
everywhere code happens . With Black Duck, security leaders can make smarter decisions and
unleash business innovation with confidence . Learn more at www .blackduck .com .
©2025 Black Duck Software, Inc . All rights reserved . Black Duck is a trademark of Black Duck Software, Inc . in the United States and other countries . All other names mentioned herein are
trademarks or registered trademarks of their respective owners . August 2025
BLACKDUCK .COM | 27

BLACKDUCK .COM | 28