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
- [Appendix B: Detailed Respondent Demographics](#appendix-b-detailed-respondent-demographics)
- [About Black Duck](#about-black-duck)

---

# Unprecedented Change for Embedded Software

The world of embedded software is changing at a faster pace than ever before. Our research drills into this new reality and finds two major stories unfolding at once. The first is the story of artificial intelligence—a massive adoption of AI tools but paired with dangerously lagging governance. The second is the story of the software supply chain becoming a core business function with the maturation of Software Bills of Materials (SBOMs) into a mainstream commercial requirement.

This report is a guide to understanding those two stories as well as the current state of embedded software development. We surveyed 785 professionals in the trenches—the developers, managers, and security pros who build the embedded software that runs our world—to give you a real, data-driven look at what’s happening.

![BlackDuck logo and page number 1]

---

# Why You Should Read This Report

“The State of Embedded Software Quality and Safety 2025” report is a field guide to the realities of embedded development. Whether you’re managing the budget or writing the code, the data presented here is directly relevant to your work.

### For Executive Leaders
This report is about risk and competitive advantages. Our findings on “shadow AI” and the governance gap aren’t technical problems; they are unmanaged business risks that create legal exposure and threaten your intellectual property. The data on SBOMs becoming a commercial requirement is a clear signal about what it now takes to win and keep customers. And the insights into the changing skillset of developers can directly inform your hiring, training, and strategic planning. This report gives you the information you need to ask the right questions from your technical teams and make informed decisions about where to invest.

### For Hands-on Coders
This report is about your job and your skills. The data showing Python overtaking C++ is a headline you can’t ignore; it’s a strong indicator of what coding skills are increasingly in demand. The findings on memory-safe languages and the “shift-everywhere” approach to security show how the definition of “good code” is changing. And the data on the manager/engineer perception gap is validation that the pressure you’re feeling is real. Use this report to understand the trends shaping your career and advocate for the tools and processes you need to do your job effectively and securely.

### Survey Methodology
The data comes from a comprehensive survey conducted by the international market research firm Censuswide in June 2025. We collected responses to 16 key questions from 785 professionals who live and breathe embedded software every day. Throughout the report you’ll see markers such as this: [Q12]. A marker indicates that the data preceding it was derived from one of those 16 questions.

![A quick look at who we talked to: Geographies, Roles, and Companies]

---

# Executive Summary

For the C-suite, the takeaway from our data is simple: The ground beneath your feet is shifting. The tools your teams use, the skills they need, and the risks they face are being completely redefined. The AI revolution and the formalization of supply chain security are your new operational reality. Ignoring these evolving changes is not an option if you care about your competitive position, your IP, or your products’ security.

> If you can’t show what’s in your software, you’re at a competitive disadvantage.

### Top Six Key Findings
- **The Stakes Are High**: The top concern among our respondents around software being released with defects was the possible safety/environment impact (19.62%) [Q2].
- **AI Is Everywhere, but the Guardrails Are Missing**: AI adoption is in full swing. A staggering 89.3% of respondents say their companies are already using AI coding assistants, and 96.1% note that their companies are building open source AI models directly into their products [Q10, Q11].
- **SBOMs Aren’t Just for Regulators Anymore**: SBOMs are no longer a checkbox for government contracts; they are a commercial demand. Over 70% of organizations now must produce an SBOM [Q15].
- **The Embedded Developer Is a New Breed**: The job description for an embedded developer is being rewritten. While C languages are still the cornerstone of embedded systems, it’s increasingly about memory-safe languages, with 80.4% of companies having already adopted them [Q9].
- **“Shadow AI” Is the Threat You May Not Be Tracking Sufficiently**: A significant 18% of companies know their developers are using AI tools against company policy [Q10].
- **Your Managers and Engineers Are Living in Different Realities**: While over 85% of VPs and directors are optimistic about on-time, on-quality releases, only 64% of the hands-on developers share that sentiment [Q7].

---

# The AI Revolution in Embedded Systems

Of all the changes sweeping the industry, one stands out as the most disruptive: artificial intelligence. Developers are adopting AI tools at a breakneck pace, but the rules and safeguards needed to manage this new power are dangerously behind.

### Unprecedented Adoption of AI
- **It’s Ubiquitous**: A stunning 89.3% of companies are already using AI-powered coding assistants [Q10].
- **It’s Built-in**: 96.1% of companies are using open source AI models in the software they ship [Q11].
- **It’s Unsanctioned**: 18% of organizations are aware that their developers use AI tools even when it is against stated company policy.

---

# The Governance Gap: Confidence Lags Behind Adoption

AI tools are everywhere, but the policies and processes to control them are lagging dangerously behind.

- **The Security Oversights**: More than one in five companies (21.1%) aren’t sure they can prevent AI from introducing vulnerabilities [Q12].
- **The Ticking Time Bomb of IP Risk**: Nearly 20% of organizations admit that they’re not confident they can manage the open source license risks that come with AI-generated code [Q13].
- **The Confidence Chasm**: Over 44% of embedded software engineers feel unequipped to handle the license risks from AI, while only about 14% of their counterparts in product security share that lack of confidence [Q13].

> The disconnect between rapid, often unsanctioned adoption and lagging governance creates a significant new category of business risk.

---

# The Maturation of Software Supply Chain Management

While the rush to AI adoption can feel like the Wild West, a different story is unfolding in the software supply chain.

- **SCA Is Now SOP**: Software composition analysis (SCA) is now a standard practice, with scans happening at every stage of the pipeline [Q3].
- **License Compliance Is No Longer an Afterthought**: More than half of all companies are actively scanning for license obligations in their main components (51.0%) and even in the tiny code snippets that developers copy and paste (54.4%) [Q5].
- **SBOMs Become a Commercial Imperative**: A full 70.8% of companies now say that producing an SBOM is a requirement for their business [Q15]. The single biggest driver for producing an SBOM is to meet customer or partner requirements (39.4%) [Q15].

---

# The People and Processes of Modern Embedded Development

### Navigating Speed vs. Quality
- **The Necessary Evil of Compromise**: Nearly 40% of all respondents admit they are only “mostly successful” because they “sometimes need to compromise” on quality to hit a deadline [Q7].
- **The Manager/Engineer Reality Gap**: 86% of CTOs feel their projects are successful, while only 56% of hands-on embedded software engineers agree [Q7].

### The Fragmented Compliance Landscape
- **Internal Standards Are King**: The most common source of authority is a company’s own “internal coding standards,” cited by 22.2% of respondents [Q14].
- **The “Build-Your-Own” Compliance Framework**: Companies are cherry-picking the controls that matter most from a variety of standards—CERT C, CWE, ISO—and combining them into a custom policy.

---

# Recommendations and Outlook

### Actionable Recommendations
- **For Technical Leaders**: Treat AI Assistants Like Talented, Unreliable Interns. Demand better, integrated tooling.
- **For Managers**: Write Your AI Policy Yesterday. Fix the skills gap. Stop treating security like a cost center.
- **For Security and Compliance Professionals**: Audit Your Tools for AI-Readiness. Update Your Threat Models. Weaponize the SBOM.

### Future Outlook
By 2026, we expect to see a boom in AI governance tools. The SBOM will cease to be a “nice to have” and will become a standard, non-negotiable line item in most B2B contracts.

---

# How Black Duck Can Help

Black Duck offers the industry’s most comprehensive and trusted portfolio of application security solutions.

### For Executive Leaders: Transforming Systemic Risk into Competitive Advantage
- **Closing the AI Governance Gap**: Black Duck SCA and Coverity® Static Analysis provide the visibility and provenance tracking needed to secure AI-generated code.
- **Mastering the Software Supply Chain**: Black Duck SCA provides multifactor detection (dependency, snippet, and binary analysis) to create accurate, dynamic SBOMs.
- **Bridging the Management/Engineering Gap**: The Black Duck Polaris™ Platform provides a single, correlated source of truth for application security risk.

### For Hands-on Developers: Building High-Quality Software Without Sacrificing Speed
- **Reliable Code That Lives in Your Workflow**: IDE and SCM integrations allow developers to receive real-time security and quality feedback.
- **Enforcing Any Standard, Automatically**: Coverity’s static analysis engine features configurable checkers that can be tuned to match an organization’s specific risk profile.
- **Making AI a Superpower**: Code Sight™ IDE Plug-in with Black Duck Assist™ automatically scans code in real time as it is written by developers or generated by AI coding assistants.

---

# Appendix A: Full Survey Questions
*(Refer to the original document for the full list of 16 questions and their corresponding statistical breakdowns.)*

---

# Appendix B: Detailed Respondent Demographics
*(Refer to the original document for the breakdown of geographies, job titles, company sizes, and industry sectors.)*

---

# About Black Duck
Black Duck is the industry’s most comprehensive and trusted portfolio of application security solutions, helping organizations secure their software, integrate security efficiently, and innovate safely with new technologies.

BLACKDUCK.COM

---

50–99

100–249

250–500

More than 500

51

92

136

219

167

120

Application/Software

Cybersecurity

Technology

Healthcare

Systems Engineer, Functional

Manufacturing

Automotive

MedTech

Government

Transportation

Telecommunication/ISP

Utilities

144

132

122

72

71

63

61

44

43

38

37

26

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

BLACKDUCK .COM  |  27

BLACKDUCK .COM  |  28