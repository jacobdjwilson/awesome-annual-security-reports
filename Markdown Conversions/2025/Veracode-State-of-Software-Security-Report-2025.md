# 2025 STATE OF SOFTWARE SECURITY: A NEW VIEW OF MATURITY

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
- [Conclusions & Recommendations](#conclusions-and-recommendations)
- [Methodology](#methodology)
  - [A Note on Mass Closures](#a-note-on-mass-closures)

---

## Opening Letter

Our research drives our own software security measures, and this year, in our 15th volume of this report, we seek to discover trends about where the most risk resides and what metrics can be used to gauge progress against it. Plus, we want to compare program performance of leading and lagging organizations using these metrics. The gaps between the top 25% and bottom 25% are fascinating.

Ultimately, realizing progress and maturity in software security requires a risk-based perspective. It takes focusing on the downside risks that matter in your context and the actions that create continuous feedback loops to see and remediate risk in an ongoing fashion.

This is easier said than done, so we hope you find the insights and guidance in this report as helpful as we have for improving security posture by adaptively securing mission-critical software in the artificial intelligence (AI) era.

Sincerely,

Niels Tanis
Senior Principal
Security Researcher

Sohail Iqbal
Chief Information
Security Officer

Chris Wysopal
Chief Security
Evangelist

## Executive Summary

In 2025, organizations face increasing threats to their software. The exploitation of vulnerabilities as the critical path to initiate a breach “almost tripled (180% increase) in the last year,” according to the Verizon 2024 Data Breach Investigations Report.

Meanwhile, security debt is rising, and the attack surface is getting increasingly complex. Plus, the rise of AI in software engineering, especially with code generators, is transforming the risk landscape. While many teams may not openly admit to using AI, other indicators of its presence and impact can be found.

![Illustration of a person saying "I won't say I'm using AI to generate code…" and another person saying "…but there will be signs."](Image of two people talking about AI code generation)

We also can’t ignore the trends in the regulatory space that are happening in the U.S. and the E.U. In the EU, the Cyber Resilience Act went into effect December 2024 and focuses especially on enhancing the security of software. In the U.S. 2020 Biden Cybersecurity Executive Order emphasized cybersecurity prevention with Zero Trust network architectures and Secure by Design software. Secure by Design included static code analysis, dynamic code analysis, and supply chain security with SBOMs.

The U.S. Federal Government even required vendors to attest to the way they developed software as part of the acquisition process. Understanding your software risk posture is now a requirement. 2024 also gave us a new U.S. Securities and Exchange Commission (SEC) ruling which forces a more disciplined approach to cybersecurity risk management.

We believe these regulatory factors have contributed to some of the positive trends we see in the data, such as the OWASP Top 10 pass rate improving from 32% to 52% in the last five years.

However, our findings reveal that relying on traditional patching alone isn’t enough. Security teams must take a more strategic, context-driven approach to managing the most urgent and exploitable risks. This requires seeing all risks in one place and focusing on what matters most to an organization. By prioritizing the most impactful risk remediation actions and creating continuous feedback loops for ongoing improvement, organizations can more effectively manage security risks over time.

### Key Findings

Good news first, the percentage of apps passing the OWASP Top 10 has increased 63% in 5 years (from 32% to 52%)

| 2020 | 2025 |
| :--- | :--- |
| 32%  | 52%  |

Now the bad news... the percentage of apps with high severity flaws has increased by 181%...

...and the average number of days to fix flaws has increased 47%.

| 2020    | 2025    |
| :------ | :------ |
| 171 days | 252 days |

Half of organizations have critical security debt (high severity, high exploitability)...

...and 70% of it comes from third party code and the software supply chain.

| ALL SECURITY DEBT | CRITICAL SECURITY DEBT |
| :---------------- | :--------------------- |
| Third party code: 11% | Third party code: 70%  |
| First party code: 89% | First party code: 30%  |

The following table is a comparison of the top 25% and bottom 25% of organizations against 5 key metrics we’ve observed indicate the maturity of an organization at finding and fixing flaws in a way that systematically drives down risk.

| METRIC                  | LEADING ORGANIZATIONS | LAGGING ORGANIZATIONS |
| :---------------------- | :-------------------- | :-------------------- |
| FLAW PREVALENCE         | Below 43%             | 86% or more           |
| FIX CAPACITY            | Above 10% of flaws monthly | <1% of flaws monthly  |
| FIX SPEED               | Half of flaws in 5 weeks | Half of flaws in over a year |
| SECURITY DEBT           | <17% of apps          | >67% of apps          |
| OPEN-SOURCE CRITICAL DEBT | <15%                  | 100%                  |

## 15 Years of Special SoSS

As a pioneer of the AppSec space, we have years of data to our advantage. This 2025 edition of the State of Software Security (SoSS) report is our 15th volume. That makes it a bit more special than the norm and creates an opportunity to highlight a few long-term trends before we dive into the latest facts and figures.

![Infographic showing 15 years of State of Software Security (SoSS) data across Volume 1 (2009), Volume 10 (2018), and Volume 15 (2024). It compares metrics such as Number of Applications Tested, Apps with at Least One Flaw, OWASP Top 10 Pass Rate, Apps with High-Severity Flaws, and Average Number of Days to Fix Flaws. Positive and negative changes since Volume 1 are indicated. For example, Number of Applications Tested increased by +455,409, OWASP Top 10 Pass Rate increased by +127.4%, and Average Number of Days to Fix Flaws increased by +193 days.](Infographic: 15 Years of Special SoSS)

The fundamental challenge hasn’t changed over the years: security flaws are very common across applications. Even so, there are signs of progress in software security.

The pass rate for scans of OWASP’s most critical risks has more than doubled since Vol. 1. That means less risk for us all!

The sample size for this study has grown from ~1,600 applications tested in 2009 to nearly half a million in 2024! That strengthens the relevance of the findings in this report.

The prevalence of severe flaws in SAST scans was cut in half since Vol. 1. However, when you add in SCA (which only started in the last 5 years) and DAST, the increase in high-severity flaws is 181% since 2020 (from 20% with SAST only in 2020 to 56.2% in 2025 including all scan types).

One aspect of AppSec that’s gotten worse over iterations of the SoSS is the time it takes to fix flaws. There are many reasons for this, but the ever-growing scope and complexity of the software ecosystem is a core issue. On the bright side, we do see organizations reversing this trend. We’ll share insights gleaned from them in this report.

[^1]: All statistics in this 15-year retrospective are based on static analysis (SAST) scans only because that’s consistent with early versions of the SoSS. You’ll see that the “State of” section shows some very different results from the latest data drawn from all SAST, dynamic analysis (DAST), and software composition analysis (SCA) scans (e.g., 56% of apps have high-severity flaws). Combined stats from all scan types is the norm for this report unless otherwise noted.

## State of Software Security