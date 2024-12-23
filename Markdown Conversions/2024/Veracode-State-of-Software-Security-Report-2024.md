# Addressing the Threat of Security Debt
## Table of Contents
- [Letter from the Editor](#letter-from-the-editor)
- [Key Findings](#key-findings)
- [State of Software Security at a Glance](#state-of-software-security-at-a-glance)
- [How common are security flaws?](#how-common-are-security-flaws)
- [Are flaws becoming less common?](#are-flaws-becoming-less-common)
- [How many flaws do applications have?](#how-many-flaws-do-applications-have)
- [How critical are software security flaws?](#how-critical-are-software-security-flaws)
- [What types of flaws are most common?](#what-types-of-flaws-are-most-common)
- [Where are flaws most likely to be introduced?](#where-are-flaws-most-likely-to-be-introduced)
- [How quickly are flaws remediated?](#how-quickly-are-flaws-remediated)
- [How common is software security debt?](#how-common-is-software-security-debt)
- [How common is software security debt? (Revisited)](#how-common-is-software-security-debt-revisited)
- [Measuring and Managing Security Debt](#measuring-and-managing-security-debt)
- [The prevalence of security debt](#the-prevalence-of-security-debt)
- [Factors that contribute to security debt](#factors-that-contribute-to-security-debt)
- [Recommendations to minimize security debt](#recommendations-to-minimize-security-debt)
- [Securing the Software Supply Chain](#securing-the-software-supply-chain)
- [Understanding open-source dependencies](#understanding-open-source-dependencies)
- [Assessing the security of third-party libraries](#assessing-the-security-of-third-party-libraries)
- [Addressing security debt in the software supply chain](#addressing-security-debt-in-the-software-supply-chain)
- [What’s it all mean?](#whats-it-all-mean)
- [Reviewing What We’ve Learned](#reviewing-what-weve-learned)
- [Methodology](#methodology)
- [A Note on Mass Closures](#a-note-on-mass-closures)

State of 
Software 
Security
2024
Veracode State of Software Security 2024
02
Veracode State of Software Security 2024
02
## Letter from the Editor
Artificial Intelligence (AI) wasn’t born last year, but 2023 was its coming-of-age party. The proliferation of  
AI-generated code brings with it insecure code at scale and the likelihood of it becoming security debt. 
Research indicates that code developed by AI contains about the same percentage of security flaws as that generated 
by humans. Other research suggests that programmers with a variety of experience levels fail to identify incorrect 
ChatGPT answers more than a third of the time. 
While AI allows more code to be written more quickly, it does not deliver more secure code. The result is more risk 
introduced into your code base in the same amount of time. 
The regulatory landscape has also evolved in the past year, with the US White House Executive Order on the Safe, 
Secure, and Trustworthy Development and Use of Artificial Intelligence, the European Union’s Cyber Resilience Act, 
and the US Security and Exchange Commission’s Rules on Cybersecurity Risk Management, Strategy, Governance, and 
Incident Disclosure by Public Companies all coming into effect. 
It’s within this context that we explored Veracode’s 18 years of data to answer questions about the accumulation of 
risk associated with insecure code. It’s not news that applications contain security flaws, but we are excited to share 
insights on where, how, and why flaws persist over time. 
In this year’s report, our 14th, we do a deep dive into the distribution of security debt within applications, across 
industries and languages. We also continue the conversation that we began in last year’s report regarding risks 
associated with how developers choose open-source libraries for their apps, with some surprising results. 
Given the extent of security debt that we found, it is worth considering whether AI-assisted remediation tools may be 
helpful to pay down that debt, without the need to redirect your development teams or to increase their size. 
As always, we hope you enjoy the journey as much as we enjoy the discovery, analysis, and writing, and that you’ll find 
in this year’s report inspiration that improves the state of your software security and reduces risk to your organization. 
The State of Software Security 2024
Addressing the Threat of Security Debt
Chris Eng
Chief Research Officer
Veracode State of Software Security 2024
03
02	
Letter from the Editor
04	
Key Findings
07	
State of Software Security at a Glance
08	
How common are security flaws?
09	
Are flaws becoming less common?
10	
How many flaws do applications have?
10	
How critical are software security flaws?
11	
What types of flaws are most common?
12	
Where are flaws most likely to be introduced?
12	
How quickly are flaws remediated?
13	
How common is software security debt?
14	
How common is software security debt? (Revisited)
15	
Measuring and Managing Security Debt
16	
The prevalence of security debt
19	
Factors that contribute to security debt
24	
Recommendations to minimize security debt
32	
Securing the Software Supply Chain
33	
Understanding open-source dependencies 
35	
Assessing the security of third-party libraries
38	
Addressing security debt in the software supply chain
40	
What’s it all mean?
41	
Reviewing What We’ve Learned
43	
Methodology
44	
A Note on Mass Closures
Veracode State of Software Security 2024
04
## Key Findings
Veracode State of Software Security 2024
05
Veracode State of Software Security 2024
05
1. Good news up front: The prevalence of 
high-severity security flaws in applications 
has dropped to half of what it was back  
in 2016. 
2. Roughly 63% of applications have flaws in 
first-party code and 70% contain flaws in 
third-party code. That’s why testing both 
throughout the SDLC is so critical. 
3. Third-party flaws take 50% longer to fix, 
with a half-life of 11 months vs. 7 months 
for flaws in first-party code. 
4. Flaws that stick around longer than a year become security debt. That occurs in 42% of applications 
and 71% of all organizations. 
5. More concerning still, almost half (46%) of 
organizations have persistent, high-severity 
flaws that constitute critical security debt. 

*For the purposes of this report, we are defining security debt to mean all flaws that remain unremediated for over one year
Veracode State of Software Security 2024
06
Veracode State of Software Security 2024
06
![Chart showing average monthly capacity of applications to eliminate security debt]
6. The prevalence of critical security debt 
across applications developed in large tech 
firms is 7x that of small firms in the retail 
and hospitality sector. 
7. Continuous scanning must be 
accompanied by continuous remediation 
to be effective. Development teams that 
fix flaws the fastest are 4x less likely to 
let critical security debt materialize in 
their applications. 
8. Almost 90% of all security debt across 
all active applications exists in first-party 
code. But third-party code claims  
two-thirds of security debt rated as  
critical severity. 
9. Only 64% of applications demonstrate a 
sustained capacity to eliminate all critical 
security debt. Prioritizing flaws for 
remediation is essential! 
10. Developer education matters! Among 
organizations that use Security Labs, 37% 
have security debt. Compare that to 48% 
among application teams that do not. 
The time-to-fix difference is even more 
significant. Applications developed by 
teams that aren’t using the Labs take seven 
months longer to reach that 37% mark.
11. All languages have multiple open-source 
developers that contribute code that is 
included in 90% of applications. These 
represent potential weak links in the 
software supply chain. 
Veracode State of Software Security 2024
07
We’re thrilled to embark on another 
chapter in our ongoing quest to share 
data-driven insights on the current 
state of software security.
You’d think after nearly a decade 
and a half of doing this, we’d 
be scraping the bottom of the 
barrel in terms of learning 
new lessons and new ways 
to apply them. But the 
reality is there’s so much 
to discover here that 
we must consciously 
restrain ourselves from 
filling 100+ pages with 
all the interesting and 
useful findings we 
uncover each year. 
And this year’s no 
different.
## State of
Software
Security
at a Glance
Thank you for joining us on this 
journey of discovery. We’ll start with a 
brief look at the lay of the land and then venture 
outward into the wilds of AppSec from there.
Veracode State of Software Security 2024
08
## How common are security flaws?
Security flaws aren’t ubiquitous, but they’re far from rare. Based on the most recent SAST, DAST, and SCA scans using Veracode, 
unresolved flaws were detected in 80% of all active applications. If you’re a longtime SOSS reader, the SAST-only version of the chart 
offers backward comparability and pegs flaw prevalence at 73% of all applications.
About 70% of applications have flaws included in the OWASP Top 10, an initiative to track the most critical risk to web applications. 
For the Common Weakness Enumeration (CWE) Top 25—another effort to track the most common and impactful security 
weakness—that statistic drops slightly to 41% of all applications. According to Veracode’s rating, half of applications have flaws 
considered high (or very high) severity (though that drops to 19%, as seen through SAST scans alone).
When parsing these stats (and all those that follow), bear in mind that this report represents organizations that are proactively 
integrating tools like Veracode into their AppSec programs. Organizations without scanning integrated into their development 
processes will likely have a higher prevalence of security flaws than shown here.
![Chart showing percent of applications with security flaws detected in most recent scan]
The big difference here that we’ll unpack throughout this report is that there are some major 
differences between first-party and third-party (largely open-source) code. SAST scans focus 
on the former, where developers are in full control and can prioritize severe flaws for faster 
remediation. Third-party libraries scanned via SCA, on the other hand, depend on other 
people to fix them before updates can be made.
> Why is the ratio of 
severe flaws lower 
in SAST?
Veracode State of Software Security 2024
09
## Are flaws becoming less common?
The prior chart showed a snapshot of applications as of their latest scan, but those stats don’t tell us whether flaws are becoming 
more or less common over time. Obviously, we’d like to see that trending down, which would indicate the overall state of software 
security is improving.
In general, the results do show a steady downward trend over the last eight years. We’re particularly encouraged to see that the 
prevalence of high-severity flaws has dropped to half of what it was back in 2016.
Some will wonder about the uptick among OWASP Top 10 flaws at the end of 2021. This traces back to some changes to the Top 10 
that year, resulting in the added flaws being detected in a larger number of applications.
Keep in mind that this chart aggregates new and old, large and small applications across many different languages and types of 
organizations. The fact that there’s a consensus trend in the direction we want to see is quite remarkable and points to the positive 
effects of sustained investments to improve AppSec.
![Chart showing trend of flaw detection rates over time]
Veracode State of Software Security 2024
10
## How many flaws do applications have?
## How critical are software security flaws?
![Chart showing density of flaws detected in applications]
We know that the majority of applications have flaws, but are we talking more like ten or a ton? We use a metric called flaw density 
for this, because it normalizes for applications of different sizes. In short, flaw density tallies the number of flaws per MB of code 
identified in testing each application.
On average, a typical application has 42 flaws for every 1 MB of code. That seemed odd to us, so we asked Deep Thought to crunch 
the numbers. It took a while, but 42 was indeed verified to be the answer to life, the universe, and everything AppSec.[^1]
There are two primary metrics for assessing whether flaws represent 
a critical security risk—severity and exploitability. Here’s the gist:
Of course, many applications don’t conform to what’s typical. We see some with densities as low as 1 flaw per 100 MB and others as 
high as 1 in 10 B. We’ll explore some reasons why applications differ so much according to flaw density later, but we’ll stop here for 
this “At a Glance” section.
1. Severity is the flaw’s potential impact on confidentiality, 
integrity, and availability.
2. Exploitability is the likelihood or ease with which an attacker 
could exploit a flaw.
Overall, about 3% of all flaws are considered very high severity, and 
16% are very likely to be exploited by attackers. Thankfully, less than 1% 
of all flaws earn the highest (worst) ratings for both criticality metrics. 
If we broaden the threshold to include issues that are high severity 
and likely to be exploited (the upper-right 2x2 quadrant), we get 
5.5% of all flaws. It goes without saying that these rare but risky 
security flaws warrant quick attention from developers, though 
it must be acknowledged that the glut of Medium-Likely flaws 
(43.5% of all flaws) represents a substantial attack surface for many 
organizations that must be managed as well.
![Chart showing rating of flaw severity and exploitability (percent of all flaws)]
[^1]: There are also 42 charts in this report and the original draft had 42 pages. Alas, there were some changes during the Vogon review process.
Veracode State of Software Security 2024
11
## What types of flaws are most common?
In addition to ratings of severity and exploitability, identifying the types of flaws present in code provides useful insight into building 
threat models, assessing risk, and prioritizing remediation. There’s no shortage of approaches for categorizing software flaws, but the 
CWE and OWASP Top 10 are two of the most popular.
The figures here plot CWE categories based on their frequency across and within applications. Those toward the right affect a lot of 
applications, and those near the top cluster in droves. Not many flaw types sit high on both the prevalence and intensity scales, but 
developers should take note of those that do. They’re the most likely to affect your code.
![Chart showing prevalence and intensity of CWE and OWASP flaws in applications]
We’ll briefly point out Vulnerable and Outdated Components in the upper-right of the OWASP Top 10 plot. The inclusion of flaws 
found via SCA scans in these results is a big reason why this features more prominently than it has in the past. It’s a reminder of a 
theme we’ll keep coming back to in this report: identifying and remediating flaws in third-party code requires a different approach. 
The pervasiveness of vulnerable versions of the log4j library two years following the discovery of a zero-day exploit is a case in point.
Veracode State of Software Security 2024
12
## Where are flaws most likely to be introduced?
## How quickly are flaws remediated?
![Chart showing prevalence of flaws in first-party (left) vs. third-party (right) code among applications]
The prevalence of flaws related to vulnerable third-party components 
necessitates a deeper look at the security of the software supply chain. 
We all know that flaws can be introduced in code that your team writes 
(first party) or via open-source software or other third-party libraries 
imported into applications. But which of these sources is more common?
Turns out it’s actually pretty close. Roughly 63% of applications have 
flaws in first-party code, and 70% contain flaws in third-party code. That 
obviously means many apps have both, which is why including scans of 
both sources at various points in your secure development life cycle is 
so critical. We share more analysis specific to third-party libraries in the 
Securing the Software Supply Chain section.
Moving on from finding security flaws, let’s talk about fixing them. 
How long do flaws stick around after being discovered? Overall, 
roughly one-third to one-fourth of all flaws are fixed in the first three 
months. The half-life for flaws across all applications (the time it 
takes to fix half of them) is about nine months. 
Per the chart below, 41% of first-party and 48% of third-party flaws 
persist beyond the one year mark to become “security debt.”  
The half-life of third-party flaws is also longer—11 months compared 
to 7 months for first-party flaws.
> First-party code: Code written 
directly by your development team 
for your applications.
> Third-party code: Code imported 
into your applications via third-party 
libraries. Though not all third-party 
libraries are open source, we use that 
term interchangeably in this report.
> Security Debt: For the purposes of 
this report, we are defining all flaws 
that remain unremediated for over 
one year, regardless of severity, 
as security debt. In some cases of 
security debt, developers make a 
decision not to fix those flaws. In 
others, fixes are delayed for various 
reasons. We’ll analyze remediation 
timelines more later in this report.
Veracode State of Software Security 2024
13
![Chart showing probability of flaws converting to security debt in first-party vs. third-party code]
Like its financial corollary, security debt tends to pile up over time and gets harder and harder for developers to pay off. But the good 
news is there are data-backed strategies for getting out of debt that we outline later in this report.
## How common is software security debt?
In many ways, security debt reflects a culmination of the software security stats we’ve measured so far. It’s a byproduct of how many 
flaws are present and how long it takes to fix them.
As shown here, 42%[^2] of active applications (those that have been scanned for at least one year) have flaws that constitute security 
debt (and some of them carry a lot of debt).[^3] That’s an important finding that deserves much more than a passing glance. Let’s dig 
deeper into exactly how much debt, where it comes from, and how to begin eliminating it in the next section.
![Chart showing prevalence of security debt across all applications greater than one year old]
[^2]: We also verified this with Deep Thought to be sure.
[^3]: The proportion of apps with debt changes substantially depending on how we slice the data. Showing those different slices goes beyond the scope of this “at a Glance” section, so we 
added a special insert on the next page for those interested.
Veracode State of Software Security 2024
14
Veracode State of Software Security 2024
14
## How common is software security debt? (Revisited)
Before moving on to explore security debt more deeply, let’s revisit the final question posed in the prior section. The answer greatly 
depends upon how we slice the data. We’ll give some examples here.
If we don’t filter out applications less than one year old, the waffle plot shown back in Figure 8 looks like this. There’s a larger 
proportion of apps with no debt (because they’re too young to have started accruing it), and the debt ratio drops from 42% to 23%.
We also see substantial differences based on the types of scans conducted. We’ll get into this later, but SCA scans of open-source 
libraries tend to show a lower proportion of security debt than SAST or DAST. The net result is that the combined view in the original 
Figure 8 has a lower overall debt rate.
To illustrate that effect, here’s a version of this same chart based on SAST and DAST scans (SCA removed). This may be more in line 
with the expectations of many with a much larger percentage of applications saddled with security debt (69% rather than 42%). 
We’re not trying to undermine the findings or delve into the pedantic here. We simply want to arm readers with the insight that 
things will shift depending on what subset of the data (or type of scans) we’re examining, which is why we’ll try to make that clear in 
the analysis that follows.
![Chart showing prevalence of security debt across all applications (NOT filtered to one year old)]
![Chart showing prevalence of security debt across all applications scanned with SAST and DAST]
Veracode State of Software Security 2024
15
We define security debt as any flaw that 
persists unremediated for longer than one 
year. We saw that 42% of all applications have 
flaws that exceed that threshold, which makes 
security debt far from a rare phenomenon. 
This section digs deeper into exactly how 
much software security debt organizations 
carry, where it comes from, and what you can 
do to begin eliminating it for good.
## Measuring
and Managing
Security Debt
Veracode State of Software Security 2024
16
The prior charts do not address the extent of debt within these organizations, so let’s go there next. To do this, we have removed 
organizations with very few applications to avoid misleading conclusions based on tiny scopes (e.g., debt in 1/1 apps would be 100% 
debt ratio). 
Within this sample, 10% of organizations show no security debt.[^4] Among those that do, as shown in Figure 12, the typical (median) 
firm has security debt in a third of its active applications. Security debt affects at least two of every three applications in a quarter of 
organizations. And just north of 1 in 10 firms has security debt in at least 90% of its applications. 
> Security Debt: All flaws that remain 
unremediated for over one year, 
regardless of severity.
> Critical Security Debt: High-severity 
flaws that remain unremediated for 
over one year.
## The prevalence of security debt
Security debt occurs within individual applications, but those applications 
are developed and managed by organizations. Thus, we begin by 
measuring the prevalence of security debt across all active applications  
for each organization in our dataset.
A large majority of organizations (71%) have security debt at some level. 
And close to half of all firms (46%) have high-severity persistent flaws that 
we’ll classify as critical security debt. Based on this, we can conclude that 
software security debt is a major organization-level challenge.
![Chart showing prevalence of security debt (left) and critical security debt (right) among organizations]
[^4]: This differs from Figure 11, the preceding donut chart (29% with no debt), because we’ve removed firms with less than seven applications.
Veracode State of Software Security 2024
17
![Chart showing prevalence of security debt across applications >1yr old within organizations]
![Chart showing prevalence of critical security debt across applications >1yr old within organizations]
We create a version of this chart that isolates critical security debt in Figure 13. Over a quarter (27%) of organizations in this sample 
show no signs of persistent high-severity flaws as of their latest scans. Roughly half of them have critical debt in less than 16% of 
their applications. About one in ten firms exceed a critical debt ratio of 49%.
Continuing our task of measuring the prevalence of security debt across all organizations, we thought it might be interesting to look 
at debt ratio as a ratio of all flaws. Figure 14 takes the form of a beeswarm chart, with each “bee” (dot) representing an organization. 
Those firms are grouped according to the percentage of flaws across all their applications that constitute security debt (top) and 
critical security debt (bottom). 
This security debt ratio is spread fairly evenly across organizations but “swarms” a bit more toward the higher end of the scale. From 
this, we can discern that just under half of all flaws (47%) for the majority of organizations can be considered security debt. In our 
experience, many dev teams let old issues slide in order to better focus on fixing new issues that arise as code is written.
At the same time, many organizations manage to achieve a much lower security debt ratio—especially for critical debt. The ratio of 
critical debt generally ranges in the low single-digit percentages among all flaws for most organizations. That, at least, is something 
we can all “bee” happy about.
Veracode State of Software Security 2024
18
![Chart showing percent of flaws per organization that qualify as security debt]
![Chart showing distribution of security debt across applications >1yr old in 20 organizations]
To close out this section and help visualize the prevalence of security debt in organizations, we offer Figure 15. Each rectangle 
represents an organization sampled from our dataset, which is subdivided into sections corresponding to the size of its active 
applications. The color applied to those applications measures their density of security debt. You can think of this as a depiction 
of the application attack surface of each organization.
Veracode State of Software Security 2024
19
> All data used in this report is 
anonymized. We’re able to 
attribute flaws and applications 
to a randomized organization ID 
to enable analysis like what you 
see in Figure 15, but the data 
does not allow for identification 
of “Org #4.” 
Organization #4 is relatively clear of debt across most of its applications, with a few 
exceptions in the lower right corner. Organization #9 below it shows pretty much 
the opposite trend—one tiny debt-free application floats alone in a sea of debt. 
Other organizations in this sample exhibit a relatively even distribution of debt 
across applications (e.g., Org #14) to an application attack surface that runs the 
gamut of debt density (e.g., Org #6).
So, what makes one organization look so different from another when it comes to 
the distribution of security debt across their applications? Is it possible for teams 
to reverse indebtedness for the applications they develop and manage? Evidence 
presented in the next couple of sections points to the affirmative—keep reading!
## Factors that contribute to security debt
How do applications and organizations fall into security debt? What dynamics are at play to drive it up or down over time? These are 
the types of questions we aim to answer in this section as we explore some of the contributing factors to security debt.
### Application age
Since security debt has a time component, it makes sense that 
the age of the application may play a role in its accumulation. 
We’ve also observed in prior SOSS editions that the pace of 
flaw remediation tends to wane as an application ages. 
The chart below suggests there is indeed an age factor driving 
security debt. Recall that unremediated flaws become debt after 
one year. At that point in an application’s life cycle, ~42% of all 
flaws roll over into security debt. Indebtedness grows to ~62% at 
the three-year mark and rises further still to 75% after five years.
![Chart showing proportion of flaws that qualify as security debt by age of application]
Veracode State of Software Security 2024
20
### Application size
The codebase of most applications grows over time, so it’s logical that a correlation might exist between age and the accumulation of 
older, unremediated flaws. Let’s test that theory.
The charts below show the distribution of security debt among applications grouped into similar age and size ranges. On the age 
scale, applications are considered younger if they’re between 1 and 2.1 years old, middle between 2.1 and 3.4 years), and older 
after 3.4 years. Those are admittedly weird breakpoints, but they roughly divide all applications into three equal bins. We took a 
similar approach for grouping small (<250kB), medium (250kB-1.55MB), and large (1.55MB+) applications based on the size of their 
codebase.
Ignoring the values in the shaded squares for a moment, let’s note the overall prevalence of security debt listed below the size labels 
on the vertical axis. Large applications have the highest proportion of security debt (40% of applications) and critical debt (47%). 
Medium-sized applications fall a little below that, and the debt ratio among small applications is lower still in both charts. 
Now, on to the shaded age-size groupings. It’s obvious that both security debt and critical debt concentrate most intensely in the 
upper-right section of large legacy applications. That tracks with our assumptions and observations.
That fact may lead one to assume that the youngest, smallest apps would be the least riddled with debt, but that does not appear to 
be the case. That designation goes to older small applications in both charts. But overall, we definitely see a size factor contributing 
to security debt here.
These results won’t settle the perennial debates on the vices and virtues of monoliths vs. microservices in AppSec. But on the topic 
of managing security debt, monoliths clearly present a greater challenge.
![Chart showing distribution of security debt across application age and size]
Veracode State of Software Security 2024
21
### Application language
In prior SOSS versions, we’ve shown that the language used to develop applications has a strong bearing on security outcomes across 
the board (flaw types, prevalence, fix times, etc.). It seems like a foregone conclusion, then, that languages would have a lot to do 
with an application’s debt destiny too. But there’s no need to rely on assumptions here; we have the data to know for sure.
Figure 18 compares the security debt profile for different development languages based on the most recent scans. It does this by 
plotting the proportion of applications (x-axis) and flaws (y-axis) that exhibit debt (left) and critical debt (right). The size of the dot 
corresponds to the number of applications for each language. 
It’s admittedly not a chart lending to quick and easy takeaways. But if you really want to understand the debt profile of the languages 
you use, the juice here is worth the squeeze. We’ll start with a couple squeezes and sips of our own to get the juices flowing.
![Chart showing prevalence of security debt by application development language]
> Remember, different languages 
have inherently different 
security postures, environments, 
and controls. Developers can 
compare how their languages 
perform and get a view of areas 
for future focus.
The top languages in terms of total applications—Java, .NET, JavaScript—
land mostly in the middle of the pack for security debt and critical debt. 
Holdovers of legacy codebases, such as VB6 and Perl, exhibit the higher rate 
of indebtedness that likely squares with the expectations of most readers. 
We also note the low levels of critical debt for iOS and Android apps.
Veracode State of Software Security 2024
22
### First vs. third-party code
We saw earlier that flaws in third-party (open-source) code tended to become security debt at a slightly higher rate (48%) than those 
in first-party code (41%). Let’s pull on that thread a bit more here to see just how big a role this plays in the piling up of security debt 
in your applications.
The aforementioned remediation statistics represent the probability that first or third-party code in applications contains 
unremediated flaws older than one year. Another way to look at this is to isolate all security debt that exists across all applications 
and then determine what proportion of that debt is in first-party or third-party code. We’ve done exactly that in Figure 19. 
### Flaw types
It’s tempting to think of all security debt as resulting from oversight, poor decisions, failure to execute, etc. But that’s not always the 
case. Sometimes, developers make conscious decisions to fix certain flaws while letting others lie. The data can’t reveal to us the logic 
behind such decisions, but it does clearly show that certain types of flaws are more likely to become security debt. 
Figure 20 lists the CWE categories we analyzed for prevalence back in the “At a Glance” section. This time, however, we’re focused 
on the likelihood of first-party flaws in each category hanging around long enough to become security debt (based on SAST and 
DAST scans). Ostensibly, those toward the top of the list tend to be addressed faster because they’re perceived to represent more 
risk or are easier to fix.
The top part of the chart makes it clear that the vast majority (89%) of all security debt across all active applications exists in first-
party code. So, statistically speaking, your own code is 90% of your debt problem. That strongly suggests that organizations wanting 
to drive down debt most effectively should focus first on code created by their own developers.
BUT there’s another side of the story (and chart) here. When we narrow in on critical security debt, third-party code comes to the 
forefront with a two-thirds majority. This suggests that organizations wanting to drive down debt representing the highest risk should 
focus first on third-party libraries that often constitute a large proportion of their codebase (see Figure 34).
![Chart showing proportion of security debt and critical debt in first-party vs. third-party code]
![Chart showing probability of first-party flaws converting to security debt by CWE category]
Veracode State of Software Security 2024
23
Because developers don’t tend to set priorities for remediating third-party code, one may expect to see different results for flaws 
identified through SCA scans. Indeed, Figure 21 reveals many new CWE categories as well as substantial shifts in the ordering among 
existing categories. For example, Credentials Management and Authentication Issues are among the least likely to become debt in 
first-party code, but the opposite is true for third-party code.
Many of these differences can be traced back to how these flaws are fixed. The developer sets the priority and fixes flaws in first-
party code. Third-party code is largely fixed by updating the libraries, so the type of flaw isn’t really a consideration. The correction 
sometimes given to children applies here: “You get what you get and you don’t get upset.” 
![Chart showing probability