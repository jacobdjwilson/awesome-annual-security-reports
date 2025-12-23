# 9th Edition The Rise of Hacker-Powered Security Report

## Table of Contents
- [Executive Summary](#executive-summary)
- [About the Hacker-Powered Security Report](#about-the-hacker-powered-security-report)
- [Part I - AI’s Transformative Impact on Cybersecurity](#part-i---ais-transformative-impact-on-cybersecurity)
  - [Security for AI](#security-for-ai)
  - [AI Attack Surface and Findings](#ai-attack-surface-and-findings)
  - [Pillars of Trusted AI: Safety and Security](#pillars-of-trusted-ai-safety-and-security)
  - [AI for Security and Program Operations](#ai-for-security-and-program-operations)
  - [Hai, HackerOne’s Agentic AI System](#hai-hackerones-agentic-ai-system)
  - [Tools of Choice](#tools-of-choice)
  - [From Automation to Autonomy: The Hackbot Arms Race](#from-automation-to-autonomy-the-hackbot-arms-race)
- [Part II - The Human Advantage in Cybersecurity](#part-ii---the-human-advantage-in-cybersecurity)
  - [Which Vulnerabilities are AI Tools Currently Weakest at Identifying?](#which-vulnerabilities-are-ai-tools-currently-weakest-at-identifying)
  - [Global Researchers, Diverse Impact](#global-researchers-diverse-impact)
  - [A Flexible Workforce](#a-flexible-workforce)
  - [Age and Maturity](#age-and-maturity)
  - [24/7 Global Coverage](#247-global-coverage)
- [Part III - Building Best-in-Class Security Programs](#part-iii---building-best-in-class-security-programs)
  - [A Year in Review](#a-year-in-review)
  - [Maturing Identity and Access: Signals from the Market](#maturing-identity-and-access-signals-from-the-market)
  - [Incentives Drive Outcomes](#incentives-drive-outcomes)
  - [The Five-Year Outlook: From Signals to Strategy](#the-five-year-outlook-from-signals-to-strategy)
  - [Driving Program Effectiveness](#driving-program-effectiveness)
- [Industry Insights 2025: Bounties, Breaches, and Business Risk](#industry-insights-2025-bounties-breaches-and-business-risk)
  - [Spotlight: Extending into Web3](#spotlight-extending-into-web3)
  - [Introducing the ARO and Payload Lenses](#introducing-the-aro-and-payload-lenses)
- [Financial Services & Insurance (FSI)](#financial-services--insurance-fsi)
- [Government](#government)
- [Retail and E-commerce](#retail-and-e-commerce)
- [Technology: Computer Software, Internet & Online, Cryptocurrencies and Blockchain, Telco](#technology-computer-software-internet--online-cryptocurrencies-and-blockchain-telco)
- [Closing Remarks](#closing-remarks)
- [Data Sources and Methodology](#data-sources-and-methodology)

---

# Executive Summary

Since 2024, HackerOne has seen a 210% increase in valid AI-related vulnerability reports and doubled the number of surveyed researchers focused on AI/ML assets.

From automakers to government agencies and global banks, today’s enterprises are fundamentally technology-driven and operating in threat landscapes that evolve faster than ever. Accelerated by the mainstream adoption of AI and the erosion of traditional perimeters, modern attackers combine automation with creativity to exploit vulnerabilities at machine speed, often before defenders even recognize the threat.

We’re witnessing the emergence of a new kind of security contributor:

These are human security researchers using AI as a catalyst, accelerating recon, triage, scaling pattern recognition, and probing complex attack surfaces faster than ever before. The gap between traditional automation and human testing is closing; not because humans are being replaced, but because they are evolving with AI.

In our 9th annual Hacker-Powered Security Report, we reveal how AI is reshaping offensive security into a more continuous and contextual process, and why the future belongs to teams who treat AI not as an add-on, but as a core extension of human expertise.

Drawing from extensive data gathered from our global community of ethical hackers and security researchers, real-world experiences from customer engagements, and proprietary intelligence from the HackerOne Platform, the 2025 report revolves around three pillars:

AI’s Transformative
Impact on
Cybersecurity

The Human
Advantage in
Cybersecurity

Building
Best-in-class
Security Programs

01

THE| 9th Edition Hacker-Powered Security Report 2025/2026

# About the Hacker-Powered Security Report

The 9th annual Hacker-Powered Security Report compiles insights, data, and analysis from customers, security researchers, and HackerOne’s vulnerability database from July 1, 2024, to June 30, 2025.

## Key Findings

**580,000+** All Time Valid Vulnerabilities
**1,950+** Customer Programs in 2025
**1,820+** Surveyed Researchers
**99** Surveyed Customers

### Valid AI Vulnerability Reports Skyrocket in 2025

Out of the 210% increase in valid AI reports, 65% were AI security issues such as prompt injection, model manipulation, or exposed endpoints, while 35% fell into the AI safety category, including ethical misuse or output integrity. This surge is fueled by growing researcher interest: in 2024, just 9% of survey respondents focused on hacking AI/ML assets. That number has now doubled to 19%, signaling a strong shift in focus within the security research community.

### AI Security Concerns Increase Among HackerOne Customers

In 2025, 78% of HackerOne customers said their concern over AI risks had grown in the past year. Just a year earlier, less than half (48%) ranked generative AI among their top security risks. The shift shows how quickly AI has moved from a watch list item to a front-line security concern, especially around data integrity and misuse.

### HackerOne Researchers Are Preparing for the AI Era

58% of surveyed security researchers are actively upskilling in AI, learning to audit AI/ML systems, and integrating AI into their own workflows. The rise of bionic hackers, humans pairing their creativity with the scale and speed of autonomous and agentic tools, is already shaping the next generation of offensive (and defensive) security capabilities.

---

**Total Bounty Payouts** $81M ^ Up 13%
**Average Bounty Payout** $1,090 ^ Up 9%
**Valid Reports** 84.9K ^ Up 270%
**Critical & High Severity Valid Reports** 23.7K ^ Up 9%
**Programs with AI in Scope or with a Valid AI Report** 1,121 ^ Up 270%
**Growth in Valid AI Reports** 210%
**Rewards Paid Out for Valid AI Reports** $3B ^ Up 339%
**Mitigated Loss Savings** $3B ^ Up 9%

02 | Year in Review | 9th Edition Hacker-Powered Security Report 2025/2026

# Part I - AI’s Transformative Impact on Cybersecurity

As organizations race to deploy AI, many still lack the capacity to secure it.

Since our last report, AI has expanded from isolated models to a connected ecosystem. New protocols and architectures now let systems operate with real-time context, coordinate across tools, and embed directly into security workflows. This shift is reshaping both sides of the HackerOne community: customers are rapidly bringing AI assets into scope, and researchers are growing the skills to test and secure them.

This first section follows that shift into practice through four lenses: securing AI itself, using AI to accelerate program operations, how researchers wield AI in their toolkit, and what hackbots add.

According to IBM’s Cost of a Data Breach Report 2025, 97% of reported AI-related security incidents had gaps in access controls. Our customer survey echoes this: more than half feel unprepared and under-resourced for AI risks. While 84% of CISOs now oversee AI security and data privacy, many report they lack the resources to manage these risks effectively.

## Security for AI

03

In 2025, 13% of organizations reported an AI-related security incident. Of those, 97% lacked proper AI access controls. | 9th Edition Hacker-Powered Security Report 2025/2026

**1,121** Distinct programs included AI in scope or received a valid AI vulnerability.
**270%** Year-over-year increase of AI in program scope.
**58%** Of the respondents have upskilled in AI/ML security.
**41%** Of the respondents are already testing AI assets as part of their work.

A major enabler in 2025 was the Model Context Protocol (MCP), which provides LLMs structured, real-time connections to tools and data.

21% of surveyed HackerOne researchers (Figure 1) are developing MCP-specific security skills as these capabilities enter customer workflows, and an overwhelming 82% are developing skills specifically in Prompt Injection.

## AI Attack Surface and Findings

As organizations integrate AI into products, workflows, and infrastructure, attackers are learning just as quickly how to exploit them.

**210%** increase in valid AI reports since 2024
**339%** increase in total rewards paid for valid AI vulnerabilities from 2024 to 2025

**Figure 1 - AI/ML security skills of surveyed researchers**
- Prompt Injection
- Offensive Tooling
- Data Poisoning
- AI Safety
- Model Theft
- Model Inversion
- A2 Protocol
- Security
- Other
- RAG Poisoning

![Bar chart showing AI/ML security skills of surveyed researchers with percentages for each skill.](image_description)

**Figure 2 - Growth of valid AI reports over time**

![Line graph showing the growth of valid AI reports over time, with data points for 2024 and 2025.](image_description)

04 | 9th Edition Hacker-Powered Security Report 2025/2026

## Pillars of Trusted AI: Safety and Security

In 2025, 78% of customers reported growing anxiety over AI risks, reflecting the surge in vulnerability findings.

Prompt injection saw the sharpest increase in 2025, up 540% (Figure 3), as researchers targeted weaknesses in how models interpret and execute user input. Sensitive information disclosure more than doubled (+152%), highlighting the risk of AI unintentionally revealing private or proprietary data.

- **LLM01 Prompt Injection**: 540%
- **LLM02 Insecure Output Handling**: 233%
- **LLM03 Training Data Poisoning**: 36%
- **LLM04 Model Denial of Service**: 9%
- **LLM05 Supply Chain Vulnerabilities**: 11%
- **LLM06 Sensitive Information Disclosure**: 152%
- **LLM07 Insecure Plugin Design**: 212%
- **LLM08 Excessive Agency**: -5%
- **LLM09 Overreliance**: 22%
- **LLM10 Model Theft**: 32%

**Figure 3 - Valid AI reports across OWASP Top 10, 2024 vs 2025**
Number of reports, by vulnerability type

![Bar chart comparing valid AI reports for OWASP Top 10 categories in 2024 and 2025.](image_description)

## AI for Security and Program Operations

Since 2021, valid vulnerability reports on HackerOne have grown by 20%, not including the large number of submissions ultimately deemed invalid. Every report, whether critical or false, demands triage, creating a workload that quickly becomes unsustainable. Manual processes alone can’t keep pace with the speed and scale of modern threat exposure management.

05 | 9th Edition Hacker-Powered Security Report 2025/2026

# Hai, HackerOne’s Agentic AI System

In 2025, 90% of HackerOne customers have enabled Hai, our agentic AI system. More than just an automation tool, Hai delivers AI for security outcomes and is redefining threat exposure management.

**3 in 5 customers cite time savings and efficiency as Hai’s biggest impact.**

**60%** save ~2 hours per week (~4–8 hours per month, about half to one full day saved).
**20%** save 6–10 hours per week (~24–40 hours per month, equal to 3 to 5 workdays saved).

**Figure 4 - Customers’ workflow improvements by Hai**
- Saves time
- Streamlines program operations
- Improves prioritization
- Strengthens researcher collaboration
- Increases confidence in decisions
- Reveals trends & performance more clearly

![Pie chart showing how Hai has impacted customer workflows.](image_description)

**Figure 5 - Customers’ time savings with Hai**
- 1-2 hours
- 3-10 hours
- More than 10 hours
- Not sure

![Bar chart showing the amount of time customers save per week with Hai.](image_description)

**Figure 6 - The use of AI in hacking**
- Report writing
- PoC generation
- Writing or refining exploit code
- Brainstorming
- Summarizing data
- Wordlist generation
- Note taking
- Automated reconnaissance
- Building or using an automated LLM agent
- Other

![Bar chart showing how researchers are using AI in hacking.](image_description)

Just as customers are embedding AI to manage rising report volumes and improve program efficiency, researchers are rapidly embracing AI to sharpen their edge. 67% of surveyed researchers now use AI or automation tools to accelerate reconnaissance, speed up testing, and reduce repetitive tasks.

## AI in the Researcher Workflow

06 | 9th Edition Hacker-Powered Security Report 2025/2026

# Tools of Choice

Researchers are experimenting broadly, combining web-based LLMs, locally hosted models, and custom-built offensive tools to fit their workflows.

Web-based LLMs are valued for their accessibility and versatility (Figure 7). Locally hosted models are gaining ground, among the 18% of researchers who cite privacy concerns as a barrier to cloud-based tools (Figure 8). These models provide power and control for sensitive or proprietary testing.

While privacy is a valid concern, the biggest blockers researchers face in adopting AI are 'Limited access to AI-specific training or resources' (39%) and a 'Lack of practical experience or expertise in AI security' (33%).

## AI-Enhanced Tools Leading Early Adoption

- **Burp AI (36%)**: integrates AI directly into Burp Suite for attack analysis, with its usage growing at ~25% month over month.
- **Cursor (26%)**: is used for AI-powered coding and debugging environment, alongside custom CLI wrappers (23%).
- **BurpGPT (20%)**: is bringing natural language and automation into everyday workflows.

> “[At PortSwigger], our vision for Burp AI has always been simple: to augment researchers, not replace them. The significant levels of adoption we’re seeing show that the community values AI that strengthens their skills. Burp AI is only the beginning. We’re iterating fast and can’t wait to see how it continues to evolve.”
>
> — Katie Warren, Product Manager for Burp AI, PortSwigger

07 | 9th Edition Hacker-Powered Security Report 2025/2026

**Figure 7 - Web-based LLMs used for hacking**
- Other
- Burp AI
- Cursor
- BurpGPT
- Custom CLI Wrappers

![Pie chart showing the distribution of web-based LLMs used for hacking.](image_description)

**Figure 8 - Locally hosted LLMs used for hacking**
- Other
- LocalGPT
- PrivateGPT
- Ollama
- LM Studio

![Pie chart showing the distribution of locally hosted LLMs used for hacking.](image_description)

# From Automation to Autonomy: The Hackbot Arms Race

With the rise of agent frameworks and hackbots in 2025, offensive security has entered the era of agentic AI. Unlike traditional scanners, hackbots and autonomous agents can already chain tools together, adapt to feedback, and make decisions in real time. This marks the move from rule-based automation to exploratory, AI-assisted offensive action.

Our 5-month review tells us that hackbots excel at pattern-matching and detecting surface-level flaws like reflected XSS, much like traditional scanners. As the technology matures, its capabilities will likely expand to uncovering IDORs or business logic issues at scale, but today, human contextual reasoning, and system-level understanding remain essential alongside automation and autonomy.

> "The future is a symbiosis between hackers and AI. Hackbots can replace the repetitive work so humans can focus on creativity and new research."
>
> – André Baptista, long-time hacker, co–founder of Ethiack

**49%** of all hackbot reports were valid
**82%** of customers are aware of hackbots operating on the platform, 63% remain cautiously optimistic, recognizing the opportunities and the risks they bring.
**66%** of researchers expect hackbots will enhance their work, while 43% see them mainly as tools for simple bugs.

HackerOne has already adapted, updating its leaderboard to represent all contributors, from individual researchers to collectives; highlighting a future where human creativity and AI’s scaling power work hand in hand.

**Figure 9 - The future of hackbots and autonomous testing tools**
- They will enhance our work as researchers and boost productivity
- They pose a risk to the integrity or fairness of bug bounty programs
- They’ll be a useful tool primarily for finding simple bugs
- I’m unsure about their long-term impact
- Other
- I think they will replace human hackers

![Bar chart showing researcher and customer expectations for hackbots and autonomous testing tools.](image_description)

**Hackbots on HackerOne**
- Valid reports submitted by hackbots: 21%
- Unique hackbots submitted reports: 17%
- Valid submissions were XSS vulnerabilities: 12%

08 | 9th Edition Hacker-Powered Security Report 2025/2026

# Part II - The Human Advantage in Cybersecurity

AI delivers speed, scale, and pattern recognition, while humans bring the nuance, creativity, and judgment needed for complex vulnerabilities. Certain challenges, such as business logic flaws, multi-step exploits, and authentication bypasses (Figure 10), still demand human context and system-level understanding. When paired with AI’s strengths in reconnaissance, scanning, and payload generation, researchers are able to identify risks more effectively.

Building on this dynamic, this section explores how humans and AI complement one another in security, then turns to the HackerOne community itself; a global workforce that mirrors adversaries in creativity, but channels those skills toward defense.

09

**Figure 10 - The limitations of AI tools**
- Multi-step Exploits / Chainable Vulns: 58%
- Privilege Escalation: 39%
- Authentication Bypasses: 29%
- Authorization Issues: 28%
- Race Conditions: 27%
- Insecure Design Flaws: 25%
- Security Control Bypasses: 24%
- Other: 20%
- Business Logic: 4%

![Bar chart showing the limitations of AI tools in identifying certain vulnerabilities.](image_description)

Only 12% of researchers believe AI will replace them. Most see the future of cybersecurity as a collaboration.

# Global Researchers, Diverse Impact

Security leaders often frame the talent shortage in terms of their own headcount, a view reinforced by ISC2, which estimates global demand for 10.2 million professionals against a workforce of just 5.5 million, leaving a gap of 4.8 million. That gap reflects in-house staffing needs, but it overlooks the global researcher community: tens of thousands of skilled practitioners already finding and fixing vulnerabilities for enterprises every day.

This distributed talent pool is a force multiplier, bringing scale, diversity, and adaptability security teams cannot achieve alone. This year, we are bringing a sharper context on who these researchers are, where they come from, and how their expertise is evolving.

## Multidisciplinary Backgrounds and Expertise

**Figure 11 - Background of surveyed researchers**
- Independent Security Researcher: 44%
- Cybersecurity Professional: 38%
- Student: 11%
- Software Development: 4%
- DevOps: 1%
- Other: 0.6%
- Data Engineering: 0.1%
- Systems Administration: 0.1%
- AI/Machine Learning: 0.1%
- Assembly Line Operator: 0.1%
- Academic/Educator: 0.1%
- OSINT Engineer: 0.1%
- Navy (Military): 0.1%
- Doctor of Pharmacy: 0.1%

![Donut chart showing the diverse backgrounds of surveyed researchers.](image_description)

The HackerOne community is far from homogeneous (Figure 11). Nearly half of the survey respondents identify as independent security researchers, over a third as cybersecurity professionals, and 11% as students, with additional representation from DevOps, AI/ML, OSINT, and even unconventional paths such as pharmacy or assembly line operations.

This multidisciplinary mix is the secret recipe for producing technically sound, creative findings with the same persistence level as real adversaries.

10 | 9th Edition Hacker-Powered Security Report 2025/2026

# A Flexible Workforce

Time commitment splits across a spectrum (Figure 12), creating unmatched flexibility among the surveyed researchers: a core of committed specialists, amplified by a broader perimeter of part-time experts who flex into programs as needed.

**Figure 12 - Time commitment of surveyed researchers**
On average, approximately how many hours a week do you spend hacking (on another platform)?
- Less than 1 hour: 7%
- 1-9 hours: 21%
- 10-19 hours: 31%
- 20-29 hours: 15%
- 30-39 hours: 4%
- 40+ hours: 29%

![Bar chart showing the time commitment of surveyed researchers per week.](image_description)

**Asset Focus**
Researchers have the agility to shift quickly as new domains mature. The standout trend in 2025 is AI/LLM testing, which doubled YoY from 9% to 19% compared to figures in the 8th edition of the report.

- **Web applications**: 96% (↑ 1 pt YoY)
- **API**: 65% (↓ 3 pts YoY)
- **Desktop software**: 14% (↑ 2 pts YoY)
- **Blockchain**: 63% (↑ 2 pts YoY)
- **Mobile applications (Android, iOS, Windows)**: 19% (↑ 10 pts YoY)
- **AI/LLMs**: 6% (↑ 1 pts YoY)

Researchers dedicate 30+ hours per week, treating hacking as a full-time career.
Researchers fall in the 10–19 hour range, tuning part-time focus and deeper commitment.
Researchers spend 1–9 hours per week, layering their day jobs with part-time hacking.

11 | 9th Edition Hacker-Powered Security Report 2025/2026

# Age and Maturity

Researchers often start young (late teens, early 20s), but our platform data shows a growing share in their 30s and 40s, even some in their 50s, signaling community maturity (Figure 14). Payout data reinforces this (Figure 13): while many researchers contribute to the long tail, the most experienced capture six and seven-figure rewards, validating both their expertise and the market’s demand for it.

**Figure 13 - Total annual platform earnings**
Total Hacker Payouts
- Top researcher earning: $1,079,738
- Average researcher earning: $39,500
- Median researcher earning: $13,800

![Bar chart showing total annual platform earnings for top, average, and median researchers.](image_description)

**Figure 14 - Age of account creation and current age (All time)**
- Average physical age of users: 26
- Average age of the user's account on platform: 2.5
- Age of account creation
- Current age

![Scatter plot showing the age of account creation versus current age of users.](image_description)

12 | 9th Edition Hacker-Powered Security Report 2025/2026

# 24/7 Global Coverage

Geography underscores the adaptability of the HackerOne community, including security researchers, pentesters, and code reviewers. India, the United States, and the United Kingdom remain the largest hubs, but the community’s footprint spans every continent. The percentages shown below are for the top 20 researcher home countries, representing 76% of the community; the remaining researchers are distributed across ~134 additional countries (Figure 15).

For enterprises, this global spread means always-on coverage across time zones and the benefit of regional perspectives that single-location teams cannot provide.

**Figure 15 - Representation of HackerOne community members in top 20 countries (2025)**
- India: 22%
- United States: 15%
- United Kingdom: 4%
- China: 4%
- Pakistan: 2%
- Indonesia: 2%
- Germany: 2%
- Turkey: 2%
- Egypt: 2%
- Brazil: 2%
- Other (rest of the world): 24%

![World map with countries color-coded to represent the percentage of HackerOne community members from each country.](image_description)

13 | 9th Edition Hacker-Powered Security Report 2025/2026

# Part III - Building Best-in-Class Security Programs

Defense in depth highlights the value of layering safeguards and testing approaches to reduce the risk of a single point of failure. In the context of vulnerability discovery, combining methods such as code review, penetration testing, AI red teaming, vulnerability disclosure programs, and bug bounties ensures that different perspectives surface flaws that others may overlook.

However, layering defenses alone does not guarantee effectiveness. The true measure of success lies in how well findings are prioritized, how quickly the most exploitable risks are mitigated, and how seamlessly each layer of insight informs the next.

This section examines what makes security programs truly effective for organizations seeking resilience and for the researchers driving meaningful impact.

## A Year in Review

In the past 12 months, HackerOne bug bounty programs collectively paid out $81 million, an increase of 13% YoY. The top 10 programs alone accounted for $21.6 million. At the researcher level, the Top 100 all-time earners took a total of $31.8M, with individual researchers now consistently surpassing six-figure annual earnings.

- **Total paid out in 2025**: $81M
- **Average yearly payout across all active programs**: $42K
- **Total earned by top 10 researchers**: $7.6M
- **Total earned by top 100 researchers**: $31.8M
- **Total paid out by the top 10 programs**: $21.6M
- **Paid out by the top 100 programs**: $51.4M

**65%** of surveyed organizations report stronger outcomes after adopting a defense in depth approach, with bug bounty now in use at 83%.

14 | 9th Edition Hacker-Powered Security Report 2025/2026

# Maturing Identity and Access: Signals from the Market

The YoY payout and valid report data (Figure 16) suggest positive signals in defenders improving identity and access security; however, the details matter.

**Figure 16 - Valid vulnerability reports and rewards comparison**

| Vulnerability Type                 | 2025 Rewards ($)      | 2025 Valid Reports | YoY Change (Reports) |
| :--------------------------------- | :-------------------- | :----------------- | :------------------- |
| Cross-Site Scripting (XSS)         | $8,377,704 (↓ 7% YoY) | 13,197 (↓ 14% YoY) | ↓ 14%                |
| Improper Access Control (IAC)      | $8,797,644 (↑ 19% YoY)| 8,787 (↑ 18% YoY)  | ↑ 18%                |
| Insecure Direct Object Reference (IDOR) | $7,610,517 (↑ 23% YoY)| 6,016 (↑ 29% YoY)  | ↑ 29%                |
| Information Disclosure             | $4,682,524 (0% YoY)   | 8,013 (↓ 2% YoY)   | ↓ 2%                 |
| Misconfiguration                   | $2,717,656 (↑ 22% YoY)| 6,105 (↑ 29% YoY)  | ↑ 29%                |
| Improper Authentication            | $2,353,009 (↓ 22% YoY)| 1,737 (↓ 9% YoY)   | ↓ 9%                 |
| Business Logic Errors              | $2,262,840 (↓ 5% YoY) | 2,001 (↑ 19% YoY)  | ↑ 19%                |
| Code Injection                     | $1,715,704 (↑ 10% YoY)| 1,043 (↓ 1% YoY)   | ↓ 1%                 |
| Server Side Request Forgery (SSRF) | $1,521,303 (0.5% YoY) | 822 (0.2% YoY)     | 0.2%                 |
| Privilege Escalation               | $1,454,399 (↓ 7% YoY) | 1,766 (↓ 8% YoY)   | ↓ 8%                 |
| SQL Injection (SQLi)               | $1,302,696 (↓ 24% YoY)| 1,213 (↓ 23% YoY)  | ↓ 23%                |
| Uncontrolled Resource Consumption  | $1,024,036 (↓ 11% YoY)| 659 (↓ 10% YoY)    | ↓ 10%                |
| Improper Authorization             | $961,750 (↓ 43% YoY)  | 1,168 (↓ 9% YoY)   | ↓ 9%                 |

15 | 9th Edition Hacker-Powered Security Report 2025/2026

### Authorization taxonomies are changing labels

The drop in Improper Authorization, alongside the rise in Improper Access Control (IAC) and Insecure Direct Object Reference (IDOR), is proof that organizations have not solved authorization. Instead, it reflects a more precise classification of these vulnerabilities by researchers and triage teams. While this improvement in taxonomy provides better clarity, the underlying risk of broken access boundaries across API's, microservices, and multi-tenant SaaS continues to climb. Hackbots are expected to accelerate this trend by increasingly automating the discovery and exploitation of these vulnerabilities, potentially reducing their relevance altogether.

**Don’t let shifting labels hide persistent systemic weaknesses.**

### Commodity bugs are entering saturation, accelerated by AI

XSS and SQL Injection are in decline, while Server-Side Request Forgery (SSRF) and Information Disclosure remain flat. This suggests that commodity bug classes are reaching a maturity point where they are no longer easy, high-value targets for attackers and researchers.

### Identity risk is improving

Improper Authentication fell in both payouts and valid reports this year, suggesting progress in hardening authentication flows and wider adoption of stronger identity providers. The decline should be viewed as a sign of progress rather than closure. Continued investment in identity assurance and monitoring is essential.

### Business logic flaws are the premium battleground

Valid reports for business logic flaws increased this year, highlighting the persistent difficulty in securing complex workflows and systemic abuse paths. However, payouts for these vulnerabilities declined, suggesting programs are not consistently treating them as premium findings. Business logic flaws remain high-risk. Align prioritization and rewards towards business impact.

**Reallocate incentives, avoid overpaying for table stakes issues, while maintaining hygiene baselines to prevent attackers from exploiting residual long-tail risks.**

16 | 9th Edition Hacker-Powered Security Report 2025/2026

# Incentives Drive Outcomes

HackerOne examined 68 cases where programs reduced bounty payouts by at least 20% between 2018 and 2025. For each case, we measured valid vulnerability reports in the 12 weeks before the cut and compared them to the 12 weeks after. The pattern was consistent: lowering bounties led to fewer valid reports. Across all severities, programs averaged a 22% decline (Figure 17), while critical vulnerabilities dropped by half (Figure 18).

**Figure 17 - Impact of total bounty decreases (weekly)**
- Bounty Change (%): Regression line Median: -54%
- Report Volume Change (%): Regression line Median: -35%

![Scatter plot showing the relationship between bounty change and report volume change.](image_description)

**Figure 18 - Impact of critical bounty decreases (weekly)**
- Bounty Change (%): Regression line Median: -73%
- Report Volume Change (%): Regression line Median: -22%

![Scatter plot showing the relationship between bounty change and critical report volume change.](image_description)

**Why it matters**
Bounties are not cosmetic. When payouts fall, researchers disengage and the flow of valid reports slows. Maintaining competitive rewards is essential to sustain researcher participation and visibility into the highest-risk weaknesses.

17 | 9th Edition Hacker-Powered Security Report 2025/2026

# The Five-Year Outlook: From Signals to Strategy

The YoY data (Figure 16) on page 15 highlights short-term shifts, but the five-year view (Figure 19) of the top 10 most common vulnerabilities confirms which signals are structural and which are noise.

**Authorization is structurally climbing**
IDOR reports more than doubled in five years (+116%). Improper Access Control rose 66%. By contrast, XSS volumes grew only 10% in five years, with declining payouts. The signal from one-year data is confirmed at scale: authorization is where attackers are concentrating.

**Design-level flaws are rising, but undervalued**
Violation of Secure Design Principles grew 21% over five years. Business Logic Errors climbed 19% in valid reports YoY, but payouts fell 5%. Since 2022, these categories show steady growth in researcher attention without equivalent program investment.

**Identity is steady in volume, steep in impact**
Improper Authentication declined 20% in five years, echoing this year’s short-term drop. Yet payouts remain disproportionately high relative to volume. This confirms identity risk is not cyclical; fewer flaws are being found, but each carries a higher business impact.

**Figure 19 - Top 10 most common vulnerabilities YoY (2021-2025)**
- XSS
- Information Disclosure
- Improper Access Control – Generic
- Privilege Escalation
- Insecure Direct Object Reference (IDOR)
- Violation of Secure Design Principles
- Improper Authentication – Generic
- Business Logic Errors
- Open Redirect
- Misconfiguration

![Line graph showing the trend of the top 10 most common vulnerabilities from 2021 to 2025.](image_description)

**Why this matters**
Winning the next five years is about context and depth. Security leaders should use automation and emerging agentic workflows to keep commodity flaws like XSS and SQLi inexpensive, while prioritizing identity, access, and design-level weaknesses that drive material risk. The winning strategy is hybrid: agents and automation for scale, human ingenuity for impact.