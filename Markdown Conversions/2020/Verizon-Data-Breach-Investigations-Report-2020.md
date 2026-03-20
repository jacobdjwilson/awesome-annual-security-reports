providers (e.g., gmail.com, yahoo.com, hotmail.com). However, the next 150
domains were almost exclusively
corporate domains. This suggests that
while the majority of leaked emails
are personal, a significant number of
corporate email addresses are also
being compromised.

This is a critical finding because
corporate email addresses are often
used as usernames for other services.
If an attacker has your corporate email
address and a password from a breach
at another site, they may be able to
gain access to your corporate systems.
This is why it is so important to use
unique passwords for every service
you use and to enable multi-factor
authentication (MFA) whenever
possible.

![Chart showing email top-level domains (TLDs) compromised]

30

2020 DBIR   Results and analysis

---

registration services. That
accounted for about 97% of the
breaches, and provides hope that
most emails compromised aren’t your
employees’ corporate addresses.
However, the little matter of the
remaining 3% was comprised of tens
of millions of addresses.

What’s that
attribute going
to cost you?

As reported in FBI IC3 complaints, the
most common loss was $32,200 this
year, up from about $29.3k last year.
That’s still basically in the preowned
car range, and while no one wants to
lose that much money, it could certainly
be much worse.

it

pl
uk

fr

de

net

other

ru

Figure 38. Prevalence of top-level domains (TLDs) in leaked emails (n = 3.94 billion)

)
4
0
4
=
n
(

B
D
C

,

)
5
6
0
3
1
=
n
(

C
A
E
/
C
E
B

i

e
p
y
t
t
n
a
p
m
o
C

l

$10

$1,000

$100,000

Figure 39. Loss amount in Corporate Data Breaches (CDB) and business email
compromises/(individual) email account compromises (BEC/EAC)
(Excludes complaints with zero loss amount)

2020 DBIR   Results and analysis

30

How many paths
must a breach
walk down?

We tend to think about incidents and
breaches as a point in time. You snap
your fingers and all the attacker actions
are complete, the stolen data is in the
attacker’s saddlebags and they are
off down Old Town Road and away
into the sunset. Still, we all know that
is not quite what actually happens.
Many of the attacks studied in this
report fall somewhere between a
stickup and the Great Train Robbery
in terms of complexity. The good
news is that defenders can use this
to their advantage.

As you can see in Figure 40, attacks
come in numerous forms and sizes,
but most of them are short, having
a small number of steps (you can
notice that by how the volume of line
segments thin out between the four
and six steps markers). The long ones
tend to be Hacking (blue) and Malware
(green) breaches, compromising
Confidentiality (the middle position)
and Integrity (the lower position) as the
attacker systematically works their way
through the network and expands their
persistence. The benefit in knowing

the “areas” (threat actions—colors/
compromising specific attributes—
positions) attackers are more likely
to pass through in their journey to
a breach gives you first advantage,
because you can choose where to
intercept them. You may want to stop
their initial action or their last. You
may not want to go near them, so
you don’t have to listen to “Old Town
Road.” All of these options are
understandable in accordance with
your response strategy.36

36  Or to how susceptible you are to ubiquitous earworms.

Figure 40. Attack paths in incidents
(n = 652. Two breaches, 77 and 391 steps respectively, not shown.)

Availability

Confidentiality

Integrity

Action

Error

Malware

Physical

Unknown

Hacking

Misuse

Social

Steps

30

20

10

8

6

4

2

2020 DBIR   Results and analysis

31

OK, take a deep breath and look at
Figure 40 on the previous page.
No, a butterfly did not just vomit
on your report. Don’t worry about
trying to understand all the graphic
has to tell. Instead, let us convey the
concept of what you are seeing here.
This abstract work of art contains
a line (a “path”) for each of several
hundred breaches. In the way a bar
chart summarizes numbers, this
graph summarizes paths taken by
the attacker.

Each colored line segment
(a “step”) represents an action
taken by the threat actor along with
the associated attribute that was
compromised. The color of each step
represents the VERIS threat action of

the step, and the position where the
step ends represents the attribute
compromised. But the real trick to
understanding this chart is that the
paths start from the left and move to
the right—the first step on a path will
either come from the top of the chart
or the bottom (because they have to
come from somewhere) and “land”
on the appropriate attribute.

So, if you pick any yellow step
coming from the top of the chart
starting at 4 on the horizontal axis
and ending on the lower position of
the chart, you just found yourself at
the beginning of a four-step incident
that started with a Social action that
compromised the Integrity attribute.
Also, notice how Error actions (the

dark blue lines coming from the
bottom of the chart) are usually part
of very short paths and land on the
Confidentiality attribute.

There’s a small amount of noise put
into the positions of the lines, since
otherwise the same lines would be
exactly on top of each other and we
wouldn’t be able to see a lot here. But
mostly we did it for the art.

Figures 41 and 42 provide us with our
next defensive advantage. Attackers
prefer short paths and rarely attempt
long paths. This means anything you
can easily throw in their way to increase
the number of actions they have to
take is likely to significantly decrease
their chance of absconding with the
data. Hopefully by now we have driven
home the significance and prevalence
of credential theft and use. While we
admit that two-factor authentication
is imperfect, it does help by adding an
additional step for the attacker. The
difference between two steps (the
Texas two-step) and three or four steps
(the waltz) can be important in your
defensive strategy.

The difference between two
steps (the Texas two-step)
and three or four steps (the
waltz) can be important in
your defensive strategy.

Figure 41. Number of steps per incident
(n = 654. Two breaches, 77 and 391 steps respectively, not shown.)

s
t
n
e
d
c
n

i

I

Steps

Figure 42. Number of steps per breach
(n = 429. Two breaches, 77 and 391 steps respectively, not shown.)

s
e
h
c
a
e
r
B

1

Steps

2020 DBIR   Results and analysis

32

Finally, take a look at Figure 43. It
shows what actions happen at the
beginning, middle and end of both
incidents and breaches. It is not what
is on top that’s interesting (we already
know “Social—Phishing” and “Hacking—
Use of stolen creds” are good ways to
start a breach and “Errors” are so short
that the beginning of the path is also
the end). The interesting bit is what’s
near the bottom. Malware is rarely the

first action in a breach because it
obviously has to come from
somewhere. Conversely, Social
actions almost never end an attack.
In the middle, we can see Hacking and
Malware providing the glue that holds
the breach together. And so, our third
defensive opportunity is to guess what
you haven’t seen based on what you
have. For example, if you see malware,
you need to look back in time for what

you may have missed, but if you see
a social action, look for where the
attacker is going, not where they are.

All in all, paths can be hard to wrap your
head around, but once you do, they
offer a valuable opportunity not just for
understanding the attackers, but for
planning your own defenses.

Figure 43. Actions at the beginning, middle and end of incidents and breaches

Beginning

Hacking

Social

Error

Malware

Misuse

Physical

Hacking

Social

Error

Misuse

Physical

Malware

s
t
n
e
d
c
n

i

I

s
e
h
c
a
e
r
B

Middle

Malware

Hacking

Social

Misuse

Physical

Malware

Hacking

Social

Misuse

Physical

End

Malware

Hacking

Error

Misuse

Social

Physical

Hacking

Malware

Error

Misuse

Social

Physical

2020 DBIR   Results and analysis

33

Timeline

As we analyze how breach timelines
have evolved over time, Discovery
in days or less is up (Figure 44) and
Containment in that same timeframe
has surpassed its historic 2017 peak
(Figure 45). However, before you break
out the bubbly, keep in mind that this
is most likely due to the inclusion of
more breaches detected by managed
security service providers (MSSPs)
in our incident data contributors’
sampling, and the relative growth
of breaches with Ransomware as
collateral damage, where Discovery
is often close to immediate due to
Actor disclosure.37

Discovery in Months or more still
accounts for over a quarter of
breaches. We are obligated to point
out that since this is a yearly report,
this is usually a trailing indicator of the
actual number, as there are potentially
a significant number of breaches that
occurred in 2019 that just have not
been discovered yet.

All in all, we do like to think that there
has been an improvement in detection
and response over the past year and
that we are not wasting precious years
of our life in a completely pointless
battle against the encroaching void of
hopelessness. Here, have a roast beef
sandwich on us.

60%

40%

20%

0%

2015

Figure 44. Discovery over time in breaches

80%

60%

40%

20%

0%

2015

Figure 45. Containment over time in breaches

Days
or less

Months
or more

2017

2019

Days
or less

2017

2019

37  Nothing quite like a rotating flaming skull asking for cryptocurrency on your servers to help you ”discover” a breach.

2020 DBIR   Results and analysis

34

Incident classification
patterns and subsets

For the uninitiated, VERIS and the DBIR
may seem overwhelming when you
consider both the amount of data we
possess (now over 755,000 incidents
over the years) and the depth of that
data (over 2,400 values we are able
to track on each incident). To help us
better understand and communicate
this vast arsenal of information, we
started to leverage what we call
“Patterns” in 2014, which are essentially
different clusters of “like” incidents.
We won’t go too much into the data
science-y aspect,38 but the outcome
was the identification of nine core
clusters, our Incident Classification
Patterns. This allows us to abstract
upward and discuss the trends in the
patterns rather than the trends in each
of our different combinations: Actions,
Assets, Actors and Attributes.

Looking over our 409,000 security
incidents and almost 22,000 quality
data breaches since the inception of
the report, the numbers reveal that
94% of security incidents and 88% of
data breaches fall neatly in one of the
original nine patterns. However, when
we focus our lenses on just this year’s
data, the percentages drop to 85%
of security incidents and 78% of
data breaches.

Nothing better demonstrates this than
our category of “Everything Else,”
effectively designed to be our spare-
USB-cable drawer of breaches, having
risen to one of the top patterns due to
the rise of Phishing, while some of the
other patterns have drastically fallen
since their initial inception. It seems
that time waits for no pattern, and
the only breach constant is breaches
changing over time.

The patterns will be referenced more
in the “Region” and “Industry” sections,
but to get acquainted with them or to
rekindle a prior relationship, they are
defined here.

Web Applications

Lost and Stolen Assets

Everything Else

Cyber-Espionage

Miscellaneous Errors

Point of Sale

Crimeware

Payment Card Skimmers

Privilege Misuse

Denial of Service

Figure 46. Patterns in breaches (n = 3,950)

Denial of Service

Miscellaneous Errors

Crimeware

Privilege Misuse

Everything Else

Cyber-Espionage

Web Applications

Point of Sale

Lost and Stolen Assets

Payment Card Skimmers

Figure 47. Patterns in incidents (n = 32,002)

38  We recommend taking a glance at the 2014 report if you are curious about the nerdy stuff.

2020 DBIR   Results and analysis

35

Patterns

Crimeware
One of the oldest games in town,
Crimeware includes all the malware
that doesn’t fall into the other patterns.
Think of these as the common type of
commodity malware that everyone has
probably seen on some email claiming
to be a fax or a missed delivery
package. These incidents and breaches
tend to be opportunistic and financially
motivated.

Notable findings: This year has
continued the trend of modest
increases in incidents and
breaches involving Crimeware,
now up to about 400, which
is higher than last year and
roughly matches the highest
levels that were reached in
2015. Unsurprisingly, these
types of attacks normally
propagate through email, either
as a link or as an attachment,
dropping something nasty like a
downloader, password dumper,
Trojan or something that’s got
C2 functionality.

Cyber-Espionage
This pattern consists of espionage,
enabled via unauthorized network or
system access, and largely constitutes
nation-states or state-affiliated actors
looking for those oh-so-juicy secrets.

Notable findings: This is one of
our patterns that has decreased
this year, both in raw numbers and
also as a percentage from 13.5%
of breaches in 2018 to 3.2% of
breaches in 2019. The drop in
raw numbers could be due to
either under-reporting or failure
to detect these attacks, but the
increase in volume of the other
patterns is very much responsible
for the reduction in percentage.

These types of attacks rely
heavily on Social and Malware
combined vectors, using Phishing
in 81% of the incidents and some
form of malware in 92%.

Denial of Service
These attacks are very voluminous (see
what we did there) in our dataset at
over 13,000 incidents this year. Attacks
within this pattern use differing tactics,
but most commonly involve sending
junk network traffic to overwhelm
systems, thereby causing their services
to be denied. The system can’t handle
both the incoming illegitimate traffic
and the legitimate traffic.

Notable findings: While the
amount of this traffic is increasing
as mentioned, in DDoS, we
don’t just look at the number of
attacks that are conducted. We
also look at the bits per second
(BPS), which tells us the size of

the attack, and the packets per
second (PPS), which tells us the
throughway of the attack. What
we found is that, regardless of the
service used to send the attacks,
the packet-to-bit ratio stays within
a relatively tight band and the PPS
hasn’t changed that much over
time, sitting at 570 Mbps for the
most common mode (Figure 48).

When it comes to defending
against DDoS, a layered approach
is best, with some of the attacks
being mitigated at the network
level by internet service providers
and the others being handled at
the endpoint or a content
delivery network (CDN) provider.
These attacks are prevalent
because of their ease of use
and the fact that internet-facing
infrastructure can be targeted;
however the impact to your
organization and the decision of
whether to mitigate will be based
entirely on your business.

bps

1M

10M

100M

1G

10G

100G

Figure 48. Most common distributed denial of service (DDoS) bits per second (BPS) (n = 195)

2020 DBIR   Results and analysis

36

Privilege Misuse
This pattern consists of “Misuse”
actions, which are intentional actions
undertaken by internal employees that
result in some form of security incident.

Notable findings: Misuse is down
as a percentage of incidents, as
the other patterns increase by
association. However, that could
be attributed to lower granularity
data this year and may rise back
to previous levels in 2021. On the
other hand, breaches are showing
a legitimate drop, which appears
to be associated with less misuse
of databases to access and
compromise data.

Miscellaneous Errors
Life is full of accidents and not to
disappoint Bob Ross, but not all of
them are happy little trees. This pattern
captures exactly that, the unintentional
(as far as we know) events that result in
a cybersecurity incident or data breach.

Notable findings: The majority of
these errors are associated with
either misconfigured storage or
misdelivered emails, committed
by either system admins or
end users. We’ll let you figure
out which actor is associated
with which action. In terms of
discovery, these are often found
by trawling security researchers
and unrelated third parties who
may have been on the receiving
end of those stray emails. The
Results and Analysis Error section
goes into even more detail for
those of you with this unique
predilection.

Payment Card Skimmers
This pattern is pretty self-explanatory:
These are the incidents in which a
skimmer was used to collect payment
data from a terminal, such as an ATM
or a gas pump.

Notable findings: Our data has
shown a continuous downward
trend of incidents involving
Point of Sale (PoS) Card
Skimmers, which are now down
to 0.7% of our breach data.

At approximately 30 incidents,
it is showing a relatively marked
decline from its peak of 206 back
in 2013. This decrease could be
attributed to a variety of different
causes, such as less reporting to
our federal contributors or shifts
in the attacker methodology.

Point of Sale (PoS)
This pattern includes the hacking and
remote intrusions into PoS servers
and PoS terminal environments for the
purpose of stealing payment cards.

Notable findings: Much like the
Payment Card Skimmers, this
pattern has received a notable
decrease in the last few years,
making up only 0.8% of total data
breaches this year. The majority
of these incidents include the
use of RAM scrapers, which
allow the adversaries to scrape
the payment cards directly from
the memory of the servers and
endpoints that run our payment
systems. However, the majority
of payment card crime has moved
to online retail.

Lost and Stolen Assets
These incidents include any time
where an asset and/or data might have
mysteriously disappeared. Sometimes
we will have confirmation of theft and
other times it may be accidental.

Notable findings: This pattern
tends to be relatively consistent
over the years, with approximately
4% of breaches this year (the
previous two years fluctuating
from 3% to 6% of breaches).
These types of incidents occur
in various different locations, but
primarily occur from personal
vehicles and victim-owned areas.
Don’t forget to lock your doors.

Web Applications
Incidents in this pattern include
anything that has a web application
as the target. This includes attacks
against the code of the actual web
application, such as exploiting code-
based vulnerabilities (Hacking—Exploit

Vuln) to attacks against authentication,
such as Hacking—Use of Stolen Creds.

Notable findings: In the data
provided by contributors who
monitor attacks against web
applications (Figure 49), SQL
injection vulnerabilities and PHP
injection vulnerabilities are the
most commonly exploited. This
makes sense since these types of
attacks provide a quick and easy
way of turning an exposed system
into a profit maker for the attacker.
However, in vulnerability data,
cross-site scripting (XSS), the
infamous ding popup vulnerability,
is the most commonly detected
vulnerability and SQLi attacks are
only half as common as XSS.

other inject

XSS

file
upload

local
file inject

PHP
inject

SQL
inject

Figure 49. Web application attack blocks
(n = 5.5 billion)

Everything Else
This pattern is our graveyard of lost
incident souls that don’t fall into any of
the previously mentioned patterns.

Notable findings: The majority
of these incidents are Phishing
or Financially Motivated Social
Engineering where attackers try
to commit fraud via email. Rather
than go into detail here, we’ll
point you to the Results and
Analysis—Social section,
which goes into great detail on
Financially Motivated Social
Engineering and Phishing.

2020 DBIR   Results and analysis

37

Subsets

In addition to the main nine Patterns, there is another level of
patterns that we examine separately due to different factors that
might skew our results and analysis, such as an extremely high
volume of low-detailed incidents. This year, like the previous one,
the subpatterns we examined separately are divided into the
Botnet subset and Secondary motives.

Botnet subset
This subset consists of 103,699
incidents from various occurrences of
Trojans and malware being installed on
desktops and servers. The majority of
these incidents tend to be low quality
and limited in detail, coming from
multiple incident sources.

Secondary webapp subset
This subset examines those security
incidents in which the victim web
application was a means to an end for
a different attack. This is often seen in
the form of servers being compromised
and used as part of a botnet or to DDoS
other systems.

Finance
(52)

Professional
(54)

s
e
i
r
t
s
u
d
n

i
r
e
h
t
O

Information
(51)

Notable findings: In Figure 50, we
see that botnets primarily affect
the Financial, Information and
Professional Services verticals.
All these industries should focus
on their customers’ security as
well as their own. The absolute
numbers on this subset have more
or less doubled from the previous
year. Also, be mindful that
these types of incidents impact
everyone, with 41% of victims
originating outside North America.

Notable findings: The Secondary
subset represents a total of
5,831 incidents, with greater
than 90% of them involving some
form of hacking, malware and
impacting servers. As we point
out in the Actor section of Results
and Analysis, if you give the bad
guy the opportunity to add your
infrastructure to theirs, they
won’t hesitate.

Figure 50. Botnet infections (n = 103,699)

2020 DBIR   Results and analysis

38

Industry analysis

Section title pulled
into footer

0
3

Industry
analysis

Introduction
to industries

This year we collected 157,525 incidents
and 108,069 breaches. That may
sound impressive until you realize that
100,000+ of those breaches were
credentials of individual users being
compromised to target bank accounts,
cloud services, etc. We break those
out into the Secondary motive subset
in the “Incident classification patterns
and subsets” section. After filtering for
quality and subsetting, we are left with
the incidents and breaches in Table 1.

Our annual statement on what not to
do with this breakout will now follow.
Do not utilize this to judge one industry
over another; a security staffer from
an Administrative organization waving
this in the face of their peer from the
Financial sector and trash-talking is a
big no-no. The number of breaches or
incidents that we examine is heavily
influenced by our contributors. These
numbers simply serve to give you an
idea of what we have to “work with,”
and is part of our pledge to the

community to be transparent about
the sourcing of the data we use in
the report.

Figures 51 and 52 come with yet
another warning. The numbers shown
here are simply intended to help you
to get your bearings with regard to
industry. The smaller the numbers in
a column, the less confidence we can
provide in any statistic derived from
that column.

Incidents:

Total

Accommodation (72)

Administrative (56)

Agriculture (11)

Construction (23)

Education (61)

Entertainment (71)

Finance (52)

Healthcare (62)

Information (51)

Management (55)

Manufacturing (31–33)

Mining (21)

Other Services (81)

Professional (54)

Public (92)

Real Estate (53)

Retail (44–45)

Trade (42)

Transportation (48–49)

Utilities (22)

Unknown

Total

Total

Small

Large

Unknown

Breaches:

32,002

407

8,666

22,929

Total

Total

3,950

Small

Large

Unknown

221

576

3,153

125

27

31

37

819

194

1,509

798

5,471

28

922

46

107

7,463

6,843

37

287

25

112

148

7

6

1

1

23

7

45

58

64

0

12

1

8

23

41

5

12

2

3

5

6,973

32,002

83

407

11

15

3

16

92

3

50

71

51

26

469

7

1

73

6,030

4

45

9

16

15

107

6

27

20

704

184

1,414

669

Accommodation (72)

Administrative (56)

Agriculture (11)

Construction (23)

Education (61)

Entertainment (71)

Finance (52)

Healthcare (62)

5,356

Information (51)

2

441

38

98

Management (55)

Manufacturing (31–33)

Mining (21)

Other Services (81)

7,367

Professional (54)

772

28

230

14

93

128

Public (92)

Real Estate (53)

Retail (44–45)

Trade (42)

Transportation (48–49)

Utilities (22)

Unknown

1,659

5,231

8,666

22,929

Total

92

20

21

25

228

98

448

521

360

26

381

17

66

326

346

33

146

15

67

26

6

6

1

1

15

3

32

31

32

0

5

0

6

14

24

3

7

1

3

2

688

3,950

29

221

7

10

0

10

22

1

28

32

32

25

185

5

1

13

50

3

18

6

6

4

118

576

79

4

20

14

191

94

388

458

296

1

191

12

59

299

272

27

121

8

58

20

541

3,153

Table 1. Number of security incidents by victim industry and organization size

2020 DBIR   Industry analysis

40

9

12

5

4

6

6

3

16

9

17

5

6

4

49

47

25

19

2

1

)
3
3
-
1
3
(

g
n
i
r
u
t
c
a
f
u
n
a
M

Breaches

9

5

1

2

3

1

11

6

9

3

1

12

12

9

18

15

5

23

15

1

1

16

32

50

5

5

15

1

55

9

5

4

7

)
2
7
(

n
o
i
t
a
d
o
m
m
o
c
c
A

1

10

2

14

10

10

9

13

2

1

59

28

142

116

149

80

63

7

24

17

9

14

95

35

97

73

52

32

8

49

19

26

27

113

62

22

126

162

114

47

2

10

1

1

46

4

4

3

13

16

34

24

2

1

9

5

2

14

85

33

193

145

176

91

26

109

80

9

2

5

90

59

14

22

29

30

13

10

2

20

59

112

6

1

4

9

17

1

2

25

18

1

1

1

15

16

6

9

15

2

4

59

25

13

14

21

4

4

7

Web Applications

Everything Else

Privilege Misuse

Crimeware

Miscellaneous Errors

Cyber-Espionage

Lost and Stolen Assets

Point of Sale

Payment Card Skimmers

Denial of Service

28

157

137

15

74

24

Hacking

39

61

7

21

18

9

32

33

38

155

90

105

57

150

35

73

8

66

23

127

181

118

7

3

28

29

2

7

12

2

21

3

45

101

14

73

79

22

68

123

9

10

12

2

7

1

35

22

13

23

9

13

14

6

16

3

n
r
e
t
t
a
P

n
o
i
t
c
A

t
e
s
s
A

Malware

Social

Misuse

Error

Physical

Environmental

Server

User Dev

Person

Network

Media

Kiosk/Term

Embedded

162

79

317

333

324

165

24

56

243

213

26

105

53

21

19

6

3

51

72

11

4

1

1

1

1

83

109

47

168

102

115

61

157

4

4

25

114

2

5

18

12

17

2

1

13

12

5

9

12

3

1

89

74

116

84

17

33

5

2

2

1

23

25

6

4

9

17

14

3

e
v
i
t
a
r
t
s
n
m
d
A

i

i

)
6
5
(

)
1
6
(

n
o
i
t
a
c
u
d
E

)
3
2
(

n
o
i
t
c
u
r
t
s
n
o
C

)
1
7
(

i

t
n
e
m
n
a
t
r
e
t
n
E

)
2
5
(

e
c
n
a
n
F

i

)
2
6
(

e
r
a
c
h
t
l
a
e
H

)
1
5
(

n
o
i
t
a
m
r
o
f
n

I

)
2
2
+
1
2
(

)
1
8
(

i

s
e
c
v
r
e
S
r
e
h
t
O

)
4
5
(

l

i

a
n
o
s
s
e
f
o
r
P

)
2
9
(

c

i
l

b
u
P

l
i

a
t
e
R

)
5
4
-
4
4
(

)
3
5
(

e
t
a
t
s
E

l

a
e
R

)
9
4
-
8
4
(

n
o
i
t
a
t
r
o
p
s
n
a
r
T

0%

25%

50%

75%

100%

s
e
i
t
i
l
i
t
U
+
g
n
n
M

i

i

Figure 51. Breaches by Industry

2020 DBIR   Industry analysis

41

Incidents

6

5

10

1

2

3

1

10

14

9

3

1

17

14

9

1

15

10

10

2

15

13

2

15

18

13

1

18

34

18

6

17

15

1

1

17

62

51

9

6

15

2

75

17

9

7

4

1

)
2
7
(

n
o
i
t
a
d
o
m
m
o
c
c
A

86

23

166

161

154

81

119

34

358

392

15

135

4,289

11

1

39

35

Everything Else

55

24

Crimeware

179

35

63

192

403

393

65

30

152

140

162

107

7

11

36

74

10

54

403

61

924

1

4,611

150

62

22

128

163

115

3

1

22

66

11

11

2

15

8

4

16

47

75

27

2

1

21

16

11

14

6

6

3

30

139

149

14

66

22

Web Applications

2

2

14

25

3

6,712

313

20

63

112

1

4

40

26

25

1,540

6

2

2

1

1

1

7

2

15

2

5

16

67

21

1

8

8

9

Privilege Misuse

Denial of Service

Miscellaneous Errors

Cyber-Espionage

Lost and Stolen Assets

Point of Sale

Payment Card Skimmers

10

196

43

88

206

420

465

26

17

168

4,347

1

82

29

498

99

1,135

179

4,806

362

37

34

6,917

1,057

16

153

38

99

23

160

173

161

393

126

37

398

314

14

36

30

7

11

36

74

10

54

67

24

133

189

119

47

12

6

33

42

8

28

11

6

4

2

21

3

14

25

72

1,641

17

14

3

7

1

16

25

14

7

17

3

651

163

1,255

451

4,994

390

53

71

7,029

692

27

195

66

96

33

148

189

80

391

46

18

183

1,754

11

63

24

111

24

173

185

165

400

126

37

413

319

14

39

30

1

6

1

5

1

4

5

18

3

4

35

1

4

9

10

1

4

6

11

1

1

3

7

6

6

25

118

4

4

19

)
2
5
(

e
c
n
a
n
F

i

)
2
6
(

e
r
a
c
h
t
l
a
e
H

)
1
5
(

n
o
i
t
a
m
r
o
f
n

I

2

23

1

)
3
3
-
1
3
(

g
n
i
r
u
t
c
a
f
u
n
a
M

e
v
i
t
a
r
t
s
n
m
d
A

i

i

)
6
5
(

)
1
6
(

n
o
i
t
a
c
u
d
E

)
3
2
(

n
o
i
t
c
u
r
t
s
n
o
C

)
1
7
(

i

t
n
e
m
n
a
t
r
e
t
n
E

Malware

Hacking

Social

Misuse

Error

Physical

Environmental

Server

User Dev

Person

Network

Media

Kiosk/Term

Embedded

)
2
2
+
1
2
(

)
1
8
(

i

s
e
c
v
r
e
S
r
e
h
t
O

)
4
5
(

l

i

a
n
o
s
s
e
f
o
r
P

)
2
9
(

c

i
l

b
u
P

l
i

a
t
e
R

)
5
4
-
4
4
(

)
3
5
(

e
t
a
t
s
E

l

a
e
R

)
9
4
-
8
4
(

n
o
i
t
a
t
r
o
p
s
n
a
r
T

0%

25%

50%

75%

100%

s
e
i
t
i
l
i
t
U
+
g
n
n
M

i

i

Figure 52. Incidents by Industry

2020 DBIR   Industry analysis

42

n
r
e
t
t
a
P

n
o
i
t
c
A

t
e
s
s
A

For example, there are 35 total assets
involved in Construction (NAICS 23)
breaches. Of those, multiple assets
may be contained in a single breach,
meaning there are potentially fewer
breaches (25) than our asset count.
Considering how few breaches we
have in this sector, our confidence in
any statistic derived from them will be
relatively low. However, in an attempt
to bring our readers information on
more industries, we have upped our
statistical game. For example, instead
of making a statement such as “64%
of Construction breaches involved a
server,” we would state “between 44%
and 82% of breaches in Construction
involved servers.” This is not an attempt
to be coy,39 we simply want to give
you as much information as possible
without being misleading and, in
industries with such a small sample,
that means using statistical ranges.
You may notice something similar in bar
charts where the black median dot is

removed. Please keep an eye out for
the “Data Analysis Notes” at the bottom
of the Summary table in each section.
We will be pointing out things such as
small sample sizes and other caveats
there. Check out the “Methodology”
section for more information on the
statistical confidence background used
throughout this report.

Another improvement on this year’s
report is that we have standardized
our control recommendations through
a mapping between VERIS and the
CIS Critical Security Controls. Each
industry will have a “Top Controls”
list on their Summary table.
You can find more details about
our mapping in our “CIS Control
recommendations” section.

Please note: Based on
feedback from our readers,
we know that while some
study the report from cover to
cover, others only skip to the
section or industry vertical that
is of direct interest to them.
Therefore, you may notice
that we repeat some of our
definitions and explanations
several times throughout the
report, since the reader who
only looks at a given section
won’t know the definition or
explanation that we might have
already mentioned elsewhere.
Please overlook this
necessary (but possibly
distracting) element.

39  Like a Gameboy.

2020 DBIR   Industry analysis

43

Accommodation
and Food Services

I

S
C
A
N

2
7

Summary

Point of Sale (PoS)-related attacks
no longer dominate breaches in
Accommodation and Food Services
as they have in years past. Instead,
responsibility is spread relatively evenly
among several different action types
such as malware, error and hacking via
stolen credentials. Financially motivated
attackers continue to target this industry
for the payment card data it holds.

Frequency

Top Patterns

Threat Actors

125 incidents,
92 with confirmed
data disclosure

Crimeware, Web
Applications and
Point of Sale represent
61% of data breaches.

External (79%), Internal
(22%), Multiple (2%),
Partner (1%) (breaches)

Actor Motives

Financial (98%),
Secondary (2%)
(breaches)

Data
Compromised

Top Controls

Payment (68%),
Personal (44%),
Credentials (14%),
Other (10%) (breaches)

Limitation and Control
of Network Ports,
Protocols and Services
(CSC 9), Boundary
Defense (CSC 12), Data
Protection (CSC 13)

Breaches served with a smile
The Accommodation and Food Services industry is one that we have been tracking
for quite a while. There’s just something welcoming about it that keeps us coming
back. One lesson that we learned from all our time spent here is that malware plays
a relatively large role in this industry. Crimeware and PoS (both malware dependent)
represent two of the top three patterns this year. These are joined by this year’s
darling of Web applications attacks, which covers both the Use of stolen credentials
and the Exploitation of vulnerabilities, as seen in Figure 53.

Crimeware

Privilege Misuse

Web Applications

Cyber-Espionage

Point of Sale

Lost and Stolen Assets

Everything Else

Denial of Service

Miscellaneous Errors

Payment Card Skimmers

Figure 53. Patterns in Accommodation and Food Services industry breaches (n = 92)

86 the PoS breaches.
We reported last year on the decrease in different attacks targeting the PoS,
either the malware-based remote attacks or the skimmers, and this trend has
continued this year as well (Figure 54). Even though PoS intrusions are still relatively
common, accounting for 16% of breaches in this industry, they are nowhere near
their high-water mark back in 2015. This may be (and probably is) indicative of the
trend of adversaries to more quickly monetize their access in organizations by
deploying ransomware rather than pivoting through the environment and spreading
malware—a more time-costly endeavor.

Do you want malware with that?
In spite of the decline in PoS intrusions, we’re still seeing Crimeware being
leveraged to capture payment card and other types of data at a higher rate than in

2020 DBIR   Industry analysis

44

our overall dataset, accounting for a quarter of the breaches this year. The malware
is found on desktops and servers alike. With regard to type, Figure 55 shows a
decrease of RAM scrapers and an increase of malware that enables access to the
environment, such as Trojans, Backdoors and C2. There is also a continued rise
in Ransomware, which has been known to leverage existing infections to access
the environment. While Ransomware is not the top malware variety in breaches,
or showing up in scans, it should be on your radar.

More than just dollar bills, y’all
This is an industry rich in payment data, and that makes for an easy dollar for bad
guys. But Payment data isn’t the only type of data being compromised. Instead,
we also see Personal data being compromised, often as a byproduct of attacks,
so be sure to pay proper attention to your security program outside of your payment
card environment.

2019

78%

2020

33%

24

18

33

21

DIFF

-44

+24

+16

+15

-11

+7

+5

+5

-4

+3

-2

-2

-2

-1

0

0

0

0

7

7

11

4

10

2

7

0

4

2

5

0

2

0

2

5

7

12

13

2

RAM scraper

Trojan

Backdoor

C2

Spyware/Keylogger

RAT

Password dumper

Ransomware

Worm

Capture stored data

Adminware

Click fraud &
cryptocurrency mining

Export data

Capture app data

Downloader

Figure 55.  Top Malware over time in Accommodation and Food Services industry breaches;
n = 45 (2019), n = 42 (2020)

2020

44%

DIFF

+28

-13

-11

-10

2019

16%

5

18

14

24

Personal

Internal

Payment

Credentials

68

78

Figure 56.  Top compromised data type over time in Accommodation and Food Services
industry breaches; n = 51 (2019), n = 87 (2020)

2020 DBIR   Industry analysis

45

0%25%50%75%201520172019Figure 54. Patterns over time in Accommodation and Food Services industry breachesPoint of SaleArts, Entertainment
and Recreation

S
C
A
N

1
7

I

Summary

Web applications attacks led to many
breaches in this sector. Denial of Service
attacks had higher bits-per-second
volume in this industry than in the
overall dataset. Social engineering
attacks and errors also figure
prominently in this vertical.

Wake up in a good mood and start hacking.
While hackers were once described as being “like an artist,” organizations in this
industry that have been on the receiving end of some of these artistic endeavors
might have a slightly different opinion. Although creativity and novelty are the
hallmarks of this industry, the majority of the breaches in this sector may suffer from
artistic criticisms such as “derivative” or “this has been done before” given that the
top breach patterns are Web Applications, Miscellaneous Errors and Everything
Else (Figure 57).

Frequency

Top Patterns

Threat Actors

Actor Motives

Data
Compromised

Top Controls

194 incidents,
98 with confirmed
data disclosure

Web Applications,
Miscellaneous Errors
and Everything Else
represent 68% of
data breaches.

External (67%), Internal
(33%), Partner (1%),
Multiple (1%) (breaches)

Financial (94%),
Convenience (6%)
(breaches)

Personal (84%),
Medical (31%), Other
(26%), Payment (25%)
(breaches)

Boundary Defense
(CSC 12), Secure
Configurations (CSC 5,
CSC 11), Implement a
Security Awareness
and Training Program
(CSC 17)

Web Applications

Lost and Stolen Assets

Miscellaneous Errors

Point of Sale

Everything Else

Cyber-Espionage

Crimeware

Denial of Service

Privilege Misuse

Payment Card Skimmers

Figure 57. Patterns in Arts and Entertainment industry breaches (n = 98)

2020 DBIR   Industry analysis

46

Fraudulent forgers fool frequently.
Much like how the authenticity of art can be difficult to establish, humans also
struggle with determining the legitimacy of electronic communications. This accounts
for the prevalence of the Everything Else pattern, where social engineering takes the
wheel. In 2019, a Social action was found in approximately 18% of breaches. But to
return to the topic of human nature, accidents and errors such as Misconfigurations
and Misdeliveries remain a common issue for this sector. The growth in accidental
breaches can been seen in Figure 58, where there has been a converging of Internal
and External actors over the last few years. While this rise could be due to changes in
breach reporting, it has remained consistent since 2016.

75%

50%

25%

External

Internal

Untitled Work II
Companies want to be able to maintain their data’s integrity, and cybercriminals
know that. This year, the top Malware varieties (Figure 59) included functionality,
such as “Capture app data.” This and the others listed allow bad actors to steal
quietly into your systems and siphon your data while leaving worms to spread
across your environment and ransomware to lock away your key data. These are
either introduced on web servers via a vulnerability, or on desktops through the
tried and true method of email phishing.

0%

2015

2017

2019

Figure 58. Actors over time in Arts and
Entertainment industry breaches

The DDoS-er
One very interesting result from our research this year was that this industry
experienced the highest rate of DDoS attacks (Figure 60), beating out even the
Information sector—our usual winner—by a wide margin. This NAICS code contains
the online gambling industry as a member, and they are likely the ones driving this
trend. Apparently, DDoSing your business rival is a thing in that realm. Who knew?

Figure 59.  Top Malware variety changes over time in Arts and Entertainment industry
incidents; n = 14 (2015), n = 35 (2020)

Figure 60. Most common BPS in Arts and
Entertainment industry DDoS
(n = 5 organizations); all industries mode
(green line): 565 Mbps

49

29

DIFF

-77

+49

+29

-14

-9

+9

+3

2020

9%

0

0

0

14

14

6

0

9

30

2015

86%

RAM scraper

Ransomware

Capture app data

Export data

C2

Trojan

Other

0 Gbps

10 Gbps

20 Gbps

2020 DBIR   Industry analysis

47

Construction N

S
C
A

I

3
2

Summary

This vertical suffers from Web App
attacks and social engineering, and
the use of stolen credentials remains
a problem. However, it boasts a
low submit rate for phishing and
exhibits a surprisingly low number
of employee errors.

Frequency

Top Patterns

37 incidents,
25 with confirmed
data disclosure

Everything Else,
Web Applications
and Crimeware
represent 95% of
all incidents.

Threat Actors

External (95%), Internal
(5%) (incidents)

Actor Motives

Financial (84%–100%),
Grudge (0% –16%)
(incidents)

Data
Compromised

Personal and
Credentials

Top Controls

Data
Analysis Notes

Secure Configurations
(CSC 5, CSC 11),
Boundary Defense
(CSC 12), Account
Monitoring and
Control (CSC 16)

Actor Motives are
represented by
percentage ranges, as
only 10 breaches had a
known motive. We are
also unable to provide
percentages for Data
Compromised.

Rob the builder
Having delved a bit deeper into our data, we were able to build sections on
several new industries this year, and Construction is among them. Although the
Construction industry may not be the first thing that comes to mind when you think
of data breaches, it is a critical industry that generates a great deal of economic
growth and helps to sustain the nation’s infrastructure. When viewed from that
perspective, one question that may come to mind is, “What motivates the attacks
in this industry?” Most cases were financially motivated and were typically carried
out by organized criminal groups. The majority of these attacks were opportunistic
in nature, which means that the actors who perpetrated them had a very well-
calibrated hammer they knew how to make work, and were just looking for some
unprotected nails.

Since this is the first time we’ve all sat down together at the Construction industry
table, we should take a moment to talk about the top attack patterns from the
Summary table on the left. The Everything Else pattern is basically our bucket
for attacks that do not fit within the other patterns. There are quite a bit of social
engineering attacks in it, and they frequently come in the form of either a pretext
attack (invented scenarios to support the attacker’s hope that the victim will do
what they are asking them to do) or general phishing, for the less industrious
criminal who doesn’t want to expend all that effort. Web Applications attacks are
what they sound like: people hacking into websites to get to the data. Crimeware
is your basic malware attack; ransomware falls in here and is increasingly popular.
While a ransomware attack usually doesn’t result in a data breach, threat actors
have been moving toward taking a copy of the data before triggering the encryption,
and then threatening a breach to try to pressure the victims into
paying up.

How they do that voodoo they do
We mentioned social engineering as a common approach in this industry (and in
the dataset as a whole). The bad guys use this approach simply because it works.
Whether the adversary is trying to convince the victims to enter credentials into
a web page, download some variety of malware or simply wire them some cash,
a certain percentage of your employees will do just that (Figure 61). What is a
proactive security person to do? We’ve talked about how important it is to know
you’re a target—and while the click rate shows that people in this industry fall for the
bait slightly more often than the average Joe, it is important for them to report that
they’ve been targeted. While the submission rate after clicking is quite low for the
sector, so is the reporting rate. You can tell by all the stacked companies at 0% in
the Figure 62 dot plot.

4.5%

Figure 61. Median click rate in Construction industry phishing tests (n = 532); all industries
median (green line): 3.6%

2020 DBIR   Industry analysis

48

For the Web Applications attacks, the most common hacking variety was the use
of stolen credentials. Sometimes these were obtained from a phishing attack, and
sometimes they were just part of the debris field from other breaches. Employees
reusing their credentials for multiple accounts (both professional and personal)
increases risk for organizations when there are breaches and the stolen credentials
are then used for credential stuffing. The key to reducing this risk is to ensure that
the stolen credentials are worthless against your infrastructure by implementing
multifactor authentication methods.

We love our employees.
One thing that really stood out when we looked at this sector was how low the
Internal actor breaches were. Internal actor breaches come in two flavors: Misuse
(malicious intent) and Error (accidental). This sector had very few breaches involving
either, as shown in Figure 63.

External

Internal

Figure 63. Actors in Construction industry
breaches (n = 25)

Report rate

Submit rate

0%

10%

20%

30%

40%

50%

0%

5%

10%

15%

Figure 62. Median rates in Construction industry phishing tests (n = 532)

2020 DBIR   Industry analysis

49

Educational
Services

S
C
A
N

1
6

I

Summary

This industry saw phishing attacks in
28% of breaches and hacking via stolen
credentials in 23% of breaches. In
incident data, Ransomware accounts
for approximately 80% of Malware
infections in this vertical. Educational
Services performed poorly in terms
of reporting phishing attacks, thus
losing critical response time for the
victim organizations.

Frequency

Top Patterns

Threat Actors

Actor Motives

Data
Compromised

Top Controls

819 incidents,
228 with confirmed
data disclosure

Everything Else,
Miscellaneous Errors
and Web Applications
represent 81%
of breaches.

External (67%), Internal
(33%), Partner (1%),
Multiple (1%) (breaches)

Financial (92%),
Fun (5%), Convenience
(3%), Espionage (3%),
Secondary (2%)
(breaches)

Personal (75%),
Credentials (30%),
Other (23%), Internal
(13%) (breaches)

Implement a Security
Awareness and Training
Program (CSC 17),
Boundary Defense
(CSC 12), Secure
Configuration
(CSC 5, CSC 11)

An island of misfit breaches
You may be wondering, “What is this Everything Else pattern that is top of the class
in this sector?” It sounds like the kitchen drawer where all the odds and ends wind
up, and in a way, it is. If an attack doesn’t meet the criteria of one of the other attack
patterns, it ends up here, with that olive pit remover you got from your Secret Santa.

Phishing dominates the Everything Else pattern by a comfortable margin, not unlike
many other industries. However, the Educational Services sector stands out by also
getting a failing grade in phishing reporting practices. Of all industries, according to
our non-incident data, only 24% of organizations had any phishing reporting at all,
and none of them had at least 50% of the emails reported in phishing awareness
campaigns. It is exceedingly important to encourage your user base to let you know
when your organization is being targeted. If they don’t report it, you miss out on your
early warning system.

Similarly, the prevalence of the Web Applications pattern is mostly because of
the use of stolen creds on cloud email accounts. Although we cannot say this is
the organizations’ fault, according to our non-incident data analysis, Educational
Services have the longest40 number of days in a year—28—where they had
credential dumps run against them. The global median here is eight days. The
overall number of credentials attempted is also one of the highest of all industries
we analyzed for this year’s report (Figure 64).

0

50M

100M

Figure 64. Credential stuffing attempts in Education industry web blocks (n = 8); all industries
mode (green line): 1.11 M

40 Mode of industry

2020 DBIR   Industry analysis

50

Outside of those two patterns, sadly, the news is still not great. Ransomware is
really taking hold of Education vertical incidents, and has been responsible for
80% of the Malware-related incidents, up from 48% last year (Figure 65). All of
those Ransomware cases have also played a role in the increase we have seen in
financially motivated incidents for the past two years.

One additional concern in this sector is the fact that, according to our analysis, this
is the only industry where malware distribution to victims was more common via
websites than email. This information doesn’t really seem to make sense until you
consider malware being distributed via unmonitored email (such as personal mail
accounts from students on bring-your-own devices connected to shared networks),
and all of those infections obviously endanger the larger organization.

Ransomware

Backdoor

Downloader

Capture app data

Other

C2

Capture stored data

Scan network

Figure 65. Top Malware varieties in Education industry incidents (n = 129)

2020 DBIR   Industry analysis

51

Financial
and Insurance

I

S
C
A
N

2
5

Summary

The attacks in this sector are perpetrated
by external actors who are financially
motivated to get easily monetized
data (63%), internal financially
motivated actors (18%) and internal
actors committing errors (9%). Web
Applications attacks that leverage the
Use of stolen credentials also continue
to affect this industry. Internal- actor-
caused breaches have shifted from
malicious actions to benign errors,
although both are still damaging.

Frequency

Top Patterns

Threat Actors

Actor Motives

Data
Compromised

Top Controls

1,509 incidents,
448 with confirmed
data disclosure

Web Applications,
Miscellaneous Errors
and Everything Else
represent 81%
of breaches.

External (64%), Internal
(35%), Partner (2%),
Multiple (1%) (breaches)

Financial (91%),
Espionage (3%),
Grudge (3%) (breaches)

Personal (77%),
Other (35%),
Credentials (35%),
Bank (32%) (breaches)

Implement a Security
Awareness and Training
Program (CSC 17),
Boundary Defense
(CSC 12), Secure
Configurations
(CSC 5, CSC 11)

Why is everybody always picking on me?
The Financial and Insurance sector has always had a target on its back due to the
kinds of data it collects from its customers. The data shows that the sector remains
a favorite playground for the financially motivated organized criminal element again
this year. Web Applications attacks are in competition with the Miscellaneous
Errors pattern for the top cause of most breaches, as shown in Figure 66. It is a
bit disturbing when you realize that your employees’ mistakes account for roughly
the same number of breaches as external parties who are actively attacking you.
Apparently, it really is hard to get good help these days, and you can take that to
the bank.

The Misuse action was among the top three causes of breaches for this vertical in
last year’s report, but it dropped from 21.7% in the 2019 report to only 8% this year.
While this pattern saw a decline in our overall dataset, we are not of the opinion that
all employees have suddenly become virtuous with regard to abusing their access.
It is more likely that this is simply reflective of a change in contributor visibility rather
than a sign of extreme moral rectitude in the workforce.

We switch our focus from malicious actions to those that were unintentional in
Figure 67. The most common Error was Misdelivery, which is pretty much exactly
what it sounds like: sending information to the wrong person. This can be with
electronic data, such as an email sent to the incorrect recipient by an autofill in the
“To:” field. Or it can be paper documents, such as a mass mailing that is incorrectly
addressed. Both can result in a large breach, depending on what file(s) were
attached to the email, or how large the mass mailing was.

Web Applications

Payment Card Skimmers

Miscellaneous Errors

Lost and Stolen Assets

Everything Else

Cyber-Espionage

Privilege Misuse

Denial of Service

Crimeware

Point of Sale

Figure 66. Patterns in Finance and Insurance industry breaches (n = 448)

2020 DBIR   Industry analysis

52

Figure 67. Top Error varieties in Finance and Insurance industry breaches (n = 109)

Misdelivery

Publishing error

Misconfiguration

Programming error

Other

Disposal error

#somefilter

As stated in past versions of this report,
we utilize filters in our data analysis for a
variety of things, including focusing on a
given industry, threat actor type, etc. We
also use them to exclude certain subsets
of data in order to reduce skew and to
help us find trends that might otherwise
be missed. However, we do not ignore
this data; we analyze it separately in
other sections of this report. You can
read more about it in our “Incident
classification patterns and subsets”
section. Specifically, for Finance, there
were tens of thousands of incidents on
the Botnet subset analyzed separately.

The second most common Error is one that has been experiencing a surge in
popularity—the Misconfiguration. This occurs when someone (often a system
administrator) fails to secure a cloud storage bucket or misconfigures firewall
settings. In the case of both Misdelivery and Misconfiguration, the motivation was
overwhelmingly carelessness. Good security practices? Ain’t nobody got time
for that.

The wallflowers of the breach world
Like the shy creatures that line the walls of the middle school dance, those attacks
that are shy in providing sufficient detail end up in the Everything Else pattern. Here
languish the average, yet successful, phishing attacks, and the increasingly common
business email compromise in its various forms. Among its many incarnations is the
phishing email masquerading as coming from someone in the executive level of the
company asking for something of monetary value.

Phishing

Pretexting

Scam

Figure 68. Social varieties in Finance and
Insurance industry breaches (n = 86)

Keep on playing those mind games together.
We also see invented scenarios (Pretexting) manufactured in order to plausibly
convince the target to transfer money to the attacker’s bank account. Figures
68 and 69 illustrate the popularity of these common social attacks. One key
takeaway is that the weakest link in many organizations is their staff. Is it likely that
the average user (who was targeted based on their access to data) will challenge
a request that appears to be coming from someone who has the authority to fire
them? Our Magic 8-Ball data indicates that signs point to no.

The majority of attacks in this sector are perpetrated by external actors who
are financially motivated to access easily monetized data stored by the victim
organizations. While there remains a small amount of Cyber-Espionage by nation-
state actors in this industry, most attacks are perpetrated by someone who is all
about the shekels.

Email

Phone

Website

Documents

2020 DBIR   Industry analysis

53

Figure 69. Social vectors in Finance and
Insurance industry breaches (n = 86)

Healthcare

I

S
C
A
N

2
6

Summary

Financially motivated criminal groups
continue to target this industry via
ransomware attacks. Lost and stolen
assets also remain a problem in our
incident dataset. Basic human error
is alive and well in this vertical.
Misdelivery grabbed the top spot
among Error action types, while internal
Misuse has decreased.

Frequency

Top Patterns

Threat Actors

Actor Motives

Data
Compromised

Top Controls

798 incidents,
521 with confirmed
data disclosure

Miscellaneous Errors,
Web Applications
and Everything Else
represent 72%
of breaches.

External (51%), Internal
(48%), Partner (2%),
Multiple (1%) (breaches)

Financial (88%),
Fun (4%), Convenience
(3%) (breaches)

Personal (77%),
Medical (67%), Other
(18%), Credentials
(18%) (breaches)

Implement a Security
Awareness and
Training Program
(CSC 17), Boundary
Defense (CSC 12),
Data Protection
(CSC 13)

As contributors come and go, our dataset will change, and that
change will be visible in both the types of attacks and the overall
number of breaches we include in this report.

This year, we saw a substantial increase in the number of breaches and incidents
reported in our overall dataset, and that rise is reflected within the Healthcare
vertical. In fact, the number of confirmed data breaches in this sector came in
at 521 versus the 304 in last year’s report. Since this is the Data Breach
Investigations Report, we tend to put more focus on actual confirmed breaches.
But in Healthcare, given the Department of Health and Human Services’ (HHS)
guidance on ransomware cases for example,41 the incidents hold higher relevance
than they might in a different vertical despite the data being simply “at-risk” rather
than a confirmed compromise.

Figure 70 shows the breakdown of the patterns for incidents in Healthcare. The
Crimeware pattern includes Ransomware incidents, and as one might expect,
that pattern accounts for a large portion of the incidents in this sector. If we drop
further down the list in this chart, we see that one pattern that tends to get lost in
the shuffle is Lost and Stolen Assets. Because the asset is not available, proving
whether the data was accessed or not is no simple matter. Therefore, we code
these as incidents with data being “at-risk” rather than as a confirmed compromise.
Our caution to the reader is not to assume that because the attacks aren’t showing
up as confirmed breaches in our dataset, you won’t have to declare a breach
according to the rules that govern your industry.

Crimeware

Lost and Stolen Assets

Miscellaneous Errors

Cyber-Espionage

Everything Else

Denial of Service

Web Applications

Payment Card Skimmers

Privilege Misuse

Point of Sale

Figure 70. Patterns in Healthcare industry incidents (n = 798)

41  “The presence of ransomware (or any malware) on a covered entity’s or business associate’s computer systems is a security incident under the HIPAA Security Rule.”

https://www.hhs.gov/sites/default/files/RansomwareFactSheet.pdf

2020 DBIR   Industry analysis

54

Miscellaneous Errors

Web Applications

Everything Else

Privilege Misuse

Lost and Stolen Assets

Crimeware

Cyber-Espionage

Denial of Service

Payment Card Skimmers

Point of Sale

Figure 71. Patterns in Healthcare industry
breaches (n = 521)

Take three patterns and call me in the morning.
If you’ve been following the “Healthcare” section for some time, you may notice a
big change in the breach pattern rankings on Figure 71. This is the first year that
the Privilege Misuse pattern is not in the top three. However, this pattern saw a
significant proportional drop in our dataset overall—not just in the Healthcare
vertical. In the 2019 report, we showed Privilege Misuse at 23% of attacks, while
in 2020, it has dropped to just 8.7%. Does that indicate that insiders are no longer
committing malicious actions with the access granted to them to accomplish their
jobs? Well, we wouldn’t go quite that far. However, it will be interesting to see if this
continues as a trend when next year’s data comes in.

Another change that goes along with decreased insider misuse breaches is the
corresponding drop in multiple actor breaches. The Healthcare sector has typically
been the leader in this type of breach—which usually occurs when External and
Internal actors combine forces to abscond with data that is then used for financial
fraud. The multiple actor breaches last year were at 4% and this year we see a drop
to 1%. The 2019 DBIR reported a first in that the Healthcare vertical had Internal
actor breaches (59%) exceeding those perpetrated by External actors (42%). This
year, External actor breaches are slightly more common at 51%, while breaches
perpetrated by Internal actors fall to 48%. However, this is a small percentage and
Healthcare remains the industry with the highest amount of internal bad actors.

As with many things in life, as one attack grows more prevalent, others begin
to decrease. So the story goes with the Miscellaneous Errors pattern. While it
has frequently graced the top three patterns in this sector, it took the gold this
year. In case you are curious, the top mistake within Healthcare is our old friend,
Misdelivery.

This Error tends to fall into two major categories:

•  Someone is sending an email and addresses it to the wrong (and frequently
wider) distribution—it’s an added bonus if a file containing sensitive data
was attached

•  An organization is sending out a mass mailing (paper documents) and the

envelopes with the addresses become out of sync with the contents of the
envelope. If sampling is not done periodically throughout the mailing process
to ensure that they remain *NSYNC, then it’s bye, bye, bye to your patients’
sensitive information

2020 DBIR   Industry analysis

55

When thinking of the Healthcare vertical, one naturally thinks of Medical data. And,
unsurprisingly, this is the industry in which that type of data is the most commonly
breached. However, we also see quite a lot of both Personal data (which can be
anything from basic demographic information to other covered data elements)
and Credentials stolen in these attacks. The second most common pattern for
Healthcare is the Web Applications attack. As more and more organizations open
patient portals and create new and innovative ways of interacting with their patients,
they create additional lucrative attack surfaces.

Finally, we see a good deal of the Everything Else pattern, which is not unlike a lost
and found for attacks that do not fit the criteria of any other attack pattern. It is
within this pattern that the business email compromise resides. If you’re not
familiar with this attack, it is typically a phishing attack with the aim of leveraging a
pretext (an invented scenario to give a reason for the victim to do what the attacker
wants) to successfully transfer money (by wire transfer, gift cards or any other
means). Although these are common attack types across the dataset, it is a good
reminder to Healthcare organizations that it isn’t only patient medical data that is
being targeted.

When did you first notice these symptoms?
The time required to compromise and exfiltrate data has been getting smaller in
our overall dataset. Unfortunately, the time required for an organization to notice
that they have been breached is not keeping pace. There is a discrepancy there
somewhat akin to how long it takes you to earn your wages vs how long it takes
for them to be taxed. Some attacks, by their very nature, will both happen quickly
and be detected quickly. A good example is a stolen laptop—how long does it take
someone to smash a car window and make off with the loot? (That is a rhetorical
question, so don’t mail in answers, there is no prize for getting it right.) Likewise, it
also doesn’t take much time for the owner to come back to their car and see the
break-in.

Both of these will have a short duration due to the nature of the crime. In contrast,
an insider who has decided to abuse their access to copy a small amount of data
each week and sell it to their buddy, who in turn utilizes it for financial fraud, may not
be caught for a very long time.

2020 DBIR   Industry analysis

56

Information

I

S
C
A
N

1
5

Summary

Web App attacks via vulnerability
exploits and the Use of stolen
credentials are prevalent in this industry.
Errors continue to be a significant
factor and are primarily made up of the
Misconfiguration of cloud databases.
Growth in Denial of Service attacks
also remains a problem for the
Information sector.

Frequency

Top Patterns

Threat Actors

Actor Motives

Data
Compromised

Top Controls

5,741 incidents,
360 with confirmed
data disclosure

Web Applications,
Miscellaneous Errors
and Everything Else
represent 88% of
data breaches.

External (67%), Internal
(34%), Multiple (2%),
Partner (1%) (breaches)

Financial (88%),
Espionage (7%),
Fun (2%), Grudge (2%),
Other (1%) (breaches)

Personal (69%),
Credentials (41%),
Other (34%), Internal
(16%) (breaches)

Secure Configurations
(CSC 5, CSC 11),
Continuous Vulnerability
Management (CSC 3),
Implement a Security
Awareness and Training
Program (CSC 17)

Come one, come all!
Welcome to the Information industry portion of the DBIR, and boy are you in for
a treat! This section has it all: web applications attacks, errors, phishing and even
some malware. The main three patterns witnessed in the NAICS 51 sector for 2019
were Web Applications with over 40% of breaches, followed by Miscellaneous
Errors and, at a distant third, Everything Else (Figure 72).

Figure 72. Patterns in Information industry breaches (n = 360)

Web Applications

Privilege Misuse

Miscellaneous Errors

Lost and Stolen Assets

Everything Else

Denial of Service

Crimeware

Payment Card Skimmers

Cyber-Espionage

Point of Sale

Since 2019, Web Applications attacks have increased significantly, both in terms of
percentage and in raw number of breaches.. This is one that organizations in this
industry should keep an eye out for, as adversaries are dividing their effort equally
between utilizing web exploits and stolen credentials to gain access to your web
applications. Considering this vertical has a high dependence on external services
and the internet, one shouldn’t be too shocked to learn that this industry has a
higher percentage of web application exploitations than other industries. However,
based on our non-incident data, Information also has one of
the highest percentages of vulnerability patching completed on time (Figure 73).

An anthem to errors
Errors are everywhere and the technical wizards that run our information
infrastructure are not immune. This is why Errors are the second most common type
of breach, maintaining relatively similar levels to previous years (this is not an area
where consistency is a good thing). Misconfigurations are by far the most common
type of errors, and largely relate to databases or file storages not being secured
and directly exposed on a cloud service. These are the types of incidents that you
hear security researchers discovering through simple trawling of the internet to see
what’s exposed. The optimist in us hopes that as these new technologies become
more commonly used, people will stop (or at least slow down) making these types of
mistakes. On the other hand, the realist in us wouldn’t put any money on it.

2020 DBIR   Industry analysis

57

You, sir, are a phish.
Technical issues are not the only thing impacting this technology-based sector.
Organizations in this vertical have fallen prey to the same type of social engineering
attacks that affect everyone else. Most of these attacks fall into our Everything Else
pattern and account for 16% of the breaches we saw in 2019. In terms of social
attacks, there is a relatively even split between phishing and pretexting (the bad
guy just asks for information via email or uses some existing conversation in order
to make a more convincing request). One of the common techniques we’ve seen is
the use of typo-squatted domains of partners that are used to send existing email
threads or request an update to a bank account.

Fast speeds and full bandwidths
Big interweb pipes are a key part of this industry since consumers demand that
videos load fast and website content gets updated at the speed of an unladen
European swallow. Unfortunately, cybercriminals know how important that is, and
have been persistently targeting this industry with DoS attacks to disrupt their
services and capabilities. The 2019 data showed continued growth in terms of the
percentage of DDoS incidents (Figure 74). Not only does this industry get targeted
more than a red barrel in a first-person shooter, they’re also facing attacks with
the second highest median BPS—meaning these attacks tend to pack a punch.
Unfortunately for many companies, these attacks often need a helping hand to
mitigate, so it helps to have a Player 2 in your corner.

Figure 73. Patching in Information industry
vulnerabilities (n = 36,255)

Information:
AUC: 82%
COT: 89%

Overall:
AUC: 44%
COT: 57%

100%

75%

50%

25%

d
e
h
c
t
a
p
t
n
e
c
r
e
P

0

25

50

75

Days since discovery

80%

60%

40%

20%

0%

2015

Denial
of Service

2017

2019

Figure 74. Patterns over time in Information industry incidents

2020 DBIR   Industry analysis

58

Manufacturing N

S
C
A

I

3
3
–
1
3

Summary

Manufacturing is beset by external
actors using password dumper malware
and stolen credentials to hack into
systems and steal data. While the
majority of attacks are financially
motivated, there was a respectable
showing of Cyber-Espionage-motivated
attacks in this industry as well. Internal
employees misusing their access
to abscond with data also remains a
concern for this vertical.

Frequency

Top Patterns

Threat Actors

Actor Motives

Data
Compromised

Top Controls

922 incidents,
381 with confirmed
data disclosure.

Crimeware, Web
Applications and
Privilege Misuse
represent 64%
of breaches.

External (75%),
Internal (25%), Partner
(1%) (breaches)

Financial (73%),
Espionage (27%)
(breaches)

Credentials (55%),
Personal (49%), Other
(25%), Payment (20%)
(breaches)

Boundary Defense
(CSC 12), Implement a
Security Awareness
and Training Program
(CSC 17), Data
Protection (CSC 13)

Bad actors, bad actions, bad puns
It has been said that the proper study of mankind is Man(ufacturing), or at least we
are pretty sure that is how the adage goes. We hope so at least, because we have
been giving a lot of thought to that topic. The Manufacturing vertical is very well
represented this year with regard to both incidents and breaches. As always when
we see a large increase, it could be indicative of a trend or simply a reflection of our
caseload. In this instance, it is certainly the latter.

However, NAICS 31–33 has long been a much-coveted target of cybercrime and
this year is no exception. Whether it is a nation-state trying to determine what its
adversary is doing (and then replicate it) or just a member of a startup who wants to
get a leg up on the competition, there is a great deal of valuable data for attackers
to steal in this industry. And steal it they do. The predominant means they employ
for this theft falls under the Crimeware pattern, as shown in Figure 75. Namely, the
Password dumper, Capture app data and Downloader varieties.

This combination of obtain password, infiltrate network, download software and
then capture data paints a very clear picture of what’s going on in this vertical, but
it may not be a picture you want hanging on your wall if you do business in this area.
But while we are on the topic of malware in general, keep in mind that ransomware
(while not considered a breach in this report) is still a very present danger for this
industry at 23% of all malware found in incidents.

Crimeware

Everything Else

Web Applications

Lost and Stolen Assets

Privilege Misuse

Point of Sale

Miscellaneous Errors

Payment Card Skimmers

Cyber-Espionage

Denial of Service

Figure 75. Patterns in Manufacturing industry breaches (n = 381)

2020 DBIR   Industry analysis

59

Figure 76. Hacking varieties in
Manufacturing industry breaches (n = 44)

Use of stolen creds

Exploit vuln

Brute force

Abuse of functionality

Use of backdoor or C2

XSS

Footprinting

Web Applications attacks took the number-two place this year and are dominated
by the Use of the stolen credentials to compromise a variety of web apps used in
enterprises. Sometimes these credentials are obtained via malicious links served
up in successful phishing attacks, sometimes they are obtained via desktop sharing
and sometimes it is unclear how the victim is infected. Regardless of how they are
compromised, these credentials, often of the cloud-based email variety, are very
successful as a means to an end in this vertical, as you can see in Figure 76.

There are several patterns that are closely grouped around the third-place position
for Manufacturing: Misuse (13%), which by definition involves insiders, and is mostly
Privilege abuse—the actor has legitimate access but they use those privileges to do
something nefarious—and Data mishandling, of which prime examples are sending
company data via personal email or placing it on cloud drives in order to work from
home (Figure 77).

Error is ubiquitous in all of the verticals this year, and in Manufacturing it is in
keeping with the trend of Misdelivery and Misconfiguration that we see in other
industries. Finally, we would be remiss to not say a word or two regarding cyber-
espionage-related attacks.

Figure 77. Misuse varieties in Manufacturing industry breaches (n = 49)

Privilege abuse

Snap picture

Data mishandling

Possession abuse

Unapproved hardware

2020 DBIR   Industry analysis

60

As a glance at Figures 78 and 79 reveals, 38% of actors were of the Nation-state
variety, and 28% of breaches were motivated by Espionage. As we have mentioned
in previous reports, it is cheaper and simpler to steal something than to design it
yourself. And while large organizations are often willing to outsource their help-desk
functions, they are, as a rule, not as eager to ship off their intellectual property and
research-and-design generation to foreign locales.

Figure 78. External actor varieties in
Manufacturing industry breaches (n = 83)

Figure 79. External actor motives in
Manufacturing industry breaches (n = 121)

Organized crime

Financial

Nation-state

Espionage

Unaffiliated

State-affiliated

Former employee

2020 DBIR   Industry analysis

61

Mining, Quarrying,
and Oil & Gas
Extraction + Utilities N

S
C
A

I

2
2
+
1
2

Summary

Breaches are composed of a variety
of actions, but Social attacks such as
Phishing and Pretexting dominate
incident data (no confirmation of data
disclosure). Cyber-Espionage-motivated
attacks and incidents involving OT assets
are also concerns for these industries.

It's an NAICS mashup!
This new section combines the Mining, Quarrying, and Oil and Gas Extraction
(NAICS 21) with the Utilities (NAICS 22) industries for a joint view of the incidents
and breaches that affected them. We really dug deep, but we were unable to strike
oil for an exclusive section for NAICS 21 on this year’s report. (There must be a
minimum number of incidents for the statistics to be valid.) However, we believe that
this blended section with NAICS 22 will be an electrifying read and hopefully not
too dry.

Frequency

Top Patterns

Threat Actors

Actor Motives

Data
Compromised

Top Controls

Data
Analysis Notes

194 incidents,
43 with confirmed
data disclosure

Everything Else,
Web Applications
and Cyber-Espionage
represent 74%
of breaches.

External (75%),
Internal (28%), Multiple
(2%) (breaches)

Financial (63%–95%),
Espionage (8%–43%),
Convenience/Other/
Secondary (0%–17%
each), Fear/Fun/
Grudge/Ideology
(0%–9% each)
(breaches)

Credentials (41%),
Personal (41%),
Other (35%), Internal
(19%) (breaches)

Secure Configurations
(CSC 5, CSC 11),
Boundary Defense
(CSC 12), Implement a
Security Awareness
and Training Program
(CSC 17)

Actor motives are
represented by
percentage ranges,
as only 21 breaches
had a known motive.

If you review Figure 80, you can see that while Everything Else, Web Applications
and Cyber-Espionage seem to be the top three patterns in breaches, it is
statistically impossible to tell which one is more prevalent—they simply overlap too
much. It’s exciting to have such a diversity of breaches in a brand-new industry
section, but it also makes it difficult to focus on precise recommendations beyond
“Note to all CISOs: Secure all the things!”

Even so, it is important to point out that the Everything Else pattern, both in
incidents and breaches, is dominated by Phishing with mostly financial gain as a
motive, including pretexting attacks that were clearly FMSEs.

Everything Else

Crimeware

Web Applications

Lost and Stolen Assets

Cyber-Espionage

Denial of Service

Miscellaneous Errors

Payment Card Skimmers

Privilege Misuse

Point of Sale

Figure 80. Patterns in Mining and Utilities industry breaches (n = 43)

2020 DBIR   Industry analysis

62

If I closed my eyes, was it still a breach?
Since the Everything Else pattern is the largest for incidents (cases in which
there was potential data disclosure but it was not confirmed), special attention is
needed here. There were about as many incidents with potential data disclosure
as there were confirmed breaches in these industries. This is especially concerning
for a vertical with a broad range of possible percentages for Espionage-motivated
breaches (between 8% and 43%), while in all incidents it accounts for 10% of
the motives.

Wrapping up the top patterns, Web Applications is filled with the Use of stolen
creds that were gathered by Phishing. Meanwhile, Miscellaneous Errors favors
Misconfiguration and Publishing Errors, both action varieties that can be mitigated
with stronger processes and personnel training.

Unpatched vulnerabilities in your web application infrastructure may lead to them
being found by someone with a set of tools to exploit them in an automated fashion.
Keeping your infrastructure patches up to date is certainly a security best practice.
In looking at our non-incident data surrounding time to patch (Figure 81), we found
the Utilities sector had a better-than-average score. This is good news because our
research has found that the patches that do not get applied within the first quarter
of being released frequently don’t get applied at all. This gives the adversaries time
to build tools that will make it easy even for a novice to attack the infrastructure that
remains vulnerable.

Also, as these industries have become a focus of our reporting, we have added
OT-specific fields to track incidents involving OT equipment in the latest version of
VERIS. The total number of cases we have for this year are few, but they are mainly
concerned with this sector along with Manufacturing (NAICS 31–33).

Figure 81. Patching in Mining and Utilities
industry vulnerabilities (n = 151,658)

100%

75%

50%

25%

d
e
h
c
t
a
p
t
n
e
c
r
e
P

Utilities:
AUC: 79%
COT: 81%

Overall:
AUC: 44%
COT: 57%

0

25

50

75

Days since discovery

2020 DBIR   Industry analysis

63

Other Services

I

S
C
A
N

1
8

Summary

Financial gain is the highest motive for
External actors, with Web Applications
being 39% of breaches. Error among
employees is another issue for this
sector, particularly with regard to
Misconfiguration and Misdelivery. While
Credentials are a desirable target, it is
Personal data that is most frequently
stolen here.

Frequency

Top Patterns

Threat Actors

Actor Motives

Data
Compromised

Top Controls

Data
Analysis Notes

107 incidents,
66 with confirmed
data disclosure

Web Applications,
Miscellaneous
Errors and Everything
Else represent 83%
of breaches.

External (68%),
Internal (33%), Multiple
(2%) (breaches)

Financial (60%–98%),
Espionage (0%–28%),
Convenience/Fear/
Fun/Grudge/Other/
Secondary (0%–15%
each) (breaches)

Personal (81%), Other
(42%), Credentials
(36%), Internal (25%)
(breaches)

Boundary Defense
(CSC 12), Implement a
Security Awareness
and Training Program
(CSC 17), Secure
Configurations
(CSC 5, CSC 11)

Actor Motives are
represented by
percentage ranges, as
only 12 breaches had a
known motive. Some
charts also do not have
enough observations
to have their expected
value shown.

Break on through to the other side.
The Other Services (NAICS 81) industry is also new to the report this year. This
NAICS code is one of several that are surprisingly broad, covering everything
from various personal and repair services to non-profit religious and social
benefit organizations. Oddly enough, it even includes a subcode (814) for private
households, but those are not represented in this dataset. For an incident to be
eligible for inclusion in the DBIR, there must be a victim organization, since that is
where the laws focus, and where the controls are most likely to have good effect.
As we have mentioned in the other new sections, while this is the first year we
are including this industry in the report, we have data going back a few years on
this sector.

Jockeying for that top spot
The top breach patterns in this industry were Web Applications attacks,
Miscellaneous Errors and Everything Else. When looking at the incident patterns (not
confirmed data breaches), the patterns remain the same, albeit in a different order.

The main change from last year’s data for this vertical is the drop in the Cyber-
Espionage pattern. Last year it held the first place slot in the footrace, and you can
see from Figure 82 that is has since told the other patterns “go on ahead, I’ll catch
up” as it struggles to catch its breath. Consistent with this change, we’ve seen the
variety and motivation of the External actor breaches transform from State-affiliated/
Espionage into Organized crime/Financial. It seems the people who like to go after
data for the sheer joy of monetizing it have found a friend in this sector.

Web Applications

Privilege Misuse

Miscellaneous Errors

Cyber-Espionage

Everything Else

Denial of Service

Crimeware

Payment Card Skimmers

Lost and Stolen Assets

Point of Sale

Figure 82. Patterns in Other Services industry breaches (n = 66)

2020 DBIR   Industry analysis

64

Figure 83. Top Error varieties in Other
Services industry breaches (n = 21)

Misconfiguration

Misdelivery

Other

Figure 84. Top Social varieties in Other
Services industry breaches (n = 12)

Other

Phishing

Pretexting

The Web Applications attack pattern includes the Hacking actions, and the favored
action variety tends to be the Use of stolen credentials. It makes sense—who
wouldn’t like credentials when trying to break into some else’s computer? What
burglar would say no to a set of free keys? And while the use of a backdoor or
Command and Control (C2) infrastructure is always nice, if you can just waltz in
the front door, why exert yourself? Do you enjoy being asked questions?

What can go wrong will happen to me.
The Miscellaneous Errors pattern is all about the mistakes your employees
make. Two stand out from the rest in the field of errors for Other Services:
Misconfiguration and Misdelivery (Figure 83). Misconfiguration errors are the
frenemies of Information Security. These breaches are caused by Internal actors
(frequently a system admin or DBA, as they have access to large amounts of data)
doing things such as standing up an instance of the data on a cloud platform, but
neglecting to put in any security controls to limit access. Once that happens, it is
a matter of time before the intrepid security researchers out there find it via their
search tools and someone gets a call.

Misdelivery—when sensitive data goes to the wrong recipient(s)—is the other most
common Error in this sector. A good example is when the autocomplete in an email
“To:” or “Cc:” field occurs and directs to the incorrect party. In other instances, it
is the mass-mailing misstep where the addresses are no longer paired with the
correct contents. It is never good to have your customer open a letter only to find
someone else’s Personally Identifiable Information (PII) inside.

Finally, we have the Everything Else pattern, which is our version of potpourri.
This is where the attacks that do not meet the criteria of the other patterns end
up. Not exactly the fragrant flowers of the security breach world, these attacks
are frequently made up of phishing attacks in which not a great deal of detail
was provided.

The business email compromises also live within this pattern. They typically come
in two main flavors: the pretext and the C-level impersonation. For the pretext, there
is an invented scenario and usually an attempt to get either an invoice paid or a
direct wire transfer to an adversary-controlled bank account. They may compromise
the mail account of the executive and wait until the person is traveling to elevate
the sense of urgency, and to minimize the ability to contact the person in order to
verify the legitimacy of the request. The latter type is when the actor pretends to be
a member of the executive suite, but they ask for data rather than a wire transfer.
Figure 84 illustrates that phishing and pretexting are still thriving in this vertical.
Both of these social engineering actions typically arrive via email.

2020 DBIR   Industry analysis

65

Professional,
Scientific and
Technical Services

I

S
C
A
N

4
5

Summary

Financially motivated attackers continue
to steal credentials and leverage them
against web application infrastructure.
Social engineering in the form of
Phishing and Pretexting is a common
tactic used to gain access. This industry
also suffers from Denial of Service
attacks regularly.

Frequency

Top Patterns

Threat Actors

Actor Motives

Data
Compromised

Top Controls

7,463 incidents,
326 with confirmed
data disclosure

Web Applications,
Everything Else and
Miscellaneous Errors
represent 79%
of breaches.

External (75%),
Internal (22%),
Partner (3%), Multiple
(1%) (breaches)

Financial (93%),
Espionage (8%),
Ideology (1%)
(breaches)

Personal (75%),
Credentials (45%),
Other (32%), Internal
(27%) (breaches)

Secure Configuration
(CSC 5, CSC 11),
Implement a Security
Awareness and
Training Program
(CSC 17), Boundary
Defense (CSC 12)

This industry is made up of a wide range of companies primarily offering service
directly to customers. They range from lawyers, accountants and architects to
research labs and consulting firms. They share some common traits: Their internet
presence is very important to the livelihood of the organization, and their employees
are human and make mistakes.

We mentioned the importance of their internet presence to the members of this
industry. This is why the Web Applications attack pattern was seen so frequently
this year (Figure 85). These attacks are driven by the use of stolen credentials
(frequently obtained in phishing attacks, but also may be laying around on the web
from another company’s breach, just waiting for some enterprising hacker to find).
These attacks drive the theft of personal data in the sector, and given that there are
always people willing to try their luck at using stolen credentials against whatever
web infrastructure they encounter, are unlikely to end anytime in the near future.

Web Applications

Privilege Misuse

Everything Else

Cyber-Espionage

Miscellaneous Errors

Point of Sale

Crimeware

Denial of Service

Lost and Stolen Assets

Payment Card Skimmers

Figure 85. Patterns in Professional Services industry breaches (n = 326)

2020 DBIR   Industry analysis

66

I feel attacked.
Why would organizations in this sector be targets of attacks? You have heard
the expression “Location, location, location”? This sector is the location of lots of
useful personal data (in fact, apart from Credentials, Personal information is the
most targeted data type in these breaches). This isn’t necessarily an industry full
of financial information or payment card records, but personal information can be
quite lucrative for a number of different kinds of financial fraud, hence the attraction.
Figure 86 shows the continued growth of Financially motivated breaches at the
expense of Espionage (and even Errors).

The Everything Else pattern is our scrap bin of unwanted attacks—if they do not
fit the criteria of the other patterns, they end up here. They are largely low-detail
phishing attacks, but sometimes the social engineering perpetrator puts a bit of
actual effort into their work and invents a likely scenario to entice their prey. If you’re
familiar with the business email compromise, this is where that lives. Professional
Services is middle of the road when it comes to being on the receiving end of
phishing attacks. But this attack isn’t just about receiving the attack—it is about
whether the victim clicks, and if they submit their data. It is also about whether they
raise a flag with their internal security people to let them know “what they done did.”

The news about phishing in this sector is a bit of a mixed bag. In Figure 87, we see
that click rate is right on the overall median. You can also see in Figure 88 that
submit rates are low (notice the large stack of companies on the 0% of the right
chart—Submit rate), which is the good news—you want the number of people giving
out their credentials to be low. Sadly, the bad news is that the reporting rate is low
as well (there is also a large stack of companies on the 0% of Report rate), meaning
that your people are not telling you they’ve fallen victim to a phish. That second
measure—the Report rate—is critical so that the organization’s security response
team can mitigate the effects of the breach.

60%

40%

20%

Financial

Error

Espionage

0%

2015

2017

2019

Figure 86. Motives over time in Professional
Services industry breaches

3.5%

Figure 87. Median click rate in Professional
Services industry phishing tests; all
industries median (green line): 3.6%

Report rate

Submit rate

0%

20%

40%

60%

0%

5%

10%

15%

Figure 88. Median rates in Professional Services industry phishing tests (n = 2,583)

2020 DBIR   Industry analysis

67

Misconfiguration

Misdelivery

Loss

Programming error

Publishing error

Physical accidents

Other

Gaffe

Disposal error

Figure 89. Error varieties in Professional
Services industry breaches (n = 67)

I should not have done that.
Miscellaneous Errors figure prominently in this industry, but really any industry is
susceptible to their employees’ mishaps causing a breach. Figure 89 shows the
errors that are on top in this industry—namely Misconfiguration, Misdelivery and
Loss. Misconfiguration has become increasingly reported, primarily because there
are people out there actively looking for this type of breach. This happens when
someone drops some of their data into a cloud database instance but fails to put
any protective measures in place. We mentioned people are actively searching for
this, right? Yeah, then hilarity ensues—not really.

Misdelivery is frequently via paper documents in the mail, when person A gets
person B’s paperwork, but it can also happen via email when people are careless
about addressing emails and what they attach. Loss is a bit of a different animal.
When the item lost is electronic, like a laptop, this would not be counted as a breach
in our dataset. For it to be counted, there must be a confirmed compromise of the
confidentiality aspect of the data—and confirming access is difficult when you don’t
have the asset anymore. While the Loss error appears in our dataset, it is most
frequently an incident, not a breach. However, here it is a breach, so what gives?
Well, it would have to be an asset that is in human-readable format, like paper
documents. We count them as a breach since there are no protections at all on
printed matter. This is why people put caution signs on printers to give people an
extra heads-up that, once printed, documents need to be treated carefully if they
contain sensitive information.

Final deliverables
Left out of the breach patterns is Denial of Service, since it also does not typically
result in an actual confidentiality breach. DDoS was over 90% of incidents in
Professional Services and Figure 90 shows us that this sector has slightly above
average DDoS bits per second.

To wrap up with some good news, Figure 91 shows that Professional Services has a
better-than-average patch rate, completing 67% of patches in the first quarter from
those being first made available from the manufacturer. If you’ve read the Results
and Analysis—Action—Hacking section, you know that it’s not the slow patching
that’s the problem; it’s the systems in the remaining third that never get patched that
are likely to come back to haunt you.

Figure 90. Most common BPS in
Professional Services industry DDoS
(n = 30 organizations); all industries mode
(green line): 565 Mbps

Figure 91. Patching in Professional Services
industry vulnerabilities (n = 87,857)

100%

75%

50%

25%

d
e
h
c
t
a
p
t
n
e
c
r
e
P

Professional
Services:
AUC: 56%
COT: 67%

Overall:
AUC: 44%
COT: 57%

0

25

50

75

Days since discovery

2020 DBIR   Industry analysis

68

Public
Administration

I

S
C
A
N

2
9

Summary

Ransomware is a large problem for
this sector, with financially motivated
attackers utilizing it to target a wide array
of government entities. Misdelivery and
Misconfiguration errors also persist in
this sector.

Frequency

Top Patterns

Threat Actors

Actor Motives

Data
Compromised

Top Controls

6,843 incidents,
346 with confirmed
data disclosure

Miscellaneous Errors,
Web Applications and
Everything Else
represent 73%
of breaches.

External (59%), Internal
(43%), Multiple (2%),
Partner (1%) (breaches)

Financial (75%),
Espionage (19%),
Fun (3%) (breaches)

Personal (51%), Other
(34%), Credentials
(33%), Internal (14%)
(breaches)

Implement a Security
Awareness and Training
Program (CSC 17),
Boundary Defense
(CSC 12), Secure
Configurations
(CSC 5, CSC 11)

I can see clearly now.
The Public Administration sector is an illustration of what good partner visibility
into an industry looks like. The bulk of our data in this vertical comes from partners
inside the United States federal government who have a finger on the pulse of data
breaches inside Public Administration. As we have stated elsewhere in this report,
in order to meet the threshold for our definition of a data breach, the compromise
of the confidentiality aspect of data must be confirmed. However, reporting
requirements for government are such that run-of-the-mill malware infections or
simple policy violations still must be disclosed. Therefore, we see an inordinately
large number of incidents and a correspondingly small number of breaches.

When we look at the difference in the attack patterns in this sector, for example,
the top three for breaches are Miscellaneous Errors, Web Applications attacks and
Everything Else. When we look at the same data for incidents, the top three patterns
are Crimeware (malware attacks), Lost and Stolen Assets, and Everything Else.

With regard to malware in the incident dataset, Figure 92 indicates that Ransomware
is by far the most common, with 61% of the malware cases. This malware is most
commonly downloaded by other malware, or directly installed by the actor after
system access has been gained. However, ransomware isn’t typically an attack that
results in a confidentiality breach. Rather, it is an integrity breach due to installation
of the software, and an availability breach once the victim’s system is encrypted.
Thus, these attacks do not typically appear when we discuss data breaches.

Ransomware

Capture app data

C2

Backdoor

Other

Password dumper

Trojan

Export data

Downloader

RAT

Capture stored data

Figure 92. Top Malware varieties in Public Administration incidents (n = 198)

2020 DBIR   Industry analysis

69

Misdelivery

Misconfiguration

Publishing error

Loss

Other

Programming error

Figure 93. Top Error varieties in Public
Administration breaches (n = 92)

The same is true of Lost and Stolen Assets. These are unencrypted devices or
they wouldn’t be considered even at risk of a data breach. Unless, of course, the
decryption key is also lost at the same time in human-readable format (before you
jeer, keep in mind that we have actually seen this). The data on these devices is
most likely protected only by a password, and is therefore considered at-risk in our
dataset, and not a confirmed data breach.

No Regerts42
In the red corner, Miscellaneous Errors is the most prominent pattern in this industry
when looking at confirmed data breaches. Figure 93 shows us that Misdelivery
remains a big problem for the public sector. This is when sensitive information
goes to the wrong recipient. It may be via electronic means, such as emails that are
misaddressed, or it may be old-fashioned paper documents. Those mass mailings
(and nobody can hold a candle to the volume of paper sent out by government
entities) where the envelopes and their contents become out of sync can be a
serious problem.

In the blue corner, weighing in at 30% of breaches, we have Misconfiguration, the
other contender for the top variety of Error. A Misconfiguration data breach is when
someone (usually a system administrator or someone in another privileged technical
role) spins up a datastore in the cloud without the security measures in place to
protect the data from unauthorized access. There are security researchers out
there who spend their time looking for just this kind of opportunity. If you build it,
they will come.

Looking back at changes from last year to this, the top three patterns have altered
composition quite a lot. The 2019 report showed the top three breach patterns
as Cyber-Espionage, Miscellaneous Errors and Privilege Misuse. You can see the
difference in the rankings in Figure 94. Both Cyber-Espionage and Privilege Misuse
declined in our dataset overall this year, and have dropped into the single digit
percentages in this sector.

Web Applications

Privilege Misuse

Miscellaneous Errors

Cyber-Espionage

Everything Else

Denial of Service

Crimeware

Payment Card Skimmers

Lost and Stolen Assets

Point of Sale

Figure 94. Patterns in Public Administration breaches (n = 346)

42  Well, except for these ugly tattoos we got on a dare last year.

2020 DBIR   Industry analysis

70

Real Estate and
Rental and Leasing

I

S
C
A
N

3
5

Summary

Web Applications attacks utilizing stolen
credentials are rife in this vertical. Social
engineering attacks in which adversaries
insert themselves into the property
transfer process and attempt to direct
fund transfers to attacker-owned bank
accounts are also prevalent. Like many
other industries, Misconfigurations are
impacting this sector.

Frequency

Top Patterns

37 incidents,
33 with confirmed
data disclosure

Web Applications,
Everything Else and
Miscellaneous Errors
represent 88% of
data breaches.

Threat Actors

External (73%), Internal
(27%) (breaches)

Actor Motives

Data
Compromised

Top Controls

Data
Analysis Notes

Financial (45%–97%),
Convenience/
Espionage (0%–40%
each), Fear/Fun/
Grudge/Ideology/
Other/Secondary
(0%–21% each)
(breaches)

Personal (83%),
Internal (43%), Other
(43%), Credentials
(40%) (breaches)

Top Controls: Secure
Configuration (CSC 5,
CSC 11), Implement a
Security Awareness
and Training Program
(CSC 17), Boundary
Defense (CSC 12)

Actor motives are
represented by
percentage ranges,
as only eight breaches
had a known motive.
Some charts also do
not have enough
observations to have
their expected
value shown.

SOLD!
There is nothing quite like that feeling of owning your first home. Moving in, enjoying
the smell of fresh paint and reflecting on all the memories you’ll make. Our data for
this vertical indicates that cybercriminals are also being allowed to move right in
and make themselves at home. Whether they are attending a showing of your data
via Web Applications attacks, utilizing social engineering in the Everything Else
pattern or simply being asked to drop in by your employees through an assortment
of Miscellaneous Errors, they are certainly being made welcome. As you can see
in Figure 95, it is difficult to state conclusively which of these three patterns is the
statistical leader but we can assert that they are all in the running.

Don’t leave the key under the welcome mat.
Although we saw a rather small number of breaches in this sector over the last
year, there are some interesting high-level findings to discuss. As in many other
sectors, criminals have been actively leveraging stolen credentials to access users’
inboxes and conduct nefarious activities. In fact, across all industries, credential
theft is so ubiquitous that perhaps it would be more accurate to consider them
time-shares rather than owned. Meanwhile, other external actors are relying on
social engineering to get the job done. Some of these activities are simply aimed
at stealing your data, but in other cases these attacks can be used to tee up a
separate assault, as seen in many of the attacks that leverage pretexting.

Web Applications

Cyber-Espionage

Everything Else

Denial of Service

Miscellaneous Errors

Payment Card Skimmers

Lost and Stolen Assets

Crimeware

Privilege Misuse

Point of Sale

Figure 95. Patterns in Real Estate industry breaches (n = 33)

2020 DBIR   Industry analysis

71

Figure 96. Top integrity impacts in Real
Estate industry incidents (n = 16)

Figure 97. Top Error varieties in Real Estate
industry incidents (n = 7)

Alter behavior

Loss

Fraudulent transaction

Misconfiguration

Other

Misdelivery

Repurpose

Other

Software installation

Programming error

Figure 96 shows how Bad Guys™43  exploit the milk of human kindness to dupe
well-meaning employees into assisting them to achieve their objectives. They use
pretexts to alter someone’s behavior in such a manner that the employee divulges
sensitive information, or otherwise unwittingly helps them to commit fraud. One
example of this type of social engineering is when the attacker inserts themselves
into an email thread regarding the sale or purchase of a new home and convinces
the victim organization to transfer funds to attacker-owned bank accounts. It’s
worthwhile to make a phone call to confirm details before making this type of
significant transaction.

You sent that to who?!
Even though this is the first time we have written an industry section for “Real
Estate,” we have been collecting data on this industry for a number of years. This
enables us to analyze how the patterns have evolved over time in this vertical. This
year, one of the more interesting findings was the continuity in volume of Errors.
These Error-related breaches involve Misconfigurations (forgetting to turn those
restrictive permissions on), Misdeliveries (email and/or paper documents sent to the
incorrect recipient) and Programming errors (mistakes in code) as seen in Figure 97.
These Error actions accounted for 18% of data breaches in the Real Estate vertical.
If you do business in this industry, we urge you to take time for security awareness
training and the implementation of sound policies and procedures.

43  Surely someone has trademarked this, right?

2020 DBIR   Industry analysis

72

Retail

I

S
C
A
N

5
4
–
4
4

Summary

Attacks against e-commerce
applications are by far the leading
cause of breaches in this industry. As
organizations continue to move their
primary operations to the web, the
criminals migrate along with them.
Consequently, Point of Sale (PoS)-
related breaches, which were for many
years the dominant concern for this
vertical, continue the low levels of 2019’s
DBIR. While Payment data is a commonly
lost data type, Personal and Credentials
also continue to be highly sought after in
this sector.

I’ll buy that for $1.
We are sure it comes as no surprise to anyone in this sector, but the Retail industry
is a frequent target for financially motivated actors. Retail as an industry is almost
exclusively financially motivated too, so it is only fair. This sector is targeted by
criminal groups who are trying to gain access to the wealth of payment card data
held by these organizations. Last year’s trend of transitioning from card-present to
card-not-present crime continued, which drove a similar decrease since 2016 in the
use of RAM-scraper malware. Personal data figures prominently in Retail breaches
and is more or less tied with Payment for the top data type compromised. Certainly,
if the attacker cannot gain access to Payment data, but stumbles across Personal
data that is lucrative for other types of financial fraud, they will not file a complaint.

Frequency

Top Patterns

Threat Actors

Actor Motives

Data
Compromised

Top Controls

287 incidents,
146 with confirmed
data disclosure

Web Applications,
Everything Else and
Miscellaneous Errors
represent 72%
of breaches.

External (75%),
Internal (25%),
Partner (1%), Multiple
(1%) (breaches)

Financial (99%),
Espionage (1%)
(breaches)

Personal (49%),
Payment (47%),
Credentials (27%),
Other (25%)
(breaches)

Boundary Defense
(CSC 12), Secure
Configurations
(CSC 5, CSC 11),
Continuous
Vulnerability
Management (CSC3)

To the web with you!
Figure 98 provides us with a good view through the display case as it were in
the “Retail” section. Over the last few years (2014 to 2019), attacks have made
the swing away from Point of Sale devices and controllers, and toward Web
Applications. This largely follows the trend in the industry of moving transactions
primarily to a more web-focused infrastructure. Thus, as the infrastructure changes,
the adversaries change along with it to take the easiest path to data.44 Attacks
against the latter have been gaining ground. In the 2019 DBIR, we stated that we
anticipated Retail breaches were about to lose their majority to web-server-related
breaches, and in Figure 99, we can see that has in fact occurred. Be sure to play
the lucky lotto numbers printed on the back cover. Winner, winner! Chicken dinner!

60%

40%

20%

0%

Web
Applications

Point
of Sale

100%

75%

50%

25%

0%

Web
application
Server

Not Web
application
Server

2015

2017

2019

2014

2015

2016

2017

2018

2019

Figure 98. Patterns over time in Retail
industry breaches

Figure 99. Web application Server vs Not
Web application Server assets in Retail
Payment data breaches over time

44  Of course, if you haven’t made this transition, your PoS infrastructure remains at risk.

2020 DBIR   Industry analysis

73

The Web Applications pattern is composed of two main action varieties: the use
of stolen credentials and the exploitation of vulnerable web app infrastructure.
Figure 100 shows that Exploit vuln and Use of stolen creds are close competitors
for first place in the Hacking varieties category and there is not a great deal to
distinguish between them from a percentage point of view. In a perfect world,
someone else’s data breach would not raise the risk to your own. However, that is
increasingly not the case, with the adversaries amassing datastores of credentials
from other people’s misfortune and trying them out against new victims.

You hold the key to my heart.
Our non-incident data tells us that in this vertical (Figure 101), credential stuffing is
a significant problem. While it is slightly below the most common value for all
industries this year, it is not likely that people who have so many keys (credentials)
will stop trying them on whatever locks they can find.

When the bad actors are not using other people’s keys against your infrastructure,
they are using unpatched vulnerabilities in your web apps to gain access. Based on
the vulnerability data in Figure 102, only about half of all vulnerabilities are getting
patched within the first quarter after discovery. It is best not to put those patches
on layaway but go ahead and handle them as soon as possible. We know from past
research that those unpatched vulnerabilities tend to linger for quite a while if they
aren’t patched in a timely manner—people just never get around to addressing them.
Our analysis found that SQL, PHP and local file injection are the most common
attacks that are attempted in this industry (Figure 103).

Figure 100. Top Hacking varieties in Retail
industry breaches (n = 48)

Use of stolen creds

Exploit vuln

Brute force

Figure 101. Credential stuffing attempts in
Retail industry web blocks (n = 284); all
industries mode (green line): 1.11 M

0

250,000

500,000

750,000 1,000,000

Figure 102. Patching in Retail industry
vulnerabilities (n = 35,098)

Figure 103. Varieties in Retail industry web
application attack blocks (n = 2.22 billion)

PHP
inject

Overall:
AUC: 44%
COT: 57%

Retail:
AUC: 46%
COT: 49%

SQL
inject

other inject

local
file inject

XSS

file
upload

100%

75%

50%

25%

d
e
h
c
t
a
p
t
n
e
c
r
e
P

25
0
Days since discovery

50

75

2020 DBIR   Industry analysis

74

Figure 104. Top data varieties in Retail
industry breaches (n = 135)

Figure 105. Top terms in hacking-related
criminal forum posts (n = 3.35 million)

bank

card

carding

cvv

exp

m
r
e
T

Percent of posts

Personal

Payment

Credentials

Medical

Internal

Other

Data types
If we were to create a ranking of the
most easily monetizable data types,
surely Payment card data would be
at the top. After all, who doesn’t have
the urge to try out that brand new
credit card and “break it in” when it
first arrives? Figure 104 shows us that
the attackers feel the same way, and
likely want to build upon their sweet
gaming rig with someone else’s money.
However, Personal data is tied with
Payment data as the reigning champion.
It’s easy to forget that as web apps
increasingly become the target of
choice, the victims’ Personal data is
sometimes boxed up and shipped off
right along with the Payment data as
a lagniappe.

Figure 105 lists the top terms in
hacking data from criminal forum and
marketplace posts. It stands to reason
that they would (like any good SEO
effort) tailor their terms to what is
most in demand. Clearly banking
and payment card data is high on
everybody’s wish list, although those
who are doing this type of trade do
not need to go to the lengths of
finding a dusty lamp to have those
wishes granted.

2020 DBIR   Industry analysis

75

Transportation
and Warehousing

I

S
C
A
N

9
4
–
8
4

Summary

Financially motivated organized
criminals utilizing attacks against web
applications have their sights set on this
industry. But employee errors such as
standing up large databases without
controls are also a recurring problem.
These, combined with social engineering
in the forms of phishing and pretexting
attacks, are responsible for the majority
of breaches in this industry.

Frequency

Top Patterns

112 incidents,
67 with confirmed
data disclosure

Everything Else,
Web Applications
and Miscellaneous
Errors represent
69% of breaches.

Threat Actors

External (68%), Internal
(32%) (breaches)

Actor Motives

Data
Compromised

Top Controls

Data
Analysis Notes

Financial (74%–98%),
Espionage (1%–21%),
Convenience
(0%–15%) (breaches)

Personal (64%),
Credentials (34%),
Other (23%)
(breaches)

Boundary Defense
(CSC 12), Implement a
Security Awareness
and Training Program
(CSC 17), Secure
Configurations
(CSC 5, CSC 11)

Actor motives are
represented by
percentage ranges,
as only 26 breaches
had a known motive.
Some charts also do
not have enough
observations to
have their expected
value shown.

The Transportation and Warehousing industry is a new one for
our report. If you’re reading this report for the first time for just this
reason, pull up a chair, we’re glad to have you! As you know, this
industry is all about getting people and goods from point A to
point B, and about storing those goods until they’re needed.
Once transported, the people are usually good enough to find
their own places to stay, but that’s another industry entirely.

All roads lead to pwnd.
What is causing breaches in this sector? Our data shows us that Web Applications
attacks and Miscellaneous Errors are quite common, and the Everything Else
pattern is also prevalent, but more on that later (Figure 106). Web applications
are a common attack across the dataset, and a fact of life in this era is that if you
have an internet-facing application, someone out there will eventually get around
to testing your controls for you. The Hacking, Social and Malware actions were
the most common in this industry, which supports the Web Applications
pattern’s prominence.

Everything Else

Lost and Stolen Assets

Miscellaneous Errors

Cyber-Espionage

Web Applications

Denial of Service

Crimeware

Payment Card Skimmers

Privilege Misuse

Point of Sale

Figure 106. Patterns in Transportation industry breaches (n = 67)

2020 DBIR   Industry analysis

76

Keep your eyes on the road.
Miscellaneous Errors are simply a byproduct of being human—we make mistakes.
The most common error in this industry was Misconfiguration, as shown in
Figure 107. A typical misconfiguration error scenario is this: An internal actor
(frequently a system admin or DBA) stands up a database on a cloud service without
any of those inconvenient access controls one would expect to see on sensitive data.
Then, an enterprising security researcher finds this instance using a search engine
that is made to spot these unprotected datastores and poof, you have a breach.

That Everything Else pattern mentioned earlier—it is a place we store odds and ends
for attacks that don’t fit into the other attack patterns, and within this pattern lives
the business email compromise (BEC). These usually come in as a phishing email,
although they can also be done over the phone. The goal of the attacker is either
to get data or facilitate a wire transfer to their conveniently provided bank account.
These attacks are perpetrated largely by organized criminal actors with a
financial motive.

You can see in Figure 108 the most common motive of the external actors in this
sector. While there are some espionage-motivated actors, they are few and far
between when compared to financially motivated attackers. The data type of choice
in this vertical appears to be Personal, which is being closely tailgated by Credentials.

Espionage

Financial

Other

Figure 108. Top Actor motives in
Transportation industry breaches (n = 25)

Loss

Misconfiguration

Misdelivery

Other

Programming error

Publishing error

Figure 107. Top Error varieties in
Transportation industry breaches (n = 15)

2020 DBIR   Industry analysis

77

Section title pulled
into footer

0
SMB
4

Does size matter?
A deep dive into
SMB breaches

Does size matter?
A deep dive into
SMB breaches

Summary

While differences between small and medium-sized businesses (SMBs) and
large organizations remain, the movement toward the cloud and its myriad
web-based tools, along with the continued rise of social attacks, has narrowed
the dividing line between the two. As SMBs have adjusted their business
models, the criminals have adapted their actions in order to keep in step and
select the quickest and easiest path to their victims.

Frequency

Top Patterns

Threat Actors

Actor Motives

Small (less than
1,000 employees)
407 incidents, 221 with
confirmed data disclosure

Large (more than
1,000 employees)
8,666 incidents, 576 with
confirmed data disclosure

Web Applications,
Everything Else and
Miscellaneous Errors
represent 70% of breaches.

Everything Else, Crimeware
and Privilege Misuse
represent 70% of breaches.

External (74%), Internal
(26%), Partner (1%), Multiple
(1%) (breaches)

External (79%), Internal
(21%), Partner (1%), Multiple
(1%) (breaches)

Financial (83%), Espionage
(8%), Fun (3%), Grudge
(3%) (breaches)

Financial (79%), Espionage
(14%), Fun (2%), Grudge
(2%) (breaches)

Data Compromised

Credentials (52%), Personal
(30%), Other (20%),
Internal (14%), Medical
(14%) (breaches)

Credentials (64%), Other
(26%), Personal (19%),
Internal (12%) (breaches)

A trip down memory lane
Several years ago (the 2013 edition of
the report to be precise), we took a
look at some of the differences and
similarities between small businesses
(under 1,000 employees) and large
businesses (1,000+ employees).
Since a lot can change in seven years,
we thought we would once again
compare and contrast the two and
see what story the data tells us. After
all, now more than ever due to the
proliferation of services available as
commodities in the cloud, including
platform as a service (PaaS), software
as a service (SaaS) and any other *aaS
of which you can conceive, a small
business can behave more like a large
one than ever before. Therefore, we
asked ourselves the question, “Have
the differences in capabilities evened
the playing field out a bit between the
two with regard to the detection of
and response to security incidents?”
Since you’re reading this section,
you’ve probably already guessed that
the answer is “Yes!” Let’s dive in and
examine how much has changed, and in
what ways the song remains the same.

The first thing we noticed when
populating the Summary table is the
wide chasm between the two when
it comes to numbers of incidents
and breaches. Breaches are more
than twice as common in the larger
companies than in the small ones.
Does this mean the small organizations
are flying under the radar, or are they
simply not aware they’ve received
visitors of the uninvited variety?
And the inequality between the two
when it comes to number of incidents
is staggering. Is it an obvious case of
“mo’ money, mo’ problems” for large

2020 DBIR   SMB

79

Overall (n = 621)

Small (n = 250)

Large (n = 235)

Tampering (Physical)
Spyware (Malware)
Backdoor (Malware)
Export data (Malware)
Use of stolen creds (Hacking)
Use of backdoor or C2 (Hacking)
Capture stored data (Malware)
Phishing (Social)
C2 (Malware)
Downloader (Malware)
Password dumper (Malware)
Brute force (Hacking)
Rootkit (Malware)
Privilege abuse (Misuse)
Adminware (Malware)
RAM scraper (Malware)
Unapproved hardware (Misuse)
Embezzlement (Misuse)
Unknown (Hacking)
SQLi (Hacking)

32%

30%

27%

25%

25%

23%

22%

22%

21%

20%

18%

18%

16%

8%

7%

7%

5%

5%

4%

4%

7%

47%

46%

20%

28%

29%

30%

26%

34%

22%

19%

20%

17%

34%

18%

8%

15%

15%

10%

10%

6%

4%

29%

26%

22%

25%

15%

23%

27%

25%

21%

8%

9%

14%

3%

2%

2%

<1%

3%

2%

Financial

Espionage

Other

Figure 109. Top 20 threat actions (referencing the 2013 DBIR)

enterprises? Is it due to increased
visibility or perhaps a much wider
attack surface? We find ourselves
in the same position that some
professional sports referees have
been in recently as we realize it’s hard
(maybe more so in the Big Easy) to
make the right call.

We call out the beginning attack
patterns in the table at the beginning
of this section, but the pattern concept
wasn’t born yet the last time we
focused on organization size. In looking
back, we can tell you there have been
some changes in the most frequent
causes (or as we like to call them in
VERIS, action varieties) since 2013.
The top 20 threat actions figure from
the 2013 DBIR (Figure 109) lists
the top 20 threat action varieties of
the year, broken out into small and
large organizations.

You can see that for large
organizations, the top action was
Physical tampering (wait, what?). For
small organizations, in contrast, it was
Spyware, although Brute-force hacking

and Capturing stored data was not far
behind. Skipping ahead seven years to
our current dataset, we see that both
large (Figure 110) and small (Figure 111)
organizations have a top threat action
of Phishing, with the Use of stolen
credentials and Password dumpers in
the top three for both (only in reverse
order). Regardless, the same three
contestants are leading the pack in
both and that is an interesting finding.
Phishing was considerably further
down the list in 2013, as compared to
the prime position it holds now.

Give me your keys and
your wallet.
In 2013, far and away the favorite
data type to steal was Payment card
information. Back in those days,
criminals would walk a long way
(barefoot, in the snow, uphill both ways)
to obtain this type of data (and they
were thankful for the opportunity!).
Following that, Credentials were
a fan favorite, and Internal and

Secret data were also very much in
vogue. Examining the types of data
stolen today, in both small and large
organizations, we see that Payment
card data is so last year. Today’s
criminal (lacking the work ethic of 2013)
is primarily concerned with obtaining
Credentials, regardless of the target
victims’ size. Personal data also seems
to be highly sought after, irrespective of
the size of an organization. After those
two heavy hitters, it becomes too close
to call between Medical, Internal or
Payment data.

Another change from 2013 is the types
of assets commonly attacked (Figure
112). The top asset for large companies
(47%) was an ATM, while Point of Sale
(PoS) controllers (34%) (followed
closely at 29% by the Point of Sale
terminal) were the top assets for small
organizations. All of those assets have
now fallen entirely off the list for both
org types. Nowadays, organizations
regardless of size are troubled with
attacks on User devices, Mail servers
and People (social attacks).

2020 DBIR   SMB

80

Figure 110. Top action varieties in large organization breaches (n = 448)

Phishing (Social)

Backdoor (Malware)

Other

Downloader (Malware)

Password dumper (Malware)

C2 (Malware)

Use of stolen creds (Hacking)

Theft (Physical)

Privilege abuse (Misuse)

Brute force (Hacking)

Data mishandling (Misuse)

Misconfiguration (Error)

Figure 111. Top action varieties in small organization breaches (n = 194)

Phishing (Social)

Exploit vuln (Hacking)

Other

Skimmer (Physical)

Use of stolen creds (Hacking)

Capture stored data (Malware)

Password dumper (Malware)

Data mishandling (Misuse)

Misconfiguration (Error)

C2 (Malware)

Ransomware (Malware)

Backdoor (Malware)

Brute force (Hacking)

Abuse of functionality (Hacking)

No time like the present
Moving on to the differences in the
dataset for this year alone (otherwise
we can’t talk about patterns), the top
attack patterns for small organizations
were Web Applications, Everything
Else and Miscellaneous Errors, with
none of them emerging as the obvious
winner. Meanwhile, large organizations
are contending with Everything Else,
Crimeware and Privilege Misuse as
their main issues. Web Applications
attacks are self-explanatory, while
the Everything Else pattern is a
pantechnicon stuffed with bits and
bobs that do not fit anywhere else.
Packed away in here you will find
attacks such as the business email
compromise—a social attack in the
form of phishing, purporting to be from
a company executive who is requesting
data or a wire transfer. Miscellaneous
Errors is a wide-ranging pattern that
encompasses the many means (and
they are legion) by which someone
you employ can hurt your organization
without malicious intent. The Crimeware
pattern is your garden-variety malware
and tends to be deployed by criminals
who are financially motivated. Finally,
Privilege Misuse is an act (usually
malicious in nature) in which an
Internal actor can ruin both your day
and your brand.

When examining Timeline data, we
noticed that the number of breaches
that take months or years to discover
is greater in large organizations
(Figure 113) than in small organizations
(Figure 114). This seems a bit
counterintuitive. On the one hand,
large organizations have a much
larger footprint and could possibly be
more likely to miss an intrusion on an
internet-facing asset that they forgot
they owned, but small orgs have a
reduced attack surface so it might
be easier to spot a problem. On the
other hand, large orgs typically have
dedicated security staff and are able
to afford greater security measures,
whereas small businesses often do not.
Whatever the reason, there is a rather
marked disparity between them with
regard to Discovery.

2020 DBIR   SMB

81

Overall (n = 621)

Small (n = 250)

Large (n = 235)

30%

25%

4%

ATM (User)
Desktop (User)
File (Server)
Laptop (User)
Other/Unknown (Server)
Other/Unknown (People)
Mail (Server)
Directory (Server)
PoS controller (Server)
PoS terminal (User)
Web application (Server)
Database (Server)
Payment card (Media)
End-user (People)
Executive (People)
Manager (People)
Former employee (People)
Unknown
Cashier (People)
Finance (People)

22%

22%

20%

20%

19%

17%

15%

13%

10%

10%

5%

5%

5%

3%

3%

2%

2%

1%

24%

22%

20%

18%

20%

22%

18%

34%

29%

10%

12%

10%

2%

4%

1%

2%

4%

1%

47%

47%

30%

28%

27%

25%

23%

17%

16%

2%

1%

2%

1%

1%

10%

9%

10%

9%

8%

8%

Financial

Espionage

Other

Figure 112. Varieties of compromised assets (referencing the 2013 DBIR)

Months

Days

Hours

Weeks

Years

Minutes

Seconds

Never

Days

Hours

Months

Weeks

Minutes

Years

Seconds

Never

Figure 113. Discovery time in large
organization breaches (n = 121)

Figure 114. Discovery time in small
organization breaches (n = 102)

2020 DBIR   SMB

82

Regional analysis

Section title pulled
into footer

0
5

Regional
analysis

Introduction
to regions

Incidents

Total

Small
(1–1,000)

Large
(1,000+)

Unknown

Breaches

Total

Small
(1–1,000)

Large
(1,000+)

Unknown

Total

APAC

EMEA

LAC

NA

Unknown

Total

32,002

4,055

4,209

87

18,648

5,003

32,002

407

8,666

22,929

Total

27

57

14

231

78

407

33

88

10

6,409

2,126

8,666

3,995

4,064

63

12,008

APAC

EMEA

LAC

NA

2,799

Unknown

22,929

Total

3,950

560

185

14

920

2,271

3,950

221

22

41

5

130

23

221

576

24

53

5

209

285

576

3,153

514

91

4

581

1,963

3,153

Table 2. Number of security incidents by victim Region and organization size

We present for the first time a
focused analysis on macro-
regions of the world, thanks to
the diligent work of the team
this year to increase the
diversity of our data
contributors and the more
precise statistical machinery
we have put in place.

After the filtering and subset creation
described in the “Introduction to
industries” section, we are left with a
similar result on Table 2. We define
regions of the world in accordance with
the United Nations M4945 standard,
joining the respective super-region
and subregion of a country together.
By combining them even further, the
subjects of our global focus are:

•  APAC—Asia and the Pacific,

including Southern Asia (034),
South-eastern Asia (035), Central
Asia (143), Eastern Asia (030) and
Oceania (009)

•  EMEA—Europe, Middle East and

Africa, including Africa (002), Europe
including Northern Asia (150) and
Western Asia (145)

•  LAC—Latin America and the

Caribbean (419), also including for

45 https://en.wikipedia.org/wiki/UN_M49

redundancy due to potential different
encodings South America (005),
Central America (013) and
Caribbean (029)

•  NA—Northern America (021), mainly
consisting of breaches in the U.S.
and Canada, as well as Bermuda,
which has also been busy lately for
some reason

As the table clearly shows, we have
better coverage in some regions than
in others. However, we did not want to
leave anyone out of our around-the-
world tour, and this is where a lot of our
estimative language and percentage
ranges will come in handy.

This is also a great opportunity for us
to ask for our readers to help us by
sharing your data so we have more data
breaches to report on. Please don’t
take this as an invitation to create data
breaches by either malicious intent or
by accident! However, by suggesting
new potential data contributors from
the regions where you, our readers,
would like more detailed analysis,
and by encouraging organizations in
those areas to contribute data to the
report, we can continue expanding our
coverage and providing better analysis
each new year.

The same caution with small sample
numbers we discussed in the
“Introduction to industries” section
applies to Figure 115—some of them
are so small that you can easily step
on them like the Lego pieces your kid
leaves lying around. Believe us when
we tell you that a biased statement
that does not take into consideration
the small sample size (n value) is just
as painful. Be on the lookout for “Data
Analysis Notes” in the “Latin America
and the Caribbean” section where we
will be calling out those “small samples”
and check out the “Methodology”
section for more information on the
statistical confidence background used
throughout this report.

Please note: Based on feedback from our
readers, we know that while some study
the report from cover to cover, others
only skip to the section or region that is of
direct interest to them. Therefore, you
may notice that we repeat some of our
definitions and explanations several
times, since the reader who only looks at
a given section won’t know the definition
or explanation that we might have
already mentioned elsewhere. Please
overlook this necessary (but possibly
distracting) element.

2020 DBIR   Regional analysis

84

Breaches

Incidents

18

30

162

2

86

8

255

8

26

35

1

21

11

88

87

22

423

133

56

38

8

2

11

2

45

40

2

4

45

326

36

C
A
P
A

7

1

40

137

32

A
E
M
E

2

1

2

4

2

4

4

8

5

2

1

4

1

4

11

4

C
A
L

74

19

305

35

165

15

5

122

189

184

363

165

122

36

340

1

22

71

17

408

563

289

A
N

1,170

136

30

29

743

1,293

798

2,602

5

86

1

9

6

22

2

12

1,214

113

89

26

2,586

2,585

1,215

1,306

9

3

12

4

685

1,483

2

4

1

10

1

688

1,483

13

2

54

6

4

3

6

4

68

20

3

1

8

2

8

4,638

Crimeware

22

Cyber-Espionage

11,279

Denial of Service

504

Everything Else

1,601

Lost and Stolen Assets

171

17

7

194

228

Miscellaneous Errors

Payment Card Skimmers

Point of Sale

Privilege Misuse

Web Applications

Environmental

1,717

Error

12,257

Hacking

4,768

Malware

194

80

445

1

27

117

25

Misuse

Physical

Social

Embedded

Kiosk/Term

Media

Network

514

Person

n
r
e
t
t
a
P

n
o
i
t
c
A

t
e
s
s
A

2,610

2,598

75

12,066

Server

228

C
A
P
A

71

A
E
M
E

9

C
A
L

2,215

User Dev

A
N

0%

25%

50%

75%

100%

Figure 115.  Breaches and incidents by region

2020 DBIR   Regional analysis

85

Northern America (NA)

Figure 116. Northern America (NA) region

Regions with records

Regions without records

2020 DBIR   Regional analysis

86

a9e2f57a. Northern America (NA) region

(Dark Blue = Region with records, Light Blue = Region without records)

Summary
Northern American organizations
suffered greatly from financially
motivated attacks against their
web application infrastructure this
year. Hacking via the Use of stolen
credentials was most commonly
seen, with social engineering attacks
that encourage the sharing of those
credentials following suit. Employee
error was also routinely observed in
our dataset.

Frequency

Top Patterns

Threat Actors

Actor Motives

Data
Compromised

18,648 incidents,
920 with confirmed
data disclosure

Everything Else, Web
Applications and
Miscellaneous Errors
represent 72% of all
data breaches in
Northern America.

External (66%),
Internal (31%) Partner
(5%), Multiple (1%)
(breaches)

Financial (91%),
Espionage (5%),
Grudge (3%)
(breaches)

Personal (43%),
Credentials (43%),
Other (35%), Internal
(21%) (breaches)

The region designated as Northern America consists of the
United States and Canada, as well as some outlying islands such
as Bermuda.
There are a couple of factors that need to be kept in mind when looking at the
findings below. First of all, this region accounts for 69% of all incidents and 55%
of all breaches in our dataset this year. That does not mean that good security
practice has disappeared into the Bermuda Triangle, though. Northern America
has arguably some of the most robust data reporting standards46 in existence,
particularly in Healthcare and Public administration. Therefore, the number of
incidents and breaches are likely to be higher than in areas with less stringent
disclosure requirements. Also, it must be admitted that while this report is
becomingly increasingly global in scope, many of our contributors are located
in and are primarily concerned with Northern American organizations. As a result
of these factors, outcomes for this region are not too dissimilar from the findings
for the overall dataset. Nevertheless, there are a few interesting differences and
highlights worthy of discussion.

Phish and whistle, whistle and phish47
Everything Else is the top pattern for this region (Figure 117). That is due in large
part to the number of financially motivated phishing attacks that we see across so
many industries (Figure 118). In the past, we have observed that security awareness
training can help limit the frequency and/or impact of phishing attacks. However, in
some instances, this training appears to be either not carried out at all or delivered
in an insufficient or inadequate manner. Whatever the reason, telling employees not
to click phishing emails can be as effective as yelling “ear muffs” when you don’t
want your child to hear something unpleasant.

Everything Else

Lost and Stolen Assets

Web Applications

Cyber-Espionage

Miscellaneous Errors

Payment Card Skimmers

Privilege Misuse

Point of Sale

Crimeware

Denial of Service

Figure 117. Patterns in Northern American breaches (n = 920)

46 This is largely due to the robust data breach notification laws passed over the years, such as California S.B. 1386 passed in 2002, which served as a blueprint for other states

in the U.S. and has now been augmented by the California Consumer Privacy Act (CCPA) in the Golden State.

47 We hope you will allow us a paraphrase of the words of the great John Prine. He will be sorely missed.

2020 DBIR   Regional analysis

87

Figure 118. Social varieties in Northern
American breaches (n = 322)

Phishing

Pretexting

Scam

Forgery

Bribery

Influence

Extortion

Get your head out of your … cloud.
Web app attacks also loom large in Northern America. The majority of these attacks
are carried out via the Use of stolen credentials (Figure 119), which are then used
to hack into web-based email and other web applications utilized by the enterprise
(Figure 120). We have mentioned in past reports that, with the growing trend of
businesses moving toward cloud-based solutions, we could expect the Use of
stolen credentials to increase proportionally. This does seem to be the case.

Use of stolen creds

Footprinting

Brute force

Exploit vuln

Other

SQLi

Use of backdoor or C2

Exploit misconfig

Abuse of functionality

Figure 119. Top Hacking varieties in Northern American breaches (n = 268)

Web application

Other

Desktop sharing

Command shell

Backdoor or C2

Desktop sharing software

Figure 120. Top Hacking vectors in Northern American breaches (n = 260)

2020 DBIR   Regional analysis

88

Partner

Internal

Multiple

External

Figure 121. Actors in Northern American
breaches (n = 908)

See! This is why we can’t have anything nice.
You don’t need External actors to harm your organization as long as your employees
are willing to do their work for them. The number of Internal actors is somewhat high
(30%) this year for this region and for the dataset as a whole (Figure 121). This is
explained by the prevalence of Error and Privilege Misuse actions. Both are caused
by Internal actors and both can be very damaging to an organization, but while Error
is unintentional, Misuse can be (and often is) malicious in nature.

Let’s take a quick look at the Error actions. As you can see in Figure 122, the vast
majority of all error-related breaches are caused by Misdelivery (sending data to
the incorrect recipient) and Misconfiguration (i.e, forgetting to secure to a storage
bucket). For whatever reason, these Error types seem to be the peanut-butter-and-
jelly sandwich of the breach world this year. Perhaps Internal actors are simply too
busy trying to perfect their Renegade dance on TikTok these days; we do not know
for sure. Whatever the reason, these errors are found in every industry and region,
and in alarmingly large percentages. As mentioned elsewhere in this report, the
vector for these errors is almost entirely carelessness on the part of the employee.

Turning our attention to Misuse, we see a proliferation of Privilege abuse (56%).
This is using legitimate access for an illegitimate purpose. Somewhat farther down
the ladder, we see approximately equal percentages of Data mishandling and
Possession abuse (Figure 123). No matter how you view it, this region would benefit
from increased controls for Internal actors.

Misdelivery

Privilege abuse

Misconfiguration

Data mishandling

Programming error

Possession abuse

Loss

Unapproved workaround

Publishing error

Unapproved hardware

Disposal error

Email misuse

Other

Gaffe

Other

Knowledge abuse

Figure 122. Top Error varieties in Northern
American breaches (n = 166)

Figure 123. Top Misuse varieties in Northern
American breaches (n = 121)

2020 DBIR   Regional analysis

89

Europe, Middle East
and Africa (EMEA)

Figure 124. Europe, Middle East and Africa (EMEA) region

Regions with records

Regions without records

2020 DBIR   Regional analysis

90

888e0ef8. Africa, Europe, and the Middle East region

(Dark Blue = Region with records, Light Blue = Region without records)

As our world has become increasingly smaller over the years,
it seems that the scope of our report has done the opposite.
In that spirit of growth and exploration, we will examine data from Europe,
the Middle East and Africa (EMEA) in this section. While some readers may
consider it “over there,” the types of attacks and cybersecurity incidents
experienced by those in EMEA are quite similar to what we observe elsewhere.
In this region, Web Applications, Everything Else and Cyber-Espionage are the top
patterns associated with the 185 breaches that we tracked this year (Figure 125).

The Web Applications pattern encompasses two major attacks that greatly affect
this region. The first is Hacking via the Use of stolen credentials, which accounts for
approximately 42% of data breaches. This scenario usually plays out in the following
manner: An attacker uses credentials, typically gathered either through phishing
or malware, to access a web application platform owned by the organization and
commit wickedness of one type or another. This year, we’ve seen adversaries
target assets such as outward-facing email servers, but also other platforms such
as business-related applications. The second type of attack associated with this
pattern is the use of exploits against web-facing applications to either gain access
to the system data itself, or to repurpose the server for something more nefarious.
These attacks account for close to 20% of our breaches in EMEA this year. If you
haven’t checked your external-facing websites recently for unpatched vulnerabilities
or missing multifactor logins, you might want to get on that.

Web Applications

Crimeware

Everything Else

Lost and Stolen Assets

Cyber-Espionage

Denial of Service

Miscellaneous Errors

Payment Card Skimmers

Privilege Misuse

Point of Sale

Figure 125. Patterns in EMEA breaches (n = 185)

Summary
Attackers are targeting web
applications in EMEA with a
combination of hacking techniques
that leverage either stolen
credentials or known vulnerabilities.
Cyber-Espionage attacks leveraging
these tactics were common in this
region. Denial of Service attacks
continue to cause availability
impacts on infrastructure as well.

Frequency

Top Patterns

Threat Actors

Actor Motives

Data
Compromised

4,209 incidents,
185 with confirmed
data disclosure

Web Applications,
Everything Else and
Cyber-Espionage
represent 78% of data
breaches in EMEA.

External (87%),
Internal (13%), Partner
(2%), Multiple (1%)
(breaches)

Financial (70%),
Espionage (22%),
Ideology (3%), Fun
(3%), Grudge (3%),
Convenience (1%)
(breaches)

Credentials (56%),
Internal (44%), Other
(28%), Personal
(20%) (breaches)

2020 DBIR   Regional analysis

91

DoS

Ransomware

Other

C2

Backdoor

Trojan

Figure 126. Top Malware varieties in EMEA
incidents (n = 1,298)

The next pattern, Everything Else, is a catch-all category for breaches and incidents
that do not readily fit into one of the other patterns. In this instance, it mostly
consists of typical business email compromises (BEC) and represents 19% of
the data breaches within this region. In this type of incident, fraudsters will mimic
a business partner, client, executive, etc., in order to get an organization to transfer
a payment over to an attacker-owned bank account. These attacks vary in degree
of sophistication between spear-phishing and pretexting (where a bad actor hijacks
an existing thread and inserts themselves into the conversation, thereby making it
much harder to catch the fraudulent action).

I spy.
In third place was the Cyber-Espionage pattern, accounting for 14% of the region’s
breaches, which is substantially higher than the average of 3% for the overall
dataset. This is an interesting finding, and there is not a clear-cut reason for it. The
most likely explanation is that it may be an artifact of our data contributors and the
cases they happen to encounter in these locales. But then again, James Bond is
British after all. In this sort of incident, one should expect to see the hallmarks of the
Advanced Persistent Threat (APT) attack—combinations of social attacks (phishing)
to gain access, along with malware being dropped and deployed in the environment
in order to maintain persistence and remain unobserved.

Zooming out
If we take a step back and look at the larger class of incidents, we see that Denial of
Service (DoS) attacks topped the regional charts for malware varieties (Figure 126).
An interesting point is that while DoS attacks accounted for a very high percentage
of incidents in this area’s overall corpus, they actually had one of the lowest rates
of bits per second (BPS) of any region. The second most common malware for the
region was ransomware, which continues to be ubiquitous globally. In fact, if we
remove DoS attacks, ransomware accounts for 6% percent of all incidents here,
and is commonly associated with C2/backdoors, Brute forcing and Password
dumpers. All the more reason we should keep our endpoints malware free and our
servers locked down.

2020 DBIR   Regional analysis

92

Asia-Pacific (APAC)

Figure 127. Asia-Pacific  (APAC) region

Regions with records

Regions without records

decba180. Asia, Pacific & Oceania

(Dark Blue = Region with records, Light Blue = Region without records)

2020 DBIR   Regional analysis

93

Summary
The APAC region is being targeted
by financially motivated actors
deploying ransomware to monetize
their access. This region is also beset
by phishing (often business email
compromises), internal errors and
has a higher-than-average rate of
Cyber-Espionage-related breaches.
Web application infrastructure
is being targeted both by Denial
of Service attacks affecting the
availability of the assets, and by
hacking attacks leveraging stolen
credentials.

Frequency

Top Patterns

Threat Actors

Actor Motives

Data
Compromised

4,055 incidents,
560 with confirmed
data disclosure

Web Applications,
Everything Else and
Miscellaneous Errors
represent 90% of
breaches.

External (83%),
Internal (17%), Partner
(0%) (breaches)

Financial (63%),
Espionage (39%),
Fun (4%) (breaches)

Credentials (88%),
Internal (14%), Other
(9%), Personal (6%)
(breaches)

The Asia-Pacific (APAC) region includes a vast amount of territory,
including most of Asia, what many refer to as Oceania (e.g.,
Australia and New Zealand), and numerous island nations in and
around the Pacific.

An incident does not a breach make … or does it?
In Figure 128, we can see the patterns that account for the majority of incidents in
this region. It is important to note that some of those patterns, while prevalent, do
not usually result in a confirmed breach. For instance, in the Crimeware pattern, the
second most common Malware variety is Ransomware incidents. These are both an
Integrity violation (Software Installation) and an Availability violation (Obscuration)
as they encrypt the data, but instances where the data is known to be viewed and
stolen (Confidentiality) remain relatively rare. However, in our data collection for
next year’s report,48 cases are surfacing in which certain groups of actors are using
the tactic of “naming and shaming” their victims in an attempt to exert additional
pressure on them to pay the ransom. In other cases, the actors will copy some or all
of the data prior to encrypting it, and then post excerpts on their websites49 in order
to further incentivize their victims to pay up.

Web Applications

Cyber-Espionage

Crimeware

Privilege Misuse

Everything Else

Lost and Stolen Assets

Denial of Service

Point of Sale

Miscellaneous Errors

Payment Card Skimmers

Figure 128. Patterns in APAC incidents (n = 4,055)

48  Sisyphus has nothing on us!
49  Some examples from publicly disclosed incidents: https://github.com/vz-risk/VCDB/issues?q=is%3Aopen+is%3Aissue+label%3ARansomeware-N%26S

2020 DBIR   Regional analysis

94

Web Applications attacks were the top pattern for both incidents and confirmed
breaches in APAC. These attacks are most frequently someone testing their trusty
store of stolen credentials against your web-facing infrastructure and crossing their
fingers they will see success. Not surprisingly, with the problem of credential reuse
and the vast treasure trove of resulting credential dumps, there are a fair number
of hackers laughing all the way to the bank. If that strategy does not work for our
hoodie-clad friends, the use of social engineering will frequently gain them the keys
to the kingdom. Clearly, something is working, since Credentials were the top stolen
data type in the region’s breaches.

The second most common pattern was Everything Else (Figure 129). This serves
as a category for breaches that do not fit the criteria for the other attack patterns.
There are a couple of common attacks that live within this pattern. One of them,
the business email compromise (BEC), is an attack that starts with a phishing email.
The attacker is frequently masquerading as someone in the executive suite of the
company and is trying to influence the actions of someone who would not normally
be comfortable challenging a request from them. For example, a payroll clerk
believes they are being told to reroute deposits to a different account by the CEO of
the organization and so they do as instructed—only to find later that the request did
not actually come from that executive.

Sometimes this comes in the form of a pretext (an invented scenario). One common
example is asking for money via a wire transfer to a specific (never before used)
account. In either case, unless there is a process in place to handle these kinds of
unusual requests from someone in high authority, the organization will likely see
an incident.

Web Applications

Privilege Misuse

Everything Else

Lost and Stolen Assets

Miscellaneous Errors

Denial of Service

Cyber-Espionage

Payment Card Skimmers

Crimeware

Point of Sale

Figure 129. Patterns in APAC breaches (n = 560)

2020 DBIR   Regional analysis

95

Oops, did I do that?
A word of warning: What you are about to hear may shock you, but people are not
perfect. Yes, we know, we didn’t believe it at first either. But our dataset certainly
indicates that it is the case, and neither organization type nor region seems to
make much difference. In fact, the Miscellaneous Errors pattern comes in third in
the APAC regional data. What are these errors? Why are they happening to me?
Hop in and we will take you on a tour of the many ways the people who make up an
organization can cause a breach without actually meaning to.

Figure 130 shows the bulk of these are Misconfiguration errors, and are due to
Carelessness. Misconfiguration errors have long been a boon companion of this
report. They occur when an employee—typically a system administrator or some
other person with significant access to scads (yes that is a technical term) of data—
stands up a database in the cloud without the usual security controls. “This will be
fine. Surely nobody will locate this here,” they think to themselves. Or perhaps the
lunch special ends at two and they leave with the intention of putting those controls
in place at the very next convenient moment. But often that moment only arrives
after a security researcher, or much worse an attacker, has already found them.
Yes, believe it or not there are truly a sizeable number of people who are employed
(and some who are freelance) to find these nuggets of data strewn about on the
internet just waiting to be unearthed. What comes next depends on the motives
of the person who found the data. Most security researchers will notify the
organization (if they can figure out who it belongs to). However, sometimes it isn’t
a person with motivations of notification, but rather an intention to monetize this
tasty find on the dark web.

Misconfiguration

Programming error

Publishing error

Misdelivery

Figure 130. Error varieties in APAC
breaches (n = 55)

2020 DBIR   Regional analysis

96

Latin America and
the Caribbean (LAC)

Figure 131. Latin America and the Caribbean (LAC) region

Regions with records

Regions without records

2020 DBIR   Regional analysis

97

d55c3105. Latin America and the Caribbean

(Dark Blue = Region with records, Light Blue = Region without records)

Summary
Even though there are a relatively
small number of incidents and
breaches recorded in the region,
the results clearly show consistency
with the global dataset. Denial of
Service attacks are seen with a
higher intensity than expected,
and ransomware incidents are a
serious problem.

Frequency

Top Patterns

Threat Actors

Actor Motives

Data
Compromised

Data Analysis
Notes

87 incidents,
14 with confirmed
data disclosure

Denial of Service,
Crimeware and
Web Applications
represent 91%
of incidents.

External (93%),
Internal (7%), Partner
(1%), Multiple (1%)
(incidents)

Financial (52%–87%),
Espionage/Ideology
(2%–27% each), Fun/
Grudge (0%–15%
each), Convenience/
Fear/Other/
Secondary (0%–8%
each) (incidents)

Credentials, Personal,
Internal, Secrets and
System (incidents)

Actor motives are
represented by
percentage ranges,
as only 24 incidents
had a known motive.

It’s the law—or not.
Before we begin, it is important to point out that not all of the countries in this region
have a legal requirement to notify of a data breach either to the government or to
those affected, with the notable exceptions of Mexico and Colombia (where only the
government is required to be notified). As such, we can surely expect a significant
under-reporting of incidents and breaches here. It should be interesting to see if,
as in other areas of the world where new disclosure laws are passed, the reporting
ramps up and we find that it was just the tip of the iceberg being reported before.
Hopefully, we can entice new contributors in LAC to increase the quality of our data.
(Is this you? Let’s talk.)

All things considered, we see a clear mirroring of the data we have available for this
region in the global dataset. The majority of actors in all incidents are External, with
the 93% in the region being very similar to the 92% of the entire dataset. Likewise,
52% to 87% of incidents were Financially motivated in LAC, while 64% were so
motivated in the global data.

The top patterns for incidents are also consistent with the larger dataset, with
Denial of Service representing between 50% to 70%, while Crimeware, Web
Applications and Everything Else are tightly grouped (Figure 132). Crimeware is
largely made up of incidents involving Ransomware, which have a very strong
showing in this region in relation to other action varieties.

Denial of Service

Privilege Misuse

Crimeware

Cyber-Espionage

Everything Else

Payment Card Skimmers

Web Applications

Lost and Stolen Assets

Miscellaneous Errors

Point of Sale

Figure 132. Patterns in LAC incidents (n = 87)

2020 DBIR   Regional analysis

98

For all those similarities, this region had the largest median bits per second (BPS)
by far—with 9 Gbps—where the global median was just a little over 500 Mbps
(Figure 133). This higher intensity is in line with what one would expect from Denial
of Service attacks against Financial organizations, which were over-represented in
our regional DDoS data.

One of the things that has been reinforced in analyzing the data across the different
locales is that, regardless of whether a specific country is represented in the
dataset from year to year, all countries are seeing similar types of attacks. Time
and again, we see that the adversaries are not adjusting their tactics based on the
geographic location of their victims. They adjust their attacks based on what they
need to do to gain access. So, while we have seen some differences across the
regions, we are consistently finding that the kinds of attacks are common to all.

0

1B

2B

3B

4B

Figure 133. Most common BPS in LAC region DDoS (n = 52 DDoS); all regions mode
(green line): 565 Mbps

2020 DBIR   Regional analysis

99

Wrap-up

Section title pulled
into footer

0
6

Wrap-up

Well, that’s it, folks! Thank you for joining us again. We hope you enjoyed reading the
report and found the contents informative. As always, we send our most sincere thanks to
our readers, supporters and contributors. This job can be a bit of a heavy lift at times, but it
is also a labor of love. We feel very fortunate to be able to create this report and share the
findings with you. We are grateful to all of you who have supported this endeavor with
your time and resources. We hope to meet you all back here again next year, and in the
meantime, be well, be prosperous and be prepared for anything.

CIS Control
recommendations

CIS Critical Security Controls (CSCs)

CSC 1

Inventory and Control
of Hardware Assets

CSC 11

CSC 2

Inventory and Control
of Software Assets

CSC 3

Continuous Vulnerability
Management

Secure Configuration
for Network Devices,
such as Firewalls,
Routers and Switches

CSC 12

Boundary Defense

CSC 13

Data Protection

CSC 4

Controlled Use of
Administrative Privileges

CSC 14

Controlled Access Based
on the Need to Know

CSC 5

Secure Configuration for
Hardware and Software on
Mobile Devices, Laptops,
Workstations and Servers

CSC 6

Maintenance,
Monitoring and
Analysis of Audit Logs

CSC 7

Email and Web
Browser Protections

CSC 8

Malware Defenses

CSC 9

Limitation and Control
of Network Ports,
Protocol and Services

CSC 10

Data Recovery
Capabilities

CSC 15

Wireless
Access Control

CSC 16

Account Monitoring
and Control

CSC 17

Implement a Security
Awareness and
Training Program

CSC 18

Application
Software Security

CSC 19

Incident Response
and Management

CSC 20

Penetration Tests and
Red Team Exercises

For all the years of hard work,
the DBIR can finally have
some standardized controls,
as a treat.

To be fair, this is simply a new take on
an old approach. If you were to take
out the 2014 version of the DBIR, blow
the dust off of the cover and glance
through the findings, you’ll see an effort
that we undertook to help standardize
our approach to talking about defense
and controls.

In this effort, we aligned our findings
with the Center for Internet Security
(CIS) Critical Security Controls (version
6 at the time) to provide you, our most
devoted and loyal readers, with a way
to match our findings to your security
efforts. You may (or may not) be happy
to hear that we’ve revisited our earlier
attempt to help provide you with the
same types of integration and assist
you with tying your security program
prioritization to our data.

Why CIS?
Most of us probably have our own
preferences regarding security
frameworks and guidance, and the
authors of this report are certainly
not without theirs (hint: one of us may
have contributed to the CIS Critical
Security Controls [CSCs] at one point
or another), but there are several
empirical reasons why we chose this
specific collection of controls. In brief,
they provide sufficient levels of detail
to meaningfully tie back between
our Actions and Vectors, and there’s
a multitude of different mappings
between the CIS CSCs and other
standards freely available online. Also,
it helps that we jibe with their non-profit
community approach.

2020 DBIR   Wrap-up

101

75%

100%

89%

100%

11%

86%

89%

60%

38%

75%

100%

100%

11%

62%

100%

100%

80%

14%

91%

11%

57%

91%

56%

78%

75%

58%

80%

100%

i

e
g
a
n
o
p
s
E
-
r
e
b
y
C

e
r
a
w
e
m

i
r
C

0%

25%

50%

75% 100%

75%

75%

100%

38%

89%

100%

29%

29%

89%

44%

100%

100%

20%

62%

44%

62%

12%

44%

12%

100%

100%

100%

100%

43%

27%

29%

82%

55%

44%

100%

11%

100%

33%

11%

83%

100%

20%

89%

58%

56%

100%

33%

40%

50%

100%

57%

18%

25%

11%

100%

1

2

3

4

5

6

7

8

9

10

11

12

13

14

15

16

17

18

19

For those who are unacquainted with
the CIS CSCs, they are a community-
built, attacker-informed prioritized set
of cybersecurity guidelines that consist
of 171 safeguards organized into 20
higher-level controls. One of the unique
elements of the CIS CSCs is their focus
on helping organizations understand
where to start their security program.
This prioritization is represented in
two ways:

•  Through the ordering of the Critical
Security Controls so that they allow
a loose prioritization (Critical Security
Control 1: Inventory of Hardware
is probably a better place to start
than Critical Security Control 20:
Penetration Testing)

•  Introduced in version 7.150 is the

concept of Implementation Groups,
in which the 171 safeguards are
grouped based on the resources
and risks the organizations are
facing. This means that a smaller
organization with fewer resources
(Implementation Group 1) shouldn’t
be expected to implement resource-
and process-intensive controls such
as Passive Asset Discovery even if it
is within Critical Security Control 1,
while an organization with more
resources and/or a higher risk level
may want to consider that control.

78%

100%

100%

56%

100%

44%

38%

38%

100%

20

i

l

e
s
E
g
n
h
t
y
r
e
v
E

l

s
t
e
s
s
A
n
e
o
t
S
d
n
a
t
s
o
L

s
r
o
r
r
E
s
u
o
e
n
a

l
l

e
c
s
M

i

l

e
a
S
f
o
t
n
o
P

i

i

e
s
u
s
M
e
g
e

l
i

v
i
r
P

s
n
o
i
t
a
c

i
l

p
p
A
b
e
W

Figure 134. Percentage of Safeguards mapped to Patterns by Critical Security Control

50  https://www.cisecurity.org/blog/v7-1-introduces-implementation-groups-cis-controls/

2020 DBIR   Wrap-up

102

Email and Web Browser Protection
(CSC 7)

Since browsers and email clients are
the main way that users interact with
the Wild West that we call the internet,
it is critical that you lock these down to
give your users a fighting chance.

Account Monitoring (CSC 16)

Locking down user accounts across
the organization is key to keeping bad
guys from using stolen credentials,
especially by the use of practices like
multifactor authentication, which also
shows up here.

Limitation and Control of Network
Ports, Protocols and Services
(CSC 9)

Much like how Control 12 is about
knowing your exposures between
trust zones, this control is about
understanding what services and ports
should be exposed on a system, and
limiting access to them.

Boundary Defense (CSC 12)

Not just firewalls, this Control includes
things like network monitoring, proxies
and multifactor authentication, which
is why it creeps up into a lot of
different actions.

Data Protection (CSC 13)

One of the best ways of limiting the
leakage of information is to control
access to that sensitive information.
Controls in this list include maintaining
an inventory of sensitive information,
encrypting sensitive data and limiting
access to authorized cloud and
email providers.

Implement a Security Awareness
and Training Program (CSC 17)

Educate your users, both on malicious
attacks and the accidental breaches.

The future is under control.
To aid us both in our continuous
improvement and transparency, we’ll
be adding our mapping of Critical
Security Controls to our VERIS GitHub
page at https://github.com/vz-risk/
veris. We encourage you to use it as
well and provide feedback on how you
think we can improve. This is really
our first step toward making this more
accessible and easier for others to
leverage, and while we acknowledge
that this first version may have room for
improvement, we plan to iterate rapidly
on it. The more we share a common
language, the easier it will be for us
to work together toward more secure
environments and organizations.

How we used it
The more observant among you may
notice that we included a new item on
our Summary tables in our industry
sections that identify the Top Controls
for the breaches found in that specific
industry. To get those Top Controls,
we developed a mapping between the
VERIS Actions and the safeguards and
then aggregated them at the Critical
Security Control level. This allows you
to get a rough approximation of some
of the controls that you should consider
prioritizing for your security program.

Figure 134 is based on the initial
mapping we did and captures the
percentage of safeguards per Critical
Security Control that play a role in
mitigating the patterns identified.51
Below is also a quick description of
some of the top controls identified
across all the industries analyzed.
Additional information on the actual
Critical Security Controls can be found
on the CIS website.52

Continuous Vulnerability
Management (CSC 3)

A great way of finding and
remediating things like code-based
vulnerabilities, such as the ones found
in web applications that are being
exploited and also handy for finding
misconfigurations.

Secure Configuration (CSC 5,
CSC 11)53

Ensure and verify that systems are
configured with only the services
and access needed to achieve their
function. That open, world-readable
database facing the internet is probably
not following these controls.

51   One thing of note is that the CIS Controls are focused on cybersecurity best practices and don’t touch upon things like physical security

(Payment Card Skimmers pattern) or availability practices (Denial of Service pattern), so we did not include them in our diagram.

52  https://www.cisecurity.org/controls/cis-controls-list/
53  We combined both Secure Configuration for Desktops, Servers and Workstations (CSC 5) AND Secure Configuration for Networking Devices (CSC 11),

for two reasons. For one, it’s difficult to know if it’s a networking issue or a system issue that is the ultimate cause of the breach and for another, it’s become
increasingly more difficult to separate the network from the device in certain environments.

2020 DBIR   Wrap-up

103

Year in review

54

January

February

March

The first intelligence collection in 2019 was an FBI Liaison Alert System on APT10 intrusion
activities targeting cloud-based managed service providers. Throughout the month, the
Verizon Threat Research Advisory Center (VTRAC) intelligence collections reflected a
continuation of some of 2018’s trends and emerging developments that would occupy us
throughout the new year. New intelligence linked two Russian APT-grade actors, GreyEnergy
and APT28 (Sofacy). Two months since we began tracking “the DNSpionage campaign,” new
collections revealed its global span and complexity. GandCrab and Ryuk ransomware surged
in January, in part to occupy the vacuum left after the SamSam operators were indicted
and ceased operations. The VTRAC continued to track and report Magecart payment card
scripting skimmer attacks on e-retailers, a threat that would resurface several more times in
2019. The Indian subsidiary of Milan-based Tecnimont SpA, fell prey to a fraud after US$18.6
million (Rs130 crore) was stolen by Chinese hackers. The attackers breached the email
system of the Mumbai branch to learn the “rhythm” of the business, identifying key players,
vocabulary and customs. A series of staged conference calls with executives in Italy and a
Swiss lawyer convinced the head of the Indian office to transfer funds to Hong Kong banks.

Australia’s parliament revealed that its computer network had been compromised by an
unspecified “security incident.” Norwegian cloud computing company Visma attributed a
breach to the menuPass threat actor. A whaling campaign was observed that was probably
aiming for Office 365 credentials to be used for a business email compromise operation.
The Bank of Valetta in Malta was the victim of a €13 million fraud. Analysis of weaponized
documents used by APT-grade actors in APAC sought to determine if a shared “digital
quartermaster” was supplying multiple actors, including multiple state-aligned ones. It found
links among some Chinese actors but that “the current exchange of offensive cyber tools
remains opaque,” and requires more research.

The successful exploitation of new vulnerabilities was a recurring problem in March, including
vulnerabilities in Cisco Adaptive Security Appliances, Cold Fusion, Drupal, Microsoft
Exchange Server and the Windows kernel. Attacks on two “zero-day” vulnerabilities were
mitigated among 36 patches on “Patch Tuesday.” “Operation ShadowHammer” by the
Chinese Winnti threat actor tampered with software updates from PC maker ASUSTeK
Computer to install malware on victims’ computers. Aluminum manufacturer Norsk Hydro
was attacked with LockerGoga ransomware. Citrix disclosed a data breach after the FBI
warned them the attackers probably used a password spraying attack to gain a foothold.
We collected intelligence about three separate campaigns targeting point-of-sale systems.

54  Thanks to David M. Kennedy from the VTRAC for this contribution.

2020 DBIR   Wrap-up

104

April

May

June

July

Pharmaceutical company Bayer announced it had prevented an attack by the Winnti threat
actors targeting sensitive intellectual property. The Indian IT services giant Wipro was
breached in order to attack its customers. The ultimate aim of the group behind the attack
appeared to be gift-card fraud. The Vietnam-aligned APT32 (Ocean Lotus) actor targeted
foreign automotive companies to acquire IP. The U.S. Department of Energy reported grid
operators in Los Angeles County, California, and Salt Lake County, Utah, suffered a DDoS
attack that disrupted their operations, but did not cause any outages. The US-CERT warned
that multiple VPN applications store the authentication and/or session cookies insecurely in
memory and/or log files. Cisco, Palo Alto Networks, F5 Networks and Pulse Secure products
were affected. A new DNS hijacking campaign, “Sea Turtle,” was discovered targeting private
and public organizations primarily located in the Middle East and North Africa.

Patch Tuesday in May included patches for CVE-2019-0708, a vulnerability in Remote
Desktop Protocol that was nicknamed “BlueKeep.” A hue and cry to patch so as to avoid
an imminent WannaCry-like worm went hyperbolic. The City of Baltimore, Maryland, was
paralyzed by RobbinHood ransomware. A new ransomware, “Sodinokibi” appeared to be
spreading from unpatched Oracle WebLogic servers. Magecart groups continued to deploy
payment card scraping scripts. They expanded their targeted platforms beyond Magento to
the PrismWeb and OpenCart e-commerce platforms. A vulnerability in Magento patched in
March became the target of mass scanning and SQLinjection attacks.

LabCorp disclosed that a breach at a third-party billing collections firm exposed the
personal information of 7.7 million Americans. Chinese intelligence services hacked into
the Australian National University to collect data they could use to groom students as
informants before they were hired into the civil service. U.S. grid regulator NERC issued a
warning that Xenotime, a major hacking group with suspected Russian ties, was conducting
reconnaissance into the networks of electrical utilities. “Operation Soft Cell” ran over
the course of seven years by the APT10 Chinese espionage actor. They hacked into 10
international mobile phone providers operating across 30 countries to track dissidents,
officials and suspected spies. The operators behind GandCrab ransomware announced
they were shutting down. Most analysts assessed they were simply shifting from GandCrab
to Sodinokibi.

Capital One revealed a hacker accessed data on 100 million credit card applications,
including Social Security and bank account numbers. Improperly secured Amazon cloud
storage was at the heart of the theft of 30 GB of credit application data by a single subject.
Microsoft revealed that it had detected almost 800 cyberattacks over the past year targeting
think tanks, non-governmental organizations and other political organizations around the
world, with the majority of attacks originating in Iran, North Korea and Russia. Several major
German industrial firms, including BASF, Siemens and Henkel, announced that they had been
the victim of a state-sponsored hacking campaign by the Chinese Winnti group.

2020 DBIR   Wrap-up

105

August

September

October

November

December

On Friday, August 16, 22 Texas towns were infected with Trickbot followed by Sodinokibi
ransomware after attackers breached their managed service provider (MSP), TSM
Consulting, and employed the MSP’s ConnectWise Control remote management tool to
distribute the malware. The following week, malware researchers observed revived activity
in Emotet distribution networks. In June, the Emotet crew seemed to suspend operations. By
mid-September, Emotet seemed to be fully operational. Emotet had been linked to multiple
Russian threat actors, including Mummy Spider, TA542 and TA505. Emotet mal-spam had
been delivering other malware payloads, including Dridex, Ursnif, Trickbot and Ryuk.

At the end of August and early in September, multiple sources began reporting strategic
web compromises targeting Tibetan rights activists and ethnic minority Uyghurs using
iOS and Android Trojans. Operation Soft Cell reported in June was probably part of this
campaign. Another new Chinese APT-grade actor, APT5, emerged and was discovered
attacking vulnerable VPN servers. Two zero-day Windows vulnerabilities were included in
September’s Patch Tuesday and before the end of the month, Microsoft released an out-of-
cycle patch for a third zero-day. A breach at social video-game developer Zynga affected
over 175 million players.

In October, the VTRAC was swamped by intelligence covering APT-grade actors, including
TA505, FIN6, FIN7 and RTM cybercrime actors. FIN4, FIN6 and Carbanak were linked
to different Magecart groups. Intelligence was received on cyber-espionage and cyber-
conflict actors included Charming Kitten, Turla, Winnti and APT29 actors. We learned of a
September attack on India’s Kudankulam Nuclear Power Plant (KNPP) by the Lazarus group.
The attack did not affect either the nuclear power plant control system or the electricity-
generating power plant control system. A new spin on business email compromises emerged
and was dubbed “Vendor Email Compromises.”

Facility services company Allied Universal suffered a Maze ransomware infection. The
miscreants demanded about US$2 million in bitcoin and threatened to release 5 GB of stolen
internal files if they weren’t paid. They did release at least 700 MB. Before the end of the
year, criminals behind at least four ransomware families had begun to exfiltrate internal files
before triggering file encryption. They threatened to make the data public to add leverage
on the victims to pay. The Iranian APT33 had been targeting industrial control system (ICS)
equipment that is used in oil refineries, electrical utilities and manufacturing.

The U.S. government warned of malicious spam-spreading Dridex banking Trojans that
were used to gain a foothold to infect networks with BitPaymer ransomware. Petróleos
Mexicanos (Pemex) was the victim of DoppelPaymer, a variant of Dridex and BitPaymer.
One of 36 vulnerabilities Microsoft patched was being exploited in watering-hole attacks
before December’s Patch Tuesday. Microsoft released another out-of-cycle security bulletin
and patch for a SharePoint vulnerability that was being exploited in the wild. The Gallium
threat actor was linked to Operation Soft Cell and the watering-hole attacks on Tibetans
and Uyghurs.

2020 DBIR   Wrap-up

106

Section title pulled
into footer

0
7

Appendices

Appendices

Appendix A:
Methodology

One of the things readers value
most about this report is the
level of rigor and integrity we
employ when collecting,
analyzing and presenting data.
Knowing that our readership cares
about such things and consumes this
information with a keen eye helps
keep us honest. Detailing our methods
is an important part of that honesty.
In order to continue to increase
the transparency of our work, we
introduced a couple of new features we
are including in the report this year.

First, we make mistakes. A column
transposed here, a number not updated
there. We’re likely to discover a few
things to fix. When we do, we’ll list
them on our corrections page: https://
enterprise.verizon.com/resources/
reports/dbir/2020/report-corrections/

Second, we check our work. The same
way the data behind the DBIR figures
can be found in our GitHub repository,55
for the first time we’re also publishing
our fact-check report there as well.
It’s highly technical, but for those
interested, we’ve attempted to test
every fact in the report.56

Non-committal disclaimer
We would like to reiterate that we make
no claim that the findings of this report
are representative of all data breaches
in all organizations at all times. Even
though the combined records from all
our contributors more closely reflect
reality than any of them in isolation,
it is still a sample. And although we
believe many of the findings presented
in this report to be appropriate for
generalization (and our confidence
in this grows as we gather more data
and compare it to that of others), bias
undoubtedly exists.

While we may not be perfect,
we believe we provide the best
obtainable version of the truth and a
useful one at that. Please review the
“Acknowledgement and analysis of
bias” section below for more details on
how we do that.

The DBIR process
Our overall process remains intact and
largely unchanged from previous years.
All incidents included in this report were
individually reviewed and converted (if
necessary) into the VERIS framework
to create a common, anonymous
aggregate dataset. If you are unfamiliar
with the VERIS framework, it is short
for Vocabulary for Event Recording and
Incident Sharing; it is free to use and
links to VERIS resources that are at the
beginning of this report.

The collection method and conversion
techniques differed between
contributors. In general, three basic
methods (expounded below) were used
to accomplish this:

1

 Direct recording of paid external
forensic investigations and related
intelligence operations conducted by
Verizon using the VERIS WebApp

2  Direct recording by contributors

using VERIS

3  Converting contributors’ existing

schema into VERIS

All contributors received instruction to
omit any information that might identify
organizations or individuals involved.

Reviewed spreadsheets and VERIS
WebApp JavaScript Object Notation
(JSON) are ingested by an automated
workflow that converts the incidents
and breaches into the VERIS JSON
format as necessary, adds missing
enumerations and then validates the
record against business logic and
the VERIS schema. The automated
workflow subsets the data and
analyzes the results. Based on the
results of this exploratory analysis,
the validation logs from the workflow
and discussions with the contributors
providing the data, the data is cleaned
and reanalyzed. This process runs
nightly for roughly three months as
data is collected and analyzed.

55  https://github.com/vz-risk/dbir/tree/gh-pages/2020
56  Interested in how we test them? Check out Chapter 9, Hypothesis Testing, of ModernDive: https://moderndive.com/9-hypothesis-testing.html

2020 DBIR   Appendices

108

Incident data
Our data is non-exclusively multinomial,
meaning a single feature, such as
“Action,” can have multiple values (i.e.,
“Social,” “Malware” and “Hacking”).
This means that percentages do
not necessarily add up to 100%.
For example, if there are five botnet
breaches, the sample size is five.
However, since each botnet used
Phishing, installed Keyloggers and
Used stolen credentials, there would
be five Social actions, five Hacking
actions and five Malware actions,
adding up to 300%. This is normal,
expected and handled correctly in our
analysis and tooling.

Another important point is that when
looking at the findings, “Unknown” is
equivalent to “unmeasured.” Which is
to say that if a record (or collection
of records) contain elements that have
been marked as “unknown” (whether it
is something as basic as the number
of records involved in the incident or as
complex as what specific capabilities a
piece of malware contained), it means
that we cannot make statements about
that particular element as it stands in
the record—we cannot measure where
we have no information. Because they
are “unmeasured,” they are not counted
in sample sizes. The enumeration
“Other” is, however, counted as it
means the value was known but not
part of VERIS or not included, as is the
case with “top” figures. Finally, “Not
Applicable,” (normally “NA”), may be
counted or not counted depending on
the hypothesis.

This year, we have made liberal use
of confidence intervals to allow us to
analyze smaller sample sizes. We have
adopted a few rules to help minimize
bias in reading such data. Here we
define “small sample” as less than
30 samples.

1

  Sample sizes smaller than five are
too small to analyze

2  We won’t talk about count or

percentage for small samples. This
goes for figures too and is why some
figures lack the dot for the median
frequency

3

 For small samples, we may talk
about the value being in some range,
or values being greater/less than
each other. These all follow the
hypothesis testing and confidence
interval approaches listed above

Incident eligibility
For a potential entry to be eligible for
the incident/breach corpus, a couple of
requirements must be met. The entry
must be a confirmed security incident,
defined as a loss of confidentiality,
integrity or availability. In addition
to meeting the baseline definition
of “security incident,” the entry is
assessed for quality. We create a
subset of incidents (more on subsets
later) that pass our “quality” filter.

The details of what is a “quality”
incident are:

1

 The incident must have at least seven
enumerations (e.g., threat actor
variety, threat action category,
variety of integrity loss, et al.) across
34 fields OR be a DDoS attack.
Exceptions are given to confirmed
data breaches with less than seven
enumerations

2  The incident must have at least one

known VERIS threat action category
(hacking, malware, etc.)

In addition to having the level of details
necessary to pass the quality filter,
the incident must be within the time
frame of analysis (November 1, 2018,
to October 31, 2019, for this report).
The 2019 caseload is the primary
analytical focus of the report, but the
entire range of data is referenced
throughout, notably in trending
graphs.57 We also exclude incidents
and breaches affecting individuals that
cannot be tied to an organizational
attribute loss. If your friend’s laptop
was hit with Trickbot, it would not be
included in this report.

Lastly, for something to be eligible
for inclusion into the DBIR, we have
to know about it, which brings us to
several potential biases we will
discuss below.

57  Our line figures use the calendar year the incident occurred in as they are continuous, while our dumbbell charts use the year of the DBIR report, as they are ordinal.

2020 DBIR   Appendices

109

Acknowledgement and
analysis of bias
Many breaches go unreported (though
not in our sample). Many more are as
yet unknown by the victim (and thereby
unknown to us). Therefore, until we (or
someone) can conduct an exhaustive
census of every breach that happens
in the entire world each year (our study
population), we must use sampling.58
Unfortunately, this process
introduces bias.

The first type of bias is random
bias introduced by sampling. This
year, our maximum confidence is
+/-1.5%59 for breaches and +/-0.5%
for incidents, which is related to our
sample size. Any subset with a smaller
sample size is going to have a wider
confidence margin. We’ve expressed
this confidence in the conditional
probability bar charts (the “slanted” bar
charts) that we have been using since
the 2019 report.

The second source of bias is sampling
bias. We strive for “the best obtainable
version of the truth”60 by collecting
breaches from a wide variety of
contributors. Still, it is clear that we
conduct biased sampling. For instance,
some breaches, such as those publicly
disclosed, are more likely to enter our
corpus, while others, such as classified
breaches, are less likely.

58  Interested in sampling? Check out Chapter 7, Sampling, of ModernDive: https://moderndive.com/7-sampling.html
59  This and all confidence intervals are 95% confidence intervals determined through bootstrap simulation.

Read more in Chapter 8, Bootstrapping and Confidence Intervals, of ModernDive: https://moderndive.com/8-confidence-intervals.html

60  Eric Black, “Carl Bernstein Makes the Case for ‘the Best Obtainable Version of the Truth,’” by way of Alberto Cairo, “How Charts Lie”

(a good book you should probably read regardless)

2020 DBIR   Appendices

110

HackingMalwareMisusePhysicalEnvironmentalErrorSocialFigure 135. Individual contributions per ActionExternalPartnerInternalFigure 136. Individual contributions per ActorServerUserDevKiosk/TermNetworkEmbeddedMediaPersonFigure 137. Individual contributions per AssetConfidentialityAvailabilityIntegrityFigure 138. Individual contributions per AttributeThe four figures at left are an attempt
to visualize potential sampling bias.
Each radial axis is a VERIS enumeration
and we have stacked bar charts
representing our data contributors.
Ideally, we want the distribution of
breaches to be roughly equally divided
between contributors in the stacked
bar charts along all axes. Axes only
represented by a single source are
more likely to be biased. However,
contributions are inherently thick tailed,
with a few contributors providing a lot
of data and many contributors providing
a few records within a certain area.
Still, we mostly see that most axes have
multiple large contributors with small
contributors adding appreciably to the
total incidents along that axes.

You’ll notice a rather large single
contribution on many of the axes. While
we’d generally be concerned about this,
it represents a contribution aggregating
several other sources, so not an actual
single contribution. It also occurs
along most axes, limiting the bias
introduced by that grouping of indirect
contributors.

The third source of bias is confirmation
bias. Because we use our entire
dataset for both exploratory analysis
as well as hypothesis testing, we
inherently test our hypotheses on the
same data we used to make them. Until
we develop a good collection method
for data breaches or incidents from
Earth-2 or any of the other Earths in the
multiverse,61 this is probably the best
that can be done.

As stated above, we attempt to mitigate
these biases by collecting data from
diverse contributors. We follow a
consistent multiple-review process
and when we hear hooves, we think
horse, not zebra.62 We also try to review
findings with subject matter experts in
the specific areas ahead of release.

Both subsets were separately analyzed
the last three years as well.

Finally, we create some subsets to
help further our analysis. In particular,
a single subset is used for all analysis
within the DBIR unless otherwise
stated. It includes only quality incidents
as described earlier and excludes the
aforementioned two subsets.

Data subsets
We already mentioned the subset
of incidents that passed our quality
requirements, but as part of our
analysis, there are other instances
where we define subsets of data.
These subsets consist of legitimate
incidents that would eclipse smaller
trends if left in. These are removed
and analyzed separately (as called
out in the relevant sections). This year,
we have two subsets of legitimate
incidents that are not analyzed as part
of the overall corpus:

1  We separately analyzed a subset of
web servers that were identified as
secondary targets (such as taking
over a website to spread malware)

2  We separately analyzed botnet-

related incidents

Non-incident data
Since the 2015 issue, the DBIR includes
data that requires the analysis that
did not fit into our usual categories of
“incident” or “breach.” Examples of
non-incident data include malware,
patching, phishing, DDoS and other
types of data. The sample sizes for
non-incident data tend to be much
larger than the incident data, but from
fewer sources. We make every effort
to normalize the data (for example,
weighting records by the number
contributed from the organization so all
organizations are represented equally).
We also attempt to combine multiple
partners with similar data to conduct
the analysis wherever possible. Once
analysis is complete, we try to discuss
our findings with the relevant partner
or partners so as to validate it against
their knowledge of the data.

61  The DBIR is a pre-Crisis on Infinite Earths work environment.
62  A unique finding is more likely to be something mundane (such as a data collection issue) than an unexpected result.

2020 DBIR   Appendices

111

Appendix B: VERIS
Common Attack
Framework (VCAF)

VERIS was developed as a
solution to the need for
consistent definitions of
incident and breach data
for analysis.
With its close ties to the DBIR and data
analysis, it was created to remove the
ambiguity inherent in terms surrounding
breaches and provide a data-driven
structure capable of quantifying the
majority of breaches. While VERIS
covers a lot of different detailed
information about an incident, including
things such as Victim demographics
and Timeline, the core of VERIS is
captured in what we call the four
“A’s” of an incident: Actor, Action,
Asset, Attribute.

However, VERIS was not designed
to represent precise and detailed
tactical and technical minutiae around
attackers’ techniques, chosen methods
of persistence or methodology
for executing malicious code on a
compromised asset. Thankfully, it
doesn’t need to because there is
something else that has come along to
help address that need.

Massive (adoption of) ATT&CK
MITRE privately developed the original
Adversarial Tactics, Techniques and
Common Knowledge (ATT&CK)
framework starting in 2013 as a means
of codifying adversarial behavior and
released it publicly in 2015.63 ATT&CK
has become a well-established way for
describing the tactical actions used by
attackers (including a heavy focus on

advanced threats). Much like VERIS,
ATT&CK is subdivided into a handful
of key components, but the core of
the framework are the “Techniques,”
which describe the atomic means of
how an attacker achieves an objective
called a “Tactic.” The 260+ Techniques
in ATT&CK for Enterprise are logically
grouped with their corresponding 11
Tactics, which describe the different
objectives an adversary might take as
part of their intrusion.

We’re better when
we’re together.
While both VERIS and ATT&CK grew
out of different needs and different
objectives, VERIS to codify incidents
and ATT&CK to codify adversary
technique, there is without a doubt an
overlap between the two that could
be leveraged to improve the value
of both standards. To get a better
understanding of the relationships
between these two frameworks, the
team spent some time researching
to see if they could map the VERIS
framework to the ATT&CK techniques
and vice-versa, the results of which
you can see in Figure 139.

What is this, a crossover
episode?
Our solution to bridge the gap and help
operationally connect the relationships
between ATT&CK and VERIS is through
the creation of an extension that we
call the VERIS Common Attack
Framework (VCAF).

63 https://www.mitre.org/sites/default/files/publications/pr-18-0944-11-mitre-attack-design-and-philosophy.pdf
64 But they sure have a large impact!

VCAF serves as a bridge to ATT&CK,
covering the portions of VERIS not
in ATT&CK with the aim of creating a
holistic framework. At its very core,
VCAF is made of two components: one
is the conceptual mapping between
VERIS and ATT&CK, and another is the
extension of ATT&CK with techniques
that cover all possible Threat Actions
present in VERIS. As much as we
would have liked to leverage a default
“meteor falling from the sky” technique
in ATT&CK, those events are definitely
quite rare.64

This approach should be flexible
enough to accommodate both general
categories found in VERIS (such as
Ransomware) and some of the more
specific attack types found either
in VERIS or ATT&CK. Aside from
expanding the scope of what is covered
and can be tracked, using VCAF can
help provide essential context to these
incidents. Below is a list that includes
a variety of the different benefits of
leveraging this powerful combination:

•  Understand the technical details

associated with an incident

•  Prioritize mitigations based on

previous all incident types (not just
the malware or hacking kind)

•  Better understand the junction of

targeting and capabilities

•  Capture incident context that goes

beyond technical artifacts

•  Ease communication of

cybersecurity concepts with
non-cybersecurity experts

2020 DBIR   Appendices

112

45%

9%

9%

0%

25%

50%

75% 100%

6%

6%

22%

82%

15%

46%

46%

49%

63%

86%

53%

100%

100%

100%

93%

2%

55%

91%

64%

75%

55%

68%

36%

59%

s
s
e
c
c
a
-
l
a
i
t
i
n

I

n
o
i
t
u
c
e
x
E

e
c
n
e
t
s
s
r
e
P

i

l

n
o
i
t
a
a
c
s
e
-
e
g
e

l
i

v
i
r
P

y
r
e
v
o
c
s
D

i

i

n
o
s
a
v
e
-
e
s
n
e
f
e
D

s
s
e
c
c
a
-
l
a
i
t
n
e
d
e
r
C

t
n
e
m
e
v
o
m

-
l
a
r
e
t
a
L

n
o
i
t
c
e

l
l

o
C

Figure 139. Percentage of MITRE Techniques covered by VERIS

7%

14%

t
c
a
p
m

I

11%

n
o
i
t
a
r
t
l
i
f
x
E

5%

l

o
r
t
n
o
c
-
d
n
a
-
d
n
a
m
m
o
C

Social

Physical

Misuse

Malware

Integrity

Hacking

Error

In this issue of the DBIR, we used
VCAF to map simulated breach data,
SIEM data and malware features to
VERIS action categories to compare
and draw conclusions in conjunction
with our incident corpus.

The beginning of
something great
Clearly, VCAF is not the end-all be-
all of cybersecurity frameworks. It
is a modest step toward having an

integrated way for the community
to discuss security incidents
and attackers. As the number of
cybersecurity frameworks grows and
the field of knowledge surrounding
cybersecurity topics deepens, there
is a need for us as a community to
integrate our own languages and
understanding in an effort to help us
communicate to the larger community
of non-cybersecurity experts. Keep your
eyes peeled for future developments
and information on VCAF by visiting65
our VERIS GitHub page at https://github.
com/vz-risk/veris.

65  And don’t forget to smash that like and subscribe button!

2020 DBIR   Appendices

113

Appendix C

Michael D’Ambrosio
Assistant Director
U.S. Secret Service

Jonah Force Hill
Senior Cyber Policy Advisor
U.S. Secret Service

Following the money—the key
to nabbing the cybercriminal

This year’s DBIR has once again highlighted the principal motive for the vast
majority of malicious data breaches: the pursuit of profit. This is surprising to
some, given the extensive media coverage of national security-related breaches.
However, it should not be. Most malicious cyber actors are not motivated by national
security or geopolitical objectives, but rather by simple greed. Cybercriminals
primarily profit through fraud and extortion. They target financial and payment
systems, steal information to use in various fraud schemes, and hold IT systems
hostage through ransomware and other means. Whatever their criminal scheme,
they then depend upon a money movement and laundering apparatus to transfer
and liquidate their proceeds.

That is why the U.S. Secret Service was first assigned responsibility for
investigating cybercrimes in the early 1980s, before it was even called “cyber,”
and why we continue to do so today. Secret Service agents are financial crimes
investigators, skilled not only at “following the money,” but at preventing criminals
from profiting from their activities and at recovering the stolen assets of victims.
When investigating any criminal cyber incident, a data breach, an “unlimited ATM
cash-out” conspiracy, a ransomware attack or any other diverse, financially motived
crime committed via the internet, the heart of the Secret Service’s approach is
following the money.

We have learned over the decades that it is through the movement of funds—from
the victim to the criminal, between and among criminals, and through the process of
money laundering—that investigators are able to generate the greatest insights and
criminal leads. Malware samples and indicator sharing are useful, no doubt, but it is
the money and where it moves that leads to arrests, asset seizures and the recovery
of assets stolen from victims of fraud.

For example, in a typical business email compromise (BEC) scheme, a victim is lured
into sending a payment, usually via a wire transfer, to a bank account maintained
under a criminal’s control. The methods used in the deception part of the crime
can range from highly sophisticated (such as deploying tailor-made malware)
to shockingly simple (such as impersonating a vendor on the phone). How the
fraudsters fool the victim is often insignificant; what is important is how they move
and liquidate their proceeds.

2020 DBIR   Appendices

114

Smart criminals understand this.
They know that the accounts, shell
companies and processes they use
to move their stolen funds contain
a wealth of location data and other
information that can lead to their arrest.
As a result, criminals try to distance
themselves and their identities from all
accounts and institutions that might be
associated with their crimes.

There are number of ways criminals
do this, but one of the principal
mechanisms is the use of “mules,”
outside individuals recruited to
participate in the scheme. Mules can be
either witting or unwitting participants.
Some mules join the scheme with full
knowledge of the criminal nature of
their involvement; others are recruited
through what appear to be legitimate
job postings. Still others are victims
themselves of ancillary frauds, often
romance scams, in which they are
conned into believing that they are
sending money to a romantic partner,
when in fact they are just moving
money for crooks.

A similar dynamic exists in cases
of ransomware and in other crimes
in which cryptocurrencies play a
role. When an organization pays a
ransom to unlock its IT systems,
for instance, the criminal generally
instructs the victim to send a bitcoin
payment to a cryptocurrency wallet.

These wallets are hosted either on a
cryptocurrency exchange, which can
be either legitimate or illegitimate, or
on a device operated by the criminal or
an associate. Here too, the criminals
seek to obscure the location of the
wallets and to limit access to any other
information that might tie their activities
to a specific wallet or account.

Criminals engaged in ransomware
attacks employ many of the same
techniques as BEC scammers to cover
their tracks. They may pay mules to
set up crypto wallets, or con unwitting
mules into thinking they have landed
a legitimate job in the cryptocurrency
industry. They may use cryptocurrency
tumblers and mixers to swap funds
from one form of cryptocurrency to
another (for instance, from bitcoin
to ether), to keep law enforcement
from tracking their movements on
the blockchain. They may set up shell
companies, open overseas bank
accounts and move money repeatedly
from one country to the next, all
with the aim of making their financial
movements as difficult as possible
to trace.

Yet there is always a chokepoint. If
cybercriminals want to enjoy the fruit of
their criminal labor, they must convert
their profits into a form of money they
can actually use, without being tracked
by law enforcement. These chokepoints

create the greatest opportunities to
counter cybercriminal activity.

The Secret Service focuses on these
chokepoints to disrupt these financial
flows, whether they are explicitly illicit
services or legitimate businesses that
are exploited by criminals. Through
undercover operations, confidential
informants and partnerships with
industry and the broader law
enforcement community, the Secret
Service excels at identifying and
interdicting these illicit financial flows.
In 2019, the Secret Service prevented
$7.1 billion of cybercrime losses and
returned over $31 million in stolen
assets to victims of fraud.

The lessons for industry are simple:
Invest in the defense of your networks
and, in the event of a breach, collect
as much evidence as you can. When
shared with law enforcement partners,
that evidence can lead not only to the
arrest of the criminal, but also to the
seizure of their assets. In many cases,
the recovered money can be returned
to the victim. This is how we prevent
cybercriminals from operating with
impunity. It is a collective struggle.
Let’s work together.

2020 DBIR   Appendices

115

Appendix D

Diego Curt
Chief Compliance Officer
State of Idaho, Office of the Governor—
Information Technology Services

State of Idaho enhances incident
response program with VERIS.

We hear it all the time. We need to share incident and breach information for
improved decision-making. The State of Idaho was facing the same issue, trying
to get different agencies to share incident and breach information for improved
decision-making and better cyber-defense investment. In order to address this, the
State of Idaho designed a program that gained approval from various stakeholders,
including the legal department. The program consists of two fundamental
components and three core components.

The two fundamental components are:

1  Cyber Kill Chain®66 developed by Lockheed Martin, Inc.—used to promote

actionable intelligence-process thinking and serves as a blueprint for building
an effective cybersecurity program

2   National Institute of Standards and Technology (NIST) Cybersecurity

Framework67—a risk reporting framework used to assess the readiness and
maturity of cybersecurity controls throughout the enterprise

The three core components of the program are:

1  NIST SP 800-5368 Incident Response Control Family—used to govern and

ensure all control processes are addressed and matured on a continuous basis

2  Vocabulary for Event Recording and Incident Sharing (VERIS)—an easy-to-use,
systematically structured language/taxonomy used to gather intelligence from
incidents and breaches for better decision-making and information sharing

3  A commercial web-based application that brings together first responders,

emergency management, National Guard, cyber-incident response handlers, etc.,
into one platform that houses the VERIS language/taxonomy

66 https://www.lockheedmartin.com/en-us/capabilities/cyber/cyber-kill-chain.html
67  https://www.nist.gov/cyberframework
68 https://nvd.nist.gov/800-53

2020 DBIR   Appendices

116

•  It provides a way for business

executives to get involved with their
organization’s cybersecurity efforts
and simplifies intelligence gathering
by repetitively asking four basic
questions: Whose actions affected
the asset? What actions affected the
asset? Which asset was affected?
How was the asset affected?

VERIS provides a solid language
foundation that can be used to build
a strong intelligence-driven incident
response program. Couple that with
other open source frameworks and
you have one heck of an incident
response program.

At the heart of the program is the
VERIS taxonomy. VERIS is a language/
taxonomy designed to help an
organization hurdle over the issues
many organizations are concerned
about—sharing confidential data with
outsiders. Without the capability to
incorporate a common language
(VERIS) designed to share incident
information, the State of Idaho would
never have been able to gain approval
from various stakeholders (including
the legal department) to share incident
and breach information both internally
(other agencies) and externally (DHS,
FEMA, etc.).

Some of the areas in which VERIS has
helped improve the State of Idaho’s
ability to share information are:

•  It has created awareness and interest
that there is a better way to gather
and use intelligence information from
adverse events that we respond to
from time to time

•  It is an open source framework

that works well with other incident
response frameworks

•  It is an easy-to-use full-schema

taxonomy/language designed to be
incorporated and implemented within
a short period of time

2020 DBIR   Appendices

117

Appendix E:
Contributing
organizations

A
Akamai Technologies
Apura Cyber Intelligence
AttackIQ
Australian Federal Police

B
BeyondTrust
Bit Discovery
Bit-x-bit
BitSight

C
Center for Internet Security
CERT European Union
CERT Insider Threat Center
CERT Polska
Check Point Software Technologies Ltd.
Chubb
Cisco Talos Incident Response
Coalition (formerly BinaryEdge)
Computer Incident Response Center
Luxembourg (CIRCL)
CrowdStrike
Cybercrime Central Unit of the Guardia
Civil (Spain)
CyberSecurity Malaysia, an agency
under the Ministry of Science,
Technology and Innovation (MOSTI)

D
Defense Counterintelligence and
Security Agency (DCSA)
Dell (formerly EMC-CIRC)
DFDR Forensics
Digital Shadows
Dragos, Inc.

E
Edgescan
Elevate Security
Emergence Insurance

F
F-Secure (formerly MWR InfoSecurity)
Federal Bureau of Investigation—
Internet Crime Complaint Center (FBI IC3)
Financial Services Information
Sharing and Analysis Center (FS-ISAC)

G
Government of Telangana, ITE&C
Dept., Secretariat
Government of Victoria, Australia—
Department of Premier and Cabinet (VIC)
GreyNoise

H
Hasso-Plattner Institut
Hyderabad Security Cluster

I
ICSA Labs
Irish Reporting and Information
Security Service (IRISS-CERT)

J
JPCERT/CC

K
Kaspersky
KnowBe4

L
Lares Consulting
LMG Security

M
Malicious Streams
Micro Focus (formerly Interset)
Mishcon de Reya
mnemonic
Moss Adams (previously AsTech Consulting)

N
National Cybersecurity and
Communications Integration Center (NCCIC)
NetDiligence
NETSCOUT

P
Paladion Networks Pvt Ltd.
Palo Alto Networks
ParaFlare Pty Ltd
Proofpoint (formerly Wombat Security)

Q
Qualys

R
Rapid7
Recorded Future

S
S21sec
SecurityTrails
Shadowserver Foundation
Shodan
SISAP—Sistemas Aplicativos
SwissCom

T
Tetra Defense (formerly Gillware
Digital Forensics)
Tripwire

U
United States Computer Emergency
Readiness Team (US-CERT)
U.S. Secret Service

V
VERIS Community Database
Verizon Cyber Risk Programs
Verizon DDoS Shield
Verizon Digital Media Services
Verizon Managed Security Services—
Analytics (MSS-A)
Verizon Network Operations and Engineering
Verizon Professional Services
Verizon Threat Research Advisory
Center (VTRAC)
Vestige, Ltd.
VMRay

W
Wandera
WatchGuard Technologies

Z
Zscaler

2020 DBIR   Appendices

118

BIT
DISCOVERY

Security Awareness Training

2020 DBIR   Appendices

119