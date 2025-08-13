# 2025 STATE OF A NEW VIEW OF MATURITY

## Table of Contents
- [Opening letter](#opening-letter)
- [Executive Summary](#executive-summary)
  - [Key findings](#key-findings)
- [15 Years of Special SoSS](#15-years-of-special-soss)
- [State of Software Security in 2025](#state-of-software-security-in-2025)
  - [Finding flaws](#finding-flaws)
  - [Fixing flaws](#fixing-flaws)
  - [Fighting debt](#fighting-debt)
- [Comparing Software Security Program Performance](#comparing-software-security-program-performance)
  - [Flaw prevalance](#flaw-prevalance)
  - [Fix capacity](#fix-capacity)
  - [Fix speed](#fix-speed)
  - [Debt prevalence](#debt-prevalence)
  - [Open-source debt](#open-source-debt)
- [Conclusions & Recommendations](#conclusions-recommendations)
- [Methodology](#methodology)

---

## Opening letter

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

![Cartoon depicting a person saying "I won't say I'm using AI to generate code…" and another person saying "…but there will be signs."](Image description of cartoon)

The U.S. Federal Government even required vendors to attest to the way they developed software as part of the acquisition process. Understanding your software risk posture is now a requirement. 2024 also gave us a new U.S. Securities and Exchange Commission (SEC) ruling which forces a more disciplined approach to cybersecurity risk management.

We believe these regulatory factors have contributed to some of the positive trends we see in the data, such as the OWASP Top 10 pass rate improving from 32% to 52% in the last five years.

However, our findings reveal that relying on traditional patching alone isn’t enough. Security teams must take a more strategic, context-driven approach to managing the most urgent and exploitable risks. This requires seeing all risks in one place and focusing on what matters most to an organization. By prioritizing the most impactful risk remediation actions and creating continuous feedback loops for ongoing improvement, organizations can more effectively manage security risks over time.

### Key findings

Good news first, the percentage of apps passing the OWASP Top 10 has increased 63% in 5 years (from **32%** in **2020** to **52%** in **2025**).

Now the bad news... the percentage of apps with high severity flaws has increased by 181%... (**2020** to **2025**)

...and the average number of days to fix flaws has increased 47%. (**171 days** in **2020** to **252 days** in **2025**)

Half of organizations have critical security debt (high severity, high exploitability)... (**50%**)

...and 70% of it comes from third party code and the software supply chain.

**ALL SECURITY DEBT**
- Third party code: **11%**
- First party code: **89%**

**CRITICAL SECURITY DEBT**
- Third party code: **70%**
- First party code: **30%**

The following table is a comparison of the top 25% and bottom 25% of organizations against 5 key metrics we’ve observed indicate the maturity of an organization at finding and fixing flaws in a way that systematically drives down risk.

| LEADING ORGANIZATIONS | LAGGING ORGANIZATIONS |
| :-------------------- | :-------------------- |
| Below 43%             | 86% or more           |
| Above 10% of flaws monthly | <1% of flaws monthly |
| Half of flaws in 5 weeks | Half of flaws in over a year |
| <17% of apps          | >67% of apps          |
| <15%                  | 100%                  |

| METRIC                  |
| :---------------------- |
| FLAW PREVALENCE         |
| FIX CAPACITY            |
| FIX SPEED               |
| SECURITY DEBT           |
| OPEN-SOURCE CRITICAL DEBT |

## 15 Years of Special SoSS

As a pioneer of the AppSec space, we have years of data to our advantage. This 2025 edition of the State of Software Security (SoSS) report is our 15th volume. That makes it a bit more special than the norm and creates an opportunity to highlight a few long-term trends before we dive into the latest facts and figures.

**15 Years of Special SoSS**

| Metric                       | Volume 1 (2009) | Volume 10 (2018) | Volume 15 (2024) | Change since Vol 1 |
| :--------------------------- | :-------------- | :--------------- | :--------------- | :----------------- |
| **NUMBER OF APPLICATIONS TESTED** | 1,591           | 85,000           | 457,000          | +455,409           |
| **APPS WITH AT LEAST ONE FLAW** | 72%             | 80.3%            | 83%              | +11.5%             |
| **OWASP TOP 10 PASS RATE**   | 23%             | 34%              | 52.3%            | +127.4%            |
| **APPS WITH HIGH-SEVERITY FLAWS** | 16%             | 20%              | 56.2% (Note 1)   | -52.9% (SAST only) |
| **AVERAGE NUMBER OF DAYS TO FIX FLAWS** | 59              | 171              | 252              | +193 DAYS          |

Note:
- Positive change since Vol 1
- Negative change since Vol 1

The fundamental challenge hasn’t changed over the years: security flaws are very common across applications. Even so, there are signs of progress in software security.

The pass rate for scans of OWASP’s most critical risks has more than doubled since Vol. 1. That means less risk for us all!

The sample size for this study has grown from ~1,600 applications tested in 2009 to nearly half a million in 2024! That strengthens the relevance of the findings in this report.

The prevalence of severe flaws in SAST scans was cut in half since Vol. 1. However, when you add in SCA (which only started in the last 5 years) and DAST, the increase in high-severity flaws is 181% since 2020 (from 20% with SAST only in 2020 to 56.2% in 2025 including all scan types).

One aspect of AppSec that’s gotten worse over iterations of the SoSS is the time it takes to fix flaws. There are many reasons for this, but the ever-growing scope and complexity of the software ecosystem is a core issue. On the bright side, we do see organizations reversing this trend. We’ll share insights gleaned from them in this report.

1. All statistics in this 15-year retrospective are based on static analysis (SAST) scans only because that’s consistent with early versions of the SoSS. You’ll see that the “State of” section shows some very