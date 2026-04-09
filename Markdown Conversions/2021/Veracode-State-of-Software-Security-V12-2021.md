# State of Software Security V12: The Progress We’ve All Made

## Table of Contents
- [Executive Summary](#executive-summary)
- [Introduction](#introduction)
- [How Software Development Has Changed](#how-software-development-has-changed)
- [Software Bill of Mistakes](#software-bill-of-mistakes)
- [The Flaws of Yesterday Are (Still) the Flaws of Today](#the-flaws-of-yesterday-are-still-the-flaws-of-today)
- [Where Do We Go From Here?](#where-do-we-go-from-here)
- [Conclusions](#conclusions)
- [Appendix: Methodology](#appendix-methodology)

---

## Executive Summary

The world is becoming more connected than ever before. Connectivity makes our lives easier, but it also increases risk. One security flaw can have a domino effect, leaving software vulnerable all across the globe.

But it’s not just increased connectivity that’s shaping the security landscape — it’s the hypercompetitiveness and the need to constantly innovate. To move faster, many development teams have turned to native cloud technologies, microservices architectures, and open-source code to accelerate and scale their efforts. Additionally, development teams have adopted agile methodologies and are automating as many steps in the development process as possible.

While this evolution increases the speed of the software development lifecycle, it also introduces new complexities and risks.

For our 12th State of Software Security report, we’ll explore these trends with the help of the Cyentia Institute to assess how the software security landscape is continuing to evolve. Our goal is to help you make informed decisions about your software security program so that you can minimize your risk and meet cybersecurity regulations like those outlined in the White House Executive Order on Improving the Nation’s Cybersecurity issued on May 12, 2021.

---

## Introduction

In 2019, for our 10th annual State of Software Security report, we began looking at the specific concerns associated with the use of open-source software and have been fortunate to be able to map the complex landscape of secure software development. We’ve identified a few ideas that many of our customers probably feel in their hearts, and we confirm them with data — things like scanning at a regular, rapid pace is good.

Security debt can build over time, and addressing it early can help mitigate work down the road. Using multiple types of scanning — static, dynamic, and software composition analysis — can give a fuller picture of an application’s security, and it helps remediation happen more quickly and more completely.

These things can help every application, even those old creaky legacy applications, and it’s been rewarding to be able to verify and quantify the effect of what many developers feel makes applications more secure.

### So where does that leave us for this 12th report?

We feel like we’ve quantified some of the mysteries about application security with Veracode’s extensive data, and we could continue to do that. But we think it behooves an industry to occasionally take a step back to try to get a view of the past and take a look toward the future — to see where the landscape has been steady and where it’s changed and to try to understand which principles have stood the test of time and which have faltered.

So we’re going to do just that:

1. **Look at the use of software analysis tools**: We’ll start with a look at how people are using software analysis tools and how that’s changed over the years.
2. **Analyze flaws in software**: Then we’ll look at how those development trends manifest themselves in the flaws that get introduced into software.
3. **Examine how flaws are fixed**: Next, we’ll examine how things are fixed and whether developers are getting better at fixing things.
4. **Look to the future of secure software**: Lastly, we’ll take a peek into the future and think about what exactly developers can do to write more secure software.

---

## How Software Development Has Changed

One of the advantages of serving the software development community for so long is that Veracode is able to see changes in development practices over time. So rather than diving right into security this year, we want to focus on how developers themselves are approaching applications and how that’s changed.

### The Number of Applications Scanned Has Tripled

![Chart showing application creation over time]

Organizations are scanning, on average, more than 17 new applications per quarter. This number is more than triple the number of apps scanned per quarter a decade ago.

### The Rise of Microservices

What defines microservices? They are collections of loosely coupled applications, usually with a small codebase, that communicate via APIs. The advantage of microservices is that it’s easier to work on the various parts of an application if changing one part is unlikely to affect the other bits.

In 2018, roughly 20 percent of applications incorporated multiple languages. This year, less than 5 percent of apps used multiple languages, suggesting a pivot to smaller, one-language applications or microservices.

### Increase in Median Scan Cadence

Continuous testing and integration, which includes security scanning in pipelines, is becoming the norm. A decade ago applications were scanned two or three times a year. Now, 90 percent of applications are scanned more than once a week with the majority scanned three times a week.

---

## Software Bill of Mistakes

"In many respects, development teams have shifted from writing software to assembling software." — Chris Wysopal, CTO and Co-Founder, Veracode.

### Organizations Heavily Leverage Open-Source Libraries

Most applications have a kind of barbell effect, being composed of almost entirely third-party code or almost entirely in-house code. Java remains steadfastly mostly third-party code and has pushed even more so in that direction in the last few years.

### Most Developers Stick With the Same Libraries Year Over Year

We found that developers stick with tried-and-true libraries and rarely attempt to refactor their code base to pick up the "coolest" or "most-popular" libraries.

### Third-Party Libraries Have Fewer Flaws

On a positive note, there is a noticeable improvement in time to remediation for third-party flaws. Back in 2017, it would take over three years to get to the 50 percent (half-life) closed point, and now it takes just over a year.

---

## The Flaws of Yesterday Are (Still) the Flaws of Today

History is teaching us that we will experience the same types of flaws year after year. Sure, there are variations among languages and things may shift around in prevalence. But by and large, the technical flaws themselves don’t go away, and any changes we do observe tend to evolve slowly.

### The Lowdown on Static, Dynamic, and Software Composition Analysis

- **Static Analysis**: Looks directly at the source code. It’s very strong at detecting places where memory isn’t managed correctly or input isn’t properly validated.
- **Dynamic Analysis**: Run against the runtime environment. It finds flaws in the execution and interface of the code.
- **Software Composition Analysis (SCA)**: Operates by tracking the various open-source projects and packages and identifying which are included in the code base.

---

## Where Do We Go From Here?

### Most Organizations Using Veracode Security Labs Are Fixing Flaws Faster

We want to help developers better understand how to fix those flaws and avoid creating new ones in the future. To that end, we’ve established Veracode Security Labs to give developers hands-on experience fixing common flaws.

Organizations with Veracode Security Labs training decrease their time to fix 50 percent of flaws by 35 percent.

---

## Conclusions

Standing here in 2022, what can we say we’ve learned?

1. **Agile development of small, modular applications has eaten the world**: We’ve seen an explosion in the number of applications being scanned.
2. **Free and open-source code will continue to be a blessing and a curse for developers**: Developers appear to be using fewer libraries with known flaws, and that’s cause for optimism.
3. **Applications are, slowly but surely, getting more secure**: While some subsets of flaws have increased in prevalence over time, the trend has generally been downward.
4. **New tools will continue to help improve the application security landscape**: Having these types of tools built into continuous integration pipelines and IDEs will only speed developer adoption.

---

## Appendix: Methodology

Our methodology for data analysis diverged slightly from that used for earlier volumes of the State of Software Security. This year, we wanted to get a longer-term view, so the core data represents the full historical data from Veracode services and customers.

This accounts for a total of:
- 592,720 applications that used all scan types
- 1,034,855 dynamic analysis scans
- 5,137,882 static analysis scans
- 18,473,203 software composition analysis scans

### A Note on Mass Closures
While preparing the data for our analysis, we noticed several large single-day closure events. These "mass closure" events have significant effects on measuring flaw persistence and time to remediation and were ultimately excluded from the analysis.