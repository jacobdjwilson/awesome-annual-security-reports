# THE PROGRESS WE’VE ALL MADE
## Table of Contents
- [Executive Summary](#executive-summary)
- [The State of Software Security at a Glance](#the-state-of-software-security-at-a-glance)
- [Introduction](#introduction)
- [How Software Development Has Changed](#how-software-development-has-changed)
- [The Number of Applications Scanned Has Tripled](#the-number-of-applications-scanned-has-tripled)
- [The Rise of Microservices](#the-rise-of-microservices)
- [Increase in Median Scan Cadence](#increase-in-median-scan-cadence)
- [Organizations Are Using Multiple Types of Scanning](#organizations-are-using-multiple-types-of-scanning)
- [Software Bill of Mistakes](#software-bill-of-mistakes)
- [Organizations Heavily Leverage Open-Source Libraries](#organizations-heavily-leverage-open-source-libraries)
- [Most Developers Stick With the Same Libraries Year Over Year](#most-developers-stick-with-the-same-libraries-year-over-year)
- [Third-Party Libraries Have Fewer Flaws](#third-party-libraries-have-fewer-flaws)
- [The Flaws of Yesterday Are (Still) the Flaws of Today](#the-flaws-of-yesterday-are-still-the-flaws-of-today)
- [The Lowdown on Static, Dynamic, and Software Composition Analysis](#the-lowdown-on-static-dynamic-and-software-composition-analysis)
- [Fix Rate Comparisons by Scan Type](#fix-rate-comparisons-by-scan-type)
- [Capacity for Flaw Remediation by Scan Type](#capacity-for-flaw-remediation-by-scan-type)
- [Where Do We Go From Here?](#where-do-we-go-from-here)
- [Most Organizations Using Veracode Security Labs Are Fixing Flaws Faster](#most-organizations-using-veracode-security-labs-are-fixing-flaws-faster)
- [Conclusions](#conclusions)
- [Appendix: Methodology](#appendix-methodology)
- [A Note on Mass Closures](#a-note-on-mass-closures)

THE PROGRESS WE’VE ALL MADE
B
State of    
Software   
Security
The Progress We’ve All Made
V O L U M E  1 2
VERACODE STATE OF SOFTWARE SECURITY REPORT 
C
THE PROGRESS WE’VE ALL MADE
01
02	
Executive Summary 
03	
The State of Software Security at a Glance
06	
Introduction
08	
How Software Development Has Changed
09	
The Number of Applications Scanned Has Tripled
11	
The Rise of Microservices
14	
Increase in Median Scan Cadence
16	
Organizations Are Using Multiple Types of Scanning
17	
Software Bill of Mistakes
18	
Organizations Heavily Leverage Open-Source Libraries
20	
Most Developers Stick With the Same Libraries Year Over Year
22	
Third-Party Libraries Have Fewer Flaws
24	
The Flaws of Yesterday Are (Still) the Flaws of Today
26	

The Lowdown on Static, Dynamic, and Software Composition Analysis
32	
Fix Rate Comparisons by Scan Type
34	
Capacity for Flaw Remediation by Scan Type
35	
Where Do We Go From Here?
36	

Most Organizations Using Veracode Security Labs  
Are Fixing Flaws Faster
40	
Conclusions
43	
Appendix: Methodology 
44	
A Note on Mass Closures
Contents
SECTION 01
SECTION 02
SECTION 03
SECTION 04
SECTION 05
SECTION 06
SECTION 07
VERACODE STATE OF SOFTWARE SECURITY REPORT 
02
## Executive Summary
VERACODE STATE OF SOFTWARE SECURITY REPORT 
02
01
SECTION
The world is becoming more connected 
than ever before … Connectivity makes 
our lives easier, but it also increases risk. 
One security flaw can have a domino 
effect, leaving software vulnerable all 
across the globe. 
But it’s not just increased connectivity 
that’s shaping the security landscape — 
it’s the hypercompetitiveness and the 
need to constantly innovate. To move 
faster, many development teams have 
turned to native cloud technologies, 
microservices architectures, and open- 
source code to accelerate and scale their 
efforts. Additionally, development teams 
have adopted agile methodologies and 
are automating as many steps in the 
development process as possible. 
While this evolution increases the speed 
of the software development lifecycle,  
it also introduces new complexities  
and risks. 
For our 12th State of Software Security 
report, we’ll explore these trends with 
the help of the Cyentia Institute to assess 
how the software security landscape is 
continuing to evolve. Our goal is to help 
you make informed decisions about your 
software security program so that you can 
minimize your risk and meet cybersecurity 
regulations like those outlined in 
the White House Executive Order on 
Improving the Nation’s Cybersecurity 
issued on May 12, 2021.
THE PROGRESS WE’VE ALL MADE
03
Similar to last year, we looked at the entire history of active 
applications, not just the activity associated with the application over 
one year. By doing so, we can view the full life cycle of applications, 
which results in more accurate metrics and observations. Aside from 
looking at the past, we also imagined the future by considering 
practices — such as Veracode Security Labs training — that might  
help improve application security.
## The State  
of Software  
Security at  
a Glance 
THE PROGRESS WE’VE ALL MADE
03
Microservices 
In 2018, roughly 20 percent 
of applications incorporated 
multiple languages. This year, 
less than 5 percent of apps used 
multiple languages, suggesting 
a pivot to smaller, one-language 
applications or microservices.
20%
5%
2018
2021
JavaScript, Python, and .NET have 
seen declines in app sizes, indicating 
a trend toward more microservices.
The Number of Apps 
Scanned Has Tripled 
Organizations are scanning,  
on average, more than 17 new 
applications per quarter. This 
number is more than triple the 
number of apps scanned per 
quarter a decade ago. 
2021
2011
3X
INCREASE IN NUMBER  
OF APPS SCANNED
VERACODE STATE OF SOFTWARE SECURITY REPORT 
04
Scan Cadence 
Continuous testing and integration, which includes security scanning in 
pipelines, is becoming the norm. A decade ago applications were scanned  
two or three times a year. Now, 90 percent of applications are scanned more 
than once a week with the majority scanned three times a week. 
VERACODE STATE OF SOFTWARE SECURITY REPORT 
04
Flaw Prevalence
Third-party libraries  
have fewer flaws. 
of libraries used  
had a known flaw 
of libraries used 
had a known flaw 
35%
10%
2017
2021
INCREASE in the use 
of multiple scan types
Multiple Scan Types
We’ve seen a 31 percent increase in the use of multiple scan types 
between 2018 and 2021, with much of that gain coming from organizations 
using the full suite of static, dynamic, and SCA scans.
2021
2010
20X
INCREASE IN MEDIAN SCAN 
CADENCE FROM 2010 TO 2021
31%
THE PROGRESS WE’VE ALL MADE
05
Third-Party 
Libraries
THE PROGRESS WE’VE ALL MADE
05
On a positive note, there is a noticeable improvement in time 
to remediation for third-party flaws. Back in 2017, it would  
take over three years to get to the 50 percent (half-life)  
closed point, and now it takes just over a year.
77%
of flaws in third-party libraries 
remain unfixed after three months
3 years
1 year
2017
2021
S E C T I O N  0 1
DECREASE in the time it takes 
for organizations to fix flaws
Open Source
Open-source libraries are still 
a significant cause for concern. 
97%
of Java applications 
are made up of open 
source libraries
Veracode Security Labs
On average, organizations with Veracode Security Labs training 
decrease their time to fix 50 percent of flaws by 35 percent.
35%
VERACODE STATE OF SOFTWARE SECURITY REPORT 
06
VERACODE STATE OF SOFTWARE SECURITY REPORT 
06
02
SECTION
In 2019, for our 10th annual State of 
Software Security report, we began 
looking at the specific concerns 
associated with the use of open-source 
software and have been fortunate to  
be able to map the complex landscape 
of secure software development.  
We’ve identified a few ideas that many  
of our customers probably feel in their 
hearts, and we confirm them with data 
— things like scanning at a regular, rapid 
pace is good. 
Security debt can build over time, and 
addressing it early can help mitigate work 
down the road. Using multiple types of 
scanning — static, dynamic, and software 
composition analysis — can give a fuller 
picture of an application’s security, and it 
helps remediation happen more quickly  
and more completely. 
These things can help every application, even 
those old creaky legacy applications, and 
it’s been rewarding to be able to verify and 
quantify the effect of what many developers 
feel makes applications more secure.
## Introduction
THE PROGRESS WE’VE ALL MADE
07
So where does 
that leave us for 
this 12th report? 
We feel like we’ve quantified some of the mysteries about application security 
with Veracode’s extensive data, and we could continue to do that. But we 
think it behooves an industry to occasionally take a step back to try to get 
a view of the past and take a look toward the future — to see where the 
landscape has been steady and where it’s changed and to try to understand 
which principles have stood the test of time and which have faltered. 
So we’re going to do just that:
1  	 Look at the use of software analysis tools
	

We’ll start with a look at how people are using software analysis tools 
and how that’s changed over the years. We’ll see development trends 
reflected in those scans. We’ll look at how free and open-source software 
continues to be integral (though variably so) to most applications. 
2    
Analyze flaws in software
	

Then we’ll look at how those development trends manifest themselves  
in the flaws that get introduced into software. 
3    
Examine how flaws are fixed
	

Next, we’ll examine how things are fixed and whether developers  
are getting better at fixing things. 
4    
Look to the future of secure software
	

Lastly, we’ll take a peek into the future and think about what exactly 
developers can do to write more secure software. In particular, we’ll  
see that the simple act of taking time to learn how to fix flaws helps  
get them fixed faster and helps prevent future bugs from showing up. 
Let’s take a quick trip down memory lane …
VERACODE STATE OF SOFTWARE SECURITY REPORT 
08
## How Software  
Development  
Has Changed
One of the advantages of serving the software 
development community for so long is that Veracode is 
able to see changes in development practices over time. 
So rather than diving right into security this year, we want 
to focus on how developers themselves are approaching 
applications and how that’s changed. 
VERACODE STATE OF SOFTWARE SECURITY REPORT 
08
03
SECTION
THE PROGRESS WE’VE ALL MADE
09
## The Number  
of Applications 
Scanned Has 
Tripled
First, we want to examine just how many applications developers are 
scanning for flaws. Figure 1 shows that more applications are being  
scanned than ever before. And the increase is not simply due to the fact 
that there are more organizations. In the last year, most organizations are 
creating, on average, more than 17 applications for scanning per quarter, up 
from approximately five a decade ago. But why might this be the case? 
We have two hypotheses: 
1    
Organizations are creating smaller, more modular,  
applications that do a single thing.
2    
Organizations are expanding the scope of their security  
to lower-criticality applications.
Organizations are scanning, on average, more than 17 new 
applications per quarter. This number is more than triple 
the number of apps scanned per quarter a decade ago.  
![Figure 1: Application creation over time](Figure 1: Application creation over time)
Scanning 
Average
0
5
10
15
20
2007
2008
2009
2010
2011
2012
2013
2014
2015
2016
2017
2018
2019
2020
2021
2022
WEEK APPLICATION FIRST SCANNED
NEW APPLICATIONS PER ACCOUNT
NUMBER OF ACCOUNTS
10
200
500
VERACODE STATE OF SOFTWARE SECURITY REPORT 
10
Very Low
Low
Medium
High
Very High
0%
25%
50%
75%
100%
SCAN DATE
PERCENT OF APPLICATIONS BY CRITICALITY
2010
2011
2012
2013
2014
2015
2016
2017
2018
2019
2020
2021
![Figure 2: Application criticality over time](Figure 2: Application criticality over time)
We actually see that the latter is not true in Figure 2. The distribution of app 
criticality has been fairly constant, with some bumps along the way when new or 
existing users onboard many applications (as was the case in mid-2020 when a single 
user scanned a few hundred “Medium” criticality applications). The skew has been 
pretty consistent over the last 10 years, with most applications having “High”  
or “Very High” criticality, and only a handful registering “Low” or “Very Low.” 
If developers are not simply scanning applications they considered unimportant 
before, perhaps there is a profusion of new applications — smaller, more modular 
ones. Some might call them “microservices.”
THE PROGRESS WE’VE ALL MADE
11
## The Rise of 
Microservices
0%
10%
20%
30%
0
25
50
75
100
WEEK APPLICATION FIRST SCANNED
PERCENT OF MULTI-LANGUAGE APPLICATIONS
INTEREST
2009
2010
2011
2012
2013
2014
2015
2016
2017
2018
2019
2020
2021
2022
NUMBER OF APPLICATIONS
1
10
100
Google search interest 
in “microservices”
Google search interest 
in “microservices”
![Figure 3: Use of multiple languages in new applications](Figure 3: Use of multiple languages in new applications)
Up until roughly 2018, there was a slow but steady increase in the number 
of applications using multiple languages, up to a peak (excluding outliers) 
of about 20 percent of apps incorporating multiple languages. But as the 
notion of microservices gained favor and took over, there was a nosedive, 
with less than 5 percent of applications currently using multiple languages.
So we see that developers are using one language at a time, but are their 
applications getting smaller? Figure 4a says it’s complicated.
What defines microservices? They are collections of loosely coupled 
applications, usually with a small codebase, that communicate via APIs.  
The advantage of microservices is that it’s easier to work on the various parts  
of an application if changing one part is unlikely to affect the other bits. 
So how might we see this reflected among Veracode users? Well, we’d expect 
applications to increasingly use one language and become smaller in size. 
Figure 3 looks at the first part of that hypothesis.
In 2018, roughly  
20 percent of applications 
incorporated multiple 
languages. This year,  
less than 5 percent of apps 
used multiple languages.
Are developers pivoting 
to microservices?
S E C T I O N  0 3
VERACODE STATE OF SOFTWARE SECURITY REPORT 
12
VERACODE STATE OF SOFTWARE SECURITY REPORT 
12
![Figure 4a: Application size over time](Figure 4a: Application size over time)
Java
0.01
1
100
C++
0.1
10
1k
2009 2011
2013
2015
2017
2019
2021
PHP
0.001
0.1
10
2011
2013
2015
2017
2019
2021
JavaScript
0.01
1
100
2015
2017
2019
2021
Python
1
0.01
100
2017
2019
2021
DATE OF FIRST STATIC SCAN
MEAN SIZE (MB)
2009 2011
2013
2015
2017
2019
2021
.NET
0.01
0.1
1
10
100
2009 2011
2013
2015
2017
2019
2021
THE PROGRESS WE’VE ALL MADE
13
0.01
0.1
1
10
DATE OF FIRST STATIC SCAN
SCAN SIZE (MB)
Android
2012
2014
2016
2018
2020
2022
![Figure 4b: Android’s abrupt size shift](Figure 4b: Android’s abrupt size shift)
  JAVASCRIPT 
JavaScript applications have gotten 
considerably smaller over time, possibly 
with the inclusion of a more diverse and 
robust library ecosystem. 
  PYTHON AND .NET 
Both Python and .NET have seen 
reductions in size, but that may be more 
regression to the mean than a true trend. 
  C++ AND JAVA 
Meanwhile, applications written in more 
established languages like C++ and Java 
have remained more or less the same 
size over the past few years. 
SCALA 
Scala applications (not shown) have seen 
a decline in size, and the popularity of 
Scala compared to its more heavyweight 
godfather Java may have something to do 
with different architectural goals. 
GO
Interestingly, Go (not shown), a language 
commonly associated with microservices, 
has actually seen an increase in 
application size.
  ANDROID 
A quick aside on Android applications: Android 
applications were getting increasingly large until the 
release of Android N, which switched to an OpenJDK.  
This allowed for significantly smaller application sizes 
and was followed by another slow and steady increase. 
We don’t think this is a trend, but it’s nice to see major 
events in software ecosystems validated in data.
Applications written in a few languages we might 
consider “good” for a microservice-type architecture 
certainly have declined in size. 
THE PROGRESS WE’VE ALL MADE
13
S E C T I O N  0 3
VERACODE STATE OF SOFTWARE SECURITY REPORT 
14
## Increase in 
Median Scan  
Cadence
“It is no longer sufficient to scan software as a pre-production 
step in the last phase of the software development lifecycle. 
Just as software is now deployed continuously, software 
security scanning must also happen continuously as a fully 
integrated part of the software development process.”
SAM KING, CEO, VERACODE 
It’s been said that “software is eating the world.” We think it’s  
probably also fair to say that “agile is eating the software world.” 
Continuous testing and integration, which includes security scanning into 
pipelines, is becoming the norm, and we can see that reflected in how often 
users are scanning their applications. A decade ago users were averaging  
two or three scans a year. Now, most are running daily static scans and 
weekly dynamic scans. Software composition analysis (SCA) scans also occur 
at least weekly. The sooner in the lifecycle you can discover problems, the 
more likely you’ll be able to solve them quickly, before they become bigger  
a problem down the road.
THE PROGRESS WE’VE ALL MADE
15
DATE OF FIRST SCAN
MEAN TIME BETWEEN SCANS (DAYS)
0
1
10
100
1k
Manual
2010
2015
2020
Dynamic
2010
2015
2020
Static
2010
2015
2020
SCA Agent
2018
2020
2022
![Figure 5: Scanning cadence over time](Figure 5: Scanning cadence over time)
S E C T I O N  0 3
But is scanning more good? 
If you look back at SOSS volumes 9, 10, and 11, you’ll see that applications 
that are scanned at a regular cadence fix more flaws faster than those that 
are only scanned periodically. Security seems to prefer agile development.
Median Scan Cadence
2010
Median application was scanned less 
than once a month (only 10 percent of 
apps scanned more often than weekly) 
2021
90 percent of apps scanned 
more than once a week (majority 
scanned three times a week)
20X
increase
VERACODE STATE OF SOFTWARE SECURITY REPORT 
16
## Organizations 
Are Using  
Multiple Types 
of Scanning
Part of the advantage of the continuous integration paradigm is the  
ability to easily add new components to the pipeline. Static testing?  
A must. The use of dynamic analysis is growing as well, and since  
we’re becoming more and more aware of the potential risks inherent  
in open-source software, it’s a no-brainer that secure development 
includes software composition analysis.
We’ve seen a 31 percent increase in the use of multiple scan types 
between 2018 and 2021, with much of that gain coming from organizations 
using the full suite of static, dynamic, and SCA scans. We’re not just 
pointing this out as a random fact. 
Organizations that used dynamic  
in addition to static scanning  
were able to remediate
50% of flaws
On average
24 days faster
And including SCA shaves off
another 6 days
LAST YEAR WE FOUND:
So fire up those 
scanners, folks!
THE PROGRESS WE’VE ALL MADE
17
## Software Bill  
of Mistakes
“In many respects, development 
teams have shifted from writing 
software to assembling software.”
CHRIS WYSOPAL, CTO AND CO-FOUNDER, VERACODE 
SECTION
04
THE PROGRESS WE’VE ALL MADE
17
VERACODE STATE OF SOFTWARE SECURITY REPORT 
18
## Organizations  
Heavily Leverage 
Open-Source  
Libraries
  
JAVA  
Java remains steadfastly mostly third-party code and has pushed  
even more so in that direction in the last few years.
  
.NET  
There is an interesting “shock” to the data for .NET: In mid-2020, we saw  
an abrupt shift in the percentage of third-party code in .NET applications. 
The relative time period coincides with the release of .NET 5 (formerly  
.NET core), which integrated and unified a good amount of functionality  
into a single framework. It’s good to see developers keep up with the  
latest updates.
  
JAVASCRIPT AND PYTHON  
JavaScript and Python show the barbell effect, with applications being  
either mostly homegrown or mostly third-party libraries, causing the  
trend line to bounce around the middle over time.
  
PHP AND C++  
PHP and C++ remain relatively constant, leaning heavily toward  
mostly homegrown code.
How has open-source, and, more generally, third-party software 
changed over the last few years? 
Last year’s report looked at the proportion of code included in each scan 
that was third-party code versus homegrown. What we saw was interesting. 
Most applications (depending on the language) had a kind of barbell effect, 
being composed of almost entirely third-party code or almost entirely  
in-house code. 
There were of course some exceptions. Java’s OOP design philosophy  
of gluing classes together until your code begins to look like a functioning 
application makes code reuse a breeze. And why write your own classes 
when there are perfectly good third-party ones freely available? The result 
is that most of the code in Java applications comes from third parties. But 
have those barbells evolved over time? Let’s take a look at Figure 6.
THE PROGRESS WE’VE ALL MADE
19
0%
50%
100%
0%
50%
100%
0%
50%
100%
PROPORTION OF THIRD-PARTY CODE
.NET
Python
C++
JavaScript
2019
2020
2021
Java
2019
2020
2021
PHP
![Figure 6: Third-party code by language](Figure 6: Third-party code by language)
S E C T I O N  0 4
VERACODE STATE OF SOFTWARE SECURITY REPORT 
20
## Most Developers Stick With the 
Same Libraries Year Over Year
We are seeing some evolution in terms of how much third-party code 
developers are using in each language. 
Last year’s open source report looked at shifts in the use of vulnerable 
libraries between 2019 and 2020. Since we’re focusing on how things have 
evolved over as long a time period as the data can muster, we want to expand 
that view a little bit here. Figure 7 takes a look at how the top 10 most popular 
libraries across our six languages of interest have evolved over time.
1
Figure 7 is what is referred to as a stacked area chart. Each band represents 
the percentage of scanned repositories that are using a particular library.  
The thicker the band, the more popular the library. When the overall height  
of the chart increases, it indicates that those 10 libraries are all growing  
in popularity. If libraries waxed and waned in popularity frequently, we  
would expect to see large swells of color that might peter out over time.  
We don’t see that in Figure 7, but rather mostly uniform popularity of  
those top libraries.
We won’t spend a ton of time going over each wiggle. But what we do see  
is that, for all the languages, the most popular libraries haven’t changed 
all that much. Things like debug and inherits continue to be popular for 
JavaScript though they may swap around the top few spots year over year.  
The larger lesson here is that developers are going to stick with tried-and-
true libraries and likely aren’t going to attempt to refactor their code base  
to pick up the latest hot commodity. 
This is indeed what we saw in last year’s SOSS: Open Source Edition. Updates 
happened slowly when libraries didn’t have flaws, but relatively quickly when 
they did. As long as open-source developers continue to fix security flaws, 
developers will keep on using those libraries.
2 
A few notes on this figure. We are swapping Ruby in here for C/C++ as most C/C++ applications don’t use an explicit package manager and 
instead use makefiles to see if appropriate libraries are present. This can make extracting what applications are using what libraries pretty 
tough. We only have data going back to 2019 on .NET, so be sure to check the scales. Finally, the colors in this figure are used to differentiate 
the individual libraries, but are reused for purely aesthetic reasons.
Keep on keeping on … 
We found that  
developers stick with 
tried-and-true libraries 
and rarely attempt to 
refactor their code  
base to pick up the 
“coolest” or “most-
popular” libraries. 
THE PROGRESS WE’VE ALL MADE
21
Apache Commons Codec
Guava
Jackson-annotations
Jackson-core
jackson-databind
org.springframework:spring-context
SLF4J API Module
Spring AOP
Spring Beans
Spring Core
Java
RELATIVE POPULARITY
Diagnostics.Debug
Globalization
IO
Newtonsoft.Json
Reﬂection
Resources.ResourceManager
Runtime
Runtime.Extensions
Text.Encoding
Threading.Tasks
.NET
2020
2021
2018
2019
2020
2021
certiﬁ
chardet
idna
python-dateutil
pytz
PyYAML
requests
setuptools
six
urllib3
Python
2018
2019
2020
2021
dif-lcs
json
rake
rspec
rspec-core
rspec-expectations
rspec-mocks
rspec-support
Ruby
thor
tzinfo
2018
2019
2020
2021
doctrine/instantiator
php-ﬁle-iterator
php-text-template
psr/log
sebastian/dif
sebastian/environment
sebastian/exporter
sebastian/global-state
sebastian/recursion-context
sebastian/version
PHP
2018
2019
2020
2021
balanced-match
brace-expansion
debug
escape-string-regexp
glob
inherits
minimatch
minimist
ms
supports-color
JavaScript
2018
2019
2020
2021
![Figure 7: Popular libraries by language](Figure 7: Popular libraries by language)
S E C T I O N  0 4
VERACODE STATE OF SOFTWARE SECURITY REPORT 
22
## Third-Party 
Libraries Have 
Fewer Flaws
We’ve seen library usage evolve over time, though maybe not in a  
nice smooth trend. But what implications does that have for security?  
After all, that’s really what we’re here to talk about, right? Making 
applications more secure. Even the federal government is taking notice  
of this whole “third-party libraries might be risky, actually” idea. 
The recent Executive Order on Improving the Nation’s Cybersecurity lays out  
the following about securing the software supply chain:
“The development of commercial software often lacks transparency, sufficient 
focus on the ability of the software to resist attack, and adequate controls to 
prevent tampering by malicious actors. There is a pressing need to implement 
more rigorous and predictable mechanisms for ensuring that products function 
securely, and as intended. The security and integrity of ‘critical software’ — 
software that performs functions critical to trust (such as affording or requiring 
elevated system privileges or direct access to networking and computing 
resources) — is a particular concern. Accordingly, the Federal Government must 
take action to rapidly improve the security and integrity of the software supply 
chain, with a priority on addressing critical software.”
So are applications using more or fewer flawed libraries? As with many things in 
our research, Figure 8 tells a language-specific story. (But before you dive into 
Figure 8, notice that the vertical axes are different for different languages.)
There are clear trends for Java, JavaScript, and Python, and that trend is very 
good, because it goes steeply down. In 2017 nearly 35 percent (on average)  
of libraries used had a known flaw. In more recent years that has come down  
to nearly 10 percent. JavaScript has gone from about 10 percent to less than  
4 percent, Python from about 25 percent to nearly 10 percent, and Go (not 
shown) from 7 percent down to 4 percent. 
THE PROGRESS WE’VE ALL MADE
23
.NET
Java
0%
25%
50%
75%
0%
5%
10%
15%
20%
PERCENT OF VULNERABLE LIBRARIES
2020
2021
2017
2018
2019
2020
2021
PHP
0%
5%
10%
15%
20%
2020
2021
Python
0%
20%
40%
60%
2018
2019
2020
2021
JavaScript
0%
10%
20%
30%
40%
50%
2018
2019
2020
2021
Ruby
0%
20%
40%
2018
2019
2020
2021
![Figure 8: Percent of flawed libraries by language](Figure 8: Percent of flawed libraries by language)
S E C T I O N  0 4
VERACODE STATE OF SOFTWARE SECURITY REPORT 
24
## The Flaws of  
Yesterday Are 
(Still) the Flaws 
of Today
This type of report would be 
relatively easy to create if all — or 
heck, even some — of the attacks 
were fresh and new. The stories 
would almost write themselves. 
But history is teaching us that we 
will experience the same types of 
flaws year after year. Sure, there 
are variations among languages 
and things may shift around in 
prevalence. But by and large, the 
technical flaws themselves don’t 
go away, and any changes we do 
observe tend to evolve slowly. 
VERACODE STATE OF SOFTWARE SECURITY REPORT 
24
05
SECTION
THE PROGRESS WE’VE ALL MADE
25
Take as an example Figure 9 (or really any of the upcoming plots). We pulled 
out the flaws listed in the OWASP Top 10 and CWE/SANS Top 25 and those 
classified as “High” criticality or above. If you look closely at each of those 
over time, you’ll notice some peaks and valleys.