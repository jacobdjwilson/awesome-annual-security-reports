# 2021 Application Security Observability Report

## Table of Contents
- [Foreword](#foreword)
- [Executive Summary](#executive-summary)
- [Introduction](#introduction)
- [Application Makeup: More Custom Code Than Assumed](#application-makeup-more-custom-code-than-assumed)
  - [By Language](#by-language)
- [Routes: Vulnerabilities Decline Later in the SDLC](#routes-vulnerabilities-decline-later-in-the-sdlc)
  - [Route Intelligence](#route-intelligence)
- [Custom Code Vulnerabilities: More Likely To Be Serious](#custom-code-vulnerabilities-more-likely-to-be-serious)
  - [Vulnerabilities Per Application](#vulnerabilities-per-application)
  - [By Likelihood And Impact](#by-likelihood-and-impact)
  - [By Language](#by-language-1)
  - [By Application Age](#by-application-age)
  - [For Applications With 80%+ Route Coverage](#for-applications-with-80-route-coverage)
  - [Vulnerability Escape Rate (Ver)](#vulnerability-escape-rate-ver)
- [Open-Source Libraries And Frameworks: Organizations Struggle To Keep Up](#open-source-libraries-and-frameworks-organizations-struggle-to-keep-up)
  - [Active Libraries And Classes](#active-libraries-and-classes)
  - [Open-Source Vulnerabilities](#open-source-vulnerabilities)
  - [Most Cves Are False Positives](#most-cves-are-false-positives)
  - [Sidebar: Library Age: Older Libraries Can Compound Risk](#sidebar-library-age-older-libraries-can-compound-risk)
- [Security Debt: Organizations Are Making Progress](#security-debt-organizations-are-making-progress)
- [Vulnerability Remediation: Slower But Much Better Than Traditional Approaches](#vulnerability-remediation-slower-but-much-better-than-traditional-approaches)
  - [Compared With Last Year](#compared-with-last-year)
  - [Compared With Traditional Practices](#compared-with-traditional-practices)
  - [By Level Of Security Debt](#by-level-of-security-debt)
- [Attacks: Increased Prevalence, Decreased Viability](#attacks-increased-prevalence-decreased-viability)
  - [By Language](#by-language-2)
- [Contrast Riskscore™ Index: Overall, A Downward Trend](#contrast-riskscore-index-overall-a-downward-trend)
  - [Sidebar: Contrast Riskscore Index](#sidebar-contrast-riskscore-index)
- [Conclusion](#conclusion)
- [Report Contributors](#report-contributors)

---

# 2021 REPORT

## 2021 Application Security Observability Report

Understanding Application and API Risk by Connecting Real-world Vulnerabilities With Actual Attack Data

contrastsecurity.com

---

## Table of Contents

01
Foreword

02
Executive Summary

03
Introduction

04
Application Makeup: More Custom Code Than Assumed

* By Language

05
Routes: Vulnerabilities Decline Later in the SDLC

* Sidebar: Route Intelligence

06
Custom Code Vulnerabilities: More Likely To Be Serious

* Vulnerabilities Per Application
* By Likelihood And Impact
* By Language
* By Application Age
* For Applications With 80%+ Route Coverage
* Vulnerability Escape Rate (Ver)

07
Open-Source Libraries And Frameworks: Organizations Struggle To Keep Up

* Active Libraries And Classes
* Open-Source Vulnerabilities
* Most Cves Are False Positives
* Sidebar: Library Age: Older Libraries Can Compound Risk

08
Security Debt: Organizations Are Making Progress

09
Vulnerability Remediation: Slower But Much Better Than Traditional Approaches

* Compared With Last Year
* Compared With Traditional Practices
* By Level Of Security Debt

10
Attacks: Increased Prevalence, Decreased Viability

* By Language

11
Contrast Riskscore™ Index: Overall, A Downward Trend

* Sidebar: Contrast Riskscore Index

12
Conclusion

13
Report Contributors

---

# 01 | Foreword

Disruptive change in the marketplace has been the name of the game for some time, and this trend promises to continue in the months and years to come. Businesses were already embracing digital transformation before the COVID-19 pandemic, which rapidly accelerated digital adoption—with McKinsey indicating late last year that the share of digital and digitally enabled products leapfrogged an astounding seven years in the past year.¹

Companies with the agility to evolve with current trends and quickly tap new revenue opportunities are best positioned to survive and thrive in the new economy. And more than ever before, software applications are a critical part of that agility. Yet, the application layer is an increasingly attractive target for cyber criminals, with high-profile software supply chain attacks on SolarWinds, Microsoft Exchange, and Kaseya making headlines in the past six months. Overall, 39% of data breaches in the past year have been the result of an application vulnerability.²

In this context, we are pleased to present Contrast Labs’ second annual Application Security Observability Report. Our flagship research report covers the past 12 months of telemetry data from our different product offerings—Contrast Assess, Contrast Protect, and Contrast OSS. Contrast is the only player in the marketplace to present findings from vulnerability, attack, and open-source library data in a single report. This year, we added data on application makeup and the vulnerability escape rate (VER), both of which bring fascinating insights. In addition, we also added data on which potential routes are exercised within applications using data from our Route Intelligence functionality, released in March 2020.

Our goal with this report is to guide organizations as they strive to grow digital innovation while maintaining application security. Accordingly, we focus first on the nuts and bolts of how software is structured—the active and inactive code that makes up the software and how many routes are exercised. We then focus on custom code vulnerabilities and open-source libraries and frameworks. We then move to data about vulnerability remediation and security debt and to telemetry about application attacks. Finally, we update the Contrast RiskScore Index, which provides an easy-to-understand score that helps organizations better understand the risk of various vulnerability types.

Throughout these analyses, a few themes pop up repeatedly. First and foremost, effective application security is a matter of good prioritization of prevention and response efforts. This year, we find that only 6% of the code in a typical application is from active third-party library classes, while 20% is custom code. This means that 74% of the code in applications is third-party content that is never invoked by the application, and vulnerabilities in this code pose no risk to an organization and should be deprioritized.

6

contrastsecurity.com

A second recurring theme is the need for comprehensive observability into all aspects of application security throughout the software development life cycle (SDLC). This includes immediate feedback when a vulnerability is created, visibility into which open-source content is active, and which attacks are probes versus those that target existing vulnerabilities and hence could cause damage. Such observability enables organizations to deal with new vulnerabilities as they occur and to reduce their security debt over time.

This brings us to a third theme in the research: the need to resolve vulnerabilities quickly to ensure the timely delivery of secure software into production. Our research finds that Contrast customers deliver on this priority almost 29 times more quickly than customers of a well-known vendor of traditional application security tools, according to their research. And the Contrast platform has the added benefit of helping developers learn to introduce fewer vulnerabilities into their code, reducing their vulnerability escape rate (VER) from initial deployment to one year by 92%.

Our 2021 report provides a snapshot in time of where things stand with the applications developed by the Contrast customer community. The security observability provided by the Contrast Application Security Platform enables their development, security, and operations teams to work together to secure their software—and deliver to increasingly aggressive deadlines in a fast-changing marketplace.

Sincerely,

Jeff Williams
Cto and Co-Founder

David Lindner
Chief Information Security Officer

7

contrastsecurity.com

---

# 02 | Executive Summary

Contrast Labs’ second annual Application Security Observability Report takes a broad look at the state of application security at a critical moment in the economy—while digital transformation continues at an accelerated pace, businesses reopen their office locations, and corporate leaders discern the next phase of how work is structured. The data comes from aggregate telemetry from applications and application programming interfaces (APIs) protected by the Contrast Application Security Platform. It includes data on vulnerabilities, attacks, and open-source libraries between June 2020 and May 2021. Such comprehensive reporting from across the software development life cycle (SDLC) is only available from Contrast.

## 78% OF ACTIVE CODE IS CUSTOM

The fact that 70% or more of the code in the typical application comes from open-
source libraries and frameworks has been widely noted in recent years. What is not
usually revealed in these reports is that the vast majority of this code is not used by
the application. Our data shows that 80% of code is open source, but only 6% of code
belongs to an active library or class. The other 74% is from inactive libraries or inactive
classes within active libraries. When this is taken into account, 78% of active code in
the typical application is custom code and only 22% comes from open sources.

### APPLICATION MAKEUP

*   **Custom Code**: 20%
*   **Active Library Classes**: 6%
*   **Inactive Libraries and Inactive Classes Within Active Libraries**: 74%

### FALSE-POSITIVE RATE

*   **for Critical CVEs**: 54%
*   **for Major CVEs**: 49%

9

contrastsecurity.com

## 39% OF CUSTOM CODE VULNERABILITIES ARE SERIOUS

Overall, a greater share of applications had custom code vulnerabilities than in the
prior 12-month period. Most concerning is the 21% increase in the percentage of
applications with at least one serious vulnerability—34% this year compared with 26%
last year. Overall, 13% of applications have one or two serious vulnerabilities, while 3%
have more than 100. And 39% of all vulnerabilities identified are serious, defined as
High or Critical—a 39% increase over last year’s 28% figure.

The top two vulnerability types in terms of percentage of applications affected are
broken access control and cross-site scripting (XSS). Unfortunately, both of these
vulnerability types were found in a larger share of applications this year than last year.
As in the past, more Java applications have serious vulnerabilities than .NET ones—
44% versus 23%.

*   **34% of Applications Have a Serious Vulnerability** (21% increase over last year)
*   **18% of Applications Impacted by Broken Access Control and Cross-site Scripting Vulnerabilities**
*   **39% of Vulnerabilities Are High or Critical**
*   **13% of Applications Have 1 to 2 Serious Vulnerabilities; 3% Have 100+**

10

contrastsecurity.com

## VULNERABILITY ESCAPE RATE (VER) FALLS FROM 18 TO 1 IN 12 MONTHS

The good news is that Contrast enables developers to improve the security of their
coding over time. With its immediate feedback when a vulnerability is created, the
platform provides actionable instructions on how to fix the problem—and avoid making
the same mistake again in the future. The result is akin to “just-in-time” security
training—something that learning managers have struggled to provide for developers
for years.

This phenomenon shows up in our data in what we are calling the vulnerability
escape rate (VER). In the first two months of an application’s tenure on the Contrast
Application Security Platform, an average 12 vulnerabilities—six of them serious—occur
in the software. But these numbers shrink steadily, reaching 6 total vulnerabilities
and 3 serious in the ninth month. By the end of the first year, the average application
sees no new serious vulnerabilities and just one non-serious one each month—a 92%
decline. As in the past, more Java applications have serious vulnerabilities than .NET
ones—44% versus 23%.

*   **12 TO 1**: The average vulnerability escape rate fell from 12 per month to 1 per month in 12 months—92% reduction

## 54% OF CRITICAL CVES ARE FALSE POSITIVES

Our data on application makeup, discussed above, upends a commonly held view
of application security risk, as vulnerabilities that exist within the 74% of code that
is inactive pose no risk to an organization. Traditional software composition analysis
(SCA) tools do not differentiate between active and inactive code. As a result, every
Common Vulnerability and Exposure (CVE) they identify that occurs in inactive code
is actually a false positive. In our dataset, a majority of vulnerabilities—including 54%
of CVEs rated as Critical and 49% rated as Major—would be false positives with
traditional tools.

Nevertheless, good library hygiene such as keeping versions relatively up to date is
important for reducing application security risk. Unfortunately, 45% of libraries found
in applications are more than two years old.

11

contrastsecurity.com

### FALSE-POSITIVE RATE

*   **for Critical CVEs**: 54%
*   **for Major CVEs**: 49%

## MEDIAN TIME TO REMEDIATION NEARLY 29X BETTER THAN TRADITIONAL APPSEC SOLUTIONS

The Contrast customers in the dataset saw much better remediation timelines than
organizations using legacy application security tools. The median time to remediation—
the time it takes to resolve half of all closed vulnerabilities—was just 3 days in our
dataset. This was 29 times faster than the 86 days reported by a traditional static
application security testing (SAST) vendor. Nearly three-quarters (74%) of serious
vulnerabilities were remediated within 90 days, and 90% of them within a year.

*   **50% OF FIXED VULNERABILITIES CLOSED**:
    *   **3 DAYS**: Contrast Customers
    *   **86 DAYS**: Traditional SAST

## SECURITY DEBT PER APPLICATION 19% LOWER

The result of this astounding remediation timeline is that organizations are reducing
their per-application vulnerability backlog to 21 vulnerabilities, down from 26 in the
previous 12 months. This 19% decline translates into lower application risk.

12

contrastsecurity.com

## 99% OF ATTACKS WERE PROBES

The typical organization was pummeled with 25,343 application attacks every month
over the past year. But one of the biggest trends in the attack data for the past 12
months is that the percentage of attacks that were viable was cut in half—from 2%
last year to 1% this year. A viable attack is one that hits an existing vulnerability in
an application, and therefore has a chance of being successful. Eleven of the top
12 attack types impacted a larger share of applications this year than last year, with
big increases in broken access control, SQL injection, XSS, command injection, and
expression language (EL) injection.

*   **1% of Attacks Were Viable**, down From 2%
*   **Vulnerability types with attacks that rose by 9+ percentage points**: BROKEN ACCESS CONTROL, SQL INJECTION, XSS, COMMAND INJECTION, EL INJECTION

## RISKSCORE INDEX DOWN BY 1.25 POINTS ON AVERAGE

The report also updated the Contrast RiskScore Index, a numerical score that helps
organizations rank and visualize the risk posed by different vulnerability types over
time. The five highest RiskScores were quite consistent over the entire 12 months,
but the average RiskScore declined by more than 1.25 points over the course of a
year. This is because our data comes from Contrast Security customers, whose risk
level declines as they build tenure with the solution (viz., the number of vulnerabilities
being introduced declines and overall security increases). Vulnerability types that saw
especially big declines include four types of injection—SQL, hibernate, NoSQL, and
expression language (EL).

### TOP 5 RISKSCORES (ANNUAL AVERAGES)

*   BROKEN ACCESS CONTROL: 9.45
*   CROSS-SITE SCRIPTING: 8.13
*   INSECURE CONFIGURATION: 7.36
*   SQL INJECTION: 7.07
*   SENSITIVE DATA EXPOSURE: 6.80

## TAKEAWAYS

Findings in this report show that it is increasingly important for organizations to
address software vulnerabilities in a timely manner, reduce their security debt, and
prioritize their application security efforts according to actual risk. This is impossible
to achieve without detailed observability on vulnerabilities, attacks, and open-source
usage and security. Without it, organizations will not only waste scarce staff time on
vulnerabilities that pose no risk but they may also defer action on truly dangerous
issues in their software.

Instrumentation enables effective prioritization with continuous scanning, immediate
feedback, and full observability. Contrast customers have a fuller understanding of
which code is used by the software, which routes are exercised within the application,
and what vulnerabilities need prioritized attention. The result is faster vulnerability
remediation, reduced security debt, and fewer new vulnerabilities in applications.

13

contrastsecurity.com

---

# 03 | Introduction

Contrast Labs’ second annual Application Security Observability Report seeks to
provide comprehensive analysis of application security trends during the time frame of
June 2020 to May 2021. The research uses a broad dataset, including vulnerabilities
identified by Contrast Assess, attacks detected by Contrast Protect, and open-source
library data gathered by Contrast OSS.

Contrast Security is the only organization that provides data and insights across these
three areas of telemetry in a single report, covering the entire software development
life cycle (SDLC) and every component of an application or application programming
interface (API). The data is also broken down by programming language, application
age, routes exercised, and more, providing the most granular view of the state of
application security available in the marketplace.

The goal of this report is to help security, development, and operations teams refine
and prioritize their application security efforts. Contrast Labs supplements this
comprehensive annual report with bimonthly Application Security Intelligence Reports,
industry-specific³ and role-specific⁴ research, an annual report focusing on open-
source security,⁵ and regular updates on specific issues in Contrast Security’s AppSec
Observer blog.

The COVID-19 pandemic was still in its early stages when the 2020 Application
Security Observability Report was researched and published, and most would agree
that the 12 months since then have been a year like no other. One thing that did
not change was a significant emphasis on the application layer as an attack vector
by cyber criminals and nation-state actors.⁶ Massive application attacks like the
hack against SolarWinds Orion software⁷ highlighted the importance of application
security—so much so that a recent White House executive order on cybersecurity
placed significant emphasis on delivering secure software.⁸

16

contrastsecurity.com

---

# 04 | Application Makeup: More Custom Code Than Assumed

It is widely reported that a vast and growing majority of the lines of code in the typical
application comes from third-party libraries and frameworks. A 2020 study found that
70% of all code in applications is from third-party sources.⁹ Our data shows an even
higher percentage of third-party code, with only 20% of code coming from custom
sources and 80% from libraries (Figure 1).

However, this figure is completely useless in calculating the amount of risk posed by
third-party code. This is because nearly three-quarters (74%) of code is inactive—that
is, not invoked by the application at all. Nearly half of code is from inactive libraries—
full libraries that are never used by the software but are included because they are
attached to other libraries that are in use.

Even within active libraries, most of the code is never invoked: 25% of code in the
typical application belongs to an inactive class within an active library. Active library
classes, on the other hand, comprise just 6% of code. With custom code making up
20% of an application, narrowing the focus to active code changes the typical view of
application security risk dramatically. Overall, third-party libraries make up just 22% of
active code in the typical application, while custom code comprises 78%.

## BY LANGUAGE

While our overall dataset shows just 6% of code consists of active library classes, the
number is a bit higher for the two most common programming languages—Java and
.NET. Active library code makes up 9% and 13% of those applications, respectively
(Figure 2). This is because applications written in the Node language have especially
low percentages of active third-party code. And a total of one-third of code (both
custom and third party) is invoked in both Java and .NET. Of course, this means that
two-thirds of code in these languages is still inactive.

Understanding which parts of an application are active is critical to properly prioritizing
vulnerability remediation, as vulnerabilities in inactive code generally pose no risk to
an organization. Yet, organizations spend multiple staff hours updating libraries that
are never used by an application to remediate Common Vulnerabilities and Exposures
(CVEs) that have been published. While keeping libraries up to date is a matter of
good hygiene, it can actually increase risk if remediations that do not reduce risk are
prioritized ahead of those that do.

18

contrastsecurity.com

### FIGURE 1

#### % OF APPLICATIONS

*   **CUSTOM CODE**: 20%
*   **INACTIVE LIBRARIES**: 49%
*   **ACTIVE LIBRARIES, INACTIVE CLASSES**: 25%
*   **ACTIVE LIBRARY CLASSES**: 6%

### % OF ACTIVE CODE

*   **CUSTOM CODE**: 78%
*   **ACTIVE LIBRARY CLASSES**: 22%

### FIGURE 2

#### % of Applications Made Up of Active Library Code

*   **ALL APPLICATIONS**: 6%
*   **JAVA APPLICATIONS**: 9%
*   **.NET APPLICATIONS**: 13%

#### % of Applications Invoked

*   **ALL APPLICATIONS**: 26%
*   **JAVA APPLICATIONS**: 33%
*   **.NET APPLICATIONS**: 33%

19

contrastsecurity.com

---

# 05 | Routes: Vulnerabilities Decline Later in the SDLC

The Route Intelligence functionality in Contrast Assess analyzes the different routes
users can take when interacting with a piece of software. The functionality has been
live for over a year, and it is interesting to observe the trends around which possible
routes in an application are exercised. Across the entire dataset, the percentage of
potential routes exercised by an application increases as its age increases (Figure 3).
Only after the ninth month do more than half of applications have more than 80%
route coverage (Figure 4). This makes sense for software under development, as
some functionalities may not yet be in place in the earlier stages of the SDLC.
By the time the typical application is 12 months old, more than 84% of potential
routes are exercised.

*   **84%** (12+ months)
*   **80%** (9-11 months)
*   **71%** (6-8 months)
*   **59%** (3-5 months)
*   **41%** (0-2 months)

### FIGURE 3

#### AVERAGE % OF ROUTES EXERCISED BY APPLICATION AGE (MONTHS)

*   **0 Months**: 37%
*   **1 Month**: 37%
*   **2 Months**: 41%
*   **3 Months**: 49%
*   **4 Months**: 52%
*   **5 Months**: 57%
*   **6 Months**: 58%
*   **7 Months**: 59%
*   **8 Months**: 63%
*   **9 Months**: 71%
*   **10 Months**: 80%
*   **11 Months**: 84%
*   **12 Months**: 84%

### ROUTE INTELLIGENCE

An application route represents how a user interacts with an application. It consists of three distinct data points: the
URL of the route, the HTTP verb associated with the request (e.g., GET or POST), and a unique signature based on that
route’s controller action. Contrast Security’s Route Intelligence capability observes an application at runtime, rather
than testing and retesting lines of code. Such monitoring reveals the different points of entry into the application, and
detects vulnerabilities that become apparent as the code runs—whether it comes from custom or third-party sources.

Beyond its ability to detect vulnerabilities that only manifest themselves in the running application, Route Intelligence
also helps organizations with prioritization of application security efforts. Because it provides observability into which
routes are invoked by the application, organizations can understand which vulnerabilities present risk, and which are
on a route that a user would never reach.

21

contrastsecurity.com

### FIGURE 4

#### % OF APPLICATIONS WITH OVER 80% ROUTE COVERAGE

*   **0 TO 2 MONTHS**: 32%
*   **3 TO 5 MONTHS**: 38%
*   **6 TO 8 MONTHS**: 42%
*   **9 TO 11 MONTHS**: 57%
*   **12+ MONTHS**: 68%

Regardless of the percentage of routes exercised by the software, data shows that a
similar percentage of routes contains at least one vulnerability. When the percentage
of routes exercised is divided into 10-percentage-point groups, between 78% and
86% of routes are vulnerable (Figure 5). Major variances based on the percentage of
routes exercised occur.

### FIGURE 5

#### AVERAGE % OF VULNERABLE ROUTES BY AVERAGE % OF ROUTES EXERCISED

*   **<10%**: 78%
*   **10%-19%**: 80%
*   **20%-29%**: 81%
*   **30%-39%**: 82%
*   **40%-49%**: 83%
*   **50%-59%**: 84%
*   **60%-69%**: 85%
*   **70%-79%**: 86%
*   **80%-89%**: 86%
*   **90%+**: 86%

22

contrastsecurity.com

---

# 06 | Custom Code Vulnerabilities: More Likely To Be Serious

Overall, more applications had vulnerabilities and serious vulnerabilities in their
custom code in the past 12 months than in the prior year (Figure 6). The percentage of
applications with at least one vulnerability increased from 96% to 98% and the share
with at least one serious vulnerability increased from 26% to 34%—a 30.7% increase.
Among all vulnerabilities, nearly 4 in 10 (39%) are classified as serious—High or Critical
(Figure 7). This is a 39% increase over the 28% that was observed last year.

### FIGURE 6

#### % OF APPS WITH 1+ VULNERABILITIES AND % OF APPS WITH 1+ SERIOUS VULNERABILITIES BY MONTH

*   **Jun**: 98% (1+ Vuln), 32% (1+ Serious Vuln)
*   **Jul**: 98% (1+ Vuln), 27% (1+ Serious Vuln)
*   **Aug**: 97% (1+ Vuln), 28% (1+ Serious Vuln)
*   **Sep**: 97% (1+ Vuln), 30% (1+ Serious Vuln)
*   **Oct**: 99% (1+ Vuln), 31% (1+ Serious Vuln)
*   **Nov**: 99% (1+ Vuln), 32% (1+ Serious Vuln)
*   **Dec**: 98% (1+ Vuln), 32% (1+ Serious Vuln)
*   **Jan**: 97% (1+ Vuln), 36% (1+ Serious Vuln)
*   **Feb**: 98% (1+ Vuln), 35% (1+ Serious Vuln)
*   **Mar**: 97% (1+ Vuln), 33% (1+ Serious Vuln)
*   **Apr**: 98% (1+ Vuln), 32% (1+ Serious Vuln)
*   **May**: 98% (1+ Vuln), 33% (1+ Serious Vuln)

### FIGURE 7

#### % OF VULNERABILITIES BY SEVERITY

*   **CRITICAL**: 5%
*   **HIGH**: 34%
*   **MEDIUM**: 34%
*   **LOW**: 26%

24

contrastsecurity.com

Looking at vulnerabilities by type, broken access control and XSS impact by far more
applications than any other types (Figure 8). This in itself is not surprising, but the
large increase in both is concerning. The percentage of applications with a broken
access control vulnerability type increased from 13.3% to 18%—a 35.3% increase.
XSS vulnerabilities were in 18% of applications, compared with 15% from the prior 12
months (June 2019–May 2020)—a 20% increase. A vulnerability type worth watching
is insecure configuration, which increased by a delta of four percentage points,
quintupling from impacting 1% of applications in the prior year to 5% this year.

### FIGURE 8

#### % OF APPLICATIONS WITH 1+ SERIOUS VULNERABILITIES BY TYPE

*   **BROKEN ACCESS CONTROL**: 18%
*   **CROSS-SITE SCRIPTING**: 18%
*   **SQL INJECTION**: 7%
*   **XML EXTERNAL ENTITIES**: 6%
*   **INSECURE CONFIGURATION**: 5%
*   **INSECURE DESERIALIZATION**: 2%
*   **LDAP INJECTION**: 2%
*   **HIBERNATE INJECTION**: 1%
*   **XPATH INJECTION**: 1%
*   **EXPRESSION LANGUAGE INJECTION**: 0%
*   **COMMAND INJECTION**: 0%
*   **NOSQL INJECTION**: 0%
*   **UNSAFE CODE EXECUTION**: 0%

#### CHANGE IN % OF APPLICATIONS WITH 1+ SERIOUS VULNERABILITIES

*   **BROKEN ACCESS CONTROL**: 4.7%
*   **CROSS-SITE SCRIPTING**: 3.0%
*   **SQL INJECTION**: 4.1%
*   **XML EXTERNAL ENTITIES**: 1.1%
*   **INSECURE CONFIGURATION**: 0.8%
*   **INSECURE DESERIALIZATION**: 0.1%
*   **LDAP INJECTION**: 0.3%
*   **HIBERNATE INJECTION**: 0.1%
*   **XPATH INJECTION**: 0.0%
*   **EXPRESSION LANGUAGE INJECTION**: -0.3%
*   **COMMAND INJECTION**: -0.5%
*   **NOSQL INJECTION**: -0.5%
*   **UNSAFE CODE EXECUTION**: -1.0%

25

contrastsecurity.com

## VULNERABILITIES PER APPLICATION

A subset of applications in the dataset has a large number of vulnerabilities—including
1% of applications that have more than 300 (Figure 9). This skews the averages
upward. One in 10 applications has more than 10 vulnerabilities, and only 13% have as
few as one or two.

### FIGURE 9

#### % OF APPLICATIONS BY NUMBER OF SERIOUS VULNERABILITIES

*   **1 TO 2**: 13%
*   **3 TO 5**: 6%
*   **6 TO 10**: 4%
*   **11 TO 20**: 3%
*   **21 TO 50**: 3%
*   **51 TO 100**: 1%
*   **101 TO 300**: 2%
*   **301+**: 1%

26

contrastsecurity.com

## BY LIKELIHOOD AND IMPACT

It is instructive to look at vulnerabilities by both how likely they are to occur and
the impact when they do occur. Contrast Labs rates each vulnerability type for the
perceived technical and business impact of a successful exploit. SQL injection, for
example, is rated as a high-impact vulnerability type because it leads to a complete
takeover of a database, complete data exfiltration, and a complete degradation of
confidentiality, integrity, and availability of the database.

In the most recent 12-month period, 5% of vulnerabilities are both high likelihood and
high impact—and any number above zero is too high for this scenario (Figure 10). But
another 20% of vulnerabilities are high impact with medium likelihood, while another
15% are medium likelihood and high impact. These three figures add up to 40% this
year, compared with 28% in the prior 12-month period. Organizations, as a result,
need to prioritize remediation on these vulnerabilities over those with lower
likelihood and impact.

### FIGURE 10

#### % OF VULNERABILITIES BY LIKELIHOOD AND IMPACT

**This Year**
*   **HIGH Likelihood, HIGH Impact**: 5%
*   **MEDIUM Likelihood, HIGH Impact**: 20%
*   **HIGH Likelihood, MEDIUM Impact**: 15%
*   **MEDIUM Likelihood, MEDIUM Impact**: 26%
*   **HIGH Likelihood, LOW Impact**: 4%
*   **MEDIUM Likelihood, LOW Impact**: 1%
*   **LOW Likelihood, LOW Impact**: 0.50%

**Last Year**
*   **HIGH Likelihood, HIGH Impact**: 5%
*   **MEDIUM Likelihood, HIGH Impact**: 16%
*   **HIGH Likelihood, MEDIUM Impact**: 7%
*   **MEDIUM Likelihood, MEDIUM Impact**: 42%
*   **HIGH Likelihood, LOW Impact**: 4%
*   **MEDIUM Likelihood, LOW Impact**: 1%
*   **LOW Likelihood, LOW Impact**: 0.10%

27

contrastsecurity.com

## BY LANGUAGE

The overall increase in serious vulnerabilities is driven by an increase in .NET serious
vulnerabilities. While the percentage of Java applications with at least one serious
vulnerability increased from 42% to 44%, .NET applications saw an increase in this
figure from 16% to 23%—a 44% increase (Figure 11).

### FIGURE 11

#### JAVA

| Metric                                     | Last Year | This Year | Delta |
| :----------------------------------------- | :-------- | :-------- | :---- |
| % of Applications with at least 1 Vulnerability | 97%       | 98%       | 1%    |
| % of Applications with at least 1 Serious Vulnerability | 42%       | 44%       | 2%    |

#### .NET

| Metric                                     | Last Year | This Year | Delta |
| :----------------------------------------- | :-------- | :-------- | :---- |
| % of Applications with at least 1 Vulnerability | 97%       | 99%       | 2%    |
| % of Applications with at least 1 Serious Vulnerability | 16%       | 23%       | 7%    |

28

contrastsecurity.com

Despite Java remaining relatively the same, one area was particularly troubling: The
percentage of Java applications with insecure configuration vulnerabilities tripled
(Figure 12). In .NET applications, XPath injection vulnerabilities impacted 3% of
applications this year, compared with just 1% last year (Figure 13)—a 300% increase.

### FIGURE 12

#### % OF JAVA APPLICATIONS WITH 1+ SERIOUS VULNERABILITIES

*