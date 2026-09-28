# VOLUME 12: State of Software Security - The Progress We’ve All Made

Organization: Veracode  
Report Title: State-of-Software-Security-V12  
Year: 2021  

## Table of Contents
- [Executive Summary](#executive-summary)
- [Introduction](#introduction)
- [How Software Development Has Changed](#how-software-development-has-changed)
  - [The Number of Applications Scanned Has Tripled](#the-number-of-applications-scanned-has-tripled)
  - [The Rise of Microservices](#the-rise-of-microservices)
  - [Increase in Median Scan Cadence](#increase-in-median-scan-cadence)
  - [Organizations Are Using Multiple Types of Scanning](#organizations-are-using-multiple-types-of-scanning)
- [Software Bill of Mistakes](#software-bill-of-mistakes)
  - [Organizations Heavily Leverage Open-Source Libraries](#organizations-heavily-leverage-open-source-libraries)
  - [Most Developers Stick With the Same Libraries Year Over Year](#most-developers-stick-with-the-same-libraries-year-over-year)
  - [Third-Party Libraries Have Fewer Flaws](#third-party-libraries-have-further-flaws)
- [The Flaws of Yesterday Are (Still) the Flaws of Today](#the-flaws-of-yesterday-are-still-the-flaws-of-today)
  - [The Lowdown on Static, Dynamic, and Software Composition Analysis](#the-lowdown-on-static-dynamic-and-software-composition-analysis)
  - [Fix Rate Comparisons by Scan Type](#fix-rate-comparisons-by-scan-type)
  - [Capacity for Flaw Remediation by Scan Type](#capacity-for-flaw-remediation-by-scan-type)
- [Where Do We Go From Here?](#where-do-we-go-from-here)
  - [Most Organizations Using Veracode Security Labs Are Fixing Flaws Faster](#most-organizations-using-veracode-security-labs-are-fixing-flaws-faster)
- [Conclusions](#conclusions)
- [Appendix: Methodology](#appendix-methodology)
- [A Note on Mass Closures](#a-note-on-mass-closures)

---

## Executive Support & Overview

The world is becoming more connected than ever before... Connectivity makes our lives easier, but it also increases risk. One security flaw can have a domino effect, leaving software vulnerable all across the globe.

But it’s not just increased connectivity that’s shaping the security landscape — it’s the hypercompetitiveness and the need to constantly innovate. To move faster, many development teams have turned to native cloud technologies, microservices architectures, and open-source code to accelerate and scale their efforts. Additionally, development teams have adopted agile methodologies and are automating as many steps in the development process as possible.

While this evolution increases the speed of the software development lifecycle, it also introduces new complexities and risks.

For our 12th State of Software Security report, we’ll explore these trends with the help of the Cyentia Institute to assess how the software security landscape is continuing to evolve. Our goal is to help you make informed decisions about your software security program so that you can minimize your risk and meet cybersecurity regulations like those outlined in the **White House Executive Order on Improving the Nation’s Cybersecurity** issued on May 12, 2021.

---

## The State of Software Security at a Glance

Similar to last year, we looked at the entire history of active applications, not just the activity associated with the application over one year. By doing so, we can view the full life cycle of applications, which results in more accurate metrics and observations. Aside from looking at the past, we also imagined the future by considering practices — such as Veracode Security Labs training — that might help improve application security.

- **The Number of Apps Scanned Has Tripled**: Organizations are scanning, on average, more than 17 new applications per quarter. This number is more than triple the number of apps scanned per quarter a decade ago (3X increase).
- **Microservices**: In 2018, roughly 20 percent of applications incorporated multiple languages. This year, less than 5 percent of apps used multiple languages, suggesting a pivot to smaller, one-language applications or microservices. JavaScript, Python, and .NET have seen declines in app sizes, indicating a trend toward more microservices.
- **Scan Cadence**: Continuous testing and integration, which includes security scanning in pipelines, is becoming the norm. A decade ago applications were scanned two or three times a year. Now, 90 percent of applications are scanned more than once a week with the majority scanned three times a week (20X increase in median scan cadence from 2010 to 2021).
- **Multiple Scan Types**: We’ve seen a 31 percent increase in the use of multiple scan types between 2018 and 2021, with much of that gain coming from organizations using the full suite of static, dynamic, and SCA scans.
- **Third-Party Libraries**: 77% of flaws in third-party libraries remain unfixed after three months. On a positive note, there is a noticeable improvement in time to remediation for third-party flaws. Back in 2017, it would take over three years to get to the 50 percent (half-life) closed point, and now it takes just over a year.
- **Open Source**: Open-source libraries are still a significant cause for concern. 97% of Java applications are made up of open source libraries. In 2010, 35% of libraries used had a known flaw; by 2021, this dropped to 10%.
- **Veracode Security Labs**: On average, organizations with Veracode Security Labs training decrease their time to fix 50 percent of flaws by 35 percent.

---

## Introduction

In 2019, for our 10th annual State of Software Security report, we began looking at the specific concerns associated with the use of open-source software and have been fortunate to be able to map the complex landscape of secure software development. We’ve identified a few ideas that many of our customers probably feel in their hearts, and we confirm them with data — things like scanning at a regular, rapid pace is good.

Security debt can build over time, and addressing it early can help mitigate work down the road. Using multiple types of scanning — static, dynamic, and software composition analysis — can give a fuller picture of an application’s security, and it helps remediation happen more quickly and more completely.

These things can help every application, even those old creaky legacy applications, and it’s been rewarding to be able to verify and quantify the effect of what many developers feel makes applications more secure.

> **So where does that leave us for this 12th report?**
> We feel like we’ve quantified some of the mysteries about application security with Veracode’s extensive data, and we could continue to do that. But we think it behooves an industry to occasionally take a step back to try to get a view of the past and take a look toward the future — to see where the landscape has been steady and where it’s changed and to try to understand which principles have stood the test of time and which have faltered.

So we’re going to do just that:
1. **Look at the use of software analysis tools**: We’ll start with a look at how people are using software analysis tools and how that’s changed over the years. We’ll see development trends reflected in those scans. We’ll look at how free and open-source software continues to be integral (though variably so) to most applications.
2. **Analyze flaws in software**: Then we’ll look at how those development trends manifest themselves in the flaws that get introduced into software.
3. **Examine how flaws are fixed**: Next, we’ll examine how things are fixed and whether developers are getting better at fixing things.
4. **Look to the future of secure software**: Lastly, we’ll take a peek into the future and think about what exactly developers can do to write more secure software. In particular, we’ll see that the simple act of taking time to learn how to fix flaws helps get them fixed faster and helps prevent future bugs from showing up.

Let’s take a quick trip down memory lane...

---

## How Software Development Has Changed

One of the advantages of serving the software development community for so long is that Veracode is able to see changes in development practices over time. So rather than diving right into security this year, we want to focus on how developers themselves are approaching applications and how that’s changed.

### The Number of Applications Scanned Has Tripled

First, we want to examine just how many applications developers are scanning for flaws. Figure 1 shows that more applications are being scanned than ever before. And the increase is not simply due to the fact that there are more organizations. In the last year, most organizations are creating, on average, more than 17 applications for scanning per quarter, up from approximately five a decade ago. But why might this be the case?

We have two hypotheses:
1. Organizations are creating smaller, more modular applications that do a single thing.
2. Organizations are expanding the scope of their security to lower-criticality applications.

*![Figure 1: Application creation over time showing an upward trend in new applications per account from 2007 to 2022]*

We actually see that the latter is not true in Figure 2. The distribution of app criticality has been fairly constant, with some bumps along the way when new or existing users onboard many applications (as was the case in mid-2020 when a single user scanned a few hundred “Medium” criticality applications). The skew has been pretty consistent over the last 10 years, with most applications having “High” or “Very High” criticality, and only a handful registering “Low” or “Very Low.”

*![Figure 2: Application criticality over time showing consistent percentages of High and Very High criticality applications]*

If developers are not simply scanning applications they considered unimportant before, perhaps there is a profusion of new applications — smaller, more modular ones. Some might call them “microservices.”

### The Rise of Microservices

What defines microservices? They are collections of loosely coupled applications, usually with a small codebase, that communicate via APIs. The advantage of microservices is that it’s easier to work on the various parts of an application if changing one part is unlikely to affect the other bits.

So how might we see this reflected among Veracode users? Well, we’d expect applications to increasingly use one language and become smaller in size. Figure 3 looks at the first part of that hypothesis.

*![Figure 3: Use of multiple languages in new applications compared to Google search interest in microservices]*

**Are developers pivoting to microservices?**
Up until roughly 2018, there was a slow but steady increase in the number of applications using multiple languages, up to a peak (excluding outliers) of about 20 percent of apps incorporating multiple languages. But as the notion of microservices gained favor and took over, there was a nosedive, with less than 5 percent of applications currently using multiple languages.

So we see that developers are using one language at a time, but are their applications getting smaller? Figure 4a says it’s complicated.

*![Figure 4a: Application size over time for JavaScript, Python, .NET, C++, Java, and others]*

Applications written in a few languages we might consider “good” for a microservice-type architecture certainly have declined in size.
- **JavaScript**: JavaScript applications have gotten considerably smaller over time, possibly with the inclusion of a more diverse and robust library ecosystem.
- **Python and .NET**: Both Python and .NET have seen reductions in size, but that may be more regression to the mean than a true trend.
- **C++ and Java**: Meanwhile, applications written in more established languages like C++ and Java have remained more or less the same size over the past few years.
- **Scala**: Scala applications have seen a decline in size, and the popularity of Scala compared to its more heavyweight godfather Java may have something to do with different architectural goals.
- **Go**: Interestingly, Go, a language commonly associated with microservices, has actually seen an increase in application size.
- **Android**: Android applications were getting increasingly large until the release of Android N, which switched to an OpenJDK. This allowed for significantly smaller application sizes and was followed by another slow and steady increase. *(See Figure 4b)*

---

### Increase in Median Scan Cadence

> "It is no longer sufficient to scan software as a pre-production step in the last phase of the software development lifecycle. Just as software is now deployed continuously, software security scanning must also happen continuously as a fully integrated part of the software development process."  
> — **Sam King, CEO, Veracode**

It’s been said that “software is eating the world.” We think it’s probably also fair to say that “agile is eating the software world.” Continuous testing and integration, which includes security scanning into pipelines, is becoming the norm, and we can see that reflected in how often users are scanning their applications. A decade ago users were averaging two or three scans a year. Now, most are running daily static scans and weekly dynamic scans. Software composition analysis (SCA) scans also occur at least weekly. The sooner in the lifecycle you can discover problems, the more likely you’ll be able to solve them quickly, before they become bigger a problem down the road.

If you look back at SOSS volumes 9, 10, and 11, you’ll see that applications that are scanned at a regular cadence fix more flaws faster than those that are only scanned periodically. Security seems to prefer agile development.

*![Figure 5: Scanning cadence over time across Manual, Dynamic, Static, and SCA Agent scans]*

- **Median Scan Cadence (2010 vs 2021)**: In 2010, the median application was scanned less than once a month (only 10 percent of apps scanned more often than weekly). By 2021, 90 percent of apps are scanned more than once a week (with the majority scanned three times a week) — a 20X increase.

---

### Organizations Are Using Multiple Types of Scanning

Part of the advantage of the continuous integration paradigm is the ability to easily add new components to the pipeline. Static testing? A must. The use of dynamic analysis is growing as well, and since we’re becoming more and more aware of the potential risks inherent in open-source software, it’s a no-brainer that secure development includes software composition analysis.

We’ve seen a **31 percent increase** in the use of multiple scan types between 2018 and 2021, with much of that gain coming from organizations using the full suite of static, dynamic, and SCA scans.

> **LAST YEAR WE FOUND:**
> Organizations that used dynamic in addition to static scanning were able to remediate 50% of flaws on average **24 days faster**. And including SCA shaves off another **6 days**.

---

## Software Bill of Mistakes

> "In many respects, development teams have shifted from writing software to assembling software."  
> — **Chris Wysopal, CTO and Co-Founder, Veracode**

---

### Organizations Heavily Leverage Open-Source Libraries

How has open-source, and, more generally, third-party software changed over the last few years? Last year’s report looked at the proportion of code included in each scan that was third-party code versus homegrown. What we saw was interesting. Most applications (depending on the language) had a kind of barbell effect, being composed of almost entirely third-party code or almost entirely in-house code.

There were of course some exceptions. Java’s OOP design philosophy of gluing classes together until your code begins to look like a functioning application makes code reuse a breeze. And why write your own classes when there are perfectly good third-party ones freely available? The result is that most of the code in Java applications comes from third parties. But have those barbells evolved over time? Let’s take a look at Figure 6.

- **Java**: Java remains steadfastly mostly third-party code and has pushed even more so in that direction in the last few years.
- **.NET**: There is an interesting “shock” to the data for .NET: In mid-2020, we saw an abrupt shift in the percentage of third-party code in .NET applications. The relative time period coincides with the release of .NET 5 (formerly .NET core), which integrated and unified a good amount of functionality into a single framework.
- **JavaScript and Python**: JavaScript and Python show the barbell effect, with applications being either mostly homegrown or mostly third-party libraries, causing the trend line to bounce around the middle over time.
- **PHP and C++**: PHP and C++ remain relatively constant, leaning heavily toward mostly homegrown code.

*![Figure 6: Third-party code proportion by language across Java, .NET, JavaScript, Python, PHP, and C++]*

---

### Most Developers Stick With The Same Libraries Year Over Year

We are seeing some evolution in terms of how much third-party code developers are using in each language. 

> **We found that developers stick with tried-and-true libraries and rarely attempt to refactor their code base to pick up the "coolest" or "most-popular" libraries.**

Last year’s open source report looked at shifts in the use of vulnerable libraries between 2019 and 2020. Figure 7 takes a look at how the top 10 most popular libraries across our six languages of interest have evolved over time.[^2]

Figure 7 is a stacked area chart where each band represents the percentage of scanned repositories using a particular library. For all languages, the most popular libraries haven't changed all that much. Things like `debug` and `inherits` continue to be popular for JavaScript. The larger lesson here is that developers stick with tried-and-true libraries and do not frequently refactor their code base to pick up the latest hot commodity.

*![Figure 7: Popular libraries by language across Java, .NET, PHP, JavaScript, Python, and Ruby]*

---

### Third-Party Libraries Have Fewer Flaws

We’ve seen library usage evolve over time. But what implications does that have for security? The recent **Executive Order on Improving the Nation’s Cybersecurity** lays out strict guidelines regarding software supply chains and critical software.

So are applications using more or fewer flawed libraries? Figure 8 tells a language-specific story.

*![Figure 8: Percent of flawed libraries by language across .NET, Java, JavaScript, PHP, Python, and Ruby]*

There are clear, steep downward trends for Java, JavaScript, and Python:
- **Java**: In 2017, nearly 35 percent of libraries used had a known flaw; in recent years, this has dropped to nearly 10 percent.
- **JavaScript**: Gone from about 10 percent to less than 4 percent.
- **Python**: Gone from about 25 percent to nearly 10 percent.
- **Go**: Gone from 7 percent down to 4 percent (not shown).

---

## The Flaws of Yesterday Are (Still) the Flaws of Today

This type of report would be relatively easy to create if all — or heck, even some — of the attacks were fresh and new. But history teaches us that we experience the same types of flaws year after year. While there are variations among languages, the technical flaws themselves do not go away, and any changes tend to evolve slowly.

Taking the flaws listed in the OWASP Top 10 and CWE/SANS Top 25 classified as "High" criticality or above, Figure 9 shows the overall trend in applications with various flaw types in static analysis. Although lines bounce around, they are all slowly decreasing.

*![Figure 9: Percent of applications with various flaw types in static analysis showing a general reduction]*

---

### The Lowdown on Static, Dynamic, and Software Composition Analysis

Each language has its own strengths and weaknesses when it comes to secure development. Figure 10 outlines the top software weaknesses discovered by scan type.

*![Figure 10: Top software weaknesses discovered by scan type (Static, Dynamic, SCA)]*

#### Static Analysis
Static analysis looks directly at the source code and depends heavily on the development language. Flaws with buffer/memory management are common in C++, but nonexistent in .NET or Java. CRLF injection is the top flaw type overall for static analysis.
- **JavaScript**: Growing challenges with identity management (credentials management and authentication issues trending upward).
- **Java**: Overall declines are clearly more pronounced than in PHP.

*![Figure 11: Software weaknesses found by static analysis by language]*

#### Dynamic Analysis
Dynamic scanning runs against the runtime environment and finds flaws in execution and interface. The top flaws (`Server Configuration`, `Information Leakage`) are consistent across all underlying languages.

*![Figure 12: Software weaknesses found by dynamic analysis]*

#### Software Composition Analysis (SCA)
SCA tracks open-source projects and packages. Flaws vary by language (Java, JavaScript, and Python show clear declines, while .NET and C++ do not show that same decline in third-party libraries).

*![Figure 13: Software weaknesses found by SCA, by language]*

---

### Fix Rate Comparisons by Scan Type

Figure 14 looks at the millions of flaws tracked and estimates how long any particular flaw remains open.

*![Figure 14: Probability of flaw remaining open by scan type]*

- **77% of flaws in third-party libraries** remain unfixed after the first three months.
- **57% of flaws found through dynamic analysis** are still around after three months.
- **Half-Life to Remediation**: 
  - Dynamic Analysis: **143 days**
  - Static Analysis: **290 days**
  - SCA: **397 days (approx. 1.1 years)**

> **Historical Progress on Half-Life (Figure 15)**: Back in 2017, SCA flaws took over three years to reach the 50% closed point; today, that has been driven down to just over a year. However, static scan remediation has slipped from under 200 days in 2017 to just under 300 days currently.

---

### Capacity for Flaw Remediation by Scan Type

Figure 16 captures the overall monthly capacity (percentage of open flaws fixed every month) over the last five years. Remediation of both static flaws and SCA flaws in a given month is on the rise.

*![Figure 16: Monthly capacity for flaw remediation by scan type]*

---

## Where Do We Go From Here?

### Most Organizations Using Veracode Security Labs Are Fixing Flaws Faster

Veracode Security Labs gives developers hands-on experience fixing common flaws through real example applications written in various languages. Most lessons average less than an hour to complete.

*![Figure 17: Time spent learning in Veracode Security Labs]*

#### Do these efforts make a difference?
Yes. Figure 18 indicates that flaws found after Veracode users completed at least one lesson were fixed faster than those found when developers had no training.
- **With Training**: 50% of flaws fixed within **110 days**.
- **Without Training**: 50% of flaws fixed within **170 days**.
- **Result**: A **2-month difference** on average!

*![Figure 18: Probability of flaw remaining open by training history]*

Furthermore, Figure 19 shows that for most languages, the percentage of static scans that find flaws is reduced after completing lessons (e.g., nearly 20% reduction for JavaScript).

*![Figure 19: Flaws found before and after training by language]*

---

## Conclusions

Standing here in 2022, what can we say we’ve learned?

1. **Agile development of small, modular applications has eaten the world.** We’ve seen an explosion in scanned applications, moving from quarterly scans to daily scans, alongside an expanded use of scanning technologies.
2. **Free and open-source code will continue to be a blessing and a curse.** Developers are using fewer libraries with known flaws, which is cause for optimism.
3. **Applications are, slowly but surely, getting more secure.** Nearly across the board, we’ve seen steady progress toward more secure applications with downward trends in flaw prevalence.
4. **New tools will continue to help improve the application security landscape.** Integrated continuous scanning and hands-on platforms like Veracode Security Labs help developers understand and prevent security flaws.

---

## Appendix: Methodology

Our methodology for data analysis diverged slightly from earlier volumes. Rather than focusing solely on active development within a 12-month window, the core data represents full historical data from Veracode services and customers.

This accounts for a total of:
- **592,720** applications that used all scan types
- **1,034,855** dynamic analysis scans
- **5,137,882** static analysis scans
- **18,473,203** software composition analysis scans

All those scans produced:
- **42 million** raw static findings
- **3.5 million** raw dynamic findings
- **6 million** raw software composition analysis findings

The data represents large and small companies, commercial software suppliers, software outsourcers, and open-source projects.[^4]

---

## A Note on Mass Closures

While preparing data, we noticed several large single-day closure events where applications closed thousands of findings in a single scan. Upon further exploration, we found many of these to be invalid (developers scanning entire filesystems, invalid branches, or previous branches, where rescan marked unfound findings as "fixed").

The top one-tenth of 1 percent of scans (0.1 percent) accounted for almost a quarter of all closed findings. These "mass closure" events significantly distort measurements of flaw persistence and time to remediation and were ultimately excluded from the analysis.

---

[^1]: Footnote content referenced throughout academic and technical literature.
[^2]: A few notes on this figure. We are swapping Ruby in here for C/C++ as most C/C++ applications don’t use an explicit package manager and instead use makefiles to see if appropriate libraries are present. This can make extracting what applications are using what libraries pretty tough. We only have data going back to 2019 on .NET, so be sure to check the scales. Finally, the colors in this figure are used to differentiate the individual libraries, but are reused for purely aesthetic reasons.
[^3]: Veracode State of Software Security, volumes 9, 10, and 11.
[^4]: Here we mean open source developers who use Veracode tools on applications in the same way closed source developers do. This is distinct from the software composition analysis presented in the report.

<!-- CONVERSION_METADATA: {"source": "https://github.com/jacobdjwilson/awesome-annual-security-reports", "date": "2026-09-17", "model": "gemini-3.5-flash-lite"} -->
