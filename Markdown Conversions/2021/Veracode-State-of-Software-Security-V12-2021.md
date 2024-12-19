# THE PROGRESS WE’VE ALL MADE

## Contents
[Executive Summary](#executive-summary)
[The State of Software Security at a Glance](#the-state-of-software-security-at-a-glance)
[Introduction](#introduction)
[How Software Development Has Changed](#how-software-development-has-changed)
[The Number of Applications Scanned Has Tripled](#the-number-of-applications-scanned-has-tripled)
[The Rise of Microservices](#the-rise-of-microservices)
[Increase in Median Scan Cadence](#increase-in-median-scan-cadence)
[Organizations Are Using Multiple Types of Scanning](#organizations-are-using-multiple-types-of-scanning)
[Software Bill of Mistakes](#software-bill-of-mistakes)
[Organizations Heavily Leverage Open-Source Libraries](#organizations-heavily-leverage-open-source-libraries)
[Most Developers Stick With the Same Libraries Year Over Year](#most-developers-stick-with-the-same-libraries-year-over-year)
[Third-Party Libraries Have Fewer Flaws](#third-party-libraries-have-fewer-flaws)
[The Flaws of Yesterday Are (Still) the Flaws of Today](#the-flaws-of-yesterday-are-still-the-flaws-of-today)
[The Lowdown on Static, Dynamic, and Software Composition Analysis](#the-lowdown-on-static-dynamic-and-software-composition-analysis)
[Fix Rate Comparisons by Scan Type](#fix-rate-comparisons-by-scan-type)
[Capacity for Flaw Remediation by Scan Type](#capacity-for-flaw-remediation-by-scan-type)
[Where Do We Go From Here?](#where-do-we-go-from-here)
[Most Organizations Using Veracode Security Labs Are Fixing Flaws Faster](#most-organizations-using-veracode-security-labs-are-fixing-flaws-faster)
[Conclusions](#conclusions)
[Appendix: Methodology](#appendix-methodology)
[A Note on Mass Closures](#a-note-on-mass-closures)

## Executive Summary
The world is becoming more connected than ever before … Connectivity makes our lives easier, but it also increases risk. One security flaw can have a domino effect, leaving software vulnerable all across the globe.

But it’s not just increased connectivity that’s shaping the security landscape — it’s the hypercompetitiveness and the need to constantly innovate. To move faster, many development teams have turned to native cloud technologies, microservices architectures, and open-source code to accelerate and scale their efforts. Additionally, development teams have adopted agile methodologies and are automating as many steps in the development process as possible.

While this evolution increases the speed of the software development lifecycle, it also introduces new complexities and risks.

For our 12th State of Software Security report, we’ll explore these trends with the help of the Cyentia Institute to assess how the software security landscape is continuing to evolve. Our goal is to help you make informed decisions about your software security program so that you can minimize your risk and meet cybersecurity regulations like those outlined in the White House Executive Order on Improving the Nation’s Cybersecurity issued on May 12, 2021.

Similar to last year, we looked at the entire history of active applications, not just the activity associated with the application over one year. By doing so, we can view the full life cycle of applications, which results in more accurate metrics and observations. Aside from looking at the past, we also imagined the future by considering practices — such as Veracode Security Labs training — that might help improve application security.

## The State of Software Security at a Glance
### Microservices
In 2018, roughly 20 percent of applications incorporated multiple languages. This year, less than 5 percent of apps used multiple languages, suggesting a pivot to smaller, one-language applications or microservices.

*Image description: A bar chart showing the percentage of applications using multiple languages in 2018 (20%) and 2021 (5%).*

JavaScript, Python, and .NET have seen declines in app sizes, indicating a trend toward more microservices.

### The Number of Apps Scanned Has Tripled
Organizations are scanning, on average, more than 17 new applications per quarter. This number is more than triple the number of apps scanned per quarter a decade ago.

*Image description: A graphic showing "3X INCREASE IN NUMBER OF APPS SCANNED" with the years 2011 and 2021.*

### Scan Cadence
Continuous testing and integration, which includes security scanning in pipelines, is becoming the norm. A decade ago applications were scanned two or three times a year. Now, 90 percent of applications are scanned more than once a week with the majority scanned three times a week.

*Image description: A graphic showing "20X INCREASE IN MEDIAN SCAN CADENCE FROM 2010 TO 2021" with the years 2010 and 2021.*

### Flaw Prevalence
Third-party libraries have fewer flaws.

*Image description: A graphic showing the percentage of libraries with known flaws in 2017 (35%) and 2021 (10%).*

### Multiple Scan Types
We’ve seen a 31 percent increase in the use of multiple scan types between 2018 and 2021, with much of that gain coming from organizations using the full suite of static, dynamic, and SCA scans.

*Image description: A graphic showing "31% INCREASE in the use of multiple scan types" with the years 2018 and 2021.*

### Third-Party Libraries
On a positive note, there is a noticeable improvement in time to remediation for third-party flaws. Back in 2017, it would take over three years to get to the 50 percent (half-life) closed point, and now it takes just over a year.

*Image description: A graphic showing the time it takes to fix flaws in third-party libraries in 2017 (3 years) and 2021 (1 year) with a text overlay stating "DECREASE in the time it takes for organizations to fix flaws".*

### Open Source
Open-source libraries are still a significant cause for concern.

*Image description: A graphic stating "97% of Java applications are made up of open source libraries".*

### Veracode Security Labs
On average, organizations with Veracode Security Labs training decrease their time to fix 50 percent of flaws by 35 percent.

*Image description: A graphic stating "35%".*

## Introduction
In 2019, for our 10th annual State of Software Security report, we began looking at the specific concerns associated with the use of open-source software and have been fortunate to be able to map the complex landscape of secure software development. We’ve identified a few ideas that many of our customers probably feel in their hearts, and we confirm them with data — things like scanning at a regular, rapid pace is good.

Security debt can build over time, and addressing it early can help mitigate work down the road. Using multiple types of scanning — static, dynamic, and software composition analysis — can give a fuller picture of an application’s security, and it helps remediation happen more quickly and more completely.

These things can help every application, even those old creaky legacy applications, and it’s been rewarding to be able to verify and quantify the effect of what many developers feel makes applications more secure.

So where does that leave us for this 12th report? We feel like we’ve quantified some of the mysteries about application security with Veracode’s extensive data, and we could continue to do that. But we think it behooves an industry to occasionally take a step back to try to get a view of the past and take a look toward the future — to see where the landscape has been steady and where it’s changed and to try to understand which principles have stood the test of time and which have faltered.

So we’re going to do just that:

1.  Look at the use of software analysis tools

    We’ll start with a look at how people are using software analysis tools and how that’s changed over the years. We’ll see development trends reflected in those scans. We’ll look at how free and open-source software continues to be integral (though variably so) to most applications.
2.  Analyze flaws in software

    Then we’ll look at how those development trends manifest themselves in the flaws that get introduced into software.
3.  Examine how flaws are fixed

    Next, we’ll examine how things are fixed and whether developers are getting better at fixing things.
4.  Look to the future of secure software

    Lastly, we’ll take a peek into the future and think about what exactly developers can do to write more secure software. In particular, we’ll see that the simple act of taking time to learn how to fix flaws helps get them fixed faster and helps prevent future bugs from showing up.

Let’s take a quick trip down memory lane …

## How Software Development Has Changed
One of the advantages of serving the software development community for so long is that Veracode is able to see changes in development practices over time. So rather than diving right into security this year, we want to focus on how developers themselves are approaching applications and how that’s changed.

## The Number of Applications Scanned Has Tripled
First, we want to examine just how many applications developers are scanning for flaws. Figure 1 shows that more applications are being scanned than ever before. And the increase is not simply due to the fact that there are more organizations. In the last year, most organizations are creating, on average, more than 17 applications for scanning per quarter, up from approximately five a decade ago. But why might this be the case?

We have two hypotheses:

1.  Organizations are creating smaller, more modular, applications that do a single thing.
2.  Organizations are expanding the scope of their security to lower-criticality applications.

Organizations are scanning, on average, more than 17 new applications per quarter. This number is more than triple the number of apps scanned per quarter a decade ago.

*Image description: A line graph showing the average number of new applications scanned per account over time, from 2007 to 2022. The number of accounts is also shown as a reference.*

We actually see that the latter is not true in Figure 2. The distribution of app criticality has been fairly constant, with some bumps along the way when new or existing users onboard many applications (as was the case in mid-2020 when a single user scanned a few hundred “Medium” criticality applications). The skew has been pretty consistent over the last 10 years, with most applications having “High” or “Very High” criticality, and only a handful registering “Low” or “Very Low.”

*Image description: A stacked area chart showing the percentage of applications by criticality (Very Low, Low, Medium, High, Very High) over time, from 2010 to 2021.*

If developers are not simply scanning applications they considered unimportant before, perhaps there is a profusion of new applications — smaller, more modular ones. Some might call them “microservices.”

## The Rise of Microservices
What defines microservices? They are collections of loosely coupled applications, usually with a small codebase, that communicate via APIs. The advantage of microservices is that it’s easier to work on the various parts of an application if changing one part is unlikely to affect the other bits.

So how might we see this reflected among Veracode users? Well, we’d expect applications to increasingly use one language and become smaller in size. Figure 3 looks at the first part of that hypothesis.

*Image description: A line graph showing the percentage of multi-language applications over time, from 2009 to 2022, with a secondary y-axis showing the number of applications. A line graph of Google search interest in "microservices" is also shown as a reference.*

Up until roughly 2018, there was a slow but steady increase in the number of applications using multiple languages, up to a peak (excluding outliers) of about 20 percent of apps incorporating multiple languages. But as the notion of microservices gained favor and took over, there was a nosedive, with less than 5 percent of applications currently using multiple languages.

In 2018, roughly 20 percent of applications incorporated multiple languages. This year, less than 5 percent of apps used multiple languages.

Are developers pivoting to microservices?

So we see that developers are using one language at a time, but are their applications getting smaller? Figure 4a says it’s complicated.

*Image description: A series of line graphs showing the mean size (MB) of applications over time for different languages: Java, C++, PHP, JavaScript, Python, and .NET. The x-axis is the date of first static scan.*

*Image description: A line graph showing the scan size (MB) of Android applications over time, from 2012 to 2022.*

### JAVASCRIPT
JavaScript applications have gotten considerably smaller over time, possibly with the inclusion of a more diverse and robust library ecosystem.

### PYTHON AND .NET
Both Python and .NET have seen reductions in size, but that may be more regression to the mean than a true trend.

### C++ AND JAVA
Meanwhile, applications written in more established languages like C++ and Java have remained more or less the same size over the past few years.

### SCALA
Scala applications (not shown) have seen a decline in size, and the popularity of Scala compared to its more heavyweight godfather Java may have something to do with different architectural goals.

### GO
Interestingly, Go (not shown), a language commonly associated with microservices, has actually seen an increase in application size.

### ANDROID
A quick aside on Android applications: Android applications were getting increasingly large until the release of Android N, which switched to an OpenJDK. This allowed for significantly smaller application sizes and was followed by another slow and steady increase. We don’t think this is a trend, but it’s nice to see major events in software ecosystems validated in data.

Applications written in a few languages we might consider “good” for a microservice-type architecture certainly have declined in size.

## Increase in Median Scan Cadence
>“It is no longer sufficient to scan software as a pre-production step in the last phase of the software development lifecycle. Just as software is now deployed continuously, software security scanning must also happen continuously as a fully integrated part of the software development process.”
>
>SAM KING, CEO, VERACODE

It’s been said that “software is eating the world.” We think it’s probably also fair to say that “agile is eating the software world.” Continuous testing and integration, which includes security scanning into pipelines, is becoming the norm, and we can see that reflected in how often users are scanning their applications. A decade ago users were averaging two or three scans a year. Now, most are running daily static scans and weekly dynamic scans. Software composition analysis (SCA) scans also occur at least weekly. The sooner in the lifecycle you can discover problems, the more likely you’ll be able to solve them quickly, before they become bigger a problem down the road.

*Image description: A line graph showing the mean time between scans (days) over time for different scan types: Manual, Dynamic, Static, and SCA Agent. The x-axis is the date of first scan.*

But is scanning more good? If you look back at SOSS volumes 9, 10, and 11, you’ll see that applications that are scanned at a regular cadence fix more flaws faster than those that are only scanned periodically. Security seems to prefer agile development.

### Median Scan Cadence
**2010**
Median application was scanned less than once a month (only 10 percent of apps scanned more often than weekly)

**2021**
90 percent of apps scanned more than once a week (majority scanned three times a week)

**20X increase**

## Organizations Are Using Multiple Types of Scanning
Part of the advantage of the continuous integration paradigm is the ability to easily add new components to the pipeline. Static testing? A must. The use of dynamic analysis is growing as well, and since we’re becoming more and more aware of the potential risks inherent in open-source software, it’s a no-brainer that secure development includes software composition analysis.

We’ve seen a 31 percent increase in the use of multiple scan types between 2018 and 2021, with much of that gain coming from organizations using the full suite of static, dynamic, and SCA scans. We’re not just pointing this out as a random fact.

>LAST YEAR WE FOUND:
>
>Organizations that used dynamic in addition to static scanning were able to remediate
>
>50% of flaws
>
>On average
>
>24 days faster
>
>And including SCA shaves off
>
>another 6 days

So fire up those scanners, folks!

## Software Bill of Mistakes
>“In many respects, development teams have shifted from writing software to assembling software.”
>
>CHRIS WYSOPAL, CTO AND CO-FOUNDER, VERACODE

## Organizations Heavily Leverage Open-Source Libraries
How has open-source, and, more generally, third-party software changed over the last few years?

Last year’s report looked at the proportion of code included in each scan that was third-party code versus homegrown. What we saw was interesting. Most applications (depending on the language) had a kind of barbell effect, being composed of almost entirely third-party code or almost entirely in-house code.

There were of course some exceptions. Java’s OOP design philosophy of gluing classes together until your code begins to look like a functioning application makes code reuse a breeze. And why write your own classes when there are perfectly good third-party ones freely available? The result is that most of the code in Java applications comes from third parties. But have those barbells evolved over time? Let’s take a look at Figure 6.

*Image description: A series of stacked bar charts showing the proportion of third-party code in applications by language (.NET, Python, C++, JavaScript, Java, PHP) over time, from 2019 to 2021.*

### JAVA
Java remains steadfastly mostly third-party code and has pushed even more so in that direction in the last few years.

### .NET
There is an interesting “shock” to the data for .NET: In mid-2020, we saw an abrupt shift in the percentage of third-party code in .NET applications. The relative time period coincides with the release of .NET 5 (formerly .NET core), which integrated and unified a good amount of functionality into a single framework. It’s good to see developers keep up with the latest updates.

### JAVASCRIPT AND PYTHON
JavaScript and Python show the barbell effect, with applications being either mostly homegrown or mostly third-party libraries, causing the trend line to bounce around the middle over time.

### PHP AND C++
PHP and C++ remain relatively constant, leaning heavily toward mostly homegrown code.

## Most Developers Stick With the Same Libraries Year Over Year
We are seeing some evolution in terms of how much third-party code developers are using in each language.

Last year’s open source report looked at shifts in the use of vulnerable libraries between 2019 and 2020. Since we’re focusing on how things have evolved over as long a time period as the data can muster, we want to expand that view a little bit here. Figure 7 takes a look at how the top 10 most popular libraries across our six languages of interest have evolved over time.

1.  Figure 7 is what is referred to as a stacked area chart. Each band represents the percentage of scanned repositories that are using a particular library. The thicker the band, the more popular the library. When the overall height of the chart increases, it indicates that those 10 libraries are all growing in popularity. If libraries waxed and waned in popularity frequently, we would expect to see large swells of color that might peter out over time. We don’t see that in Figure 7, but rather mostly uniform popularity of those top libraries.

We won’t spend a ton of time going over each wiggle. But what we do see is that, for all the languages, the most popular libraries haven’t changed all that much. Things like debug and inherits continue to be popular for JavaScript though they may swap around the top few spots year over year. The larger lesson here is that developers are going to stick with tried-and-true libraries and likely aren’t going to attempt to refactor their code base to pick up the latest hot commodity.

This is indeed what we saw in last year’s SOSS: Open Source Edition. Updates happened slowly when libraries didn’t have flaws, but relatively quickly when they did. As long as open-source developers continue to fix security flaws, developers will keep on using those libraries.

2.  A few notes on this figure. We are swapping Ruby in here for C/C++ as most C/C++ applications don’t use an explicit package manager and instead use makefiles to see if appropriate libraries are present. This can make extracting what applications are using what libraries pretty tough. We only have data going back to 2019 on .NET, so be sure to check the scales. Finally, the colors in this figure are used to differentiate the individual libraries, but are reused for purely aesthetic reasons.

Keep on keeping on …

We found that developers stick with tried-and-true libraries and rarely attempt to refactor their code base to pick up the “coolest” or “most-popular” libraries.

*Image description: A series of stacked area charts showing the relative popularity of the top 10 libraries for different languages (Java, .NET, Python, Ruby, PHP, JavaScript) over time, from 2018 to 2021.*

## Third-Party Libraries Have Fewer Flaws
We’ve seen library usage evolve over time, though maybe not in a nice smooth trend. But what implications does that have for security? After all, that’s really what we’re here to talk about, right? Making applications more secure. Even the federal government is taking notice of this whole “third-party libraries might be risky, actually” idea.

The recent Executive Order on Improving the Nation’s Cybersecurity lays out the following about securing the software supply chain:

>“The development of commercial software often lacks transparency, sufficient focus on the ability of the software to resist attack, and adequate controls to prevent tampering by malicious actors. There is a pressing need to implement more rigorous and predictable mechanisms for ensuring that products function securely, and as intended. The security and integrity of ‘critical software’ — software that performs functions critical to trust (such as affording or requiring elevated system privileges or direct access to networking and computing resources) — is a particular concern. Accordingly, the Federal Government must take action to rapidly improve the security and integrity of the software supply chain, with a priority on addressing critical software.”

So are applications using more or fewer flawed libraries? As with many things in our research, Figure 8 tells a language-specific story. (But before you dive into Figure 8, notice that the vertical axes are different for different languages.)

*Image description: A series of line graphs showing the percentage of vulnerable libraries by language (.NET, Java, PHP, Python, JavaScript, Ruby) over time, from 2017/2018 to 2021. Note that the vertical axis scales differ between languages.*

There are clear trends for Java, JavaScript, and Python, and that trend is very good, because it goes steeply down. In 2017 nearly 35 percent (on average) of libraries used had a known flaw. In more recent years that has come down to nearly 10 percent. JavaScript has gone from about 10 percent to less than 4 percent, Python from about 25 percent to nearly 10 percent, and Go (not shown) from 7 percent down to 4 percent.

## The Flaws of Yesterday Are (Still) the Flaws of Today
This type of report would be relatively easy to create if all — or heck, even some — of the attacks were fresh and new. The stories would almost write themselves. But history is teaching us that we will experience the same types of flaws year after year. Sure, there are variations among languages and things may shift around in prevalence. But by and large, the technical flaws themselves don’t go away, and any changes we do observe tend to evolve slowly.

Take as an example Figure 9 (or really any of the upcoming plots). We pulled out the flaws listed in the OWASP Top 10 and CWE/SANS Top 25 and those classified as “High” criticality or above. If you look closely at each of those over time, you’ll notice some peaks and valleys. But we want you to pull back a bit, and perhaps squint your eyes so that you can see the overall trend in these plots. Notice that, even though the lines may bounce around, they are all slowly decreasing.

That’s good news: The trend across all the applications is a general reduction in flaw prevalence.

*Image description: A line graph showing the percentage of applications with various flaw types (Any Flaws, CWE/SANS Top 25, High Severity, OWASP) in static analysis over time, from 2016 to 2020.*

The trend across all the applications is a general reduction in flaw prevalence.

## The Lowdown on Static, Dynamic, and Software Composition Analysis
Even though we just said you should take a step back and look at the big picture, we offer this next plot as an example of both why that’s a good thing and why you don’t want to stop there.

As you look at the rankings in Figure 10 you’ll probably notice that CRLF injection is more prevalent than information leakage. Maybe you find that helpful, but as anyone who’s worked in more than one language will tell you, each language has its own strengths and weaknesses, and this applies to secure development as well. The development language matters when it comes to the types of flaws introduced — at least for some of the detection methods.

Therefore, it’s worthwhile to understand a bit about these methods because it will help point us in the direction of further areas to investigate.

*Image description: A table showing the top software weaknesses discovered by scan type (Static Analysis, Dynamic Analysis, SCA). The weaknesses are listed in order of prevalence.*

Static analysis looks directly at the source code and thus needs to know what to look for in different languages. It’s very strong at detecting places where maybe memory isn’t managed correctly or input isn’t properly validated or sanitized.

And given that, it shouldn’t come as a surprise that the results of static analysis are very dependent on the development language. It’s rather common to find flaws with buffer/memory management in a language like C++, but those are nonexistent in languages like .NET or Java, where those functions are abstracted away from the developer. So even though CRLF injection is the top flaw type for static analysis overall, it’s not even in the top 10 flaws in C++ or PHP.

Figure 11 expands the list of static analysis flaws (the top graph in Figure 10) in two different ways. First, it breaks out the flaws by language, so the differences across languages become more apparent. (But note that the vertical axis differs for different languages.) Second, it adds the element of time. This enables us to see the trends and, again, if we pull back a bit and squint through the details, it’s clear that most everything is trending down over the past few years.

There are a few things worth calling out here that are not trending down, though.

*   JAVASCRIPT

    Has some growing challenges with identity management: Both credentials management and authentication issues are trending upward over time.
*   JAVA

    And the overall declines across Java are clearly more pronounced than the very subtle declines seen in PHP applications.

*Image description: A series of line graphs showing the proportion of applications with various static analysis findings by language (PHP, Python, Java, JavaScript, .NET, C++) over time, from 2017 to 2021. Note that the vertical axis scales differ between languages.*

Dynamic scanning takes advantage of, and is run against, the runtime environment.

*Image description: A line graph showing the proportion of applications with various dynamic analysis findings over time, from 2017 to 2021.*

Software composition analysis is the third type of scan, and it operates by tracking the various open-source projects and packages and then identifying which are included in the code base.

It doesn’t dive deeply into the idiosyncrasies of the underlying languages but instead can find more flaws in the execution and interface of the code. Notice the top types of flaws here generally don’t overlap with the static analysis findings. Server configurations and information leakage were consistently the leading categories of flaws found across all the underlying languages. The flaws were so consistent across languages that it’s not worth showing the differences. Each individual language looked like the overall trends shown in Figure 12.

This allows all the existing information in those libraries to be shared with the developers. The flaws in third-party software can be reported from a variety of sources such as static code scans, manual code review, security researchers reporting flaws, etc. Once again, we find that these types of flaws vary by language, as you can see in Figure 13 (but note that the vertical axis uses different scales for different languages). Some languages (Java, JavaScript, and Python) show clear declines while .NET and C++ don’t appear to show that type of decline in their third-party libraries.

*Image description: A series of line graphs showing the proportion of applications with various SCA findings by language (PHP, Python, Java, JavaScript, .NET, C++) over time, from 2017 to 2021. Note that the vertical axis scales differ between languages.*

## Fix Rate Comparisons by Scan Type
We’ve spent our time up until now looking at applications, detection methods, types of flaws and their prevalence, and how developers have changed their security practices over time. But what about actually fixing things? This is a good point to transition into thinking about how many flaws are getting fixed and how quickly (or not so quickly). Anyone who’s been reading our research for the last few years will surely recognize this next plot. It looks at the millions of flaws we’ve been tracking and shows estimates for how long any particular flaw will remain open. It factors in both the flaws that have been remediated and those that have yet to be fixed to give us a more accurate measurement of expected closure rates over time.

*Image description: A line graph showing the probability of a flaw remaining open over time for different scan types (Dynamic, SCA, Static). The graph also includes text overlays stating "HALF OF THE FLAWS from static analysis are closed within the first 290 days, while half of the flaws from dynamic analysis are closed in the first 143 days" and "77% of flaws in third-party libraries remain unfixed after the FIRST THREE MONTHS, while only 57% of flaws found through dynamic analysis are still around".*

This year’s research expands beyond just remediations for flaws found through static analysis (we focused on that in previous years) and looks at flaws discovered through dynamic analysis and SCA. Figure 14 shows that dynamic flaws get fixed the fastest and SCA flaws the slowest, with flaws from static analysis being fixed at a rate between those two.

Dynamic flaws get fixed the fastest and SCA flaws the slowest, with flaws from static analysis being fixed at a rate between those two.

Let’s focus on the horizontal dashed line at 50 percent shown in Figure 14. It represents how long it may take to close about half the flaws, or what we can call the “half-life” of a flaw.

*Image description: A line graph showing the half-life of flaws by scan type (Dynamic Analysis, Static Analysis, SCA) over time, from 2017 to 2021.*

It may seem absurd that it can be over a year before even half the flaws identified through SCA are closed — especially when we see flaws found through dynamic analysis lasting just under 5 months for the same half-life metric. But what if we told you that’s actually a great improvement? Take a look at Figure 15, which tracks that half-life metric over time. With that historical perspective, flaws found in SCA show a dramatic improvement. Back in 2017, it would take over three years to get to the 50 percent (half-life) closed point, and that’s been driven down to what we see today: just over a year.

Remediation efforts have slid back a bit for static scans. In 2017, half-life to remediation was just under 200 days, now remediation has slowed down to just under 300 days.

After looking at the SCA flaws and feeling optimistic that things are improving, take a look at the static scans. It looks like remediation efforts have slid back a bit from an all-time low around 2017 with a half-life of just under 200 days. Currently, remediation has slowed down to just under 300 days. Part of the challenge here is that the competitive market demands timely releases, and software development teams are forced to make difficult tradeoffs between a timely delivery and risk. Some flaws may be left unaddressed to meet deadlines.

If we want to track speed to remediation, half-life is a good metric, but there is a challenge in relying on it as a complete measure: It doesn’t account for all the flaws being fixed in a given time period. In order to measure just how many flaws are being fixed in a window of time, we must look at the overall capacity that development teams have for fixing flaws.

## Capacity for Flaw Remediation by Scan Type
To gauge capacity, we look at all the flaws facing a development team in a given month and then see how many of those are fixed in that month. Naturally, there are variations from application to application, but Figure 16 captures the overall trend over the last five years.

*Image description: A line graph showing the monthly capacity for flaw remediation by scan type (Dynamic Analysis, Static Analysis, SCA) over time, from 2017 to 2021.*

The points in Figure 16 represent individual applications, and the lines show the overall trend. Keep in mind that capacity here is looking at the number of remediated flaws out of the total number of open flaws in a given month. This gives us the percentage of flaws being fixed every month. It’s good to see the remediation of both static flaws and SCA flaws in any given month on the rise here even if the increase isn’t dramatic and (according to Figure 15) it takes a little longer. The remediation of flaws found with dynamic analysis has been bouncing around a bit, but we should see it stabilize as we get more data.

Overall, the signs here give us hope that there is a focus on application security and that added attention is having a positive impact on the security of our applications.

## Where Do We Go From Here?
As we wrap up this whirlwind tour of the evolution of software security over time, let’s take a look at the future and think about what practices might be next in improving application security.

## Most Organizations Using Veracode Security Labs Are Fixing Flaws Faster
Here at Veracode, we don’t want to simply point out, “Hey, there’s a flaw here, you should fix it” — we also want to help developers better understand how to fix those flaws and avoid creating new ones in the future. To that end, we’ve established Veracode Security Labs to give developers hands-on experience fixing common flaws.

*Image description: A histogram showing the time spent per lesson in Veracode Security Labs, with the x-axis representing the time and the y-axis representing the percentage of accounts.*

Before you roll your eyes, we want you to know this isn’t just a pile of training videos that developers are expected to slog through. Veracode Security Labs lessons are fully realized example applications, written in a variety of languages, with real flaws. The lessons help developers understand the flaws by giving them hands-on experience actually exploiting them. Using real code, developers are led through examples of specific coding flaws. They then develop and execute exploits to build their intuition about security flaws. And more importantly, developers write the patches that fix the flaws, giving them valuable experience when they are alerted to flaws in their own code.

This is starting to sound like a marketing pamphlet, but we promise it’s not. We want to know if this type of system can help developers fix flaws faster and help prevent the creation of flaws in the future. Most lessons are short, averaging less than an hour to complete.

But do these efforts actually make a difference in the ability to fix flaws?

*Image description: A line graph showing the probability of a flaw remaining open over time for organizations with and without Veracode Security Labs training. The graph also includes text overlays stating "2 month difference" and "110 days it takes to fix approximately 50% of flaws" and "170 days it takes to fix approximately 50% of flaws".*

We looked at organizations that had completed some number of lessons and compared the flaws that were found