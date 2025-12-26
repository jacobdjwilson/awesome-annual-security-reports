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

## Table of
contents

01

DBIR Master’s Guide

Introduction

Summary of findings

02

Results and Analysis

Actor

Action

Assets

Attribute

Timeline

Impact

2021 DBIR Table of contents

4

6

7

8

12

15

19

22

24

25

03

05

Incident Classification Patterns

29

SMB

Denial of Service

Lost and Stolen Assets

Miscellaneous Errors

Privilege Misuse

Social Engineering

System Intrusion

Basic Web Application Attacks

Everything Else

04

Industries

Introduction to industries

Accommodation and Food Services

Arts, Entertainment and Recreation

Educational Services

Financial and Insurance

Healthcare

Information

Manufacturing

Mining, Quarrying,
and Oil & Gas Extraction + Utilities

Professional, Scientific
and Technical Services

Public Administration

Retail

Diving back into SMB breaches

06

Regions

Introduction to Regions

Asia Pacific (APAC)

Europe, Middle East and Africa (EMEA)

Northern America (NA)

07

Wrap-up

Year in review

08

Appendices

Appendix A: Methodology

Appendix B: Controls

Appendix C: U.S. Secret Service

Appendix D: Contributing organizations

35

41

43

46

49

54

58

62

64

65

69

71

73

75

76

77

79

81

82

84

86

88

89

91

92

93

95

97

100

102

105

106

110

113

115

3

# 01 DBIR Master’s Guide

Hello first-time reader, and
welcome to the 2021 Data
Breach Investigations Report
(DBIR). We have been creating
this report for a while now,
and we appreciate that all the
verbiage we use can be a bit
obtuse at times. We use very
deliberate naming conventions,
terms and definitions and
spend a lot of time making
sure that we are consistent
throughout the report.
Hopefully this section will
help make all of those
more familiar.

## VERIS resources
The terms “action,” “threat actor” and
“variety” will be referenced often.
These are part of the Vocabulary for
Event Recording and Incident Sharing
(VERIS), a framework designed to allow
for a consistent, unequivocal collection
of security incident details. Here is how
they should be interpreted:

*   **Threat actor**: Who is behind the event?
    This could be the external “bad guy”
    who launches a phishing campaign
    or an employee who leaves sensitive
    documents in their seat back pocket.
*   **Action**: What tactics (actions) were
    used to affect an asset? VERIS
    uses seven primary categories of
    threat actions: Malware, Hacking,
    Social, Misuse, Physical, Error and
    Environmental. Examples at a high level
    are hacking a server, installing malware
    or influencing human behavior through
    a social attack.
*   **Variety**: More specific enumerations of
    higher-level categories, e.g., classifying
    the external “bad guy” as an organized
    criminal group or recording a Hacking
    action as SQL injection or brute force.

Learn more here:

*   github.com/vz-risk/dbir/tree/
    gh-pages/2021 includes DBIR
    facts, figures and figure data
*   veriscommunity.net features
    information on the framework with
    examples and enumeration listings
*   github.com/vz-risk/veris features
    the full VERIS schema
*   github.com/vz-risk/vcdb provides
    access to our database of publicly
    disclosed breaches, the VERIS
    Community Database
*   http://veriscommunity.net/
    veris_webapp_min.html allows you
    to record your own incidents and
    breaches. Don’t fret, it saves any
    data locally and you only share
    what you want

## Incident vs. breach
We talk at length about incidents and
breaches and we use the following
definitions:

*   **Incident**: A security event that
    compromises the integrity,
    confidentiality or availability of
    an information asset.
*   **Breach**: An incident that results in the confirmed disclosure—not just
    potential exposure—of data to an
    unauthorized party.

## Industry labels
We align with the North American
Industry Classification System (NAICS)
standard to categorize the victim
organizations in our corpus. The
standard uses two- to six-digit codes to
classify businesses and organizations.
Our analysis is typically done at the
two-digit level and we will specify
NAICS codes along with an industry
label. For example, a chart with a label
of Financial (52) is not indicative of 52
as a value. “52” is the code for Finance
and Insurance sector. The overall label
of “Financial” is used for brevity within
the figures. Detailed information on
the codes and classification system is
available here:

https://www.census.gov/
naics/?58967?yearbck=2012

## Being confident of our data
Starting in 2019 with slanted bar
charts, the DBIR has tried to make the
point that the only certain thing about
information security is that nothing is
certain. Even with all the data we have,
we’ll never know anything exactly.
However, instead of throwing our hands
up and complaining that it is impossible
to measure anything in a data-poor
environment, or worse, simply making
stuff up, we get to work. This year
we continue to represent uncertainty
throughout the report figures.

![Figure 1. Example slanted bar chart (n=402)](Image description: A slanted bar chart illustrating uncertainty in data points, with a 95% confidence level indicated by the slant. Overlapping slants suggest no significant difference between bars.)

![Figure 2. Example spaghetti chart](Image description: A spaghetti chart visualizing data over time, with darker areas indicating higher probability.)

![Figure 3. Example dot plot (n=672)](Image description: A dot plot where each dot represents an organization, with each dot representing 0.5% of organizations. This visualization aims to show data distribution among organizations.)

![Figure 4. Example violin chart (n=581)](Image description: A violin chart illustrating proportions of changes over a specific time period, with darker areas indicating higher probability.)

Figures 1, 2, 3 and 4 all convey the range
of realities that could credibly be true.
Whether it be the slant of the bar chart,
the threads of the spaghetti chart, the
dots of the dot plot, or the color of the
violin chart, they all convey the uncertainty
of our industry in their own special way.

The slant on the bar chart represents the
uncertainty of that data point to a 95%
confidence level (which is quite standard
for statistical testing). In layman’s terms, if
the slants of two (or more) bars overlap,
you can’t really say one is bigger than the
other without angering the math gods
(and their wrath is terrible).

Dot plots are also frequently used, and
the trick to understanding this chart is
that the dots represent organizations.
For example, if there are 200 dots (like
in Figure 3), each dot represents 0.5%
of organizations. This is a much better
way of understanding how something
is distributed among organizations and
provides additional information than
an average or a median. We added
additional colors and callouts to make
these even more informative this year.

Our newcomers this year are spaghetti
and violin charts. They attempt to capture
uncertainty in a similar way to slanted
bar charts but are more suited for,
respectively, data visualized over time and
proportions of changes over a specific
time period. For these charts, the darker
area is more likely to be the correct value.

Let us know what you think of them.¹ We
hope they make your journey through this
complex dataset a little less daunting.

## Credit where credit is due
Turns out folks enjoy citing the report,
and we often get asked how they
should go about doing it.

You are permitted to include statistics,
figures and other information from
the report, provided that you (a) cite
the source as “Verizon 2021 Data
Breach Investigations Report” and
(b) that content is not modified in any
way. Exact quotes are permitted but
paraphrasing requires review. If you
would like to provide people a copy
of the report, we ask that you provide
them a link to verizon.com/dbir/ rather
than the PDF.

## Questions?
Comments?
Upset there is no
AR/VR version of
the DBIR?²

Let us know! Drop us a
line at dbir@verizon.com,
find us on LinkedIn, tweet
@VerizonBusiness with
#dbir. Got a data question?
Tweet @VZDBIR!

¹ But only if you like them. Our figures guy is really thin skinned.
² We REALLY want to make it happen!

2021 DBIR Master’s Guide
4

# Introduction

Greetings! Welcome to the 2021 Data
Breach Investigations Report (DBIR)!
We always appreciate you, our readers,
but this year we would like to say thank
you for just showing up. Thanks for
simply making it through the often
frightening and always unpredictable
dystopian wasteland that was 2020,
and still having enough interest and
energy to care about making the world
a safer place. By the time you read this,
it is devoutly to be hoped that we have
moved on to a place of relative safety,
somewhere beyond Thunderdome if
you will.

Recent events around the world have
been deemed by many to be sufficient
cause to re-evaluate their priorities. In
similar fashion, we have stepped back
and taken another look at what we have
been doing over the past few years.
This exercise led to a revamp of our
patterns, the creation of some shiny
new ones and the recalibration of some
others. It is our hope that doing this will
increase awareness of where possible
dangers lie, and how organizations may
best avoid them. Perhaps we should say
“probable dangers,” since one lesson
from 2020 is that many more things are
possible than we might imagine. What
is impossible is to accurately predict
what those things might be. Therefore,
we will not meddle with words like
“possible,” but will confine ourselves
to what is “probable.”

This year we analyzed 79,635
incidents, of which 29,207 met our
quality standards and 5,258 were
confirmed data breaches, sampled
from 88 countries around the world.
Once again, we include breakouts
for 11 of the main industries, the SMB
section, and we revisit the various
geographic regions studied in the prior
report to see how they fared over the
last year. We also include our Center
for Internet Security (CIS) Controls®
recommendation mapping, because
the world being unpredictable and
uncertain doesn’t mean your security
strategy has to be.

As always, we wish to humbly say thank
you to our 83 contributors, both old and
new. This report would not be possible
without you and we are always grateful
for your continued support. Likewise,
we thank you again, our readers, for
continuing to share this journey with us.

Sincerely,
The DBIR Team

Gabriel Bassett
C. David Hylender
Philippe Langlois
Alexandre Pinto
Suzanne Widup

2021 DBIR Introduction
6

# Summary of findings

![Figure 5. Patterns in breaches (n=5,275)](Image description: A chart showing patterns in data breaches, with the number of breaches represented for each pattern.)

![Figure 6. Patterns in incidents (n=29,206)](Image description: A chart illustrating patterns in security incidents, with the number of incidents represented for each pattern.)

![Figure 7. Select action varieties (n=4,073)](Image description: A chart displaying selected action varieties within security incidents, indicating their frequency.)

![Figure 8. Select impacts of incidents](Image description: A chart detailing the selected impacts of security incidents.)

2021 DBIR Summary of findings
7

# Results and Analysis

## 02 Results
and Analysis

### Results
and Analysis:
Introduction

The results found in this and
subsequent sections within the report
are are based on a dataset collected
from a variety of sources, including
cases provided by the Verizon Threat
Research Advisory Center (VTRAC)
investigators, reports provided by our
external collaborators, and publicly
disclosed security incidents. The year-
to-year data will have new incident and
breach sources as we continue to strive
to locate and engage with additional
organizations that are willing to share
information to improve the diversity and
coverage of real-world events. This is a
sample of convenience,³ and changes
in contributors—both additions and
those who were not able to contribute
this year—will influence the dataset.

Moreover, potential changes in
contributors’ areas of focus can shift
bias in the sample over time. Still other
potential factors, such as how we filter
and subset the data, can affect these
results. All of this means that we are
not always researching and analyzing
the same population. However, they
are all taken into consideration and
acknowledged where necessary within
the text to provide appropriate context
to the reader.

Having said that, the consistency and
clarity we see in our data year-to-year
gives us confidence that while the
details may change, the major trends
are sound.

The DBIR is not in the business
of prediction,⁴ but it can go a
long way to help you shape
your response strategy in the
face of an uncertain future.

We believe it is fair to say that one of
the primary lessons that 2020 had to
teach us was that it is often futile to
attempt to predict the future. However,
not trying to predict it is not the same
thing as giving up on scenario planning
and preparing your organization for
probable outcomes to the best of
your ability. The DBIR is not in the
business of prediction,⁴ but it can go
a long way to help you shape your
response strategy in the face of an
uncertain future.

Consider Figure 9 for instance; it’s
your run-of-the-mill DBIR chart with
all the slanted bar-charted goodness,
courtesy of our Misuse action varieties.⁵
We have a few big things up top, and a
lot of stuff near the end.

One valid way to interpret this is
that the top bar or two are the norm
of what may happen, namely in this
example “Privilege abuse” and “Data
mishandling.” Those are the Action
varieties that are understood to be so
common that, if they were to cause a
breach, someone (most likely on a bird
website) would say, “That organization
should have known better!”

³ Convenience sampling is a type of nonrandom sampling that involves the sample being drawn from that part
of the population that is close at hand or available. More details can be found in our “Methodology” section.
⁴ Though we do suggest you put your money on “Trail Blazer” in the third.
⁵ Where are my insider threat fans at? Whoop whoop!

![Figure 9. Misuse varieties in breaches (n=178)](Image description: A slanted bar chart illustrating misuse varieties in breaches, showing the frequency of different types of misuse.)

2021 DBIR Results and Analysis
9

Suffice it to say, there’s a great deal of
inequality in the frequencies of the
varieties shown. Those small bars are
the extraordinary and uncommon
attacks that could happen but are
unlikely. If they were to cause a breach
the victim would claim, “It was an
advanced attack. There was nothing
that anyone could have done.”⁶

The Gini coefficient is
a measure of statistical
dispersion most commonly
used to represent the income
or wealth inequality within
a nation or other group
of people.⁹

However, if you take all those small bars
on the Action varieties and add their
breach frequencies together, you get
Figure 10. Now it doesn’t look quite so

uncommon anymore, does it? In fact,
in this example it appears that a breach
is just as likely to be caused by one
of our myriad exceptions as it is to
be caused by our second most likely
Action variety.

income (in other words, the “income
per person” chart is a horizontal line),
as a 0, and a world where one individual
has all the income (in other words all we
have on the chart is a huge vertical spike
somewhere) as a 1.

But does breach data always behave
like this? Rather than show you lots of
bar charts,⁷ we’re going to condense
that concept down into a single number.
Figures 11 and 12 show some data with
different levels of inequality. We use the
word “inequality” not by chance, but to
introduce the fact that we can calculate
the Gini coefficient⁸ to represent this
long tail behavior.

The Gini coefficient is a measure of
statistical dispersion most commonly
used to represent the income or wealth
inequality within a nation or other group
of people.⁹ While it uses a lot of math
none of us can be bothered with, it
ultimately represents a completely equal
outcome, where everyone has the same

Let’s bring this closer to our subject
matter by looking at some security-
related data, like how often your SIEM
generates a group of critical alerts that
need immediate review. Anecdotally, you
could attest that happens exactly “every
time you are on-call,” but humor us for
a moment. In Figure 11, we generated
some simulated example data that is
perfectly smooth and looks horizontal
on the chart—this one has an equality
score of 0 (perfectly equal). Figure 12
has actual data representing the time
interval between critical SIEM events,
and it is extremely spikey.¹⁰ It has a Gini
equality score of 0.95, demonstrating a
huge variation time between events. It’s
not just you: critical SIEM events fall into
everyone’s laps indiscriminately.

![Figure 10. Top Misuse varieties in breaches (n=178)](Image description: A chart showing the top misuse varieties in breaches, highlighting their frequencies.)

![Figure 11. Simulated time between SIEM events (n=1,335,343)](Image description: A chart showing simulated time intervals between critical SIEM events, presented as a smooth, horizontal line indicating perfect equality.)

![Figure 12. Time between SIEM events (n=1,335,343)](Image description: A chart illustrating actual time intervals between critical SIEM events, showing a highly variable and "spikey" distribution.)

⁶ This report makes no claim about the validity of such a statement. Please refer to our official spokesperson and legal counsel. The data privacy of our readers is of the utmost
importance to us.
⁷ And completely obliterate our page count budget.
⁸ https://en.wikipedia.org/wiki/Gini_coefficient
⁹ A less well-known fact is that the wish for wealth redistribution led to the phrase “Gini in a bottle.” Not really, but it would have been cool if it did.
¹⁰ A technical term of art in Data Science, we assure you.

2021 DBIR Results and analysis
10

This complicated mathematical setup is
to convey the reality that the DBIR data
(incident and non-incident alike) is very
unequal,¹¹ but at least we can measure
it. Figure 13 shows the equality scores
for Action, Actor, Asset, and Attribute
varieties and vectors over the last
seven years. The scores range from
about 0.73 to 0.94, or as we would say
here, “high.” Breach data may seem
likely to always be the same, but some
varieties are more equal than others.

The reality is you don’t need a crystal
ball, a neural network or next-gen AI to
tell you what the norm¹² is. You can do
that for yourself and plan accordingly.
On the other hand, you can’t solution
your way out of the long tail. It is
made up of a legion of little things
that happen only rarely—they are the
exceptions to the norm. Well, maybe
you can if you have enough money. And
some organizations that are in critical
roles to our society have no choice
but to try to do so. But from a purely
monetary value, if you look at what
breaches cost in the Impacts section,
it’s not a wise use of your organization’s
resources to engineer solutions for
every single possible exception.¹³

Armed with the knowledge of what is
the norm and what is the exception, an
ideally optimized solution would be to
engineer solutions for the norm, and
train your security operation teams
to handle the exceptions. Turns out
humans are very flexible problem-
solvers, and most love a good
challenge occasionally.

The next time we are up against
a paradigm-shifting breach that
challenges the norm of what is most
likely to happen, don’t listen to the
ornithologists on the blue bird website
chirping loudly that “We cannot patch
manage or access control our way out
of this threat,” because in fact “doing the
basics” will help against the vast majority
of the problem space that is most likely
to affect your organization.

Read on to learn what the normal actor
has been up to for the last year, and pick
out the areas where you can improve,
against both the norm and the exception.
Because the only way to predict the
future is to change it yourself.

![Figure 13. Inequality of enumerations in DBIR varieties and vectors for last 7 years](Image description: A chart showing the inequality scores for Action, Actor, Asset, and Attribute varieties and vectors over the past seven years, ranging from approximately 0.73 to 0.94.)

¹¹ We deeply apologize to the junior U.S. senator from Vermont for the fact that the top 3% of varieties are responsible for 87% of the breaches.
¹² You’re reading the DBIR, and that is a great step in the right direction, if we may say so.
¹³ This argument does not consider potential incidents where loss of life or the security of individuals is concerned, as it would make no sense to
assign a monetary value to that, and would, in fact, be callous and cruel.

2021 DBIR Results and analysis
11

### Actor

“All the world’s a stage,” and our threat
actors “all have their exits and their
entrances.” We must admit that they
seem to know their cues very precisely.
However, at this point the analogy breaks
down a bit, as rather than “playing their
many parts”¹⁴ we seem to keep viewing
the same performance repeated ad
infinitum, as if forced to endlessly
re-watch a recorded musical theater
presentation on a streaming service.¹⁵

It seems clear that our External actors
are not giving up their close-ups,
as they continue year after year to
dominate the Actor types in breaches
as illustrated in Figure 14. As a reminder
to our readers, the Internal type
shown here will include breaches in
which both Misuse actions (where the
mythical winged internal threats live in
our taxonomy) and Error actions (the
oopsies) occurred.

Of course, an External actor breaking
into an organization by leveraging
illicitly obtained credentials or other
illegal access to pivot internally may
initially resemble an internal threat
before detailed incident forensics are
engaged. But even though the call may
be coming from inside the house, there
is still a stranger on the line.

As in past years, financially motivated
attacks continue to be the most common
(Figure 15), likewise, actors categorized
as Organized crime continue to be
number one (Figure 16).

As in past years, financially
motivated attacks continue
to be the most common (Figure
15), likewise, actors categorized
as Organized crime continue to
be number one (Figure 16).

![Figure 14. Threat actor over time in breaches](Image description: A line chart showing the trend of threat actor types in breaches over time, indicating the dominance of External actors.)

![Figure 15. Top threat actor motive over time in breaches](Image description: A line chart illustrating the trend of top threat actor motives in breaches over time.)

![Figure 16. Top threat actor varieties in
breaches (n=2,277)](Image description: A bar chart showing the top threat actor varieties in breaches, with frequencies indicated.)

¹⁴ As You Like It, William Shakespeare.
¹⁵ Anyone know if the Cyber+ trademark is available?

2021 DBIR Results and analysis
12

However, since 2015 it is relatively
common for State-sponsored actors
to also crave that cold hard cash¹⁶ as
the Financial motives for those actors
have fluctuated between 6% and 16%
of recorded breaches. Given this result,
it should come as no surprise when you
glance at Figure 17 and find that the
two most common cybercrime terms
found on criminal forums are bank
account and credit card related.

Even as awareness of supply chain
attacks has increased over the last
few months, the overall percentage of
incidents with a Secondary motive—
where the ultimate goal of an incident
was to leverage the victim’s access,
infrastructure or any other asset to
conduct other incidents—has decreased
slightly as a percentage from last year.
There are two caveats here that should
be kept in mind: The associated growth

year-over-year of Financially motivated
breaches, and that most Secondary
motive breaches reported to us are
simple in nature (which suggests the
catastrophic ones on everyone’s minds
are still very much the exception).

![Figure 17. Terms over time in criminal forums and marketplaces](Image description: A chart showing terms over time in criminal forums and marketplaces, highlighting bank account and credit card related terms.)

¹⁶ Or the hot ethereal cryptocurrency.

2021 DBIR Results and analysis
13

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

![Figure 18. Top Actor motives in incidents (n=5,085)](Image description: A bar chart showing the top actor motives in security incidents, with frequencies indicated.)

![Figure 19. Ratio of days of high to low detection in honeypot data](Image description: A chart illustrating the ratio of days with high to low detection rates in honeypot data, showing the relative occurrence of attack types.)

### Secondary motive subset
In the Secondary Motive subset, we had an additional 24,913 incidents of which
only one was a known breach. In all of these incidents, web apps were attacked with
a secondary motive by External actors. Beyond that, we know very little.

### Action

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
to address the virulent elephant¹⁷ in
the room, so we have centered this
initial analysis of Actions on evaluating
how adapting to life in a pandemic-
stricken world has impacted the threat
landscape. The DBIR team released a
COVID-19 Threat Landscape Trends
article¹⁸ in the middle of last year, and
it is only fair that we revisit how our
speculations (see how we avoided
the word predictions?) fared.

![Figure 20. Top Action varieties in breaches (n=4,073)](Image description: A bar chart showing the top action varieties in data breaches, with frequencies indicated.)

![Figure 21. Top Action varieties in incidents (n= 24,362)](Image description: A bar chart displaying the top action varieties in security incidents, with frequencies indicated.)

¹⁷ Viruphant? Eleplent?
¹⁸ https://enterprise.verizon.com/resources/articles/analyzing-covid-19-data-breach-landscape/

2021 DBIR Results and analysis
15

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
in breaches as it has in the past.
Admittedly, we expected to see an
increase here due to a larger remote
workforce. However, the numbers
have remained in the region of
25% of breaches, which is still a
significant number.

The major change this year with regard
to action types was Ransomware
coming out like a champ and grabbing
third place in breaches (appearing in
10% of them, more than doubling its
frequency from last year). This is also
something we discussed, but this may
have less to do with the changes in
working arrangements than it does
the shift in tactics of the actors who
“named and shamed” their victims.

These actors will first exfiltrate the data
they encrypt so that they can threaten
to reveal it publicly if the victim does not
pay the ransom. We are not sure if this
breach double-dipping is permitted in
the Threat Actor Code of Conduct, but
there has been no evidence that they
have one anyway.

![Figure 22. Change in COVID-19-related Action varieties](Image description: A chart showing the change in action varieties related to COVID-19, comparing current data with previous reports.)

The final piece of this puzzle pertains
to Error actions, where we opined that
we would see an increase, but actually
had a decrease this year to 17% of
breaches (from 22%). This breaks a
three-year streak of either staying the
course or increasing. Granted, the
absolute number of Error breaches did
increase from 883 to 905. However,
as a proportion of the dataset, Error
decreased due to the rapid growth of
Social breaches.

Of course, we here on the team secretly
blame each other for this miscalculation
on our part, as any team would. Still,
both in relative and absolute terms, this
is a significant value and is on par with
Malware-related breaches as Figure 23
demonstrates, and it should certainly
be front and center in your control
definition strategy.

![Figure 23. Actions in breaches (n=5,257)](Image description: A bar chart showing the actions taken in data breaches, with frequencies indicated.)

2021 DBIR Results and analysis
16

Actions have
consequences¹⁹

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
those findings align with the attack
chain information that is present in
some of the incidents we analyze. If