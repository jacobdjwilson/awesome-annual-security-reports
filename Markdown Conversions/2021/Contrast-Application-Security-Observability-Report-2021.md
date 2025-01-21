# 2021 Application Security Observability Report

contrastsecurity.com

Understanding Application and API Risk by Connecting Real-world Vulnerabilities With Actual Attack Data

## Table of Contents
- [Foreword](#foreword)
- [Executive Summary](#executive-summary)
- [Introduction](#introduction)
- [Application Makeup: More Custom Code Than Assumed](#application-makeup-more-custom-code-than-assumed)
    - [By Language](#by-language)
- [Routes: Vulnerabilities Decline Later in the SDLC](#routes-vulnerabilities-decline-later-in-the-sdlc)
    - [Sidebar: Route Intelligence](#sidebar-route-intelligence)
- [Custom Code Vulnerabilities: More Likely To Be Serious](#custom-code-vulnerabilities-more-likely-to-be-serious)
    - [Vulnerabilities Per Application](#vulnerabilities-per-application)
    - [By Likelihood And Impact](#by-likelihood-and-impact)
    - [By Language](#by-language-1)
    - [By Application Age](#by-application-age)
    - [For Applications With 80%+ Route Coverage](#for-applications-with-80-route-coverage)
    - [Vulnerability Escape Rate (Ver)](#vulnerability-escape-rate-ver)
- [Vulnerability Remediation: Slower But Much Better Than Traditional Approaches](#vulnerability-remediation-slower-but-much-better-than-traditional-approaches)
    - [Compared With Last Year](#compared-with-last-year)
    - [Compared With Traditional Practices](#compared-with-traditional-practices)
    - [By Level Of Security Debt](#by-level-of-security-debt)
- [Security Debt: Organizations Are Making Progress](#security-debt-organizations-are-making-progress)
- [Open-Source Libraries And Frameworks: Organizations Struggle To Keep Up](#open-source-libraries-and-frameworks-organizations-struggle-to-keep-up)
    - [Active Libraries And Classes](#active-libraries-and-classes)
    - [Open-Source Vulnerabilities](#open-source-vulnerabilities)
    - [Most Cves Are False Positives](#most-cves-are-false-positives)
    - [Sidebar: Library Age: Older Libraries Can Compound Risk](#sidebar-library-age-older-libraries-can-compound-risk)
- [Attacks: Increased Prevalence, Decreased Viability](#attacks-increased-prevalence-decreased-viability)
    - [By Language](#by-language-2)
- [Contrast Riskscore™ Index: Overall, A Downward Trend](#contrast-riskscore-index-overall-a-downward-trend)
    - [Sidebar: Contrast Riskscore Index](#sidebar-contrast-riskscore-index)
- [Conclusion](#conclusion)
- [Report Contributors](#report-contributors)

---
# Foreword
01

Disruptive change in the marketplace has been the name of the game for some time, and this trend promises to continue in the months and years to come. Businesses were already embracing digital transformation before the COVID-19 pandemic, which rapidly accelerated digital adoption—with McKinsey indicating late last year that the share of digital and digitally enabled products leapfrogged an astounding seven years in the past year.[^1]

Companies with the agility to evolve with current trends and quickly tap new revenue opportunities are best positioned to survive and thrive in the new economy. And more than ever before, software applications are a critical part of that agility. Yet, the application layer is an increasingly attractive target for cyber criminals, with high-profile software supply chain attacks on SolarWinds, Microsoft Exchange, and Kaseya making headlines in the past six months. Overall, 39% of data breaches in the past year have been the result of an application vulnerability.[^2]

In this context, we are pleased to present Contrast Labs’ second annual Application Security Observability Report. Our flagship research report covers the past 12 months of telemetry data from our different product offerings—Contrast Assess, Contrast Protect, and Contrast OSS. Contrast is the only player in the marketplace to present findings from vulnerability, attack, and open-source library data in a single report. This year, we added data on application makeup and the vulnerability escape rate (VER), both of which bring fascinating insights. In addition, we also added data on which potential routes are exercised within applications using data from our Route Intelligence functionality, released in March 2020.

Our goal with this report is to guide organizations as they strive to grow digital innovation while maintaining application security. Accordingly, we focus first on the nuts and bolts of how software is structured—the active and inactive code that makes up the software and how many routes are exercised. We then focus on custom code vulnerabilities and open-source libraries and frameworks. We then move to data about vulnerability remediation and security debt and to telemetry about application attacks.Finally, we update the Contrast RiskScore Index, which provides an easy-to-understand score that helps organizations better understand the risk of various vulnerability types.

Throughout these analyses, a few themes pop up repeatedly. First and foremost, effective application security is a matter of good prioritization of prevention and response efforts. This year, we find that only 6% of the code in a typical application is from active third-party library classes, while 20% is custom code. This means that 74% of the code in applications is third-party content that is never invoked by the application, and vulnerabilities in this code pose no risk to an organization and should be deprioritized.

A second recurring theme is the need for comprehensive observability into all aspects of application security throughout the software development life cycle (SDLC). This includes immediate feedback when a vulnerability is created, visibility into which open-source content is active, and which attacks are probes versus those that target existing vulnerabilities and hence could cause damage. Such observability enables organizations to deal with new vulnerabilities as they occur and to reduce their security debt over time.

This brings us to a third theme in the research: the need to resolve vulnerabilities quickly to ensure the timely delivery of secure software into production. Our research finds that Contrast customers deliver on this priority almost 29 times more quickly than customers of a well-known vendor of traditional application security tools, according to their research. And the Contrast platform has the added benefit of helping developers learn to introduce fewer vulnerabilities into their code, reducing their vulnerability escape rate (VER) from initial deployment to one year by 92%.

Our 2021 report provides a snapshot in time of where things stand with the applications developed by the Contrast customer community. The security observability provided by the Contrast Application Security Platform enables their development, security, and operations teams to work together to secure their software—and deliver to increasingly aggressive deadlines in a fast-changing marketplace.

Sincerely,

Jeff Williams
Cto and Co-Founder

David Lindner
Chief Information Security Officer

[^1]: “How COVID-19 has pushed companies over the technology tipping point—and transformed business forever,” McKinsey, October 5, 2020.
[^2]: “2021 Data Breach Investigations Report,” Verizon, May 2021.

---
# Executive Summary
02

Contrast Labs’ second annual Application Security Observability Report takes a broad look at the state of application security at a critical moment in the economy—while digital transformation continues at an accelerated pace, businesses reopen their office locations, and corporate leaders discern the next phase of how work is structured. The data comes from aggregate telemetry from applications and application programming interfaces (APIs) protected by the Contrast Application Security Platform. It includes data on vulnerabilities, attacks, and open-source libraries between June 2020 and May 2021. Such comprehensive reporting from across the software development life cycle (SDLC) is only available from Contrast.

### 78% OF ACTIVE CODE IS CUSTOM
The fact that 70% or more of the code in the typical application comes from open-source libraries and frameworks has been widely noted in recent years. What is not usually revealed in these reports is that the vast majority of this code is not used by the application. Our data shows that 80% of code is open source, but only 6% of code belongs to an active library or class. The other 74% is from inactive libraries or inactive classes within active libraries. When this is taken into account, 78% of active code in the typical application is custom code and only 22% comes from open sources.

### APPLICATION MAKEUP
![Application Makeup]

### FALSE-POSITIVE RATE
9
BIMONTHLY REPORT
contrastsecurity.com
9

20% Custom Code
54% for Critical CVEs
6% Active Library Classes
49% for Major CVEs
74% Inactive Libraries and Inactive Classes Within Active Libraries

### 39% OF CUSTOM CODE VULNERABILITIES ARE SERIOUS
Overall, a greater share of applications had custom code vulnerabilities than in the prior 12-month period. Most concerning is the 21% increase in the percentage of applications with at least one serious vulnerability—34% this year compared with 26% last year. Overall, 13% of applications have one or two serious vulnerabilities, while 3% have more than 100. And 39% of all vulnerabilities identified are serious, defined as High or Critical—a 39% increase over last year’s 28% figure.

The top two vulnerability types in terms of percentage of applications affected are broken access control and cross-site scripting (XSS). Unfortunately, both of these vulnerability types were found in a larger share of applications this year than last year. As in the past, more Java applications have serious vulnerabilities than .NET ones—44% versus 23%.

10
BIMONTHLY REPORT
contrastsecurity.com
10

34% of Applications Have a Serious Vulnerability (21% increase over last year)
18% of Applications Impacted by Broken Access Control and Cross-site Scripting Vulnerabilities
39% of Vulnerabilities Are High or Critical
13% of Applications Have 1 to 2 Serious Vulnerabilities; 3% Have 100+

### VULNERABILITY ESCAPE RATE (VER) FALLS FROM 18 TO 1 IN 12 MONTHS
The good news is that Contrast enables developers to improve the security of their coding over time. With its immediate feedback when a vulnerability is created, the platform provides actionable instructions on how to fix the problem—and avoid making the same mistake again in the future. The result is akin to “just-in-time” security training—something that learning managers have struggled to provide for developers for years.

This phenomenon shows up in our data in what we are calling the vulnerability escape rate (VER). In the first two months of an application’s tenure on the Contrast Application Security Platform, an average 12 vulnerabilities—six of them serious—occur in the software. But these numbers shrink steadily, reaching 6 total vulnerabilities and 3 serious in the ninth month. By the end of the first year, the average application sees no new serious vulnerabilities and just one non-serious one each month—a 92% decline.As in the past, more Java applications have serious vulnerabilities than .NET ones—44% versus 23%.

### 54% OF CRITICAL CVES ARE FALSE POSITIVES
Our data on application makeup, discussed above, upends a commonly held view of application security risk, as vulnerabilities that exist within the 74% of code that is inactive pose no risk to an organization. Traditional software composition analysis (SCA) tools do not differentiate between active and inactive code. As a result, every Common Vulnerability and Exposure (CVE) they identify that occurs in inactive code is actually a false positive. In our dataset, a majority of vulnerabilities—including 54% of CVEs rated as Critical and 49% rated as Major—would be false positives with traditional tools.

Nevertheless, good library hygiene such as keeping versions relatively up to date is important for reducing application security risk. Unfortunately, 45% of libraries found in applications are more than two years old.

11
BIMONTHLY REPORT
contrastsecurity.com
11

12 TO 1 The average vulnerability escape rate fell from 12 per month to 1 per month in 12 months—92% reduction

### MEDIAN TIME TO REMEDIATION NEARLY 29X BETTER THAN TRADITIONAL APPSEC SOLUTIONS
The Contrast customers in the dataset saw much better remediation timelines than organizations using legacy application security tools. The median time to remediation—the time it takes to resolve half of all closed vulnerabilities—was just 3 days in our dataset. This was 29 times faster than the 86 days reported by a traditional static application security testing (SAST) vendor. Nearly three-quarters (74%) of serious vulnerabilities were remediated within 90 days, and 90% of them within a year.

### SECURITY DEBT PER APPLICATION 19% LOWER
The result of this astounding remediation timeline is that organizations are reducing their per-application vulnerability backlog to 21 vulnerabilities, down from 26 in the previous 12 months. This 19% decline translates into lower application risk.

### FALSE-POSITIVE RATE
50% OF FIXED VULNERABILITIES CLOSED
12
BIMONTHLY REPORT
contrastsecurity.com
12

54% for Critical CVEs
3 DAYS Contrast Customers
49% for Major CVEs
86 DAYS Traditional SAST

### 99% OF ATTACKS WERE PROBES
The typical organization was pummeled with 25,343 application attacks every month over the past year. But one of the biggest trends in the attack data for the past 12 months is that the percentage of attacks that were viable was cut in half—from 2% last year to 1% this year. A viable attack is one that hits an existing vulnerability in an application, and therefore has a chance of being successful. Eleven of the top 12 attack types impacted a larger share of applications this year than last year, with big increases in broken access control, SQL injection, XSS, command injection, and expression language (EL) injection.

### RISKSCORE INDEX DOWN BY 1.25 POINTS ON AVERAGE
The report also updated the Contrast RiskScore Index, a numerical score that helps organizations rank and visualize the risk posed by different vulnerability types over time. The five highest RiskScores were quite consistent over the entire 12 months, but the average RiskScore declined by more than 1.25 points over the course of a year. This is because our data comes from Contrast Security customers, whose risk level declines as they build tenure with the solution (viz., the number of vulnerabilities being introduced declines and overall security increases). Vulnerability types that saw especially big declines include four types of injection—SQL, hibernate, NoSQL, and expression language (EL).

Vulnerability types with attacks that rose by 9+ percentage points:

BROKEN ACCESS CONTROL, SQL INJECTION, XSS, COMMAND INJECTION, EL INJECTION

### SECURITY DEBT
13
BIMONTHLY REPORT
contrastsecurity.com
13

21 Per Application: 21 Vulnerabilities, Down From 26
1% of Attacks Were Viable, Down From 2%

### TOP 5 RISKSCORES (ANNUAL AVERAGES)
BROKEN ACCESS CONTROL, 9.45
CROSS-SITE SCRIPTING, 8.13
INSECURE CONFIGURATION, 7.36
SQL INJECTION, 7.07
SENSITIVE DATA EXPOSURE, 6.80

### TAKEAWAYS
Findings in this report show that it is increasingly important for organizations to address software vulnerabilities in a timely manner, reduce their security debt, and prioritize their application security efforts according to actual risk. This is impossible to achieve without detailed observability on vulnerabilities, attacks, and open-source usage and security. Without it, organizations will not only waste scarce staff time on vulnerabilities that pose no risk but they may also defer action on truly dangerous issues in their software.

Instrumentation enables effective prioritization with continuous scanning, immediate feedback, and full observability. Contrast customers have a fuller understanding of which code is used by the software, which routes are exercised within the application, and what vulnerabilities need prioritized attention. The result is faster vulnerability remediation, reduced security debt, and fewer new vulnerabilities in applications.

---
# Introduction
03

Contrast Labs’ second annual Application Security Observability Report seeks to provide comprehensive analysis of application security trends during the time frame of June 2020 to May 2021. The research uses a broad dataset, including vulnerabilities identified by Contrast Assess, attacks detected by Contrast Protect, and open-source library data gathered by Contrast OSS.

Contrast Security is the only organization that provides data and insights across these three areas of telemetry in a single report, covering the entire software development life cycle (SDLC) and every component of an application or application programming interface (API). The data is also broken down by programming language, application age, routes exercised, and more, providing the most granular view of the state of application security available in the marketplace.

The goal of this report is to help security, development, and operations teams refine and prioritize their application security efforts. Contrast Labs supplements this comprehensive annual report with bimonthly Application Security Intelligence Reports, industry-specific[^3] and role-specific[^4] research, an annual report focusing on open-source security,[^5] and regular updates on specific issues in Contrast Security’s AppSec Observer blog.

The COVID-19 pandemic was still in its early stages when the 2020 Application Security Observability Report was researched and published, and most would agree that the 12 months since then have been a year like no other. One thing that did not change was a significant emphasis on the application layer as an attack vector by cyber criminals and nation-state actors.[^6] Massive application attacks like the hack against SolarWinds Orion software[^7] highlighted the importance of application security—so much so that a recent White House executive order on cybersecurity placed significant emphasis on delivering secure software.[^8]

[^3]: “2021 State of Application Security in Financial Services Report,” Contrast Security, May 2021.
[^4]: “Priorities and Challenges for Modern Software Developers,” Contrast Security, March 2021.
[^5]: “2021 State of Open-source Security Report,” Contrast Security, April 2021.
[^6]: “2021 Data Breach Investigations Report,” Verizon, May 2021, found that 39% of data breaches were the result of application vulnerabilities.
[^7]: Michael Riley, et. al, “Russia-Linked SolarWinds Hack Snags Widening List of Victims,” Bloomberg, December 17, 2020.
[^8]: “Executive Order on Improving the Nation’s Cybersecurity,” The White House, May 12, 2021.

---
# Application Makeup: More Custom Code Than Assumed
04

It is widely reported that a vast and growing majority of the lines of code in the typical application comes from third-party libraries and frameworks. A 2020 study found that 70% of all code in applications is from third-party sources.[^9] Our data shows an even higher percentage of third-party code, with only 20% of code coming from custom sources and 80% from libraries (Figure 1).

However, this figure is completely useless in calculating the amount of risk posed by third-party code. This is because nearly three-quarters (74%) of code is inactive—that is, not invoked by the application at all. Nearly half of code is from inactive libraries—full libraries that are never used by the software but are included because they are attached to other libraries that are in use.

Even within active libraries, most of the code is never invoked: 25% of code in the typical application belongs to an inactive class within an active library. Active library classes, on the other hand, comprise just 6% of code. With custom code making up 20% of an application, narrowing the focus to active code changes the typical view of application security risk dramatically. Overall, third-party libraries make up just 22% of active code in the typical application, while custom code comprises 78%.

### BY LANGUAGE
While our overall dataset shows just 6% of code consists of active library classes, the number is a bit higher for the two most common programming languages—Java and .NET. Active library code makes up 9% and 13% of those applications, respectively (Figure 2). This is because applications written in the Node language have especially low percentages of active third-party code. And a total of one-third of code (both custom and third party) is invoked in both Java and .NET. Of course, this means that two-thirds of code in these languages is still inactive.

Understanding which parts of an application are active is critical to properly prioritizing vulnerability remediation, as vulnerabilities in inactive code generally pose no risk to an organization. Yet, organizations spend multiple staff hours updating libraries that are never used by an application to remediate Common Vulnerabilities and Exposures (CVEs) that have been published. While keeping libraries up to date is a matter of good hygiene, it can actually increase risk if remediations that do not reduce risk are prioritized ahead of those that do.

[^9]: “2020 Open Source Security and Risk Analysis Report,” Synopsys, May 2020.

18
BIMONTHLY REPORT
contrastsecurity.com
18

![Figure 1: Custom Code, Inactive Libraries, Active Libraries, Inactive Classes, Active Library Classes]
04 | Application Makeup: More Custom Code Than Assumed
19
BIMONTHLY REPORT
contrastsecurity.com
19

**FIGURE 1**
CUSTOM CODE 20%
INACTIVE LIBRARIES 49%
ACTIVE LIBRARIES, INACTIVE CLASSES 25%
ACTIVE LIBRARY CLASSES 6%

CUSTOM CODE 78%
ACTIVE LIBRARY CLASSES 22%

**FIGURE 2**
ALL APPLICATIONS 6%
JAVA APPLICATIONS 9%
.NET APPLICATIONS 13%
% of Applications Made Up of Active Library Code

ALL APPLICATIONS 26%
JAVA APPLICATIONS 33%
.NET APPLICATIONS 33%
% of Applications Invoked

---
# Routes: Vulnerabilities Decline Later in the SDLC
05

The Route Intelligence functionality in Contrast Assess analyzes the different routes users can take when interacting with a piece of software. The functionality has been live for over a year, and it is interesting to observe the trends around which possible routes in an application are exercised. Across the entire dataset, the percentage of potential routes exercised by an application increases as its age increases (Figure 3). Only after the ninth month do more than half of applications have more than 80% route coverage (Figure 4). This makes sense for software under development, as some functionalities may not yet be in place in the earlier stages of the SDLC. By the time the typical application is 12 months old, more than 84% of potential routes are exercised.

21
BIMONTHLY REPORT
contrastsecurity.com
21
05 | Routes: Vulnerabilities Decline Later in the SDLC

**FIGURE 3**
AVERAGE % OF ROUTES EXERCISED
APPLICATION AGE (MONTHS)
0 37%
1 37%
2 41%
3 49%
4 52%
5 57%
6 58%
7 59%
8 63%
9 70%
10 71%
11 80%
12 84%

### SIDEBAR: ROUTE INTELLIGENCE
An application route represents how a user interacts with an application. It consists of three distinct data points: the URL of the route, the HTTP verb associated with the request (e.g., GET or POST), and a unique signature based on that route’s controller action. Contrast Security’s Route Intelligence capability observes an application at runtime, rather than testing and retesting lines of code. Such monitoring reveals the different points of entry into the application, and detects vulnerabilities that become apparent as the code runs—whether it comes from custom or third-party sources.

Beyond its ability to detect vulnerabilities that only manifest themselves in the running application, Route Intelligence also helps organizations with prioritization of application security efforts. Because it provides observability into which routes are invoked by the application, organizations can understand which vulnerabilities present risk, and which are on a route that a user would never reach.

Regardless of the percentage of routes exercised by the software, data shows that a similar percentage of routes contains at least one vulnerability. When the percentage of routes exercised is divided into 10-percentage-point groups, between 78% and 86% of routes are vulnerable (Figure 5). Major variances based on the percentage of routes exercised occur.

22
BIMONTHLY REPORT
contrastsecurity.com
22

**FIGURE 4**
APPLICATION AGE (MONTHS)
% OF APPLICATIONS WITH OVER 80% ROUTE COVERAGE
0 TO 2 MONTHS 32%
3 TO 5 MONTHS 68%
6 TO 8 MONTHS 57%
9 TO 11 MONTHS 42%
12+ MONTHS 38%

**FIGURE 5**
LIKELIHOOD OF VULNERABLE ROUTES
AVERAGE % OF ROUTES EXERCISED
<10%
10%-19%
20%-29%
30%-139%
40%-49%
50%-59%
60%-69%
70%-79%
80%-89%
90%+

---
# Custom Code Vulnerabilities: More Likely to be Serious
06

Overall, more applications had vulnerabilities and serious vulnerabilities in their custom code in the past 12 months than in the prior year (Figure 6). The percentage of applications with at least one vulnerability increased from 96% to 98% and the share with at least one serious vulnerability increased from 26% to 34%—a 30.7% increase. Among all vulnerabilities, nearly 4 in 10 (39%) are classified as serious—High or Critical (Figure 7). This is a 39% increase over the 28% that was observed last year.

24
BIMONTHLY REPORT
contrastsecurity.com
24
06 | Custom Code Vulnerabilities: More Likely To Be Serious

**FIGURE 6**
% OF APPS WITH 1+ VULNERABILITIES
% OF APPS WITH 1+ SERIOUS VULNERABILITIES
JUN 98% 32%
JUL 98% 27%
AUG 98% 28%
SEP 98% 30%
OCT 97% 31%
NOV 97% 32%
DEC 97% 32%
JAN 99% 36%
FEB 99% 35%
MAR 98% 33%
APR 97% 32%
MAY 98% 33%

**FIGURE 7**
% OF VULNERABILITIES
CRITICAL 5%
HIGH 34%
MEDIUM 26%
LOW 1%
NOTE 34%

Looking at vulnerabilities by type, broken access control and XSS impact by far more applications than any other types (Figure 8). This in itself is not surprising, but the large increase in both is concerning. The percentage of applications with a broken access control vulnerability type increased from 13.3% to 18%—a 35.3% increase. XSS vulnerabilities were in 18% of applications, compared with 15% from the prior 12 months (June 2019–May 2020)—a 20% increase. A vulnerability type worth watching is insecure configuration, which increased by a delta of four percentage points, quintupling from impacting 1% of applications in the prior year to 5% this year.

25
BIMONTHLY REPORT
contrastsecurity.com
25

**FIGURE 8**
% OF APPLICATIONS WITH 1+ SERIOUS VULNERABILITIES
UNSAFE CODE EXECUTION 0%
NOSQL INJECTION 0%
COMMAND INJECTION 0%
EXPRESSION LANGUAGE INJECTION 0%
XPATH INJECTION 1%
HIBERNATE INJECTION 1%
LDAP INJECTION 2%
INSECURE DESERIALIZATION 2%
INSECURE CONFIGURATION 5%
XML EXTERNAL ENTITIES 6%
SQL INJECTION 7%
CROSS-SITE SCRIPTING 18%
BROKEN ACCESS CONTROL 18%

CHANGE IN % OF APPLICATIONS WITH 1+ SERIOUS VULNERABILITIES
UNSAFE CODE EXECUTION -1%
NOSQL INJECTION 0%
COMMAND INJECTION 1%
EXPRESSION LANGUAGE INJECTION 2%
XPATH INJECTION 3%
HIBERNATE INJECTION 4%
LDAP INJECTION 5%
INSECURE DESERIALIZATION 0.1%
INSECURE CONFIGURATION 1.3%
XML EXTERNAL ENTITIES 4.1%
SQL INJECTION 0.8%
CROSS-SITE SCRIPTING 1.1%
BROKEN ACCESS CONTROL 3.0%

### VULNERABILITIES PER APPLICATION
A subset of applications in the dataset has a large number of vulnerabilities—including 1% of applications that have more than 300 (Figure 9). This skews the averages upward. One in 10 applications has more than 10 vulnerabilities, and only 13% have as few as one or two.

26
BIMONTHLY REPORT
contrastsecurity.com
26

**FIGURE 9**
NUMBER OF SERIOUS VULNERABILITIES PER APPLICATION
% OF APPLICATIONS
1 TO 2 13%
3 TO 5 6%
6 TO 10 4%
11 TO 20 3%
21 TO 50 3%
51 TO 100 1%
101 TO 300 2%
301+ 1%

### BY LIKELIHOOD AND IMPACT
It is instructive to look at vulnerabilities by both how likely they are to occur and the impact when they do occur. Contrast Labs rates each vulnerability type for the perceived technical and business impact of a successful exploit. SQL injection, for example, is rated as a high-impact vulnerability type because it leads to a complete takeover of a database, complete data exfiltration, and a complete degradation of confidentiality, integrity, and availability of the database.

In the most recent 12-month period, 5% of vulnerabilities are both high likelihood and high impact—and any number above zero is too high for this scenario (Figure 10). But another 20% of vulnerabilities are high impact with medium likelihood, while another 15% are medium likelihood and high impact. These three figures add up to 40% this year, compared with 28% in the prior 12-month period. Organizations, as a result, need to prioritize remediation on these vulnerabilities over those with lower likelihood and impact.

27
BIMONTHLY REPORT
contrastsecurity.com
27

**FIGURE 10**
LIKELIHOOD IMPACT
HIGH HIGH 5%
MEDIUM HIGH 20%
LOW HIGH 4%
HIGH MEDIUM 15%
MEDIUM MEDIUM 26%
LOW MEDIUM 1%
HIGH LOW 4%
MEDIUM LOW 0%
LOW LOW 26%
This Year

LIKELIHOOD IMPACT
HIGH HIGH 5%
MEDIUM HIGH 16%
LOW HIGH 4%
HIGH MEDIUM 7%
MEDIUM MEDIUM 42%
LOW MEDIUM 0.50%
HIGH LOW 1%
MEDIUM LOW 0.10%
LOW LOW 24%
Last Year

### BY LANGUAGE
The overall increase in serious vulnerabilities is driven by an increase in .NET serious vulnerabilities. While the percentage of Java applications with at least one serious vulnerability increased from 42% to 44%, .NET applications saw an increase in this figure from 16% to 23%—a 44% increase (Figure 11).

28
BIMONTHLY REPORT
contrastsecurity.com
28

**FIGURE 11**
JAVA
LAST YEAR
% OF APPLICATIONS WITH AT LEAST 1 SERIOUS VULNERABILITY 42%
% OF APPLICATIONS WITH AT LEAST 1 VULNERABILITY 97%
THIS YEAR
% OF APPLICATIONS WITH AT LEAST 1 SERIOUS VULNERABILITY 44%
% OF APPLICATIONS WITH AT LEAST 1 VULNERABILITY 98%
DELTA
% OF APPLICATIONS WITH AT LEAST 1 SERIOUS VULNERABILITY 2%
% OF APPLICATIONS WITH AT LEAST 1 VULNERABILITY 1%

.NET
LAST YEAR
% OF APPLICATIONS WITH AT LEAST 1 SERIOUS VULNERABILITY 16%
% OF APPLICATIONS WITH AT LEAST 1 VULNERABILITY 97%
THIS YEAR
% OF APPLICATIONS WITH AT LEAST 1 SERIOUS VULNERABILITY 23%
% OF APPLICATIONS WITH AT LEAST 1 VULNERABILITY 99%
DELTA
% OF APPLICATIONS WITH AT LEAST 1 SERIOUS VULNERABILITY 7%
% OF APPLICATIONS WITH AT LEAST 1 VULNERABILITY 2%

29
BIMONTHLY REPORT
contrastsecurity.com
29

Despite Java remaining relatively the same, one area was particularly troubling: The percentage of Java applications with insecure configuration vulnerabilities tripled (Figure 12). In .NET applications, XPath injection vulnerabilities impacted 3% of applications this year, compared with just 1% last year (Figure 13)—a 300% increase.

**FIGURE 12**
% OF JAVA APPLICATIONS WITH 1+ SERIOUS VULNERABILITIES
INSECURE CONFIGURATION
LDAP INJECTION
INSECURE DESERIALIZATION
XML EXTERNAL ENTITIES
SQL INJECTION
BROKEN ACCESS CONTROL
CROSS-SITE SCRIPTING
HIBERNATE INJECTION
EXPRESSION LANGUAGE INJECTION
XPATH INJECTION
COMMAND INJECTION
LAST YEAR
THIS YEAR
0%
1%
1%
2%
2%
2%
9%
9%
9%
8%
27%
26%
23%
22%
3%
0%
0%
0%
0%
0%

30
BIMONTHLY REPORT
contrastsecurity.com
30

**FIGURE 13**
% OF .NET APPLICATIONS WITH 1+ SERIOUS VULNERABILITIES
INSECURE CONFIGURATION
LDAP INJECTION
INSECURE DESERIALIZATION
XML EXTERNAL ENTITIES
SQL INJECTION
BROKEN ACCESS CONTROL
CROSS-SITE SCRIPTING
HIBERNATE INJECTION
EXPRESSION LANGUAGE INJECTION
XPATH INJECTION
COMMAND INJECTION
LAST YEAR
THIS YEAR
0%
0%
0%
0%
1%
1%
1%
2%
5%
5%
3%
3%
6%
7%
8%
10%
10%
12%
13%
0%
0%
0%
0%

### BY APPLICATION AGE
Looking at vulnerabilities by application age, it becomes clear that the Contrast customers in our dataset are reducing the number of new vulnerabilities that occur as they work their way through the SDLC. While a new application (0–2 months) has a 39% chance of seeing a new serious vulnerability, an application that is more than a year old only has a serious vulnerability 3% of the time (Figure 14).

31
BIMONTHLY REPORT
contrastsecurity.com
31

### FOR APPLICATIONS WITH 80%+ ROUTE COVERAGE
It is interesting to compare these vulnerability figures with the route coverage data we discussed earlier in the report. As an application gets older, more potential routes are invoked by the software, potentially increasing the attack surface. But the likelihood of a new vulnerability declines (Figure 15).

**FIGURE 14**
APPLICATION AGE (MONTHS)
LIKELIHOOD A NEW VULNERABILITY REPORTED
0 TO 2 MONTHS ANY SERIOUS 39% ANY VULNERABILITY 89%
3 TO 5 MONTHS ANY SERIOUS 23% ANY VULNERABILITY 85%
6 TO 8 MONTHS ANY SERIOUS 19% ANY VULNERABILITY 79%
9 TO 11 MONTHS ANY SERIOUS 21% ANY VULNERABILITY 41%
12+ MONTHS ANY SERIOUS 3% ANY VULNERABILITY 5%

32
BIMONTHLY REPORT
contrastsecurity.com
32

### VULNERABILITY ESCAPE RATE (VER)
One interesting insight revealed by the vulnerability data is that the Contrast customers in our dataset see dramatic improvements in vulnerability prevalence quite quickly after onboarding an application into the Contrast Application Security Platform. In the first two months of an application’s tenure on the platform, an average of 12 vulnerabilities—six of