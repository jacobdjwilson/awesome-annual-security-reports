2026 Data Breach
Investigations
Report

About the cover Our own 2026 report is
the topmost ring, followed
“The only constant is change” is
by 2025, 2024 and 2023,
an aphorism commonly ascribed
the last one already settled
to Greek philosopher Heraclitus.
into the foundation.
There has been no historical
evidence uncovered that he had There are more zero days and
any hands-on experience with critical vulnerabilities year over
cybersecurity, but he would be year (YoY), generative artificial
right at home in our field with intelligence (GenAI) augmented
this mentality. But even as the malware is now a common
threat landscape constantly occurrence, and complex
evolves and changes, the 2026 forms of social engineering are
edition of the Data Breach becoming more successful as the
Investigations Report (DBIR) prelude to a breach. Their speed
invites you to consider the may be increasing, their scale
importance of the fundamentals might be a concern, but those
of cybersecurity as the best way are all challenges defenders have
to brave all of this change. A been facing for a long time. This
little cyber-stoicism, if you will. new world should require more
focus, more agility, but does
On our cover, you can see
not necessitate an upheaval.
concentric rings, each one
Refinement, not revolution. We
representing a year of our
will be ready for the future if we
data, floating down and settling
continue to collaborate and work
onto the foundation of our
together for the greater good.
cybersecurity knowledge.
They add to our understanding Also, yes, those are technically
and complement our defensive donut charts. Sorry, not sorry.
strategies and are segmented
by the incident patterns from
the past four years.

61% System Intrusion
17% Social Engineering
2026
10% Basic Web
Application Attacks
8% Miscellaneous Errors
3% Privilege Misuse
53% System Intrusion
18% Basic Web
Application Attacks
2025
17% Social Engineering
12% Miscellaneous Errors
7% Privilege Misuse
36% System Intrusion
25% Miscellaneous Errors
2024
22% Social Engineering
9% Basic Web
Application Attacks
8% Privilege Misuse

Table of
contents
| 1             | 4                     | 8        |
| ------------- | --------------------- | -------- |
| Introduction  | 5 Deep-dive analysis  | Wrap-up  |
How to use this report  6 The paths of privilege escalation  67 Year in review  108
Key topics and findings   10 The North Korean IT worker risk  73
9
| 2   | 5   |     |
| --- | --- | --- |
Appendices
| Results and analysis  | Industries  |     |
| --------------------- | ----------- | --- |
Appendix A: Methodology  111
The big picture  15 Introduction  76 Appendix B: U.S. Secret Service  113
VERIS Actors  23 Educational Services  82 Appendix C: Using the DBIR
for Security Risk Decisions   114
| VERIS Actions  | 29 Financial and Insurance  | 84  |
| -------------- | --------------------------- | --- |
Appendix D: Contributing
| VERIS Assets  | 33 Healthcare  | 86  |
| ------------- | -------------- | --- |
organizations  117
| VERIS Attributes  | 35 Manufacturing       | 88  |
| ----------------- | ---------------------- | --- |
|                   | Public Administration  | 90  |
3
|                                   | Retail               | 94  |
| --------------------------------- | -------------------- | --- |
| Incident Classification Patterns  | 6                    |     |
| Introduction                      | 38                   |     |
| System Intrusion                  | 40 Focused analysis  |     |
Social Engineering  48 Small- and medium-sized businesses  97
| Basic Web Application Attacks  | 54  |     |
| ------------------------------ | --- | --- |
7
| Miscellaneous Errors  | 56                 |     |
| --------------------- | ------------------ | --- |
| Privilege Misuse      | 58                 |     |
| Denial of Service     | 62 Regions         |     |
|                       | Regional analysis  | 100 |
2026 DBIR Table of contents 4

Introduction
Welcome to Verizon’s 2026 Data Breach Investigations As we have done for the past several
years, we examine key industry verticals
Report! Hello again to those who’ve been with us over
in detail, along with a snapshot for small-
the years—and to those joining the DBIR community and medium-sized businesses (SMBs).
And last but certainly not least, we once
for the first time, it’s great to have you. As always,
again provide regional analysis for the
we’re glad you’re here. Asia and the Pacific (APAC) and Europe,
Middle East and Africa (EMEA) regions,
so you can see how these trends show
up in your own sector and part of
In this 19th edition of the Verizon We have observed that, in some areas, the world.
DBIR, we dig into more than 31,000 cybercrime has shifted in meaningful
Amid all this change, one message stays
actual real-world security incidents, of ways since the publication of the 2025
the same: The threat landscape will keep
which more than 22,000 were confirmed report. In others, it is less a matter
evolving, but the fundamentals still matter
data breaches involving organizations of change and more a matter of speed
most. Organizations that stay grounded
in 145 countries. This represents the and scale. Exploitation of vulnerabilities,
in strong cybersecurity basics (clear
largest number of breaches we have discussed in several sections of the
visibility into assets and third parties,
ever examined in a single report! Yes, we report, has now emerged as the most
disciplined patch management, and
realize that we have said that before, but common way attackers gain initial access
well-practiced response plans along
what can we say? It’s still true because into an organization’s environment, which
with a culture that supports and enables
the number of cases we examine underlines the ongoing importance of
secure behavior) are better positioned
continues to increase YoY. We leave it getting the basics right. Additionally, as
to handle today’s realities and whatever
up to you to determine if that is a good the ancient prophecies2 foretold, threat
comes next.
thing or a not so good thing.1 For the actors are increasingly relying on GenAI
victim organizations, it is undoubtedly the to assist them with various stages of Sincerely,
latter, but for our purposes of illuminating their attacks, such as choosing targets,
The Verizon DBIR team
threats to your business, it is firmly in the gaining a foothold within those targets,
C. David Hylender, Philippe Langlois,
former camp. conducting vulnerability research, and
Alex Pinto, Suzanne Widup
developing malware and other tools to
If we were to give this report an
make their efforts more effective and With special thanks to our Verizon
overarching theme, it would be “keeping a efficient. Meanwhile, Social Engineering, colleagues:
strong foundation in the face of change.”
a longtime fan favorite, is evolving, - Chris Novak, for guidance and support
Few people would argue that change, in
as well, with attackers increasingly all these years
every aspect of modern life, confronts us
using voice and other mobile-centric - Steven Baskerville, Darrin Kimes
at an ever-increasing pace these days.
techniques to catch people off guard and Jim Meehan from the Verizon
The insights we try to provide in this
in the middle of the workday. Threat Research Advisory Center
report attempt to equip enterprises to
(VTRAC) team
meet cybersecurity changes in the most Regarding the System Intrusion pattern,
- John Sandiford from Verizon
effective manner possible. And even we discuss the fact that Ransomware
Cybersecurity Architecture Australia
though this report's dataset covers Oct continues to be among the most
2024 through Nov 2025, both the DBIR disruptive and impactful types of Additional recognition for some of our
team and Verizon are keenly aware of breaches we see. Not unlike the price research partners this year:
the growing impact and capabilities of of everything from fast food to adult - Raymond Carney and Scott Caveza
AI-augmented vulnerability research and beverages in ballparks, it continues to from Tenable
weaponization so far in 2026 based on trend upward. And we would certainly
- Saeed Abbasi from Qualys
early indicators and trends observed at be remiss if we did not reference the
- Jay Jacobs and Michael Roytman
the time of publication, and will provide increasing role that the broader web
from Empirical Security
some forward-looking commentary in of third parties that organizations rely
regards to that where applicable. on can play in your security posture. - Felipe Esposito and Alexandre Sieira
However, there is a silver lining, but you from Tenchi Security
will have to read on to learn about it. After - Kyla Guru and Jacob Klein
all, we didn’t spend all this time and effort from Anthropic
writing jokes and witty content to simply
- Simran Khalsa and Kelly Shortridge
give away the whole story on page one. from Fastly
- Kellie Roessler, Michael Barnhart
1. Or a fantastic thing! Ok, we’re data breach geeks. and Rajan Koo from DTEX
2. And by ancient, we mean predicted in the past two DBIR reports and mentioned a couple paragraphs ago.
2026 DBIR Introduction 5

How to use this report
Sections of the report
The report is divided into four
First-time readers: large sections:
• In “Results and analysis,” we will be
Before you get started on the 2026 DBIR, it might be a good focusing on the big picture of what
idea to take a look at this section first. We have been doing this happened in the previous year and
exploring our complete dataset in each
report for quite a while now, and we appreciate that the verbiage
of the four main components of the
we use can be a bit obtuse at times. We use very deliberate
VERIS framework (Actors, Actions,
naming conventions, terms and definitions and spend a lot of Assets and Attributes), with eventual
time making sure we are consistent throughout the report. guest appearances from other VERIS
Hopefully this section will help make all of those more familiar. enumerations as applicable. This
section should be useful and provide
If you are a longtime reader (thank you!) and are already familiar
actionable information for all our
with how to use the DBIR, you are welcome to skip to the
readers, regardless of their industry
next section. segments or regions of the world.
• In “Incident Classification Patterns,”
we subdivide our dataset into patterns,
which are shorthand for specific, very
common incident archetypes with
illustrative names such as System
Intrusion or Denial of Service (DoS).
What you will find here The breadth of data collection is
This section is specifically helpful
what sets this report apart. Vendor-
if you are looking for a deeper dive
The Data Breach Investigations Report specific reports are able to talk very
into those categories of incidents
(DBIR) focuses on the analysis of authoritatively and in great detail about
and seeking additional research and
anonymized cybersecurity incident data the cases they investigated themselves,
remediation guidance.
that Verizon collects every year from but here we are seeking to bridge
almost a hundred data contributors. different perspectives and contributor • In “Deep-dive analysis,” we highlight
Those data points are normalized using types—large incident response long-form research we have done
the Vocabulary for Event Recording and outfits, boutique forensics firms, law for this year’s report that didn’t fit
Incident Sharing (VERIS) framework enforcement from local to country well in any other section. Expect
(more about it on the right), which level, cyber insurance brokers and cork boards, lots of red string and
provides us a great foundation for reinsurers—with the hope that it will get analysis combining all sorts of different
statistical analysis of this type of data. us closer to the capital T “Truth” of what datasets from our data contributors.
Given the culture of secrecy (and is going on in the threat landscape. This
• In “Industries,” “Focused analysis”
just how difficult incident response is poses unique challenges that we go over
and “Regions,” we focus our view of
sometimes) that still permeates these at length in our “Methodology” appendix,
the dataset across different industry
cases, we often don’t have all the very and sometimes in the content of the
verticals and regions of the world and
specific details of any given incident. report itself.
provide additional analysis on SMBs.
These sections provide more specific
analysis for the segment and should
help folks in each segment to focus
on where they might want to prioritize
their efforts.
2026 DBIR How to use this report 6

VERIS framework Learn more here:
resources
• github.com/vz-risk/veris—features the
framework’s JavaScript Object Notation
The terms “threat actions,” “threat
(JSON) schema with some usage, utility
actors” and “varieties” will be referenced
scripts, enumeration listings, mappings
often. These are part of the VERIS, a
to Center for Internet Security (CIS)
framework designed to allow for the
Critical Security Controls, MITRE
consistent, unequivocal collection of
ATT&CK and a VERIS Style Guide
security incident details. Here is how
they should be interpreted:
• verisframework.org—a slightly more
Threat actor: Who is behind the event? user-friendly website providing
This could be the external “bad guy” information on the framework with
who launches a phishing campaign examples and enumeration listings Figure 2. Example slanted bar chart
or an employee who leaves sensitive (n=230)
documents in their seat back pocket.
Incident vs. breach
Threat action: What tactics (actions) Industry labels
We talk a lot about incidents
were used to affect an asset? VERIS
uses seven primary categories of and breaches and we use the We align with the North American
threat actions: Malware, Hacking, following definitions: Industry Classification System (NAICS)
Social, Misuse, Physical, Error and Incident: A security event that standard to categorize the victim
Environmental. Examples at a high level compromises the integrity, confidentiality organizations in our corpus. The
are hacking a server, installing malware or availability of an information asset. standard uses two- to six-digit codes to
or influencing human behavior through a classify businesses and organizations.
social attack. Breach: An incident that results in the Our analysis is typically done at the
confirmed disclosure—not just potential two-digit level, and we will specify NAICS
Variety: More specific enumerations of exposure—of data to an unauthorized codes along with an industry label. For
higher-level categories—e.g., classifying party. A distributed DoS (DDoS) attack, example, a chart with a label of Financial
the external “bad guy” as an organized for instance, is most often an incident (52) is not indicative of 52 as a value.
criminal group or recording a hacking rather than a breach since data is rarely “52” is the NAICS code for the Financial
action as SQL injection or brute force. exfiltrated. However, we realize that and Insurance sector. The overall label
There are also “vectors” and “motives” doesn’t make it any less serious. of “Financial” is used for brevity within
and “categories,” but we do our best the figures. Detailed information on the
in each section to ease folks into the codes and the classification system are
nomenclature and try to make it clear available here: census.gov/naics.
how to interpret those terms. Also, any
weird capitalization issues you may find
throughout the report are referring to
VERIS “Proper Nouns” and have specific
meaning tied to them in the framework.
As much as in the Fae world, true names
have power here.
Figure 1. Example spaghetti chart
2026 DBIR How to use this report 7

Being confident in our data
Starting in 2019 with slanted bar charts,
the DBIR has tried to make the point that
the only certain thing about information
security is that nothing is certain. Even
with all the data we have, we’ll never
know anything with absolute certainty.
However, instead of throwing our hands
up and complaining that it is impossible
to measure anything in a data-poor
environment or, worse yet, just plain
making stuff up, we get to work. This
year, you’ll continue to see the team
representing uncertainty throughout the
Figure 3. Example dot plot (n=10,000—each dot is one event)
report figures.
Orange: lower half of 80%; Yellow: upper half of 80%; Green: 80%–95%; Blue:
The examples shown in Figures 1, 2, 3 Outliers, 95% of events: 402–597 80% of events: 435–565, Median: 500
and 4 all convey a range of realities that
could credibly be true. Whether it be
the slant of the bar chart, the threads As you can see, some of the threads This is what you could be looking
of the spaghetti chart, the dots of the are looser than others, indicating a at instead of unreadable pie charts
dot plot or the colors of the pictogram wider confidence interval and a smaller everywhere else. Embrace the silly
plot, all convey the uncertainty of the sample size. glyphs and never forget what they took
cybersecurity industry in their own from you.
The dot plot is another returning
special way.
champion, and the trick to understanding
The slanted bar chart will be familiar this chart is to remember that the dots
to returning readers. The slant on the represent a specific number of events,
bar chart represents the uncertainty described in the figure caption. This is
of that data point to a 95% confidence a much better way of understanding
level (which is a common standard for how something is distributed among
statistical testing). In layman’s terms, if organizations and provides considerably
the slanted areas of two (or more) bars more information than an average or
overlap, you can’t really say one is bigger a median. We added more colors and
than the other without angering the callouts to those in an attempt to make
math gods. them even more informative. In statistical
terms, it’s just a quantized density chart.
Much like the slanted bar chart, the In non-statistical terms, who doesn’t love
spaghetti chart represents the same colored little dots?
concept: the possible values that
exist within the confidence interval. The pictogram plot attempts to capture
However, it’s slightly more involved uncertainty in a similar way to slanted
because we have the added element of bar charts but is more suited for a single
time. The individual threads represent value or two. We hope they make your
a sample of all possible connections journey through this complex dataset
between the points that exist within even smoother than previous years.
each observation’s confidence interval.
Figure 4. Example pictogram plot
(n=100—each glyph is one kiwi bird)
2026 DBIR How to use this report 8

About the 2026 DBIR
incident dataset
Questions? Comments? Concerns?
Each year, the DBIR timeline for in-scope
incidents is from Nov 1 of one calendar
year through Oct 31 of the next calendar Let us know! Send us a note at dbir@verizon.com or reach
year. Thus, the incidents described in this
out to Verizon Business (or one of the authors) on LinkedIn.
report took place between Nov 1, 2024,
Be sure to tell your colleagues, families and neighbors (and
and Oct 31, 2025. The 2025 caseload
is the primary analytical focus of the Verizon Executives) about how much you love the report!
2026 report, but the entire range of
If your organization aggregates incident or security data and
data is referenced throughout, notably in
trending graphs. The time between the you’re interested in becoming a data contributor or research
latter date and the date of publication partner to the annual Verizon DBIR (and we hope you are), the
for this report is spent in acquiring
process is very easy and straightforward. Please email us at
the data from our global contributors,
dbircontributor@verizon.com so we can discuss the details
anonymizing and aggregating that data,
analyzing the dataset, and finally creating and make you a part of the DBIR research community.
the graphics and writing the report. The
jokes, sadly, do not write themselves.
Credit where credit is due
Turns out folks enjoy citing the report,
and we often get asked how to go
about doing it.
You are permitted to include statistics,
figures and other information from the
report, provided that (a) you cite the
source as “Verizon 2026 Data Breach
Investigations Report” and (b) the
content is not modified in any way.
Exact quotes are permitted, but
paraphrasing requires review. If you
would like to provide people a copy of
the report, we ask that you provide them
a link to verizon.com/dbir rather than
the PDF. You are, however, forbidden to
generate pie charts based on data from
the report. No exceptions.
2026 DBIR How to use this report 9

Key topics
and findings
Rise of
vulnerability
exploitation
Exploitation of vulnerabilities is now
the most common initial access vector
for breaches. It has risen to 31% in this
year’s reporting dataset, while credential
abuse—the previous leader—is down
to 13%.
Only 26% of critical vulnerabilities—
defined as being in the Cybersecurity
Infrastructure and Security Agency
Known Exploited Vulnerabilities (CISA
KEV) catalog—were fully remediated by
organizations in 2025, a drop from the
previous year’s 38%.
The median time for full resolution went
up to 43 days, almost two weeks more
than the previous year’s 32 days. In the
median case, organizations had 50%
Figure 5. Known initial access vectors in non-Error, non-Misuse breaches over time
more critical vulnerabilities to patch in
(n for 2026 dataset=19,905)
this year’s reporting dataset compared
to the previous year.
2026 DBIR Key topics and findings 10

Growth in
ransomware
and third-
party breaches
continues.
Ransomware grew again to 48%
of all breaches, up from 44% from
the previous year. However, ransom
payments have continued to decline
among our dataset, as 69% of
ransomware victims didn’t pay. The
median amount of ransom paid also
continues a downward trend: $139,875
in this year’s reporting dataset from
$150,000 in the previous year.
As organizations increase their
reliance on third parties for services
and software, their exposure increases,
as well, and breaches with third-party
involvement have increased by 60% from
last year’s dataset, reaching 48% of
total breaches.
Looking at remediation over time in
Figure 6. Survival analysis of third-party, cloud-based MFA exposures (n=7,513) third-party cloud exposure, only 23% of
third-party organizations fully remediated
missing or improperly secured
multifactor authentication (MFA) on their
cloud accounts, with 50% of all findings
being resolved within a month.
For weak passwords and permission
misconfigurations, the time to resolve
50% of all findings was much worse,
reaching almost eight months.
2026 DBIR Key topics and findings 11

Generative AI
impacting the
threat landscape
Threat actors are demonstrably using
GenAI to help at different stages of
attack, including targeting, initial access,
and development of malware and
other tools. The median threat actor
researched or used AI assistance in 15
different documented techniques, with
some Actors leveraging as many as 40
or 50.
Most AI-assisted development of
malware and tooling was associated
with well-known and defined attack
techniques, with a median of 55 existing
known malware examples performing the
same functions.
Less than 2.5% of the AI-assisted
malware observations involved less-
common techniques with one or fewer
known malware examples.
Figure 7. Distribution of known existing malware examples per ATT&CK technique
observed (n=9,897—each dot is 247.43 observations)
Mobile-centric
Social Engineering
Human element was present in 62%
of breaches, a slight increase from the
previous year’s 60%. Social Engineering
was our third most common breach
pattern, representing 16% of all breaches.
In phishing simulations, the median rate
of successful “click” rates in mobile-
centric vectors (such as voice and text
messaging) is 40% higher than via email.
Pretexting has become a more common
initial access vector to ransomware
and extortion attacks. In all breaches, it
reached 6%, while Phishing remained
at 16% like the previous year. Pretexting
is an attacker tactic in which a trusted
relationship is built through concocted
scenarios to trick the user into taking an
action that unknowingly compromises
the organization, frequently by voice
communications but also seen via email
Figure 8. Distribution of success rate of non-Email vector-simulated social attack
or text messaging.
campaigns (n=35—each dot is 0.88 campaigns)
2026 DBIR Key topics and findings 12

Shadow AI policy
violations and
malicious insiders
Regarding usage of unauthorized GenAI
services (“Shadow AI”), 67% percent of
users are using non-corporate accounts
on their corporate devices to access
AI services, a slight decrease from
the previous year. However, 45% of
employees are now considered regular
users of AI (authorized or not) on their
corporate devices, up from 15% in the
previous year.
Shadow AI is now the third most
common non-malicious insider action
detected in our data loss prevention
(DLP) dataset in 2025, a fourfold
increase in percentage from the
Figure 9. Select data types in untrusted DLP events targeting generative AI tools
previous year.
(n=858,440)
The most common type submitted to
external GenAI models was source code,
followed by images and other types of
structured data. In 3.2% of DLP policy
violations, we even found research and
technical documentation being uploaded
to those unauthorized AI systems,
which presents a risk of intellectual
property exposure.
2026 DBIR Key topics and findings 13

Results
and analysis
/02

The big picture
Hello, everyone, and welcome to the This year, we have managed to analyze Vulnerable
“Results and analysis” section. This is more than 22,000 breaches—a
beginnings and
where we cover the highlights we found significant increase from our previous
in the incident dataset for this year’s reports. Not only have we expanded
social changes
report. This dataset is collected from our contributor base, but we have also
a variety of sources, including our own doubled down on our capabilities to
VTRAC investigations, incident reports collect data in bulk from major public As any writer knows, there are few
and summaries provided by our data extortion and Espionage-motivated things more oppressive than a blank
contributors and publicly disclosed campaigns, along with ransomware page staring back at you from your
security incidents. actor activity. As a result, the report computer screen, as if mocking your
now offers a more expansive view of inability to put your scattered thoughts
Because data contributors sometimes
the threat landscape, although this down on paper.
come and go, one of our priorities
information overload made our data
is to make sure we can get broad Well, not today, blank paper! There is a
pipelines run considerably slower.3
representation on different types of good place to start this edition of the
security incidents and the countries This subsection focuses on broader, DBIR, and that is at the literal beginning
where they occur. This ebb and flow and hopefully more actionable, high- of the breaches we analyzed. We have
of contributors obviously influences level findings that go beyond the been tracking the initial access vectors
our dataset, and we will do our best traditional structure of the VERIS 4As of breaches for a few years now, and
to provide context on those potential (Actor, Action, Asset and Attribute) and the continual growth of exploitation of
biases where applicable. builds on some of the key metrics we vulnerabilities since the 2024 DBIR had
have been highlighting over the past us wondering when it would find its way
few years. to being the top vector. There is no need
to wonder anymore.
Hey kids, no name-calling please.
Longtime readers are likely aware that the DBIR team has always
taken the position that we will not “call out” specific cases in the
report and will refrain from including anything that would allow
for inferring non-publicly available victim information.
This is very much still the case; however, for large-scale,
publicly disclosed campaigns that affected a high number
of organizations, we refer to the campaigns by their most
commonly used terminology in the report to avoid confusion.
We also comment on high-profile individual breaches but
only refer to their publicly available information. Even if we
had non-public information about those, we would be unable Figure 10. Initial access vectors—select
enumerations in non-Error, non-Misuse
to correlate it with our dataset due to its anonymization.
breaches (n=20,023)
Figure 10 has all the details we need.
The exploitation of vulnerabilities is the
most prominent initial access vector
in our dataset this year, reaching the
height of 31%, up from 20% last year,
which represents a 55% increase in
this vector.
3. Have y’all seen how much computer memory and hard drives are costing these days?
2026 DBIR Results and analysis 15

Credential abuse, previously our most You should stop postponing that MFA “Enter your password here,” “download
common, has fallen steeply from 22% rollout in your organization because this software there,” whatever suits the
in the 2025 DBIR to 13%, but there is a credentials are an integral part of the threat actor’s fancy.
good contributing reason for that. This threat actor’s toolkit.4
Pretexting, however, is much more
year, we added Pretexting—our second
involved and insidious, as it intrinsically
most frequent social action variety—to
It’s not just a pretext. involves a synchronous component.
our tracked list of initial access vectors.
There the actor is—on the other side of
Because there is frequently some The addition of Pretexting was not simply
the phone, text message conversation
overlap between Pretexting actions and done on a whim.5 Even though its total
or email thread—trying to convince
credential abuse (this also happens in percentage is roughly the same as in the
the victim to do something or provide
Phishing cases), this addition played a previous report (within statistical error),
some information they shouldn’t. The
role in the lowered percentage for our there was a significant number of high-
reason this matters is because the
former champion. For comparison with profile ransomware breaches in
countermeasures and training needed
the 2025 DBIR results, this value without this year’s dataset that utilized this
to combat those two different scenarios
the addition of Pretexting would have Social Engineering technique as the
are actually quite distinct.
been 16%. initial action.6
Security awareness training involving
However, this does not mean that From this development, we believe it is
email phishing simulation is quite
defenders should discount the important to re-introduce the distinction
ubiquitous in security programs
importance of mitigating credential between the Phishing and Pretexting
nowadays, but the nature of pretexting
abuse. This analysis focuses on the actions in the VERIS framework—and
requires more involved business-oriented
first initial action we can determine for by extension in the DBIR—because the
rules and guidelines that are aligned
the breaches we collect, but credential mitigations necessary for each of them
with the nature of each potential target
abuse is pervasive across various attack might not be as similar as you think.
area in your organization. Training
paths and is a legitimate mitigation target
chokepoint. As Figure 11 demonstrates, As VERIS defines it, Phishing is, in IT help desks and customer support
if you consider all instances of credential essence, an asynchronous social action. agents to not be helpful and supportive
abuse at any point in the breach The victim will receive an email (or a in cases when a threat actor is trying
progression, it still sits on top at 39%. text message) that attempts to alter to manipulate them is not as simple as
their behavior in ways that will allow the “check if the email is external, from a
incident to progress to its next step. source you trust and if it uses proper
language.”7 We will be discussing voice
and other non-email means of Social
Engineering in the—drumroll—“Social
Engineering” section of this report.
Knowledge is half the
“vulnerability” battle.
Given the uptick in Exploitation of
vulnerabilities in our initial access vector
analysis, it is a good idea to check
in on our favorite sisyphean cause:
vulnerability management.
To be clear, vulnerability management
is an incredibly important risk mitigation
process that needs to exist in virtually
every organization, but the headwinds
Figure 11. Select initial access vectors in non-Error, non-Misuse breaches over time facing organizations implementing it
(n for 2026 dataset=19,905) have been discouraging, to say the least.
Put quite simply, there are often too
many vulnerabilities and not enough
4. If you are interested in learning more, we have some fascinating topics about infostealers and Initial time for patching all of them.
Access Brokers (IABs) in the “System Intrusion” section.
5. There are several of those all the time in the DBIR, but this one is not one of them.
6. We will discuss them a bit further in this section.
7. Given the reported increase of AI assistance in phishing emails, we are changing the detection guidance
from “does it contain many typos” to “does it contain em dashes.”
2026 DBIR Results and analysis 16

We once again chose the CISA KEV
list as our subset of vulnerabilities8 that
all organizations are incentivized to
patch, and we set out to replicate the
metrics of percentage of remediation
and the median time to do so. In this
study, which includes aggregated
information from more than 13,000
organizations, we were not only focusing
on vulnerabilities added to the CISA KEV
in 2025. Any vulnerabilities uncovered
by the scanners in an organization’s
environment that were in the CISA KEV
by the end of 2025 were being counted. Figure 13. Distribution of the median of days until full remediation of CISA KEV
After all, an old unpatched vulnerability vulnerabilities in a single company (n=10,597—each dot is 132.46 unique CVEs
that suddenly becomes the focus of an per company)
attacker campaign can be as disruptive
to the process as a brand new one.
Figure 12 shows the percentage of
unique CISA KEV vulnerabilities found in
organizations per remediation status.
Figure 14. Distribution of unique CISA KEV CVEs per organization (n=13,773—each
dot is 247.43 organizations)
The “Remediated” column is our The results are worse than last year.
favorite because it represents that the Only 26% of the CISA KEV vulnerabilities
organizations in question have fully had been fully remediated, a
patched all instances of those considerable drop from last year’s 38%.
specific vulnerabilities. Even if you are a “glass half full” person
and want to give full marks to partially
In the “Partially remediated” column, only
remediated ones, the unremediated ones
some of the instances were patched for
add up to 16%, an increase from the 12%
whatever reason, and maybe there were
found last year.
valid risk management-related reasons
not to patch them all, as opposed to a There is also a worse result for the
simple failure to complete the task. Of median time elapsed for a vulnerability
Figure 12. CISA KEVs per CVE the “Unremediated,” we dare not speak. to be fully patched by detection, shown
resolution status (n=515,170) That way lies madness. in Figure 13. Our new median time is
43 days, almost two weeks longer than
last year’s 32 days. Figure 14, however,
begins to elucidate the mystery: The
median number of KEV vulnerabilities
that had to be patched by organizations
8. To allow for easier comparison and aggregation of the multiple vulnerability management research has risen in 2025 to 16, where this figure
partners the DBIR has, the singular focus was on vulnerabilities that have an assigned Common
was 11 in 2024. That is almost 50% more
Vulnerabilities and Exposures (CVE) identifier. We know there are exploited vulnerabilities with no
CVE assigned and also the larger discipline of exposure management, but we need to be able to KEV vulnerabilities to patch in a year.
compare apples to apples here across disparate datasets.
2026 DBIR Results and analysis 17

There were 68.7 million records in
the 2022 dataset and 527.3 million in
2025—almost eight times the volume.
At Day 28, that 35% translates to 184
million open vulnerability instances, up
from 31 million in 2022. The number of
distinct organizations in this dataset
did not vary significantly YoY, so we
are comfortable in comparing those
absolute vulnerability numbers to provide
perspective on the enormity of the task
they face.
Another interesting way to measure this
is by focusing on the top performers.
Organizations with well-developed
vulnerability management processes do
not typically wait for a vulnerability to
appear in the CISA KEV catalog before
committing to patching it.
In the 2024 calendar year, 17% of
Figure 15. CISA KEV vulnerability survival analysis: four-year comparison (2022– vulnerability instances were remediated
2025) (n for 2022=68,697,749 vulnerability instances) (n for 2023=120,803,360 prior to their inclusion in the KEV
vulnerability instances) (n for 2024=295,795,092 vulnerability instances) catalog. However, despite organizations’
(n for 2025=527,255,454 vulnerability instances) best efforts, this preemptive remediation
rate fell to 12% in 2025. In absolute
numbers, defenders proactively patched
Survival of the vulnerable The 2025 DBIR, based primarily on data
a staggering 63.7 million vulnerability
from 2024, was the high water mark.
instances in 2025, a 30% increase from
Those findings reinforce the “patching At every milestone in the survival chart,
2024 (48.9 million).
capacity issue” hypothesis we organizations were remediating faster
have proposed in our vulnerability than they ever had before, showing There appears to be a ceiling, and
management analysis section over the improvements from 2022 to 2023 the data suggests diminishing returns
past few years. To shed more light on and from 2023 to 2024. at current resource levels. By Day 7,
this subject, we decided to go back to which is an incredibly fast milestone for
a survival analysis approach to allow Then 2025 happened and the curve remediation by any standard, somewhere
us to measure the full life cycle of shifted back to 2023 levels, with 35% between 60% and 70% of KEV
each patched vulnerability instead of a still open at Day 28 (up from 27% in vulnerabilities remain open regardless of
snapshot at the end of the year. 2024) and with the long tail settling year, volume or organizational maturity.
at 9%. This represents 47 million
This first-week rate barely moved
Figure 15 shows the survival curve—the vulnerability instances that, based on
despite three years of additional process
percentage of KEV vulnerabilities still our curve trajectory, are simply not being
development, tooling investment and
open at weekly intervals—grouped by addressed any time soon.
mandate pressure.10
the last four DBIR reporting periods
starting with the 2022 report. This In aggregate, the conclusion seems to Those results should inspire additional
dataset combines more than 1 billion be that organizations collectively did get analysis by other researchers, but
anonymized vulnerability detection worse at this patching thing, but what more than 1 billion records are nothing
records, courtesy of one of our tipped the scales here was the volume to sneeze at. This might be an initial
vulnerability management research flowing through the system. measurement of the “speed of light”—
partners.9 The picture it paints is that a theoretical limit—for vulnerability
of a treadmill picking up speed. remediation processes.11 Organizations at
their very best only get to fix 30%–40%
9. Qualys published additional insights from this dataset in a report they published in March 2026: qualys. of KEV instances in the first week after
com/forms/whitepapers/the-broken-physics-of-remediation detection, so choosing12 the correct ones
10. Let’s be optimists for a moment and assume organizations continually improve their processes.
to patch really is the key strategy.
11. Huge opportunity for a cybersecurity company to invent the Alcubierre drive: en.wikipedia.org/wiki/
Alcubierre_drive
12. Or guessing
2026 DBIR Results and analysis 18

Recency bias for the win? It should shock no one that nearly half
of the vulnerabilities in the KEV are
On the topic of strategies for choosing deemed to have “Persistent” exploitation,
which vulnerabilities to patch first, the which means they could be detected an
team was inspired by a recent report average of 96% of the days. What might
from one of our research partners13 prove surprising, though, is how many of
about the concept of resurgent those were older vulnerabilities and not
vulnerabilities. The main concept is just the latest and shiniest. Only 20%
that even vulnerabilities that are very of the vulnerabilities in the “Persistent”
old—discovered years ago and that category were registered in the CVE
in an ideal world should have been database in 2024 and 2025. For the
patched already—will sometimes have other 80%, organizations would have
exploitation activity associated with had about two years’ advance notice
them all of a sudden. in which to patch.
At a high level, their results suggest The challenge is that the CISA KEV is a
that focusing only on patching the timestamp and not a timeline. It marks
newer vulnerabilities and leaving a Figure 17. Clusters of expoitation activity when a vulnerability reaches a critical
backlog of critical ones with no apparent frequency of CISA KEVs (n=991) mass of exploitation in the wild but does
exploitation is not a guaranteed win. not discuss if the exploitation rate falls
However, this just gives us more tasks to or disappears. Let’s try to add this time
We will be focusing on those for the
complete, which does not help the issue dimension to it because, regardless of
analysis, as the dataset did not (or could
of our patching needs outstripping our the categorical label on a vulnerability,
not) detect exploitation activity for the
capacity to effectively patch. Is there a the same decay pattern seems to hold
remaining vulnerabilities.
more principled way of deciding against once exploitation is observed.
new versus old? Figure 16 shows the frequency of
Using the same frequency analysis of
exploitation in a very colorful chart,
To replicate this analysis with frequency vulnerabilities as before, and some light
similar to the ones in the GreyNoise
of exploitation data from another of our modeling, it is possible to try to forecast
report we mentioned earlier. With the
new research partners, we enlisted one how likely it is for a vulnerability to
help of some old-fashioned unsupervised
of the former DBIR writers who happens resurge and go back to being actively
clustering algorithms, we can boil
to work at said research partner.14 exploited based on how recently it has
this down to four discrete frequency
been exploited.
There were 1,526 CVEs listed on the categories, described in Figure 17, for
CISA KEV as of February 2026, and 991 the CISA KEVs with detectable The analysis covers roughly 1.4 million
of those had some exploitation activity exploitation activity. observations of approximately 1,000
over the past 12 months. vulnerabilities over six years. For each
day a vulnerability was being tracked,
we recorded two things: how many
days had passed since the last known
exploitation activity (so we naturally had
to wait for the first observed activity)
and whether that vulnerability was
exploited again within the next 30 days.
The model shown in Figure 18 finds the
mathematical relationship between
those two things.
The main conclusion here is that the
longer it’s been since a vulnerability
has been exploited, the less likely it is
to be exploited again soon. A case
Figure 16. Heat map of exploitation activity frequency of CISA KEVs per day (n=991) of recency bias if we’ve ever seen
one but surprisingly aligned to
the measurements.
13. Read the GreyNoise report at greynoise.io/resources/how-resurgent-vulnerabilities-jeopardize-
organizational-security.
14. Shout out to Jay Jacobs, Chief Data Scientist at Empirical Security. Much of the automation the DBIR
team uses today leverages code he wrote more than a decade ago, and we will never forgive him
for that.
2026 DBIR Results and analysis 19

People are not computers. Plan
accordingly in your cybersecurity
strategy. And please feel free to refer
back to our discussions of this topic in
the 2024 and 2025 DBIRs.18
The third and last measure concerns the
involvement of third parties in breaches,
and we will dedicate time to discussing it
in the next few pages. This metric comes
in at 48% this time around, up from 30%
last year. That is a 60% increase, after
already doubling the year before—quite
a trajectory.
Figure 18. Re-exploitation probability by last known exploitation (points=empirical
rate by observation count, line=GLM fit) This sustained growth has proven
impossible to ignore, as many of
the year’s most high-profile and
The pattern held consistently across However, this is a base assumption that
well-publicized breaches involved
the full six-year observation, which gives the promise of increased automation
multiple third parties. In several of the
reasonable confidence it reflects an of vulnerability discovery and exploit
more notable campaigns, attackers
actual structural feature of exploitation development from GenAI tooling could
compromised more than one third-party
behavior rather than just noise.15 upend. It’s a fun way to look at the
provider at the same time.
problem, regardless.
The odds drop off quickly in this model.
The probability drops by roughly half at
30 days, again at 90 days and again by Two’s company,
half around nine months. After around a
three’s a breach.
year, the probability of seeing resurgent
exploitation activity is about the same as
if it wasn’t ever exploited. In addition to our usual discussion of
initial access vectors, there are a few
With this result, if faced with the choice
other metrics we have been tracking as
of patching a vulnerability that is less
part of our big-picture analysis. We have
than a year old in the KEV but that hasn’t
a visual aid for you in Figure 19, where we
been exploited recently or one that
capture major data points in our dataset,
isn’t on the KEV (yet) that your threat
including the first item, which serves as
intelligence indicates does show recent
an important reminder of the prevalence
exploitation history, focusing on the
of credential abuse even in the face of
one with recent activity could be a
growing vulnerability exploitation.
smarter bet.
The second data point measures
This approach is informed by historical
the non-intentional human element Figure 19. Select key enumerations
patterns and should be weighed
contribution in breaches, which has been in breaches
alongside other risk factors specific to
fairly stable since the 2024 DBIR. This
your environment.16 This model behavior
year it reached 62% of all breaches.
does align with the understanding that
While this is technically a statistical
threat actors have to develop exploits
increase from the 60% recorded in the
and maintain infrastructure scanning
2025 DBIR, when one accounts for
for vulnerabilities, and there are only so
our error margins, it definitely does not
many of those that can be done at the
warrant extensive analysis.17
same time.
15. Or the recency bias devils trying to clean up their act
16. The insights offered by the DBIR should not be used for vulnerability betting in prediction markets.
17. If you’re disappointed to hear this, don’t fret. We have a whole section dedicated to Social Engineering.
18. Unfortunately, we have to adhere to a very strict page budget to get this report out the door each year.
2026 DBIR Results and analysis 20

The rule of three19 The bad news is that we increasingly But with a closer analysis of the root
see a combination of two of those—or causes, a good number of these cloud-
As a reminder, our third-party metric even all three—contributing to a breach. based, third-party incidents highlighted in
combines three different kinds of Based on publicly disclosed information, the media in 2025 boil down to insecure
business relationship archetypes, which one such example involved a recent authentication (absence of MFA,
concern themselves with where the initial campaign around the Salesforce plugin improper credential rotation) or lack of
access happens and where the data that Salesloft Drift facilitating breaches of least privilege enforcement for users or
was breached was stored: customer data in the platform.21 service accounts.
1. Vendor in an organization’s software According to publicly available Excessive privileges in cloud
supply chain: The data and initial information on this campaign, the environments—be they Infrastructure,
vector were under the organization’s customer OAuth tokens (or the keys Platform or Software as a Service
custody and control, but the initial to derive those OAuth tokens at will) (IaaS, PaaS and SaaS, respectively)—
vector was only made possible given from the Salesloft Drift application were is a pervasive issue. In fact, any
a vulnerability in a vendor product compromised (Archetype 3, initial access considerations on authentication,
(i.e., the majority of single Exploit vuln vector against the Salesloft vendor) secret management and obviously MFA
actions we mention in this report) or and then they were used against the are strong points of attention for any
the compromise of said vendor and Salesforce platform to steal data from cloud environment. Since we are in the
the inclusion of a back door in the the customers (Archetype 2, your data third-party section, let’s dive into what
software (such as what happened with exfiltrated from the vendor environment). can happen in your third-party’s cloud
SolarWinds a few years ago, based on environment configuration, aka, their
publicly disclosed information). third party.22
Avoiding data breach
2. Vendor hosting an organization’s spectator mode
data in its environment: The initial
access is against the vendor itself, At first glance, there doesn’t appear
and the vendor is the custodian of to be anything that could have been
your organization’s data. The two done to prevent these from the victim
big sub-categories here involve organization’s perspective.
your vendor’s infrastructure being
breached directly or your account to
the vendor’s environment being stolen
and used against its systems (last
year’s campaign involving Snowflake is
a good example of the latter, based on
publicly disclosed information).
3. Vendor with connection to an
organization’s environment: The
initial access is on the vendor, and
lateral movement is done to reach the
data inside your organization. This can
either be a literal network connection
that is leveraged by attackers (like the
Target breach that happened more
than a decade ago where a network
connection to a vendor was the
way in, based on publicly disclosed
information) or by the vendor losing20 Figure 20. Survival analysis of third-party, cloud-based authentication and privilege
exposures (n=354)
credentials to an organization’s internal
systems to attackers.
19. Not to be confused with The Sign of Four
20. Or handing over due to Social Engineering
21. help.salesforce.com/s/articleView?id=005134951&type=1
22. As our 2025 DBIR cover would like to remind you, it is third parties all the way down.
2026 DBIR Results and analysis 21

For a different perspective, looking
at a point-in-time snapshot across
another cloud exposure dataset, 37%
of organizations had an admin account
with MFA disabled on an IaaS offering.
For reference, only 14% of organizations
had an admin account with MFA disabled
on Snowflake, leading us to believe most
customers got the memo from last year’s
breach campaign.
This is just a small slice of potential
exposures of cloud environments, but
a strong starting point is to focus on
the authentication and authorization
layers, as those are usually the ones
that end up on an organization’s end
Figure 21. Survival analysis of third-party, cloud-based MFA exposures (n=7,513)
of the responsibility matrix of cloud
environments. These are security
fundamentals that have been understood
The third rule of survival The lingering tail remaining so high—
and had measurable success for
close to our 50% survival rate—
This year, we have access to a robust shows that this is an exposure that decades now,24 and they should be
dataset from a new research partner organizations struggle with resolving. applied to all systems and environments
focused on third-party cyber risk In fact, what is an “excessive permission” that allow them, where feasible and
management (TPCRM), including anyway? An admin account is an easy appropriate to the organization’s risk
resolution times of common types of concept to understand, but given the profile. We should pay special attention
exposures collected directly from inside granularity present in cloud environment to service and machine accounts, as
the third-party cloud environments— configurations in IaaS environments,23 those will likely be the ones leveraged in
a remarkable find because, up until it is an almost impossible task to make our potential agentic AI future.
now, we’ve only had access to informed decisions based on the least-
outside scanning data of those privilege principle under normal business
kinds of environments. time constraints.
Resolution times allow us to do survival Figure 21 shows that with something
analysis and thereby pull off the same that is commonly accepted as a control
tricks we usually have available for that should be implemented at every
vulnerability management. Figure 20 opportunity, such as correct MFA
includes the survival analysis of poor configuration, the overall remediation
password practices and excessive results are better. Our 50% survival rate
access permissions combined on here is roughly a month, and the tail
those third-party cloud environments. converges to roughly 32% of lingering
Taking almost eight months to fix MFA-related issues. The percentage of
this category of exposure makes our organizations that fully remediated this
vulnerability management numbers seem category of issues is a bit lower, sitting
lightning fast. Still, the full remediation around 23%.
percentage here is 31%, comparable
with our success rate with the CISA KEV
vulnerabilities in the initial access vector
analysis discussed earlier in this section.
23. Not to mention the incredibly complex user interface and experience (UI/UX) involved in taming access
control in those cloud environments.
24. At least our Certified Information Systems Security Professional (CISSP) Exam Prep book from 25
years ago said this, so we can confidently say decades, plural (RIP, Shon Harris).
2026 DBIR Results and analysis 22

VERIS Actors
Throughout this report, we use That’s been the story for all 19 iterations Who would
terminology from the VERIS framework.25 of this report, and this year is no
do such a thing?
At the highest level of VERIS categories exception: 88% of threat actors were
are the 4As: Actor, Action, Asset and External—a bit higher than last year but
Attribute. When we say “Actor,” we mean still slightly below many of the earlier Each of the top-level Actor categories
exactly what it sounds like—the threat years when that number routinely sailed can be sliced into more specific varieties.
actor behind the breach or incident. past 90%. For external actors, most roads lead
Those actors fall into a few familiar back to Organized criminal groups
Internal actors appeared in 12% of
buckets: External (someone outside the (Figure 23). In this context, Organized
breaches this year—a decline from last
organization), Internal (an employee or crime isn’t about cinematic mob families;
year’s 18% but still enough to keep IT
other insider), Partner (an entity with a it simply means criminals who run their
and security teams from chalking it up
business relationship with the victim) operations in a systematic, repeatable
as a rounding error. These cases can
and, finally, multiple (any combination way. They have a process, and they
be especially thorny, since they typically
of the above). follow it with great success. This variety
involve people with legitimate access
dominates the dataset, driven largely by
and at least a basic understanding
the continued popularity of ransomware
of how things work on the inside. By
and other extortion-centric attacks.
contrast, breaches involving Partners
or multiple actors were relatively State-affiliated actors make up the bulk
uncommon and barely moved the needle of the remainder, appearing in close to
when compared to the dominant Internal 15% of breaches.
vs. External storyline.
Figure 22. Actors in breaches
(n=22,345)
You don’t need a calculator to figure out
that, no matter how big your organization
is, there are always more people on
the outside than the inside. Therefore,
it shouldn’t shock anyone unduly that Figure 23. Top External actor varieties Figure 24. Top Internal actor varieties in
External actors continue to be the in breaches (n=16,491) breaches (n=1,000)
ones causing the most trouble
(Figure 22).
25. Yes, we know we discuss this in the “How to use this report” section, but we also know many of you
don’t read it.
2026 DBIR Results and analysis 23

It’s also worth calling out that The Espionage motivation is also
many of these internal cases aren’t present, albeit to a much smaller degree,
cloak-and-dagger sabotage; they’re as shown by the presence of state-
often mistakes, Misconfigurations, or affiliated actors in the data.
creative shortcuts and unapproved
While most Espionage cases involve
workarounds that simply backfire. These
those groups, the same motive also
are all carried out without any malicious
surfaces among internal actors looking
intent but with very real consequences.
to walk off with proprietary data—
whether to hand it to a competitor or
But why, though? to benefit themselves in some other
manner. These kinds of cases are
Motives tend to mirror who is behind the frequently the hardest to catch without
attack. As Figure 25 shows, Financial specific offboarding processes in place
gain remains the leading driver for for those employees who have access
cybercriminals (we’ll pause while you to the most sensitive data.
recover from the shock).
Figure 25. Top actor Motives in
breaches (n=18,175) Actor categories26
As usual, these cases tend to be External: External threats originate from sources outside
Espionage-driven, helping to bankroll of the organization and its network of partners. Examples
foreign nation-states’ more ambitious
include criminal groups, lone hackers, former employees and
projects—whether that’s advanced
government entities. This category also includes God (as in “acts
weapons programs or, who knows,
maybe even chipping away at a few of”), “Mother Nature” and random chance. Typically, no trust or
student loans. privilege is implied for external entities.
Once we stop looking over the fence Internal: Internal threats are those originating from within the
and turn our gaze inward, the internal
organization. This encompasses company full-time employees,
actors driving risk are mostly familiar
independent contractors, interns and other staff. Insiders are
faces: End-users at 75% and System
administrators at 19% (Figure 24). trusted and privileged (some more than others).
Internal actors may only account for 12%
Partner: Partners include any third party sharing a business
of breaches overall (both unintentional
errors and deliberate actions), but when relationship with the organization. This includes suppliers,
an employee acts maliciously, the blast vendors, hosting providers and outsourced IT support. Some
radius can occasionally rival—or even
level of trust and privilege is usually implied between business
exceed—that of an External attack. This
partners. Note that an attacker could use a partner as a vector,
is especially true when privileged access
or sensitive systems are involved. but that does not make the partner the Actor in this case.
The partner has to initiate the incident to be considered the
responsible party.
26. verisframework.org/actors.html
2026 DBIR Results and analysis 24

Yes, I’d love to help
you write that malware.
The number of reports of malware Would the use of AI by attackers even be It’s not depth of use—
and other hacking tools that leverage notable or visible from an organization’s it’s breadth of reach.
AI-assisted code27 or elements of perspective, especially considering the
large language models (LLMs) in their current scale and scope of cybercrime Anthropic’s dataset covers 793 unique
workflows28 has really grown in the last activity? threat actors between Mar 2025 and
few months of 2025 and early months Feb 2026. All 793 received enforcement
To try to answer some of those
of 2026. Threat intelligence groups have action from the Anthropic Safeguards
questions, we collaborated with
been working hard to try to pin down Team for violating the acceptable use
Anthropic (developers of the Claude AI
this frontier-of-attack technology and to policy and had sufficient behavioral
model) to understand their perspective
discover if there is something really data to analyze. Their queries spanned
on how threat actors are misusing their
novel going on. malicious cybersecurity topics, including
platform for nefarious cyberactivity.
malware development, capability
Over the past couple of years, the DBIR Anthropic’s recent report29 about the
building and tasking. Anthropic
has maintained a skeptic stance around first documented case of a largely AI-
took this data and classified the
the usage of those tools and whether executed state-sponsored espionage
behavior against the MITRE ATT&CK
they would move the needle in a way that campaign was a watershed moment for
framework, which provides us a unique
could be measured by real incidents. understanding the potential and risks of
perspective to correlate this activity
Of course, experimentation happens, the technology for many cybersecurity
with what defenders can see from their
but how much would that actually practitioners, your authors included.
perspectives. This included both cases
change the likelihood an organization Building on this research, we wanted to
of actors using the platform to write
gets breached? understand the overall usage of LLMs
code to perform one or more of the
by threat actors and its implications
techniques or leveraging it to complete
for defenders.
the action in an agentic fashion.
Figure 26. Distribution of unique ATT&CK techniques researched by actors on AI platform (n=793)
27. bitdefender.com/en-us/blog/businessinsights/apt36-nightmare-vibeware
28. cloud.google.com/blog/topics/threat-intelligence/distillation-experimentation-integration-ai-
adversarial-use
29. anthropic.com/news/disrupting-AI-espionage
2026 DBIR Results and analysis 25

Figure 26 shows the distribution of This lines up with some of our previous
techniques that were leveraged by each results from last year, where the
of those malicious actors. In the median increased use of AI-assisted text in
case, actors sought AI assistance for malicious emails had doubled in relation
around 15 distinct techniques across to the previous years.
the MITRE ATT&CK. In the extreme
However, looking at our own incident
cases, actors were querying for as many
dataset outside of Anthropic’s data,
as 40 or 50 techniques, representing
the percentage of Phishing as an initial
multisession campaigns where actors
access vector has barely moved over
treated the platform as a co-developer
the past few years, signaling that maybe
across the full attack chain.
AI assistance in this specific group of
It’s worth pointing out that these are techniques is not increasing the success
extreme cases. Anthropic rates threat rate in the victim organizations that
actor risk using signals such as number make up the DBIR’s incident dataset.
of detection hits, technical sophistication There could have been an increase of
and which platform was used for the success rate in targeting individuals for
activity (e.g., code assistance plugin or fraud purposes that we are not able to
the chatbot interface)—and less than measure, as they are out of scope of the
1% of those 793 actors fell into the analysis of this report. It can uplift less-
High or Critical category, while 99% of experienced groups to a higher baseline
actors fell into the Medium and Low level of proficiency in English, or the
Figure 27. Generative AI-assisted
Risk categories. target language of their social attack, but techniques categorized as initial
that new baseline might not be enough access methods (n=837)
for a higher success rate.
Here is how we
break it down. However, we note that 32% of initial
access techniques are related to
To start off, let’s look at the reported exploitation of vulnerabilities, a
techniques that fall under the Initial concerning finding given its growth
Access ATT&CK tactic and map them trajectory in our incident initial access
to our most common initial access vector analysis. Leveraging AI coding
vectors,30 as they may explain some of assistance tools to create an exploit
the changes this past year or they might tool, change the language of the tool
signal a future shift in pressure against or discover new potential vulnerabilities
organizations’ defenses. Figure 27 has is within reach with current AI
the details. coding assistance.31
Although Exploitation of vulnerabilities
and credential abuse match our previous
analysis in the incident dataset, we can
see Phishing in the lead aggregating
44% of the AI-assisted initial
access vectors.
30. As discussed earlier in the report in the “Results and analysis” section
31. We will discuss this recent development a bit more in a sidebar in the “VERIS Actions” section.
2026 DBIR Results and analysis 26

The shocking reason The hypothesis: The fewer existing The median sits at 55, likely meaning
why that matters tools that support a given AI-assisted most AI-assisted techniques already
technique, the rarer that technique would have dozens of known tools that
A key question in understanding AI- be in the wild. implement them. In other words, the
enabled cyberthreats is whether most common uses are well-trodden
This helps provide visibility into
attackers are using LLMs to execute paths. The techniques with the most
whether the attackers are using LLMs
well-documented techniques more existing software examples show actors
to implement techniques that are
efficiently, or to pursue techniques that are likely outsourcing basic tasks to
already well known and documented,
are rarely seen in practice. If LLMs AI, such as file obfuscation or forensic
such as Process Injection, or if they
are lowering the barrier to techniques cleanup, whereas the ones with fewer
are leveraging LLMs for lesser-known
that are less documented and rare, software examples demonstrate more
techniques. It’s worth noting again that
defensive postures will need to catch creativity, with “Pre-OS Boot: The
since Anthropic’s analysis is bound
up. To investigate this, the DBIR team Unified Extensible Firmware Interface
by MITRE ATT&CK, “rare” here refers
developed a measure of technique rarity (UEFI)” and “Process Injection: Virtual
to techniques that are operationally
based on MITRE ATT&CK’s catalog Dynamic Shared Object (VDSO)
uncommon or difficult to execute within
of known malicious software and Hijacking” as standouts. According to
the existing taxonomy—not novel
offensive tooling. this classification, less than 2.5% of the
techniques altogether.33
techniques observed could be classified
MITRE publishes a list of known
Having said all that, Figure 28 shows the as rare (i.e., one known software example
malicious software or offensive security
number of existing software examples available or fewer).
tooling and the techniques that are
per technique observed in abuse cases.
leveraged by each of them.32
Figure 28. Distribution of known existing malware examples per ATT&CK technique observed (n=9,897)
32. attack.mitre.org/software
33. The world is not ready for a groundbreaking, quantum-enabled, blockchain-powered metaverse attack.
2026 DBIR Results and analysis 27

The takeaway from our dataset is Still, this raises the tide for all attackers,
that AI’s primary impact is currently and the baseline of what can be
operational: automating and scaling achieved with relative low cost is
techniques defenders already know broader. In a world where the security
how to detect, not yet unlocking these poverty line35 exists, any industrialization,
novel or rare attack surfaces—which even of simple techniques, could make
means defensive postures don’t need to the gap between the cybersecurity
be reinvented today, but they do need haves and have-nots even wider.
to keep pace with faster, more adaptive
Some of the top variables we need to
execution. But who knows? Given the
keep track of here as an industry are
rate of change in AI capabilities, this
how many of the actors start to present
assessment might be obsolete by the
a higher-risk profile, how many are
time this report is finally published.34
getting assistance in a greater variety
of techniques, and which ones point
Can I help you hack to more novel behavior in the software
another company? ecosystem where our ability to mitigate
and detect are not as well developed.
The current state of our dataset
reinforces what we’re seeing across
the threat landscape: AI is primarily
accelerating the operationalization of
well-known, documented techniques—
lowering the barrier to execute what was
once out of reach for less-sophisticated
actors. Anthropic’s previous reporting
from Nov 2025 actually demonstrates
that the real sophistication of actors
has historically come from the behavior
they do around the MITRE technique
assistance they get from AI. The
more novel cases include combining
or chaining together multiple stages
of the attack or taking more agentic
approaches to the attack, where the
agent makes executive decisions about
the targets.
34. Who is reading this report on their transparent, foldable phone in 2030?
35. Shout out to Wendy Nather and her seminal paper, “T1R Insight: Living Below the Security Poverty Line”:
web.archive.org/web/20140203193523/https:/451research.com/t1r-insight-living-below-the-security-
poverty-line
2026 DBIR Results and analysis 28

VERIS Actions
In the “VERIS Actors” section, we
covered the “who” behind the attacks in
our dataset. Here in the “VERIS Actions”
section, we shift to the “how”—the
methods those threat actors used to
ruin your day. You may think of actions
in cyberattacks like fashion trends: They
come in, they go out and just when
you think you’ve seen the last of them,
they resurface on your runway.36 In
any case, we wouldn’t mind if a few of
these techniques went the way of velour
tracksuits and never came back.
As you will see in other parts of the
report, particularly in the “Industries”
section, the top-level action types of Figure 30. Action varieties over time (n for 2026 dataset=22,624)
Hacking and Malware often appear in
relatively equal measure as illustrated
Once inside, threat actors often pair This highlights how unpatched or
in Figure 29. Hacking actions showed
Malware with additional Hacking actions otherwise exposed systems are
up in 64% of breaches this year, and a
to wander laterally around the victim’s still rolling out the red carpet to
corresponding Malware action appeared
network as if they own the place. As cybercriminals rather than being the
in 63% of breaches.
Figure 30 shows, both Hacking and hardened entry points they were
This makes sense because all that Malware have been rising in lockstep thought to be.
malware doesn’t just magically appear over the past few years. Much of that
Backdoor or command and control
on a system—it usually needs a little consistent rise has been driven by the
(C2) functionality appears in 16% of
help to get its foot in the door, and this ever-present Ransomware attacks we
breaches, only a modest increase
assistance frequently comes from some see, well, more or less everywhere.
from the previous year’s 14%.
kind of Hacking action. Meanwhile, Social attacks played a role
in a comparatively low 21% of breaches.
The top action varieties in breaches
(Figure 31) confirm that Ransomware is
still the yoga pants of cybersecurity—
ubiquitous, stubbornly popular and
appearing in unexpected places near
you. Nearly half (48%) of breaches in this
report feature Ransomware somewhere
in the attack chain. The sizable Other
category in second place isn’t hiding
anything exotic; it’s just a parking spot
for Hacking and Malware actions we
know occurred but couldn’t cleanly
classify due to limited visibility.
The Use of stolen credentials
holds steady at 36%, continuing its
long-running role as an attacker favorite.
Exploitation of vulnerabilities, however,
is having a breakout season. After
hitting an all-time high of 18% in last
year’s report, it has doubled to 32%
of breaches.
Figure 29. Actions in breaches Figure 31. Top action varieties in
(n=22,624) breaches (n=19,550)
36. Admit it, you missed parachute pants so much, you’re secretly delighted we brought them back.
You’re welcome!
2026 DBIR Results and analysis 29

One reason this number isn’t higher
comes into focus in Figure 33: Threat
actors seem to be dialing back their
reliance on traditional tools such as
Cobalt Strike as defenders get better at
detecting and blocking them. Instead,
attackers are increasingly blending in
with normal operations by using the
same access paths as legitimate users—
such as desktop-sharing tools and virtual
private networks (VPNs)—which helps
explain the noticeable rise of those
vectors in recent incidents.
Finally, a quick word on the top action
varieties in incidents: They largely track
what we see in the breach data, with a Figure 33. Select action varieties over time (n for 2026 dataset=18,175)
notable bit of extra flair in the form of
DoS attacks (Figure 32). In other words,
various forms of Hacking, Malware and
Social tactics tend to figure prominently
here, as well. However, incidents add
another layer of woe with disruption- Action categories37
focused activity rather than simply
data compromise. DoS attacks are less
Hacking: attempts to intentionally access or harm information
about stealing information and more
about kicking the chair out from under assets without (or exceeding) authorization by circumventing
Availability, reminding organizations that or thwarting logical security mechanisms.
not every incident is about data loss.
Malware: any malicious software, script or code run on a
device that alters its state or function without the owner’s
informed consent.
Error: anything done (or left undone) incorrectly or inadvertently.
Social: employ deception, manipulation, intimidation, etc., to
exploit the human element, or users, of information assets.
Misuse: use of entrusted organizational resources or privileges
for any purpose or manner contrary to that which was intended.
Physical: deliberate threats that involve proximity, possession
or force.
Environmental: not only includes natural events such as
earthquakes and floods but also hazards associated with
the immediate environment or infrastructure in which assets
are located.
Figure 32. Top action varieties in
incidents (n=27,765)
37. verisframework.org/actions.html
2026 DBIR Results and analysis 30

Exploring the
weakness within
This report has already spent quite a lot
CWE Percentage
of pages talking about the prevalence of
vulnerabilities and the struggle to patch CWE-125 - Out-of-bounds Read 79%
them, but there is another interesting
CWE-122 - Heap-based Buffer Overflow 77%
analysis angle that can shed some light
CWE-416 - Use After Free 77%
on the difficulties we are facing.
CWE-73 - External Control of File Name or Path 77%
This subsection was inspired by the
CWE-843 - Access of Resource Using
great work from the MITRE CWE38
Incompatible Type (‘Type Confusion’) 76%
team, where they rank the CISA KEV
CVE vulnerabilities discovered each
year by the weaknesses they are based
Table 1. CWE frequency of detected CISA KEV CVEs per organization (n=12,208)
on.39 Every single vulnerability has an
underlying technical raison-d’être, and
those are captured in the weakness
enumerations of the CWE. For example, CWE category Percentage
something like a Remote Code
CWE-1399 - Memory Safety 89%
Execution (RCE) vulnerability could
CWE-1396 - Access Control 85%
be caused by CWE-122, a “Heap-
based Buffer Overflow” or CWE-416, CWE-1416 - Resource Lifecycle Management 80%
a “Use After Free.”
CWE-1407 - Improper Neutralization 77%
The CWE focuses on the root cause of CWE-1404 - File Handling 77%
the vulnerabilities, so this is a sensible
and informative way of grouping together
vulnerabilities that otherwise would make Table 2. CWE category frequency of detected CISA KEV CVEs per organization
(n=12,208)
little sense to aggregate. They focus on
different software, and the vulnerabilities
were discovered at different times by
In fact, to find a weakness present in less This is why so much of the focus of
different security researchers—you get
than 70% of organizations, you would Secure by Design43 initiatives has
the picture.
need to go beyond the top 10. This is been centered around the elimination
Instead of looking at which vulnerabilities already very informative, and almost all of classes of bugs like those and,
were discovered in 2025, let’s have a of the top five seem related to memory specifically in this case, the advocacy
look at the ones that were the most safety vulnerabilities.40 of using memory-safe languages for
detected in our vulnerability management developing software.
We can summarize this further by
dataset throughout the analysis period of
rolling up the CWEs to their top-level As a bonus, we thought it would be
the DBIR and find the weaknesses most
categories.41 The results in Table 2 interesting to take a look at the other
commonly found therein.
confirm our fears. A staggering 89% of side of this equation, courtesy of one
Table 1 only shows the top five, but all organizations had to patch vulnerabilities of our new contributors that provided
of those weaknesses have been among associated with Memory Safety. Memory us with a very robust dataset of the
vulnerabilities detected in more than 75% Safety! “Smashing the stack for fun and detection of code flaws during the
of the organizations in our vulnerability profit”42 is from 1996, 30 years ago! software development life cycle. One of
management dataset. What are we still doing here? If this the metrics we can extract is the time of
vulnerability were a person living in the resolutions by categories of flaws.
U.S., they would not only be able to drive
but could also rent a car without paying By calculating the survival analysis for
a “young rental fee.” every single CWE grouping of flaws
found, we can get a measurement in
months of how long it takes to correct
the code and re-submit for testing of
50% of the flaws associated with
38. Not a typo, we do mean the Common Weakness Enumeration this time. each CWE.
39. cwe.mitre.org/top25/archive/2025/2025_kev_list.html
40. We can only speculate as to whether or not Rust would have prevented these from happening.
41. More about those categories, from the MITRE CWE itself: cwe.mitre.org/data/definitions/1400.html
42. A seminal paper published in Phrack 49 that introduced the concepts of buffer overflow, a common
memory safety exploit technique: phrack.org/issues/49/14
43. cisa.gov/resources-tools/resources/secure-by-design
2026 DBIR Results and analysis 31

By arranging those findings in a
distribution for each of the CWE
categories we used earlier, we can get a
good sense of how hard it is to resolve
our top three CWE categories from the
previous figure in practice for companies
with mature Software Developer Life
Cycle (SDLC) loops.
As Figure 34 shows, our top three CWE
categories have a median 50% survival
rate of between six and seven months.44
Re-testing cycles can potentially vary
a lot depending on the application or
organization’s SDLC processes, but this
result highlights how costly (or plain time
consuming) resolving the code flaws
can be if fixing them is taken seriously
by the developer. If you are curious, the
worst median 50% survival time for a
CWE category is for “Improper Input
Validation”—another nigh-unforgivable45
weakness category—sitting at just a bit
Figure 34. Distribution of time to remediate 50% of codebase weaknesses
over 13 months.
(in months)
Artificial strength
As solutions pairing those detection continue to promote the foundation
training46
capabilities with suggestions on how to and importance of Secure by Design
fix them emerge, will those remediation (with AI assistance when available) and
It is worth highlighting the recently
capabilities be equally effective across tried and true processes for software
declared success in the usage of GenAI
all vulnerability types, and would their testing and remediation, even if we
platforms to discover large numbers
detection strengths align with the are still having issues with 30-year-
of new vulnerabilities in code bases,
areas where those automated fixes are old classes of vulnerabilities. Outside
and we wonder how this will actually
the most needed. We look forward to your own development pipeline, one
change the calculus of discovery and
evaluating this as more data becomes recommendation is to prepare for a large
resolution of code flaws ahead of
available, but the expectation is that number of patches from coordinated
shipping software. Static Application
a model from an AI frontier lab with disclosures of AI-augmented vulnerability
Security Testing (SAST) and Dynamic
focused post-training and fine-tuning discovery, while making sure to inventory
Application Security Testing (DAST)
would likely47 achieve good results. and minimize your internet-facing
have distinct capabilities to find different
Still, “Quis custodiet ipsos custodes?”48 footprint.49 The zero-days will keep being
types of weaknesses, and maybe the
comes to mind. discovered and weaponized, regardless
GenAI solutions, when properly tuned
if fueled by tokens, by coffee or most
and productized, would eventually lean There is a lot of potential for changing
likely a mix of both.
toward SAST due to the whole “analyzing the landscape of the “code flaw to CVSS
the source code in bulk” angle. It’s hard 10.0 vulnerability pipeline” if the right The DBIR team wishes that there was
to conjecture, though, without objective types of weaknesses are targeted by more available and verifiable data on
data at hand. those solutions. In the meantime, we’ll what the future defensive landscape
leveraging those technologies will look
like. However, as reductive as “only
44. We know how it looks, but we did not mean to make a six-seven joke here. a good guy with AI can stop a bad
45. Speaking of influential papers, it’s never a bad time to reference “Unforgivable Vulnerabilities” by Steve guy with AI” may sound, practitioners
Christey Coley from 2007: cwe.mitre.org/documents/unforgivable_vulns/unforgivable.pdf.
46. This section was written in Feb 2026, roughly a couple months before the advancements in frontier should spend time exploring this AI
models by AI companies. It has been updated to provide actionable recommendations on a topic that frontier to help improve their defenses
becomes less theoretical by the minute.
when possible. The speed of those
47. And at least on the flaw detection and exploit development front in Apr 2026, the results have the
foremost experts in vulnerability discovery and disclosure on the edges of their seats. advancements really puts our only-
48. “Who watches the watchmen?,” a rhetorical question way older than the graphic novel itself publishes-once-a-year DBIR framework
49. For even more in-depth recommendations and discussions of impact, we suggest taking a look at a
to the test.
recent briefing put together by the Cloud Security Alliance: labs.cloudsecurityalliance.org/mythos-ciso.
2026 DBIR Results and analysis 32

VERIS Assets
Assets are ultimately the targets of the
attacks. This is where the proverbial
rubber meets the road in terms of
whether the ploy of the adversaries is
successful in furthering their goals. They
are also the places where your defenses
can make the most difference in stopping
an attack in its tracks. Understanding
which assets are targeted is critical
to drive the types (and placement) of
controls an organization needs to deploy.
Figure 36. Select top assets in breaches over time (n for 2026 dataset=20,862)
As in prior years, we break the data
down in multiple ways, including which
It accounted for just 1.5% of breaches Figure 37 shows which Asset varieties
assets are targeted most per industry
in last year’s report, but it is now tied we see most frequently targeted in these
(see the introduction in the “Industries”
with User devices, accounting for 5% of attacks. The top three are the same as
section). This provides defenders with
breaches where the asset was known. If last year. Unsurprisingly, web servers
a basic road map to link the attacks
you look at this chart on the 2025 report, and mail servers are prime entry points
targeting your industry to the assets
you will find a much smaller value for for criminals attempting to break into an
they are likely to hit. It works well as a
Network (0.3%). However, we changed organization’s infrastructure. The Person
tabletop exercise to determine if your
the way we code cases involving remote asset is also a tried-and-true target for
organization’s controls as they currently
access from a Server to Network to Social attacks, as mentioned above.
exist would be able to detect and
better align with those devices’ edge of
respond to the top attacks in
network role. It is still a significant rise in
your industry.
percentage for this variety of asset.
Figure 35 shows the ranking of the
Last year, User devices were targeted
VERIS Assets in breaches. The Server
in 8% of attacks, putting them ahead
and Person assets are in consistent
of Network assets. This year, they have
rankings with last year, but the Network
fallen to slightly below Network assets,
asset has seen quite an increase
but the difference between them is
this year.
statistically negligible. Suffice it to say
that Network and User device assets are
similarly targeted in this year’s dataset.
The pairing of Server and Person has
dominated the asset landscape since
at least 2019, with nothing else coming
close to those two asset classes, as
Figure 36 shows. However, there is still Figure 37. Asset varieties in breaches
a significant difference in frequency (n=9,723)
between the two. This highlights
how prevalent Social actions, which
OT or not OT?
compromise the Person asset, remain
despite ongoing efforts to reduce this That’s the
risk through training and awareness.
question.
Does this mean that your people will
always fall for social attacks? No, but it
Figure 35. Asset types in breaches
(n=20,862) does mean that you should make it as Information about incidents in
painless as possible for them to notify operational technology (OT) equipment
you when they do, so you have a is often sparse and has not grown
chance to contain the damage enough in the past few years for us to
before it escalates. do a deep dive of any sort.
2026 DBIR Results and analysis 33

However, there are almost 800 OT-
adjacent incidents we have recorded
this past year on NAICS 21 (Mining,
Quarrying, and Oil and Gas Extraction) Asset categories52
and NAICS 22 (Utilities), which may
give some insights on how these critical Server: a device that performs functions of some sort
sectors are being impacted in the
supporting the organization, commonly without end-user
threat landscape.
interaction. This is where all the web applications, mail services,
On the topic of OT-adjacent networks,
file servers and all that magical layer of information is generated.
there is one specific threat we would
If someone has ever told you “the system is down,” rest assured
like to point out based on mass internet
scanning and network telemetry around that some Servers had their Availability impacted. Servers
end of life (EOL) internet-facing cellular are common targets in almost all of the attack patterns, but
routers in NAICS 21 and 22 companies. especially in our System Intrusion, Basic Web Application
Those EOL devices are either vulnerable
Attacks, Miscellaneous Errors and Denial of Service patterns.
to configuration oversights—such as
default passwords in internet exposed Person: the folks (hopefully) doing the work at the organization.
management interfaces—or unpatched
No AI chatbots allowed. Different types of Persons will be
publicly known vulnerabilities.
members of different departments and will have associated
Those devices were often put in place
permissions and access in the organizations stemming from
to enable Internet of Things (IoT)
their roles. At the very least, they will have access to their very
sensors and connectivity to remote
outposts and are being repurposed as own User device and their own hopes and dreams for the future.
operational relay boxes (ORBs) to be Person is a common target in the Social Engineering pattern.
used as proxies for threat actor attack
campaigns.50 For example, our internet User device: the devices used by Persons to perform their
scan analysis validated the existence work duties in the organization. Usually manifested in the form
of between 45,000 and 50,000 EOL of laptops, desktops, mobile phones and tablets. These are
wireless modem devices with a publicly
common targets in the System Intrusion pattern but also in the
accessible ACEmanager interface
Lost and Stolen Assets pattern. People do like to take their little
between the months of June and
October of 2025. computers everywhere.
These are not easy-to-replace devices Network: not the concept, but the actual network computing
even for the most well-intentioned
devices that make the bits go around the world, such as routers,
organizations, and that makes network
telephone and broadband equipment, and some of the traditional
segmentation one of the simplest
solutions to help mitigate the issue in-line network security devices, such as firewalls and intrusion
ahead of a potential replacement of detection systems. Hey, Verizon is also a telecommunications
the EOL modems. Recent technologies company, OK?
such as 5G network slicing51 and private
mobile networks would be something Media: precious distilled data in its most pure and crystalline
worth taking a look at if this is a scenario form. Just kidding, mostly thumb drives and actual printed
that concerns your organization.
documents. You will see the odd full disk drive and actual
physical payment cards from time to time, but those are
not common.
50. This repurposing of assets to attack other victims is referred to in VERIS as a Secondary actor motive.
51. What if your cell tower acted like a network switch full of virtual local area networks (VLANs), or more
accurately virtual wide area networks (VWANs)?
52. verisframework.org/assets.html
2026 DBIR Results and analysis 34

VERIS Attributes
We’ve covered the who, how and what Because we define a breach as any Figure 38 looks at how Attributes
of data breaches; now it’s time to incident where Confidentiality is were affected across all incidents in
examine the “so what” of the incidents. compromised, every case labeled as this year’s dataset. 82% of incidents
The Attributes capture what impact an a “breach” in this report includes at showed confirmed data disclosure—
incident actually had on the Asset and least some form of data disclosure. But meaning someone who shouldn’t have
are rooted in the well-known CIA triad: depending on what happened, Integrity access either viewed or downloaded
Confidentiality, Integrity and Availability. and Availability can easily get pulled into confidential information. Integrity took
In plain terms: Did the attack expose the mess, as well. A single event can leak a hit in 64% of incidents, ranging from
data, alter the asset in some way, take data, corrupt records and knock systems phishing campaigns that manipulate
the asset offline or encrypt it—or some over, all in one go. For more information, users into clicking malicious links to the
combination of all three? please see the definition of each in unauthorized installation of software on
the callout. victim assets. Availability was impacted
in 53% of incidents, driven by events
such as successful DoS attacks or
ransomware that led to the encryption of
the victim’s data, leaving systems offline
or their contents unusable.
Attribute categories53
The share of incidents in which the
Interruption variety of availability was
Confidentiality: refers to limited observation and disclosure of affected rose significantly in this year’s
report. Two main factors are at play here.
an asset (or data). A loss of confidentiality implies that data was
First, VERIS is not static—the schema
actually observed or disclosed to an unauthorized actor rather
evolves as attack types change and as
than endangered, at-risk or potentially exposed (the latter fall we refine how we capture incident data.
under the attribute of Possession or Control54). Short definition: Historically, ransomware was primarily
limited access, observation and disclosure. coded under the Obscuration variety of
availability, since the data was encrypted.
Integrity: refers to an asset (or data) being complete and We did not consistently capture the
unchanged from the original or authorized state, content and Interruption aspect, or in other words,
the system downtime that often
function. Losses to integrity include unauthorized insertion,
accompanies a successful ransomware
modification and manipulation. Short definition: complete and
attack. This year’s coding more fully
unchanged from original. reflects that operational disruption.
Second, we are seeing (and coding)
Availability: refers to an asset (or data) being present,
more large-scale ransomware outages,
accessible and ready for use when needed. Losses to availability such as the Apr 2025 incident affecting
include destruction, deletion, movement, performance impact Marks & Spencer.55 In that case, online
sales, stock tracking and reordering,
(delay or acceleration) and interruption. Short definition:
and even the electronic monitoring
accessible and ready for use when needed.
of refrigeration was disrupted for
weeks, resulting in an estimated
£300 million in losses from
prolonged outages.
53. verisframework.org/attributes.html
54. en.wikipedia.org/wiki/Parkerian_Hexad
55. blackfog.com/marks-and-spencer-ransomware-attack
2026 DBIR Results and analysis 35

Naturally, these high-impact events
exert quite an influence on the dataset
and help push the overall percentage
of incidents involving the Interruption
variety of availability upward.
Figure 39 lays out the top data varieties
in breaches, and Internal data is the
most commonly stolen at 67%. That’s
not exactly a head-scratcher when you
remember that “Internal” mostly means
emails, plans and reports—the kind of
material you’d expect to be lying around
once an attacker strolls in via stolen
credentials or an unpatched vulnerability.
It would almost be more surprising if they
didn’t take a peek.56
Credentials appeared in 28% of
breaches and are relatively self-
explanatory—and entirely on brand—
given the password habits of many
organizations, as we’ve been lamenting Figure 38. Attributes in incidents
(n=31,850)
for 19 years.
Personal data (names, addresses and
phone numbers) was taken in 23%
of breaches, with sensitive personal
information, such as Social Security
numbers getting compromised in 1.7%
of breaches.
In short, the data shows that once
attackers are inside, they can (and do)
go in many directions in an organization’s
environment, and whether they are
looking for something specific or just
looting as they go, much of the data
in their path may be at risk. Between
the persistent headache of stolen
credentials and ever-rising cost of
operational downtime, the “so what” of
an incident seems to be getting more
expensive by the year. Perhaps the
takeaway is that you should not only be
concerned about what they will see but
also what they may break.
Figure 39. Top Data varieties
compromised in breaches (n=19,538)
56. Sadly, the adage does not say “Curiosity killed the criminal.”
2026 DBIR Results and analysis 36

Incident
Classification
Patterns
/03

Introduction
After watching case after case cross Using that structure, we arrive at seven
our desks, it’s hard to ignore that most Incident Classification Patterns that
security incidents are essentially reruns you will see referenced throughout
of the same plot, with only the occasional this section. Each of the pattern sections
ad-lib by the attackers. The same traits will include the CIS Security Controls57
often kept appearing together, and relevant to them.
those recurring combinations gave us
Returning readers may also notice
just enough structure to tame the chaos
some editorial decisions about what
into a sensible set of categories. Since
earns a full discussion versus what is
most people find it easier to reason
summarized at a glance. Certain patterns
about complex ideas when they can be
are remarkably consistent from year to
placed into clearly labeled containers,
year, both in terms of frequency and in
those Incident Classification Patterns
the defenses that matter most. In those
became our organizing framework—and
areas, the story does not change much:
they have remained with us ever since,
The same tried-and-true practices often
bolstered along the way by updated
continue to have the greatest impact,
machine learning models that handle
and the data does not warrant pages of
much of the classification work.
new commentary. Where the data does
These patterns are still the primary lens surprise us through sharp increases,
we use to group incidents that share notable declines or meaningful shifts in
similar characteristics into categories how attacks play out, you will see those
that are easier to understand, explain changes called out and examined in
and recall. They are grounded in the more detail in the pages that follow.
4As of VERIS—Action, Actor, Asset and
Attribute—which together capture how
something happened, who was involved,
what was affected and in what way.
Figure 40. Patterns over time in breaches (n for 2026 dataset=22,624)
57. cisecurity.org/controls
2026 DBIR Incident Classification Patterns 38

Figure 41. Patterns over time in incidents (n for 2026 dataset=31,860)
Lost and
Frequency 525 incidents, 88
with confirmed
Stolen Assets
data disclosure
Threat actors Internal (88%),
Summary External (13%),
Multiple (1%)
This year, we saw a sharp uptick in the (breaches)
number of incidents involving Lost and
Stolen Assets. However, 82% of those Actor motives Financial (79%–
were considered breaches in the 2025 100%) (breaches)
report, and in this year’s report, that
number is only 17%. The fact that the Data Personal (96%),
number of confirmed breaches this compromised Internal (43%),
year is so much lower than the number Other (21%),
of incidents may be attributable in part Sensitive
to the victim organization being unable Personal (18%)
to confirm if the data on the asset (breaches)
was accessed.
What is the same?
Personal data remains the primary
data type at risk in these cases. This
pattern remains largely one of insiders
making mistakes and losing track of their
devices, that being roughly four times
more likely than the assets in question
“growing legs” and wandering off with
the help of financially motivated thieves.
2026 DBIR Incident Classification Patterns 39

System
Intrusion
Summary Frequency 14,309 incidents,
13,758 with
Threat actors are leveraging trusted confirmed data
applications, such as Remote Monitoring disclosure
and Management (RMM) software,
stolen credentials and exploits to Threat actors External (100%)
monetize their access via Ransomware. (breaches)
Actor motives Financial (88%),
What is the same?
Espionage (12%)
Ransomware continues to be the (breaches)
driving force behind the growth of
System Intrusion. Data Internal (93%),
compromised Credentials
(26%), Other
(20%), Secrets
(13%) (breaches)
Figure 42. Top Action varieties in
System Intrusion breaches (n=12,006)
While a good number of our breach Intrusive
To a lesser extent, we see the more
patterns include some degree of
techniques general lateral movement techniques,
intrusion being inflicted on systems
such as Scan network and the ever-
of one sort or another, this pattern
popular Password dumper, being used in
gets its name from the more complex Figure 42 describes the top Action
order to find and extract credentials from
and involved breaches. In these varieties for the System Intrusion
compromised systems. Look forward to a
cases, determined external actors pattern. They provide a demonstrable
longer discussion of privilege escalation
are leveraging a combination of cross-section of what types of attacks
techniques—and their mitigations—later
Malware (and other software) and their defenders are up against.
in this section.
knowledge of Hacking techniques to
Unsurprisingly, Ransomware is at the
compromise our best-guarded data. Even though the actions themselves
top of the list and is seen in 77% of the
This pattern has been our top breach are in line with previous reports, the
breaches in the System Intrusion pattern.
pattern since 2022 and currently vectors used to achieve them show
As we have pointed out in previous
accounts for 60% of our breaches. It is some interesting variation from last
reports, these attacks represent the
difficult to overstate the contribution that year. In Figure 43, we see a certain
main method of monetization used by
the growth of Ransomware-like attacks degree of evolution in tactics, with a
criminals in this pattern. Conversely, we
has made to this pattern over the last growth in targeting Web applications
see more of an equal split in the common
few years.58 and Desktop sharing software. This can
initial access vectors Use of stolen creds
be partially attributed to more exploited
and Exploit vuln (both at 39%).59
vulnerabilities against these types of
services, while VPN maintains a similar
level as last year, around 16%. It’s worth
noting that those vectors are also prime
targets for credential abuse-related
actions, and that contributes to their
58. We wonder how future cybersecurity history will refer to this era. We suggest the Ransoming Twenties! lasting presence over the years.
59. It’s worth checking out our discussion of initial access vectors this year in the “Results and
analysis” section.
2026 DBIR Incident Classification Patterns 40

Unapproved
admin(ware)
One of the key things attackers enjoy
doing is controlling a system remotely,
which coincidentally is also something
most administrators are also fond of.60
Unfortunately, this coincidence works
against our established technology and
security infrastructure strategies.
Figure 43. Select Action vectors in System Intrusion breaches (n for 2026
In many cases, attackers leverage the dataset=6,678)
typical hacker-style toolkit while also
bringing in a C2 framework to manage
their remote persistence agents on
victim systems and to carry out activities
such as dumping passwords and
scanning local networks.61
However, Figure 44 presents a clear
increase in threat actors leveraging
legitimate RMM software to orchestrate
their attacks. This year shows a sharp
increase in the prevalence of those
techniques, with a relative growth of
Figure 44. Select Malware varieties over time in System Intrusion breaches (n for
240% over the previous year. When
2026 dataset=10,828)
coupled with the 27% decrease of the
Backdoor or C2 action, it solidifies the
belief that defenders have more than a The invisible First, the median amount of ransom
few war stories to share relating to these payments to threat actors has been
types of scenarios.62 hand of the in decline over the past two years, as
demonstrated by Figure 45. We want to
Those tools, while not chock full of ransom market
bring specific attention to the fact that
hacking scripts, do provide actors with
the medians shown in this Figure for
a remote session that they can easily
Those who read the DBIR regularly 2024 and 2023 are different from the
leverage and deploy to an environment.
are no doubt weary of being told how ones we published in the 2025 DBIR.
They often have the added bonus
Ransomware has continued to grow This is because we have added several
of not requiring the actor to set up
over the past few years. This year’s new data contributors who conduct
additional infrastructure. Instead,
growth has not been as dramatic as last ransom payments, negotiations and
they are conveniently included in the
year (for which we are grateful), but in threat actor crypto wallet tracking.
application and network whitelists
2025, 48% of all the breaches analyzed Adding these new data sources to our
of the organization deploying them.
had a Ransomware action involved, long-standing partnership with the
At the end of the day, what is a
as discussed previously in the “VERIS FBI Internet Crime Complaint Center
threat actor but an unapproved
Actions” section of this report. Even (IC3),64 who got us started on this whole
(and malicious) administrator?63
with this continual growth, there’s an analysis of ransom impact in 2019, gives
opposing trend we have been reporting us a better view into areas where we
around the decrease in the success previously had lower visibility.
of the monetization of Ransomware
payments. This trend manifests in two
important ways in our data.
60. They also enjoy long walks on the beach. Away from computers.
61. We wish they would pick better hobbies.
62. Maybe buy them a drink and let them regale you with their tales from the cyber trenches when
next you meet.
63. Could they at least have the decency to pick up a couple of tickets and solve some problems
while they’re in there? No, we didn’t think so.
64. ic3.gov
2026 DBIR Incident Classification Patterns 41

Setting aside the DBIR dataset’s version If companies are paying less Smoke and mirrors
of inside baseball, the takeaway is frequently—even if they have encrypted
in ransomland
that our sample size has tripled or assets—then the recent attack trend
quadrupled, depending on the year.65 In of attempting to inflict the maximum
spite of this increase in data volume, the business interruption in order to put a Gaining an accurate grasp of the scale
downward trend in the median amount greater time pressure on victims makes of the Ransomware threat has been
if ransom paid observed from 2023 to even more sense. an ongoing challenge for the industry.
2024 has remained consistent even The DBIR’s generalized approach has
Our dataset reveals a market in
with the new data sampling,66 and it largely been to focus on a variety of
decline, albeit a slow decline, where
has continued from 2024 to 2025. This different sources and combine them so
there is rampant commoditization
constitutes relatively strong evidence that the biases and limitations can iron
and the numerous actors involved are
to support the claim that the downward themselves out across these sources.
desperately trying to scale to cover their
trend may be real.
margin compression. The good news However, the often public nature of a
Adding to this finding, Figure 46 here is that the margin compression ransomware attack and the way the
shows that the percentage of does not only arise from threat actor groups seem to have a constant need
organizations that are not willing to pay competition, but by improved defensive to advertise themselves as “reliable
the ransomware actors also increased adaptations and increased resilience of Ransomware as a Service providers”
last year—from 65% in 2024 to 69% the victims. For defenders wondering if complicates matters significantly.
in 2025. One notable finding from this their efforts are being successful, the There is a growing disconnect between
analysis is that the increase in “Not volume reduction of payments to threat what is being reported and the reality of
Paid” outcomes also occurred in cases actors may be one of those signs of what has occurred, in no small part due
involving encryption, rather than in data progress that we could measure. to threat actors reusing old breaches,
exfiltration events only. reposting breaches from other criminal
partners and making up breaches
out of whole cloth to help increase
their notoriety in the criminal world.
We’re beginning to think that these
cybercriminals might not be
entirely trustworthy.
To probe this a little further from
a different perspective, we cross-
referenced data from actor-disclosed
ransomware attacks with known actor
crypto-wallet payments to estimate how
many of the alleged victims actually pay.
After an excruciating amount of time
combining, mapping and connecting
all the different names, pseudonyms
and groupings, the analysis in Figure
47 shows that, based on the reviewed
dataset, the median percentage of
publicized victims that paid the ransom
per ransomware group is about 9%.
We cannot do end-to-end tracking
of victims due to the nature of the
anonymized data, but considering our
Figure 45. Distribution of loss due to ransom payment in 2025 (n for 2023=1,700— volume analysis, this sounds like a lot
each dot is 8.50 events) (n for 2024=2,027—each dot is 10.14 events) of work for little pay.67
(n for 2025=1,494—each dot is 7.47 events)
65. More data samples is a good thing. Ask any data person.
66. Previous analysis and hypothesis holding steady in a whole new data sample is an even better thing.
Ask any data person. Ask a different one than before to increase your sample size!
67. Which, as we all know, contributes to making Jack a dull boy
2026 DBIR Incident Classification Patterns 42

This result suggests publicized victim
records could potentially contain a
significant percentage of fabricated
entries, as the percentage of payments
is under the expected value. This is
made worse by the fact that victims
that engage and pay the ransom very
quickly sometimes are not publicized.
As a consequence, the total number
of publicized victims per group, which
serves as the denominator for these
calculations, excludes some of those
who actually paid the ransom. This
would, of course, skew the results.
This uncertainty complicates even
further a problem that was already
hard to solve. Policymakers and even
individual organizations need accurate
information on the impact of ransomware
to make better-informed decisions for
themselves or their constituents. One
of the paths forward involves creating
Figure 46.Percentage of ransomware cases where the ransom was not paid
a policy for mandatory reporting of
(n for 2025 dataset=400)
ransomware payments, which has been
adopted or is being studied by some
countries. The Department of Home
Affairs in Australia is one example,
and they have provided us with some
details of their reporting program on
the next page.
Regardless of the percentage of true
disclosures, all economic indicators point
to the need for threat actors to continue
to expand and cast as large a net as
possible to get a consistent payday. As
this trend of less organizations paying
these actors continues, we could end up
reaching some sort of saturation point,
or perhaps the actors will move toward
retirement with a change of heart and a
new perspective on their criminal ways.68
Figure 47. Distribution of ratio of publicized victims to confirmed payments (n=261)
68. And be arrested as soon as they step into a country with extradition agreements with Interpol
2026 DBIR Incident Classification Patterns 43

Infostealer to
ransomware
Ransomware and Cyber
pipeline
Extortion Reporting Regime
We are often forced to revisit a topic that
By Australian Department of Home Affairs we feel we were not able to do justice
to for various reasons (never let it be
The mandatory ransomware and cyber extortion reporting said that the DBIR authors are afraid of
regime commenced on 30 May 2025 under Part 3 of the Cyber beating a dead horse).69 A case in point
is the fact that infostealers as a threat
Security Act 2024. It requires entities to notify the Australian
have continued to persist and evolve
Government of any payments made in response to ransomware
even in the face of various actions taken
or cyber extortion incidents, with the aim of improving visibility by law enforcement. Therefore, we feel
of cyber extortion activity and reducing the profitability of these justified in retreading some old territory
criminal operations. on this topic.
Building on the previous year’s approach
The obligation applies to entities with an annual turnover of AUD
of analyzing the co-occurrence of
$3 million or more, as well as operators of critical infrastructure
infostealer credential leaks and
regulated under Part 2B of the Security of Critical Infrastructure ransomware, we expanded the
Act 2018. The requirement to report is triggered only when a dataset to include a wider collection
of ransomware victims from the two
payment has been made, and the report must be lodged within
previous years to identify if any of
72 hours of the payment.
them had infostealers or other types
of credential leaks prior to being
Implementation of this regime has commenced with an education
publicized as a ransomware victim. The
first approach. This focuses on helping businesses understand
analysis found that 27% of ransomware
their obligations through guidance materials and engagement victims had no associated infostealer
activities. From January 2026, we have continued to promote or credential leak occur within the year.
the new regime while moving toward a more mature regulatory But of the organizations that did, 50%
of those ransomware victims had a
posture, maintaining an emphasis on partnership and uplift as
credential or infostealer event occur
organizations adapt to the new requirements.
within 95 days prior to falling victim to
a ransomware attack. Figure 48 shows
the distribution of those events, with zero
being the day of publication of the victim.
69. Mostly looming deadlines, but more frequently the lack of the right research partner
2026 DBIR Incident Classification Patterns 44

By outsourcing the target acquisition,
ransomware operators are able to focus
on their skillset of lateral movement,
privilege escalation, deploying their
ransomware payload and, well,
potentially getting paid.
By examining offers made by these IABs,
we can get a general understanding of
the types of access they are offering
and the associated prices. There is
large diversity in terms of the different
Figure 48. Distribution of days where a credential leakage event occurred prior to access vectors to the environments,
ransomware (n=4,395)
everything from more traditional VPN
access to specific application servers.70
Figure 49 has a breakout of these types
In addition, it’s not just large
of connections across the last four
organizations that experience credential
years. Without much surprise, we see
leakage events in general. Small
that 44% of the connection types are
organizations represented in this
VPN, followed closely by some type of
dataset experienced a median of seven
remote desktop application (e.g., RDP,
credential leak events over the course of
RDPweb, VNC). Also interesting is the
the year, while larger organizations faced
inclusion of ProxyShell/ProxyLogon
around 20. Although not all of these
access, considering the majority of these
events mean that an organization is
credential offers were found to have
going to experience a ransomware event,
occurred two to three years after the
they can provide threat actors with an
vulnerability was disclosed, once again
easy entryway that can then be resold
reiterating the value of the long-tail of
to others.
our incomplete patching and mitigation
process to attackers.
Cost of access
One of the complex elements associated
with Ransomware is trying to pin down
a pattern across all the various groups,
as they rebrand more often than Silicon
Valley startups. Individual threat actor
groups are known to leverage multiple
distinct ransomware toolsets. Adding to
the complexity, when trying to determine Figure 49. Percentage of select known
connection types by IAB offerings
initial access, some ransomware
(n=876)
groups are simply purchasing already
compromised access from third parties
called Initial Access Brokers (IABs).
70. Wanting access to more than a single project management tool instance is clearly a hallmark of the
criminally insane.
2026 DBIR Incident Classification Patterns 45

When it comes down to the actual
value of these types of access, Figure
50 shows that regular, non-privileged
accounts were typically worth around
$700. Administrative accounts, however,
were worth almost double that, valued
at around $1,300 per account. The
DBIR’s function is not to provide
recommendations or suggestions to
threat actors, but we were expecting a
higher median price, to be honest.
Median analysis aside, the contrast
between a basic account and a
privileged one on the extreme end of the
distribution shows how much attackers
value these high-privileged accounts, as
they allow them to bypass one of the key
steps required for them to achieve their
missions: privilege escalation. There is a
section later in the report dedicated to a
deep dive regarding our observations on
privilege escalation.
Figure 50. Cost of IAB offerings per access level (n for Admin=453)
(n for User=1,008)
2026 DBIR Incident Classification Patterns 46

CIS Controls for Protecting accounts
consideration Account Management [5]
– Establish and Maintain an Inventory
of Accounts [5.1]
– Disable Dormant Accounts [5.3]
Protecting devices
Access Control Management [6]
Secure Configuration of Enterprise – Establish an Access Granting/
Assets and Software [4] Revoking Process [6.1, 6.2]
– Establish and Maintain a Secure – Require MFA for Externally-Exposed
Configuration Process [4.1] Applications [6.3]
– Establish and Maintain a Secure – Require MFA for Remote Network
Configuration Process for Network Access [6.4]
Infrastructure [4.2]
– Implement and Manage a Firewall on Security awareness
Servers [4.4]
programs
– Implement and Manage a Firewall on
End-User Devices [4.5] Security Awareness and Skills Training
[14]
Email and Web Browser
Protections [9]
– Use DNS Filtering Services [9.2]
Malware Defenses [10]
– Deploy and Maintain Anti-Malware
Software [10.1]
– Configure Automatic Anti-Malware
Signature Updates [10.2]
Continuous Vulnerability
Management [7]
– Establish and Maintain a
Vulnerability Management
Process [7.1]
– Establish and Maintain a
Remediation Process [7.2]
Data Recovery [11]
– Establish and Maintain a Data
Recovery Process [11.1]
– Perform Automated Backups [11.2]
– Protect Recovery Data [11.3]
– Establish and Maintain an Isolated
Instance of Recovery Data [11.4]
2026 DBIR Incident Classification Patterns 47

Social
Engineering
Summary Frequency 5,302 incidents,
3,814 with
Threat actors continue to largely confirmed data
leverage email-based phishing attacks disclosure
to compromise organizations; however,
these attacks are getting more complex
Threat actors External (100%)
as attackers are targeting mobile devices
(breaches)
and other unconventional vectors to
reach victims.
Actor motives Financial (86%),
Espionage (25%)
What is the same?
(breaches)
Email is still the preferred attack
Data Other (56%),
vector for the majority of Social
compromised Internal (51%),
Engineering breaches.
Credentials
(39%), Secrets
(31%) (breaches)
Figure 51. Top Social vectors in Social
Engineering breaches (n=3,777)
Social Engineering and phishing via The social quo When we’re looking at data from
email have been more or less considered email security gateways, we see
synonymous in the defender’s playbooks similar breakdowns (Figure 54), with
This pattern is mainly focused on the
for some time now. For those of us who 80% of the attacks blocked being
attacks that leverage deception to
have been around long enough, we still plain phishing, 10% being emails with
accomplish some specific objective, be it
have memories of the early days of malware, 5% being attempts of getting
deploying malware, collecting credentials
AOL and our first email accounts, the victim to call back to the attacker
or transferring money to the actor’s bank
along with the desperate pleas from and 3% consisting of Business Email
account. The common element in this
rich princes in foreign lands in need of Compromise-style attacks such as
pattern is that individuals are targeted
help from someone trustworthy whose attackers trying to get the victim to
in the attack.
only qualifications were owning an update an existing bank account (or
email address.71 Typically, in these types of attacks, the register a new one) ahead of a wire
first step against the victim is the Social transfer, usually by pretending to be
While some things have changed over
action, as it is what provides the attacker that user by leveraging the historical
the course of the last few decades,
access to an organization’s environment. email chain. Those last two are actually
some have also stayed the same, with
Figures 51 and 52, respectively, show good examples of Phishing followed by
Social Engineering continuing to be one
the Social action varieties (types of another social action, Pretexting, due to
of the most common types of attack
attacks) and vectors (the distribution the synchronous nature of the attack. If
resulting in breaches since 2018. The
methodology). As expected, we see there is someone on the other side of
Social Engineering pattern shows up as
Phishing and Email as the primary the proverbial line interacting with
our third most common breach pattern,
methods used. you to do something you shouldn’t,
representing 16% of breaches. But like
that’s Pretexting.
everything else in cybersecurity, change
and evolution are inevitable.
71. And a bank account
2026 DBIR Incident Classification Patterns 48

When examining how much these mobile
devices are getting phished via SMS,
as Figure 53 shows, we find that the
median amount per year of those SMS-
based phishing campaigns targeting
mobile devices in large organizations is
48 (12 for smaller organizations). While
these numbers don’t look eye-poppingly
large,72 they do demonstrate an existing
and present threat that can bypass
traditional approaches to phishing
mitigation by reaching directly to the
users through their mobile devices.
It’s important to point out that those
detections were only visible because
those are managed devices—either
corporate owned or with some form of
mobile device management software.
If your employees are using purely
unmanaged personal devices to perform
organizational duties, this can represent
Figure 52. Top Social actions in Social Figure 54. Median percentage of
Engineering incidents (n=5,217) a risky gap in your visibility. Email attack types by month
(n=3,709,045,972)
Multipronged
social approach
Much like how advertisers try to grab our
attention through a variety of different
methods—web applications, emails, text
messages and airplane banners at the
beach—so do attackers. In fact, 41% of
our Social Engineering breaches involve
social vectors other than just Email. In
this section, we’ll look at the types of
attacks that go beyond just the Email
vector and explore the other methods
that attackers are leveraging to target
our employees and the implications to
our defenses.
When we’re looking at our incident data,
we see that about a fourth of our social
action vectors come from either Social
media or Phones, which really represents
the widening of the net that attackers
Figure 53. Annual number of mobile device Phishing attempts detected by org size
are leveraging to snare our users.
(n=12,363—each dot is 103.025 attacks)
72. We’d argue that being targeted by such a campaign every eight calendar days in the year is worth
looking into.
2026 DBIR Incident Classification Patterns 49

The caveat on this analysis should
become apparent when you look at the
sample sizes. Phishing simulation is a
well-established business practice, and
we have a handful of leading companies
in this space as data contributors. On
the other hand, we struggled to find
companies doing simulations of voice-
and text message-based campaigns,
which leads to this small-ish sample
size. We hope that, for the 2027 DBIR,
we will be able to collect more data as
additional companies that offer these
kinds of services want to participate in
Figure 55. Distribution of success rate of Email vector-simulated social attack this research.
campaigns (n=8,395—each dot is 209.88 campaigns)
Regardless, the result suggests that
different strategies of training and
simulation are needed to mitigate the
risk of those “new” vectors. The more
involved Pretexting attacks on the rise
are also of a different nature to the
“send-message-and-hope-for-a-click”
Phishing attacks, as they are tailored to
appeal to the nature of the employees
being targeted.73 The takeaway reflection
here is this: How are users taught to
detect these unconventional social
engineering attacks? Could you detect
someone impersonating your help desk,
and by what means can your users be
reached on your devices?
Figure 56. Distribution of success rate of non-Email vector-simulated social attack
campaigns (n=35—each dot is 0.88 campaigns)
Aside from receiving sneaky links for The bottom line here is that social
users to click on, phones are also the attacks using phone-centric vectors—
perfect tool for voice phishing, which text messages, voice or the previously
is just another way of saying Social mentioned callback-focused emails—
Engineering over a phone call. Now, if are more successful in our dataset
you have been following along, this is than using the traditional Email vector
where we put our VERIS hats back on defenders are used to. While the
and reinforce that those are classified median click rate of email phishing
as Pretexting in our dataset, which has simulation campaigns is 1.4%, we see
seen a substantial increase in our initial the median rate of simulations on phone-
access vector analysis from last year. centric methods is closer to 2%, as
Regardless of the terminology, various demonstrated in Figures 55 and 56.
attackers have been leveraging these That is an increase of 40% in the median
means, by impersonating help desk click rate between those vectors.
agents or users needing a password
reset, with moderate levels of success.
73. What do you mean the help desk is not supposed to help someone, in some cases?
2026 DBIR Incident Classification Patterns 50

The (click)fix is in!
At this point, you have probably sworn
In the trenches
off of ever checking your email or
picking up your phone again. Don’t
One common breach structure we reviewed this year involves worry, threat actors have a Social action
combining multiple elements to make for a convincing scenario just for you! Welcome to the world of
Baiting, where attackers set up realistic
to request and obtain access to internal systems.
webpages, create online adverts, or
1. Attackers will create some fake type of IT emergency for compromise existing websites to get
users to download their malware via
users, for example, by signing them up for various spam
crafty webpages posing as downloads of
services, which results in the users getting bombarded with
legitimate tools and software. These can
suspicious emails. show up in a few different varieties, but
the main types that we’ve encountered
2. Fortunately for the users (and unfortunately for the
this year are the search engine
organizations), a “helpful” individual sends an external chat optimization (SEO) abuse downloads
request via Microsoft Teams74 claiming to be from the help and the ClickFix attack.
desk and offers to help if the users just share access to their
The ClickFix attacks are a newer twist
desktop systems. on an old tactic, where the malicious
webpages present themselves as a
3. With this access, the attacker is able to conduct the attack
CAPTCHA, which in itself is pretty
from the victims’ user devices while “troubleshooting” for familiar to any modern-day netizen.
the users.
For defenders, detecting those types of attacks can be very
challenging, as there’s no malicious code being executed, the
access point is via a messaging app that oftentimes by default
will allow external entities to send in connection requests and
the remote access usually leverages tools built into the operating
system and approved by the organization.
74. According to publicly available incident reports, Teams has been a very common vector along with
Quick Assist, but this does not preclude the involvement of other messaging systems.
2026 DBIR Incident Classification Patterns 51

However, there is a twist! This CAPTCHA Tactical Espionage
isn’t about solving some indecipherable
social action
scribbles or pressing a button but is
prompting the user to open up a terminal
window and paste a command into that When it comes to Social Engineering, it’s
terminal.75 Naturally, the command is clear that the APT Crowd is living up to
some malicious payload that promptly the title of persistent. About 25% of our
downloads actual malware onto Espionage-motivated incidents involve
the system. Social Engineering actions as part of the
attack path. Where these actions play
While this may seem obvious in a
out is through long-term interactions
controlled setting, these attacks are
and the development of rapport with
not reserved exclusively for use against
the targets.
non-technically savvy users. In practice,
attackers skillfully combine technical One such tactic these attackers
instructions with Social Engineering leverage is by weaponizing a job
to instill a sense of both urgency hiring process, such as attempting
and distraction. These psychological to recruit employees of the target
pressures are designed to bypass users’ organization as means of getting
typical caution, leading them to execute internal information. Alternatively, they
commands (in this case, press Ctrl-Alt-R may try getting the user to download
and then Ctrl-V) they would otherwise and troubleshoot a git repository that
recognize as a threat. happens to have malware embedded
in it. As our analysis on bring your own
Figure 57. Attack types detected at the When we examine attacks blocked at
device (BYOD) and infostealers in the
browser (n=8,498) the browser level (Figure 57), we
2025 DBIR shows, even on personal
find that these ClickFix attacks only
devices, it was relatively common for
represent about 2.7% of attacks, still
employees to have corporate account
being overshadowed by the traditional
credentials or information that is ripe to
phishing pages and malicious downloads.
be compromised. When it comes down
These attacks are interesting from the
to helping employees protect themselves
novelty perspective, but also for the
in situations like these, the focus
implications for defenders in how
should also be on promoting the same
they can detect and mitigate users
discerning sensibility at home in their
copying and executing commands
personal lives as they do at work.
from a webpage.
75. Be very careful which link you click in your web search if you are trying to install legitimate open-
source software.
2026 DBIR Incident Classification Patterns 52

CIS Controls for
consideration
Protect accounts
Account Management [5]
– Establish and Maintain an Inventory
of Accounts [5.1]
– Disable Dormant Accounts [5.3]
Access Control Management [6]
– Establish an Access Granting/
Revoking Process [6.1, 6.2]
– Require MFA for Externally-
Exposed Applications [6.3]
– Require MFA for Remote Network
Access [6.4]
Security awareness
programs
Security Awareness and Skills Training
[14]
Managing incident response
Incident Response Management [17]
– Designate Personnel to Manage
Incident Handling [17.1]
– Establish and Maintain Contact
Information for Reporting Security
Incidents [17.2]
– Establish and Maintain an
Enterprise Process for Reporting
Incidents [17.3]
2026 DBIR Incident Classification Patterns 53

Basic Web
Application Attacks
| Summary | Frequency | 3,217 incidents,  |
| ------- | --------- | ----------------- |
2,281 with
| Basic Web Application Attacks remain  |     | confirmed data  |
| ------------------------------------- | --- | --------------- |
| widespread and are typically driven   |     | disclosure      |
by stolen credentials and unpatched
vulnerabilities. While often low in  Threat actors External (100%)
| sophistication, they are highly effective  |     | (breaches) |
| ------------------------------------------ | --- | ---------- |
and frequently lead to credential theft,
internal data exposure and further
|                        | Actor motives | Financial (74%),  |
| ---------------------- | ------------- | ----------------- |
| compromise of systems. |               | Espionage (23%),  |
Ideology (3%)
(breaches)
What is the same?
|     | Data  | Credentials  |
| --- | ----- | ------------ |
The Use of stolen creds continues its
historic run in this pattern, showing  compromised (52%), Internal
| the more things change, the more they  |     | (48%), Other    |
| -------------------------------------- | --- | --------------- |
| remain the same.                       |     | (33%), Secrets  |
(15%) (breaches)
Figure 59. Top Action varieties in Basic
Web Application Attacks breaches
(n=2,193)
The Basic Web Applications Attacks
pattern is, as the name suggests,
relatively straightforward. Rather
than the intricate, movie-style heists
orchestrated by brilliant criminal
masterminds, it’s closer akin to “oh, they
left the door open” on the spectrum of
attack complexity. Figure 58 shows us
that it has been trending down in favor
of the more complicated System
Intrusion. This trend suggests that
defenders may be successfully raising
the bar, thereby making attackers work
harder (or attackers are leveraging
their initial access to achieve more
Figure 58. System Intrusion and Basic Web Application Attacks breaches over time
(n for 2026 dataset=22,624) complex objectives).
2026 DBIR Incident Classification Patterns 54

Once again, the Use of stolen creds is CIS Controls for
the top action in this pattern (Figure 59).
How attackers obtain these credentials consideration
is often unknown. They may be coming
from phishing, infostealers or from data
exposed in prior breaches and later Mitigation efforts against
packaged and sold on the dark web.
stolen credentials
However they acquire them, they are
making good use of them in this pattern.
Account Management [5]
We also saw a rise of the Exploit vuln – Establish and Maintain an Inventory
action this year due to several large of Accounts [5.1]
cases involving software vulnerabilities – Disable Dormant Accounts [5.3]
that were left unpatched and later
exploited—either in an organization’s Access Control Management [6]
own infrastructure or that of a partner. – Establish an Access Granting/
Revoking Process [6.1, 6.2]
Also making a debut this year is
– Require MFA for Externally-
Password dumper. It is not uncommon
Exposed Applications [6.3]
for the perpetrators of this type of
– Require MFA for Remote Network
attack to harvest additional credentials
Access [6.4]
for use in further attacks or to simply
monetize them. It is closely followed by
Mitigation efforts against
Brute force,76 which is an excellent way
vulnerability exploitation
of breaking the passwords when you
cannot steal them.
Continuous Vulnerability
The number of incidents and breaches Management [7]
classified under this pattern rose – Establish and Maintain a
significantly compared to 2025’s report. Vulnerability Management
This could mean the number of incidents Process [7.1]
increased, but it could also mean our – Establish and Maintain a
partners had improved visibility into the Remediation Process [7.2]
low-effort attacks that typically fall into – Perform Automated Operating
this pattern. As always, it is difficult to System Patch Management [7.3]
attribute such changes to a single cause – Perform Automated Application
when looking at our data. Patch Management [7.4]
We observed an increase in financially
motivated actor breaches compared
to last year, while Espionage-related
breaches declined. Incidents driven
by Ideology, however, remained
fairly consistent.
76. They are the Brute Squad!
2026 DBIR Incident Classification Patterns 55

Miscellaneous
Errors
Summary Frequency 1,757 incidents,
1,750 with
Employee mistakes—especially confirmed data
Misdelivery and Misconfiguration— disclosure
remain a persistent and significant
cause of data breaches, often exposing Threat actors Internal (100%)
personal data. Better access controls, (breaches)
monitoring and safeguards against
common human errors are critical to Data Personal (98%),
reducing these incidents. compromised Internal (16%),
Other (8%), Bank
(7%) (breaches)
What is the same?
Errors were the cause of breaches
slightly more often than last year.
Misconfiguration and Misdelivery
continue to be the primary issues
organizations are experiencing in terms
of the kinds of errors their employees
are making.
Figure 60. Top Action varieties in
Miscellaneous Errors breaches (n=1,719)
Better to ask We witnessed some movement in the Misconfiguration errors, by contrast,
top three Errors for this pattern this year. occur when someone deploys a data
forgiveness?
Figure 60 illustrates that Misdelivery, store on the internet without applying
Misconfiguration and Loss were the appropriate access controls. These are
There is an old adage that it is better to most common, with Publishing errors not most commonly discovered by security
ask forgiveness than permission, but it far behind. Last year, Publishing errors researchers, who then attempt to make a
doesn’t really age well when it comes were in third place. For those new to the notification if they can determine whose
to the kinds of mistakes we repeatedly report, Publishing errors occur when data it is. What we don’t know is how
observe in this pattern. Some industries private data is mistakenly placed on a often other, less civic-minded people
(we’re looking at you, Healthcare) have public-facing server. These are typically have encountered the same data, made
had this pattern in their top three for discovered when search engines a copy and quietly slipped away. The fact
as long as we have been tracking it. index the content and customers that Misconfiguration remains among the
Surely the organizations (and the people searching their own name receive top errors over time is rather concerning.
whose data has been compromised) are an unpleasant surprise.
rather tired of people doing things in the
name of expediency (or convenience)
or other reasons that result in a breach.
Forgiveness is generally not a concept
recognized in most data breach
disclosure laws.
2026 DBIR Incident Classification Patterns 56

Figure 61. Select Actor varieties over time in Miscellaneous Errors breaches
(n for 2026 dataset=861)
Misdelivery errors occur when data CIS Controls for Secure infrastructure
is delivered to the wrong recipient.
While we still see this happening with consideration Continuous Vulnerability
documents, particularly for those Management [7]
organizations that do large mass – Perform Automated Vulnerability
mailings, it also occurs frequently in Control data Scans of Externally-Exposed
electronic form, as well. It is very easy Enterprise Assets [7.6]
to make this type of mistake—does your Data Protection [3]
organization have a way of intercepting – Establish and Maintain a Data Application Software Security [16]
these kinds of errors before there is a Management Process [3.1] – Use Standard Hardening
full-blown data breach? – Establish and Maintain a Data Configuration Templates for
Inventory [3.2] Application Infrastructure [16.7]
One useful step would be to identify
– Configure Data Access Control Lists – Apply Secure Design Principles in
who most often causes these Errors in
[3.3] Application Architectures [16.10]
your organization. We can see in Figure
– Enforce Data Retention [3.4]
61 that Developers, System admins and Train employees
– Securely Dispose of Data [3.5]
End-users top our list. Certainly End-
– Segment Data Processing and
users will be more numerous at any Security Awareness and Skills Training
Storage Based on Sensitivity [3.12]
organization, but Developers and System [14]
– Deploy a Data Loss Prevention
admins tend to have access to higher – Train Workforce on Data Handling
Solution [3.13]
volumes of data and privileged access, Best Practices [14.4]
which increases the potential impact of – Train Workforce Members on
this type of mistake. Causes of Unintentional Data
Exposure [14.5]
Organizations that want stronger
access controls in place may want
Application Software Security [16]
to limit who has access to their most
– Train Developers in Application
critical data and place safeguards and
Security Concepts and Secure
procedures accordingly.
Coding [16.9]
2026 DBIR Incident Classification Patterns 57

Privilege
Misuse
Summary Frequency 1,141 incidents,
766 with
Intentional insider misuse is less confirmed data
common than External attacks, but disclosure
privileged access, convenience-driven
policy violations, AI data leakage and Threat actors Internal (100%),
fraudulent employee activities are External (1%),
growing insider-related risks that Multiple (1%)
organizations must monitor closely. (breaches)
Actor motives Convenience
What is the same?
(60%), Financial
Financially motivated insiders continue (33%), Espionage
to steal data to benefit them down the (4%), Grudge
road. Whether it is taking it to another (4%), Fun (2%),
employer or starting a competing Other (2%)
business, these are notoriously difficult (breaches)
to detect.
Data Personal (60%),
compromised Other (35%),
Secrets (27%), Figure 63. Top Actor varieties in
Internal (25%) Privilege Misuse breaches (n=89)
(breaches)
As Figure 62 illustrates, the Privilege
Misuse pattern has never been a
dominant driver of data breaches.
Organizations generally face far more
risk from External actors than from
their own employees. This doesn’t mean
insider malice is insignificant, and when
it occurs, the impact is rarely trivial.
However, your own people are typically
much more likely to lose an asset or
make a mistake than to intentionally
abuse their access.
Misuse breaches have declined over the
past two years, after peaking at nearly
8% of breaches in the 2024 report.
In this year’s report, they account for
less than half that figure at just under
Figure 62. Select patterns over time in Privilege Misuse breaches (n for 2026 4% of breaches. By comparison, the
dataset=22,624) Miscellaneous Errors pattern represents
nearly 9% of breaches this year.
2026 DBIR Incident Classification Patterns 58

Some of this can be attributed to
changes in our contributor base and the
degree to which they can detect and
report malicious insider breaches. Even Coercion of high-risk employees
so, the Privilege Misuse pattern has
remained a relatively minor player overall. Over the years, many of our data contributors in DLP and
behavioral engineering have shared a very clear datapoint:
The trust gap Policy violations are rarely evenly distributed. There are always
“troublemakers” inside organizations, in the sense that many
Now that we have established that these
policy violations are often concentrated in a small group of
types of breaches occur less frequently
individuals.77 Even when unintentional and accidental, there
than some might think, when they do
occur, their impact can be exceptionally remains a small subset of individuals who account for a
damaging to organizations. This leads us disproportionately high level of risk.
to the obvious question: Who do we see
perpetrating serious violations against However, one under-explored topic around very high-risk
their employers? In most cases (54%), individuals is their susceptibility to coercion-based collaboration
it is your average End-user (Figure with External actors. Coercion tactics often require a blackmail
63). However, we also see Developers
target, and recent technological developments, along with
and System admins being involved—
the availability of personal information that might make for
which is especially concerning given
that these two account types tend to newsworthy topics, have made it much easier to obtain leverage
have higher levels of privileged access. against those high-risk individuals.
Finally, Managers are also sometimes
responsible for compromising data, and More to the point, research from one of our newest data
most frequently, these are financially contributors78 shows that across their installation base of almost
motivated and are intended to benefit
270,000 enterprise work computers, approximately 1 in 500
them at future employers.
employees accessed high-risk compromising materials on an
This year, we observed an increase in enterprise device.
the number of these breaches that had
Convenience as a motive. A common This includes content related to extremism, promotion of bodily
example is when an employee wants to harm or exploitative materials not appropriate for a workplace
work from home and emails company
environment. The existence of such compromising materials has
data to a personal account. That would
often been associated with an increase of how susceptible to
be a case where the person wasn’t
specifically acting with malicious intent— coercion an employee can be. If those employees have any sort
they wanted to keep working—but they of privileged access in your organization, their trusted access
clearly violated the data-handling policies
could become externally leverageable.
of their employer and caused a data
breach. We will be watching closely to Military and intelligence agencies have long incorporated
see whether this type of Convenience-
coercion-based insider risk mitigation procedures in their
related breach continues to become
environments. Given the documented increase we have seen
a trend.
of state-sponsored activity targeting the private sector, it is
definitely worth considering when iterating your organization’s
insider risk program.
77. A Misuse Pareto, if you will
78. NetClean has more details on their insights section at netclean.com/knowledge/insights-and-data.
2026 DBIR Incident Classification Patterns 59

Insider breaches can be very difficult
to detect in real time because they are
frequently using access legitimately
granted to them to perform their duties.
The question is whether your controls
can identify when these actors go
rogue. If you are unsure what this kind
of breach might look like, perhaps a
good starting point would be to begin
with the offboarding process for those
people with access to the most sensitive
data in your organization. For example,
triggering a simple activity review when
someone on that list resigns (or is let go)
may bring to light a breach that would
have otherwise remained undetected
until that data is misused later. This
simple control has caught numerous
breaches in our dataset.
DataGPT: gone,
Figure 64. Top non-malicious insider Figure 65. Select data types in
untrusted DLP event targets untrusted DLP events targeting
pilfered or
(n=4,280,149) generative AI tools (n=858,440)
transferred
When it comes to the provenance of the And it’s not just bots we have to be
Just as we can’t go through a report accounts being used on AI platforms, careful of. Even our portal to the internet,
without mentioning vulnerabilities and we find a similar type of breakout as the browser, is becoming increasingly
credentials at least 56 times, we’re also last year, with 67% percent of users more integrated with AI. We found
going to be banging the drums around using non-corporate accounts on this year that the average company
GenAI. Specifically, this section focuses their corporate devices to access AI had more than 15% of users with
on the possible exposure of our most platforms.80 These types of unaccounted unauthorized AI extensions installed
precious commodity, our data. The AI systems that contain corporate data on their browsers. One of the main
last few years could perhaps be best are sometimes referred to as “Shadow functions of these AI plugins is often to
described as having a blistering rate AI.” Much like Shadow IT,81 these collect and retain information about what
of adoption of this new technology, as systems exist outside of the control of the user is browsing for context, so if
now 45% of employees are considered the organizations and can represent a your corporate users are browsing your
regular users79 of AI on their corporate significant risk for data leakage. This internal sites, some of your non-public
devices, up from 15% that we reported issue has become so prevalent this year data might be getting vacuumed up
last year. However, while the user that it is now the third most common
adoption is growing, it’s unclear if non-malicious insider action detected When it comes to where our data goes
security is either playing whack-a-bot or in our DLP service datasets in 2025 and whose probabilistic model gets to
driving and informing these decisions as (Figure 64), a fourfold increase from pontificate on it, we found that the most
part of a comprehensive AI usage policy. last year. common data submitted to external AI
models was source code, by a large
margin (Figure 65), followed by images
and other types of structured data.
79. In our dataset, that means access to an AI platform at least once every 15 days.
80. Last year, that percentage was 72%.
81. And unlike Shadow the Hedgehog, even though he also ended up outside of the control of
his organization
2026 DBIR Incident Classification Patterns 60

In 3.2% of DLP events, we even found CIS Controls for
research and technical documentation
being uploaded to untrusted and consideration
unauthorized AI systems, possibly
leaking key internal research. As if the
source code part was not enough, you Manage access
now have potential intellectual property
walking out the door. Secure Configuration of Enterprise
Assets and Software [4]
Considering the amount of data that
– Establish and Maintain a Secure
these models consume, process and
Configuration Process [4.1]
log, how comfortable should we be
– Manage Default Accounts
with uploading our secret recipes and
on Enterprise Assets and
key intellectual property data to these
Software [4.7]
unauthorized third parties? Especially
considering the increasing number of
Account Management [5]
systems, servers and hands that reside
– Disable Dormant Accounts [5.3]
between your user and the actual
– Restrict Administrator Privileges
model.82 Just because there’s a new toy
to Dedicated Administrator
to play with doesn’t mean we should
Accounts [5.4]
ignore decades of data governance and
third-party risk management practices.
Access Control Management [6]
Roko’s basilisk83 is not real and it cannot
– Establish an Access Granting
hurt you!
Process [6.1]
– Establish an Access Revoking
Process [6.2]
82. If it wasn’t clear, this is a rhetorical question.
83. en.wikipedia.org/wiki/Roko%27s_basilisk
2026 DBIR Incident Classification Patterns 61

Denial
of Service
Summary Frequency 5,514 incidents, 3
with confirmed
DDoS extremes continue to increase as data disclosure
organizations face erratic burst attacks
year-round, with the median breached Threat actors Internal (100%)
entity contending with 17 distinct attacks (breaches)
throughout the year.
What is the same?
DDoS attacks continue to be one of the
top incidents targeting a wide variety of
different industries.
Figure 66. Top victim industries in DDoS
incidents (n=5,513)
As our world continues its movement Down but not out Extreme growth
toward interconnectedness (and
possibly the singularity), the systems
The first step into our analysis is simply Channeling our inner 90s kids, rocking
and networks that connect us become
to understand who is being impacted our skateboards and inexplicably calling
increasingly more important every day.
by DDoS (or who knows that they were everyone “Brah,” we wanted to look a bit
While many of the newsworthy outages
targeted), as Figure 66 shows. What into the extremes of the DDoS dataset.
this year were due to DoS accidents,
we see are the same industries that But to first understand the extremes
rather than DoS attacks, it doesn’t
we’ve seen for the last couple of years, (what we’re really talking about are the
mean that these threats haven’t been
just with some shifting in terms of rank outliers), we need to understand the
a consistent and thorny issue for
ordering. While in the 2025 report there things that are essentially the baseline in
many organizations.
was a relatively large spike in DDoS this dataset. In comparison to previous
events targeting the government and years, there has been some light
the wider Public Sector, possibly due to jockeying in terms of the typical size,
hacktivism, they’ve settled back down to volume and duration of an attack. The
their normal spot near the bottom. On median size of an attack has fluctuated
the top, we continue to see that Finance, between 4.2 Gbps and 6 Gbps over
Professional Services and Manufacturing the last few years, with 50% of attacks
are the typical main targets, as they have lasting less than nine minutes.
been since 2022.
However, when we start to look at the
extremes of our dataset and focus on
the max values, we find a relatively large
growth in capability. Compared to last
year, the largest attacks increased by
198% in bits per second (BPS) and 156%
in packets per second (PPS).
2026 DBIR Incident Classification Patterns 62

We don’t normally spend too much time
discussing the outliers because they are
just that—outliers—but this growth in
capacity from the attackers shows that
they are continuing to build their abilities,
even if the majority of their attacks
tend to show similar characteristics as
previous years.
Syncing with
DDoS frequencies
One thing we wanted to understand
a bit more this year was about the
nature of the attacks. Not so much
what and how, but the frequency in
which organizations experience attacks
and what that might tell us in terms of
the nature of the adversaries who are
targeting via DDoS. What we did was
categorize organizations based on the
Figure 67. Distribution of time between attacks based on pattern (n=217)
time differences between attacks to
help determine whether attacks were
consistent, random or showed attributes
of the attacks in bursts. What we found is
that of the victim organizations, 2% had
attacks that were periodic and relatively
predictable, 40% of organizations
had attacks that showed up as bursts
of activity, and 57% of organizations
experienced attacks that occurred in
seemingly random intervals.
Figures 67 and 68 provide the
breakdown of the differences and
similarities that exist among our three
classes of DDoS victims. For the
victims that largely experience Bursty
(aggressive and frequent) types of
attacks, the median time between
attacks was about one day. This is a
pretty stark contrast to the Random
(no discernable patterns) organizations
that experienced about 14 days without
an event.
Figure 68. Distribution of number of different attack types (n=217)
2026 DBIR Incident Classification Patterns 63

In addition, over the course of the year,
our Bursty victims would face about 17
different attacks (with a median duration
of 24 minutes), while our Random victims
had a median of six events in the same
time period (also with a median duration
of 24 minutes).84 The higher end of the
distribution for duration is around 88
minutes for the 90th percentile and 101
minutes for the 95th percentile. The
question arises, “What would be the
impact to your business if your business
was affected?”
Lastly, when it comes down to the
types of DDoS attacks experienced,
organizations have to be able to mitigate
a complicated concoction of different
techniques. Attackers commonly target
organizations with at least 10 different
attack types tailored to different types
of network protocols and services over
the course of the year. For organizations
that experienced more Bursty styles of
attacks, 50% of victims experienced
at least 10 different types of attacks,
in comparison to the other attack type
victims experiencing only seven.
As attackers continue to build their
capabilities and capacity for their
attacks, we as defenders have
to maintain our footing and use
collaboration and partnerships to
counteract these actors.
84. Common durations aren’t super surprising to us as these different types of organizations are probably
being targeted by the same attack toolkits, just in different frequency.
2026 DBIR Incident Classification Patterns 64

The (AI) bots
are back in town.
GenAI in general, and agentic AI
specifically, can potentially bring
automation but also disruption to
markets and supply chains. The DBIR
can confirm that—as far as bandwidth
considerations and protection of
intellectual property are concerned—
the disruption is possibly already here.
Consequently, cybersecurity teams are
scrambling to automate handling the
surge of AI scanning bots, and AI-driven
traffic in general.
There are two main categories to be
found today: the AI crawlers that have a
similar function to the old search engine
crawlers and gather data for training and
fine-tuning of models and the AI fetchers
designed to act on a direct request from
users (or indirectly from AI agents) to
retrieve information to support a task. If
you are feeling too lazy to read a website
and you ask the model to summarize it
for you, the fetcher is there to gather
the information.
The traffic generated by these bots has
been growing significantly. Roughly 15%
of non-malicious bot traffic in Q3 2025
was related to AI bots, whereas our Figure 69. Relative growth of AI bot traffic over time
good old search engine crawlers were
responsible for 60% of the pie.85 Think
Figure 69 shows the surprising The next two, Digital Media Publishing
about that for a second. We have these
comparison of relative growth of all and Retail organizations—with growth
new types of bots that did not exist four
industries and the top three individually. rates between 45% and 48%—have
years ago, and that now represent as
During the reporting period, global traffic business models that depend on direct
much as one-quarter of the traditional
from AI crawlers and fetchers grew traffic and engagement, raising concerns
search engine crawler traffic.
21% month over month (MoM) across regarding content authority, attribution
And it keeps growing. With a bot traffic all observed industries, a 4% growth on and commercial impact.
dataset spanning May 2025 to Dec fetchers and a 32% growth on crawlers.
Managing this increased traffic will be a
2025, we calculated the Compound For reference, human-led traffic growth
challenge, doubly so if you care about
Monthly Growth Rate (CMGR) of AI was essentially flat at 0.3% CMGR.86
the dichotomy between crawlers and
bot growth in general terms, but also
The top three industries in growth tell us fetchers. Accounting for increased
by industry.
a lot about the objectives of these bots. resource usage in this evolving
Online Gambling has seen an absurd landscape is the bare minimum, and
growth of 133% MoM,87 demonstrating bot management solutions would be
how quickly AI systems can vacuum required for more fine-grained control,
up high-value, data-rich environments. especially if your content is proprietary
and monetizable.
85. Findings from our research partner Fastly. You can find the research referenced and their latest
reports here: fastly.com/threat-insights.
86. This is a good time to brush up on the Dead Internet Theory: en.wikipedia.org/wiki/Dead_
Internet_theory.
87. We are surprised the prediction markets didn’t predict that.
2026 DBIR Incident Classification Patterns 65

Deep-dive
analysis
/04

The paths of
privilege escalation
Passwords, The baseline Let’s do a simple level-set of what we
mean by each element:
configurations,
The best starting point for this type of 1. Passwords: Pretty obvious as to what
permissions and analysis is understanding the foundation. we mean by passwords, but what
In this case, we will leverage the MITRE we want to highlight is the use of
patches ATT&CK89 model. For those who aren’t crackable or guessable passwords.
experts on it, no worries; we aren’t In the world of Windows, hashes
Although the title has a relatively nice going to be splitting hairs between “Path are heavily utilized as the means of
ring and sing-songy element to it,88 it Interception by Search Order Hijacking” authentication, and weak passwords
might also strike a familiar chord of and “Path Interception by PATH in combination with weak hashing
“isn’t this just what cybersecurity is?” Environment Variable.” All we are really protocols are often a simple recipe
And yes, we could probably understand focused on is that ATT&CK provides for attackers getting a hold of the
cybersecurity as largely residing within a lingua franca of what different types actual credentials.
of actions (techniques) actors use to
these four pillars. What’s important,
achieve their objectives (tactics). 2. Configurations: These are the
though, is that this gives us a relatively
toggles and settings that exist in
simple communication vehicle and
Although there are more than 691 operating systems and services. Our
method of determining which ones we
different techniques as of ATT&CK point of reference was to refer to the
believe are important in which context.
version 18, what we’re really going to CIS Benchmarks91 as our source of
This can be how many successful
be focusing on are two of the Navigator truth in terms of what are considered
ransomware attacks, how many red team
columns: Privilege Escalation and configuration elements.
engagements and how this contrasts to
Credential Access. There are (only)
the daily hamster wheel of chasing down 176 techniques, as these are the ways 3. Permissions: Permissions are the
critical alerts and findings. in which low-level users are either rights allocated to users, services
able to escalate the permissions on or and groups. A simple example of a
Over the years, we have developed an
compromise higher-privileged accounts permission is “SeDebugPrivilege”
understanding of the different initial
and are a key step in many attacks. in Windows environments, which
access vectors, and now the questions
is typically assigned to the
we have are: How are adversaries
As part of each of these techniques, administration local group and allows
moving from low-level users to domain there are a set of mitigations,90 and each administrators to attach a debugger
admins, and are we as a community of these mitigations are grouped into one to any process and is commonly
prioritizing these gaps appropriately? of the four buckets we just discussed leveraged to dump credentials
(passwords, configurations, permissions from memory.
and patches).
4. Patches: Of course, outdated
and vulnerable systems and some
vulnerabilities can give attackers
a straight shot to credentials or
higher permissions.
88. An early draft had “configurations” as “parameters” in the title, but that was trying a bit too hard.
89. attack.mitre.org
90. Except for ~10% of techniques that don’t have mitigations listed for some reason. Ah, maybe in
version 19.
91. A community resource produced by the non-profit Center for Internet Security, which defines hardening
security guidance among other helpful community-focused resources
2026 DBIR Deep-dive analysis 67

Lastly, we see that only about 10% • Incidents: The incidents that we’re
of our techniques are mitigated by examining here are a slightly different
applying patches. It’s worth pointing out subset from our larger incident
that Exploitation of vulnerabilities is far corpus. Some of these incidents are
more traditionally present in incidents incorporated into our larger dataset
as an initial access vector (as seen in and some are ineligible for inclusion.
the “Results and analysis” section of The reason we’re examining this
this report) and will only have limited subset of incidents is that a few of our
presence here in Privilege Escalation. data contributors provided us with a
And though this starting point is still a sufficient level of detail to allow us to
relatively large field of things that can be accurately map things to ATT&CK
done, we will narrow our analysis to the and VERIS.92
techniques that are being leveraged.
Figure 71 captures the techniques found
across these different data sources.
Understanding An interesting finding is OS Credential
Dumping93 (T1003), specifically LSASS
observations
Figure 70. Percentage of techniques dumping, was one of the most common
mitigated by mitigation type (n=157) techniques found in both the threat
The first place we want to look is how we intelligence dataset (34%) and the
can quantify the commonness of each incidents dataset (20%), as shown in
With that explained, let’s take a quick technique. To get an understanding of the figure.
look at which techniques are mitigated prevalence, we combined a variety of
(partially or entirely) by each type different sources, each with their own set The limited appearance of this technique
of safeguard in Figure 70. As you of biases and limitations, and found out in red team engagements is probably
can see, the biggest percentage of how this wide view can help us prioritize more due to the structure of the
techniques can be addressed by our security efforts. testing (“Assume compromise”) rather
Privilege Management, with about than it being a technique beneath the
65% of techniques showing this • Threat intelligence: One way that hack-o-mancers that perform these
element as being key to mitigating the we can understand observations is by tests. LSASS memory is one of those
attack. The types of mitigations we examining threat intelligence reports, interesting cybersecurity problems. It’s
find recommended include restricting which are recorded observations of foundational to how Windows works, and
administrative functionality or restricting different techniques being used there are built-in mitigations in place;
access to sensitive folders, such as by Actors. however, it’s still the bread and butter94
startup folders or top-level operating of attackers once they get access to an
• Red team activity: Red teams
system directories. endpoint system.
are ethical hackers that test an
The next two most common mitigations organization’s ability to detect and In contrast, in the red teaming world, we
are Configurations and Password respond to attacks. Some of these see a lot of targeting of authentication
Policies, at 33% and 30%, respectively. tests are structured as “Assume services by using Kerberoasting95
These types of mitigations focus on compromise,” in which attackers are attacks and stealing and forging
tweaks to the operating system and given access to a system within the authentication certificates. These
servers with the recommendations environment and leverage that system types of attacks are largely focused
pertaining to password practices, such to conduct their attacks, rather than on compromising service accounts
as password strength, MFA and having to establish a foothold on a that are misconfigured and have
disabling insecure protocols or compromised system. weak passwords.
weak hashing algorithms.
92. To be clear, most of our data contributors do so, and we love them. However, some of our data comes
from public sources, where this level of detail is harder to come by.
93. Semantics alert: Because we’re incorporating a bunch of different datasets, we aren’t capturing or
representing hierarchical relationships here that exist between the techniques and subtechniques.
94. Or the “meat and potatoes” or the “rice and beans,” depending where in the world you are from
95. Apologies for the ultra-oversimplification of these attacks, but we got to stick to our report page budget!
2026 DBIR Deep-dive analysis 68

Figure 71. Privilege and credential access techniques by observations
2026 DBIR Deep-dive analysis 69

We also see the attack DCSync and However, when it comes to password To put it simply, based on this dataset,
Security Account Manager (SAM) strength, the battle isn’t just against users are more than four times more
dumps showing up, which are alternative compute power (at least not until the likely to use an already compromised
methods of dumping credentials. quantum singularity98 occurs) but also password than a “weak” password.
DCSync does this by convincing a against human nature.
Compounding this issue, the median
remote domain controller to replicate its
Remembering and creating unique percentage of users that are reusing
data (including passwords), and SAM
passwords is challenging, but enforcing passwords, or have the same password
dumps extract credentials either from
complexity isn’t. We found that the as others, is about 6%. When attackers
memory or from a secure location in
median percentage of Active Directory are looking to crack the hashes of the
the registry.
user accounts not meeting complexity passwords they have collected from their
Lastly, it’s worth mentioning Exploitation requirements was less than 1%. engagements, they are banking on the
for Privilege Escalation, which shows fact that passwords are being reused,
Although organizations are good at
up in 9% of incidents and 20% of threat either from previous compromises in
enforcing “strong passwords”—it’s
intelligence. That means the majority other organizations or internally. If the
a default option in most systems
(83%) of incidents did not include systems also aren’t configured to use
nowadays—that is not keeping users
exploiting a vulnerability96 for escalating modern hashing algorithms, it makes
from using passwords that have
privileges. So even though patching will their job even easier, which is a good
already been compromised, with the
have a positive impact on your initial segway to our next section.
median percentage being 4%, as
access vector mitigation, it’s not the only
Figure 72 demonstrates.
way to move the needle for preventing
privilege escalation. However, when we
took a quick look across our vulnerability
management dataset for this year, we
found 26% of organizations still had
privilege escalation vulnerabilities from
2021, and 11% had some from 2018.
Let’s focus on our other mitigation
strategies, but don’t leave those old
vulnerabilities behind.
Passwords
Is this the year passwords die? We say
this in jest, nearly every year, knowing
full well in our heart of hearts that’s
likely not the case. Passwords are used
in various places as the only line of
defense. However, this line of defense
may be more of a Maginot Line than
The Wall of Westeros.97 When it comes
to passwords, we as an industry have
previously tried to drive complexity
Figure 72. Distribution of percentage of accounts scanned with breached passwords
recommendations as the foundation
(n=7,345)
of making strong and uncrackable
passwords.
96. Vulnerability in the strictest definition as being a CVE-assigned vulnerability. Yes, that does include the
ones in the backlog of the National Vulnerability Database.
97. What do you mean The Wall fell in Season 7? Game of Thrones only ran for six seasons. That’s not funny.
98. With or without AI. Take your pick.
2026 DBIR Deep-dive analysis 70

Configurations The solutions exist, but they often Permissions
require the organizations to explicitly
implement those, as vendors have to
We are fully aware that security The longer you spend staring into
balance the business need of making
configurations aren’t the spicy and ATT&CK techniques,100 the more you
their software easy to use out of the box
exciting part of cybersecurity.99 start to see a common pattern: the
and these additional security risks.
Turning on features, testing them in a requirement for proper permissions to
staging environment, pushing them to Figure 73 has a breakdown of the conduct the attack. Having access to
all employees, reverting them back to percentage of failed configuration permissions of a local admin (or, even
the previous state after some ancient checks associated with different better, domain admin) opens up several
application breaks, crying in the office ATT&CK techniques as compared venues for attackers, such as reading
bathroom and calling it a day doesn’t between servers and desktops. First, into protected files and memory or
really make for the most compelling some major takeaways: The majority of making key configuration changes to a
storytelling. assets failed password configuration system. Of the techniques we examined,
checks based on traditional security 65% mentioned restricting permissions
However, secure configurations are a
hardening recommendations. The as one of the main ways to prevent
key component to preventing many of
most common failed checks related these techniques.
the techniques that we have discussed
to passwords are the number of failed
in this section. Of those, about 33% have Privileges are a bit more nuanced than
login attempts before lockout (97%
some element of configuration being one might think, though, and don’t
of assessed devices) and passwords
listed as a key mitigation. simply involve looking at a list of objects
requiring lengths of 15 characters or
that have overly strong permissions.
more (90% of assessed devices).
In some instances, these permissions
The most implemented configuration, are transitory in nature. One privilege
in which less than 10% of assets failed may allow you access and/or allow
the check, pertained to protecting you to modify an object that might, in
against Access Token Manipulation. turn, allow you more privileges. These
These types of techniques rely on are sometimes understood as attack
systems that are misconfigured and paths, whereby chaining these transitory
allow users with access to administrative relationships of privileges, attackers
functions. Also of note is the difference are able to pivot from low-level users
in LSASS protection between servers to domain admins. To understand the
and desktops. Desktops continue to complex relationships that exist within
be largely vulnerable to these types an environment, organizations can map
of attacks in comparison to servers, the relationships that exist between
which when we consider the possible users, groups and permissions to create
exposures that exist from administrators an attack graph. These attack graphs
logging into end-user systems, can show how attackers find the easiest
constitutes a perfect segue for our paths between low-level users and
next section on permissions. domain admins and assist defenders in
identifying exposures. Based on attack
graphs collected from organizations,
it was found that 16% of organizations
had about 80% exposure, meaning that
given initial access to the environment,
an attacker with low-level privileges had
an 80% or better chance of successfully
compromising a key administrative
account or infrastructure element.
Figure 73. Percentage of failed
configuration checks by attack
techniques and asset type
(n for Desktop=10,279,021)
(n for Server=1,149,990)
99. Is there one?
100. The techniques eventually stare back.
2026 DBIR Deep-dive analysis 71

Figure 74 captures the 10 most
common attack paths found in these
assessments. Some of these exposures,
such as Tier Zero accounts logging
into non-privileged systems, could
directly expose high-privilege accounts
to techniques such as Credential
Dumping. Still, other privileges can
open up organizations to different
types of attacks, depending on how the
systems are configured and the type of
access the attackers have, such as the
ability of low-level users to have write
privileges over higher-tier resources, a
clear compromise of the least-privilege
principle. For organizations to help
properly defend themselves, they
need to adopt a stronger stance than
just chasing down vulnerabilities and
alerts. Instead, they need to examine
their cybersecurity in a holistic fashion,
including examining the exposures
that exist in their environments from
permissions, configurations and
poor passwords.
Figure 74. Top attack paths by
permissions (n=1,500)
2026 DBIR Deep-dive analysis 72

The North Korean
IT worker risk
Overemployed Figure 75 shows the variety of different
industries that were being targeted in
and over-trusted
2025 by ITWs. It seems that the vast
majority of the activity uncovered was
One of the defining features of the focused on the raising of funds through
2025 IT landscape was the systematic payroll. Some industry sources have
infiltration of IT workers (ITWs) from the suggested that ITWs may facilitate
Democratic People’s Republic of Korea further access for state-sponsored
(DPRK). Some of these workers—which groups, though we have not been able
we shall refer to collectively as ITWs— to substantiate this with sufficient data.
were able to achieve multiple positions
across a large spread of industries.
Competitive job
Using stolen identities, the ITWs were
market challenges
able to acquire jobs and operate out
of regionally hosted laptop farms
run by local accomplices. This setup For obvious reasons, ITWs have
allowed the actors to pass the interview Figure 75. Top targeted industries by historically targeted remote jobs focused
process and perform the jobs without North Korean ITW campaigns on programming and data engineering.
requiring a physical presence in the Given they have to pass the technical
area. Interestingly enough, some of interviews and make a convincing
these ITWs did more than just “quiet I don’t have enough appeal to be hired, job
quit” and collect a paycheck, as some specifications needing IT and software
anything
organizations were surprised to find development skills have been the
that some of their top-performing interesting. primary focus.
new recruits were misrepresenting
As of more recent times, with shifts in
their identities.101 Why would I be
the hiring market and more awareness of
This is a pretty serious concern on the a target? the specific jobs that would be targeted,
outset, since employing individuals with they have also started to move toward
falsified credentials and skills poses a human resources and marketing jobs.
When tackling a complex issue, it’s
big enough risk, but adding the fact that
helpful to get an idea of the scope of the Figure 76 has the breakdown of job
these employees may also be associated
problem. In 2025 and earlier, there were specifications that have been targeted
with or operating on behalf of the
various reports102 and indictments103 that by ITWs in 2025 and include frontend
North Korean government, according
came out from law enforcement as they developers, with blockchain/Web3 and
to U.S. government advisories and law
continued to actively pursue and disrupt full-stack engineering jobs at the top.
enforcement filings, is enough to give
these operations. Reviewing those Other researchers104 that track this
your compliance and security officers a
sources, it was clear that companies threat have found these actors pivoting
collective heart attack.
from widely different sectors were falling to AI-focused jobs, as well, showing that
victim to these types of fraud. they are following market trends in terms
of where those high-paying remote jobs
are. Too bad those folks are not active
on LinkedIn, as we could all benefit from
some hiring tips in hot markets.
101. This sounds like a traditional DBIR joke, but this fact was raised to us in multiple interviews with subject
matter experts (SMEs) we conducted while writing this section.
102. reports.dtexsystems.com/DTEX-Exposing+DPRK+Cyber+Syndicate+and+Hidden+IT+Workforce.pdf
103. justice.gov/opa/pr/justice-department-announces-coordinated-nationwide-actions-combat-north-
korean-remote
104. okta.com/blog/threat-intelligence/north-korea-s-it-workers-expand-beyond-us-big-tech
2026 DBIR Deep-dive analysis 73

In terms of protecting your organization,
like so many other things in security,
it comes down to collaboration within
your organization, especially with the
teams running human resources and
recruitment processes. That includes
things like:
• Additional scrutiny to backgrounds,
resumes and information provided
by applicants
• Verifying identity through multiple
touchpoints during the hiring process
• Making sure your insider threat and
security awareness programs discuss
these new types of threats
Figure 76. Top targeted job
specifications by North Korean
ITW campaigns
How big of a
problem is this?
Reaching a precise number of victims
is relatively challenging, as organizations
are not required to publicly disclose that
they have accidentally hired a North
Korean IT worker, but looking at the
other side of the equation can give us an
understanding of how many fake ITWs
there are. According to our analysis,
ITWs leveraged an estimated 15,000
possible stolen identities, with the typical
ITW leveraging around three to five
identities at any given time. With those
back-of-the-napkin calculations, our
rough analysis suggests the figure
could be in the low thousands,
though this estimate carries
considerable uncertainty.
2026 DBIR Deep-dive analysis 74

Industries
/05

Introduction
Welcome to the “Industries” section of Many of our readers refer to this
the 2026 DBIR! As noted previously, we section to find “bespoke post” results
analyzed more than 22,000 confirmed for their own industries. When doing
data breaches this year—by far the so, we recommend starting with the
largest number we have ever examined top patterns for your sector in this
in a single report. In this section, we section, then circling back to the main
break those breaches down by industry. pattern chapters referenced for your
Different industries face different threats, vertical. This should give you a deeper
largely because their attack surfaces are understanding of the attacks you will
not created equal. likely need to defend against.
When reading this section, it’s important Finally, since this is a security report and
to be aware of a few caveats. Industry- not a novel penned by Tolstoy or Proust,
level differences can be influenced by we do not have sufficient space (and in
factors such as varying regulatory and some cases not enough data) to look
reporting requirements and the resulting at all industries exhaustively; therefore,
differences in the level of external we provide Table 3. It offers a quick
scrutiny they receive, along with the reference for high-level information on
size of the data sample we have for any the industries that we do not delve
given industry. These and other factors into here.
can affect how a vertical appears in the
report, so please keep that in mind when
comparing one industry to another.
2026 DBIR Industries 76

|     | Incidents |     |     |     | Breaches |     |     |     |
| --- | --------- | --- | --- | --- | -------- | --- | --- | --- |
Industry Total Small (1–1,000) Large (1,000+) Unknown Total Small (1–1,000) Large (1,000+) Unknown
| Total               | 31,861 | 7,257 | 528 | 24,076 | 22,625 | 7,153 | 466 | 15,006 |
| ------------------- | ------ | ----- | --- | ------ | ------ | ----- | --- | ------ |
| Accommodation (72)  | 319    | 89    | 11  | 219    | 250    | 88    | 11  | 151    |
| Administrative (56) | 422    | 295   | 12  | 115    | 419    | 295   | 12  | 112    |
| Agriculture (11)    | 223    | 34    | 0   | 189    | 219    | 34    | 0   | 185    |
| Construction (23)   | 843    | 525   | 8   | 310    | 828    | 524   | 8   | 296    |
| Education (61)      | 1,302  | 219   | 22  | 1,061  | 1,252  | 216   | 22  | 1,014  |
| Entertainment (71)  | 587    | 90    | 5   | 492    | 483    | 90    | 5   | 388    |
| Finance (52)        | 3,809  | 365   | 52  | 3,392  | 1,300  | 358   | 50  | 892    |
| Healthcare (62)     | 1,492  | 472   | 21  | 999    | 1,438  | 466   | 20  | 952    |
| Information (51)    | 1,703  | 214   | 79  | 1,410  | 1,099  | 202   | 59  | 838    |
| Management (55)     | 103    | 30    | 0   | 73     | 101    | 30    | 0   | 71     |
Manufacturing (31–33) 3,627 1,198 56 2,373 2,713 1,176 50 1,487
| Mining (21)         | 72    | 35    | 3   | 34    | 70    | 35    | 2   | 33    |
| ------------------- | ----- | ----- | --- | ----- | ----- | ----- | --- | ----- |
| Other Services (81) | 900   | 206   | 4   | 690   | 885   | 205   | 4   | 676   |
| Professional (54)   | 3,578 | 1,400 | 82  | 2,096 | 2,558 | 1,380 | 58  | 1,120 |
Public Administration (92) 3,634 148 17 3,469 2,410 148 17 2,245
| Real Estate (53)       | 505    | 189   | 1   | 315    | 499    | 188   | 1   | 310    |
| ---------------------- | ------ | ----- | --- | ------ | ------ | ----- | --- | ------ |
| Retail (44–45)         | 997    | 315   | 32  | 650    | 806    | 313   | 32  | 461    |
| Transportation (48–49) | 689    | 242   | 24  | 423    | 652    | 242   | 21  | 389    |
| Utilities (22)         | 638    | 57    | 8   | 573    | 597    | 57    | 7   | 533    |
| Wholesale (42)         | 1,057  | 877   | 18  | 162    | 1,048  | 875   | 18  | 155    |
| Unknown                | 5,361  | 257   | 73  | 5,031  | 2,998  | 231   | 69  | 2,698  |
| Total                  | 31,861 | 7,257 | 528 | 24,076 | 22,625 | 7,153 | 466 | 15,006 |
Table 3. Number of security incidents by victim industry and organization size
2026 DBIR Industries 77

2026 DBIR Industries 78
nrettaP
noitcA
tessA
Incidents
Figure 77. Incidents by industry

Breaches
Figure 78. Breaches by industry
2026 DBIR Industries 79
nrettaP
noitcA
tessA

Industry  Frequency Top patterns Threat actors Actor motives Data
(NAICS) compromised
Agriculture (11) 223 incidents, 219  System Intrusion,  External (100%)  Financial (71%),  Internal (70%),
with confirmed data  Basic Web  (breaches) Espionage (29%),  Other (43%),
| disclosure | Application         |     | Ideology (1%)  | Secrets (36%)  |
| ---------- | ------------------- | --- | -------------- | -------------- |
|            | Attacks and Social  |     | (breaches)     | (breaches)     |
Engineering
represent 91% of
breaches
Administrative (56) 422 incidents, 419  System Intrusion,  External (99%),  Financial (100%)  Internal (96%),
with confirmed data  Social Engineering  Internal (1%)  (breaches) Credentials (28%),
| disclosure | and Basic Web        | (breaches) |     | Other (2%),   |
| ---------- | -------------------- | ---------- | --- | ------------- |
|            | Application Attacks  |            |     | System (2%)   |
|            | represent 98% of     |            |     | (breaches)    |
breaches
Construction (23) 843 incidents, 828  System Intrusion,  External (99%),  Financial (97%),  Internal (86%),
with confirmed data  Social Engineering  Internal (1%)  Espionage (5%)  Credentials (34%),
disclosure and Basic Web  (breaches) (breaches) Other (13%),
|     | Application Attacks  |     |     | Secrets (6%)  |
| --- | -------------------- | --- | --- | ------------- |
|     | represent 95% of     |     |     | (breaches)    |
breaches
Entertainment (71) 587 incidents, 483  System Intrusion,  External (86%),  Financial (89%),  Internal (54%),
with confirmed data  Social Engineering  Internal (14%)  Espionage (20%),  Personal (45%),
disclosure and Everything Else  (breaches) Ideology (1%)  Other (31%),
|     | represent 82% of  |     | (breaches) | Secrets (20%)  |
| --- | ----------------- | --- | ---------- | -------------- |
|     | breaches          |     |            | (breaches)     |
Information (51) 1,703 incidents,  System Intrusion,  External (89%),  Financial (84%),  Internal (52%),
1,099 with confirmed  Basic Web  Internal (11%),  Espionage (16%),  Personal (39%),
data disclosure Application Attacks  Multiple (1%) Ideology (2%) Other (31%),
and Everything Else  (breaches) (breaches) Credentials (24%)
|     | represent 79% of  |     |     | (breaches) |
| --- | ----------------- | --- | --- | ---------- |
breaches
Management (55) 103 incidents, 101  System Intrusion,  External (100%)  Financial (100%)  Internal (96%),
with confirmed data  Social Engineering  (breaches) (breaches) Credentials
| disclosure | and Basic Web        |     |     | (35%), Multi-      |
| ---------- | -------------------- | --- | --- | ------------------ |
|            | Application Attacks  |     |     | factor credential  |
|            | represent 98% of     |     |     | (3%), Other (2%)   |
|            | breaches             |     |     | (breaches)         |
Mining (21) 72 incidents, 70  System Intrusion,  External (100%)  Financial (97%),  Internal (74%),
with confirmed data  Everything Else  (breaches) Espionage (1%),  Credentials
| disclosure | and Basic Web        |     | Ideology (1%)  | (31%), Personal    |
| ---------- | -------------------- | --- | -------------- | ------------------ |
|            | Application Attacks  |     | (breaches)     | (17%), Other (9%)  |
|            | represent 96% of     |     |                | (breaches)         |
breaches
Table 4. At-a-glance table for victim industries without a section
2026 DBIR Industries 80

Industry  Frequency Top patterns Threat actors Actor motives Data
(NAICS) compromised
Other Services (81) 900 incidents, 885  System Intrusion,  External (81%),  Financial (78%),  Internal (66%),
with confirmed data  Social Engineering  Internal (19%)  Espionage (23%) Personal (38%),
disclosure and Miscellaneous  (breaches) (breaches) Other (28%),
|     | Errors represent  |     |     | Secrets (20%)  |
| --- | ----------------- | --- | --- | -------------- |
|     | 85% of breaches   |     |     | (breaches)     |
Professional (54) 3,578 incidents,  System Intrusion,  External (97%),  Financial (96%),  Internal (80%),
2,558 with  Social Engineering  Internal (3%) Espionage (5%) Credentials
confirmed data  and Basic Web  (breaches) (breaches) (31%), Personal
| disclosure | Application Attacks  |     |     | (14%), Other (11%)  |
| ---------- | -------------------- | --- | --- | ------------------- |
|            | represent 91% of     |     |     | (breaches)          |
breaches
Real Estate (53) 505 incidents, 499  System Intrusion,  External (79%),  Financial (100%)  Internal (63%),
with confirmed data  Social Engineering  Internal (22%) (breaches) Personal (43%),
| disclosure | and Miscellaneous  | (breaches) |     | Credentials (24%),  |
| ---------- | ------------------ | ---------- | --- | ------------------- |
|            | Errors represent   |            |     | Other (16%)         |
|            | 85% of breaches    |            |     | (breaches)          |
Transportation  689 incidents, 652  System Intrusion,  External (99%),  Financial (89%),  Internal (84%),
(48–49) with confirmed data  Basic Web  Internal (1%)  Espionage (15%),  Credentials (27%),
disclosure Application Attacks  (breaches) Ideology (1%)  Secrets (16%),
|     | and Everything Else  |     | (breaches) | Other (14%)  |
| --- | -------------------- | --- | ---------- | ------------ |
|     | represent 89% of     |     |            | (breaches)   |
breaches
Utilities (22) 638 incidents, 597  System Intrusion,  External (97%),  Espionage (71%),  Internal (85%),
with confirmed data  Basic Web  Internal (3%) Financial (36%)  Secrets (68%),
| disclosure | Application         | (breaches) | (breaches) | Other (21%)  |
| ---------- | ------------------- | ---------- | ---------- | ------------ |
|            | Attacks and Social  |            |            | (breaches)   |
Engineering
represent 94% of
breaches
Wholesale Trade  1,057 incidents,  System Intrusion,  External (100%)  Financial (100%)  Internal (98%),
(42) 1,048 with confirmed  Basic Web  (breaches) (breaches) Credentials (29%)
| data disclosure | Application  |     |     | (breaches) |
| --------------- | ------------ | --- | --- | ---------- |
Attacks and Social
Engineering
represent 99% of
breaches
Table 4. At-a-glance table for victim industries without a section (continued)
2026 DBIR Industries 81

Educational
Services
 SCIAN
16
System Intrusion is the undisputed
Summary Frequency 1,302 incidents, 1,252  headliner for this vertical, appearing
|     | with confirmed data  | approximately three times as often  |
| --- | -------------------- | ----------------------------------- |
The Education vertical is troubled
|     | disclosure | as any other pattern and accounting  |
| --- | ---------- | ------------------------------------ |
primarily by external, financially  for 52% of all Education breaches
motivated actors who utilize  Top patterns System Intrusion,  (Figure 79). In practice, that means
Ransomware, Exploit vulnerabilities   Social Engineering  many incidents involve attackers
and rely greatly on the Use of   and Miscellaneous  actively working their way into the
stolen credentials.
|     | Errors represent 83%  | victim environments—often by chaining  |
| --- | --------------------- | -------------------------------------- |
|     | of breaches           | together various action types or by    |
What is the same? generally employing whatever tools
| Threat actors | External (78%),  | are necessary to pull off a more  |
| ------------- | ---------------- | --------------------------------- |
The System Intrusion, Social Engineering  Internal (22%)  complex attack. Victims can take some
|     | (breaches) | consolation in the fact that they made  |
| --- | ---------- | --------------------------------------- |
and Miscellaneous Errors patterns are
the attackers earn every inch of the
still the top three patterns, as they were
| Actor motives | Financial (78%),  |     |
| ------------- | ----------------- | --- |
last year and the year before.  systems they compromised.105 Small
|     | Espionage (21%)  | comfort, we know. |
| --- | ---------------- | ----------------- |
Ideology (2%)
Social Engineering (17%) and
(breaches)
Miscellaneous Errors (16%) represent
significantly smaller numbers but
| Data        | Internal (64%),        |                                        |
| ----------- | ---------------------- | -------------------------------------- |
| compromised | Personal (41%), Other  | still play meaningful roles. Think     |
|             | (26%), Secrets (19%)   | phishing emails that open the door or  |
misconfigurations that kindly leave it
(breaches)
propped wide open for anyone to walk
through. Nevertheless, in this vertical,
| Initial access  | Exploitation of  |     |
| --------------- | ---------------- | --- |
they are both only supporting roles and
| vector    | vulnerabilities (34%),  |                            |
| --------- | ----------------------- | -------------------------- |
| breakdown | Phishing (22%),         | not the stars of the show. |
Credential abuse (8%)
The Education sector is beset by
(breaches)
Hacking and Malware attacks in equal
measure (55% of breaches), as shown
Other metrics Human element (68%),  in Figure 80. When we break down the
Third-party (40%)
Hacking varieties in play (see Figure 81),
we get a slightly atypical picture. The
Exploitation of vulnerabilities leads the
pack, showing up in 77% of hacking-
related breaches. Those weaknesses
are being worked primarily by Organized
crime and State-affiliated actors,
although the data doesn’t always go
deep enough for us to name and shame
the specific vulnerabilities that caused
most of the damage. In a more familiar
pattern, stolen credentials are also
heavily represented, appearing
in 65% of breaches that involve
Hacking actions.
Figure 79. Top patterns in Educational Services breaches over time (n for 2026
dataset=1,252)
105. In true Chuck Norris style!
2026 DBIR Industries 82

Figure 82 confirms what most defenders
in Education already suspect:106
Ransomware remains the undisputed
heavyweight of the sector, appearing in
65% of malware-related breaches. While
this lack of a "plot twist" may not surprise
seasoned veterans, the mechanics of
these attacks deserve a closer look.
Backdoor or C2 functionality shows up
in 35% of malware-driven breaches,
giving attackers a handy way to maintain
access, recon the environment and
perpetrate more illicit operations long
after the initial infection.
The primary vector of infection is via
Web applications (Figure 83), which
serve as the front door in 71% of
cases. To illustrate, we need only
look back to the late summer of 2025.
A well-known ransomware gang—the
same group behind the 2023 MOVEit
Figure 80. Action types in Educational Figure 82. Top Malware action varieties
Services breaches (n=1,252) exploitation—shifted their sights to in Educational Services breaches (n=631)
a zero-day vulnerability in Oracle’s
E-Business Suite.107 This campaign
resulted in more than 100 organizations
being compromised and subjected to
extortion, with a heavy concentration of
those victims residing right here in the
Education sector.
Meanwhile, web application downloads
are close behind at 65%, and email
attachments are doing their usual
damage in 52% of incidents.
Social attacks appear in 22% of
breaches and, no surprise here, they’re
mostly classic phishing attacks (81%),
with Email acting as the primary
delivery vehicle in 88% of those cases.
Meanwhile, Errors are less common
in this vertical, showing up in just 17%
of breaches. Misdelivery remains the
leading error variety, consistent with
last year’s findings. However, this year,
the picture shifts slightly with Loss now
Figure 81. Top Hacking action varieties accounting for 21% of errors, edging out Figure 83. Top Malware vectors in
in Educational Services breaches Educational Services breaches (n=272)
Misconfiguration, which played a more
(n=435)
prominent role in the prior report.
106. Ok, already know for sure
107. github.com/vz-risk/VCDB/issues/22574
2026 DBIR Industries 83

Financial and
Insurance
It’s a rich
Summary
man’s world.
This sector continues to be heavily
targeted by financially motivated This sector continues to be a favorite
external attackers, with Ransomware- among attackers, which isn’t surprising
driven System Intrusions, Phishing, given that its core business is handling
Exploit vulnerability and Use of stolen money. Incidents increased this year, but
credentials being the primary threats. the proportion that resulted in successful
Human error and third-party exposure breaches remains fairly consistent.
remain significant contributing factors.
As Figure 84 shows, the System
Intrusion pattern has been on a strong
What is the same?
upward trajectory over the past several
years. After briefly competing with
System Intrusion remains the top pattern
Social Engineering in the 2022 and
since 2022. Attackers remain primarily
2023 DBIRs, it has reigned supreme
financially motivated.
ever since. If you’re not familiar with our
attack patterns, System Intrusion is the
more complex pattern, where the attacks
that take a bit more work tend to live.
It has been dominated by Ransomware,
and we also see the Use of stolen
creds and Exploit vuln hacking actions
appearing frequently as the primary
methods of initial access.
2026 DBIR Industries 84
SCIAN
25
Frequency 3,809 incidents, 1,300
with confirmed data
disclosure
Top patterns System Intrusion,
Social Engineering
and Everything Else
represent 81% of
breaches
Threat actors External (88%),
Internal (12%)
(breaches)
Actor motives Financial (98%),
Espionage (3%)
(breaches)
Data Internal (53%),
compromised Personal (43%), Other
(28%), Credentials
(26%) (breaches)
Initial access Exploitation of
vector vulnerabilities (22%),
breakdown Phishing (20%),
Credential abuse
(15%) (breaches)
Other metrics Human element (65%),
Third-party (34%)
Figure 84. Top patterns in Financial and Insurance breaches over time (n for 2026
dataset=1,300)

The Social Engineering pattern has
long played second fiddle to System
Intrusion, and this year is no different.
The top social actions in this sector were
Phishing and Pretexting. Phishing, being
the lower-effort attack, is seen more than
twice as often as Pretexting. Criminals
are nothing if not efficient in their
efforts to gain access to your systems,
and we saw significant examples of
compromises targeting this industry
being initiated by social engineering
attacks against third parties this
past year.
This year, the Everything Else pattern
has moved into third place. This isn’t a
true pattern but a catch-all for cases
that lack enough detail to be classified
elsewhere. Its rise to third place for this
sector is notable, however, since Basic
Web Application Attacks held that spot
in the 2025 report. This may turn out to
be an interesting change, but it may also
be due to the normal year-to-year data
variation from our partners.
Attackers in this industry are still
predominantly External and financially
motivated. Internal actors decreased
substantially since last year, from 22%
to just 12%. However, it is important to
remember that Internal actor breaches
are mainly accidental and not carried out
with malicious intent.
2026 DBIR Industries 85

Healthcare
Snake oil remedies come and go on
Summary social media, often promising “this one
weird trick” will melt away belly fat with
Healthcare organizations face a mix of no effort on your part. These claims
Ransomware-driven System Intrusions can be ignored, but basic hygiene,
and persistent human errors, with whether personal or cyber, cannot.
financially motivated external attackers The fundamental principles must be
exploiting vulnerabilities, Phishing, and addressed for an organization to be
using stolen credentials. Staff mistakes able to weather cyber incidents
and Misconfigurations remain a chronic and breaches.
source of breaches.
Breaches take many forms, but in the
Healthcare sector, one pattern stands
What is the same? out: Miscellaneous Errors. DBIRs from
2014 through 2026 have shown that
Miscellaneous Errors has been in the
Healthcare has been among the most
top patterns for this industry since we
affected by staff mistakes. Miscellaneous
started keeping track. System Intrusion
Errors has been among the top three
is, once again, in the number one spot for
patterns each year. The ranking may
the second year in a row.
vary from year to year, but it remains a
chronic problem that needs a cure.
This year’s top errors in Healthcare
were Misdelivery (data is delivered
to the wrong recipient, in any format)
Loss (often involving unencrypted
user devices and portable media)
and Misconfiguration (such as
exposing a data store to the internet
without appropriate controls). These
Misconfigurations are frequently
discovered by security researchers who
typically make an effort to notify the
victim organizations rather than simply
take the data for their own use.
Figure 86 illustrates that despite
repeated recommendations to implement
controls to prevent or limit the impact
of such mistakes, these Errors have
remained persistent over the years.
Controls to combat these kinds of
mistakes, which appear in our dataset
again and again, would be part of those
security fundamentals we mentioned.
2026 DBIR Industries 86
SCIAN
26
Frequency 1,492 incidents, 1,438
with confirmed data
disclosure
Top patterns System Intrusion,
Miscellaneous Errors
and Social
Engineering represent
81% of breaches
Threat actors External (81%),
Internal (19%)
(breaches)
Actor motives Financial (99%),
Espionage (2%)
(breaches)
Data Internal (65%),
compromised Personal (37%),
Credentials (25%),
Other (19%)
(breaches)
Initial access Exploitation of
vector vulnerabilities (20%),
breakdown Phishing (14%),
Credential abuse (11%)
(breaches)
Other metrics Human element (54%),
Third-party (32%)
(breaches)
Figure 85. Top patterns in Healthcare breaches over time (n for 2026 dataset=1,438)

Figure 86. Top Error varieties in Healthcare breaches over time
(n for 2026 dataset=186)
Hopping off The security fundamentals do not only
apply to your own organization—they
our soapbox
must also be baked into the contracts
made with business associates and
System Intrusion remains the top suppliers, as well.
pattern for the Healthcare industry
The Social Engineering pattern re-
and is largely driven by Ransomware.
entered the top three, replacing last
Threat actors commonly gain access
year’s Everything Else. For social
via the Use of stolen credentials or by
actions, Phishing was most common,
the Exploitation of vulnerabilities, then
followed by Pretexting. This year, we
deploy Ransomware and frequently
saw a small number of Baiting cases in
follow up with the exfiltration of data for
which attackers infected the websites
future leverage. In other cases, Actors
frequently visited by their targets.
simply rely on extortion alone and do not
trigger the encryption of data.
This year, many industries were
affected by the Oracle E-Business Suite
vulnerability,108 and Healthcare was
not spared. A number of organizations
reported having been affected by this
attack, largely attributed to the Cl0p
criminal group. In part, this contributed to
the third-party figure of 32% of breaches
in this sector and illustrates how the
complex web of third-party relationships
can impact any organization.
108. z2data.com/insights/everything-you-need-to-know-about-the-oracle-data-breach
2026 DBIR Industries 87

Manufacturing
 SCIAN 33–13
| Summary | Frequency | 3,627 incidents, 2,713  |     |
| ------- | --------- | ----------------------- | --- |
with confirmed data
| The number of breaches in this   |     | disclosure |     |
| -------------------------------- | --- | ---------- | --- |
industry continues to grow, with the
uptick in numbers largely due to
|     | Top patterns | System Intrusion,  |     |
| --- | ------------ | ------------------ | --- |
Ransomware attacks.
Social Engineering
and Basic Web
Application Attacks
What is the same?
represent 91% of
breaches
The top patterns for Manufacturing
are the same as last year, with the
| vast majority of actors being   | Threat actors | External (95%),  |     |
| ------------------------------- | ------------- | ---------------- | --- |
| financially motivated.          |               | Internal (5%)    |     |
(breaches)
|     | Actor motives | Financial (87%),  |     |
| --- | ------------- | ----------------- | --- |
Espionage (15%)
(breaches)
|     | Data        | Internal (81%),        |                                     |
| --- | ----------- | ---------------------- | ----------------------------------- |
|     | compromised | Credentials (26%),     | Figure 88. Top Action varieties in  |
|     |             | Other (22%), Personal  | Manufacturing breaches (n=2,417)    |
(17%) (breaches)
Initial access  Exploitation of  Ransomware is still, in large part, the
|     |     | vulnerabilities (38%),  | driving force behind both the growth in  |
| --- | --- | ----------------------- | ---------------------------------------- |
vector
breaches and the prominence of System
|     | breakdown | Phishing (13%),  |     |
| --- | --------- | ---------------- | --- |
Intrusion incidents. Malware was involved
Credential abuse (11%)
in 75% of the breaches in this vertical,
(breaches)
with Ransomware accounting for 61%
Other metrics Third-party (61%),  (Figure 88). A prominent example within
|     |     | Human element (56%)  | this sector is the late 2025 Ransomware  |
| --- | --- | -------------------- | ---------------------------------------- |
|     |     | (breaches)           | attack on the Japanese company           |
Asahi Group Holdings.109 The incident
forced a shutdown of their domestic
manufacturing facilities and resulted in
a suspension of shipments, while also
potentially compromising corporate data.
This event illustrates that the financial
impact of a breach can often extend
far beyond the immediate ransom or
extortion demands, as the operational
downtime and downstream supply
chain disruption can be considerable.
Figure 87. Top patterns in Manufacturing breaches over time (n for 2026
dataset=2,713)
109. github.com/vz-risk/VCDB/issues/22512
2026 DBIR Industries 88

Hacking actions were involved in 71%
of Manufacturing breaches. The main
tactics haven’t changed much since last
year’s report: Use of stolen credentials
and Exploit vulnerability each contributed
to 41% of Manufacturing breaches.
Social Engineering may be the second
most common pattern in this vertical,
but its actions still lag well behind the
leaders Malware and Hacking, as
shown in Figure 89. Social actions
appeared in only 16% of breaches,
and most of those were of the Phishing
variety (77%). The more elaborate
Pretexting schemes barely register
by comparison, accounting for
only 18% of social attacks in
Manufacturing breaches.
Internal data in this sector apparently
didn’t get the memo about staying put.
It’s involved in 80% of breaches (see Figure 89. Action types in
Manufacturing breaches (n=2,713)
Figure 90), making emails, plans and
reports among the favorite items on
the criminal’s takeout menu, or perhaps
simply the easiest to obtain. Credentials
show up next in 26% of incidents,
and Personal (personally identifiable
information, or PII) data makes an
appearance in 17% of Manufacturing
breaches—less common but still more
than enough to ruin someone’s day.
Figure 90. Top Data varieties in
Manufacturing breaches (n=2,452)
2026 DBIR Industries 89

Public
Administration
 SCIAN
29
This year, the top three incident patterns
in Public Administration are System
| Summary | Frequency | 3,634 incidents, 2,410  |                                      |
| ------- | --------- | ----------------------- | ------------------------------------ |
|         |           | with confirmed data     | Intrusion, Miscellaneous Errors and  |
Public Administration is primarily  disclosure  Privilege Misuse (Figure 91). It’s worth
targeted by a combination of financially  noting, however, that Privilege Misuse is
motivated criminals and State-affiliated  Top patterns System Intrusion,  only 0.01% more common than Social
actors, leading to a high frequency  Miscellaneous Errors  Engineering, so those two are still
of System Intrusion via vulnerability  and Privilege Misuse  essentially battling for supremacy.
exploitation and Ransomware.
represent 80% of
At first glance, the prominence of Error
| Additionally, the sector faces an  |     | breaches  |     |
| ---------------------------------- | --- | --------- | --- |
and Misuse might make you think, “Is the
unusually high rate of internal incidents
government really this prone to mistakes
| driven by Miscellaneous Errors— | Threat actors | External (56%),  |     |
| ------------------------------- | ------------- | ---------------- | --- |
and bad behavior?” Possibly—but there
| specifically Misdelivery due to the sheer  |     | Internal (44%)  |     |
| ------------------------------------------ | --- | --------------- | --- |
are some important context points to
| volume of correspondence—as well as  |     | (breaches)  |     |
| ------------------------------------ | --- | ----------- | --- |
intentional data mishandling. keep in mind when looking at NAICS 92:
|     | Actor motives | Financial (69%),  | •  We receive incident data about  |
| --- | ------------- | ----------------- | ---------------------------------- |
What is the same? Espionage (33%),  government entities from a limited
|     |     | Ideology (2%)  | number of contributors, and that  |
| --- | --- | -------------- | --------------------------------- |
The first two attack patterns in this  (breaches)  number is much smaller than the
sector remain the same as last year,  contributors reporting on private
|     | Data  | Personal (50%),  |     |
| --- | ----- | ---------------- | --- |
although Basic Web Application Attacks  sector incidents. Because the Public
Internal (39%), Other
gave way to Privilege Misuse this year.  compromised Administration dataset is smaller, the
The prevalence of External actors  (37%), Secrets (30%)  results are more susceptible to bias.
| targeting this industry remains   |     | (breaches)  |     |
| --------------------------------- | --- | ----------- | --- |
•  On the positive side, the government-
consistent YoY.
Initial access  Exploitation of  related data we do receive tends to be
vector  vulnerabilities (40%),  detailed and high quality. This allows
|     |     | Phishing (20%),  | for a more granular, in-depth view  |
| --- | --- | ---------------- | ----------------------------------- |
breakdown
|     |     | Credential abuse (8%)  | of what’s happening, even though it  |
| --- | --- | ---------------------- | ------------------------------------ |
reflects fewer organizations overall.
(breaches)
•  An even more critical factor is that
|     | Other metrics | Human element (69%),  |     |
| --- | ------------- | --------------------- | --- |
government entities often operate
Third-party (36%)
under stricter regulatory and reporting
requirements than most private sector
organizations. They are often required
to report more types of incidents and
at a higher level of detail.
Figure 91. Top patterns in Public Administration breaches over time (n for 2026
dataset=2,410)
2026 DBIR Industries 90

Figure 92. Top Actions in Public Figure 93. Top Hacking varieties in Public Administration breaches (n = 661)
Administration breaches (n=2,410)
With those caveats in mind, we can now When we examine hacking in greater Malware actions such as Ransomware,
look more closely at what drives the detail (Figure 93), the Exploitation of Backdoors, C2, disabling controls and
patterns that appear at the top of the list. vulnerabilities is predominant, accounting evading defenses are in frequent use.
for 82% of hacking-related breaches If we require any further clarity on why
In Public Administration, Hacking (38%)
in government. Evade defenses also the patterns fall where they do, a look
and Malware (43%) actions show up in
appears at an unusually high rate, at these Malware actions provides
roughly equal proportions (Figure 92),
present in 64% of breaches involving it. This blend of activity reflects how
which tracks with what we see across
hacking. Finally, the Use of stolen Ransomware and other complex attack
most industries this year. Given that more
credentials is a common tactic for scenarios typically unfold.
complex attacks tend to blend multiple
threat actors targeting government
techniques (and with System Intrusion
entities, occurring in 59% of hacking-
sitting in the top spot), that balance is
related breaches.
not exactly shocking. What is notable,
however, is that Hacking and Malware
appear at lower rates in breaches here
than in many other verticals.
2026 DBIR Industries 91

Figure 94. Actor varieties in Public Administration breaches (n=1,146) Figure 95. Actor motives in Public
Administration breaches (n=1,201)
In this segment, a quick look at the main State-affiliated actors also feature This type of action is part of a broader
threat actors is quite illuminating. Figure heavily, appearing in just over one-third pattern of Chinese cyberespionage
94 does a nice job of summarizing of breaches (35%) and frequently acting aimed at U.S. critical infrastructure and
who is driving the action in Public with an Espionage motive (33%) (Figure national security frameworks primarily
Administration. External actors make up 95). One example of this kind of activity due to rising global political tensions.
a slim majority of breaches at 56%, but was the breach of the U.S. Department
In other words, this sector is contending
Internal actors still accounted for of the Treasury by the Chinese nation
with a mix of financially motivated
a substantial portion of incidents in state hacking group Silk Typhoon, in
criminal groups and state-aligned actors
NAICS 92. which a vulnerability present in the
focused on intelligence gathering.
software of a third party’s cloud-based
On the External side, organized criminal This is what ultimately puts System
support services was exploited.110
groups are the primary offenders and Intrusion in the number one spot
are, unsurprisingly, mostly in it for the among the patterns.
money (69% financially motivated).
110. govinfosecurity.com/report-chinese-hackers-breached-cfius-a-27274?rf=2025-01-13_ENEWS_SUB_
GIS__Slot1_ART27274
2026 DBIR Industries 92

We all make (the You did that on
same) mistakes. purpose!
The Miscellaneous Errors pattern Shifting from honest mistakes
makes a strong showing in this sector: to intentional behavior, misuse-
Instances of this pattern (31%) are related breaches in this sector are
considerably higher here than in most overwhelmingly about Data mishandling
other verticals. Misdelivery, once again, (82%). At its core, Data mishandling
rises to the top as the dominant error is the inappropriate use of data, and it
type, keeping pace with what we see in wears many hats: Sending information
nearly every other sector. Misdelivery through unauthorized channels,
is, at its core, what it sounds like: Data convenient workarounds that put data
intended for one recipient is sent to at risk, or storing data in ways that don’t
someone else. Of all the industries where meet policy or regulatory requirements
this can happen, Public Administration all qualify.
is perhaps the easiest to understand.
The second most common flavor of
There is a large chain of individuals to
misuse is Privilege abuse, appearing
notify—often by letter or email—that
in 18% of misuse-related breaches. In
they did something wrong or that they
these cases, the actors are not breaking
owe a few dollars more to the powers
in—they are simply logging on. They
that be, and that sheer volume creates
deliberately use the legitimate access
room for mistakes.
they already have to systems or data
Misdelivery can also involve printed for an improper purpose, typically to
correspondence or electronic gain some real (or at least perceived)
communications. Whether it is a physical personal benefit.
letter, an email or a form that must be
Misuse can be insidious and difficult
filled out in triplicate and returned, it
to detect if all of your organization’s
is surprisingly easy to make an “off by
controls are outward facing, looking
one” error and send it to the wrong
only for the attacker trying to get in
person. Misdelivery accounts for 88%
from the outside. Part of those security
of all errors in the Public Sector. For
fundamentals is to make sure you can
comparison, the second most common
detect malicious activity, even when it is
error type—Classification error—comes
“coming from inside the house.”
in at just 4%. If your organization sends
out a large volume of correspondence, it
would be wise to implement safeguards
to reduce this all-too-common problem
(and the government is far from alone
here; large healthcare and insurance
firms with their constant mailings face
similar exposure).
For anyone hoping for a silver lining,111
it’s worth noting that most government
errors are not the result of inadequate
processes (1%) or poor technology
(9%) but of plain old Carelessness
(91%)—which does not exactly
inspire confidence.
111. We will be sure to let you know as soon as we find one.
2026 DBIR Industries 93

Retail
I have a
Summary
coupon code.
Retail organizations face persistent
threats from external attackers exploiting Few shoppers can resist a good deal.
vulnerabilities, stealing credentials and This is also true of attackers, and they
Phishing. These activities often lead have been compromising systems like
to ransomware attacks and data theft, they were on final clearance.
with third-party systems and internal
This year, the number of incidents rose
corporate data becoming increasingly
slightly, but the number of breaches
valuable targets.
nearly doubled. Despite that, the top
three patterns essentially remain the
What is the same?
same as last year, just in a different order.
System Intrusion still leads, while Basic
The top three patterns remained the
Web Application Attacks and Social
same, but their order of supremacy
Engineering continue to dance around
shifted a bit. The patterns have been the
each other.
same consistently for many years now,
but which is more prevalent in a given As Figure 96 illustrates, it is not until you
year changes. look all the way back to the 2020 DBIR
that you see a change in the membership
of the top three patterns. While they
have shuffled about a bit on the stage,
they have been close compatriots for
several years. This consistency tells us
that the same kinds of attacks are often
being leveraged against this industry’s
infrastructure year after year—with a
certain level of success. Case in point,
this past year saw clothing retailer Hot
Topic experiencing a breach affecting
57 million customers.112 Clearly there
remains significant incentive for
attackers to target this sector, given the
sheer volume of data up for grabs.
The unholy trio of Ransomware, Exploit
vuln and Use of stolen creds figured
prominently in the actions taken in
this sector (Figure 97), and when
combined with social attacks, you have
accounted for the most prevalent ways
in. Ransomware remains an ongoing
problem across this industry and was
the top malware action in breaches in
this sector.
2026 DBIR Industries 94
SCIAN 54–44
Frequency 997 incidents, 806
with confirmed data
disclosure
Top patterns System Intrusion,
Basic Web Application
Attacks and Social
Engineering represent
95% of breaches
Threat actors External (99%),
Internal (1%)
(breaches)
Actor motives Financial (85%),
Espionage (19%)
(breaches)
Data Internal (84%),
compromised Credentials (26%),
Secrets (20%), Other
(14%) (breaches)
Initial access Exploitation of
vector vulnerabilities (42%),
breakdown Credential abuse
(14%), Phishing (9%)
(breaches)
Other metrics Third-party (68%),
Human element (58%)
(breaches)
Figure 96. Top patterns in Retail breaches over time (n for 2026 dataset=806)
112. github.com/vz-risk/VCDB/issues/21205

The social varieties most commonly seen
in these breaches have been Phishing
and Pretexting, with the former almost
twice as common as the latter, as seen
in Figure 98. That makes some sense,
since Phishing tends to be the lower-
effort attack, where Pretexting tends to
take a bit more time and skill to achieve
a successful result (from the attacker’s
perspective). However, since both tactics
have been quite successful for the
attackers, it behooves organizations to
have easy methods for people to report
when they have become victims of these
kinds of attacks.
Espionage-motivated actors increased
again this year, rising from 9% to 19% of
breaches where the motive was known.
This suggests more sophisticated actors
have taken notice of this sector and are
turning their attention to what kinds of
Figure 97. Top Action varieties in Retail Figure 99. Top Data varieties
breaches (n=719) useful data their victims may have. compromised in Retail breaches (n=721)
While this sector once saw primarily
Payment card data compromised, threat
actors have evolved and now target
any data they can monetize, leading to
a more diverse mix of data types being
affected. Internal data, which can include
plans, strategies and other information of
value to Espionage-motivated attackers
and ransomware actors looking for
leverage rose from 65% last year to
84%. Figure 99 has the details.
Figure 98. Top Social actions in Retail
breaches (n=120)
2026 DBIR Industries 95

Focused
analysis
/06

Small- and medium-
sized businesses
Here, we view our data through the
lens of organizational size, to give a
| Summary | Frequency | 7,256 incidents, 7,152  |                                            |
| ------- | --------- | ----------------------- | ------------------------------------------ |
|         |           | with confirmed data     | perspective for the smaller organizations  |
Small organizations are disproportionally  disclosure  that can get lost in the overall dataset.
impacted by Ransomware and face   For our purposes, organizations with
many of the same threats as other  Top patterns System Intrusion,  fewer than 1,000 employees are
industries and organizations but often  Basic Web Application  considered small businesses. Hiring
with less resources available. Attacks and Social  that 1,001st employee moves you to the
|                   |     | Engineering represent  | enterprise category. Welcome to the   |
| ----------------- | --- | ---------------------- | ------------------------------------- |
| What is the same? |     | 100% of breaches       | big leagues!                          |
Being a small organization, you may
| System Intrusion, Basic Web Application  | Threat actors | External (100%)  |     |
| ---------------------------------------- | ------------- | ---------------- | --- |
mistakenly think that your threat
(breaches)
Attacks and Social Engineering continue  profile and who would be interested
to be the main drivers of breaches
Actor motives Financial (100%)  in compromising you are significantly
in SMBs.
different from everyone else. That is,
(breaches)
until you find yourself on the wrong
side of a ransomware attack. Overall,
|     | Data  | Internal (97%),  |     |
| --- | ----- | ---------------- | --- |
SMBs face similar types of threats
|     | compromised | Credentials (31%),  |     |
| --- | ----------- | ------------------- | --- |
as everyone else, including the same
System (1%), Other
breach patterns that show across many
(1%) (breaches)
different industries, and this has been the
Initial access  Exploitation of  case for many years now. While the top
three patterns changed slightly (Figure
|     | vector  | vulnerabilities (26%),  |     |
| --- | ------- | ----------------------- | --- |
100), System Intrusion remains the top
|     | breakdown | Credential abuse  |     |
| --- | --------- | ----------------- | --- |
pattern in small organization breaches,
(13%), Phishing (9%)
while Social Engineering and Basic Web
(breaches)
Application Attacks switched positions.
Other metrics Third-party (55%),  Unsurprisingly, financially motivated
|     |     | Human element (45%)  | External actors are perpetrating the  |
| --- | --- | -------------------- | ------------------------------------- |
majority of the breaches here.
(breaches)
Figure 100. Top patterns in SMB breaches over time (n for 2026 dataset=7,152)
2026 DBIR Focused analysis 97

When we examine the specific actions
impacting SMBs, we’re struck with
a heavy dose of déjà vu, as we see
Ransomware, Use of stolen credentials
and Exploit vulnerabilities show up in the
top (Figure 101). As we’ve discussed in
our section on Ransomware (found in
the “System Intrusion” pattern section),
these actors are often casting out
wide nets to compromise as many
organizations as possible in the hope
that at least some of the victims will pay.
For many of these attacks, they’re
opportunistic in nature, and it’s not so
much about industry or the revenue of
the victims but the fact that the victims
had credentials that were compromised
(38%) or unpatched vulnerabilities in
edge devices (29%) that resulted in them
being victimized. Of the Ransomware
cases where we have information on
the organization size, we found that Figure 101. Top Action varieties in SMB
about 96% of Ransomware victims were breaches (n=6,182)
SMBs. While SMB Ransomware cases
may rarely make the news, they certainly
make it into our dataset.
In terms of the data stolen from SMBs,
Internal and Credentials remain the
primary data types taken, while Personal
dropped off the list entirely. Internal data
is one of the common enumerations
that’s selected when it comes down
to these ransomware cases, as it’s not
always clear as to what was taken,
but odds are it was likely some type of
non-public data that the actors are then
trying to extort.
2026 DBIR Focused analysis 98

Regions
/07

Regional analysis
In this section, we examine breaches We define world regions in accordance LAC: Latin America and Caribbean,
from a macro-regional perspective to with the United Nations M49113 standards, which consists of breaches in South
highlight how trends differ or remain which combine super-regions and sub- America (005), Central America (013)
consistent across geographical regions. regions. Based on this framework, we will and Caribbean (029)
examine the following regions:
Our visibility into any given area is NA: Northern America (021), which
determined by several variables, APAC: Asia and the Pacific, including primarily consists of breaches in the
including regional disclosure laws, our Southern Asia (034), South-eastern Asia United States and Canada
specific datasets and the locations (035), Central Asia (143), Eastern Asia
Longtime readers will recognize the at-a-
where our contributors conduct (030) and Oceania (009)
glance tables located at the top of each
business. If you feel your region is
EMEA: Europe, Middle East and Africa, major section. We have combined these
not adequately represented in the
including North Africa (015), Europe to provide a quick comparison across all
following pages, please contact us
(150) and Eastern Europe (151) and regions regarding incident frequency, top
about becoming a data contributor and
Western Asia (145) patterns and other key metrics.
encourage other organizations in your
area to do the same.
Region Frequency Top patterns Threat Actor Data Initial access Misc
actors motives compromised vectors
APAC 5,229 System Intrusion, External Financial Internal (70%), Exploitation of Third-party
incidents, Basic Web (99%), (70%), Credentials vulnerabilities (69%),
2,855 with Application Internal (1%) Espionage (36%), Other (42%), Credential Human
confirmed Attacks and Social (breaches) (36%) (35%), Secrets abuse (25%), element
data Engineering (breaches) (30%) (breaches) Phishing (15%) (71%)
disclosure represent 97% (breaches) (breaches)
of breaches
EMEA 8,245 System Intrusion, External Financial Internal (73%), Exploitation of Third-party
incidents, Social Engineering (80%), (76%), Other (49%), vulnerabilities (54%),
6,060 with and Miscellaneous Internal (20%) Espionage Personal (34%), (47%), Phishing Human
confirmed Errors represent (breaches) (27%) Secrets (24%) (28%), Credential element
data 92% of breaches (breaches) (breaches) abuse (6%) (70%)
disclosure (breaches) (breaches)
LAC 813 incidents, System Intrusion, External Financial Internal (93%), Exploitation of Third-party
718 with Social Engineering (99%), (90%), Credentials vulnerabilities (74%),
confirmed and Basic Web Internal (1%) Espionage (23%), Secrets (44%), Phishing Human
data Application (breaches) (11%) (24%), Other (3%) (20%), Credential element
disclosure Attacks represent (breaches) (breaches) abuse (5%) (57%)
98% of breaches (breaches) (breaches)
NA 12,371 System Intrusion, External Financial Internal (77%), Exploitation of Third-party
incidents, Social Engineering (88%), (98%), Credentials vulnerabilities (43%),
8,426 with and Basic Web Internal (12%) Espionage (36%), Personal (30%), Credential Human
confirmed Application (breaches) (3%) (9%), Other (8%) abuse (20%), element
data Attacks represent (breaches) (breaches) Phishing (12%) (59%)
disclosure 87% of breaches (breaches) (breaches)
Table 5. At-a-glance table by region
113. unstats.un.org/unsd/methodology/m49
2026 DBIR Regions 100

Nevertheless, financially motivated
organized crime groups still account
for the bulk of breaches in APAC and
were involved in 67%. The influence of
organized crime groups in this region
can clearly be seen in the July 2025
breach affecting the airline Qantas.114
The personal data of more than five
million customers was stolen by a group
known as Scattered Lapsus$ Hunters via
a third-party platform. The criminal group
then placed extortion demands on the
victim and released the data when the
ransom was not paid. This incident was
one of Australia’s largest since 2022 and
underscores the continued risk of third-
Figure 102. Top patterns in APAC breaches over time (n for 2026 dataset=2,855)
party data stores and the downstream
impact they can create.
The APAC region Hacking is involved in 83% of breaches
With regard to the types of data stolen,
in APAC and Malware in 71%, compared
in case our readers have any lingering
to 64% and 63%, respectively, in
APAC is still contending with the same doubts regarding how strong the
the overall data, which is quite a
familiar patterns that have topped the Espionage signal is in APAC, the data
noticeable jump (Figure 103). Some of
charts there for the last few years. varieties should put them to rest. Secrets
that difference can be chalked up to
System Intrusion continues to lead by appear in 28% of APAC breaches. In
contributor bias in the region, based
a wide margin and is responsible for the overall dataset, those numbers drop
on who sends us data and what kinds
60% of breaches—still roughly three to 13%. That’s a clear indication that
of cases they see. Nevertheless, that
times the share of the next closest APAC is experiencing more breaches,
combination of Hacking and Malware is
patterns, even though it experienced in proportion where highly sensitive
a hallmark of multistep, more-complex
a sharp drop from 89% in the 2025 information is the main prize.
breaches that require both lateral
report. Social Engineering remains fairly
movement and persistence. Therefore,
steady with last year’s level at 21%. The
a significant portion of this uplift likely
standout change comes from Basic Web
reflects the higher volume of Espionage-
Application Attacks, which have doubled
related attacks in the APAC region.
since last year and now account for 22%
of breaches. That rise likely correlates The topic of espionage provides us with
with the prominence of the Use of stolen an excellent entry point for discussing
credentials as the leading Hacking who’s doing the attacking in APAC and
action, since those are often the fuel what’s driving them. Threat actors here
that powers the shorter, less- are almost entirely External, accounting
sophisticated Basic Web Application for 99% of breaches. State-affiliated
Attacks-style attacks. actors are responsible for a striking 36%
of breaches—more than in any other
APAC shares the same leading
region. Again, a certain amount of that
patterns—and by extension, the same
is a reflection of our contributor base
leading Action types—as the overall
in APAC, and some of it also reflects
dataset, but some of them show up more
regional geopolitics and where these
frequently here than elsewhere.
targets sit on the map.
Figure 103. Top Action varieties in APAC
breaches (n for APAC=2,855)
114. reuters.com/sustainability/boards-policy-regulation/qantas-says-customer-data-released-by-cyber-
criminals-months-after-cyber-breach-2025-10-12
2026 DBIR Regions 101

Collective Cyber Resilience in Action:
Operational Lessons from Responding to UNC3886
David Koh Cyberspace is a shared domain, and Third, public-private partnership is
securing it is a team sport. Sustaining imperative in cybersecurity, which is
digital trust therefore relies on collective ultimately a shared responsibility.
Commissioner of resilience, rather than individual The telcos proactively cooperated and
Cybersecurity and measures alone. The campaign by worked alongside government agencies
Chief Executive of the Advanced Persistent Threat (APT) throughout the operation, supporting
actor UNC3886 against Singapore’s investigations and implementing the
Cyber Security Agency
telecommunications infrastructure was necessary detection and remediation
(CSA) of Singapore
a timely reminder of this reality. The measures. The telcos have also
sophistication of the campaign made strengthened their defences through
detection challenging, and necessitated interventions such as joint threat hunting,
a coordinated national response across penetration testing, and uplifting their
government and industry. From this capabilities. This close partnership
experience, we share several operational enabled effective containment, limited
reflections that may be useful to fellow the threat actor’s activities, and
cyber defenders. safeguarded our essential services.
First, early detection and trusted Singapore has taken a transparent and
reporting channels are crucial. The threat measured approach in communicating
actor’s activities were first detected the cyber threats that we face. Beyond
by our telecommunications operators raising public awareness, transparency
(telcos), who proactively notified the also signals resolve and reinforces the
Singapore authorities. The prompt collective commitment to safeguard
notification enabled a swift whole-of- our networks and systems against
Government response, mounted in close sophisticated threats. We hope that
partnership with the telcos to contain sharing these lessons will reinforce and
and remediate the breach. demonstrate collective cyber resilience
in action, even as the threats grow more
Second, effective inter-agency
complex and frequent.
coordination was central to the response.
Codenamed ‘Operation Cyber Guardian’,
the effort became Singapore’s largest
coordinated cyber incident response to
date. More than 100 cyber defenders
were mobilised across agencies such as
CSA, the Infocomm Media Development
Authority (IMDA), the Centre for
Strategic Infocomm Technologies
(CSIT), the Singapore Armed Forces’
Digital and Intelligence Service (DIS),
the Government Technology Agency of
Singapore (GovTech), and the Internal
Security Department (ISD). The breadth
and scale of participation reflected the
sophistication of the threat, and affirmed
coordinated response as a key pillar of
Singapore’s cyber defence.
2026 DBIR Regions 102

The most substantive of the differences
with regard to EMEA has to do with
the Social actions category. Phishing in
EMEA shows up in 84% of social-related
breaches, which is 15% higher than
the overall dataset (69%). This lines up
neatly with another EMEA hallmark: a
higher share of State-affiliated actors.
Across the full dataset, State-affiliated
actors are involved in 14% of breaches;
in EMEA, that figure jumps to 23%. Not
surprisingly, that also tracks with a higher
rate of Espionage-motivated breaches
in EMEA (27%) compared to the overall
data (13%). This is certainly related to
the higher percentage of State-affiliated
Figure 104. Top patterns in EMEA breaches over time (n for 2026 dataset=6,060)
actors that we see here. Considering the
complex current political landscape in
The EMEA region For the overall dataset, 63% of breaches the region, it doesn’t come as a surprise
involve Malware, while EMEA edges to see the threat of Espionage continue
that out ever so slightly with the highest to persist.
System Intrusion, Social Engineering
regional share at 66%, up notably from
and Miscellaneous Errors are once
54% last year. Hacking-related breaches
again headlining the EMEA story, closely
in EMEA are at 59%, a bit lower than
mirroring last year. System Intrusion
the 64% we see across the full dataset.
accounts for 57% of breaches in the
Neither difference is statistically
region, up slightly from 53% last year.
earth-shattering, but together they do
Miscellaneous Errors moves in the
suggest that EMEA is now tracking a
opposite direction, dropping (though
bit closer to the global picture than it
not significantly) from 19% to 14%, while
has in previous years. As one might
Social Engineering holds steady at 22%
imagine, the high levels of malware and
of breaches, keeping its usual seat at
hacking in EMEA are representative of
the table.
the continued pressure that financially
In previous reports, we’ve been up front motivated organized crime actors
about a built-in tilt toward North America continue to exert by launching frequent
in our dataset, which is driven largely Ransomware attacks against targets in
by where many of our contributors are this region.
located. Over the last two to three years,
Meanwhile, Social (27%), Error (14%) and
we’ve pushed to widen that view and
Misuse (6%) actions all come in slightly
bolster coverage across other regions as
higher here than in the overall dataset.
much as possible. The results suggest
that these efforts have been successful
to some degree. As the bar chart in Figure 105. Top Action varieties in
EMEA breaches (n for EMEA=6,060)
Figure 105 shows, EMEA is dealing
with many of the same issues
we see elsewhere.
2026 DBIR Regions 103

Error actions tell a slightly different story.
In EMEA, Misdelivery leads the error
category at 50%. While Misdelivery is
also the top error type in the overall
dataset (61%), it appears less frequently
in EMEA by comparison. Loss, however,
is notably higher in EMEA at 19%, versus
11% in the rest of the dataset.
Misconfiguration-related breaches come
in at 17% for EMEA, compared to 13%
overall. Of these three, Misconfiguration
is arguably the most worrisome, even
if it’s less common than Misdelivery.
Accidentally sending an attachment
to the wrong recipient and exposing
a small amount of data is unfortunate,
but spinning up an unsecured cloud
database holding terabytes of PII is the
kind of mistake that can keep incident
responders and legal teams up at night.
Figure 106. Incidents and breaches by region
2026 DBIR Regions 104

Critical economic infrastructure
Any discussion regarding cybercrime in EMEA this year should
probably include some mention of the massive 2025 attack on
Jaguar Land Rover (JLR).115 This incident represents the most
economically damaging cyberattack in U.K. history, with an
estimated £1.9 billion in loss due to a grueling five-week business
interruption. This disruption rippled downstream to impact
approximately 5,000 entities, demonstrating that incidents that
affect an organization’s supply chain can quickly escalate into
loss for others involved, other than the criminals presumably.
The JLR breach was damaging to the economy as a whole. This
was a contributing factor to the U.K. gross domestic product
missing its projection by 0.1%,116 which could be part of the
reason why the government intervened with loans to support
JLR and their supply chain. This makes us think about the real
significance of critical infrastructure with today’s deep economic
interconnection and how to best support the private sector, in
general, against attacks of this magnitude.
As one of their response measures, the U.K. National Cyber
Security Centre (NCSC) has released a campaign to incentivize
companies to increase their cyber resilience,117 with a focus on
recovery planning and execution after a damaging attack.
115. bbc.com/news/articles/cy9pdld4y81o
116. reuters.com/world/uk/uk-economy-grows-01-q3-2025-11-13
117. ncsc.gov.uk/campaigns/cyber-resilience
2026 DBIR Regions 105

Wrap-up
/08

You are now free to return
to your organization’s ongoing
crisis management activities,
and thanks for reading.
Whether you used this report
to sharpen your defensive
strategy or simply dropped by
to find fault, we sincerely
hope you found it useful.
Each year, our goal is the same: While we are handing out thank- On behalf of the entire team,
to provide a compass that you’s, we thank you, our loyal we wish you a secure and
can assist you in navigating readers, for taking the time prosperous year. Finally, as
an increasingly chaotic to support us by reading and always, stay vigilant, stay out
environment by drawing attention sharing this document and by of the headlines and—most
to the threats that could be asking questions or making importantly—stay in touch.
the most impactful to your suggestions that enable us to
organization and supporting remain relevant in a world that
your decision-making when refuses to ever stand still.118
deploying resources. We hope
Looking toward next year,
that, to some degree, we have
we can’t help but notice a
accomplished that goal.
milestone on the horizon: 2027
As we do every year, we owe a will mark the 20th anniversary
massive debt of gratitude to our of the DBIR! We aren’t quite
data contributors. Without their sure where the time (or our
willingness to share their data hair) went, but we are already
and expertise, this report simply hard at work ensuring that our
wouldn’t exist. platinum anniversary edition is
the most impactful one yet.
118. Just a few weeks would be nice.
2026 DBIR Wrap-up 107

Year in review
Monthly snapshot as reported by the VTRAC Monthly Intelligence briefings and kindly
provided by Steven Baskerville, Darrin Kimes and Jim Meehan from the VTRAC team
January The identity and edge assault: The year opened with a strategic shift from traditional endpoints to core identity and edge
infrastructure. Chinese state-sponsored actor Silk Typhoon compromised the U.S. Treasury Department by stealing a
BeyondTrust security key, granting remote access to classified workstations. Simultaneously, the J-Magic campaign
targeted Juniper routers, utilizing a custom cd00r backdoor that scanned for “magic packets” to establish reverse shells
on VPN gateways. High-severity zero-days in Ivanti Connect Secure (CVE-2025-0282) were weaponized by UNC5337
to deploy the SPAWN malware ecosystem, providing persistent, unauthenticated access to hundreds of enterprise
networks. This month also saw a massive phishing campaign hijack 35 Chrome extensions, injecting data-stealing code
that impacted 2.6 million users.
February Bypassing the identity perimeter: Adversaries focused on the “Identity Crisis,” utilizing Device Code Authentication
phishing to bypass MFA for Microsoft 365 accounts by impersonating high-level government officials. The Akira
ransomware group demonstrated a novel persistence tactic by exploiting unsecured webcams to move laterally and
encrypt VMware ESXi shares while remaining invisible to Windows-based endpoint detection and response systems.
Law enforcement executed Operation PHOBOS AETOR, dismantling the 8Base/Phobos ransomware infrastructure
in Thailand, though the group’s affiliates rapidly pivoted to new Malware as a Service (MaaS) models. The month also
saw the viral emergence of DeepSeek-R1, which was immediately met with 100% successful jailbreaking campaigns to
generate malicious code.
March Cascading supply chain failures: Supply chain fragility took center stage as a cascading breach of GitHub Actions
exposed secrets for more than 23,000 repositories. China-nexus group UNC3886 (Weaver Ant) demonstrated extreme
technical depth by maintaining network access for four years and bypassing Juniper’s kernel-based file integrity (CVE-
2025-21590). Law enforcement seized the Garantex crypto exchange after it processed $96 billion in illicit transactions.
Meanwhile, the discovery of BADBOX 2.0 revealed a botnet of more than one million infected connected TVs used
for systemic ad fraud. North Korea officially launched Research Center 227, a unit dedicated to developing AI-driven
offensive hacking capabilities.
April High-leverage extortion: Threat actors pivoted toward high-leverage sectors where downtime causes immediate
systemic pressure. U.K. retailers Marks & Spencer, Co-op and Harrods were hit by ransomware—the Co-op breach alone
compromised the personal data of 6.5 million members. A hacker known as “rose87168” claimed a massive breach of
Oracle Cloud, exfiltrating 6 million records from 140,000 tenants. A critical zero-day in CrushFTP (CVE-2025-31161)
allowed unauthenticated administrative takeovers via AWS4-HMAC race conditions.
May The zero-day sprint: A sharp escalation in zero-day activity saw 15 such flaws added to the KEV catalog. The Russian
Qilin ransomware group and China-nexus actors exploited a critical SAP NetWeaver unauthenticated file upload flaw
(CVE-2025-31324) weeks before disclosure to deploy webshells globally. Russian hacktivists (NoName057(16))
launched persistent DDoS attacks against Dutch and Romanian state websites in retaliation for military aid to Ukraine.
Ivanti Endpoint Manager Mobile (EPMM) software was hit by a zero-day exploit chain (CVE-2025-4427/4428) delivered
via AWS S3 buckets to gain remote code execution on managed devices.
June Blurring state and criminal lines: The distinction between financial extortion and state-sponsored data collection
vanished. ShadowPad variants were deployed by China-aligned FamousSparrow against research institutes in the U.S.
and Mexico. Operation Endgame disrupted Lumma Stealer and DanaBot infrastructure across 1,300 domains, though
developers restored MaaS operations within days. A massive 631GB database leak exposed four billion user records
from Chinese platforms WeChat and Alipay. French authorities arrested five operators of the BreachForums platform,
including individuals associated with the ShinyHunters group.
2026 DBIR Wrap-up 108

July Systemic infrastructure fragility: Fragility was underscored by the SharePoint ToolShell zero-day chain (CVE-2025-
53770), allowing Chinese actors such as Linen Typhoon to gain unauthenticated access to hundreds of high-value
networks. Citrix NetScaler faced a second crisis with CitrixBleed 2 (CVE-2025-5777), which was exploited as a zero-
day to leak session tokens from critical infrastructure in the Netherlands. In Brazil, the Datzbro Android trojan began
utilizing AI-generated Facebook events to trick elderly users into device-takeover attacks.
August AI and infrastructure sabotage: AI moved from theoretical research into offensive implementation. MITRE revealed
LameHug, an APT28 experiment using Alibaba’s Qwen LLM to generate polymorphic malware code on demand.
ShinyHunters (UNC6040) launched a massive supply-chain campaign, exploiting compromised Salesloft Drift OAuth
tokens to pivot into the Salesforce instances of major firms such as Google, Zscaler and Cisco. The PromptLock
malware emerged as the first AI-powered ransomware to generate cross-platform encryption scripts dynamically via
local LLMs. Pro-Russian hackers were suspected of sabotaging a Norwegian dam, breaching control systems to
release water.
September The industrial impact: The industrial sector faced its costliest cyber event in U.K. history as a ransomware attack on
Jaguar Land Rover (JLR) halted production for five weeks, causing £1.9 billion in damages. Amazon revealed it thwarted
more than 1,800 North Korean “remote worker” infiltration attempts by identifying a unique 110 ms keystroke input lag. A
self-replicating npm worm called Shai-Hulud compromised more than 500 packages to exfiltrate developer credentials
and GitHub access tokens.
October Volumetric and hypervisor warfare: Record-breaking volumetrics defined the month as the Aisuru botnet (300,000 IoT
hosts) launched a record 29.7 Tbps DDoS attack, nearly doubling previous peaks. State-sponsored actors exploited
Cisco ASA zero-days (CVE-2025-20333) to deploy the LINE VIPER and RayInitiator malware families. Federal
authorities seized nearly 130,000 Bitcoins (approx. $15 billion) from the Cambodian Prince Group, targeting a massive
investment fraud and human trafficking empire. Analysis found that 29% of KEV vulnerabilities were attacked before
public disclosure this year.
November The vishing and SaaS siege: Vishing (voice phishing) surged, with the FakeCall malware intercepting calls on infected
mobile devices to steal banking credentials. ShinyHunters expanded their SaaS siege, breaching Gainsight to access
285 additional Salesforce instances. A nation-state actor gained long-term access to F5’s development environment,
exfiltrating BIG-IP source code and undisclosed vulnerability data. Airstalk malware emerged in a supply chain attack
that misused MDM APIs as a “dead drop” for C2 communication.
December Mass exploitation of modern stacks: The year closed with the widespread exploitation of React2Shell (CVE-2025-
55182), an RCE vulnerability in React Server Components exploited by China-nexus groups to deploy backdoors across
39% of cloud environments. North Korean hackers reached a record annual theft of $2.02 billion in cryptocurrency. The
discovery of VoidLink, a malware framework written in six days by an AI agent, marked a point of no return for automated
threat development.
2026 DBIR Wrap-up 109

Appendices
/09

Appendix A:
Methodology
One of the things readers value most All incidents included in this report were Incident data
about this report is the level of rigor and reviewed and converted (if necessary)
integrity we employ when collecting, into the VERIS framework to create a
Our data is non-exclusively multinomial,
analyzing and presenting data. Knowing common, anonymous aggregate dataset.
meaning that a single feature, such as
our readership cares about such things If you are unfamiliar with the VERIS
“Action,” can have multiple values (e.g.,
and consumes this information with a framework, it is short for Vocabulary for
“Social,” “Malware” and “Hacking”).
keen eye helps keep us honest. Detailing Event Recording and Incident Sharing, it is
This means that percentages do not
our methods is an important part of free to use, and links to VERIS resources
necessarily add up to 100%. For example,
that honesty. can be found throughout this report.
if there are five botnet breaches, the
To begin with, we would like to remind The collection method and conversion sample size is five. However, because
our readers that science comes in two techniques differed among contributors. each botnet used phishing, installed
flavors: creative exploration and causal In general, three basic methods keyloggers and used stolen credentials,
hypothesis testing. The DBIR is squarely (expounded below) were used to there would be five Social actions, five
in the former. While we may not be accomplish this: Hacking actions and five Malware actions,
perfect, we believe we provide the best adding up to 300%. This is normal,
obtainable version of the truth based 1. Direct recording of paid external expected and handled correctly in our
on the datasets we have available (to forensic investigations and related analysis and tooling.
intelligence operations conducted by
a given level of confidence and under
Verizon using the VERIS Webapp Another important point is that when
the influence of biases acknowledged
looking at the findings, “unknown” is
later). However, proving causality is best 2. Direct recording by partners equivalent to “unmeasured.” Which is
left to randomized control trials. The using VERIS to say that if a record (or collection of
best we can do is correlation. And while
records) contains elements that have
3. Converting partners’ existing schema
correlation is not causation, they are often
been marked as “unknown” (whether
into VERIS
related to some extent, and often useful.
it is something as basic as the number
All contributors received instruction to of records involved in the incident or as
Non-committal omit any information that might identify complex as what specific capabilities a
organizations or individuals involved. piece of malware contained), it means
disclaimer that we cannot make statements about
Some source spreadsheets are converted
that particular element as it stands in the
to our standard spreadsheet formatted
We would like to reiterate that we make through automated mapping to ensure record—we cannot measure where we
no claim that the findings of this report consistent conversion. Reviewed have too little information. Because they
are representative of all data breaches in spreadsheets and VERIS Webapp JSON are unmeasured, they are not counted in
all organizations at all times. Even though are ingested by an automated workflow sample sizes. The enumeration “Other,”
we believe the combined records from that converts the incidents and breaches however, is counted because it means
all our contributors more closely reflect within into the VERIS JSON format as that the value was known but not part
reality than any of them in isolation, it is necessary, adds missing enumerations, of VERIS (or not one of the other bars
still a sample. And although we believe and then validates the record against if found in a bar chart). Finally, “Not
many of the findings presented in this business logic and the VERIS schema. Applicable” (normally “n/a”) may be
report to be appropriate for generalization The automated workflow subsets the counted or not counted depending on the
(and our conviction in this grows as we data and analyzes the results. claim being analyzed.
gather more data and compare it to that Based on the results of this exploratory We make liberal use of confidence
of others), bias still exists. analysis, the validation logs from the intervals to allow us to analyze smaller
workflow and discussions with the sample sizes. We have adopted a few
The DBIR process partners providing the data, the data is rules to help minimize bias in reading such
cleaned and reanalyzed. This process data. Here we define “small sample” as
runs nightly for roughly two months as fewer than 30 samples.
Our overall process remains intact and
data is collected and analyzed.
largely unchanged from previous years.119 1. Sample sizes smaller than five
are too small to analyze.
119. As does this sentence
2026 DBIR Appendices 111

2. We won’t talk about count or Lastly, for something to be eligible for We also acknowledge that some types
percentage for small samples. inclusion into the DBIR, we have to know of breaches that are very common in
This goes for figures, too, and is about it, which brings us to several a specific analysis period—looking
why some figures lack the dot for potential biases. at you, Ransomware—might end up
the median frequency. being overrepresented due to the vast
availability of samples. We often try
3. For small samples, we may talk Acknowledge-
to point it out in the report when that
about the value being in some range
ment and analysis is the case.
or values being greater/less than each
other. These all follow the confidence The third source of bias is confirmation
of bias
interval approaches listed previously. bias. Because we use our entire dataset
for exploratory analysis, we cannot test
Many breaches go unreported (though specific hypotheses. Until we develop
Incident eligibility
our sample does contain some of those, a collection method for data breaches
as well). Many more are as yet unknown beyond a sample of convenience, this is
For a potential entry to be eligible for by the victim (and thereby unknown to probably the best that can be done.
the incident/breach corpus, a few us). Therefore, until we (or someone) can
requirements must be met. The entry conduct an exhaustive census of every As stated earlier, we attempt to mitigate
must be a confirmed security incident breach that happens in the entire world these biases by collecting data from
defined as a loss of confidentiality, each year (our study population), we must diverse contributors. We follow a
integrity or availability. In addition to use sampling. Unfortunately, this process consistent multiple-review process and
meeting the baseline definition of introduces bias. when we hear hooves, we think horses,
“security incident,” the entry is not zebras.120 We also try and review
assessed for quality. The first type of bias is random bias findings with subject matter experts in
introduced by sampling. This year, our the specific areas ahead of release.
We create a subset of incidents that pass maximum confidence is +/- 0.7% for
our quality filter. The details of what is a incidents and +/- 0.9% for breaches,
Non-incident data
“quality” incident are: which is related to our sample size. Any
subset with a smaller sample size is
• The incident must have at least seven
going to have a wider confidence margin. Since the 2015 issue, the DBIR has
enumerations (e.g., threat actor variety,
We’ve expressed this confidence in included data that requires analysis that
threat action category, variety of
the complementary cumulative density does not fit into our usual categories
integrity loss) across 34 fields OR be
(slanted) bar charts, hypothetical of “incident” or “breach.” Examples
a DDoS attack. Exceptions are given
outcome plot (spaghetti) line charts and of non-incident data include malware,
to confirmed data breaches with fewer
quantile dot plots. However, sometimes vulnerability management, phishing,
than seven enumerations.
the nature of non-incident data we may DDoS, internet-wide honeypots, internet-
• The incident must have at least one be working with is not conducive to this wide scanning and other types of data.
known VERIS threat action category confidence level analysis, and we might The sample sizes for non-incident
(e.g., Hacking, Malware). have some plain vanilla bar and line charts data tend to be much larger than the
throughout the report. More on non- incident data but from fewer sources.
In addition to having the level of details
incident data in the next section. We make every effort to normalize the
necessary to pass the quality filter, the
data (for example, weighting records
incident must be within the timeframe of The second source of bias is sampling
by the number contributed from the
analysis (Nov 1, 2024, to Oct 31, 2025, bias. We strive for “the best obtainable
organization so all organizations are
for this report). The 2025 caseload is version of the truth” by collecting
represented equally). We also attempt
the primary analytical focus of the report, breaches from a wide variety of
to combine multiple partners with
but the entire range of data is referenced contributors. Still, it is clear that we
similar data to conduct the analysis
throughout, notably in trending graphs. conduct biased sampling. For instance,
wherever possible. Once analysis is
We also exclude incidents and breaches some breaches, such as those publicly
complete, we try to discuss our findings
affecting individuals that cannot be tied disclosed, are more likely to enter
with the relevant partner or partners
to an organizational attribute loss. If your our corpus, while others, such as
so as to validate the findings against
friend’s laptop was hit with ransomware classified breaches, are less likely.
their knowledge of the data and make
while downloading a game cheat, it would
sure we are representing it correctly.
not be included in this report.
120. A unique finding is more likely to be something mundane, such as a data collection issue, than an
unexpected result.
2026 DBIR Appendices 112

Appendix B:
U.S. Secret Service
The autonomous These threats are increasing in volume
By Assistant Special Agent in
and diversity, and even unskilled
adversary
Charge Richard Hersh III, criminals can launch sophisticated
campaigns with just a few queries
Digital Forensics Incident
The digital battlefield continues to to an AI platform. Law enforcement
Response-Network Intrusion
evolve. Agentic AI (autonomous AI responders and investigators face a
PM Bernard Wilson, and capable of independent action) is clear challenge: they must adapt or risk
Management and Program redefining cybercrime by creating falling behind.
adversaries that can operate without
Analyst Stephen Hampton, Autonomous adversaries are pushing
human limits. Traditionally, cybercriminals
cybercrime into a new era, one
United States Secret Service relied on human effort and technical
where attacks are limited only by the
skill to execute attacks. Now, Agentic AI
imagination of the algorithms behind
systems can automate every stage of
them. The Secret Service has a mandate
cybercrime: reconnaissance, phishing,
to investigate these cybercrimes under
data theft, and even laundering stolen
the Computer Fraud and Abuse Act,
and illicit assets. The United States
codified at Title 18, United States Code,
Secret Service is on the front lines with
Section 1030.121 Under this authority,
an unwavering commitment to counter
the Secret Service continues to evolve
cyber threats.
investigative techniques, advance
Agentic AI has the potential to lower the analytics, and leverage collaborative
barrier for sophisticated cyberattacks expertise across public and private
while expanding their scope. Agentic sectors to counter AI-driven threats.
AI can run persistent campaigns, adapt The Secret Service is leaning into
tactics in real time, and target thousands, this challenge, ensuring that even as
if not millions, of victims simultaneously. adversaries become more autonomous,
As a result, cyberattacks are often faster, law enforcement remains agile,
smarter, and more relentless. Agentic AI innovative, and relentless in pursuit
doesn’t just scale up old tricks, it invents of cybercriminals.
new ones, automates deception, and
As a defense tool, Agentic AI can
exploits vulnerabilities at a pace that
deploy real-time monitoring, automate
overwhelms traditional defenses.
threat detection, and implement
This shift is both profound and urgent innovative response platforms, which
for law enforcement, and a call to can significantly reduce Mean Time
innovate with exceptional operational to Respond/Repair (MTTR) and are
technologies. Adversaries that never essential tools in the fight against
sleep can test law enforcement autonomous adversaries.
capabilities and incident response
The stakes have never been higher.
expertise. This new type of cybercriminal
The battle is just beginning. The Secret
operates without human fatigue or skill
Service refuses to stand still.
limitations. Agentic AI can generate
convincing scam messages, impersonate
trusted contacts, and orchestrate
complex attacks seamlessly.
121. uscode.house.gov/view.xhtml?req=(title:18%20section:1030%20edition:prelim)
2026 DBIR Appendices 113

Appendix C:
Using the DBIR
for Security Risk
Decisions
Every year, thousands of security Mistaking the statistic for probability is
By Tony Martin-Vegue,
professionals follow the same ritual: a common mistake, and it can lead to
Cyber Risk Expert download the DBIR, read the findings, misguided risk decisions.
and use them to understand trends,
Unpacking what the statistic means is
track the evolving threat landscape,
the key. Think of it this way: when we
inform security decisions, and
say ransomware was present in 48%
support planning.
of breaches, what we’re really saying is
The Verizon Data Breach Investigations "among organizations that got breached
Report is one of a kind, a longitudinal AND detected it AND reported it, or had
study of security trends that has been it reported by someone else, 48% of
ongoing for 19 years. It’s a gold mine those breaches involved ransomware."
of useful data for organizations, large
Think for a moment about the filter that
and small. However, some security
creates. For something to appear in the
professionals struggle to get from
DBIR dataset, the attack had to succeed,
"Phishing was involved in 14% of
someone had to notice it, it had to meet
healthcare breaches" to actionable
eligibility/quality criteria, and it had to be
decisions. How do you use evidence
available to contributors.
like this to improve your security and
risk decisions? Each one of those steps is important.
Each one creates a filter for what you
This appendix provides practical
see. So, it's not a probability of a data
advice on using DBIR data in a way
breach. It’s a statistic about observed
that withstands scrutiny within your
organizations that experienced an
organization. You’ll understand where
incident serious enough to end up in
the data comes from, what it means,
the dataset, and among those, 48%
and how to use it.
involved ransomware.
The DBIR reports detected and reported
Understanding
data breaches and the types and
the statistics patterns of those incidents. It does not
capture attacks that failed, activity that
was blocked or disrupted before causing
One of the first things to understand
harm, or incidents that went undetected
when reading the report is how to
or never met reporting criteria. All of
interpret the statistics. For example,
those nuances matter for understanding
when the DBIR reports that "ransomware
both your risk and the statistics the DBIR
was present in 48% of breaches," that
is reporting.
does not mean your organization or your
sector has a 48% chance of being hit If you miss this distinction, everything
by ransomware. else you interpret about the report will
be off.
2026 DBIR Appendices 114

Using the DBIR The very large sample size across many What evidence
sectors provides more comprehensive
as your baseline helps you adjust
coverage. You’re seeing a reasonably
wide distribution of outcomes in the real
the baseline
The DBIR splits things out by industry, world, not just the worst-case scenarios.
size, and region for a reason: threat However, you’re not seeing organizations
landscapes look different depending that successfully defended against Once you’ve identified your relevant
on where you sit. What’s common for a attacks, and you’re not seeing breaches DBIR baseline, the next step is figuring
hospital might be rare for a retailer. What that went undetected. out whether you should adjust it up or
hits a small business isn’t the same as down for your organization. Here’s what
what goes after an enterprise. Your first What this means for you: the DBIR evidence matters:
shows you patterns in breaches when
step is to find your relevant demographic
they occur in your sector. It tells you
in the report: your industry vertical, Strong evidence:
what attack methods succeeded, what
your organization size, and your
vulnerabilities got exploited, and what
geographic region. Your own history. This is the
controls failed. It doesn’t tell you your
strongest evidence you have. If you’ve
With tens of thousands of incidents overall probability of being breached.
been successfully phished multiple
analyzed over 19 years, the DBIR That depends on your specific situation.
times, that’s direct evidence of your
provides a baseline for what has
Now the question becomes: when you vulnerability to phishing attacks. If you’ve
historically happened to organizations in
look at these patterns, are you better been hit by ransomware before, that
your category. This provides very useful
prepared than what’s typical in these gives you concrete evidence of your
context and tells you what an attack
incidents, worse, or about the same? exposure. Your track record provides
would look like at your organization.
Do you have stronger controls than real data about how your defenses
those that failed in these breaches? perform under actual attack conditions.
Understanding Weaker detection capabilities? Different
What attackers find when they
threat exposure?
the baseline and test you. Pen test results, red team
Understanding where you stand relative findings, and bug bounty reports show
its limitations to these patterns is how you turn DBIR you what external testers discover
statistics into useful information for your about your defenses. If they’re finding
There’s an important caveat here: the organization. Practical ways to assess critical vulnerabilities, that’s evidence
DBIR only captures organizations that where you stand include conducting that you may be more vulnerable than
got breached, detected it, and had it internal control assessments and the baseline. If they’re coming up mostly
reported. This creates selection bias, comparing your security posture against empty, that suggests stronger defenses.
which means the sample (breached sector benchmarks. Many research What controls do you have versus
organizations in the report) may be firms, vendors, and industry reports what failed in breaches? DBIR findings
unrepresentative of the whole population publish control benchmarking data for often describe what was missing or
(all organizations). By definition, these different sectors, and these can help what broke in successful attacks:
organizations in the report had defenses you understand whether your controls No MFA, unpatched critical systems,
that failed. Does that mean they all are stronger, weaker, or similar to what’s weak passwords, successful social
had worse security than average? typical in organizations like yours. engineering, etc. Compare that list to
Not necessarily. The sample includes This can help you adjust the baseline your environment, and if you have some
organizations across the spectrum: DBIR statistic up or down based on of the same gaps, you may be more
some with weak security that were your findings. vulnerable than the baseline. If you’ve
easy targets, some with decent security addressed those common failure points,
that got unlucky, and some with strong you may be better positioned.
security that faced sophisticated,
determined attackers.
2026 DBIR Appendices 115

Your ability to detect problems. The Applying this Six months later, simulated phishing
DBIR only captures breaches that were click rates dropped from 28% to 8%.
in practice
detected. If your detection capabilities The next pen test shows measurable
are limited, you might have exposure improvement. They’ve improved their
you don’t know about yet. Strong A hospital reads the DBIR and position relative to the baseline, and
detection and monitoring capabilities sees that credential compromise their risk profile has changed because
suggest you’re better positioned than following successful phishing is the security projects have moved
organizations that miss breaches entirely. common in healthcare breaches. them to a stronger position than
They ask themselves: Should the industry baseline.
we adjust the baseline up or
Supporting evidence:
down for our organization?
Making it
How you stack up against baseline
They look at the evidence:
requirements. If you’re barely meeting actionable
compliance minimums, you’re likely • MFA is deployed on email and the EHR
close to the baseline. If you’re exceeding system, but not on VPN
The DBIR gives you 19 years of data
requirements significantly, that suggests
• Successfully phished twice in the past about what happens when organizations
stronger controls.
eighteen months in your sector get breached. Use it
What your peers tell you. Conversations as your starting point, then gather
with similar organizations can help • Last pen test showed weak password evidence about your specific situation to
you understand whether your security practices and a 28% click rate on determine if your risk is higher or lower
posture is typical, ahead, or behind simulated phishing than that baseline.
what’s common in your sector. • Security awareness training happens When you read about patterns in
What insurers care about. Cyber once a year the data, ask yourself: are we better
insurance questionnaires often reflect • Peer hospitals that got breached had prepared than this baseline, worse, or
what insurers see as meaningful risk similar security programs about the same? If you’re worse, you
factors based on their claims data. know what needs to change. If you’re
Where you stand on those factors The evidence suggests they’re more better, you should be able to point to
provides useful context. vulnerable than the baseline. That’s never specific evidence showing why.
a fun conversation with leadership, but it
This does not need to be an overly changes decisions. That’s how you turn industry statistics
onerous and time-consuming exercise. into actionable risk decisions for
Gather just enough evidence to make In our example, phishing becomes the your organization.
top priority. They extend MFA to VPN
a reasonable judgment about whether
access, move to continuous security
you should adjust the baseline DBIR
awareness training, and implement
statistics up or down for your
monthly phishing simulations.
specific situation.
2026 DBIR Appendices 116

Appendix D:
Contributing
organizations
| A                   | COWBELL                            | F                                  |
| ------------------- | ---------------------------------- | ---------------------------------- |
| Abstract            | Cyber Security Agency of Singapore | Fastly                             |
| Akamai Technologies |                                    | Federal Bureau of Investigation –  |
Cybersecurity Infrastructure Security
|     | Agency (CISA) | Internet Crime Complaint Center   |
| --- | ------------- | --------------------------------- |
Ankura
(FBI IC3)
CyberSecurity Malaysia, an agency
Anthropic
|                          | under the Ministry of Communications  | F-Secure |
| ------------------------ | ------------------------------------- | -------- |
| Apura Cyber Intelligence | and Multimedia (KKMM)                 |          |
Flare
| Archer Hall  | Cybersixgill  |     |
| ------------ | ------------- | --- |
Flashpoint
Atos
D
G
| B   | DarkWeb IQ |     |
| --- | ---------- | --- |
Global Resilience Federation
| bit-x-bit | Defense Counterintelligence and  |     |
| --------- | -------------------------------- | --- |
GreyNoise
Security Agency (DCSA)
Bitsight
Department of Home Affairs
| Brand Defense |     | H   |
| ------------- | --- | --- |
Digital.ai
| Breachlock |     | HackNotice |
| ---------- | --- | ---------- |
DigitalMint
| Bridewell |     | Halcyon |
| --------- | --- | ------- |
DomainTools
Hoxhunt
| C                                  | Dragos, Inc |           |
| ---------------------------------- | ----------- | --------- |
| Censys, Inc.                       | DTEX        | I         |
| Center for Internet Security (CIS) |             | ImmuniWeb |
E
| Cequence Security |     | Infoblox |
| ----------------- | --- | -------- |
Edgescan
CERT – European Union (CERT-EU) Information Commissioner’s Office (ICO)
Emergence Insurance
Check Point Software Technologies Ltd. Irish Reporting and Information Security
|     | Empirical Security | Service (IRISS-CERT) |
| --- | ------------------ | -------------------- |
Coalition
Enduir
Compass Security
J
Enzoic
Coveware
JPCERT/CC
EUROCONTROL
2026 DBIR Appendices 117

| K   | O   | T   |
| --- | --- | --- |
K–12 Security Information Exchange  Office of the National Cyber Security  Tenable
| (K–12 SIX) | Agency, Thailand |     |
| ---------- | ---------------- | --- |
Tenchi Security
| Keep Aware | Okta |     |
| ---------- | ---- | --- |
Thales
| Keepnet Labs | Onapsis |     |
| ------------ | ------- | --- |
The CWE Program
| KnowBe4 | OpenText Cybersecurity |     |
| ------- | ---------------------- | --- |
The DFIR Report
KordaMentha
Tidal Cyber
P
Triskele Labs
| L   | Proofpoint |     |
| --- | ---------- | --- |
TRM Labs
LayerX
Q
Legal Services Information Sharing and
U
| Analysis Organization (LS-ISAO) | Qualys |     |
| ------------------------------- | ------ | --- |
U.S. Secret Service
Lookout
R
V
| M   | Recorded Future, Inc. |     |
| --- | --------------------- | --- |
Veracode
| Maritime Transportation System ISAC  | RedHunt Labs |                          |
| ------------------------------------ | ------------ | ------------------------ |
| (MTS-ISAC)                           |              | VERIS Community Database |
ReversingLabs
| Mimecast |     | Verizon Cyber Security Consulting |
| -------- | --- | --------------------------------- |
|          | S   | Verizon DDoS Defense              |
N
|     | SAFE | Verizon Network Operations and  |
| --- | ---- | ------------------------------- |
National Crime Agency
Engineering
Security Scorecard
National Cyber-Forensics & Training  Verizon Threat Research Advisory
Shadowserver Foundation
| Alliance (NCFTA) |     | Center (VTRAC) |
| ---------------- | --- | -------------- |
Shodan
| Netclean |     | Verizon VTRAC Labs |
| -------- | --- | ------------------ |
Sistemas Aplicativos
NetDiligence®
|     | Six Degrees | W   |
| --- | ----------- | --- |
NETSCOUT
|     | Sophos | Wabtec |
| --- | ------ | ------ |
Wiz
SpecterOps
Swisscom
Z
Zscaler
2026 DBIR Appendices 118

2026 DBIR Appendices 119

Verizon Threat
| Verizon Cyber  |               | Verizon Network  |                  |
| -------------- | ------------- | ---------------- | ---------------- |
| Security       | Verizon DDoS  | Operations and   | Research         |
|                | Defense       |                  | Advisory Center  |
| Consulting     |               | Engineering      |                  |
(VTRAC)
Verizon
VTRAC Labs
2026 DBIR Appendices 120

© 2026 Verizon. All rights reserved. OGREP2020526

<!-- CONVERSION_METADATA: {"source": "https://github.com/jacobdjwilson/awesome-annual-security-reports", "date": "2026-08-27", "model": "gemini-3.5-flash-lite"} -->
