Organization: Verizon
Report Title:  Data-Breach-Investigations-Report
Year:          2021

About the cover
There are eight pendulums on the
cover. Each pendulum represents one
of the new patterns in the DBIR. The
weight of the pendulum represents
how often the pattern occurs. The
length of the pendulum is how often
they are breaches, as opposed to
simply incidents. Just like in security,
it’s difficult to predict where they’ll be
in the future.

## Table of Contents
- [DBIR Master’s Guide](#dbir-masters-guide)
- [Introduction](#introduction)
- [Summary of findings](#summary-of-findings)
- [Results and Analysis](#results-and-analysis)
- [Incident Classification Patterns](#incident-classification-patterns)

01
DBIR
Master’s Guide
Hello first-time reader, and Variety: More specific enumerations of
welcome to the 2021 Data higher-level categories, e.g., classifying Industry labels
the external “bad guy” as an organized
Breach Investigations Report We align with the North American
criminal group or recording a Hacking
(DBIR). We have been creating Industry Classification System (NAICS)
action as SQL injection or brute force.
standard to categorize the victim
this report for a while now,
organizations in our corpus. The
and we appreciate that all the
Learn more here: standard uses two- to six-digit codes to
verbiage we use can be a bit
obtuse at times. We use very
- github.com/vz-risk/dbir/tree/ classify businesses and organizations.
deliberate naming conventions,
gh-pages/2021 includes DBIR Our analysis is typically done at the
facts, figures and figure data
terms and definitions and
two-digit level and we will specify
- veriscommunity.net features
spend a lot of time making
NAICS codes along with an industry
information on the framework with
sure that we are consistent
label. For example, a chart with a label
examples and enumeration listings
throughout the report.
of Financial (52) is not indicative of 52
Hopefully this section will
- github.com/vz-risk/veris features
as a value. “52” is the code for Finance
the full VERIS schema
help make all of those
and Insurance sector. The overall label
- github.com/vz-risk/vcdb provides
more familiar.
of “Financial” is used for brevity within
access to our database of publicly
the figures. Detailed information on
disclosed breaches, the VERIS
the codes and classification system is
Community Database
publicly available here:
- http://veriscommunity.net/
https://www.census.gov/
VERIS resources
veris_webapp_min.html allows you
naics/?58967?yearbck=2012
The terms “action,” “threat actor” and to record your own incidents and
“variety” will be referenced often. breaches. Don’t fret, it saves any
These are part of the Vocabulary for data locally and you only share
Event Recording and Incident Sharing what you want Starting in 2019 with slanted bar
(VERIS), a framework designed to allow
charts, the DBIR has tried to make the
for a consistent, unequivocal collection
point that the only certain thing about
of security incident details. Here is how Incident vs. breach
information security is that nothing is
they should be interpreted:
certain. Even with all the data we have,
We talk at length about incidents and
we’ll never know anything exactly.
Threat actor: Who is behind the event?
breaches and we use the following
However, instead of throwing our hands
This could be the external “bad guy”
definitions:
up and complaining that it is impossible
who launches a phishing campaign
to measure anything in a data-poor
or an employee who leaves sensitive
Incident: A security event that
environment, or worse, simply making
documents in their seat back pocket.
compromises the integrity,
stuff up, we get to work. This year
confidentiality or availability of
we continue to represent uncertainty
Action: What tactics (actions) were
an information asset.
throughout the report figures.
used to affect an asset? VERIS
uses seven primary categories of
Breach: An incident that results in
threat actions: Malware, Hacking,
the confirmed disclosure—not just
Social, Misuse, Physical, Error and
potential exposure—of data to an
Environmental. Examples at a high level
unauthorized party.
are hacking a server, installing malware
or influencing human behavior through
a social attack.
2021 DBIR Master’s Guide 4

Figures 1, 2, 3 and 4 all convey the range in Figure 3), each dot represents 0.5%
of realities that could credibly be true. of organizations. This is a much better Credit where credit is due
Whether it be the slant of the bar chart, way of understanding how something
Turns out folks enjoy citing the report,
the threads of the spaghetti chart, the is distributed among organizations and
and we often get asked how they
dots of the dot plot, or the color of the provides additional information than
should go about doing it.
violin chart, they all convey the uncertainty an average or a median. We added
of our industry in their own special way. additional colors and callouts to make You are permitted to include statistics,
these even more informative this year. figures and other information from
The slant on the bar chart represents the
the report, provided that you (a) cite
uncertainty of that data point to a 95% Our newcomers this year are spaghetti
the source as “Verizon 2021 Data
confidence level (which is quite standard and violin charts. They attempt to capture
Breach Investigations Report” and
for statistical testing). In layman’s terms, if uncertainty in a similar way to slanted
(b) that content is not modified in any
the slants of two (or more) bars overlap, bar charts but are more suited for,
way. Exact quotes are permitted but
you can’t really say one is bigger than the respectively, data visualized over time and
paraphrasing requires review. If you
other without angering the math gods proportions of changes over a specific
would like to provide people a copy
(and their wrath is terrible). time period. For these charts, the darker
of the report, we ask that you provide
area is more likely to be the correct value.
them a link to verizon.com/dbir/ rather
Dot plots are also frequently used, and
than the PDF.
the trick to understanding this chart is Let us know what you think of them.[^1] We
that the dots represent organizations. hope they make your journey through this
For example, if there are 200 dots (like complex dataset a little less daunting.
Questions?
Comments?
Upset there is no
AR/VR version of
the DBIR?[^2]
Let us know! Drop us a
line at dbir@verizon.com,
find us on LinkedIn, tweet
![Figure 1. Example slanted bar chart (n=402)](Figure_1) @VerizonBusiness with
#dbir. Got a data question?
Tweet @VZDBIR!
![Figure 3. Example dot plot (n=672)](Figure_3)
Each dot represents 0.5% of organizations

![Figure 2. Example spaghetti chart](Figure_2)
![Figure 4. Example violin chart (n=581)](Figure_4)

[^1] But only if you like them. Our figures guy is really thin skinned.
[^2] We REALLY want to make it happen!
2021 DBIR Master’s Guide 5

## Introduction
Greetings! Welcome to the 2021 Data possible than we might imagine. What
Breach Investigations Report (DBIR)! is impossible is to accurately predict
We always appreciate you, our readers, what those things might be. Therefore,
but this year we would like to say thank we will not meddle with words like
you for just showing up. Thanks for “possible,” but will confine ourselves
simply making it through the often to what is “probable.”
frightening and always unpredictable
dystopian wasteland that was 2020, This year we analyzed 79,635
and still having enough interest and incidents, of which 29,207 met our
energy to care about making the world quality standards and 5,258 were
a safer place. By the time you read this, confirmed data breaches, sampled
it is devoutly to be hoped that we have from 88 countries around the world.
moved on to a place of relative safety, Once again, we include breakouts
somewhere beyond Thunderdome if for 11 of the main industries, the SMB
you will. section, and we revisit the various
geographic regions studied in the prior
Recent events around the world have report to see how they fared over the
been deemed by many to be sufficient last year. We also include our Center
cause to re-evaluate their priorities. In for Internet Security (CIS) Controls®
similar fashion, we have stepped back recommendation mapping, because
and taken another look at what we have the world being unpredictable and
been doing over the past few years. uncertain doesn’t mean your security
This exercise led to a revamp of our strategy has to be.
patterns, the creation of some shiny
new ones and the recalibration of some As always, we wish to humbly say thank
others. It is our hope that doing this will you to our 83 contributors, both old and
increase awareness of where possible new. This report would not be possible
dangers lie, and how organizations may without you and we are always grateful
best avoid them. Perhaps we should say for your continued support. Likewise,
“probable dangers,” since one lesson we thank you again, our readers, for
from 2020 is that many more things are continuing to share this journey with us.
Sincerely,
The DBIR Team
Gabriel Bassett
C. David Hylender
Philippe Langlois
Alexandre Pinto
Suzanne Widup
2021 DBIR Introduction 6

## Summary of findings
![Figure 5. Patterns in breaches (n=5,275)](Figure_5) ![Figure 6. Patterns in incidents (n=29,206)](Figure_6)
![Figure 7. Select action varieties (n=4,073)](Figure_7) ![Figure 8. Select impacts of incidents](Figure_8)
2021 DBIR Summary of findings 7

## Results and Analysis
02
Results
and Analysis

Results
and Analysis:
Introduction
The results found in this and
subsequent sections within the report The DBIR is not in the business
are based on a dataset collected from of prediction,[^3] but it can go a
a variety of sources, including cases long way to help you shape your
provided by the Verizon Threat
response strategy in the face of
Research Advisory Center (VTRAC)
an uncertain future.
investigators, reports provided by our
external collaborators, and publicly
disclosed security incidents. The year-
to-year data will have new incident and
breach sources as we continue to strive We believe it is fair to say that one of
to locate and engage with additional the primary lessons that 2020 had to
organizations that are willing to share teach us was that it is often futile to
information to improve the diversity and attempt to predict the future. However,
coverage of real-world events. This is a not trying to predict it is not the same
sample of convenience,[^4] and changes thing as giving up on scenario planning
in contributors—both additions and and preparing your organization for
those who were not able to contribute probable outcomes to the best of
this year—will influence the dataset. your ability. The DBIR is not in the
business of prediction,[^3] but it can go
Moreover, potential changes in a long way to help you shape your
contributors’ areas of focus can shift response strategy in the face of an
bias in the sample over time. Still other uncertain future.
potential factors, such as how we filter
and subset the data, can affect these Consider Figure 9 for instance; it’s
results. All of this means that we are your run-of-the-mill DBIR chart with
not always researching and analyzing all the slanted bar-charted goodness,
the same population. However, they courtesy of our Misuse action varieties.[^5]
are all taken into consideration and We have a few big things up top, and a
acknowledged where necessary within lot of stuff near the end.
the text to provide appropriate context
One valid way to interpret this is
to the reader.
that the top bar or two are the norm
Having said that, the consistency and of what may happen, namely in this
clarity we see in our data year-to-year example “Privilege abuse” and “Data
gives us confidence that while the mishandling.” Those are the Action
details may change, the major trends varieties that are understood to be so
are sound. common that, if they were to cause a
breach, someone (most likely on a bird
website) would say, “That organization
should have known better!”

[^3] Though we do suggest you put your money on “Trail Blazer” in the third.
[^4] Convenience sampling is a type of nonrandom sampling that involves the sample being drawn from that part of the population that is close at hand or available. More details can be found in our “Methodology” section.
[^5] Where are my insider threat fans at? Whoop whoop!
![Figure 9. Misuse varieties in breaches (n=178)](Figure_9)
2021 DBIR Results and Analysis 9

Suffice it to say, there’s a great deal of uncommon anymore, does it? In fact, income (in other words, the “income
inequality in the frequencies of the in this example it appears that a breach per person” chart is a horizontal line),
varieties shown. Those small bars are is just as likely to be caused by one as a 0, and a world where one individual
the extraordinary and uncommon of our myriad exceptions as it is to has all the income (in other words all we
attacks that could happen but are be caused by our second most likely have on the chart is a huge vertical spike
unlikely. If they were to cause a breach Action variety. somewhere) as a 1.
the victim would claim, “It was an
advanced attack. There was nothing But does breach data always behave Let’s bring this closer to our subject
that anyone could have done.”[^*6] like this? Rather than show you lots of matter by looking at some security-
bar charts,[^7] we’re going to condense related data, like how often your SIEM
that concept down into a single number. generates a group of critical alerts that
The Gini coefficient is
need immediate review. Anecdotally, you
a measure of statistical
Figures 11 and 12 show some data with could attest that happens exactly “every
dispersion most commonly different levels of inequality. We use the time you are on-call,” but humor us for
used to represent the income word “inequality” not by chance, but to a moment. In Figure 11, we generated
introduce the fact that we can calculate some simulated example data that is
or wealth inequality within
the Gini coefficient[^8] to represent this perfectly smooth and looks horizontal
a nation or other group
long tail behavior. on the chart—this one has an equality
of people.[^9] score of 0 (perfectly equal). Figure 12
The Gini coefficient is a measure of has actual data representing the time
statistical dispersion most commonly interval between critical SIEM events,
used to represent the income or wealth and it is extremely spikey.[^10] It has a Gini
However, if you take all those small bars inequality within a nation or other group equality score of 0.95, demonstrating a
on the Action varieties and add their of people.[^9] While it uses a lot of math huge variation time between events. It’s
breach frequencies together, you get none of us can be bothered with, it not just you: critical SIEM events fall into
Figure 10. Now it doesn’t look quite so ultimately represents a completely equal everyone’s laps indiscriminately.
outcome, where everyone has the same
![Figure 10. Top Misuse varieties in breaches (n=178)](Figure_10) ![Figure 11. Simulated time between SIEM events (n=1,335,343)](Figure_11) ![Figure 12. Time between SIEM events (n=1,335,343)](Figure_12)

[^*6] This report makes no claim about the validity of such a statement. Please refer to our official spokesperson and legal counsel. The data privacy of our readers is of the utmost importance to us.
[^7] And completely obliterate our page count budget.
[^8] https://en.wikipedia.org/wiki/Gini_coefficient
[^9] A less well-known fact is that the wish for wealth redistribution led to the phrase “Gini in a bottle.” Not really, but it would have been cool if it did.
[^10] A technical term of art in Data Science, we assure you.
2021 DBIR Results and analysis 10

This complicated mathematical setup is exceptions to the norm. Well, maybe The next time we are up against
to convey the reality that the DBIR data you can if you have enough money. And a paradigm-shifting breach that
(incident and non-incident alike) is very some organizations that are in critical challenges the norm of what is most
unequal,[^11] but at least we can measure roles to our society have no choice likely to happen, don’t listen to the
it. Figure 13 shows the equality scores but to try to do so. But from a purely ornithologists on the blue bird website
for Action, Actor, Asset, and Attribute monetary value, if you look at what chirping loudly that “We cannot patch
varieties and vectors over the last breaches cost in the Impacts section, manage or access control our way out
seven years. The scores range from it’s not a wise use of your organization’s of this threat,” because in fact “doing the
about 0.73 to 0.94, or as we would say resources to engineer solutions for basics” will help against the vast majority
here, “high.” Breach data may seem every single possible exception.[^13] of the problem space that is most likely
likely to always be the same, but some to affect your organization.
varieties are more equal than others. Armed with the knowledge of what is
the norm and what is the exception, an Read on to learn what the normal actor
The reality is you don’t need a crystal ideally optimized solution would be to has been up to for the last year, and pick
ball, a neural network or next-gen AI to engineer solutions for the norm, and out the areas where you can improve,
tell you what the norm[^12] is. You can do train your security operation teams against both the norm and the exception.
that for yourself and plan accordingly. to handle the exceptions. Turns out Because the only way to predict the
On the other hand, you can’t solution humans are very flexible problem- future is to change it yourself.
your way out of the long tail. It is solvers, and most love a good
made up of a legion of little things challenge occasionally.
that happen only rarely—they are the
![Figure 13. Inequality of enumerations in DBIR varieties and vectors for last 7 years](Figure_13)

[^11] We deeply apologize to the junior U.S. senator from Vermont for the fact that the top 3% of varieties are responsible for 87% of the breaches.
[^12] You’re reading the DBIR, and that is a great step in the right direction, if we may say so.
[^13] This argument does not consider potential incidents where loss of life or the security of individuals is concerned, as it would make no sense to assign a monetary value to that, and would, in fact, be callous and cruel.
2021 DBIR Results and analysis 11

## Actor
“All the world’s a stage,” and our threat as they continue year after year to initially resemble an internal threat
actors “all have their exits and their dominate the Actor types in breaches before detailed incident forensics are
entrances.” We must admit that they as illustrated in Figure 14. As a reminder engaged. But even though the call may
seem to know their cues very precisely. to our readers, the Internal type be coming from inside the house, there
However, at this point the analogy breaks shown here will include breaches in is still a stranger on the line.
down a bit, as rather than “playing their which both Misuse actions (where the
many parts”[^14] we seem to keep viewing mythical winged internal threats live in As in past years, financially motivated
the same performance repeated ad our taxonomy) and Error actions (the attacks continue to be the most common
infinitum, as if forced to endlessly oopsies) occurred. (Figure 15), likewise, actors categorized
re-watch a recorded musical theater as Organized crime continue to be
presentation on a streaming service.[^15] Of course, an External actor breaking number one (Figure 16).
into an organization by leveraging
It seems clear that our External actors illicitly obtained credentials or other
are not giving up their close-ups, illegal access to pivot internally may

As in past years, financially
motivated attacks continue
to be the most common (Figure
15), likewise, actors categorized
as Organized crime continue to
be number one (Figure 16).

![Figure 14. Threat actor over time in breaches](Figure_14)
![Figure 15. Top threat actor motive over time in breaches](Figure_15) ![Figure 16. Top threat actor varieties in breaches (n=2,277)](Figure_16)

[^14] As You Like It, William Shakespeare.
[^15] Anyone know if the Cyber+ trademark is available?
2021 DBIR Results and analysis 12

However, since 2015 it is relatively Even as awareness of supply chain year-over-year of Financially motivated
common for State-sponsored actors attacks has increased over the last breaches, and that most Secondary
to also crave that cold hard cash[^16] as few months, the overall percentage of motive breaches reported to us are
the Financial motives for those actors incidents with a Secondary motive— simple in nature (which suggests the
have fluctuated between 6% and 16% where the ultimate goal of an incident catastrophic ones on everyone’s minds
of recorded breaches. Given this result, was to leverage the victim’s access, are still very much the exception).
it should come as no surprise when you infrastructure or any other asset to
glance at Figure 17 and find that the conduct other incidents—has decreased
two most common cybercrime terms slightly as a percentage from last year.
found on criminal forums are bank There are two caveats here that should
account and credit card related. be kept in mind: The associated growth
![Figure 17. Terms over time in criminal forums and marketplaces](Figure_17)

[^16] Or the hot ethereal cryptocurrency.
2021 DBIR Results and analysis 13

However, Secondary is still in second place (fittingly enough) as a top Actor motive,
as Figure 18 demonstrates. So, if you are a software developer or service provider
that has assets that could be repurposed in that manner, please make sure you are
paying the proper attention to the operational parts of your organization.
In the same way automation may be helping you scale up your defensive operations,
it can also help attackers scale up their offense. Figure 19 illustrates the relative
occurrence of attack types in honeypot data. Near the top of the attacker’s
opportunistic sales funnel, we see scanners. Down near the bottom are where the
Remote Code Execution (RCE) attacks reside. Regardless of their placement in
the figure, automation is likely to assist attackers in moving potential victims from
the top of the funnel to the bottom. As such, it’s important to limit your public
facing attack surface, through asset management, defensive boundaries and
intelligent patching.

In the same way automation may be helping you scale up
your defensive operations, it can also help attackers scale
up their offense.

![Figure 18. Top Actor motives in incidents (n=5,085)](Figure_18)

Secondary motive subset
In the Secondary Motive subset, we had an additional 24,913 incidents of which
only one was a known breach. In all of these incidents, web apps were attacked with
a secondary motive by External actors. Beyond that, we know very little.

![Figure 19. Ratio of days of high to low detection in honeypot data](Figure_19)
2021 DBIR Results and analysis 14

Action
Do we have an action-packed section
for you, folks! Step right up, make
room in the back so everyone can see!
Figures 20 and 21 will reveal all you
need to know about the frequency of
Action varieties for the past year.
We do not want to divert all of your
attention from the brand-new incident
patterns. So we saved additional details
on how those Actions manifested in the
wild for you to dig your teeth into there.

Talking the
talk and acting
the action
It would be impolite on our part not
to address the virulent elephant[^17] in
the room, so we have centered this
initial analysis of Actions on evaluating
how adapting to life in a pandemic-
stricken world has impacted the threat
landscape. The DBIR team released a
COVID-19 Threat Landscape Trends
article[^18] in the middle of last year, and
it is only fair that we revisit how our
speculations (see how we avoided
the word predictions?) fared.

![Figure 20. Top Action varieties in breaches (n=4,073)](Figure_20) ![Figure 21. Top Action varieties in incidents (n= 24,362)](Figure_21)

[^17] Viruphant? Eleplent?
[^18] https://enterprise.verizon.com/resources/articles/analyzing-covid-19-data-breach-landscape/
2021 DBIR Results and analysis 15

Figure 22 shows how the Actions
we highlighted in that article varied
in relation to last year’s report. We
highlighted Phishing, Use of
stolen creds, Ransomware and
Errors as Action varieties that could
possibly increase.

Even in a year as unexpected as 2020,
there are some things we can trust to
stay the same. Phishing remains one
of the top Action varieties in breaches
and has done so for the past two years.
Not content to rest on its scaly laurels,
however, it has utilized quarantine to
pump up its frequency to being present
in 36% of breaches (up from 25% last
year). This increase correlates with
our expectations given the initial rush
in phishing and COVID-19-related
phishing lures as the worldwide
stay-at-home orders went into effect.

Phishing continues to walk hand-in-
hand with Use of stolen credentials
The final piece of this puzzle pertains
in breaches as it has in the past.
to Error actions, where we opined that
Admittedly, we expected to see an
we would see an increase, but actually
increase here due to a larger remote
had a decrease this year to 17% of
workforce. However, the numbers
breaches (from 22%). This breaks a
have remained in the region of
three-year streak of either staying the
25% of breaches, which is still a
course or increasing. Granted, the
significant number.
absolute number of Error breaches did
increase from 883 to 905. However,
The major change this year with regard
as a proportion of the dataset, Error
to action types was Ransomware
decreased due to the rapid growth of
coming out like a champ and grabbing
Social breaches.
third place in breaches (appearing in
10% of them, more than doubling its
Of course, we here on the team secretly
frequency from last year). This is also
blame each other for this miscalculation
something we discussed, but this may
on our part, as any team would. Still,
have less to do with the changes in
both in relative and absolute terms, this
working arrangements than it does
is a significant value and is on par with
the shift in tactics of the actors who
Malware-related breaches as Figure 23
“named and shamed” their victims.
demonstrates, and it should certainly
be front and center in your control
These actors will first exfiltrate the data
definition strategy.
they encrypt so that they can threaten
to reveal it publicly if the victim does not
pay the ransom. We are not sure if this
breach double-dipping is permitted in
the Threat Actor Code of Conduct, but
there has been no evidence that they
have one anyway.

![Figure 22. Change in COVID-19-related Action varieties](Figure_22)
![Figure 23. Actions in breaches (n=5,257)](Figure_23)
2021 DBIR Results and analysis 16

Actions have
consequences[^19]

A data point we started collecting
over the past few years pertains to
the results of Actions, which provide
some interesting insights especially
when you consider it as a complement
to our ongoing attack chain research.
For example, a threat actor might
perform a Use of stolen credentials
or Phishing action to Infiltrate a victim
organization, but then deploy Malware
in order to Exfiltrate the data they had
their sights on.

The heatmap in Figure 24 shows how
our most frequent results relate to our
top-level Action categories.

Points of interest here are how well
![Figure 24. Results in breach Actions](Figure_24)
those findings align with the attack
chain information that is present in
some of the incidents we analyze. If an
Action is concentrated into Infiltrate, it
is closer to the top of the first actions
in a chain chart, as shown in Figure 25,
while Exfiltrate will correlate with the
last one. Misuse actions are different, as
they often assume or require legitimate
access to the Asset that was breached,
and, as such, are very focused into
Exfiltration. With regard to Malware,
well, given the Swiss Army Knife
behavior of modern variants, it looks like
you can eat your cake and have it too.[^20]

[^19] Just like your Momma said.
[^20] Mmm…cake.
2021 DBIR Results and analysis 17

Beginning Middle End
![Figure 25. Actions at the beginning, middle and end of breaches](Figure_25)

Shared
access
is double
access

Another noteworthy change this year
is the increase in rank of Desktop
sharing as the vector of a Hacking
action to second place. As Figure
26 demonstrates, it is completely
overshadowed by Web application
as the attack vector. But it is now on
the 5% threshold and we recommend
attention to the authentication security
of those. Notably, 89% of the Hacking
varieties in this vector involved some
sort of credential abuse (Use of stolen
creds or Brute force).

![Figure 26. Top Hacking vectors in breaches (n=1,610)](Figure_26)
2021 DBIR Results and analysis 18

Assets
If, after looking at Figures 27 and 28, you had to double
check that you weren’t still in 2020, you would be forgiven.
Servers are still dominating the Asset landscape due to
the prevalence of web apps and mail services involved in
incidents. And as social attacks continue to compromise
people (they have now pulled past user devices), we begin to
see the domination of phishing emails and websites delivering
malware used for fraud or espionage.

However, we can glimpse the impact of a world where the
flickering flames of digital transformation have slowly built
into a sizable inferno when we review the Assets involved in
breaches. Figure 29 shows that there is a large gap between

![Figure 27. Assets in incidents (n=27,634)](Figure_27)
![Figure 28. Top asset varieties in incidents (n= 9,188)](Figure_28) ![Figure 29. Top Assets in breaches (n=4,717)](Figure_29)
2021 DBIR Results and analysis 19

Person and User devices as the most
breached Assets, and the decline of
User devices is statistically verifiable in
relation to the previous two years. This
result makes sense when we consider
that breaches are moving toward Social
and Webapp vectors, and those are
becoming more server based, such as
gathering credentials and using them
against cloud-based email systems.

A related result that will likely not be
surprising is that this year, external cloud
assets were more common than on-
premises assets in both incidents and
breaches. Now before you put that in
your marketing brochure for your next-
gen AI[^21] cloud security product, there
were 10 times as many Unknowns (quite
plainly incidents where the information
on the location of the assets was not
available) as there were cloud assets.
That is more than enough to tip the
scales in the other direction if we’d
known more about what happened. Still,
in a sample of random organizations,
17% that had a web presence had
internet-facing cloud assets.[^22] If it
was not obvious by now, cloud assets
deserve a seat at the grown-up security
table and a piece of your budget pie.[^23]
Even the median random organization
with an internet presence has 17 internet-
facing assets (Figure 30). Figure 31
gives you an idea of how vulnerable
those organizations are. Most had
no vulnerabilities at all. Furthermore,
one might think that more recent
vulnerabilities would be more common.[^24]
However, as we saw last year, it is
actually the older vulnerabilities that
are leading the way.[^25]

Rather than selecting out
of something like the Alexa
top 1 million domains, we
randomly sampled a
database of hundreds
of millions of companies
worldwide. Out of a million
companies, only 1.4% had
a web presence (a domain
connected to the
organization). It’s easy
to forget that the average
security-conscious
organization might be
quite different from the
average company.

![Figure 30. Number of internet-facing assets in randomly selected organizations (n=85). Each dot represents 2% of organizations](Figure_30)

![Figure 31. Organizations’ oldest internet-facing vulnerability (n=85)](Figure_31)

[^21] Emphasis on the “Artificial” not on “Intelligence.”
[^22] See the sidebar for what we mean by “random organizations.”
[^23] A terrible “pie in the sky” joke was edited out here. You are welcome!
[^24] You know, because of patching.
[^25] Just don’t call them “boomer vulnerabilities,” or you will start a fight. They might even tell you to get off their lawn.
2021 DBIR Results and analysis 20

![Figure 33. Patching in vulnerability scan data (n=110)](Figure_33)

These older vulnerabilities are what
the attackers continue to exploit.
Figure 32 shows the discovery years of
vulnerabilities that attackers attempted
to exploit in bulk as seen from the
perspective of honeypots. If Tom Brokaw
were writing this report, he’d call them
the greatest generation of vulnerabilities.
Eternal Blue is a crowd favorite, which
shows that the amount of time since
discovery does not really factor into why
actors target vulnerabilities. Instead,
it seems to be simply a matter of what
capabilities exploiting a vuln provides to
the attacker, along with the robustness of
current working exploits and payloads.[^26]

So, what’s a good, clean-cut, security-
conscious organization to do? Based on
Figure 33, the patching performance this
year in organizations has not been stellar.
Granted, it’s never been great.[^27]
There are several likely hypotheses to explain
why this year might be underperforming.

The ideal state for any organization is
to patch smarter, not harder, by using
vulnerability prioritization not necessarily
to improve security, but to improve
the organization’s productivity. Every
patch that has to be applied means
you are that much farther from putting
down the keyboard and picking up the
d-pad.[^28] Anything you can do to avoid
patching vulnerabilities that do not
improve your security keeps you just
as secure but involves much less work
(and less chance of burnout from your
employees or service providers).

Mobile phones made the list in Figure
28 at the beginning of this section. As
with last year, this finding is somewhat
anticlimactic, as the vast majority are
simply lost phones. Still, that’s not quite
the end of our mobile foray. We also
have mobile data on malicious URLs
and APKs[^29] in Figure 34. What we
found, in short, was that you don’t have
to be a large organization to have a URL
good chance that one of your members
has received a malicious URL or even
installed a malicious APK.[^30]

![Figure 32. Percent of vulnerabilities by year in honeypot data (n=42,532,746)](Figure_32)

[^26] As we write this section, a Microsoft Exchange Remote Code Execution Vulnerability (CVE-2021-26855) is being actively and massively exploited that has all the ingredients to also be part of this growing background noise of exploitation activity in the internet.
[^27] 2017 DBIR, Figure 56.
[^28] Or your kid, or your running shoes, or something else that keeps you sane.
[^29] Android apps.
[^30] Observant readers may have noticed the assets section missing anything about Information Technology (IT) vs. Operational Technology (OT) assets. That’s because it was largely missing from our dataset as well. We’ve heard those OT breaches are somewhere, but they’re not in our dataset.
![Figure 34. Probability that someone in the company will receive a malicious URL or install a malicious APK based on organization size (n=5,440,000). Blue is malicious APKs, green is malicious URLs](Figure_34)
2021 DBIR Results and analysis 21

## Attribute
The Attributes are the Confidentiality,
Integrity and Availability (aka the As we have pointed out in previous reports, Credentials remain
CIA[^31] Triad) violations of the impacted one of the most sought-after data types.
asset. Whether it is a confirmed data
breach in which the confidentiality
of the data was compromised, or an
integrity incident, such as altering
the behavior of a person via phishing,
the actions against the assets result
in CIA violations. First, let’s discuss
Confidentiality and the types of data
that are most frequently compromised.

As we have pointed out in previous
reports, Credentials remain one of
the most sought-after data types
(Figure 35). Personal data is a close
second. Considering that Personal data
includes items such as Social Security
numbers, insurance-related information,
names, addresses and other readily
monetizable data, it is little wonder
that attackers favor them as they do.
They are also useful for financial fraud
further down the line, not to mention
their resale value.

We do not mean to imply that attackers
are the only way data is compromised.
Sadly, we cannot discount the ability of
our own employees to make mistakes,
thereby contributing to the problem.
However, they are less likely to involve
credentials, and more likely to involve
other data such as Personal information
(Figure 36).

![Figure 35. Top data varieties in breaches (n=4,552)](Figure_35) ![Figure 36. Top data varieties in Error breaches (n=839)](Figure_36)

[^31] Not the CIA that keeps the alien presence on the DL, the other kind.
2021 DBIR Results and analysis 22

Moving on to Integrity violations
(Figure 37), these are usually the
result of a Social or Malware action.
For the Social actions, Phishing and
Pretexting will alter the behavior of
their targeted victim. In some cases,
Pretexting results in the initiation of
a Fraudulent transaction, causing
money to go where it was not
supposed to. With the prevalence of
Phishing and Pretexting in our dataset
this year (43% of breaches) it is no
surprise that Alter behavior ranks
first among the Integrity violations.

But we must not forget the Malware
actions. Software installation comes
in second place due to the high
number of System Intrusion pattern
cases that had a Malware component.
Most commonly these were directly
installed by the actor after system
access—usually after a Hacking
action such as the Use of stolen
creds or Brute force.

Finally, we arrive at our Availability
violations (Figure 38). The most
common is Obscuration, which is what
you get when ransomware is installed
and the encryption is triggered. Loss
is our second most common violation,
and results from either a lost or stolen
asset, as you no longer have access
to that data.

![Figure 37. Integrity varieties in breaches (n=2,762)](Figure_37)
![Figure 38. Top Availability varieties in breaches (n=541)](Figure_38)
2021 DBIR Results and analysis 23

Timeline
This year we decided to take a look at something is wrong. Examples include The other end of the spectrum for
which breach types take the longest Stolen assets, because the employee discovery methods is when the threat
to discover (Figure 39). Traditionally, found evidence of a break-in, and actor involved makes the “notification”
this has been insider Privilege Misuse. Errors, where the employee had that in the form of a ransom note that
However, when looking at this year’s sinking feeling that they screwed up, appears on screen.
data (largely due to the insight provided and reported it in the hopes that it
by the new patterns), we found that the could be quickly contained. These are Finally, we were also curious what
differences between Privilege Misuse both internal methods of discovery, and kind of data was the fastest to be
and System intrusion were negligible. if you don’t already have an easy and compromised, and that turns out to
Both were present in the longest to fast way for your people to report these be Credentials. This is particularly the
discover breaches. kinds of breaches, you should look into case in Phishing, which typically goes
it. Why not cultivate your employees to after the victim’s credentials for use in
In contrast, the breaches that are the be your early warning system when it gaining further access to their chosen
fastest to discover appear to be those can have a great return on investment? victim organization.

![Figure 39. Discovery over time in breaches](Figure_39)
2021 DBIR Results and analysis 24

Impact
Many hands
make for
light work

Attackers continue to profit substantially
from the adversity that befalls breach
and incident victims. And while that
profit is certainly of interest,[^32] what
really concerns us is how the amounts
tally up on the other side of the
transaction. Figure 40 illustrates the
range of loss from various types of
incidents based on adjusted losses
reported to the FBI Internet Criminal
Complaint Center (IC3).[^33] In this figure,
each dot represents half a percent of
incidents. First and foremost, according
to IC3 data, is the fact that whether
the attack was a Business Email
Compromise (BEC), Computer Data
Breach (CDB) or a ransomware attack,
a large percentage of incidents did not
actually result in a financial loss (42%,
76%, and 90% respectively).

When losses did occur, they were not
of the one-size-fits-all variety. Following
the rules of good business, we expect
attackers to charge what the market
can bear. For a small organization that
is usually a small amount. For a large
organization, however, losses can be
much more substantial. When examining
breaches that included a reported
loss, 95% of BECs fell between $250
and $985,000 dollars with $30,000
being the median. That is a pretty big
range, you say? Maybe so, but CDB
ranges were even wider with 95% falling
between $148 and $1.6 million, and a
median loss of $30,000. Finally, for
ransomware the median amount lost
was $11,150, and the range of losses in
95% of the cases fell between $70 and
$1.2 million.

![Figure 40. Loss by incident type. Each dot represents 0.5% of incidents](Figure_40)

[^32] It would be fascinating to analyze profitability of different types of attacks from the perspective of the threat actors, but not only do we not believe we have the data necessary; we are not sure if this analysis would benefit the threat actors more than the defenders.
[^33] https://www.ic3.gov
2021 DBIR Results and analysis 25

Let us state this in a somewhat different
Of course, direct losses are not the not covered in the overall costs. Of
manner: If you only consider the bottom
sole cost one encounters due to a course, to address the elephant in
half (everything below the medians
breach. Apart from the damage done by the room,[^35] it is unlikely that your
that we just mentioned), CDBs are
the attacker, there remains the expense insurance will cover the damage to your
often associated with bigger losses
of Digital Forensics and Incident company’s reputation. And depending
than are ransomware events. This
Response (DFIR) and legal counsel. on several factors such as disclosure
finding, when coupled with the 90%
Figure 42 provides an idea of what to requirements, the size of the breach,
of ransomware incidents that did not
expect in these areas based on cyber and other things hiding in the fine print,
result in any loss, could be telling the
insurance[^34] claims. Each dot represents that damage can be considerable.
story that organizations are no longer
2% of incidents. As you can see,
paying the ransoms. It must also be
50% of incidents had no associated Various studies have arrived at very
kept in mind that this loss data includes
forensics costs. When forensics costs different conclusions regarding the
individuals as well as organizations,
were present, 95% fell into the range impact on stock price from a breach
which is another potential reason for the
of $2,400 to $336,500. Slightly fewer in the days immediately following
numbers being smaller. Unfortunately,
incidents had no associated legal costs, a breach, including 2.53% (Rosati,
we do not have a sufficient level of detail
(36%). For the remaining 64%, 95% of Cummins, Gogolin, van der Werff, &
to distinguish between the two. There is
the legal costs fell between $800 and Lynn, 2017), 5% (Cambell, Gordon,
also the specter of potential bias toward
$54,000. Loeb, & Zhou, 2003), 2.1% (Cavusoglu,
underreporting of larger ransoms. If,
Mishra, & Raghunathan, 2004), and 1%
however, organizations are skipping the
It should be pointed out that insurance (Goel & Shawky, 2009). The findings
ransom, the low payout ranges could
data can be somewhat biased. For of these studies are helpful, but they
have been yet another contributing
instance, insurance may not cover don’t shed much light on what happens
factor for the rise of the ransomware
legal costs or penalties. There may in the long term. Figure 43 may help to
“name and shame” threat actors
also be an additional deductible illuminate the matter somewhat.
witnessed in late 2019.

In a “glass half full” view of the above
situation, there is some possible
good news in that there is a chance
you can reverse the mass migration
of your funds to other environs. The
IC3 Recovery Asset Team (RAT) can
sometimes assist victims in the freezing
of lost funds for possible recovery. In
Figure 41, we see that when the IC3
RAT acts on BECs, and works with the
destination bank, half of all US-based
business email compromises had
99% of the money either recovered or
frozen, whereas only 11% had nothing
at all recovered. If your organization
experiences an incident, we highly
recommend that you contact the local
branch of your national law enforcement
and seek their assistance. Or, better yet,
get to know them before the
breach occurs!

![Figure 41. Percent of losses frozen for recovery (n=1,086). Each dot represents 2% of incidents](Figure_41)

[^34] For an additional fee, Verizon will provide a version of the DBIR that replaces all instances of “Cyber” with “Security.” See your local Verizon representative for details.
[^35] Another elephant? This is a pachyderm-filled space!
2021 DBIR Results and analysis 26

Based on data collected by
comparitech.com,[^36] breached
companies underperformed the
NASDAQ (a U.S. Stock Market) by about
5% after six months, though if you look
at 95% of companies the performance
was anywhere from 48% under to 39%
over performing. If we look two years
into the future of those organizations
(after the breach), those downward
trends continued, suggesting that
perhaps the breach wasn’t actually
the cause, but the symptom.[^37]

To answer the question, “what
might a breach cost in total?” we ran
1,000 Monte Carlo simulations using
bootstrap sampling on breaches we had
cost information about on this year’s
dataset like the good data nerds we
are. Fourteen percent of the simulated
breaches had no impact. Of the 86%
that were impacted, Table 1 captures the
results. What you do with these numbers
is, of course, up to you. While you could
plan for the median breach of $21,659,
a better option might be to plan for the
middle 80% of breach impacts, $2,038
to $194,035. Or better yet, be prepared
for the most common 95% of impacts,
between $826 and $653,587. If you add
to that an organizational devaluation of
around 5% (from Figure 43), then you
just may have yourself a tangible figure
you can plan around.

![Figure 42. Cost by incident type. Each dot represents 2% of incidents](Figure_42)

| Percent of breaches | Lower | Upper |
| :--- | :--- | :--- |
| Median | $21,659 | |
| 80% | $2,038 | $194,035 |
| 95% | $826 | $653,587 |

Table 1. Simulated breach costs

![Figure 43. Changes in stock price for companies with breaches after six months (n=39). Each dot represents 0.5% of incidents](Figure_43)

[^36] More precisely, Paul Bischoff’s (@pabischoff) blog post at https://www.comparitech.com/blog/information-security/data-breach-share-price-analysis/
[^37] Dr. Frank N. Furter nods approvingly.
2021 DBIR Results and analysis 27

About
the FBI

Over the past decade, the cyber
Of utmost importance to the FBI, and
Herbert Stapleton
threat has grown exponentially
a key component of our foundational
Deputy Assistant Director, FBI Cyber with nation state and cyber criminals
cyber strategy, is the ability to share
increasing the scale, scope and level
relevant and actionable information
of sophistication of their cyber attacks.
with our government partners, the
Addressing this kind of complex and
international community, private
agile environment requires a more
industry, and the public. But, we also
comprehensive response than any one
rely on the information received from
single government agency, business,
our partners, private industry, and
technology, or data source can provide.
victims to develop a broader picture
Instead, an interwoven architecture
of cyber threats. The Internet Crime
of combined capabilities from across
Complaint Center (IC3) serves as a
public agencies and the private sector
reliable, convenient, tool for submitting
must be leveraged to protect critical
information to the FBI about suspected
infrastructure and impose risk and
internet-facilitated criminal activity, while
consequences on attackers.
also developing effective partnerships
with law enforcement and private sector
The FBI is committed to sharing as
entities. Information provided to the
much as possible about cyber threats
IC3 is further analyzed, resulting in
as quickly as possible so the public
investigative leads or the identification
is alerted and prepared. We strive
of new or emerging cyber threats. We
to be viewed as an indispensable
share what we’ve learned through our
partner, using our unique authorities
analysis of IC3 data with the public and
as a law enforcement agency
private industry through PSAs, alerts
and member of the United States
and reports such as the DBIR.
Intelligence Community to enable
government operations against our
For the 2021 DBIR, the FBI’s IC3
cyber adversaries and allow the public
focused on supplying data specifically
to enhance their security posture.
for business email compromises/
Because of our unique authorities,
email compromises (BEC/EAC), and
world-class capabilities, enduring
other data breach incidents reported
partnerships, and presence we
to IC3. In recent years, the FBI’s IC3
can conduct investigations, collect
has observed that BEC/EAC and data
intelligence, and interact with victims –
breach incidents trend more towards
all in pursuit of attribution. Attribution
victimizing corporations and/or private
is what allows the U.S. government
sector entities and less on targeting a
to impose risk and consequences
single individual. IC3 recognizes that the
on our adversaries and prioritize our
public plays a central role in IC3 being
operations with our partners, including
able to understand how cyber criminals
the private sector. Cyber [Combatting
are evolving. By submitting a cyber
cyber crime] is the ultimate team sport
related complaint, the public is assisting
and we all must be committed to using
the FBI in addressing those specific
every tool we have at our disposal to
complaints, as well as, identifying the
address the cyber threat.
2021 DBIR Results and analysis 28

03
Incident
Classification
Patterns

## Incident Classification Patterns
Incident
Classification
Patterns: Introduction

The times they
are a-changin’

Remember 2014? Uptown was funky,
Pharrell Williams was happy, and if you
had a problem, you could shake it off.
The DBIR first introduced the Incident
Classification Patterns in 2014, as a
useful shorthand for the sometimes
complex combinations of VERIS Actors,
Actions, Assets and Attributes that
frequently occur. The threat landscape
has changed a bit since then, and we
are now happy to introduce a refresh of
the DBIR patterns.

As you can imagine, this was a very
hard decision for the team, but we
were able to find strength and courage
from the leadership shown by big, bold,
refreshing business moves such as the
release of New Coke and Crystal Pepsi.
Our new patterns explain 99.3% of
analyzed breaches and 99.6% of
analyzed incidents this year. They
also explain 95.8% of quality breaches
and 99.7% of quality incidents over
all time.[^38]

![Figure 44. Patterns over time in incidents](Figure_44)
![Figure 45. Patterns over time in breaches](Figure_45)

[^38] Last but not least, it kills 99.9% of germs on contact! Ok not really.
2021 DBIR Incident Classification Patterns 30

Of course, not everything has
The original patterns were based on a
Figures 46 and 47 give an idea of
changed. Denial of Service, Basic Web
hierarchical clustering approach that
where incidents and breaches went
Application Attacks,[^39] Lost and Stolen
helped derive some simple rules used
between the old and new patterns.
Assets, Miscellaneous Errors, Privilege
to assign incidents to patterns. It was a
First, the easy-to-explain changes. Lost
Misuse, and Everything Else renew
very prescriptive process that worked
and Stolen Assets are still mostly in the
their contract for another season.
quite well at the time, but we could see
Lost and Stolen Assets pattern. The
Payment Card Skimmers, Crimeware,
the strain starting to show.[^41]
same can be said for Miscellaneous
Cyber-Espionage, and Point of Sale
Errors, Privilege Misuse, Basic Web
are the MVPs[^40] retired to make room
The new patterns are based on an
Applications Attacks, and Denial of
for a couple of seasoned minor league
elegant machine-learning clustering[^42]
Service. What has changed starts with
patterns, ready for the big leagues:
process. Making this decision was
Payment Card Skimmers, which now
Social Engineering and System Intrusion.
a gamble in many ways, as we were
falls squarely into Everything Else. It
committed to trust the data on this
originally had some similarities to the
Now just because some names haven’t
process, and it paid off. The new
current System Intrusion pattern in that
changed it does not mean the patterns
patterns clearly fell around the same
that is where non-webapp payment
are the same. What has been currently
ones that had been prescriptive before,
card breaches ended up. Obviously,
assigned to the 2021 version of
but also better capture complex
skimming isn’t really what we think of
Miscellaneous Errors (for example) is
interaction rules the old ones were
when we picture a popped system, so
not necessarily what was in the 2014
unlikely to handle.
over to Everything Else it goes.
Miscellaneous Errors.

![Figure 46. Old patterns mapped to new patterns in incidents](Figure_46)

[^39] Which, after going through an incredibly scientific, focus-tested rebranding, briefly became “The pattern formerly known as Web Applications,” but then Verizon Branding and Communications said we couldn’t do that either. We were bummed—we had a symbol picked out and everything.
[^40] Most Valuable Patterns
[^41] Like a three-day holiday visit with your in-laws.
[^42] We will be talking about it in way more detail than necessary in the next part of the section.
2021 DBIR Incident Classification Patterns 31

Of more interest are Point of Sale,
Crimeware, Cyber Espionage and
Everything Else. They are now defined
by the characteristics of the breach.
Was Social Engineering the significant
aspect? To the new Social Engineering
pattern it goes! Was it a simple attack
where the initial intrusion point was
the web application? To Basic Web
Application Attacks it goes! Or was it
more of an elaborate system intrusion
where the attacker gained access and
poked around, maybe without us even
knowing how they gained access?
System Intrusion is just waiting to
welcome those incidents with open
arms like an old Journey song. Those big
changes weren’t exactly planned (quite
frankly nothing in the DBIR ever is in
regard to what the data is going to tell us).

Thanks to the re-focused patterns,
we can provide better guidance when
one of those patterns appear at the
top of your industry. Cyber Espionage
and Crimeware could suggest a
different complexity of the incidents
in most cases, but your controls don’t
care if the threat actor has a cushy
government job or if they are a free-
market enthusiast entrepreneur.

![Figure 47. Old patterns mapped to new patterns in breaches](Figure_47)
2021 DBIR Incident Classification Patterns 32

This is the way
Coming up with new patterns was not
a superficial process. It has been in
the works for some time. Clustering
DBIR data is not quite as straight-
forward as it might seem. First, we have
almost 2,600 columns in the dataset
leading to almost assured overfitting.
Second, our data is mostly logical
rather than categorical or continuous,
limiting the approaches that are likely
to work. Third, we have over 800,000
rows in our dataset, again limiting the
approaches that would work. Fourth,[^43]
we are well aware that our clusters
would be imbalanced. There would be
some clusters with far fewer incidents
and breaches than others. Fifth,
the results needed to be somewhat
explainable, always a fun proposition
on large-scale, machine-learning
endeavors. Sixth,[^44] whatever approach
we took would have to provide rules
we could use to classify data later since we
shouldn’t be re-clustering things every
single year. Seventh, we want it to be
possible for an incident to be able to
fit into two or more patterns in order
to better capture the nuance of more
elaborate incidents. All of these, plus
the importance of getting it right, meant
we’ve taken it slow and steady.

![Figure 48. Model rating by cluster number](Figure_48)

Breaches

Incidents

all-to-all comparisons needed. Principal
Component analysis didn’t penalize
using lots of features enough for our
needs. Latent Dirichlet Allocation was
slightly better, but still not good enough.
Lasso and Ridge Regression didn’t
converge well. Association Rules did
not differentiate clusters well and would
have had to be paired with a predictor.
Artificial Neural Networks (ANNs)
would have provided prediction but not
small and large clusters, handle high
dimensionality without overfitting,
handle logical data, and be explainable)
while also not choking on our rather
large dataset. Normal k-means
calculates the distance between all the
rows in the dataset in the dimensional
space of the number of columns.
It randomly creates a set number
of cluster centers and assigns the
points to the closest center

---

. It then
Before we get to what did work, let’s clustering.45 We even tried Gaussian recalculates the center of each cluster,
talk about some of the things that didn’t Finite Mixture Model clustering, and repeats the two steps until there
work. We started with hierarchical but it had the opposite problem of are no significant changes in the cluster
clustering similar to the 2014 pattern’s hierarchical clustering in that all the memberships. All those distance
original methodology. Unfortunately, clusters were minor variants on the big calculations take a lot of time and
it was too unbalanced, finding small, themes; kinda like seeing the forest, but memory. Spherical k-Means improves
highly similar things instead of bigger not the trees.46 on that by calculating cosine distance,
trends; kind of like seeing the trees and taking advantage of that special
but not the forest. K-means clustering What we eventually settled on was structure to avoid calculating full
would have been ideal, however given spherical k-means. It provided us object-to-object distance matrices.47
the size of our data, it’s simply too the clustering benefits of k-means
memory intensive due to the number of (ability to classify new data, find both
43 Even I thought this list would only be three items long, but man did we have a lot of challenges.
44 Another one? We get it. It was hard.
45 We also tried ANNs for clustering, specifically Self-organizing Maps, but that didn’t work either.
46 You have our permission to read this out loud as many times as you would like on first dates and/or at family get-togethers and Super Bowl® parties.
47 http://www.stat.cmu.edu/~rnugent/PCMI2016/papers/SphericalKMeans.pdf
2021 DBIR Incident Classification Patterns 33

We then manually examined the Assets; and one in Denial of
The new patterns provide patterns generated around the “bend” Service) and then named, forming
a clear framework for us to in the lines (around five for incidents the new patterns.53
explain the threat landscape and eight for breaches; see Figure 48).
Eventually we settled on eight breach Table 2 is what we got for all of that
and for you to bring it
clusters and 10 incident clusters. After work. In some places, nothing has
to the stakeholders in clustering, the clusters were examined changed. In some places, everything
your organization. and some were grouped together (five has changed. But, more importantly,
in System Intrusion; three in Privilege the new patterns provide a clear
Misuse and Miscellaneous Errors; framework for us to explain the threat
two in Basic Web Application Attacks, landscape and for you to bring it to the
Even then, it would be 10 Social Engineering, and Lost and Stolen stakeholders in your organization.
hyperparameter variations until we
were sure the approach would work
and an additional six cluster versions
based on the 2021 DBIR data to finalize
Social Psychological compromise of a person, which alters their
the model. We settled on 517 columns Engineering
behavior into taking an action or breaching confidentiality.
to cluster, primarily dealing with the
VERIS 4A’s (Action, Actor, Asset and Basic Web Simple web application attacks with a small number
Attribute), victim, targeted, timeline Application of steps/additional actions after the initial web
and discovery method. Attacks application compromise.
We wanted to prioritize more recent System System Intrusion captures the complex attacks that leverage
incidents over older ones, and while Intrusion Malware and/or Hacking to achieve their objectives including
we tried just using the last few years deploying ransomware.
of data, we ultimately settled on an
exponential weighting function. We Miscellaneous Incidents where unintentional actions directly compromised a
used a Lloyd-48Forgy49 style fixed-point Errors security attribute of an information asset. This does not include
algorithm with local improvements via lost devices, which is grouped with theft instead.
Kernighan-Lin chains.50,51 While we
wanted pattern overlap, the spherical Privilege Incidents predominantly driven by unapproved or malicious
Misuse
k-Means fuzziness parameter yielded use of legitimate privileges.
poor results, so instead we set it to hard
partitions and, after clustering, included Lost and Any incident where an information asset went missing, whether
incidents in multiple clusters if the next Stolen Assets through misplacement or malice.
closest cluster(s) were almost as close
as the main cluster. And voilà. We have Denial of Attacks intended to compromise the availability of networks and
some new patterns to play with. Service systems. Includes both network and application layer attacks.
From experience, we know that incident
Everything This last “pattern” isn’t really a pattern at all. Instead, it covers
and breach data can be very different. Else all incidents that don’t fit within the orderly confines of the
Breaches are a subset of incidents,
other patterns.54
but many times more important than
incidents for our analysis.52 To ensure
that both incidents and data breaches Table 2. New Incident Classification Patterns
were reflected in the patterns, we ran
clustering twice, once for each. To
pick the best number of clusters, we
calculated the total sum of squares (a
measure of success in clustering) for
several different numbers of clusters.
48 Lloyd, Stuart P. (1982)
49 Forgy, Edward W. (1965)
50 Dhillon, Guan and Kogan (2002)
51 Did that make sense to you? We’ll be honest, we didn’t read the papers. We just chose that option on the software.
52 It is the Data Breach Investigations Report, not the Data Incident Investigations Report, after all.
53 Astute readers may notice that we did not actively attempt to retain old patterns. The fact that so many of them remain is a testament to the relevancy of the 2014 patterns.
54 Like that container you keep all the cables in for electronics you do not own anymore just in case.
2021 DBIR Incident Classification Patterns 34

Denial
of Service
Figure 49. DoS incident paths (n=5)
Denial55 of Service (DoS) is one of But when you look at Figure 51, you’ll
Summary those infosec threats that actually can notice that the median bits per second
be addressed. This is the one you do (bps) of 1.3 Gbps may be only a bit (no
The Denial of Service pattern consists
something about for an injection of pun intended) more than your home
of attacks intended to compromise the
self-empowerment when you’re feeling internet connection. Ninety-five percent
availability of networks and systems.
down about the latest threat du jour of incidents fell between 13 Mbps and
This pattern includes both network and
that you have no clue how to stop. 99 Gbps, an easily mitigatable range.
application layer attacks, and is the most
Admittedly, as we can see in Figure So, sign up for a DoS mitigation service
common pattern across incidents.
50 it’s not a small threat. In fact it’s and reward yourself with that cannoli
However, don’t let its volume concern
the most common pattern across you’ve had your eye on.
you, as this is often one of the easiest
all incidents.
threats to mitigate effectively.
Frequency 14,335 incidents,
4 with confirmed
data disclosure
55 It’s not just a river in Egypt, Harry.
2021 DBIR Incident Classification Patterns 35

Figure 50. Patterns over time in incidents
Figure 51. Bits per second in DDoS Incidents (n=11,306)
Each dot represents 0.5% of organizations
2021 DBIR Incident Classification Patterns 36

Figure 52. Peak PPS in various DoS locations
Each dot represents 0.5% of organizations
2021 DBIR Incident Classification Patterns 37

One reason DDoS attacks aren’t more In Figure 53 we take a quick look at a We bounce back and forth a bit
of a threat is that those mean56 packets couple of different types of attacks. between packets per second (PPS) and
have to cross a lot of internet to get to DoS attacks can be direct (packets bits per second (BPS). We do so largely
you. Figure 52 covers just how much come directly from the actor or their based on the data we have available,
DDoS is getting blocked at various botnets) or reflected (actor sends but in case that is what’s keeping you
places, from Internet Service Providers packets to a vulnerable service that up at night right now, we’d like to put
(ISPs) at the start of the trip, to then reflects the packets to the your fears to rest.58 For any given
Autonomous System Numbers (ASNs) victim). They can also be intended for packet type (and there are several),
in the middle, to Content Delivery resource exhaustion (send packets that there’s a fixed range of how many bytes
Networks (CDNs) that your site might cause abnormal load on memory or you can expect in the packet. You can
sit behind. All have a hand in mitigating processing) or volumetric (lots and lots see that in the linear nature of Figure
the attack. of packets). What we see is that there 54. And so, whether we’re using BPS or
aren’t many differences between the PPS, the conclusions are still the same.
different attack types (and frankly, a
single DDoS attack57 can use multiple).
Figure 53. Peak BPS in various DoS types
56 Malevolent mean, not average mean.
57 In fact, what is a DDoS attack really? Does it start with the first packet and end with the last? How would we know? What if it’s a different botnet at the
same time? Or if it stops for a few seconds and starts again? Or… or…. When did the DBIR footnotes become the Wikipedia discussion page?
58 Metaphorically and literally.
2021 DBIR Incident Classification Patterns 38

Figure 54. Relationship between PPS and BPS per DoS
2021 DBIR Incident Classification Patterns 39

Figure 55 gives you an idea of the
equality in DDoS packets per second.
It shows that for the majority of
organizations, the data is pretty
spikey. Figure 56 shows predictions
of a Recurrent Neural Network (RNN)
trained on 450,000 DDoS attacks. All
it does is predict the average DDoS
timing and fails if the DDoS is anything
but average. Don’t spend your time
worrying about predicting the next
DDoS. You can’t predict it. Hire a
service to handle it for you and it’s
cannoli time.
Figure 55. Inequality of DDoS PPS by organization (n=54)
Each dot represents 2% of organizations
DoS Index
Figure 56. Predictions of RNN trained to predict the next DDoS
2021 DBIR Incident Classification Patterns 40

Lost and
Stolen Assets
Figure 57. Lost and Stolen Assets incident paths (n=13)
We are all perhaps too familiar with
Summary that sinking feeling of reaching for This primordial fear of
your cellphone in your pocket or purse, misplacing tiny devices that
Devices continue to be lost or stolen, a
only to find it missing. After frantically contain thousands of personal
pattern that is unlikely to change anytime
tearing the house apart, flipping seat
and work-related files is one of
soon. While the actor may be Internal (for
cushions and asking anyone in close
loss) or External (for theft), the controls to the common themes for the
proximity to call your phone, you
protect the data on these devices probably found out that you were breaches and incidents in
remain constant.
holding it all along, or is that just us? this pattern.
Anyway, this primordial fear of
Frequency 1,295 incidents,
misplacing tiny devices that contain
84 with confirmed
thousands of personal and work-
data disclosure This is especially true when it comes to
related files is one of the common
where and how we work. The findings
Threat Actors External (87%), Internal themes for the breaches and incidents here might need to be taken with the
(17%), Multiple (5%), in this pattern. Computers, documents, tiniest speck of salt, as this is not
Partner (1%) (breaches) USB devices and cell phones end up necessarily going to be a representative
disappearing, accidentally or otherwise.
year. Let’s take a dive into the data.
Actor Motives Financial (100%) Like many of the patterns and incidents
(breaches) that we’re covering this year, bear in
mind the unique circumstances of how
Data Personal (80%), we’ve evolved our work habits over the
Compromised Medical (43%), Bank course of 2020.
(9%), Other (7%)
(breaches)
2021 DBIR Incident Classification Patterns 41

Steady-state
thefts and error
While many things have changed over
the last year, some things haven’t
changed a great deal in this pattern.
One of those things is that Error trumps
Theft in incidents. In our data, much like
previous years, Errors in which some
Internal user accidentally mislays an
asset and reports the loss is significantly
more common than someone reporting
an asset stolen. However, for an
organization this is more or less the
same problem: You now have to know
what was on that device, how was it
protected, and how you are going to
respond. The distinction in cases like
this is often a moot point since you’re
probably going to have to remotely wipe
Figure 58. Assets in Lost and Stolen Assets breaches over time
the device either way.
Would you like paper or silicon
for your data breach?
One of the trends that we have noticed over the last few years is the transition from
Media (such as Documents) to User devices (such as Mobile phones) being the
main assets involved in Lost and Stolen breaches. If we needed a barometer as to
when digital transformation occurred, we could probably point back to 2019 when,
for the first time in our dataset’s history, User devices were more frequently stolen
and lost than Documents. This year about 43% of the breached assets with known
data disclosure were Media while the rest are Desktops and laptops (Figure 58).
For incidents where we don’t know if there’s a confirmed breach, cell phones were
lost or stolen the most. Not that we’re gambling people, but if we were to place
money on whether or not this trend will continue, we would probably take the over,
since many new organizations, schools and businesses had to quickly pivot to a
remote workforce.
The type of data lost with the majority of known data breaches involves loss of
Personal data, quickly followed by Medical data, which really shouldn’t be too
surprising. The amount of legislation regarding privacy breach disclosure (medical
and otherwise) would explain why we see this in our data. And lastly, when it comes
to discovering that an asset is lost or stolen (Figure 59), your best line of detection
Figure 59. Discovery methods in Lost and
won’t be the next-gen AI, but your employees themselves. Make sure that they are
Stolen Assets breaches (n=9)
provided with a means to easily report any lost or stolen assets to your organization.
For instance, if they lose their phone they have a number they can call…wait,
never mind. The quicker the organization knows, the better position they’ll be in to
respond. Something…something…obligatory “hindsight is 2020” joke.
2021 DBIR Incident Classification Patterns 42

Miscellaneous
Errors
Figure 60. Miscellaneous Errors incident paths (n=126)
The Miscellaneous Errors pattern We show the breakdown for Internal
Summary should be a familiar frenemy from actors in Figure 61, and they are
years gone past. We have included this relatively intuitive since both system
Errors are unintentional actions, typically
pattern since the beginning, and the administrators and developers typically
taken by an Internal actor, but Partner actor
errors have remained constant. What have privileged access to data on the
errors also occur. Misconfiguration of
can we really say about this pattern? systems they maintain. However, the
database assets being found by Security
Humans make mistakes, often at scale. adage of “to whom much is given, much
researchers is a growing problem.
This pattern consists of Internal and/or is expected” assuredly applies here.
Employees sending data to the wrong
Partner actors only. When people in these roles do make
recipients also continues to be a
mistakes, the scope is often of much
significant issue.
greater significance than the foibles of
an average end-user.
Frequency 919 incidents,
896 with confirmed
data disclosure
Threat Actors Internal (99%), Partner
(1%), Multiple (1%)
(breaches)
Data Personal (79%), Medical
Compromised (17%), Other (13%), Bank
(13%), Credentials (13%)
(breaches)
2021 DBIR Incident Classification Patterns 43

Sadly, Misdelivery remains
alive and well in our dataset,
and while a number of these
breaches are electronic data
only (e.g., email to the wrong
distribution list), there remains
a significant number that
involve paper documents.
Allow us to take you on a tour of
pairings—no, not wine and cheese,
but Actors and Actions. Given the
pairing of sys admins and developers
with the Misconfiguration action
varieties (Figure 62), you can imagine
that this combination can wreak
havoc on the confidentiality of an
organization’s data, or that of their
customers’ or employees’.
The other pairing we frequently
observe is data stores (such as
relational or document databases,
Figure 61. Internal actor varieties in Figure 62. Top Error varieties in
or cloud-based file storage) being
Miscellaneous Errors breaches (n=157) Miscellaneous Errors breaches (n=609)
placed onto the internet with no
controls, combined with the security
researchers who search for them
(Figure 63). These rather undesirable
combinations have been on the rise for
the past few years.
Sadly, Misdelivery remains alive
and well in our dataset, and while
a number of these breaches are
electronic data only (e.g., email to
the wrong distribution list), there
remains a significant number that
involve paper documents (Figure 64).
These are particularly common in
industries in which large mass mailings
are a preferred method of getting
information to the customer base. One
example being when the envelopes
become out of sync with the contents.
Many of these events could be avoided
by a basic sample check at different
points during the mailing process.
Nevertheless, we continue to see this
occurring regularly, but rarely with
any of our bills (those always seem to
arrive on time).
Figure 63. Discovery method varieties in Figure 64. Top Asset varieties in
Miscellaneous Errors breaches (n=110) Miscellaneous Errors breaches (n=635)
2021 DBIR Incident Classification Patterns 44

Personal data is the most
commonly disclosed data
type in these cases by a
wide margin.
The Assets involved in Error
actions run the gamut, from the
aforementioned misconfigured
databases to physical documents
and user devices (Figure 64). A certain
portion of this is from Asset loss,
although if the device is configured
such that unauthorized data access
cannot be confirmed, it would be
considered an incident rather than
a breach.
Personal data is the most commonly
disclosed data type in these cases
by a wide margin (Figure 65). Medical
data is also exposed in this manner,
but not nearly as often. The other data
varieties represented appear in much
smaller quantities.
Just take a gander at that lovely
Discovery timeline in Figure 66. See
how it flexes all of those breaches Figure 65. Top Data varieties in Figure 66. Discovery timeline in
discovered within hours and days of Miscellaneous Errors breaches (n=839) Miscellaneous Errors breaches (n=39)
the event? Surely this is the story of
successful detective controls! Actually,
it may be because people usually
realize they goofed fairly quickly.
But just in case they don’t, they have
the added safety net of legions of
devoted Security researchers out
there scouring the internet with their
specialized search engines just looking
for mistakes.
2021 DBIR Incident Classification Patterns 45

Privilege
Misuse
Figure 67. Privilege Misuse incident paths (n=51)
This pattern is an uncomfortable one— are almost exclusively perpetrated
Summary this is where the people we trust betray by Internal actors (or occasionally by
us. Privilege Misuse is our colleagues Partners), this is the pattern where
Privilege abuse was the most common
deciding (for a number of reasons) to we most frequently see evidence of
action type for this pattern, with the majority
take their access and use it to pilfer multiple types of actors working in
of actors being Financially motivated. The
data they are not authorized to take, concert.
most common data type stolen was Personal
or use it in ways they really shouldn’t.
information, and somewhat surprisingly, the Most Internal actors are motivated
rise in remote workers did not appear to This is the malicious Internal actor by greed—they’re trying to cash in on
have a noticeable effect on Misuse. pattern—the wicked stepsister of the the data they steal. A much smaller
innocent Miscellaneous Errors pattern. percentage are in it for the LOLs.
While Miscellaneous Errors is perhaps Fewer still are holding a grudge
Frequency 265 incidents, 222
a bit of a klutz, Privilege Misuse is against their employer. And finally,
with confirmed data
actively piling chores on us to make we get to those who are doing this to
disclosure
sure we don’t get to attend the ball. start a competing business or benefit
Threat Actors Internal (99%), Multiple their next employer. The last three
Now that we’ve stretched that make up a small percentage of the
(9%), External (8%),
metaphor right to the breaking point, whole, and the main takeaway here is
Partner (2%) (breaches)
let’s move on. You can see in the At- that people are frequently financially
Actor Motives Financial (64%), Fun a-Glance table that most of the cases motivated—whether they have trusted
(17%), Grudge (14%), in which there is Misuse there is also access or not.
Espionage (9%), a confirmed data breach. While these
Convenience (3%),
Ideology (1%) (breaches)
Data Personal (64%), Other
Compromised (35%), Medical (27%),
Internal (19%)
(breaches)
2021 DBIR Incident Classification Patterns 46

How they do
what they do
The most common variety of Privilege
Misuse is Privilege abuse (Figure 68).
The second-place spot went to Data
mishandling. Note, the Other bar is a
combination of the remaining varieties
added together. The majority of
vectors for those were described as
network-based access of some sort to
the assets. We would have expected
an appreciable increase in people
performing Misuse from home, given Figure 68. Top Misuse varieties in Privilege
the increase of those who are working Misuse breaches (n=175)
remotely due to the pandemic. However,
we did not see an increase from Remote
Access as a vector, but it may simply
be that the detail was left out of the
data when the cases were worked, or
organizations aren’t able to detect and
report on this vector of access.
There were a variety of data types
stolen in these cases, with Personal
being in the lead, as shown in Figure 69.
But others included Medical, Internal,
Bank and even Secrets. It usually comes
down to the type of data the individual
can access that drives which variety
they take.
Figure 69. Top Data varieties in Privilege
Misuse breaches (n=176)
2021 DBIR Incident Classification Patterns 47

Discovery all
As we mentioned in the Timeline
section, Misuse breaches can be
difficult to detect. When one compares
the Discovery timeline for this pattern
vs. the overall dataset, it really
illustrates that point, with more Privilege
Misuse cases taking years to discover
than non-Privilege Misuse cases
(Figures 70 and 71).
The three longest timelines (weeks,
months and years) show up even with
each other for Misuse cases this year.
In reality, most organizations have
tailored their controls primarily to
find people trying to get in from the
outside. But for organizations that
have especially sensitive data, such
as Healthcare, along with regulatory
requirements that make reporting
mandatory, it showcases the need for
detective controls that can quickly
catch this kind of misuse. Until they
are in place, and tested, people will
continue their thieving ways.
Figure 70. Discovery timeline in Privilege Figure 71. Discovery timeline in 2021
Misuse breaches (n=22) breaches (n=195)
2021 DBIR Incident Classification Patterns 48

Social
Engineering
Figure 72. Social Engineering incident paths (n=103)
Anyone who has been around children to an uptick in the compromise of
Summary for an extended period of time is well cloud-based mail servers. What we
acquainted with social engineering. cannot say is why email is so enticing to
Phishing is responsible for the vast majority
Watching them trying to convince a threat actors.59 Maybe it’s for the email
of breaches in this pattern, with cloud-based
parent (or sibling) to see things their addresses themselves. Maybe it’s for
email servers being a target of choice.
way can be quite entertaining. Not that the internal information they contain.
Business Email Compromises (BECs) were
you can blame them. We’re all trying to Maybe it’s for the creds, personal
the second most common form of Social
get ahead. But none of us wants to be and other monetizable information.
Engineering. This attack scenario reflects
the one handing over something we’d Or it could simply be that they want
the meteoric rise of Misrepresentation, which
rather keep just because the actor, to repurpose the server to send more
was 15 times higher than last year in Social
whether they are three years old or 30, malicious emails out. Sometimes it’s
incidents. Additionally, Social Engineering
has a really good story about why they best to admit when you just don’t know.
attacks often result in the loss of Credentials.
need it.
This pattern saw those stolen credentials Hopefully it is not a surprise that all
used in both Hacking and Malware attacks. We’ve definitely seen a jump in Social Social Engineering incidents have a
Engineering breaches as a pattern Social action,60 but as you can see in
from last year with an overall upward Figure 72, Malware and Hacking pop
Frequency 3,841 incidents, 1,767
trend since 2017. For the past couple up as well.
with confirmed data
of years, it appears to be correlated
disclosure
Threat Actors External (100%)
(breaches)
Actor Motives Financial (95%),
Espionage (6%)
(breaches)
Data Credentials (85%),
Compromised Personal (17%), Other
59 Just like the old Defcon adage the person on stage (or in this case writing the report) is probably not the
(9%), Medical (4%) smartest person in the room. Maybe in this case, the smartest person is you. If you have data showing what
threat actors are doing with all the email accounts they’re compromising, give us a holler.
(breaches)
60 Mostly delivered by email.
22002211 DDBBIIRR IInncciiddeenntt CCllaassssiiffiiccaattiioonn PPaatttteerrnnss 49

Figure 73. Top Social varieties in Social
Engineering incidents (n=3,810)
A lot of Social Engineering breaches
steal Credentials61 and once you have
them, what better thing to do than to put
those stolen creds to good use, which
falls under Hacking. On the other hand,
that Phishing email may have also been
dropping Malware, which tends to be a
Trojan or Backdoor of some type (Figure
74), a trap just waiting to be sprung.
As with past years, Social actions
are predominantly Phishing, though
Pretexting, normally associated with
the BEC,62 also makes a strong showing.
Remember those children and their great
stories? This is the grownup version of
why they need what you have.
Figure 74. Malware varieties in Social Engineering incidents (n=130)
61 Though we’d be remiss to overlook the second most common data variety: Personal. It’s just that it’s kinda obvious that if someone’s got your email,
they’ve probably also got personal info.
62 Fun fact, BEC doesn’t even have to compromise a business email address. Your.CEO@davesmailservice.com comes up all too often in our dataset.
2021 DBIR Incident Classification Patterns 50

Figure 75. Click rate for organizations
in their last phishing campaign (n=18,177)
Each dot represents 2% of organizations.
Figure 76. Percent of people likely to click various phishing simulation templates (n=1,186,766)
The bars are our confidence. A bigger bar means less confident.
The good news about Phishing is that
the click rate in phishing simulations
is down to a median of 3%. But as we
can see in Figure 75, it’s not “most
companies are around 3%.” Instead,
there’s a long tail of companies with far
larger click rates.
The phishing email itself has a lot to
do with the click rate. An analysis63 of
150 phishing templates found that the
expected click rate varied significantly.
In Figure 76, you can see the click rate
could be anywhere from almost none to
expecting over half of respondents to
click. Additionally, real phishing may be
even more compelling than simulations.
In a sample of 1,148 people who
received real and simulated phishes,
none of them clicked the simulated
phish, but 2.5% clicked the real
phishing email. Finally, phishing volumes
are very unequal. As you can see in
Figure 77, no organizations experienced
consistent malware by email. On the
other hand, most experienced just a Figure 77. Inequality of Malware phishes per day (n=1,767)
few days with extremely high malicious Each dot represents 0.5% of organizations
email volumes.
63 Pretty vague huh. We figured it sounded better than “a Markov Chain Monte Carlo Mixture Model.” That’s just downright scary. (Though we totally did it.)
2021 DBIR Incident Classification Patterns 51

Engineering Incidents
Figure 78 reveals another concerning stat: The majority of Social Engineering
incidents were discovered externally. Out of the top varieties in Figure 79, only
one (Reported by employee) is internal. This means that when employees are
falling for the bait, they don’t realize they’ve been hooked. Either that, or they
don’t have an easy way to raise a red flag and let someone know they might
have become a victim. The former is difficult to address, but the latter is simple
and should be implemented—something as basic as a well-publicized email of
cert@yourorganizationhere.com (which, of course, is monitored) can give you
a heads-up that something is amiss.
Finally, we would be remiss if we let the BECs slide by. They were the second
most common form of Social attacks and, as Figure 80 shows, they’re continuing
to take off. Misrepresentation is 15 times higher than last year in Social Figure 78. Discovery methods in Social
incidents.64 Together with Phishing and Pretexting, Misrepresentation helps drive Engineering incidents (n=691)
the BEC juggernaut. And while the impact can be hard to quantify in some kinds
of incidents, with a BEC it’s a lot easier.65 As we point out in the Impact section,
of the 58% of BECs that successfully stole money, the median loss was $30,000
with 95% of BECs costing between $250 and $984,855. Not bad for a day’s work.
Figure 79. Top discovery methods varieties
in Social Engineering incidents (n=234)
Figure 80. BEC over time in non-DoS incidents
64 We mentioned that BECs don’t even have to compromise an email address, but when they do, using it to send the malicious email is considered a Misrepresentation
integrity compromise.
65 Readers may be familiar with the old cyber shanty regarding phishing. “Soon may the phisherman come, to bring us creds to pwn for fun, one day, when the hacking’s done,
we’ll take our crypto and goooo.....”
2021 DBIR Incident Classification Patterns 52

Building
Cybersecurity
Culture
The conversation about data leakage We used the Huang and Pearlson model
Masha Arbisman has flipped from “if” to “when” a in combination with behavioral science
Behavioral Engineering Manager for the company will be breached by malicious techniques67 to develop a three-step
Paranoids, the information security team actors. The fight against cyber approach68 to drive experimentation
at Verizon Media breaches continues to depend on an and make decisions aimed at improving
organization’s ability to train and adapt the security behaviors of employees.
its members’ behaviors to protect Over two years, the approach tripled
against actions such as credential theft, adoption of a password manager
social engineering, and user error. and decreased the overall phishing
susceptibility of employees by half,
Verizon Media believes the simulations as calculated by the results of our
and training offered by most security phishing simulation programs correlated
education teams do not mimic real with real company attacks measured by
life situations, do not parallel the their Security Operations team.
behaviors that lead to breaches, and
are not measured against real attacks There is no singular approach to
the organization receives. This is why minimizing the human risks that
it is important to progress from the lead to breaches. Each corporation
traditional security awareness model experiences different flavors of the
to that of using behavioral science to same types of attacks and must
change the habits that lead to attack customize their behavioral engineering
path breaking actions. and cybersecurity education programs
accordingly. The Verizon Media data-
Huang and Pearlson’s cybersecurity driven and measurable approach can
culture model66 suggests that cyber be used as a starting point to building
secure behaviors are driven by the customized programs.
values, attitudes, and beliefs of an
organization, which are visible at the
leadership, group, and individual levels.
Influencing how employees prioritize,
interpret, learn about, and practice
cybersecurity allows managers a way
to create a cybersecurity culture within
the organization.
66 https://scholarspace.manoa.hawaii.edu/bitstream/10125/60074/0634.pdf
67 See the Dictionary of Terms in the case study in the next footnote for a list of techniques.
68 https://cams.mit.edu/wp-content/uploads/Verizon-Media-CyberCulture-Paper.pdf
2021 DBIR Incident Classification Patterns 53

System
Intrusion
Figure 81. System Intrusion incident paths (n=251)
Not only is this one of the “newer” Actors in
Summary
patterns, it certainly is one of the more
interesting ones to talk about, as you’ll chains
This new pattern consists of more complex
see in a few. This pattern consists of the
attacks, typically involving numerous steps.
more complex attacks, often involving
The majority of these attacks involve Malware
multiple steps as the attackers move As “trained” data scientists, when
(70%), usually of the Ransomware variety, but
through the environment to find the we’re presented with complex data
also of the Magecart attack type used to
hidden stash of wealth. and detailed charts like Figure
target payment card data in web applications.
81, representing the event chains
Hacking (40%) also appears in many attacks In previous years, some of the incidents associated, we’ll go through and
and most often consists of the Use of stolen we discuss in this section would have quickly triage potential key findings.
credentials or Brute force attacks. fallen under the Cyber Espionage We pull out gems like “there sure
pattern, which would have captured are a lot of colors” and “those lines
most of the hijinks of Nation-states definitely seem long” to see if they
Frequency 3,710 incidents, 966
and their affiliated actors looking for are indeed relevant or statistically
with confirmed data
Secrets. Still others would have been significant. In this case, the lines are
disclosure
found in the Crimeware pattern, and indeed long, indicating that a lot of
Threat Actors External (93%), Internal lastly, the often-forgotten POS server the attacks within this pattern involve
(8%), Multiple (1%) attacks that target servers processing a variety of different actions done by
(breaches) credit cards. Our new System Intrusion actors until they finally achieve their
pattern is intended to capture those goal. Only the Social Engineering
Actor Motives Financial (95%), (sometimes only slightly) more elaborate pattern has a similar number of steps
Espionage (6%) “human-operated” attacks regardless of
(breaches) the motive the actors present. Without
further ado, let’s get into the details.
Data Personal (48%), Other
Compromised (35%), Credentials
(33%), Payment (24%)
(breaches)
2021 DBIR Incident Classification Patterns 54

involved in both data breaches and incidents. In terms of colors, this pattern has a
good combination of mostly Malware events, with some Hacking and a very small
smattering of other Action types as a garnish.
Figure 82 describes this differently, and shows Malware being involved in
over 70% of the cases and Hacking in over 40%. Lastly, at a very high level, we can
tell that the vast majority of the incidents in this pattern are from Financially motivated
External actors. The further we dig, the more interesting this pattern becomes.
When we did a deep dive into the data, we found that there are three main
“components” that make up this pattern. The first is Ransomware, with 99% of the
Ransomware cases falling into this one pattern. The second is Malware in general,
and the third is Magecart attacks in which Web applications are compromised with a
script to export data as it is processed. Let’s go over them.
We’re still writing
about ransomware?
Unfortunately, this is a section that we’ve had to write consistently over the last few
years and odds are that we’ll probably continue to write about this in subsequent
reports. This year, we’re displeased to report that we’ve seen yet another increase
in Ransomware cases, which has been continuing on an upward trend since 2016
and now accounts for 5% of our total incidents. The novel fact is that 10% of all
breaches now involve Ransomware. This is because Actors have adopted the new
tactic of stealing the data and publishing it instead of just encrypting it. These
attacks have some variety in terms of how the Ransomware gets on the system,
Figure 82. Actions in System Intrusion
with Actors having strong preferences that can be broken into several vectors. The
breaches (n=966)
first vector is through the Use of stolen credentials or Brute force. We’ve seen 60%
of the Ransomware cases involving direct install or installation through desktop
sharing apps. The rest of the vectors that we saw were split between Email, Network
propagation and Downloaded by other malware, which isn’t surprising as we found in
our web proxy detections dataset that 7.8% of organizations attempted to download
at least one piece of known Ransomware last year (Figure 83). For these types of
incidents and breaches, we largely see servers being targeted, which makes sense
considering that’s where the data is located.
Figure 83. Ransomware in breaches over time
2021 DBIR Incident Classification Patterns 55

Magecart attacks
30% of the malware was
directly installed by the actor,
The second attack type that we found in this pattern involved the targeting of
23% was sent there by email
Web applications processing Payment cards. Now before you interrupt us and
and 20% was dropped from
ask “but DBIR team, isn’t there a whole pattern dedicated to attacks against Web
a web application. While this
applications?” let us state that the incidents we discuss here are slightly different
than those attacks based on a few key components. The biggest differentiator is the probably doesn’t surprise
subsequent use of Malware to capture Payment card data. In the System Intrusion many people, it does highlight
pattern, we found that of the web servers targeted in this pattern, 60% had malware
the importance of having
installed to capture app data and 65% of incidents involved payment cards. These
a robust defense to cover
types of attacks follow the trends of attack that we in the biz69 have been calling
these three major entry
Magecart-style attacks based on their original targets. For those who aren’t familiar
with this attack archetype, attackers will exploit some vulnerability, then use stolen paths for Malware.
credentials or some other means to access the code of an e-commerce website that
processes credit card data. By using that access to the code base or server, they
will insert additional code that will ship off the payment data not only to the correct
endpoint, but also to their own servers, thereby quietly siphoning off valuable data.
General malware
The final breakdown of this pattern involves the general use of Malware that is
found on a system. In many of these situations, we may not necessarily know if
that Malware would have been used to cause further damage down the road or if it
was just there for the sake of being there, doing the kind of things Malware enjoys
doing.70 When we removed the Ransomware cases, we found that 40% of the
Malware cases we had left involved the use of C2/Trojans/Downloaders. There was
also an interesting split in terms of how the Malware arrived on the system. We found
30% of the malware was directly installed by the actor, 23% was sent there by email
and 20% was dropped from a web application. While this probably doesn’t surprise
many people, it does highlight the importance of having a robust defense to cover
these three major entry paths for Malware.
When it comes down to the daily amount of malware incidents, Figure 84 shows that
for the majority of organizations, this data has a whole lot of spikiness, which means
some days it’s probably relatively quiet—until it’s not.
Figure 84. Inequality of Malware per day (n=16,524)
Each dot represents 0.5% of organizations
69 There is no biz like Cyberbiz.
70 Even Malware wants to live its best life.
2021 DBIR Incident Classification Patterns 56

While we don’t necessarily know the severity of these malware events, we do
know that data from botnet incidents we reviewed indicates that the majority Attackers are less likely to
of botnet infections only compromised three or fewer credentials. So, having purely target Payment data
malware in your environment, if properly cleaned and handled, probably isn’t the and are more likely to broadly
end of the world, but it’s best to not let it fester.
target any data that will impact
the victim organization’s
operations. This will
increase the likelihood
The big picture shifts.
that the organization will pay
up in a Ransomware incident.
In the last few iterations of this report, we have mentioned the decrease in the
targeting of Payment data. We have continued to see this trend in this pattern.
As Figure 85 demonstrates, attackers are less likely to purely target Payment
data and are more likely to broadly target any data that will impact the victim
organization’s operations. This will increase the likelihood that the organization will
pay up in a Ransomware incident. As we have often repeated, the monetization
through Ransomware seems to have become the preferred method, and the
targeting of data will shift to reflect that. The attacks that come out of this pattern
impact all of the industries we track at some level, which shows the wide net that
these Actors cast to turn a profit.
Figure 85. Attribute varieties in breaches over time
2021 DBIR Incident Classification Patterns 57

Basic Web
Application Attacks
Figure 86. Basic Web Application Attacks incident paths (n=130)
Basic Web Application Attacks While the Assets present in this
Summary (or BWAA)—we wanted BWAHA but pattern according to Figure 88 are
we couldn’t justify the H—is the new overwhelmingly represented by the
Basic Web Application Attacks are those with
and improved version of our trusty Hacking of Servers, there are a few
a small number of steps or additional actions
Web Applications pattern. We do realize different sub-patterns encapsulated
after the initial Web application compromise.
the name is a mouthful, but it better here, and they are all easy to explain
They are very focused on direct objectives,
captures the nature of these short and and visualize.
which range from getting access to email and
to-the-point attacks that target open
web application data to repurposing the web web and web-adjacent interfaces (it The first sub-pattern covers the Use
app for malware distribution, defacement or also freshens breath and whitens teeth). of stolen credentials and Brute force
future DDoS attacks. Our other name option was almost as through a Web application vector to
long: Simple Web Attack Group (or compromise either actual Web apps or
SWAG), and perhaps that would have Mail servers, as you can see on Figure
Frequency 4,862 incidents, 1,384
been better, since those attacks are 86. Almost all (96%) of those Mail
with confirmed data
looking for some low-hanging, easily servers compromised were cloud-
disclosure
available knickknacks to grab. based, resulting in the compromise of
Threat Actors External (100%), Internal Personal, Internal or Medical data.
(1%), Multiple (1%)
(breaches)
Actor Motives Financial (89%),
Espionage (7%),
Grudge (2%), Fun (1%)
(breaches)
Data Credentials (80%),
Compromised Personal (53%), Other
(25%), Internal (12%)
(breaches)
2021 DBIR Incident Classification Patterns 58

Figure 87. Actions in Basic Web Application Figure 88. Assets in Basic Web Application
Attacks breaches (n=1,384) Attacks breaches (n=1,369)
Figure 89. Asset varieties in Basic Web
Application Attacks breaches (n=1,324)
2021 DBIR Incident Classification Patterns 59

All of those Brute force
attempts do not happen all
at the same time, or even with
any predictable regularity.
Astute readers will point out that if
using stolen credentials is the leading
characteristic of this part of BWAA,
how is it differentiated from other
threat actor favorites such as Social
Engineering and System Intrusion?
Glad you asked! It turns out that the
credential abuse actions in this pattern
were not preceded by any kind of Social
attacks as far as the victims were aware.
This could mean that either they didn’t
notice it, or that they were victims of
Figure 90. Credential stuffing attempts per organization (n=821)
a credential stuffing attack, where the
Each dot represents 0.5% of organizations.
credentials were actually compromised
elsewhere and were, sadly, the same
on the affected system.
Brute force and credential stuffing
attacks are extremely prevalent
according to SIEM data analyzed in
our dataset. We found that 23% of the
organizations monitored had security
events related to those types of attacks,
with 95% of them getting between 637
and 3.3 billion(!) attempts against them,
as Figure 90 demonstrates. This is a
very large number at face value, but
when you consider the sheer volume of
automated bots and worms looking for
vulnerable services out there, it feels
par for the course.
However, as you may suspect if you have
been reading up on the other patterns,
all of those Brute force attempts do not
happen all at the same time, or even
with any predictable regularity. Figure
91 demonstrates that more often than Figure 91. Inequality of login attempts per day (n=328)
not for the organizations we reviewed, Each dot represents 0.5% of organizations
those attacks happened in very uneven
intervals. It seems the cost of keeping
up with potential credential dumps can’t
be simplified as something you should
do every month or so.
2021 DBIR Incident Classification Patterns 60

The other sub-pattern covers the
exploitation of vulnerabilities in Web
applications. They are not as common
as the credential-related ones, as Figure
92 shows, but they are significant.
Vulnerability exploitation is also the
territory of a sister pattern, System
Intrusion, but those present here in
BWAA are not only focused on Web
applications. They are also attacking
with a small number of steps or
additional actions after the initial
Web application compromise.
In those incidents, the Actor will be
focused on repurposing the web app
for malware distribution, defacement71
or installing malware for future DDoS
attacks and calling it a day. Needless
to say, a lot of the motive here is
Secondary, more precisely in 78% of
incidents. Threat actors are clearly
not wasting the opportunity to shout
“It’s free real estate!” and expand their
nefarious domains. Figure 93 shows
this distribution in incidents, as in
defacement, cases we often cannot get
Figure 92. Top Hacking varieties in Basic Figure 93. Top Integrity varieties in Basic
confirmation of a fully realized breach.
Web Application Attacks incidents (n=947) Web Application Attacks breaches
(n=3,653)
71 It’s the ’90s! Join our DBIR webring in Geocities!
2021 DBIR Incident Classification Patterns 61

Everything
Else
Figure 94. Everything Else incident paths (n=3)
The fairway plot (Figure 94) provides Yes, you read that correctly, we actually
Summary a good illustration of the two main had three cases from the Environmental
types of incidents that ended up in the action that made it into the dataset this
This pattern was recalibrated and now
Everything Else pattern. As you may year. It does our geeky VERIS hearts
consists primarily of Physical tampering
recall from last year, this pattern was proud to finally be able to talk about
cases, in addition to three shiny new
quite popular and could be found in the them. We considered creating “Ask
Environmental cases, which still have
top three patterns in several industries. me about my Environmental breaches”
that new incident smell. It does not feature
It was clearly time for us to recalibrate bumper stickers, but bumper stickers
prominently in any of the industries this year
when our catch-all bucket was full to are bad for the environment.
and has been relegated to the “stuff leftover
overflowing with incidents that didn’t fit
that didn’t fit in anywhere else” status it the other patterns. We used to have (back in the murky
formerly occupied prior to the astronomical depths of antiquity) an entire pattern
rise of Social Engineering. Now that we’ve sifted through the data devoted to Payment Card Skimmers,
and completed our recalibration (which but they have been decreasing
is covered at length in the Introduction dramatically in our dataset over the
Frequency 129 incidents, 38 with
to Patterns section), there are still a years. This year we saw an even
confirmed data
few incidents and breaches that fit into sharper drop-off than ever before.
disclosure
the Everything Else pattern. They are There were only 20 skimming incidents
Threat Actors External (95%), Internal Physical tampering cases (think ATM (all confirmed breaches) in the dataset
and gas pump skimmers) and the so- this year. We attribute this decrease, at
(5%) (breaches)
rare-we-are-excited-to-be-able-to-talk- least in part, to the travel restrictions
Actor Motives Financial (100%) about-it-FINALLY Environmental cases. related to COVID-19.
(breaches)
Data Payment (61%-96%)
Compromised (breaches)
2021 DBIR Incident Classification Patterns 62

In prior years, particularly in the public dataset (VCDB),72 we saw evidence of Environmental
skimming groups from abroad coming into the U.S. and installing skimming devices # breaches variety
on their infrastructure of choice (some favor ATMs, some focus on Gas terminals).
In fact, one could almost plot their progress along the major routes before they 1 Fire
would presumably return to their place of origin along with their stolen data. Given
the travel restrictions that began in March 2020, the freedom to carry out this type
1 Hurricane
of concentrated raid has significantly diminished. And while it is possible that this
kind of breach is no longer being tracked at the national level, we like to think there
is at least one positive outcome from what has been a very difficult year for most of 1 Tornado
the world.
Now, on to our Environmental breaches. As mentioned, we only have three of Table 3. Environmental breaches
them, which is admittedly a very small number. However, they are separate and
distinct events. We saw incidents that arose from one fire, one hurricane and one
tornado (Table 3). All three affected paper documents strewn to the winds (in the
classic Wizard of Oz fashion) from the violence of their encounters with the forces
of nature. The actor in these cases is considered External of type Force majeure.
We hope nature will now retire from the data breach stage and leave the loss of
records to the normally scheduled actors.
72 https://github.com/vz-risk/VCDB
2021 DBIR Incident Classification Patterns 63

04
Industries

Introduction to
industries
This year we looked at 29,207 incidents,  than a small mom and pop shop with no  derived from that small number must
which boiled down to 5,258 confirmed  internet presence, but who uses a Point  also be less.
data breaches (Table 4). Once again, we  of Sale vendor to manage their systems.
As in past years, we have broken down
break these incidents and breaches into  The infrastructure, and conversely the
the breaches and incidents by industry
their respective industries to illustrate  attack surface, largely drives the risk.
that all industries are not created equal  in a heat map that categorizes the
in terms of attack surfaces and threats.  While keeping that in mind, we caution  data into Patterns, Actions and Assets
The kinds of attacks suffered by a  our readers not to make inferences about  (Figures 95 and 96 respectively). These
particular industry will have a lot to do  the security posture (or lack thereof) of  figures help to answer the “so what?”
a particular sector based on how many  question in our data, and are useful as
with what kind of infrastructure they rely
breaches or incidents that industry  indications of what attack patterns an
on, what kind of data they handle, and
how people (customers, employees and  reports. These numbers are heavily  organization is most likely to encounter,
everyone else) interact with them.  influenced by several factors, including  given their industry. This, paired with the
data breach reporting laws and partner  CIS Controls in each industry section,
A large organization whose business  visibility. Because of this, some of the  can be a guide for determining how best
model focuses entirely on mobile  industries have very low numbers, and as  to mitigate risk.
devices, where customers use an app  with any small sample, we must caution
on their phone, will have different risks  you that our confidence in any statistics
Incidents Total Small (1-1,000) Large (1,000+) Unknown Breaches Total Small (1-1,000) Large (1,000+) Unknown
| Total                  | 29,207 | 1,037 | 819 27,351 | 5,258 | 263 | 307 | 4,688 |
| ---------------------- | ------ | ----- | ---------- | ----- | --- | --- | ----- |
| Accommodation (72)     | 69     | 4     | 7 58       | 40    | 4   | 7   | 29    |
| Administrative (56)    | 353    | 8     | 10 335     | 19    | 6   | 7   | 6     |
| Agriculture (11)       | 31     | 1     | 0 30       | 16    | 1   | 0   | 15    |
| Construction (23)      | 57     | 3     | 3 51       | 30    | 3   | 2   | 25    |
| Education (61)         | 1,332  | 22    | 19 1,291   | 344   | 17  | 13  | 314   |
| Entertainment (71)     | 7,065  | 6     | 1 7,058    | 109   | 6   | 1   | 102   |
| Finance (52)           | 721    | 32    | 34 655     | 467   | 26  | 14  | 427   |
| Healthcare (62)        | 655    | 45    | 31 579     | 472   | 32  | 19  | 421   |
| Information (51)       | 2,935  | 44    | 27 2,864   | 381   | 35  | 21  | 325   |
| Management (55)        | 8      | 0     | 0 8        | 1     | 0   | 0   | 1     |
| Manufacturing (31-33)  | 585    | 20    | 35 530     | 270   | 13  | 27  | 230   |
| Mining (21)            | 498    | 3     | 5 490      | 335   | 2   | 3   | 330   |
| Other Services (81)    | 194    | 3     | 2 189      | 67    | 3   | 0   | 64    |
| Professional (54)      | 1,892  | 793   | 516 583    | 630   | 76  | 121 | 433   |
| Public (92)            | 3,236  | 22    | 65 3,149   | 885   | 13  | 30  | 842   |
| Real Estate (53)       | 100    | 5     | 3 92       | 44    | 5   | 3   | 36    |
| Retail (44-45)         | 725    | 12    | 27 686     | 165   | 10  | 19  | 136   |
| Wholesale Trade (42)   | 80     | 4     | 10 66      | 28    | 4   | 7   | 17    |
| Transportation (48-49) | 212    | 4     | 17 191     | 67    | 3   | 8   | 56    |
| Utilities (22)         | 48     | 1     | 2 45       | 20    | 1   | 2   | 17    |
| Unknown                | 8,411  | 5     | 5 8,401    | 868   | 3   | 3   | 862   |
| Total                  | 29,207 | 1,037 | 819 27,351 | 5,258 | 263 | 307 | 4,688 |
Table 4. Number of security incidents and breaches by victim industry and organization size
| 2021 DBIR  Industries |     |     |     |     |     |     | 65  |
| --------------------- | --- | --- | --- | --- | --- | --- | --- |

Breaches
Figure 95. Breaches by industry
2021 DBIR Industries 66
nrettaP
noitcA
tessA

Incidents
Figure 96. Incidents by industry
2021 DBIR Industries 67
nrettaP
noitcA
tessA

When discussing the industries with a It is worth noting that some of the
small sample, we will provide ranges industry sections this year may look Check out our riveting
within which the actual value may smaller than usual. This is because Methodology section for
reside. This allows us to maintain we did not want to steal the thunder more information about
our confidence interval while still from the deep-dive analysis we did on
the statistical confidence
providing you with an idea of what the new Patterns. If you are just here
background used
the actual number might be, had we for a glimpse of your industry,73 our
been given a large enough sample. recommendation is to verify what the throughout this report.
For example, instead of saying “In Top Patterns are in the At-a-Glance
the Accommodation industry, 92% of table accompanying each industry
attacks were Financially motivated,” and then spend some time with those
we show that Financially motivated pattern sections.
attacks ranged between 86 and 100%.
Check out our riveting Methodology We also provide a description of which
section for more information about the CIS Controls from Implementation
statistical confidence background used Group 1 (IG1) to prioritize in each
throughout this report. industry section for ease of reading
in case you want to get straight to
strategizing your security moves.
73 We can’t blame you. Sometimes we eat the dessert first, too.
2021 DBIR Industries 68

Accommodation and
Food Services
The Accommodation and Food Services Industry (NAICS 72) shows fewer breaches
this year than in the past (92 last year). A logical explanation for this would be that due
to the global conditions during the greater part of 2020, travel and dining out were
significantly curtailed. That would result in fewer transactions, and by extension, less
breaches. Nevertheless, 40 incidents are a statistically sufficient number for us to
derive some conclusions. The most prevalent patterns in this industry were System
Intrusion, Social Engineering and Basic Web Application Attacks, although there was
almost nothing to tell them apart (Figure 97).
Frequency 69 incidents, 40 with
confirmed data
disclosure
Top Patterns System Intrusion, Social
Engineering and Basic
Web Application
Attacks represent 85%
of breaches
Threat Actors External (90%), Internal
(10%) (breaches)
Actor Motives Financial (86%-100%),
Espionage (0%-14%)
(breaches)
Data Personal (51%),
Compromised Credentials (49%),
Payment (33%), Other
(15%) (breaches)
Top IG1 Security Awareness
Protective and Skills Training (14),
Controls
Access Control
Management (6),
Secure Configuration of
Enterprise Assets and
Software (4)
69
SCIAN
27
Summary
The Accommodation and Food Services
industry is experiencing Hacking, Social
and Malware attacks with close to
equal frequency.
Figure 97. Patterns in Accommodation and Food Services breaches (n=40)
As pointed out elsewhere in this report, certain Action types have been clustered
together to form the System Intrusion pattern. This includes Malware actions that would
have previously been found in the Crimeware pattern. However, while the patterns may
have changed, as you can see in Figure 98, the malware prevalent in this industry is of
the Backdoor, C2 and Trojan varieties that we have witnessed in previous years.
2021 DBIR Industries

Direct installation by the attacker is by
far the most common vector for the
malware seen in this vertical.
With regard to data type, Credentials
(49%), Personal (51%) and Payment
(33%) all come in at or near the same
number, and are again what one might
expect as a result of the attack types
mentioned above. Finally, while we
must admit that our sample size is very
small (n=18), the Discovery method,
when known, is (as it has been for
many years) via a third party, 39%-
75%. Usually via notification by law
enforcement or from a Common Point
of Purchase audit, but in some cases by
the threat actors themselves. We would
love to see some positive change in
Discovery methods for this industry, as
it only stands to reason that the impact
of a breach will likely be greater if you
have to wait for someone outside of
your organization to inform you.
Figure 98. Top Malware varieties in
Accommodation and Food Services
breaches (n=13)
2021 DBIR Industries 70

Arts, Entertainment
and Recreation
While the way in which we consumed entertainment changed this year, hopefully
temporarily, attackers continued to follow the same winning combination that
they’ve been using for the last few years in this industry. Namely, targeting web
applications and utilizing malware to its fullest extent. And of course, there was
the occasional human blunder that serves to keep life interesting.
Frequency 7,065 incidents, 109
with confirmed data
disclosure
Top Patterns System Intrusion, Basic
Web Application
Attacks and
Miscellaneous Errors
represent 83% of
breaches
Threat Actors External (70%), Internal
(31%), Multiple (1%)
(breaches)
Actor Motives Financial (100%)
(breaches)
Data Personal (83%),
Compromised Credentials (32%),
Medical (26%), Other
(18%) (breaches)
Top IG1 Security Awareness
Protective and Skills Training (14),
Controls Secure Configuration
of Enterprise Assets
and Software (4),
Access Control
Management (6)
71
SCIAN
17
Summary
The Use of stolen credentials, Phishing and
Ransomware continue to play big roles in
this industry. Compromised Medical
information was seen at an unexpectedly
high level as well.
FPO
Figure 99. Patterns in Arts and Entertainment breaches
System Intrusion, Web Applications and Errors are more or less tied for the
top ranking. Their combined weight accounts for 83% of the breaches in this
sector. This is in line with the trend set in previous years, and what we saw in last
year’s report (Figure 99). With that in mind, it is perhaps only to be expected that
action types such as the Use of stolen credentials, Ransomware, Phishing and
Misconfiguration were responsible for most breaches (Figure 100).
2021 DBIR Industries

What was a bit surprising was the high From an incident point of view, DDoS
level of Medical information breached attacks were once again quite high
in this sector. One would typically this year. This is potentially due to the
associate medical record loss with the gambling websites that also reside
Healthcare industry. However, upon in this sector. Therefore, if you are
digging into the data a bit more, the operating an online gambling platform
Personal Health Information (PHI) was the safe bet is to plan for DDoS,
related to athletic programs, which fall because the house always needs
under this vertical. It is possible the to win.
medical nature of the data was unclear,
and so the worst case (medical rather
than just personal) data was reported.
Still, this reveals an important lesson:
Don’t assume that because your
organization is not in the medical field
that you don’t possess medical data
(or that you don’t have a duty to ensure
that it is protected appropriately).
Figure 100. Top Actions in Arts and
Entertainment breaches (n=90)
2021 DBIR Industries 72

Educational
Services
The Education sector has certainly had a challenging year, with the pandemic
mandating that classes be held online, in a hybrid form and sometimes not at all.
With those challenges comes opportunity—mostly for criminals. This sector is
assailed by Financially motivated actors looking to gain access to the data and
systems of the people who are just trying to get through the school day.
Frequency 1,332 incidents, 344
with confirmed data
disclosure
Top Patterns Social Engineering,
Miscellaneous Errors
and System Intrusion
represent 86% of
breaches
Threat Actors External (80%), Internal
(20%), Multiple (1%)
(breaches)
Actor Motives Financial (96%),
Espionage (3%), Fun
(1%), Convenience (1%),
Grudge (1%) (breaches)
Data Personal (61%),
Compromised Credentials (51%), Other
(12%), Medical (7%)
(breaches)
Top IG1 Security Awareness
Protective and Skills Training (14),
Controls
Access Control
Management (6),
Secure Configuration
of Enterprise Assets
and Software (4)
One of the top patterns in this industry is Social Engineering (Figure 101), and in
looking at these cases, we find a larger than usual amount of Pretexting. Frequently,
Social Engineering aficionados will craft a simple phishing email and wait for their
victims to reach out to them. In the Education sector, they seem to be harkening
back to their creative writing courses, and are putting forth the effort to invent a
convincing scenario to get their victim to respond (Figure 102).
2021 DBIR Industries 73
SCIAN
16
Summary
The Education vertical has an unusually
large percentage of Social Engineering
attacks in which Pretexting is the variety.
These are typically with a view toward
instigating a fraudulent transfer of funds.
Miscellaneous Errors and System Intrusion
are both still enrolled as well, and are taking
a full load.
Figure 101. Patterns in Education breaches (n=344)

Are they getting good grades for this kind of attack. Other controls to The System Intrusion pattern tells a
their efforts? Yes, they get an A for prevent wire transfers to new bank tale of two actions—namely Hacking
“appropriation” of funds that do not accounts should also be put in place. and Malware. Credential attacks are
belong to them. Considering their the most common starting point, with
continued success at causing money Miscellaneous Errors and System the credentials frequently coming from
to be transferred to them, they have Intrusion were almost tied in their bid the result of other breaches and/or
clearly mastered the art of believability for second place in the patterns for credential re-use. The attacker moves
in their prose. this sector. We see Misconfiguration on to installing malware once they have
(largely of databases that are spun up their foothold established. Ransomware
It stands to reason that people with without the benefit of access controls, is a favorite malware flavor, and we’ve
access to wire transfers and other open for the world to see because seen some groups taking copies of the
kinds of payments should be targeted knowledge wants to be free, right?) as data prior to triggering the encryption
for special training to help combat the most common variety (Figure 103). and then using it as further pressure
against the victim.
Ransomware is a favorite
malware flavor, and we’ve
seen some groups taking
copies of the data prior to
triggering the encryption and
then using it as further
pressure against the victim.
Figure 102. Social varieties in Education
breaches (n=164)
Figure 103. Error varieties in Education
breaches (n=33)
2021 DBIR Industries 74

Financial and
Insurance
The Financial Services industry has long been known for rapid changes, including
sudden dips, dizzying highs and unforeseen fluctuations (thanks, Reddit users).
This vertical has seen quite a diverse set of changes when it comes to the
cybersecurity landscape as well. One that we have seen over the last few years
has been a convergence of Internal actors and their associated actions with the
more famous and nefarious External varieties.
This year, 44% of the breaches in this vertical were caused by Internal actors
(having seen a slow but steady increase since 2017) (Figure 104). The majority of
actions performed by these folks are the accidental ones, specifically the sending
Frequency 721 incidents, 467 with
of emails to the wrong people, which represents a whopping 55% of all Error-based
confirmed data
breaches (and 13% of all breaches for the year).
disclosure
Top Patterns Miscellaneous Errors,
Basic Web Application
Attacks and Social
Engineering represent
81% of breaches
Threat Actors External (56%), Internal
(44%), Multiple (1%),
Partner (1%) (breaches)
Actor Motives Financial (96%),
Espionage (3%),
Grudge (2%), Fun (1%),
Ideology (1%)
(breaches)
Data Personal (83%), Bank
Compromised (33%), Credentials
(32%), Other (21%)
(breaches)
Top IG1 Security Awareness
Protective and Skills Training (14),
Controls
Secure Configuration of
Enterprise Assets and When we turn our attention to malicious External actors, the Financial industry
Software (4), Access faces a similar onslaught of Credential attacks, Phishing and Ransomware attacks
Control Management (6) that we see topping the charts in other industries. With regard to data type,
Personal comes in first, followed by Credentials and Bank data, hardly surprising
given the focus of the industry.
Finally, this industry continues to be heavily reliant upon external parties for breach
discovery. Typically via bad actors making themselves known (38% of the incidents)
or notification from monitoring services (36% of incidents).
75
SCIAN
25
Summary
Misdelivery represents 55% of
Financial sector errors. The Financial
sector frequently faces Credential
and Ransomware attacks from
External actors.
Figure 104. Actors in Finance breaches over time
2021 DBIR Industries

Healthcare
Since 2019, the Healthcare sector has seen a shift from breaches caused by
Internal actors to primarily External actors. This brings this vertical in line with the
long-term trend seen by the other industries. This is good news actually, as no
industry wants their employees to be their primary threat actor. While one of the
top patterns for Healthcare continues to be Miscellaneous Errors, with Misdelivery
being most common, at least errors are not malicious in nature (Figure 105). The
insider breaches that were maliciously motivated have not shown up in the top
three patterns in Healthcare for the past several years. But does this mean they
are no longer occurring, or are they still around but we just aren’t catching them
(like Bigfoot)? Only time will tell.
For the second year in a row, we have seen Personal data compromised more often than
Medical in this sector. That strikes us as strange, given the fact that this is the one sector
where you would expect to see Medical information held most commonly. However, with
the increase of External actor breaches, it may simply be that the data taken is more
opportunistic in nature. If controls, for instance, are more stringent on Medical data, an
Frequency 655 incidents, 472 with
attacker may only be able to access Personal data, which is still useful for financial fraud.
confirmed data
Simply put, they may take what they can get and run.
disclosure
Top Patterns Miscellaneous Errors,
Basic Web Application
Attacks and System
Intrusion represent
86% of breaches
Threat Actors External (61%), Internal
(39%) (breaches)
Actor Motives Financial (91%), Fun
(5%), Espionage (4%),
Grudge (1%) (breaches)
Data Personal (66%), Medical
Compromised (55%), Credentials
(32%), Other (20%),
(breaches)
Top IG1 Security Awareness
Protective and Skills Training (14),
Controls
Secure Configuration
of Enterprise Assets
and Software (4),
Access Control
Management (6)
2021 DBIR Industries 76
SCIAN
26
Summary
Basic human error continues to beset this
industry as it has for the past several years.
The most common Error continues to be
Misdelivery (36%), whether electronic or
of paper documents. Malicious Internal
actions, however, have dropped from the
top three for the second year in a row.
Financially motivated organized criminal
groups continue to target this sector, with
the deployment of Ransomware being a
favored tactic.
Figure 105. Error varieties in Healthcare breaches (n=70)

Information
Errors and accidents, depending on your worldview, are either natural occurrences
of complex systems or the fault of an intern who overcame your organization’s
robust and well-crafted safeguards. Regardless of your opinions on errors, they
certainly are not uncommon in the Information sector. The pattern of Miscellaneous
Errors, along with Basic Web Application Attacks and System Intrusion, accounted
for 83% of breaches in this vertical.
Frequency 2,935 incidents, 381
with confirmed data
disclosure
Top Patterns Basic Web Application
Attacks, Miscellaneous
Errors and System
Intrusion represent 83%
of breaches
Threat Actors External (66%), Internal
(37%), Multiple (4%),
Partner (1%) (breaches)
Actor Motives Financial (88%),
Espionage (9%),
Grudge (2%),
Convenience (1%), Fun
(1%) (breaches)
Data Personal (70%),
Compromised Credentials (32%),
Other (27%), Internal
(12%) (breaches)
Top IG1 Security Awareness
Protective and Skills Training (14), In terms of the types of Errors seen, Misconfigurations accounted for over 70%
Controls Secure Configuration of of all Errors in this industry (Figure 106). This was followed by a three-way tie
Enterprise Assets and of Misdeliveries, Programming and Publishing Errors. With this combination, it
Software (4), Access shouldn’t be a surprise that System Engineers (or are they called DevOps 24/7
Control Management (6) Super Engineers?) had a strong showing in terms of the Internal actors responsible
for those breaches. While the overall percentage of Error breaches hasn’t increased
over the last few years, it remains a persistent issue facing organizations in
this sector.
77
SCIAN
15
Summary
This industry struggles with credential
stealing botnets. Errors are also very
common with Misconfiguration leading the
way. From an incident perspective, DoS
attacks accounted for the vast majority
of attacks.
Figure 106. Error varieties in Information breaches (n=111)
2021 DBIR Industries

When organizations discover that then make the notification. Speaking of we observed, with the rest being
something unpleasant has occurred, Security researchers, they accounted credential-based attacks such as Brute
External actors typically delivered the for 30% of these data breach force or the Use of stolen credentials.
news (Figure 107). We found that 50% discoveries.
of the breaches were disclosed by the We identified another interesting finding
bad actor themselves, which sounds If we look at only incidents, we find that in the Information industry when we
helpful of them, but really isn’t. This this industry tends to be bombarded analyzed botnet-related breaches. This
is usually done either when a ransom with DoS attacks, a trend that has year, the amount of credential stealing
note politely informs you that you’re been occurring ever since computers botnet breaches targeting Information
going to have a really bad day, or were networked, or at least since we’ve organizations overtook the Finance
when actors openly share or sell your been doing this report (Figure 108). sector (Figure 109). Data is really the
data on forums that are monitored by Of the incidents, DoS alone accounts new oil, it seems.
researchers and advisories alike—who for over 90% of the Hacking actions
Industry
Figure 107. Top Discovery method varieties Figure 108. Top Hacking varieties in
in Information breaches (n=84) Information incidents (n=2,452)
Figure 109. Industries in botnet breaches
(n=222,162)
2021 DBIR Industries 78

Manufacturing
As we confronted our organic almond milk and toilet paper shortages this past year,
we were reminded of the real implications of continuous strain on factories and the
manufacturing supply chain. Certain areas in this vertical faced some very unique
and difficult challenges in 2020 due to the demand created by the pandemic. Even
so, the Manufacturing sector was still not given a free pass by the threat actors who
are not known for their magnanimity.
However, the challenges faced from a cybercrime perspective were not unique. In fact,
Manufacturing suffered most from the same devious trio of System Intrusion, Social
Frequency 585 incidents, 270
Engineering and Basic Web Application Attacks as did our overall breach dataset.
with confirmed data
disclosure
Top Patterns System Intrusion,
Social Engineering and
Basic Web Application
Attacks represent 82%
of breaches
Threat Actors External (82%), Internal
(19%), Multiple (1%)
(breaches)
Actor Motives Financial (92%),
Espionage (6%),
Convenience (1%),
Grudge (1%), Secondary
(1%) (breaches)
Data Personal (66%),
Compromised Credentials (42%),
Other (36%), Payment
(19%) (breaches)
Top IG1 Security Awareness
Protective and Skills Training (14),
Controls
Access Control
Management (6),
Secure Configuration
of Enterprise Assets
and Software (4)
The scenarios play out in Figure 110, which illustrates the top Actions taken in each
step of the breach. Threat actors were more likely to use a Social attack (75.4%
were Phishing) or a Hacking attack (79.5% were Use of stolen credentials) to gain
the initial foothold. From there, either additional Credentials would be compromised
and utilized, or Malware would be installed.
79
SCIAN
33-13
Summary
This industry, like many others, is beset by
Social Engineering attacks. Manufacturing
also saw a marked rise in Ransomware
related breaches.
Beginning Middle End
Figure 110. Actions at the beginning, middle and end of Manufacturing breaches
2021 DBIR Industries

On that note, Ransomware played customer PII) overtook Credentials, If you are asking yourself the question
a significantly increased role in thus breaking the statistical tie we saw “who would win in a fight: massive
Malware associated breaches (61.2%) between them last year. This suggests factories or one “encrypt-y boi?”
in relation to previous years. This is more Actors are achieving their final the result may surprise you. This
likely attributable to the continued goals, since Credentials breaches is definitely a great area to focus
rise of “name and shame” tactics of happen naturally as an attacker moves improvement with regard to this
Ransomware actors. In those cases, within an environment. sector’s defense strategy.
we can be sure the data has been
compromised as well as rendered The number of ransomware related
inaccessible in place. Malware incidents (as opposed to
breaches discussed above) also
Personal data was the most saw a sharp increase from last year, The number of ransomware
compromised data type in this sector, overtaking both DoS and Phishing as related Malware incidents
possibly also related to increased the most common varieties of attacks (as opposed to breaches) also
automation and the ease of attack. shown in Figure 111.
saw a sharp increase from last
This data type (mostly consisting of
year, overtaking both DoS and
Phishing as the most common
varieties of attacks.
Figure 111. Top Action varieties in Manufacturing incidents (n=476)
2021 DBIR Industries 80

Mining, Quarrying,
and Oil & Gas
Extraction + Utilities
While most of us do not have to think about how to extract precious metals and
minerals, or how to generate electricity and manage the complex infrastructure
required to power up your PlayStation 5 (if you could find one), the folks in these
industries have to do all those things on a daily basis. Not only must they combat
various environmental threats, like thunderstorms, broken pipes and squirrels, but
they also face threats from the cyber world. Let us dig into the industries that have
made our modern connected world possible, despite how that modern connected
world tries to bite the hands that feed them.
These industries do not differ vastly from other industries in regard to the top three
Frequency 546 incidents, 355 with
patterns. However, the breakdown of these patterns does vary. In this sector, Social
confirmed data
Engineering seems to be dominating both breaches and incidents this year, with
disclosure
sustained phishing campaigns occurring against some organizations (Figure 112).
Top Patterns Social Engineering, Social Engineering accounts for 86% of the breaches in this vertical, followed by
System Intrusion and System Intrusions and Basic Web Application Attacks.
Basic Web Application
The next most common type of attack is Ransomware, which accounts for 44% of
Attacks represent 98%
non-Social Engineering attacks in this industry.
of breaches
Threat Actors External (98%), Internal
(2%) (breaches)
Actor Motives Financial (78%-100%),
Espionage (0%-33%)
(breaches)
Data Credentials (94%),
Compromised Personal (7%), Internal
(3%), Other (3%)
(breaches)
Top IG1 Security Awareness
Protective and Skills Training (14),
Controls
Access Control
Management (6),
Account Management (5)
81
SCIAN 22+12
Summary
These industries suffered from Social
Engineering attacks this year. Credentials,
Personal and Internal data are the most
commonly lost data varieties. Ransomware
is also a major threat for these verticals.
Social Engineering
Figure 112. Patterns in Mining and Utilities incidents over time
2021 DBIR Industries

Professional,
Scientific and
Technical Services
 SCIAN
45
If Professional Services is your sector,
Summary
you know that it is at best an eclectic
NAICS code, with members that have
The combination of the System Intrusion  wildly different footprints in terms of
and Social Engineering patterns account   attack surfaces. One thing they seem
for the majority of cases in this sector. The
to have in common is their reliance on
Use of stolen credentials is widespread and
internet connected infrastructure, and
employees have a definite tendency to fall
the risk inherent in that architecture.
for Social tactics.
The System Intrusion and Social
Engineering patterns competing for
the top slots illustrates not only the
| Frequency | 1,892 Incidents, 630  |                                        |
| --------- | --------------------- | -------------------------------------- |
|           | with confirmed data   | vulnerability of that infrastructure,  |
|           | disclosure            | but also of the employees of these     |
organizations (Figure 113).
| Top Patterns | System Intrusion, Social  |                                         |
| ------------ | ------------------------- | --------------------------------------- |
|              | Engineering and Basic     | The actors behind the System Intrusion  |
pattern have some powerful tools at
Web Application
their disposal to gain access to their
Attacks represent 81%
targets. Some of these cases began
of breaches
with the Use of stolen credentials or
Threat Actors External (74%), Internal  Exploiting a vulnerability, and ended
|     | (26%) (breaches) | with Malware being dropped on their  |
| --- | ---------------- | ------------------------------------ |
victims. Frequently that malware was
| Actor Motives | Financial (97%),       | Ransomware, leading to extortion   |
| ------------- | ---------------------- | ---------------------------------- |
|               | Espionage (2%),        | demands and downtime. The overall  |
|               | Grudge (1%) (breaches) | rise of Ransomware is something    |
we’ve talked about in prior DBIRs, and
| Data  | Credentials (63%),  |     |
| ----- | ------------------- | --- |
the trend shows no signs of slowing.
| Compromised | Personal (49%), Other  |     |
| ----------- | ---------------------- | --- |
The growing tactic of the adversaries
|     | (21%), Bank (9%)  | taking a copy of the data as a prod to  |
| --- | ----------------- | --------------------------------------- |
|     | (breaches)        | help encourage their victims to pay up  |
(which we saw begin just after the data
| Top IG1     | Security Awareness  |                                       |
| ----------- | ------------------- | ------------------------------------- |
| Protective  |                     | collection period had ended for last  |
and Skills Training (14),
| Controls |     | year’s report) has become increasingly  |
| -------- | --- | --------------------------------------- |
Access Control
popular as well. Thus we see a rise  Figure 113. Patterns in Professional
Management (6),
of Ransomware cases where there is  Services breaches (n=630)
Secure Configuration
also a confirmed data breach, as these
of Enterprise Assets
actors post copies of their victim’s data
and Software (4)
on the internet.
2021 DBIR  Industries 82

Combine this with the Social
Engineering pattern, and you Phishing was the leading Social
have to worry about not only your action, but we also saw a good
infrastructure, but your people’s representation of Pretexting
ability to withstand Social tactics as
via email.
well. Phishing was the leading Social
action, but we also saw a good
representation of Pretexting via
email (Figure 114).
When you have the use of an
invented scenario, the follow-on
action is frequently an attempt to get
money. This shows up in our data
as a Fraudulent transaction and is
represented along with the Integrity
violation of Alter behavior when
someone falls for the Social action
(Figure 115).
Figure 115. Top Integrity varieties in
Professional Services breaches (n=337)
Figure 114. Social varieties in Professional
Services breaches (n=191)
2021 DBIR Industries 83

Public
Administration
The Social Engineering pattern was responsible for over 69% of breaches in this
vertical (Figure 116). Clearly, this industry is a favorite honey hole among the phishing
fiends. The Social actions were almost exclusively Phishing with email as the vector
(Figure 117). Pretexting was rarely leveraged at all, and why should they go to all the
work of inventing a scenario when a straight up phish gets the job done?
Frequency 3,236 incidents, 885
with confirmed data
disclosure
Top Patterns Social Engineering,
Miscellaneous Errors
and System Intrusion
represent 92% of
breaches
Threat Actors External (83%), Internal
(17%) (breaches)
Actor Motives Financial (96%),
Espionage (4%)
(breaches)
Data Credentials (80%),
Compromised Personal (18%), Other
(6%), Medical (4%)
(breaches)
Top IG1 Security Awareness
Protective and Skills Training (14),
Controls
Access Control
Management (6),
Account Management (5)
84
SCIAN
29
Summary
By far the biggest threat in this industry is
the social engineer. Actors who can craft
a credible phishing email are absconding
with Credentials at an alarming rate in
this sector.
Figure 117. Social varieties in Public
Administration breaches (n=611)
Figure 116. Patterns in Public Administration
breaches (n=885)
2021 DBIR Industries

The Miscellaneous Errors pattern was
a far distant second and consisted of
Misconfiguration (although not usually
found by Security researchers—which
was a surprise, as that is the most
common pairing) and Misdelivery
(Figure 118). Certainly, government
entities are responsible for a lot of
mass mailings, and paper documents
were the second most common assets
that were delivered to the wrong
recipient, with good old-fashioned
emails taking first place.
The System Intrusion pattern rounds
out our top three and is a combination
of Hacking and Malware actions. We
found the Use of stolen credentials,
followed by dropping Malware with
either C2 or ransomware capabilities
to be the most common story in
this pattern.
The most frequently stolen data type
is Credentials, which are then used
to further the attacker’s presence
in the victim’s network and systems
(Figure 119). After Credentials Personal
information is the top data type
compromised where breaches were
confirmed in this sector.
Figure 118. Top Error varieties in Public
Administration breaches (n=86)
Figure 119. Top Data varieties in Public
Administration breaches (n=841)
2021 DBIR Industries 85

Retail
Frequency 725 incidents, 165 with
confirmed data
disclosure
Top Patterns System Intrusion, Social
Engineering and Basic
Web Application
Attacks represent 77%
of breaches
Threat Actors External (84%), Internal
(17%), Multiple (2%),
Partner (1%) (breaches)
Actor Motives Financial (99%),
Espionage (1%)
(breaches)
Data Payment (42%),
Compromised Personal (41%),
Credentials (33%),
Other (16%) (breaches)
Top IG1 Security Awareness
Protective and Skills Training (14),
Controls Secure Configuration of
Enterprise Assets and
Software (4), Access
Control Management (6)
The first noteworthy item in the At-a-Glance table is the difference in the number of
incidents vs. the number of confirmed data breaches. The main cause of this was a
large number of DoS attacks (409) that were launched against this sector. And while
System Intrusion was the top pattern for breaches (Figure 120), it came in second
place for incidents where no breach could be confirmed (177 incidents in this pattern,
69 of which were confirmed breaches).
Our main point here is: Don’t let the low number of breaches fool you—this sector
remains a target.
The System Intrusion pattern was prevalent, and tells the story of the common
coupling of the Use of stolen creds with dropping Malware to capture application
data. The Social Engineering pattern is a close runner up in this race, with
86
SCIAN 54-44
Patterns
Summary
The Retail industry continues to be a target
for Financially motivated criminals looking
to cash in on the combination of Payment
cards and Personal information this sector is
known for. Social tactics include Pretexting
and Phishing, with the former commonly
resulting in fraudulent money transfers.
Figure 120. Patterns in Retail breaches (n=165)
2021 DBIR Industries

We’ve said it before, and we’ll
say it again—everyone loves
credentials. Credentials are the
glazed donut of data types.
Pretexting—where the adversary
develops an invented scenario to get
their target to take the bait (usually
followed by a money transfer of some
type)—being more common than
we usually see in other industries
(Figure 121). Don’t get us wrong, the
Phishing lure is still effective here. It is Figure 121. Social varieties in Retail
breaches (n=32)
difficult to determine if the targeting of
employees via Pretexting is a sign that
criminals are having to work harder
Figure 122. Top Data varieties in Retail
for the money, or if it is just simpler for
breaches (n=153)
the attackers to dupe employees into
committing fraud on their behalf.
Unsurprisingly, the top data types
compromised include Payment card
data (which is largely what makes this
industry so very attractive to Financially
motivated criminals), Personal data
(also useful for various kinds of financial
fraud) and Credentials (Figure 122).
We’ve said it before, and we’ll say it
again—everyone loves credentials.
Credentials are the glazed donut of
data types.
2021 DBIR Industries 87

05
SMB

Diving back into
SMB breaches
One size fits
Small (Less than 1,000
employees) all-most
Frequency 1,037 incidents, 263 The first thing we noticed while
with confirmed data analyzing the data by organizational
disclosure size this year was that the gap between
the two with regard to the number
Top Patterns System Intrusion,
of breaches, has become much
Miscellaneous
less pronounced. Last year, small
Errors and Basic Web
organizations accounted for less than
Application Attacks
half the number of breaches that large
represent 80% of
organizations showed. Unlike most
breaches
political parties, this year these two
are less far apart with 307 breaches
Threat Actors External (57%), Internal
in large and 263 breaches in small
(44%), Multiple (1%),
organizations.
Partner (0%) (breaches)
Actor Motives Financial (93%), Another interesting finding was that
Espionage (3%), Fun the top patterns have aligned across
(2%), Grudge (1%), both org sizes. For the first time since
Other (1%) (breaches) we began to look at this from an
organizational size perspective, the two
Data Credentials (44%), groups are very similar to each other
Compromised Personal (39%), Other and, at least pattern-wise, this seems
(34%), Medical (17%) like a “one size fits all” situation.
(breaches)
Last year, small organizations were
greatly troubled by Web Applications,
Everything Else and Miscellaneous
Figure 123. Discovery timeline in Small and
Errors. The changes in our patterns Medium Business breaches (n=83)
account for a good bit of what we
see this year in small organizations,
since the Everything Else pattern
was recalibrated, and the attacks
that remain are largely Hacking and
Malware, thus fitting into the System
Intrusion pattern. In contrast, large
organizations saw a fair amount of
actual change. The top three last year
were Everything Else, Crimeware
and Privilege Misuse. The pattern
recalibration means that most of the
Crimeware type events went into
System Intrusion and Basic Web
Application Attacks, but Privilege
Misuse is not a pattern that saw
any substantial degree of change.
Therefore, this is an indication that we
saw fewer Internal actors doing naughty
things with their employer’s data.
2021 DBIR SMB 89

Since the patterns have now largely
Large (More than 1,000 aligned between the two organizational
employees) sizes, we can talk a little about what
that means for both. First, both are
being targeted by financially motivated
Frequency 819 incidents, 307 with
organized crime actors. This isn’t a
confirmed data
news flash to anyone (or shouldn’t be)
disclosure
because professional criminals do
tend to be motivated by money. For
Top Patterns System Intrusion,
that matter, we’d wager most amateur
Miscellaneous Errors
criminals are as well (if we were the
and Basic Web
wagering type, which, of course, we
Application Attacks
aren’t. As far as you know).
represent 74% of
breaches
Concerning the common patterns
of System Intrusion and Basic Web
Threat Actors External (64%), Internal
Application Attacks, those run
(36%), Partner (1%),
the gamut of simple to complex
Multiple (1%) (breaches)
attacks, frequently focused on web
Actor Motives Financial (87%), Fun infrastructure. The Hacking action
(7%), Espionage (5%), of Use of stolen creds followed by
Convenience (2%), Malware installation is the playbook
Grudge (2%), these actors prefer to follow.
Secondary (1%) Increasingly, we see ransomware
(breaches) deployed by the actor after access;
sometimes after they have taken a copy
Data Credentials (42%), of the data to incentivize their victims
Compromised Personal (38%), Other to part with their hard-earned Bitcoin.
(34%), Internal (17%)
(breaches) When we turn to Discovery timelines,
we see a difference between the
Figure 124. Discovery timeline in Large
organizational sizes (Figures 123 Business breaches (n=92)
and 124 respectively). Last year we
reported that smaller organizations
seemed to be doing better in terms of
discovering breaches more quickly than
their larger counterparts.
This year’s data shows that large
organizations have made a shift to
finding breaches within “Days or less”
in over half of the cases (55%), while
small organizations fared less
positively at 47%.
2021 DBIR SMB 90

06
Regions

Introduction
to Regions
Last year we analyzed incidents and presented them from a macro-region
perspective for the first time. This year we once again visit (where possible) the
various regions of the world in an attempt to provide readers with a more global
view of cybercrime. As one might expect, we have greater or lesser visibility into
a given region based on several factors such as contributor presence, regional
disclosure regulations, our own caseload and so on.
Do you live and work in an area of the world that is not mentioned below? Do you
feel that more focus should be given to your sphere of operations? Then contact us
about becoming a data contributor and/or encourage other organizations in your
area and industry to share their data so that we can continue to expand and refine
our coverage each year. It is important to keep in mind that if you do not see your
region represented here, it does not necessarily mean that we have no visibility at all
into the region, but simply that we do not have enough incidents in that geographic
location to be statistically relevant.74
We define the regions of the world in accordance with the United Nations M49
standards, which combine the super-region and sub-region of a country together.
By so doing, the regions we will examine are as follows:
APAC: Asia and the Pacific, including Southern Asia (034), South-eastern Asia
(143), Central Asia (143), Eastern Asia (030) and, last but certainly not least,
Oceania (009).
EMEA: Europe, Middle East and Africa, including North Africa (002), Europe and
Northern Asia (150) and Western Asia (145).
NA: Northern America (021), which primarily consists of breaches in the U.S.
and Canada.
74 Don’t blame the messenger. We don’t make the rules here (they are made by the Illuminati and Intergalactic Aliens, or something like that).
2021 DBIR Regions 92

Asia Pacific
(APAC)
Summary
The most common type of breaches that
took place in APAC were caused by
Financially motivated attackers Phishing
Regions with records
employees for creds, and then using those
Regions without records
stolen creds to gain access to mail accounts
and web application servers.
Frequency 5,255 incidents, 1,495
with confirmed data
disclosure
Top Patterns Social Engineering,
Basic Web Application
Attacks and
Miscellaneous Errors
represent 98% of
breaches
Threat Actors External (95%), Internal
(6%) (breaches)
The APAC region covers an immense
Actor Motives Financial (96%),
Espionage (3%), Fun portion of the globe, and includes a
(1%) (breaches) multitude of nations, languages and
diverse cultures, along with a fair share
Data Credentials (96%), of venomous reptiles. In keeping with
Compromised Personal (3%), Other that diversity, the APAC region shows
(2%), Secrets (1%) a relatively wide range of industries
(breaches) that were breached over the last year.
All of the main verticals you might
expect to see are present to some
degree. Finance, Healthcare, Retail,
Manufacturing and Education all make
an appearance. In fact, for the first time
ever we saw more breaches in APAC
last year than in any other region.
One industry in particular that posted
impressive numbers this year was
NAICS 21: Mining, Quarrying, and Oil
and Gas Extraction (Figure 125). This
was due to the fact that organizations
in that vertical fell prey to sophisticated
Social Engineering attacks.
Figure 125. Top industries in APAC
breaches (n=1,130)
2021 DBIR Regions 93

As Figure 126 illustrates, 70% of committed by Financially motivated
attacks in APAC contained a Social organized criminals. While we have
Engineering action, typically Phishing. only anecdotal data on this topic, we
What those attacks harvested were feel certain that hoodies and dark
almost exclusively Credentials (98%). rooms were involved to some degree.
Those creds were then either used to But regarding the last and most
escalate or laterally expand the Social interesting of those questions (where
attack or were otherwise utilized to is ransomware?), it holds the number
hack into web applications operated by 10 spot in Malware variety for APAC,
the organization (23%). which is in relatively stark contrast to
what we see elsewhere. However, this
If you have perused the other sections is almost certainly a byproduct of our
of this report, you might be asking contributors and their caseload rather
yourself certain questions at this point. than an actual dearth of this type of
Who perpetrated these crimes? Were malware. We expect the “stand-and-
they in a dark room wearing a hoodie? deliver, your money or your data”
Why am I not seeing ransomware in attacks are flourishing in APAC as they
this region? All good questions, and most certainly are in other regions.
as far as we can tell, they were mostly
Figure 126. Patterns in APAC breaches
(n=1,495)
2021 DBIR Regions 94

Europe, Middle East
and Africa (EMEA)
Summary
EMEA continues to be beset by Basic Web
Application Attacks, System Intrusion and
Social Engineering.
Frequency 5,379 incidents, 293
with confirmed data
disclosure
Top Patterns Basic Web Application
Attacks, System
Intrusion and Social
Regions with records
Engineering patterns
Regions without records
represent 83% of
breaches
Threat Actors External (83%), Internal
(18%) (breaches)
Actor Motives Financial (89%),
Espionage (8%), Fun
(1%), Grudge (1%)
(breaches)
EMEA is made up of Europe, the data type in EMEA is Credentials, and
Data Credentials (70%),
Compromised Internal (52%), Personal Middle East and Africa. For the second this goes some way toward explaining
year in a row, Basic Web Application the placement of the patterns. While
(22%), Other (16%)
Attacks are the most commonly seen in many cases we know that stolen
(breaches)
pattern in this region, accounting for Credentials were used, we do not
approximately 54% of breaches. always have visibility into how they were
initially acquired. However, we do know
Sometimes these attacks are aimed at that Social Engineering in the form
obtaining the data within the application of Phishing is very often the means
For the second year in a row, itself, but in other cases it is simply a attackers use to obtain them.
means to an end in order to perpetrate
Basic Web Application Attacks
other forms of badness. Regardless of how they originally got
are the most commonly seen
their grubby little hands on them, using
pattern in this region, The System Intrusion, Social stolen Credentials is the primary means
accounting for approximately Engineering and Miscellaneous Errors by which the actor hacks into the
54% of breaches. patterns are all closely grouped for organization, and in many cases,
second place in this region (Figure it is via a Web application.
127). By far the most often breached
2021 DBIR Regions 95

Finally, 17% of actors in EMEA
are Internal (most often system
administrators), which explains the
presence of Miscellaneous Errors in
the top four patterns. In the majority of
cases (67%), these are unintentional
Misconfiguration errors.
FPO
TWO COLUMN GRAPH
Figure 127. Patterns in EMEA breaches (n=293)
2021 DBIR Regions 96

Northern America
(NA)
Summary
Northern American organizations continue
to be the target of Financially motivated
actors searching for money or easily
monetizable data. Social Engineering,
Hacking and Malware continue to be the
favored tools utilized by these actors.
Frequency 13,256 incidents, 1,080
with confirmed data
Regions with records
disclosure
Top Patterns Social Engineering,
System Intrusion and
Basic Web Application
Attacks represent 92%
of breaches
Threat Actors External (82%), Internal
(19%), Multiple (2%),
Partner (1%) (breaches)
Actor Motives Financial (96%),
Espionage (3%),
Grudge (2%), Fun (1%) When viewing data regarding incidents There seem to be two very distinct
(breaches) and breaches in Northern America, it competitions with regard to Northern
is important to realize the influence America’s data (Figure 128). The first
Data Credentials (58%), of the regulatory environment on the of these is a tight race between Social
Compromised Personal (34%), Other numbers shown. Engineering and System Intrusion
(27%), Internal (11%) (approximately 35% each). The
(breaches) Data breach disclosure laws in this second struggle is between Basic Web
region are prevalent and far reaching Application Attacks and Miscellaneous
with the result that our visibility into Errors for a smaller piece of the action.
cybercrime is better than in areas The confidence intervals overlap to
where such laws are not in place. such a degree between those groups
Healthcare and Public Administration that it is very difficult to call a clear
are among the more strongly winner. Therefore, when looking at the
regulated industries; therefore, we statistics from these patterns, keep in
see a corresponding prevalence mind what we are really seeing are two
in these industries. In addition to sets of partners dancing together.
the aforementioned laws, one must
keep in mind that we also have more
contributors in this geographical
area than in others.
2021 DBIR Regions 97

Our brand-new Social Engineering
pattern is largely comprised of
Pretexting and Phishing actions (Figure
129). Usually, we see more of the simple
type of phishing activities than we do
people going to the trouble of inventing
a scenario. As a rule, criminals tend
to be efficient in their efforts and the
basics usually bring success, so why
put in more work than necessary? One
possible answer is that the end goal
of the Pretexter is not the same as
that of the standard Phisher. Pretext
attacks are frequently an attempt to
get a direct route to the money: The
most common goal is to influence the Figure 129. Social varieties in Northern
American breaches (n=385)
target to send them money (under
false pretenses, of course). These
invented scenarios vary somewhat, but
examples include the substitution of
banking information, or the payment All of these Social and Malware actions
of fictitious invoices. A phisher, in share one characteristic—they cause
contrast, may be going for data rather Integrity violations in the CIA triad.
than cash, and their aim may ultimately For the Social attacks, Alter behavior
be either to monetize the data stolen shows up to account for the change in
in the phish (Credentials), or to gain the behavior of the victim affected by
a foothold into the organization. The the Social action. For the Pretexting
System Intrusion pattern (also newly attacks that were successful, you
minted) most often tells the story of a can see the Fraudulent transaction
Hacking action paired with a Malware Integrity attribute when the criminal
action. We typically see the Use of managed to get someone to send
stolen creds to gain access, followed them cash. Malware, of course, results
by the actor dropping Malware to in Software installation as a violation,
further their aims in the organization. In and Misrepresentation is another side
Figure 128. Patterns in Northern American Northern America, this most commonly effect of Phred the Phisherman and
breaches (n=1,080) means the deployment of Ransomware. Patti the Pretexter, both pretending
As mentioned in last year’s report, to be someone they aren’t (like most
we saw Ransomware groups begin everyone else), and attempting to gain
pivoting to take a copy of the data for more victims in the organization (more
use as leverage against their victims followers, if you will).
prior to triggering the encryption. This
began with the Maze Group, and as
they enjoyed success, other groups
jumped onto the bandwagon. Now it
has become commonplace, with many
of the Ransomware groups having
developed infrastructure specifically
to host these data dumps.
2021 DBIR Regions 98

Given the prevalence of the Phishing Looking at our Discovery timeline, you We would expect to see that happen
attacks, this is where the Credentials can see a significant percentage are soon after the encryption is triggered.
frequently come into play (Figure 130). discovered in Days or less (Figures 131 While we would rather see internal
Personal data is a prime target as well, and 132 respectively). However, over detective controls be responsible for
since that includes such data elements half of these cases were discovered finding the majority of the breaches, at
as Social Security/Insurance numbers by the threat actor disclosing the least when that ransom note appears,
paired with other bits of information breach—this is typically the way organizations can start to contain
that allow criminals to commit further Ransomware is discovered, when the the breach and get the actors out of
financial fraud. ransom note flashes up on the screen. their network.
Figure 130. Top Data varieties in Northern Figure 131. Discovery timeline in Northern Figure 132. Discovery timeline in breaches
America breaches (n=579) America breaches (n=128) (n=195)
2021 DBIR Regions 99

07
Wrap-up

Here we are at last, at the
conclusion of the 14th installment
of the Verizon Data Breach
Investigations Report.
Give yourselves, and each Of course, we can’t close out a
other, a pat on the back, or even report without thanking our
better, a big virtual hug.75 All will contributors who freely give
be well. Thank you, readers, for their time, their expertise and,
spending time here with us yet most importantly, their data to
again. We hope that the make this report a reality each
information contained in these year. On behalf of the DBIR
pages has been of assistance Team, we thank you all. We
to you and that you found it encourage you, our readers, to
both informative and easy to reach out to us with your
ingest. As we mentioned at questions, comments and
different points in this year’s thoughts, or just to say hi. Here
report, it is not always easy to is hoping that we will find you
see what is coming at us all with us next year for number
around the next bend. But one 15. Stay safe, and be happy!
thing we do know is that if we
meet whatever it may be with
reason, with compassion and
caring,76 most importantly, with
each other, we can handle it.
75 Or a real one if you have really long arms.
76 As Dan Kaminsky would do.
2021 DBIR Wrap-up 101

Year in review
Year in review
77
January The Verizon Threat Research Advisory Center intelligence collections in both 2019 and 2020 began with
cyber espionage targeting cloud environments by the Chinese menuPass threat actor. Among the ongoing
threats were attacks on remote access. These included attacks on new vulnerabilities in Citrix products
and continued password spraying attacks on Pulse Secure, FortiOS and Palo Alto VPN servers. London-
based financial services company Travelex suffered a Sodinokibi ransomware infection on New Year’s Eve
that some sources claimed was the result of failing to patch a Pulse Secure VPN server. The U.S. Coast
Guard announced a port facility had to shut down for 30 hours due to a Ryuk infection. The first zero-day
attacks in 2020 exploited CVE-2020-0674 Internet Explorer use-after-free vulnerability in JScript. Qihoo
360 reported a watering hole attack by the DarkHotel actor using a cocktail of exploits: CVE-2020-0674
(Internet Explorer JScript) and CVE-2019-17026 (Firefox) and CVE-2017-11882 (Office Equation editor).
February The Australian Cyber Security Centre issued an advisory on ransomware known as “Mailto” or
“Netwalker” after the Australian transportation and logistics company The Toll Group suffered an attack.
On patch Tuesday, Microsoft released 99 patches including one for CVE-2020-0674. Another patch
was for a vulnerability in Microsoft Exchange, CVE-2020-0688. Within two weeks, the VTRAC collected
intelligence about mass scanning and exploitation targeting the Exchange Server vulnerability. The
Cybersecurity and Infrastructure Security Agency (CISA) issued an alert with intelligence about a Ryuk
ransomware attack on a natural gas pipeline facility. Industrial Control Systems (ICS) security company
Dragos released an assessment with links to January’s U.S. Coast Guard report. Five days after releasing
a new version of their Chrome browser, Google released another to mitigate a type confusion vulnerability,
CVE-2020-6418, that was being exploited in the wild (ITW).
March Fans of Westerns (movie genre) will recognize “ringing the chuck wagon triangle bell” at dinnertime.
COVID-19 began to have the same effect for cybercriminals. Perhaps the most immediately useful
collection was RiskIQ’s COVID-19 Daily Update reports and domain watch or block lists. Prevailion and
Proofpoint produced intelligence on TA505 attacks using COVID-19 bait. Before the end of the month,
Microsoft was warning customers about limited targeted attacks exploiting a new Windows 7 vulnerability.
Windows 10 was not vulnerable. CVE-2020-1020 was a security flaw in the Adobe Type Manager Library.
FIN7 targeted a Trustwave customer with a malicious USB drive in conjunction with a US$50 gift card bait.
April BAH published a re-assessment of 200-plus cyber operations by the GRU (Russian military intelligence)
concluding they conform to Russian strategic doctrine, which makes them somewhat more predictable.
Recorded Future leveraged MITRE’s ATT&CK for a report exploring the most common cyber-attacker
TTP in 2019. Malwarebytes published “APTs and COVID-19: How advanced persistent threats use the
coronavirus as a lure.” Two other resources for cybersecurity during the COVID-19 pandemic were BBC
cybersecurity correspondent Joe Tidy’s searchable Coronavirus Phishing Scams collection, and the
National Cyber Security Alliance’s COVID-19 Security Resource Library. Three of the 113 vulnerabilities
patched by Microsoft were being exploited ITW. Patches for CVE-2020-1020 and CVE-2020-0938
mitigated the “limited targeted Windows 7 based attacks that could leverage un-patched vulnerabilities
in the Adobe Type Manager Library.” The third surprise attack exploited a Windows kernel elevation of
privilege vulnerability, CVE-2020-1027. But before the end of April, Microsoft released an out-of-cycle
advisory for a vulnerable Autodesk DLL, CVE-2020-7085.
77 Thanks to David M. Kennedy from the VTRAC for this contribution.
2021 DBIR Year in review 102

May Oracle reported ITW exploitation attempts on WebLogic servers without the patch for CVE-2020-2883
that was in the April Critical Patch Update. F-Secure announced two severe vulnerabilities in SaltStack
Salt management framework, a configuration management and administration tool frequently used in
data centers and cloud environments including Amazon Web Services and GCP. CISA published “Top 10
Routinely Exploited Vulnerabilities.” New intelligence from ESET detailed Winnti attacks on video game
companies in South Korea and Taiwan. Taiwan’s Ministry of Justice believes Winnti was responsible for
ransomware attacks on both of the countries’ oil refineries. Broadcom/Symantec intelligence covered
attacks on telecommunications companies in South Asia by the Greenbug threat actor. Cisco disclosed
that six of its backend servers were compromised by hackers who exploited SaltStack vulnerabilities
CVE-2020-11651 and CVE-2020-11652. The Australia logistics giant Toll Group was hit by a second
ransomware attack in three months. Trustwave disseminated a report on “GoldenSpy,” a backdoor in the
tax payment software mandated by the Chinese bank of a UK-based technology company.
June Cycldek, a low-profile Chinese threat actor deployed “USBCulprit” malware that Kaspersky assessed is
intended to spread to and exfiltrate data from systems isolated from the internet. None of the 150-plus
vulnerabilities patched in June were being exploited prior to patch release. Australian Prime Minister
Morrison said Australian organizations, including governments and businesses, are currently being
targeted by a sophisticated foreign “state-based” actor. The “Evil Corp’’ APT-grade cybercrime threat
actor began “big game hunting” with relatively new WastedLocker ransomware. NCC Group and Symantec
independently released intelligence on the new Evil Corp campaign.
July Enterprises with F5 BIG-IP appliances were at risk from attacks on two new vulnerabilities that U.S. Cyber
Command called to be “remediated immediately.” Exploit code was ITW. BIG-IP honeypots had been
attacked and malware installed. FortiGuard, Palo Alto and Deep Instinct each reported intelligence about
EKANS (SNAKE) ransomware that sidelined systems at Honda and Enel. Citrix released a security bulletin
and patches for 11 new vulnerabilities in Citrix ADC, Gateway and SD-WAN. Within three days, the VTRAC
collected reports of Citrix exploit detections by honeypots followed by de rigueur attempts to install
cryptocurrency mining software. The U.K., U.S. and Canada jointly reported APT29 (Cozy Bear) (Russia)
has been targeting COVID-19 vaccine research organizations. Sansec reported the Lazarus Group had
been attacking U.S. and E.U. e-tailers using Magecart payment card skimming. McAfee and SentinelOne
each reported different campaigns by Lazarus.
August We collected security advisories about Cisco firewalls and TeamViewer, the management tool used by
many managed service providers and their clients. We collected intelligence on campaigns spreading
new variants of banking Trojans: IcedID, Dridex and Emotet. MITRE published, “2020 CWE Top 25 Most
Dangerous Software Weaknesses.” Three U.S. agencies released joint reports on a newly distinguished
North Korean threat actor, “BeagleBoyz,” and malware that the actor uses for ATM “jackpotting” attacks.
F-Secure reported North Korean actors targeting virtual currency organizations.
2021 DBIR Year in review 103

September Group-IB reported “UltraRank” an actor behind Magecart payment card skimming campaigns since 2015.
SWIFT and BAE Systems released a report on the cybercrime economy fittingly titled, “Follow the Money.”
CISA released two products covering Iranian threat activity. Several vulnerabilities used by Iranian actors
are also favored by ransomware actors according to SenseCy. Intel 471 assessed Lazarus has been using
Russian crimeware for initial access to their targets. Microsoft Security reported ITW attacks exploiting
systems without patches for the so-called “ZeroLogon” vulnerability, CVE-2020-1472.
October The Australian Cyber Security Centre (ACSC) issued an advisory on an “ongoing and widespread” Emotet
campaign impacting Australian organizations. The VTRAC continued to collect threat intelligence about
exploitation of Netlogon/ZeroLogon (CVE-2020-1472). CISA and Microsoft have observed Netlogon/
ZeroLogon exploitation by APT-grade actors like MuddyWater and TA505. The MuddyWater Iranian
APT actor has been targeting Israeli organizations according to ClearSky Security. Telsy attributed
MuddyWater was behind another campaign targeting professionals in the aerospace and avionics sectors
in Italy. Google said it mitigated a 2.54 Tbps DDoS attack, one of the largest ever recorded. The U.S.
barbeque restaurant chain Dickey’s suffered a point-of-sale attack between July 2019 and August 2020.
November The VTRAC collected risk-relevant intelligence about eight new vulnerabilities, three of which have
already been exploited and the remainder having exploit code ITW without reports of successful attacks.
November’s Patch Tuesday came with 114 Microsoft patches, two Adobe product updates, 12 SAP
security notes (six Hot News), four Chrome browser updates and 40 Intel security advisories. Exploit
code was already ITW for one Microsoft and five Chrome browser vulnerabilities. Bitdefender released a
report of Chinese APT attacking South East Asian governments. Attacks by Lazarus and Kimsuky were
reported by ESET and EAST Security respectively. Egregor ransomware has been establishing itself as
the successor to Maze ransomware. The Australian Cyber Security Centre alerted the healthcare sector
about TA505 attacks using SDBBot remote access Trojan and Clop ransomware.
December Malwarebytes and CERT-Bund warned about a campaign that had been targeting users in Germany with
Gootkit banking Trojans and REvil (Sodinokibi) ransomware. The milestone attack abusing the SolarWinds
Orion update process will probably eclipse WannaCry as the most costly cyberattack. The 18,000
SolarWinds customers exposed to the first stage Sunburst malware will be threat hunting to determine if
they were among the priority targets for the attackers. Microsoft identified more than 40 customers that
were “targeted more precisely and compromised through additional and sophisticated measures.” There
were probably at least two different threat actors inside SolarWinds’ network. One was the APT-grade
actor discovered by FireEye. Another less-sophisticated actor was spreading SUPERNOVA backdoors.
The APT actor prioritized a much smaller set of customers for reinforcing attacks using Teardrop dropper
Trojans to deliver a Cobalt Strike Beacon. These priority victims probably number in the low hundreds and
are being identified by unravelling Sunburst’s network use for Command and Control and
malware distribution.
2021 DBIR Year in review 104

08
Appendices
Appendices

Appendix A:
Methodology
One of the things readers value However, proving causality is best The collection method and conversion
most about this report is the left to the controlled experiments of techniques differed between
day science. The best we can do is contributors. In general, three basic
level of rigor and integrity we
correlation. And while correlation is methods (expounded below) were
employ when collecting,
not causation, they are often related to used to accomplish this:
analyzing and presenting data. some extent, and often useful.
1 Direct recording of paid external
Knowing our readership cares about
forensic investigations and related
such things and consumes this
intelligence operations conducted by
information with a keen eye helps keep
Non-committal disclaimer
Verizon using the VERIS Webapp
us honest. Detailing our methods is an
important part of that honesty. We would like to reiterate that we make
2 Direct recording by partners
no claim that the findings of this report
First, we make mistakes. A column are representative of all data breaches using VERIS
transposed here; a number not updated in all organizations at all times. Even
there. We’re likely to discover a few though the combined records from all 3 Converting partners’ existing schema
things to fix. When we do, we’ll list our contributors more closely reflect into VERIS
them on our corrections page: https:// reality than any of them in isolation,
www.verizon.com/business/resources/ it is still a sample. And although we All contributors received instruction to
reports/dbir/2021/corrections/ believe many of the findings presented omit any information that might identify
in this report to be appropriate for organizations or individuals involved.
Second, we check our work. The same
generalization (and our confidence
way the data behind the DBIR figures in this grows as we gather more data Some source spreadsheets are
can be found in our GitHub repository,78 and compare it to that of others), bias converted to our standard spreadsheet
as with last year, we’re also publishing undoubtedly exists. formatted through automated mapping
our fact check report there as well. to ensure consistent conversion.
It’s highly technical, but for those Reviewed spreadsheets and VERIS
interested, we’ve attempted to test Webapp JavaScript Object Notation
every fact in the report.79 The DBIR process (JSON) are ingested by an automated
workflow that converts the incidents
Third, François Jacob described “day Our overall process remains intact and breaches within into the VERIS
science” and “night science.”80 Day and largely unchanged from previous JSON format as necessary, adds
science is hypothesis driven while years. All incidents included in this missing enumerations, and then
night science is creative exploration. report were reviewed and converted (if validates the record against business
The DBIR is squarely night science. necessary) into the VERIS framework logic and the VERIS schema. The
As Yanai et al. demonstrate, focusing to create a common, anonymous automated workflow subsets the data
too much on day science can cause aggregate data set. If you are unfamiliar and analyzes the results. Based on the
you to miss the gorilla in the data.81 with the VERIS framework, it is short results of this exploratory analysis, the
While we may not be perfect, we for Vocabulary for Event Recording validation logs from the workflow, and
believe we provide the best obtainable and Incident Sharing, it is free to use, discussions with the partners providing
version of the truth82 (to a given level of and links to VERIS resources are at the the data, the data is cleaned and re-
confidence and under the influence of beginning of this report. analyzed. This process runs nightly for
biases acknowledged below). roughly two months as data is collected
and analyzed.
78 https://github.com/vz-risk/dbir/tree/gh-pages
79 Interested in how we test them? Check out Chapter 9, Hypothesis Testing, of ModernDive: https://moderndive.com/9-hypothesis-testing.html
80 Jacob F. The Statue Within: An Autobiography. CSHL Press; 1995. By way of Selective attention in hypothesis-driven data analysis, Itai Yanai, Martin Lercher, bioRxiv
2020.07.30.228916;
81 Really. They made printing the data print a gorilla and people trying to test hypotheses completely missed it
82 Eric Black, “Carl Bernstein Makes the Case for ‘the Best Obtainable Version of the Truth,’” by way of Alberto Cairo, “How Charts Lie”
(a good book you should probably read regardless).
2021 DBIR Appendix A 106

This year we again made use of
1 The incident must have at least
Incident data confidence intervals to allow us to
seven enumerations (e.g., threat
analyze smaller sample sizes. We
Our data is non-exclusively multinomial, actor variety, threat action category,
adopted a few rules to help minimize
meaning a single feature, such as variety of integrity loss, etc.) across
bias in reading such data. Here we
“Action,” can have multiple values (i.e., 34 fields OR be a DDoS attack.
define “small sample” as less than 30
“Social,” “Malware” and “Hacking”). This Exceptions are given to confirmed
samples.
means that percentages do data breaches with less than seven
not necessarily add up to 100%. enumerations.
1 Sample sizes smaller than five are
For example, if there are five botnet
too small to analyze.
breaches, the sample size is five. 2 The incident must have at least one
However, since each botnet used known VERIS threat action category
phishing, installed keyloggers, and used 2 We won’t discuss count or (Hacking, Malware, etc.)
percentage for small samples.
stolen credentials, there would be five
This applies to figures, too, and is
Social actions, five Hacking actions, In addition to having the level of details
why some figures lack the dot for
and five Malware actions, adding up to necessary to pass the quality filter, the
the point estimate.
300%. This is normal, expected and incident must be within the timeframe
handled correctly in our analysis of analysis, (November 1, 2019, to
3 For small samples we may talk about
and tooling. October 31, 2020, for this report). The
the value being in some range, or
2020 caseload is the primary analytical
Another important point is that when values being greater/less than each
focus of the report, but the entire
looking at the findings, “Unknown” is other. These all follow the confidence
range of data is referenced throughout,
equivalent to “Unmeasured.” Which is interval approaches listed above.
notably in trending graphs. We also
to say that if a record (or collection of
exclude incidents and breaches
records) contains elements that have
affecting individuals that cannot be
been marked as “Unknown” (whether it
tied to an organizational attribute loss.
is something as basic as the number of Incident eligibility
If your friend’s laptop was hit with
records involved in the incident, or as
Trickbot it would not be included in
For a potential entry to be eligible
complex as what specific capabilities a
this report.
for the incident/breach corpus, a
piece of malware contained), it means
couple of requirements must be
that we cannot make statements about Lastly, for something to be eligible for
met. The entry must be a confirmed
that particular element as it stands inclusion in the DBIR, we have to know
security incident defined as a loss of
in the record—we cannot measure about it, which brings us to several
confidentiality, integrity or availability.
where we have too little information. potential biases we will discuss on the
In addition to meeting the baseline
Because they are “unmeasured,” next page.
definition of “security incident” the
they are not counted in sample sizes.
entry is assessed for quality. We
The enumeration “Other,” however, is
create a subset of incidents (more on
counted, as it means the value was
subsets later) that pass our quality
known but not part of VERIS. Finally,
filter. The details of what is a “quality”
“Not Applicable” (normally “NA”) may
incident are:
be counted or not counted depending
on the claim being analyzed.
2021 DBIR Appendix A 107

Breaches Breaches
Acknowledgement and
analysis of bias
Many breaches go unreported (though
our sample does contain many of
those). Many more are as yet unknown
by the victim (and thereby unknown to
us). Therefore, until we (or someone)
can conduct an exhaustive census of
every breach that happens in the entire
world each year (our study population),
we must use sampling.83 Unfortunately,
this process introduces bias.
The first type of bias is random
bias introduced by sampling. This
Figure 133. Individual contributions Figure 134. Individual contributions
year, our maximum confidence is
per action per actor
+/- 0.6%84 for incidents and +/- 1.5%
for breaches, which is related to our
sample size. Any subset with a smaller
Breaches Breaches
sample size is going to have a wider
confidence margin. We’ve expressed
this confidence in the conditional
probability bar charts (the “slanted” bar
charts) we have been using since the
2019 report.
The second source of bias is sampling
bias. Still, it is clear that we conduct
biased sampling. For instance, some
breaches, such as those publicly
disclosed, are more likely to enter our
corpus, while others, such as classified
breaches, are less likely.
Figures 133, 134, 135 and 136 are an
Figure 135. Individual contributions Figure 136. Individual contributions attempt to visualize potential sampling
per asset per attribute
bias. Each radial axis is a VERIS
enumeration, and we have ribbon charts
representing our data contributors.
Ideally, we want the distribution of
sources to be roughly equal on the
stacked bar charts along all axes. Axes
only represented by a single source
are more likely to be biased. However,
contributions are inherently thick tailed,
with a few contributors providing a lot
83 Interested in sampling? Check out Chapter 7, Sampling, of ModernDive: https://moderndive.com/7-sampling.html
84 This and all confidence intervals are 95% confidence intervals determined through bootstrap simulation or Markov Chain Monte Carlo.
Read more in Chapter 8, Bootstrapping and Confidence Intervals, of ModernDive: https://moderndive.com/8-confidence-intervals.html
2021 DBIR Appendix A 108

of data and many contributors providing
a few records within a certain area. Data subsets Non-incident data
Still, we mostly see that most axes have
We already mentioned the subset Since the 2015 issue, the DBIR includes
multiple large contributors with small
of incidents that passed our quality data that requires the analysis that
contributors adding appreciably to the
requirements, but as part of our did not fit into our usual categories of
total incidents along that axis.
analysis there are other instances “incident” or “breach.” Examples of
where we define subsets of data. These non-incident data include malware,
You’ll notice rather large contributions
subsets consist of legitimate incidents patching, phishing, DDoS, and other
on many of the axes. While we’d
that would eclipse smaller trends if left types of data. The sample sizes for
generally be concerned about this, they
in. These are removed and analyzed non-incident data tend to be much
represent contributions aggregating
separately (as called out in the relevant larger than the incident data, but from
several other sources, so not actual
sections). This year we have two fewer sources. We make every effort
single contributions. It also occurs
subsets of legitimate incidents that to normalize the data (for example
along most axes, limiting the bias
are not analyzed as part of the weighting records by the number
introduced by that grouping of indirect
overall corpus: contributed from the organization
contributors.
so all organizations are represented
The third source of bias is confirmation 1 We separately analyzed a subset of equally). We also attempt to combine
bias. Because we use our entire dataset web servers that were identified as multiple contributors with similar data
for exploratory analysis (night science), secondary targets (such as taking to conduct the analysis wherever
we do not test specific hypotheses over a website to spread malware). possible. Once analysis is complete,
(day science). Until we develop a good we try to discuss our findings with the
collection method for data breaches or 2 We separately analyzed botnet- relevant contributor or contributors so
incidents from Earth-616 or any of the related incidents. as to validate it against their knowledge
other Earths in the multiverse, this is of the data.
Finally, we create some subsets to
probably the best that can be done.
help further our analysis. In particular,
As stated, we attempt to mitigate these a single subset is used for all analysis
biases by collecting data from diverse within the DBIR unless otherwise
contributors. We follow a consistent stated. It includes only quality incidents
multiple-review process and when we as described above and excludes the
hear hooves, we think horse, not zebra. aforementioned two subsets.
2021 DBIR Appendix A 109

Appendix B:
Controls
Hopefully you didn’t think we had
1 Inventory and Control 11 Data Recovery
of Enterprise Assets forgotten about this important
and helpful section?
12 Network Infrastructure
2 Inventory and Control Management
Never fear, back by popular demand
of Software Assets
from auditors, CISOs and control freaks
13 Network Monitoring and in general, we’re updating our mapping
3 Data Protection Defense with the community-built CIS Controls.85
If you haven’t heard, they have gone
4 Secure Configuration of 14 Security Awareness and through a major update for their eighth
Enterprise Assets and Skills Training iteration, much like our patterns have this
Software year, and have been creatively named
CIS Controls v8. Fortunately, there’s no
15 Service Provider
“should’ve had a V8” of the Controls
5 Account Management Management
mapping to VERIS, because we’ve got
you covered.
6 Access Control 16 Application Software
Management Security The CIS Controls are a community-
built, maintained and supported series
7 Continuous Vulnerability 17 Incident Response of best practices targeted at helping
Management Management organizations prioritize their defenses
based on what attackers are doing—the
so-called “Offense informs Defense”
8 Audit Log Management 18 Penetration Testing
approach to best practices. The DBIR is
but one resource of attacker knowledge
9 Email and Web Browser at the macro level. Nevertheless, we were
Protections fortunate enough to be in a position to
provide feedback and suggest input into
10 Malware Defenses their community process. Whether you
are presenting your NIST Cybersecurity
Framework (CSF) strategic roadmap at
the Board level or defending an individual
funding request for a new security
program initiative, our goal is to allow you
to easily tie our findings and data to your
organization’s efforts. We are thrilled to
witness the evolution of the best practices
due to the hard work of the individuals that
donated their valuable time to help. Here is
an overview of what has changed:
• Incorporating technologies such as
cloud and mobile
• In recognition of “borderless” networks
and tighter coordination between
network/system administrators, the
Controls are organized by activity,
resulting in reducing the number of
Controls from 20 to 18
85 https://www.cisecurity.org/controls/
2021 DBIR Appendix B 110

• Reordering of Controls to show In the report, you have hopefully organizations manage the access to
the importance of Data Protection noticed the addition of the Top accounts and is useful against brute
(formerly 13, now 3) Protective Implementation Group 1 forcing and credential stuffing attacks.
Controls listed for each industry. By
• Addition of a “Service Provider
using the combination of the mappings
Management” Control to address Control 6: Access Control Management
to patterns, implementation groups and
how organizations should manage
security functions of the Controls, we This is Control 5’s little cousin in which
cloud services
identified the core set of Controls that instead of simply looking at the user
One of the more helpful components every organization should consider accounts and managing access to
that the CIS community has decided implementing regardless of size those, you’re managing the rights
to continue from version 7 are the and budget: and privileges and lastly enforcing
multifactor authentication on key
Implementation Groups (IG), which
components of the environment, a
help organizations further prioritize Control 4: Secure Configuration of
useful tactic against Use of stolen
their implementation of Controls based Enterprise Assets and Software
credentials.
on their resources, risk and other
This control is not only a mouthful, but
factors. The notion being that while
it also contains safeguards focused
every organization needs security, the Control 14: Security Awareness
on engineering solutions that are
giant, international leader on ethical and Skills Training
secure from the outset, rather than
pharmaceutical practices Umbrella
tacking them on later. In this Control This control is a classic and hopefully
Corp probably needs a larger and
you will see substantial benefit toward doesn’t need a whole lot of explanation.
different set to protect its research
reducing Error-based breaches like Considering the high prevalence of
facilities in Raccoon City than does the
Misconfiguration and Loss of assets Errors and Social Engineering, it is
local pet hotel. The IGs build on each
through enforcing remote wipe abilities obvious that awareness and technical
other, with Implementation Group 1
on portable devices. training are probably a smart place
being the starting point where a smaller
to put some dollars to help support
subset of the Controls are implemented
your team against a world full of
(approximately 36%), and then building Control 5: Account Management
cognitive hazards.
all the way up to Implementation Group
While this is technically a new Control
3, where all 153 safeguards
in version 8, it should be extremely
are implemented.
familiar as the safeguards are really
just a centralization of the previous
Figure 137 breaks out the mapping into
account management practices that
more granular detail and shows the
were found in a few previous Controls,
relationships between the patterns and
like Boundary Protect and Account
the overlap with the CIS Control for
Monitoring and Control. This control
each Implementation Group.
is very much targeted toward helping
2021 DBIR Appendix B 111

| 0% 25% | 50% 75% | 100% |
| ------ | ------- | ---- |
Figure 137. CIS to pattern mapping
2021 DBIR  Appendix B 112

Appendix C:
U.S. Secret Service
Protecting the Financial
David Smith
Special Agent in Charge Infrastructure Amidst a
Criminal Investigative Division
U.S. Secret Service Global Pandemic
Bernard Wilson
The year 2020 will be remembered as the year of the COVID-19 global pandemic,
Network Intrusion Response with its short and long-term impacts. The pandemic began with lockdowns and
Program Manager a rapid transition to remote work, and continued with economic slowdowns
Criminal Investigative Division and associated relief efforts. The pandemic affected all aspects of life and was
U.S. Secret Service
particularly conducive to cybercrime.
In a matter of weeks, organizations had to transition to remote work, where
possible. The reliance of a vastly expanded remote workforce resulted in a surge in
the number and severity of attacks related to the weaknesses in underlying Internet
and information technology infrastructure. This led to an increase in the number
of incidents associated with the telework portion of the Business Continuity Plan
(BCP) for many organizations. BCPs generally contain provisions for remote access
to services available on an organization’s network, a proliferation in email traffic for
internal communications, and an increased reliance on enterprise video and audio
communications. With this shift came an increase in malware and social engineering
attacks, consistent with the exploitation of general communications.
Organizations that neglected to implement multi-factor authentication, along with
virtual private networks (VPN), represented a significant percentage of victims
targeted during the pandemic. The zero-trust model for access quickly became
a fundamental security requirement rather than a future ideal. Nonrepudiation via
Personal Identity Verification (PIV), Fast Identity Online (FIDO) or similar solutions
became essential in zero-trust architectures. Security postures and principles,
such as proper network segmentation, the prevention of lateral movement, least
privilege, and “never trust, always verify” have proven to be strong indicators of
an organization’s ability to prevent or recover from unauthorized presence in its
network environment.
In 2020, in the midst of the pandemic, cyber actors increased malware attacks
against U.S. victims, including the healthcare and public health sector. The U.S.
Secret Service noted a marked uptick in the number of ransomware attacks,
ranging from small dollar to multi-million dollar ransom demands. While most
organizations had adequate data backup solutions to mitigate these attacks, cyber
actors shifted their focus to the exfiltration of sensitive data. These cyber actors,
often organized criminal groups, proceeded to monetize the theft by threatening to
publicize the data unless additional ransom was paid. The monetization of proceeds
was typically enabled by cryptocurrency, in an attempt to obfuscate the destination
of proceeds and hamper the ability of law enforcement to locate and apprehend
those responsible for the crime.
2021 DBIR Appendix C 113

One of the primary responsibilities of The year 2020 demonstrated, once
Preventing and deterring
the Secret Service is to protect the again, the enduring threat posed by
pandemic relief fraud became financial infrastructure of the United organized cyber-criminal groups.
the focus of the Secret Service States. The pandemic required an Whether the crime involves a hospital
unprecedented response from the ransomware attack, the sale of
and other law enforcement
Federal government. Legislators exfiltrated customer data, ATM cash-
agencies, particularly focused
approved the release of $2.6 trillion out attacks, or the theft of pandemic
on Federal funding allocated to of taxpayer funds to address the relief funds, the common indicator is
states for unemployment economic effects of the pandemic the prevalence of organized crime.
benefit programs. on the nation. The release of federal Criminals can be either formally
funding attracted the attention or informally organized, at times in
of organized criminal groups and partnership with nation-state malicious
individuals attempting to exploit actors, based on a common interest
pandemic relief programs. As a result, in illicit profit. Cyber actors quickly
preventing and deterring pandemic shift their activity based on emerging
relief fraud became the focus of opportunities to steal and launder
the Secret Service and other law funds using any tactics, techniques
enforcement agencies, particularly and procedures available to them.
focused on Federal funding allocated Collaboration between domestic and
to states for unemployment benefit foreign law enforcement partners to
programs. The Secret Service worked combat cybercriminal groups and
with law enforcement partners at the their schemes is key to dismantling
U.S. Department of Labor to prevent organized crime and apprehending
criminal activity and arrest those cyber actors.
responsible for exploiting the programs.
This effort prevented more than $1.5 To address this continued shift
billion from reaching criminals and of criminality, the Secret Service
ensured that hundreds of millions of operates a network of Cyber Fraud
dollars intended to provide support to Task Forces (CFTF), a partnership of
affected communities was returned to federal, state, local, and foreign law
the states and the intended recipients. enforcement agencies, prosecutors,
the private sector, and academia.
Yet in spite of these efforts, criminals Outreach is at the core of the Secret
continued attempting to divert Service CFTFs, as it fosters trusted
pandemic relief funds from different relationships and information sharing,
programs, to include $697.3 billion in which are important tools in mitigating
loans intended to support businesses. cybercrimes. While apprehending
The Secret Service and partner law criminals is, and will continue to be, the
enforcement agencies have expanded ultimate goal of the Secret Service,
our efforts to prevent and mitigate prevention and mitigation are equally
these crimes, and ultimately locate and critical in the protection of the U.S.
arrest those responsible. financial infrastructure.
2021 DBIR Appendix C 114

Appendix D:
Contributing
organizations
| A                                | D               | J         |
| -------------------------------- | --------------- | --------- |
| Akamai Technologies              | Dell            | JPCERT/CC |
| Ankura                           | Digital Shadows |           |
| Apura Cybersecurity Intelligence | Dragos, Inc     | K         |
| Arics Cooper                     |                 | Kaspersky |
| Atos (Paladion)                  | E               | KnowBe4   |
| AttackIQ                         | Edgescan        |           |
L
Elevate Security
|     | Emergence Insurance | Lares Consulting |
| --- | ------------------- | ---------------- |
B
| Bad Packets   | EUROCONTROL       | Legal Services - ISAO  |
| ------------- | ----------------- | ---------------------- |
| BeyondTrust   |                   | LMG Security           |
| Bit Discovery | F                 |                        |
| Bit-x-bit     | Farsight Security | M                      |
BitSight Federal Bureau of Investigation - Internet  Malicious Streams
Crime Complaint Center (FBI IC3)
| BlackBerry Cylance |     | Maritime Transportation System ISAC  |
| ------------------ | --- | ------------------------------------ |
(MTS-ISAC)
F-Secure
Micro Focus
C
|     | G   | Mishcon de Reya |
| --- | --- | --------------- |
Center for Internet Security
|     | Global Resilience Federation | mnemonic |
| --- | ---------------------------- | -------- |
CERT European Union
Government of Telangana, ITE&C Dept.
CERT National Insider Threat Center
|             | Government of Victoria, Australia -     | N   |
| ----------- | --------------------------------------- | --- |
| CERT Polska | Department of Premier and Cabinet (VIC) |     |
National Cybersecurity & Communications
Checkpoint Software Technologies Ltd. Grey Noise Integration Center (NCCIC)
Chubb
NetDiligence®
| Cisco Talos Incident Response  |     | NETSCOUT |
| ------------------------------ | --- | -------- |
H
| Coalition | Hasso-Plattner Institut |     |
| --------- | ----------------------- | --- |
Computer Incident Response Center  Homeland Security Solutions B. V (HLSS) P
Luxembourg (CIRCL)
ParaFlare Pty Ltd
CrowdStrike
|     | I   | Proofpoint |
| --- | --- | ---------- |
Cybersecurity and Infrastructure Security
|     | ICSA Labs | PSafe  |
| --- | --------- | ------ |
Agency (CISA)
Irish Reporting and Information Security
CyberSecurity Malaysia, an agency under
Service (IRISS-CERT)
| the Ministry of Communications and  |     | Q   |
| ----------------------------------- | --- | --- |
Multimedia (KKMM)
Qualys
Cybir (formerly DFDR Forensics)
2021 DBIR  Appendix D 115

R
Rapid7
Recorded Future
S
S21sec
SecurityTrails
Shadowserver Foundation
Shodan
SISAP - Sistemas Aplicativos
Swisscom
T
Tetra Defense
U
U.S. Secret Service
V
VERIS Community Database
Verizon Cyber Risk Programs
Verizon DDoS Shield
Verizon Digital Media Services
Verizon Managed Security Services -
Analytics (MSS-A)
Verizon Network Operations and
Engineering
Verizon Professional Services
Vestige Digital Investigations
VMRay
Verizon Threat Research Advisory Center
(VTRAC)
W
WatchGuard Technologies
Z
Zscaler
2021 DBIR Appendix D 116

2021 DBIR Appendix D 117

2021 DBIR Appendix D 118

<!-- CONVERSION_METADATA: {"source": "https://github.com/jacobdjwilson/awesome-annual-security-reports", "date": "2026-09-17", "model": "gemini-3.5-flash-lite"} -->
