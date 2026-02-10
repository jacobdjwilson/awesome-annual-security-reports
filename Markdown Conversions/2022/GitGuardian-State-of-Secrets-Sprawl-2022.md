# THE STATE OF
# SECRETS SPRAWL

↑

# Occurrences of secrets detected per AppSec
engineer in 2021

The growing problem of secrets sprawling
in corporate repositories can only be
solved by enabling collaboration
between AppSec and Developers.

↑

It’s safe to say that 2021
will go down in history
for cybersecurity experts.
Ransomware and other large-scale cyberattacks (SolarWinds,
Colonial Pipelines) or vulnerabilities (Log4Shell) have made
headlines around the world. Software supply chain attacks
have seen their number explode, and this comes as no surprise
considering the plethora of vulnerabilities and misconfigurations
found across software development environments.

Unsurprisingly, a lot of attacks start with the compromise of a leaked
secret. Credentials are a nightmare for security engineers because
they can end up in so many places: build, monitoring,
or runtime logs, stack traces, and … git history. Our data show
the extent of publicly exposed secrets on GitHub has more than
doubled since 2020. The problem is not bound to this particular
platform, as revealed by our Docker Hub analysis.

In 2020, GitGuardian started monitoring private repositories as well,
which granted us a unique insight into what really happens behind
the scenes.

The data reveals that on average, in 2021, a typical company with
400 developers would discover 1,050 unique secrets leaked upon
scanning its repositories and commits. With each secret detected
in 13 different places on average, the amount of work required
for remediation far exceeds current AppSec capabilities:
with a security-to-developers ratio of 1:100*, 1 AppSec engineer
needs to handle 3,413 secrets occurrences on average.

This comforted our view that the only way to address the challenge
of secrets sprawling within corporate repositories is to enable
a shared responsibility between AppSec and Devs.

* From TAG Cyber, see Methodology

GitGuardian · State of Secrets Sprawl

# Summary

04

# Definitions

07

# Public
# Monitoring

# How leaky was 2021?

15

# Internal
# Monitoring

# Security teams
# are overwhelmed

A false sense
# of secrecy

# Recommendations

# Developer
# in the Loop

# Solving the problem
# of secrets sprawl

# Let’s conclude

# About GitGuardian

# Methodology

# Appendix

05

08

09

10

11

13

14

17

18

20

21

22

23

24

25

27

GitGuardian · State of Secrets Sprawl

# Definitions

05

# Secret

A secret can be any sensitive data that we want to keep private.
When discussing secrets in the context of software development,
we refer to digital authentication credentials that grant access to
services, systems, and data. These are most commonly API keys,
usernames and passwords, or security certificates.

# Secret
# incident

A secret incident is a uniquely identified security event that has
been determined to have an impact on the organization and
necessitates remediation. An incident often has multiple
occurrences across files or repositories.

# Secret
# occurrences

A single incident generally encompasses multiple occurrences,
which are the various locations across files or repositories where
the secret was identified. Occurrences map to the magnitude of
the sprawl, and are therefore correlated to the amount of work
needed to redistribute the secret after it has been rotated.
Occurrences can be assimilated to technical debt.

# Secrets
# sprawl

Unlike traditional credentials, secrets are meant to be distributed
to developers, applications, and infrastructure systems. Adding
more of these factors will inevitably make the number of secrets
used in a development cycle increase, leading to a natural
sprawling phenomenon: secrets start to appear hardcoded in
source code. From an organization’s point of view, visibility and
control over their distribution start to degrade. This is what
secrets sprawl is all about.

GitGuardian · State of Secrets Sprawl

Source code is a huge
wealth of knowledge.
It also happens to
exist on pretty much
every developer’s
workstation, which
they probably take
home with them. You
probably don’t want
your secrets being all
over the country.

Don, Security engineer

↑

GitGuardian · State of Secrets Sprawl
# Public
# Monitoring

ON GITHUB

56M  users

+25% repositories created last year

*from the state of the Octoverse 2021

+23%

commits scanned by GitGuardian

# How leaky was 2021?

Over 6M secrets  detected in 2021

2x  increase compared to 2020

On average, 3 commits out of 1,000 exposed at least one secret,

+50 % compared to 2020 *

* see Methodology

SECRETS BY CATEGORY

r
e
h
t
O

32.8%

e
g
a
r
o
t
s
a
t
a
D

21%

r
e
d
i
v
o
r
p
d
u
o
C

l

15.2%

y
e
k
e
t
a
v
i
r
P

l

o
o
t
t
n
e
m
p
o
e
v
e
D

l

m
e
t
s
y
s
g
n
g
a
s
s
e
M

i

9.6%

9.5%

8.5%

08

m
r
o
f
t
a
l
p

l

o
r
t
n
o
c
n
o
i
s
r
e
V

%
4
1

.

↑

Public MonitoringGitGuardian · State of Secrets Sprawl
# Leaks correlate
# to popularity

It should come as no surprise that leaks are proportional to user
adoption, and this is especially true for newcomers rapidly gaining
in popularity.

Supabase, which has consistently ranked in GitHub’s top-20
fastest-growing open-source startups and launched 50,000
databases in 2021 only, is a telling example. Another one is
PlanetScale, a serverless database platform released in 2021 Q4,
which immediately started appearing on our radars.

EVOLUTION OF THE NUMBER OF DETECTED SECRETS IN 2021

PLANETSCALE

SUPABASE

S
T
I
M
M
O
C
K
0
1
R
E
P
S
T
E
R
C
E
S
D
E
T
C
E
T
E
D
F
O
R
E
B
M
U
N

1

0.75

0.5

0.25

0

JAN

FEB

MAR

APR

MAY

JUN

JUL

AUG

SEP

OCT

NOV

DEC

↑

Public MonitoringGitGuardian · State of Secrets Sprawl
# Scanning Docker Hub

When it comes to open-source, GitHub certainly is the first
platform that comes to mind. Yet it is not the only resource for
code-sharing. Since Docker popularized the use of containers to
package apps, its official public registry, Docker Hub, has become
another developers’ favorite.

It’s therefore not surprising to find secrets in Docker Hub.

The layers making up Docker images are as many additional attack
surfaces that can too easily be left out of the security perimeter.
For attackers, it is yet another chance of finding an access vector,
just as demonstrated by the Codecov breach.

Docker Hub = 8.8M Docker images publicly available

This motivated us to conduct our first study on the extent of
secrets sprawl in Docker Hub a few months ago. To deepen this
first estimation, we reiterated the exercise, this time with a 5x
larger sample. Here are our results:

4.62%

of the images expose at least one secret

10K

images scanned

4K

secrets

1.2K

unique

6

secrets

EVERY

100

layers

↑

Public MonitoringGitGuardian · State of Secrets Sprawl
# Fun facts!

Leaks mostly happen
on weekends…

DIFFERENCE IN SECRETS/COMMIT FOUND ACROSS THE WEEK

4%

2%

0%

-2%

-4%

40%

30%

20%

10%

0%

MON

TUE

WED

THUR

FRI

SAT

SUN

The worst day of 2021 was
 Saturday, November 20th
(+66% secrets/commit)

If we exclude weekends, most leaks happen
on holidays…

WORST DAYS OF THE YEAR, EXCLUDING WEEKENDS (∆ SECRETS/COMMIT)

%
9
3

%
1
3

%
1
3

%
8
2

%
7
2

%
4
2

%
4
2

%
3
2

AUG 21

JUL 27

JUL 23

AUG 18

AUG 20

JUL 6

MAR 23

JUL 26

↑

Public MonitoringGitGuardian · State of Secrets Sprawl
We found more than

500 commit
messages

containing GitHub

personal access tokens!

12

↑

Public MonitoringGitGuardian · State of Secrets Sprawl
# Public Monitoring

13

# Where leaks
# come from

01

02

03

04

05

06

07

08

09

10

India

USA

Germany

France

Indonesia

Russia

Nigeria

Bangladesh

Brazil

UK

GitGuardian · State of Secrets Sprawl

↑
↑

GitGuardian · State of Secrets Sprawl
# 2021 breaches
# involving secrets leaks

14

Codecov

Twitch

Indian
government

A favorite of many open-source projects, Codecov is a code
coverage tool. Between January 31st and April 1st, it was
compromised by attackers who were able to extract all of the
environment variables of Codecov’s customers. Initial access was
obtained by extracting a static GCP service account credential
from one layer of Codecov Docker image, which allowed them to
tamper with a downstream CI script. Attackers were thus able to
piggyback on Codecov to enter its users’ private code repositories,
exposing many more secrets. Read the full play-by-play.

While most of the media attention has been focusing on
streamers’ revenues, GitGuardian conducted a deep-dive review
to inspect the 6,000 git repositories of the Twitch codebase leaked
this year. Despite lots of evidence demonstrating a certain level of
AppSec maturity, nearly 7,000 secrets were uncovered, including
hundreds of AWS, Google, Stripe, and GitHub keys. We triaged
these secrets to explain how a malicious actor could easily
leverage just a few of them to get a foothold into critical systems.
To be fair, we found it quite disturbing that the main narrative
about this leak was that it didn’t present a security risk since no
significant customer data was leaked. It simply shows that the
problem of secrets sprawl is largely underplayed, even by some
security experts.

When white hat group Sakura Samurai started to scrutinize official
Indian government endpoints under a vulnerability disclosure
program, it didn’t take them too long to find leaked credentials
inside public-facing .git directories. In the end, 35 separate
instances of exposed credential pairs were reported, indicating a
massive breach affecting government systems. As detailed in our
play-by-play, the attack itself followed a well-proven
methodology that is of relatively low sophistication, making it
accessible to the widest range of hackers.

↑

Public MonitoringGitGuardian · State of Secrets Sprawl
# Internal
# Monitoring

In 2020, GitGuardian launched Internal Repositories
Monitoring for Enterprise.

Monitoring thousands of repositories in real-time
and scanning for the entire history of corporate
codebases, we gained a realistic view of the state of
application security in the DevOps era.

If there is a single conclusion to be drawn from the
data, it is that

the amount of work required

for both remediating

real-time incidents and

investigating leaks detected

in the git history (which can

still represent a threat) far

exceeds current AppSec

teams' capabilities.

↑

16

Secrets detection is a very
essential part of security.
It’s one of the basics that
you need to cover all the
time. Otherwise, you’re
going to expose your
endpoints online and you’re
going to suffer endless
attacks. When it comes to
application development,
secrets detection is
essential to a security
program. You need to have
it. Otherwise, you’ll fail.

Abbas Haidar, Head of InfoSec

↑

Internal MonitoringGitGuardian · State of Secrets Sprawl
# Security teams
# are overwhelmed

On average, in 2021, a typical company with 400 developers
and 4 AppSec engineers would discover

1,050 unique secrets leaked
upon scanning its repositories and commits.

With each secret detected in 13 different places on average,
the amount of work required for remediation far exceeds
current AppSec teams capabilities (1 AppSec engineer
for 100 developers)*.

* From TAG Cyber, see Methodology

1 AppSec engineer needs to handle

3,413

secrets occurrences
on average

17

↑

Internal MonitoringGitGuardian · State of Secrets Sprawl
# A false sense
# of secrecy

Our intuition that private repositories permeate a false sense of
secrecy, causing even more leaks to occur compared to public
ones, could be confirmed:

On average, private repositories are 4x
more likely to reveal at least one incident.

Not only private repositories are more likely to be affected, but
they also reveal the real magnitude of secrets sprawl:

INCIDENTS DETECTED ON PUBLIC REPOSITORIES ARE ONLY THE TIP OF THE ICEBERG

PUBLIC

PRIVATE

25

20

15

10

5

0

MICROSOFT AZURE
STORAGE ACCOUNT KEY

AWS KEYS

SALESFORCE OAUTH2 KEYS

OKTA TOKEN

AVERAGE NUMBER OF INCIDENTS PER ENTERPRISE REPOSITORY (SCANNED IN 2021) PER DETECTOR

18

↑

Internal MonitoringGitGuardian · State of Secrets Sprawl
I think people are getting more

aware of secrets. [ ...]

I think that it has had a positive

impact on the culture itself.

You’re only as good as the

software you write, and you’re

in for a world of hurt if you put

the keys to the castle inside of

that source code that could be

somehow reverse-engineered.

By separating the two, the

source code and the keys,

you’re one step ahead of that.

I think it’s essential.

Blake, DevSecOps engineer

↑

Internal MonitoringGitGuardian · State of Secrets Sprawl
# Recommendations

Private repositories fall too often victim of secrets sprawl,
threatening security efforts and creating unnecessary
remediation needs.

To prevent codebases from becoming hackers’ playgrounds
without overwhelming security teams, the focus needs to shift to
collaborative prevention.

Secrets leaking in source code is unavoidable, but like other
vulnerabilities, it is completely determined by endogenous
factors: more developers, requiring access to more resources,
building and deploying at a faster rate.

It means that with enough

discipline and education, coupled

with the right tools, it is possible to

drastically improve the situation,

just like any technical debt.

20