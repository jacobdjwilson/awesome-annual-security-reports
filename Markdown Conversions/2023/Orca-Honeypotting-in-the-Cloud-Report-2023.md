```markdown
# in the Cloud Report

## Table of Contents
- [Foreword](#foreword)
- [About the Orca Research Pod](#about-the-orca-research-pod)
- [Executive Summary](#executive-summary)
- [Methodology](#methodology)
- [Research Findings](#research-findings)
- [GitHub Honeypot](#github-honeypot)
- [AWS S3 Bucket Honeypot](#aws-s3-bucket-honeypot)
- [SSH Honeypot](#ssh-honeypot)
- [HTTP Honeypot](#http-honeypot)
- [DockerHub Honeypot](#dockerhub-honeypot)
- [ECR Honeypot](#ecr-honeypot)
- [Elasticsearch Honeypot](#elasticsearch-honeypot)
- [Amazon EBS (AMI) Honeypot](#amazon-ebs-ami-honeypot)
- [Redis Honeypot](#redis-honeypot)
- [Summary](#summary)
- [Key Recommendations](#key-recommendations)
- [About Orca Security](#about-orca-security)

Aacker Tactics and Techniques Revealed

Inside This Report

[Foreword](#foreword)

[About the Orca Research Pod](#about-the-orca-research-pod)

[Executive Summary](#executive-summary)

[Methodology](#methodology)

[Research Findings](#research-findings)

[1. GitHub Honeypot](#github-honeypot)

[2. AWS S3 Bucket Honeypot](#aws-s3-bucket-honeypot)

[3. SSH Honeypot](#ssh-honeypot)

[4. HTTP Honeypot](#http-honeypot)

[5. DockerHub Honeypot](#dockerhub-honeypot)

[6. ECR Honeypot](#ecr-honeypot)

[7. Elasticsearch Honeypot](#elasticsearch-honeypot)

[8. Amazon EBS (AMI) Honeypot](#amazon-ebs-ami-honeypot)

[9. Redis Honeypot](#redis-honeypot)

[Summary](#summary)

[Key Recommendations](#key-recommendations)

[About Orca Security](#about-orca-security)

3

4

6

10

11

12

17

22

24

25

26

27

28

29

31

36

41

2

<a name="foreword"></a>
# Foreword

"Know thy enemy and know

yourself; in a hundred bales,

you will never be defeated.”

Chinese general Sun Tzu.

In an era where cloud computing has become an integral

part of modern business operations, ensuring the security of

cloud environments is of paramount importance. Cybercriminals

are relentlessly seeking to exploit vulnerabilities and

misconﬁgurations to gain unauthorized access to valuable

resources. The more security teams can understand aacker

tactics and techniques, the more eective they will be at

defending themselves.

For this purpose, the Orca Research Pod launched a honeypot

research project to simulate misconﬁgured resources in the

cloud, and then monitor whether bad actors would take the bait

while shedding light on the latest aack vectors and providing

essential insights for fortifying cloud defenses.

3

<a name="about-the-orca-research-pod"></a>
# About the Orca Research Pod

![14+ vulnerabilities discovered on AWS, Azure, and Google Cloud]

The Orca Research Pod is a group of cloud security
researchers that discover and analyze cloud risks
and vulnerabilities to strengthen the Orca Cloud
Security Platform and promote cloud security best
practices. In addition, the Orca research team
discovers and helps resolve vulnerabilities in cloud
provider platforms so organizations can rely on a safe
infrastructure in the cloud.

2021

1. AWS Superglue
2. Azure AutoWarp
3. AWS BreakingFormation
4. Databricks

2022

1. Azure SynLapse
2. Azure FabriXxs
3. Azure CosMiss
4. Azure Digital Twins SSRF
5. Azure Functions App SSRF
6. Azure API Management SSRF
7. Azure Machine Learning SSRF
8. Azure Super FabriXss

2023

1. Azure Storage Account Keys

Exploitation Path

2. Two Azure PostMessage IFrame

Vulnerabilities

4

Copyright Orca Security 2023
Orca Security, Highly
Conﬁdential

![Bar Kaduri]

Bar Kaduri

Threat Research Team Leader, Orca Security

![Tohar Braun]

Tohar Braun

Research Technical Lead, Orca Security

The goal of our honeypot research was to

ﬁnd out the following:

Which of the popular cloud services are most frequently targeted by aackers?

How long does it take for aackers to access public or easily accessible resources?

How long does it take for aackers to ﬁnd and use leaked secrets?

What are common aack routes and methods?

How can we leverage this information to increase defenses?

This research aims to equip

cloud security professionals, DevOps,

DevSecOps, CISOs, and development

leaders with valuable insights and practical

recommendations for safeguarding their cloud

environments, and in doing so, help to secure

the cloud for everyone.

5

Copyright Orca Security 2023

<a name="executive-summary"></a>
# Executive Summary

1

Discovery is fast

In some ways, our study conﬁrmed what is already widely
known: aackers are constantly scanning the Internet
for lucrative opportunities. What did surprise us however
was how fast this was happening:

On GitHub, aackers weaponized our leaked keys within minutes. It

only took 2 minutes until one of our GitHub honeypot keys was

used.

The ﬁrst access to our HTTP honeypot was within 3 minutes.

We saw access to our SSH honeypot within 4 minutes. There were

no aempts to use the key we planted, but we saw hundreds of

aempts to install malware and cryptominers on our server.

Our S3 Buckets were accessed in one hour and the keys were used

within 8 hours.

It took aackers..

2 minutes
to exploit keys exposed on GitHub

3 minutes
to access our HTTP Honeypot

4 minutes
to access our SSH Honeypot

1 hour
to access our S3 Buckets

6

Copyright Orca Security 2023
Orca Security, Highly
Conﬁdential

# Executive Summary

Time to Asset Access

2

Aackers target each
resource dierently

The more popular the resource, the easier it is to
access, and the more likely it is to contain
sensitive information -> the more aackers will
do (automatic) reconnaissance.

Certain assets, such as SSH, are highly targeted for

malware and cryptomining. We saw hundreds of

aempts by aackers to install malware and

cryptominers on our SSH honeypot.

Even though public assets on some resources are discovered much
faster than others, it’s clear that wherever you store public data, it
will be compromised at some point - whether it’s in minutes, hours,
days, or months.

2

3

4

1

2 mins
GitHub

3 mins
HTTP

4 mins
SSH

1 hour
S3 Bucket

2

2.5

4

2 hours
Elasticsearch

2.5 hours
Redis

4 months
AWS ECR

No aempts to access:
DockerHub or Amazon EBS

Time to Key Usage

2

8

4

2 mins
GitHub

8 hours
S3 Bucket

4 months
AWS ECR

No aempts to use the keys on:
HTTP, SSH, Elasticsearch, or Redis

7

Copyright Orca Security 2023
Orca Security, Highly
Conﬁdential

# Executive Summary

3

Automated key protection
cannot be relied on

AWS keys were automatically locked
down on GitHub, but..

Secrets are automatically locked down on GitHub but not on any
of the other resources, such as ECR and S3 Buckets.

Even though permissions of the leaked keys were
locked down as soon as the git push occurred..

Except for the breached keys from AWS in GitHub, no keys were
reported as breached, despite the fact that some of them were used by
unauthorized users.

Even if key permissions are locked down (as they were on GitHub), the
key is not entirely blocked. Although the policy denies most
permissions, an aacker can potentially still perform malicious actions
on some services, such as RDS, EKS, and Elasticsearch.

This means that defenders need to be extra careful not to include
secrets on S3 Buckets, and to a lesser extent Elastic Container Registry,
since we also saw relatively fast key usage from these resources.

Using the AWS Compromised Key policy, which
denies access to destructive actions..

Even with this policy applied, if the leaked
credentials have a lot of permissions, an aacker
can still do damage.

8

Copyright Orca Security 2023
Orca Security, Highly
Conﬁdential

# Executive Summary

4

No region is safe

Although we saw 50% of the AWS key
exploitation in the US, usage also occurred in
almost every other region, including Canada,
Asia Paciﬁc, Europe, and South America.

As more and more
organizations around the
world adopt the cloud,
aackers are not just sticking
to North America, but are
opportunistically targeting
every possible region.

AWS regions where API calls were
made with leaked keys on GitHub:

Canada

3%

South America

4%

Europe 20%

Asia Paciﬁc 23%

United States 50%

9

Copyright Orca Security 2023
Orca Security, Highly
Conﬁdential

<a name="methodology"></a>
# Methodology

The purpose of this research was to achieve a beer understanding of how
quickly aackers ﬁnd assets and use secrets in each scenario. Armed
with this information, security teams can establish the right protections
to keep assets from being exposed, and perform the most eective
remediations when an exposed asset has been found.

In our research we measured the following:

• Probability of asset access: How likely is it that an accidentally exposed asset will be accessed
and how quickly? Does this likelihood dier depending on the resource environment? We tracked
this by monitoring traic to the services using t-pot[^1] or native access logs.

• Tactics applied in asset access: If assets are accessed, what types of commands are used most
often? What does this tell us about aacker tactics? We were also able to track this by monitoring
traic to the services using t-pot[^1] or native access logs.

• Probability of secret usage: How likely is it that an exposed secret in that asset will be used? By
using canary AWS tokens (valid access tokens that act as tripwires), we could see when, where,
and how they were used without providing the aacker access to anything that was actually of
interest.

• Tactics applied in secret usage: If exposed secrets are used, what type of tactics do aackers

use the most? What does this tell us about their strategies?

[^1]: hps://github.com/telekom-security/tpotce

Data collection

Our research was conducted between
January and May 2023. To set up our
‘honeypots’ and simulate misconﬁgured
resources, we basically broke all security
best practices (don’t try this at home!):

We started by creating a number of
resources in dierent environments that
allowed public or easy access. Next, we
placed a secret - in this case AWS keys - in
our honeypots. And then we observed as
aackers took the bait..

10

Copyright Orca Security 2023
Orca Security, Highly
Conﬁdential

<a name="research-findings"></a>
# Research Findings

<a name="github-honeypot"></a>
# 1 GitHub Honeypot - Setup

![50% of organizations store sensitive data in at least one Git repository]

We created a public
repository with two
Python ﬁles.

Why is there signiﬁcant leakage risk
on GitHub?

1

2

3

One of the Python ﬁles contained an AWS access key
(secret and access keys).

The second one contained a bucket (s3://switanok-zustricz)
with an access key in it.

Although GitHub doesn’t provide access logs to public repos, we could tell
repo access by tracking usage of the keys in the repos.

GitHub is a source control system that stores intellectual
property such as software source code, build scripts, and
Infrastructure as Code scripts.

It is not uncommon for organizations to accidentally leak
secrets, database passwords and other sensitive data in
code commits. This is especially problematic as it’s
relatively easy for aackers to discover public GitHub
repositories and commits.

In view of this potential risk, we wanted to ﬁnd out how
quickly aackers would discover and weaponize leaked
secrets in GitHub commits.

12

Copyright Orca Security 2023
Orca Security, Highly
Conﬁdential

# GitHub Honeypot - Key Usage

Usage of the AWS key occurred quickly and from many sources.
It took only 2 minutes for an aacker to use the leaked key.

It only
took:

2 minutes
before keys were exploited

The good news is that the leaked keys were quarantined by AWS as
soon as the git push occurred; The AWS Compromised Key
Quarantine policy for the leaked key was added at the exact same
time as the git push was commied.

However, even with this policy applied, this
does not mean that the key is entirely
blocked. Although the policy denies most
of the EC2, S3 Bucket, Lambda, and IAM
service permissions, aackers can still
access all other permissions a user might
have, such as Amazon Relational Database
Service (RDS), Amazon Elastic Kubernetes
Service (EKS), and Opensearch.

In other words, if
the leaked
credentials have a
lot of permissions,
an aacker can still
do damage.

Beware of the Git History

We decided to see what would happen if we created a new
commit that removed the secret while leaving the original
commit in the Git history. We observed that the keys that were
published in old commits were rescanned after a newer commit,
indicating that aackers are searching the Git History for keys
as well. Even though fewer actors discovered and used the key
from the history than from the original commit, it is important to
make sure that any keys are not only removed from the newest
commit, but also from the commit in the history.

13

Copyright Orca Security 2023
Orca Security, Highly
Conﬁdential

# GitHub Honeypot - Key Tactics

The majority of key usage was around reconnaissance:
aackers were trying to ﬁnd out whether the key provided
access to any resources that could be of interest.

API calls made with the keys
leaked on GitHub:

• “GetCallerIdentity” (25%) was the most used API call, followed

by “GetAccount” (14%), which suggests that actors are trying to
test the validity of the secret and gather more information about
the owner of the exposed key.

• Next “ListUsers” (8%), and “DescribeInstances” (6%) are used
most commonly, which point to reconnaissance commands where
the actor is trying to ﬁnd out what the key provides access to.

• “ListHostedZones” (5%) is of further interest because it can

enable an aacker to further enumerate their target’s footprint
and look for additional access.

```
L
i
s
t
T
o
p
i
c
s         5
%

e
ListId
ListHostedZones     5%
ntities         5
ListClusters       6%

%
List Certiﬁcates     6%

ListBuckets      6%

DescribeInstances    6%

%
s    8

r
e
s
U
t
Lis

GetCallerIdentity  25%

Other    14%

GetAccount   14%
```

14

Copyright Orca Security 2023
Orca Security, Highly
Conﬁdential

# GitHub Honeypot - Aacker Close Up

A closer look at the individual actors shows that most start initial
reconnaissance and then give up, but a small number of actors
are very persistent.

Observations

Testing key validity

Reconnaissance

Aempting to access data

API calls that the top source IPs tried with our keys

Malicious intent

IP addresses 3.109.16.140 and 35.200.187.59 were
behind the most usage aempts and tried to access
data with our key. We suspect they’re the same actor. On
the day of the key publication, they tried the same calls
only milliseconds apart. Both IPs are located in Mumbai,
yet, the aacker tried to use API calls in almost all
regions, and mainly in US-East-1. The ﬁrst scan from this
actor came about 5 minutes after publication.

IP address 88.99.96.208 is a scanner based in
Germany, it initiated one GetAccount call for each AWS
region, but then gave up.

IP address 54.39.190.134 is a GitGuardian scanner
(a code security platform) scanning periodically up
to 7 days after publication.

15

Copyright Orca Security 2023
Orca Security, Highly
Conﬁdential

# GitHub Honeypot - Regions

Although we saw half of the AWS key exploitation in the US,
usage also occurred in almost every other region.

AWS regions where API calls were made
with leaked keys on GitHub:

From the chart on the right we can see that, as can be
expected, most of the aackers tried to use the key in
us-east-1, which is the most used AWS region. However, we did
not expect to see key usage in almost every other region as
well, including Asia Paciﬁc (23%), Europe (20%), South
America (4%), and Canada (3%).

So, as we can see, no region
is out of target for aackers.

```
C
a
C
-
c
a
e
-
c
n
e
t
n
r
al-
t
r
al-
1  3
1  3
%
%

E
u
-
n
o
r
t
h
-
1
 3
%

Sa-east-1  4%
Sa-east-1  4%
Eu-west-3  4%
Eu-west-3  4%
Eu-west-2  4%
Eu-west-2  4%
Eu-west-1  4%
Eu-west-1  4%
Ap-southeast-2  4%
Ap-southeast-2  4%
Ap-southeast-1  4%
Ap-southeast-1  4%
Ap-northeast-2  4%
Ap-northeast-2  4%
Ap-northeast-1  5%
Ap-northeast-1  5%
ntral-1  5
ntral-1  5

%
%

e
u-c
e
u-c
E
E

Us-east-1  34%
Us-east-1  34%

Us-west-2  6%
Us-west-2  6%
Us-west-1  5%
Us-west-1  5%

U
s
U
-
e
s
a
-
e
s
a
t
-
s
2
t
-
 5
2
 5
%
%

%
5
%
1
5
-
h
1
t
-
u
h
o
t
u
s
-
o
p
s
A
-
p
A
```

16

Copyright Orca Security 2023
Orca Security, Highly
Conﬁdential

<a name="aws-s3-bucket-honeypot"></a>
# 2 AWS S3 Bucket Honeypot - Setup

Bucket naming

1

2

3

We created 13
public buckets
using commonly
used names.

Then we granted them full List and Get permissions.

Next, we put AWS access keys as a canary token in each bucket, so we
would get a notiﬁcation when the token was used as well as metrics on how
it was used.

Our S3 Bucket Honeypot Names

● ben-application-mirroring
● org.com
● static-assets-com
● prod-sandra-sadeh-simon
● san-gui-images
● sergei-bucket
● shen-test

● slava-images
● sophie-tests
● roy-prod-duplication
● staging-production-assets
● static-prod-bucket
● switanok-zustricz

• Because there is no easy way to ﬁnd names of new or existing

S3 buckets without having the appropriate permissions to begin
with, aackers have to ﬁnd accessible buckets by cycling through
possible names until they discover accessible ones (known as
brute-forcing).

• To aract our aackers, we used bucket names that included
variations of names that we know public bucket scanners are
already actively searching for, and are included on common bucket
names lists used by aackers.

Public access

• Our public S3 Buckets allowed anybody to list the objects

stored in the bucket and read the contents of those objects.

• This is what we wanted in our honeypot, but precisely what we
wouldn’t want on a storage bucket that contains sensitive
information.

17

Copyright Orca Security 2023

# AWS S3 Bucket Honeypot - Access

While there are actors who actively scan for public buckets with
easily guessable names, only one of our buckets was actually
discovered this way.

It took aackers..

The bucket org.com was the ﬁrst to be accessed - within two
days. We suspect this is because it had a website structure
and it may have aracted possible non-malicious access.

However, when none of the other buckets were accessed, we
concluded that this was probably due to the lack of digital
‘breadcrumbs’ to our buckets, and decided to publish 9 of the
13 bucket names on forums and sites to try to aract more
potential aackers.

And voilà! After we published the names, we saw the ﬁrst
access within one hour. Within three hours, six of the buckets
were accessed.

1 hour
to access S3 Buckets

Count on even faster access for legitimate buckets:

While we had to leave breadcrumbs to our (fake) buckets before we
saw access, we would expect there to be many more digital
breadcrumbs to legitimate buckets (such as references to bucket
names, IDs, and links) and therefore also expect them to be accessed
even faster than in our tests.

18

Copyright Orca Security 2023
Orca Security, Highly
Conﬁdential

# AWS S3 Bucket Honeypot - Publication

We ﬁrst posted to Pastebin in dierent geographies and languages,
which led to some access. Initially, we saw the most access from
the Chinese and Ukrainian postings, but no access from our
Russian postings.

Next, we used Twier (posted with appropriate hashtags), GitHub
(public repository with script that included the S3 bucket name), and
Reddit (posted to r/Hacking_Tutorials). This led to a large number of
logins on the shen-test bucket.

| Bucket Name          | # of Initial Logins | First Publication | Post Views | # of Additional Logins | Second Publication | Post Views | # of Additional Logins | # of Total Logins |
| -------------------- | ------------------- | ----------------- | ---------- | ---------------------- | ------------------ | ---------- | ---------------------- | ----------------- |
| shen-test            | 0                   | Pastebin (CN)     |            | 126                    | Twitter            |            | 126                    |
| org.com              | 23                  | Not published     |            | N/A                    |                    |            |                        | 23                |
| roy-prod-duplications | 0                   | Pastebin (EN)     |            | N/A                    |                    |            |                        | 0                 |
| sergei-bucket        | 0                   | Pastebin (UA)     |            | 0                      | Reddit             |            | 0                      | 0                 |
| switanok-zustricz    | 0                   | Pastebin (UA)     |            | 6                      | GitHub             |            | 6                      | 6                 |
| sophie-tests         | 0                   | Pastebin (RU)     |            | 3                      | Twitter            |            | 3                      | 3                 |
| slava-imeges         | 0                   | Pastebin (RU)     |            | 3                      | Twitter            |            | 3                      | 3                 |

The most accessed bucket was shen-test. Shen-test was
ﬁrst published on the Chinese Pastebin, but got far more
access aempts after a post on Twier (in English).

The S3 buckets, for which we published breadcrumbs on the
Russian Pastebin weren’t accessed until we also posted
them on Twier (in English).

19

Copyright Orca Security 2023
Orca Security, Highly
Conﬁdential

# AWS S3 Bucket Honeypot - Tactics

What actions did aackers take once they discovered the buckets?

Scoping out the target

By far the most used action was HEAD-BUCKET. This action is used
to determine if a bucket exists and whether you have permission to
access it. Other often used commands were GET_ACL (to read the
access control list of the resource), GET_Policy_Status (to ﬁnd out
whether the bucket is public), and GET_Public_Access_Block (to
retrieve the PublicAccessBlock conﬁguration of the bucket).

Commands used to access the S3 buckets

We can tell from the actions aackers took that they
were trying to ﬁnd out whether they could access
the bucket and if it contained anything interesting:

• Is this bucket public?
• What permissions do I have?
• Which users can access the bucket?
• Is there a public access block on the bucket?
• Which instances are running in this bucket?

20

Copyright Orca Security 2023
Orca Security, Highly
Conﬁdential

# AWS S3 Bucket Honeypot - Key Usage

After the buckets were accessed, it took 8 hours for aackers to
start using the key. The diagram on the right shows the actions the
aackers tried to take with the leaked keys.

It took aackers:

Commands used with the keys exposed on S3 buckets

8 hours  to exploit keys in S3 Buckets

How did  aackers try to use the keys they found?

We can see that more than half used ‘GetCallerIdentity’ (64%),
followed by ‘GetBucketLocation’ (9%), ‘Describe Instances’ (9%),
and ListBuckets (9%). As can be expected, the majority are
reconnaissance type actions.

We also saw more malicious aempts, such as ‘CreateUser’ (9%),
where an actor is trying to gain persistency in the account.

If these keys had been ‘real’ keys, no doubt the aackers could
have leveraged any information found in the buckets and caused
some real damage.

```
9%
GetBucketLocation
9%
Describe Instances

9%
List Buckets

9%
Create User

64%
GetCallerIdentity
```

21

Copyright Orca Security 2023
Orca Security, Highly
Conﬁdential

<a name="ssh-honeypot"></a>
# 3 SSH Honeypot

For our SSH honeypot, we opened port 22 and allowed any
user/password combination. We did not need to wait long: we saw
access to our SSH honeypot within 4 minutes.

SSH allows for easy discovery because tools like Shodan help
perform automated scanning, similar to any other open TCP port.
The key location was /home/<user>/.aws/credentials.

Aackers were using automated logins with common usernames
like, root, admin, Admin, Administrator, and default, and obvious
passwords such as admin, 123456, root, (empty), and password.

It took aackers..
4mins to access our SSH honeypot

![Top usernames detected on aempted logins through SSH]

![Top passwords detected on aempted logins through SSH]

22

Copyright Orca Security 2023
Orca Security, Highly
Conﬁdential

# SSH Honeypot - Tactics

The exposed key was located in /home/<user>/.aws/credentials.
However, we did not detect any usage of the key.

From the CLI commands that were used, it seems like aackers
were more interested in the SSH compute resources to for
instance deploy cryptominers, rather than exploiting the key.

![Top CLI Commands]

Aempts to run Malware

We saw hundreds of aempts by aackers to install malware on our
SSH honeypot - mainly Mirai variants. Mirai is a notorious botnet, for
which the source code was published in 2016. It frequently appears
with new variants. If this malware is installed successfully, the
machine becomes a bot that could be controlled remotely and used
for many purposes, for example as a bot in a DDoS aack.

Mirai variants detected:
771229b5b05e22d4f43e728b38c1e6f08fe7157e3c6dcade0e9af065f710f22d
77a2c317ca9d43acc056cf8217a8c838d23af63965b33dc931877360d5919b8d
C5bd2146ebbe575a47a666e07b99eb526d46d74e0d7758bf0bf5cb5b3adaa55a
36bc49ede8e0f4a54449602ca2bc681f96b14869841a243ddfb7d94fb6f28749
A04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3

Aempts to run Cryptominers

Another very known malware threat of recent years are cryptominers.
Many opportunistic aackers are using the compute resource of the
machine they exploited to mine cryptocurrency. We also saw hundreds
of aempts to install cryptominers on our machine.

Miners detected:
B9e643a8e78d2ce745fbe73eb505c8a0cc49842803077809b2267817979d10b0
28516b0407f1bef5de782d7bf916a9a7cf692ef66261768efae4423e93efe280
3a43e9ceededc2d3b8bae8f8fc8c539047cdacdd315ebef3adc6651117325e
94f2e4d8d4436874785cd14e6e6d403507b8750852f7f2040352069a75da4c00

23

Copyright Orca Security 2023
Orca Security, Highly
Conﬁdential

<a name="http-honeypot"></a>
# 4 HTTP Honeypot

![Top URIs accessed]

For our HTTP honeypot, we
created a machine with an open
port of 80 and a simple
webpage. The secret key was
under the following path:
“hp://<IP>/credentials.html”.
We created a web server that
returned an AWS key in a
webpage when accessing it via
tcp/80 or tcp/8080.

The ﬁrst access to the machine
was within 3 minutes. Most of
the access we saw was
reconnaissance on the website
and some were aempts to ﬁnd
potentially vulnerable web
pages. We never saw usage of
the key that we exposed.

It took aackers..

3 mins

to access our
HTTP honeypot

From the URIs we can see that aackers
were searching for standard HTTP paths
that could help with typical HTTP
exploitation aacks and for credentials
that could be relevant. However they were
not searching for an exposed secret, which
is why they did not discover or use the key.

24

Copyright Orca Security 2023
Orca Security, Highly
Conﬁdential

<a name="dockerhub-honeypot"></a>
# 5 DockerHub

For our Docker honeypot, we created a Docker image that builds
a container with an AWS conﬁg ﬁle that contains keys, then
published it in a public Docker repository and waited..

However, the Docker image was never downloaded.

We think the reason for this is that scanning Docker is a far
harder task than for instance scanning GitHub. In GitHub, all an
aacker needs to do is scan the content that is visible on the
website. However on DockerHub, an aacker would need to
actually download the Docker image before they are able to
access any information.

This is probably why there does not seem to be automated
reconnaissance on DockerHub.

No aackers
accessed our
Docker image

The cost/beneﬁt ratio is far less
aractive on DockerHub and this is why
aackers are less likely to target it.

25

Copyright Orca Security 2023
Orca Security, Highly
Conﬁdential

<a name="ecr-honeypot"></a>
# 6 ECR Honeypot

We created a public registry in Amazon’s Elastic Container Registry
(ECR) with names we believed would aract the interest of aackers:

1

2

3

Production-app-new

Evelyn-image

images-uploads

The images contained an embedded AWS key. For two months, we
waited for someone to download the image and use the keys. After no
actors took the bait, we decided to post a question in Stack Overﬂow
about the image stored in ECR with the details and authentication of
the image.

The question was immediately reviewed 20-30 times, then received
more views over time. After 4 months, we observed two actors
downloading the images and initiating calls with our keys. One of the
keys was used by an IP registered in the Asia Paciﬁc region, another
one by an IP registered to Microsoft.

It took..

4 months

before keys were