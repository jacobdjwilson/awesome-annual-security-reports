# 2025 State of Software Security Report

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

Niels Tanis, Senior Principal Security Researcher  
Sohail Iqbal, Chief Information Security Officer  
Chris Wysopal, Chief Security Evangelist

---

## Executive Summary

In 2025, organizations face increasing threats to their software. The exploitation of vulnerabilities as the critical path to initiate a breach “almost tripled (180% increase) in the last year,” according to the Verizon 2024 Data Breach Investigations Report.

Meanwhile, security debt is rising, and the attack surface is getting increasingly complex. Plus, the rise of AI in software engineering, especially with code generators, is transforming the risk landscape. While many teams may not openly admit to using AI, other indicators of its presence and impact can be found.

> "I won't say I'm using AI to generate code… but there will be signs."

We also can’t ignore the trends in the regulatory space that are happening in the U.S. and the E.U. In the EU, the Cyber Resilience Act went into effect December 2024 and focuses especially on enhancing the security of software. In the U.S. 2020 Biden Cybersecurity Executive Order emphasized cybersecurity prevention with Zero Trust network architectures and Secure by Design software. Secure by Design included static code analysis, dynamic code analysis, and supply chain security with SBOMs.

The U.S. Federal Government even required vendors to attest to the way they developed software as part of the acquisition process. Understanding your software risk posture is now a requirement. 2024 also gave us a new U.S. Securities and Exchange Commission (SEC) ruling which forces a more disciplined approach to cybersecurity risk management.

We believe these regulatory factors have contributed to some of the positive trends we see in the data, such as the OWASP Top 10 pass rate improving from 32% to 52% in the last five years. However, our findings reveal that relying on traditional patching alone isn’t enough. Security teams must take a more strategic, context-driven approach to managing the most urgent and exploitable risks.

---

## Key Findings

- **OWASP Improvement**: The percentage of apps passing the OWASP Top 10 has increased 63% in 5 years (from 32% in 2020 to 52% in 2025).
- **High Severity Flaws**: The percentage of apps with high severity flaws has increased by 181%.
- **Fix Speed**: The average number of days to fix flaws has increased 47% (from 171 days in 2020 to 252 days in 2025).
- **Security Debt**: Half of organizations have critical security debt (high severity, high exploitability).
- **Supply Chain**: 70% of critical security debt comes from third-party code and the software supply chain.

### Comparison of Leading vs. Lagging Organizations

| Metric | Leading Organizations | Lagging Organizations |
| :--- | :--- | :--- |
| **Flaw Prevalence** | Below 43% | 86% or more |
| **Fix Capacity** | Above 10% of flaws monthly | <1% of flaws monthly |
| **Fix Speed** | Half of flaws in 5 weeks | Half of flaws in over a year |
| **Security Debt** | <17% of apps | <15% |
| **Open-Source Critical Debt** | >67% of apps | 100% |

---

## 15 Years of Special SoSS

![Infographic showing 15-year trends in application testing, flaw prevalence, and remediation times]

The fundamental challenge hasn’t changed over the years: security flaws are very common across applications. Even so, there are signs of progress in software security.

- **Sample Size**: The sample size for this study has grown from ~1,600 applications tested in 2009 to nearly half a million in 2024.
- **OWASP Pass Rate**: The pass rate for scans of OWASP’s most critical risks has more than doubled since Vol. 1.
- **High-Severity Flaws**: The prevalence of severe flaws in SAST scans was cut in half since Vol. 1. However, when including SCA and DAST, the increase in high-severity flaws is 181% since 2020.
- **Fix Times**: The time it takes to fix flaws has worsened, largely due to the growing scope and complexity of the software ecosystem.

---

## State of Software Security in 2025

The findings analyzed in this report were discovered via 1.8 million SAST, DAST, and SCA scans of nearly half a million applications.

### Finding Flaws
Figure 1 reveals that 80.3% of the applications tested over the last year have at least one security flaw. 47.7% have OWASP Top 10 flaws, and 56.2% exhibit high or critical severity flaws.

### Fixing Flaws
Survival analysis shows that 28% of flaws are still open two years after being discovered. After five years, 9% of flaws linger on. The half-life of flaws stands at just over eight months.

### Fighting Debt
Security debt refers to flaws that remain unfixed for over a year. 74.2% of organizations have accrued some level of debt, and 49.9% have critical security debt.

---

## Comparing Software Security Program Performance

We analyzed 20 example organizations to see how they manage security debt. Some organizations have almost no security debt, while others are drowning in it.

### Flaw Prevalence
The typical organization has security flaws in about two-thirds of its applications (median of 66%). Leading organizations maintain a flaw prevalence below 43%.

### Fix Capacity
The average monthly fix capacity for most applications is less than 10% of all flaws. Leading teams have fix capacities above 10%, while the bottom tier fixes just 1% of its flaws each month.

### Fix Speed
The typical organization takes about five months to fix half of all detected security flaws. Leading teams cross the halfway point in roughly five weeks.

### Debt Prevalence
Just over 10% of organizations have no security debt. A quarter of organizations with security debt have it in less than 17% of their applications, while lagging organizations struggle with debt in two-thirds of their applications or more.

### Open-Source Debt
The majority of an organization’s critical security debt exists in third-party code. Teams on the low end keep that proportion under 15%, while over a quarter of organizations live in the reality where all of their critical debt is contained in open-source libraries.

---

## Conclusions & Recommendations

To mature your software security program, you need:

1. **Visibility and integration across your SDLC**: Prevent net new flaws through automation and feedback loops. Use AI to address simple flaws at scale and implement policy to guide remediation.
2. **Correlate and contextualize findings**: Use an Application Security Posture Management solution to see what is exploitable, reachable, and urgent. Allocate a percentage of a security champion’s sprint capacity to prioritized security debt.

---

## Methodology

The report contains findings from 1.3M unique applications with 126.4M raw findings, including:
- 107.4M findings via SAST
- 3.9M findings via DAST
- 15M findings via Software Composition Analysis

"Mass closure" events (where thousands of findings are closed in a single scan due to file system scanning errors) were excluded from the analysis to ensure data integrity.

[^1]: All statistics in this 15-year retrospective are based on static analysis (SAST) scans only because that’s consistent with early versions of the SoSS. Combined stats from all scan types is the norm for this report unless otherwise noted.
[^2]: Remember that findings in this report combine SAST, DAST, and SCA scans unless otherwise noted.
[^3]: Another benefit of survival analysis is that it accounts for “censored data” that includes flaws still open when our measurement period ends.
[^4]: We filtered this to applications that have been actively tested for at least one year to allow for the accrual of debt.
[^5]: Here, we mean open-source developers who use Veracode tools on applications in the same way closed-source developers do. This is distinct from the software composition analysis presented in the report.