# 2025 State of Software Security: A New View of Maturity

## Table of Contents
- [Opening Letter](#opening-letter)
- [Executive Summary](#executive-summary)
- [Key Findings](#key-findings)
- [15 Years of Special SoSS](#15-years-of-special-soss)
- [State of Software Security in 2025](#state-of-software-security-in-2025)
- [Finding Flaws](#finding-flaws)
- [Fixing Flaws](#fixing-flaws)
- [Fighting Debt](#fighting-debt)
- [Comparing Software Security Program Performance](#comparing-software-security-program-performance)
- [Flaw Prevalence](#flaw-prevalence)
- [Fix Capacity](#fix-capacity)
- [Fix Speed](#fix-speed)
- [Debt Prevalence](#debt-prevalence)
- [Open-Source Debt](#open-source-debt)
- [Conclusions & Recommendations](#conclusions--recommendations)
- [Methodology](#methodology)

---

## Opening Letter
Our research drives our own software security measures, and this year, in our 15th volume of this report, we seek to discover trends about where the most risk resides and what metrics can be used to gauge progress against it. Plus, we want to compare program performance of leading and lagging organizations using these metrics. The gaps between the top 25% and bottom 25% are fascinating.

Ultimately, realizing progress and maturity in software security requires a risk-based perspective. It takes focusing on the downside risks that matter in your context and the actions that create continuous feedback loops to see and remediate risk in an ongoing fashion.

This is easier said than done, so we hope you find the insights and guidance in this report as helpful as we have for improving security posture by adaptively securing mission-critical software in the artificial intelligence (AI) era.

Sincerely,
Niels Tanis (Senior Principal Security Researcher), Sohail Iqbal (Chief Information Security Officer), Chris Wysopal (Chief Security Evangelist)

---

## Executive Summary
In 2025, organizations face increasing threats to their software. The exploitation of vulnerabilities as the critical path to initiate a breach “almost tripled (180% increase) in the last year,” according to the Verizon 2024 Data Breach Investigations Report.

Meanwhile, security debt is rising, and the attack surface is getting increasingly complex. Plus, the rise of AI in software engineering, especially with code generators, is transforming the risk landscape. While many teams may not openly admit to using AI, other indicators of its presence and impact can be found.

Understanding your software risk posture is now a requirement. 2024 also gave us a new U.S. Securities and Exchange Commission (SEC) ruling which forces a more disciplined approach to cybersecurity risk management.

We also can’t ignore the trends in the regulatory space that are happening in the U.S. and the E.U. In the EU, the Cyber Resilience Act went into effect December 2024 and focuses especially on enhancing the security of software. In the U.S. 2020 Biden Cybersecurity Executive Order emphasized cybersecurity prevention with Zero Trust network architectures and Secure by Design software. Secure by Design included static code analysis, dynamic code analysis, and supply chain security with SBOMs.

We believe these regulatory factors have contributed to some of the positive trends we see in the data, such as the OWASP Top 10 pass rate improving from 32% to 52% in the last five years. However, our findings reveal that relying on traditional patching alone isn’t enough. Security teams must take a more strategic, context-driven approach to managing the most urgent and exploitable risks.

---

## Key Findings
- The percentage of apps passing the OWASP Top 10 has increased 63% in 5 years (from 32% to 52%).
- The percentage of apps with high severity flaws has increased by 181% (2020: 20% vs 2025: 56.2%).
- The average number of days to fix flaws has increased 47% (2020: 171 days vs 2025: 252 days).
- Half of organizations have critical security debt (high severity, high exploitability).
- 70% of critical security debt comes from third-party code and the software supply chain.

---

## 15 Years of Special SoSS
![Chart showing 15 years of growth in applications tested, from 1,600 in 2009 to nearly half a million in 2024.]

The sample size for this study has grown from ~1,600 applications tested in 2009 to nearly half a million in 2024. The fundamental challenge hasn’t changed: security flaws are very common across applications. However, the prevalence of severe flaws in SAST scans was cut in half since Vol. 1. One aspect that has worsened is the time it takes to fix flaws, largely due to the growing scope and complexity of the software ecosystem.

---

## State of Software Security in 2025
The findings analyzed in this report were discovered via 1.8 million SAST, DAST, and SCA scans of nearly half a million applications.

### Finding Flaws
![Chart showing 80.3% of applications have any flaws, 47.7% have OWASP Top 10 flaws, 38.7% have CWE Top 25 flaws, and 56.2% have high severity flaws.]

### Fixing Flaws
Survival analysis shows that 28% of flaws are still open two years after discovery, and 9% linger after five years. The half-life of flaws stands at 252 days.

### Fighting Debt
Security debt refers to flaws that remain unfixed for over a year. 74.2% of organizations have security debt, and 49.9% have critical security debt.

---

## Comparing Software Security Program Performance
We compared the top 25% and bottom 25% of organizations against 5 key metrics:
1. **Flaw Prevalence**: Leading (<43%) vs. Lagging (86% or more).
2. **Fix Capacity**: Leading (>10% of flaws monthly) vs. Lagging (<1% of flaws monthly).
3. **Fix Speed**: Leading (Half of flaws in 5 weeks) vs. Lagging (Half of flaws in over a year).
4. **Security Debt**: Leading (<17% of apps) vs. Lagging (>67% of apps).
5. **Open-Source Critical Debt**: Leading (<15%) vs. Lagging (100%).

---

## Conclusions & Recommendations
The new view of software security maturity requires:
1. **Visibility and integration across your SDLC**: Prevent net new flaws through automation and feedback loops. Use AI to boost fix capacity and speed.
2. **Correlate and contextualize findings**: Use an Application Security Posture Management solution to prioritize what is exploitable, reachable, and urgent.

---

## Methodology
The report contains findings from 1.3M unique applications with 126.4M raw findings, including 107.4M via SAST, 3.9M via DAST, and 15M via Software Composition Analysis. "Mass closure" events (where thousands of flaws are closed in a single scan due to filesystem or branch errors) were excluded from the analysis to ensure data integrity.

[^1]: All statistics in this 15-year retrospective are based on static analysis (SAST) scans only because that’s consistent with early versions of the SoSS. Combined stats from all scan types is the norm for this report unless otherwise noted.