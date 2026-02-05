# The Secure Sign-in Trends Report 2024

## Table of Contents
- [First, a word on measuring MFA adoption](#first-a-word-on-measuring-mfa-adoption)
- [Summary of key findings](#summary-of-key-findings)
- [Introduction](#introduction)
- [How to use the data](#how-to-use-the-data)
- [Current state of MFA adoption](#current-state-of-mfa-adoption)
- [MFA adoption over time](#mfa-adoption-over-time)
- [MFA adoption by region](#mfa-adoption-by-region)
- [MFA adoption by industry](#mfa-adoption-by-industry)
- [MFA adoption by organization size](#mfa-adoption-by-organization-size)
- [MFA adoption by user type](#mfa-adoption-by-user-type)
- [MFA adoption by authenticator type](#mfa-adoption-by-authenticator-type)
- [A data-driven assessment of authenticator usability and security](#a-data-driven-assessment-of-authenticator-usability-and-security)
- [Authenticator challenge time](#authenticator-challenge-time)
- [Authenticator enrollment time](#authenticator-enrollment-time)
- [Authenticator challenge failure rate](#authenticator-challenge-failure-rate)
- [Phishing-resistant coverage](#phishing-resistant-coverage)
- [Phishing-resistant alert coverage](#phishing-resistant-alert-coverage)
- [Authenticator challenge brute-force failure rate](#authenticator-challenge-brute-force-failure-rate)
- [Authenticator Metric Survey](#authenticator-metric-survey)
- [Assessing authenticator performance and adoption](#assessing-authenticator-performance-and-adoption)
- [The way forward](#the-way-forward)
- [Methodology](#methodology)
- [About Okta](#about-okta)
- [Disclaimer](#disclaimer)

---

2024

An inside look at
MFA adoption and
the authenticators
that influence it

The Secure Sign-in
Trends Report

It took a little time to convince the world of the virtues of multi-factor authentication (MFA).

From the outset, the consensus in the security community was that MFA was essential to protecting against wave after wave of password-based attacks, but many organizations would only require an MFA challenge for access to their most treasured systems.

During the pandemic, MFA adoption went mainstream. Okta observed a 15% rise in the use of MFA within a few short months, as the world rushed to support remote work. We’re now at the point where most Okta admins, and the majority of users, access workplace applications after MFA challenges. And we’re seeing regulators and standards bodies across the world demanding that organizations secure access with these stronger sign-in methods.

In this year’s Secure Sign-in Trends Report, we find strong growth in the adoption of passwordless, phishing-resistant sign-in methods. In January of this year, 5% of users on our workforce platform didn’t sign in once using a password. That small number belies a huge, latent, exciting potential. It’s a small number that says that passwordless is here and now. It’s possible. If these Okta customers did it, so can you.

So we expect the next wave of MFA adoption won’t be driven by security purists, or even by those very sensible policy makers demanding that regulated entities enroll users in MFA. It’s going to be driven by a demand for a better user experience and higher security assurance. Once you’ve experienced passwordless, whether as an employee or a customer, you will never want to go back.

I hope you enjoy geeking out on these numbers. Thanks for reading.

Todd McKinnon
CEO, Okta

01

## Table of
contents

  03

  06

  07

  09

   11

  13

  15

  17

  19

21

23

  27

  29

33

35

37

39

41

43

  47

  49

51

First, a word on measuring MFA adoption

Summary of key findings

Introduction

How to use the data

Current state of MFA adoption

MFA adoption over time

MFA adoption by region

MFA adoption by industry

MFA adoption by organization size

MFA adoption by user type

MFA adoption by authenticator type

A data-driven assessment of authenticator usability and security

Authenticator challenge time

Authenticator enrollment time

Authenticator challenge failure rate

Phishing-resistant coverage

Phishing-resistant alert coverage

Authenticator challenge brute-force failure rate

Authenticator Metric Survey

Assessing authenticator performance and adoption

The way forward

Methodology

The Secure Sign-in Trends Report 2024

## First, a word
on measuring
MFA adoption

Before you dive in, it’s important to understand that the data and conclusions in this report reflect the authentication choices made by organizations, their administrators, and employees. While we frequently refer to users, these users are typically employees in a workplace setting and their authentication options are often limited by organizational policies.

There are multiple ways to measure multi-factor authentication (MFA) adoption, as outlined in the table below. For this study, we measured adoption for actual MFA usage: the percentage of users who signed in using MFA over a given period.

| Measurement option             | Definition                                                               |
| :----------------------------- | :----------------------------------------------------------------------- |
| Tenants-Level MFA Adoption Rate | % of Okta customer tenants, with users who signed in using MFA at least once during a month |
| User-Level MFA Adoption Rate   | % of users who signed in using MFA during a month                        |
| Event-Level MFA Adoption Rate  | % of successful sign-in events that involved an MFA challenge during a month |
| MFA Attach Rate                | % of customers that have purchased an SKU that includes MFA              |
| Tenants-Level Enrollment Rate  | % of tenants, Okta organizations, that have configured MFA for use       |
| User-Level Enrollment Rate     | % of users who have enrolled in MFA authenticators                       |
| User-Level MFA Use             | % of users signed in using MFA over a given period                       |

We also chose to aggregate MFA usage data at the user level, given that we are attempting to measure user adoption:

| Aggregation option             | Definition                                                               |
| :----------------------------- | :----------------------------------------------------------------------- |
| MFA Attach Rate                | % of customers that have purchased an SKU that includes MFA              |
| Tenants-Level Enrollment Rate  | % of tenants, Okta organizations, that have configured MFA for use       |
| User-Level Enrollment Rate     | % of users who have enrolled in MFA authenticators                       |
| User-Level MFA Use             | % of users signed in using MFA over a given period                       |

It’s also important to keep in mind that this study only counted direct MFA authentication events in the Okta Workforce Identity Cloud (WIC). If users authenticate exclusively using MFA provided by other Identity providers and make use of enterprise federation or social login to connect to Okta, they are not captured by our MFA adoption data. Therefore, it’s likely that the reported MFA adoption rate will slightly underestimate the overall rate of MFA use among our customers. We have also excluded test accounts. All adoption and metric data is derived from revenue-linked production orgs/tenants.

03

04

Authenticator usability and security properties

To best understand the hurdles to MFA adoption, we first must answer some foundational questions: Can we develop a framework and provide a systematic, quantitative view of authenticator properties? Can we use data-driven insights to educate our customers on better protecting their organizations and guiding product development?

For this task, we evaluated authenticators from both usability and security perspectives, as shown in Table 2. Measuring these criteria is a challenging task, given that the logic and user interface (UI) flows of each authenticator vary and can be highly customized. To achieve consistency, we leveraged Okta Identity Engine (OIE), which provides better-designed and more flexible Identity experiences and flows.

We measured the properties of the following authentication methods: password, email, hardware one-time password (OTP), push, software OTP, security question, SMS, voice OTP, Okta FastPass, FIDO2 WebAuthn, and smart card. Unless otherwise specified, we collected the data during January 2024 from revenue-linked production organizations of workforce customers using the Okta Identity Engine.

We took considerable care to develop data collection methods that allow for apples-to-apples comparisons between authenticators. This report highlights conditions that complicate these comparisons and explains the implications for our results. We also checked for month-to-month variations in the data to ensure the general trends were consistent over time.

The Secure Sign-in Trends Report 2024

## Summary of
key findings

MFA adoption continues
its upward trajectory

Adoption rates vary widely
by industry and company size

As of January 2024, MFA adoption climbed to
66% among Okta workforce users, and 91% of
administrators use MFA.

Government and Education, saw above 5% year-
over-year growth in adoption, and this may further
increase with recent U.S. executive orders (EOs)
and regulatory changes.

Phishing-resistant authenticators
show great momentum

Passwordless
has arrived

The adoption of phishing-resistant authenticators
increased substantially. The adoption rate for FIDO2
WebAuthn increased from 2% in 2023 to 3% in 2024,
while the adoption rate for Okta FastPass leaped from
2% to 6% in the same time period.

The number of Okta customers who are using
passwords is finally starting to decline as
organizations adopt modern authentication
methods. Just under 5% of users did not use a
password during any sign-ins during January 2024.

Security vs. user
experience is a false choice

Phishing-resistant authenticators offer a superior
user experience. In our authenticator performance
and usability assessment, FastPass and FIDO2
WebAuthn came out on top as more secure
and user friendly than other options, even under
revised, more practical criteria.

05

The Secure Sign-in Trends Report 2024

## Introduction

Introduction

“[Multi-Factor Authentication] MFA is widely recognized as one,
if not the most, important preventative security controls available today.
It provides a strong defense against various adversarial attack
techniques such as password spraying, compromised password
reuse, and—in some instances— phishing. However, a key challenge
is that it is notoriously difficult to deploy and many organizations, small
and large, still have not done so even if they recognize the value.” [1]

We all understand the assurance Multi-Factor
Authentication (MFA) adds to user sign-in events.

One of the most difficult trade-offs in identity and
access management is determining what level of
friction you're willing to impose on end users in order
to secure access to the organization's applications
and data. Too little friction creates opportunities for
attackers, and too much friction drives employees to
use unsanctioned applications, which also creates risk.

As the number of serious security incidents and the
costs of these incidents climb, most organizations
and employees are coming to accept that strong
authentication is a non-negotiable requirement,
especially when securing remote access to resources.
The challenge now is how to enforce high assurance
authentication while minimizing the friction applied to
end users.

In this report, we explore the wide variety of
approaches companies today are taking to verify their
users' identities and prevent unauthorized access.
Based on anonymized data from Okta customers’
billions of monthly authentications, we've updated
our assessment of the state of authentication,
identifying trends and analyzing approaches based on
considerations such as industry, region, and company
size.

Ultimately, this year’s report shows that while we are
moving in the right direction, we’re not moving fast
enough. During the COVID pandemic, we saw a 15%
spike in MFA adoption as organizations rushed to
secure remote working, so it’s a little disheartening to
see the pace slow: MFA adoption only improved two
percentage points year-over-year since 2023, albeit
from an already high baseline. As of January 2024, 66%
of users authenticated with MFA.

It appears that we are at a turning point. The US Executive
Order on Improving the Nation’s Cybersecurity is
coming into force, and Organizations and Cloud
Providers alike are stepping up to drive users toward
more secure authentication. Concurrently, technology
leaders like Salesforce, GitHub, Okta and Microsoft are
all embarking on projects to enforce MFA for privileged
users, which will drive interest in the development and
adoption of authentication methods that provide high
assurance without imposing user friction.

With this report, we aim to provide IT and security
professionals with a data-driven perspective on the
solutions available today and to dispel the myth that
strong authentication must translate to extra friction
for users. In fact, the opposite is true: passwordless,
phishing-resistant authentication is both more secure
and easier to use.

All data and conclusions in this report are based on our analysis of anonymized
Okta data unless otherwise noted.

07

[1] https://media.defense.gov/2023/Oct/04/2003313510/-1/-1/0/ESF%20
CTR%20IAM%20MFA%20SSO%20CHALLENGES.PDF

The Secure Sign-in Trends Report 2024

## How to
use the data

The answers to these questions can help IT and security
leaders weigh the costs and benefits of different
authenticators to determine the best solution for their
organization and users.

This report provides a framework for measuring the
usability and security properties of a comprehensive
list of authenticators. We asked critical questions to
help CIOs, CSOs, and policymakers understand the
why behind the varying rates of MFA adoption. These
questions included:

 • What observable security features are relevant to
MFA adoption?
    ⚪ How much coverage does any given
    authenticator provide for phishing-resistant
    authentication flows?
    ⚪ How often do adversaries target accounts
    using any given authenticator in brute-force
    attacks?

 • How has MFA adoption changed over time?

 • Does an organization's industry group, location, or
size affect MFA adoption rates?

 • What observable usability features are relevant to
MFA adoption?
    ⚪ How long does it usually take for a user to
    authenticate with any given authenticator?
    ⚪ How long does it usually take for a user to set
    up/enroll in any given authenticator?
    ⚪ How often do authentication events fail using
    any given authenticator?

Okta has enjoyed the benefits of
passwordless, phishing-resistant
authentication for several years.
Over the 12 months since the last
Secure Sign-in Trends report, we’ve
invested in enforcing phishing
resistance throughout the entire
user lifecycle: from user enrollment,
through to access, and into account
recovery. The great news is: it’s
possible.”

David Bradbury
Chief Security Officer

09

The Secure Sign-in Trends Report 2024

## Current state:
MFA adoption

MFA is an essential part of any high-assurance
security posture. When signing in using MFA, a user
must provide two or more distinct factors to verify their
Identity. Those factors include something you know (a
“knowledge factor” such as a password), something
you have (a “possession factor” such as a registered
device), or something you are (an “inherence factor”
such as a biometric).

While MFA is generally regarded as table stakes for
secure sign-in, multiple internal and external factors
influence its adoption. In this section, we examine
adoption rates over time as well as by region, industry,
organization size, authenticator type, and user type
(whether the user has administrative permissions).
The results serve as both a benchmark to gauge
organizational and industry progress and to identify
areas for improvement.

“Factor” vs. “authenticator”

This report uses the terms “authenticator” and
“factor” in accordance with the National Institute of
Standards and Technology (NIST) definitions:

Authenticator: Something a claimant owns or
controls and uses to authenticate their Identity.

Factor: An authentication property, e.g., a knowledge
factor (something you know, like a password or
security question), a possession factor (something
you have, like an enrolled device), or an inherence
factor (something you are, like your fingerprint).

Note: Every authenticator has one or more
authentication factors. Often the terms are confused
when “factor” is used instead of “authenticator,” or
when an authenticator can satisfy multiple factors.
For example, Okta FastPass can provide both a
possession factor (a registered device) and an
inherence factor (using biometric verification).

11

The Secure Sign-in Trends Report 2024

## Current state: MFA adoption

MFA adoption
over time

Figure 1 shows MFA user adoption rates for Okta
Workforce Identity Cloud customers — those who
use Okta to provide employees, contractors, and
partners with secure access to corporate resources
— from October 2019 to January 2024. Each data point
represents the MFA adoption during that month.

As we discussed in our 2023 report, from February
through March 2020, the MFA adoption rate soared
from 35% to 50% as organizations quickly pivoted to
remote work and sought to secure a perimeter that
now extended well beyond the corporate network.
Since then, year-over-year growth in MFA adoption
was at 6% per year from 2020 to 2023, and slowed
down to 2% in 2024. As of January 2024, 66% of users
sign in using MFA.

This growth rate is not keeping up with the increase in
identity-based attacks. In 2024, we saw multiple events
where threat actors targeted human and machine
accounts that did not have multi-factor authentication
enabled. In response, many cloud vendors are now
mandating MFA adoption for privileged user accounts,
if not all accounts.

Key insight

As enforcement of MFA for privileged accounts
becomes a baseline control organizations
expect, we expect more service providers
to join the list of those already mandating
MFA for privileged accounts. IT and Security
professionals should leverage this as a driver to
accelerate MFA adoption more broadly across
their organizations.

13

The Secure Sign-in Trends Report 2024

## Current state: MFA adoption

MFA adoption
by region

In the 2023 report, we noted that MFA adoption was
relatively consistent across geographic regions, and
we expected that to hold true in 2024. Okta customers
are more likely to apply MFA to users than any other
competing service, irrespective of location.

Our data validated this position: showing MFA
adoption rates of between 61 and 68% for the
Americas (AMER), Asia Pacific (APAC) and EMEA
(Europe, Middle East and Africa). We observed a 3%
improvement in adoption rates in AMER and EMEA
compared to 2023, and a decrease of 1% in APAC.

Key insight

We can subsequently conclude that — within
the regions we serve — the location of an
organization and its users isn’t a determining
factor in MFA adoption, at least at the
aggregated regional level.

15

The Secure Sign-in Trends Report 2024

## Current state: MFA adoption

MFA adoption
by industry

In 2024, we continue to observe a wide variation in
MFA adoption by industry - increasing to a difference
of 50 percentage points between the industry with
the highest adoption (technology) from that with the
lowest adoption (transportation and warehousing). As
is often the case, the technology sector plays the role
of early adopter and continues to record the highest
MFA adoption rate (88%) among Okta Workforce
customers.

There was higher MFA adoption across almost all
industries during the past year. The Government (up
to 55% from 48%) [2] and Education sectors (up to
69% from 64%) saw an increase of above 5% year-
over-year in MFA adoption. Both sectors are highly
regulated industries that started out with relatively low
rates of MFA adoption and are now catching up, and
we expect recent U.S. executive orders and regulatory
changes to further accelerate the trend. On the flip
side, we observed decreases in MFA adoption in the
Arts, Entertainment & Recreation sector (down to 53%
from 57%) and the Insurance sector (down to 71%
from 77%). These industries are among several that
compete on user experience when authenticating
large networks of business partners (consider
insurance brokers, for example). Given the data these
small businesses access, however, we find it unlikely
that a password alone or a password with SMS MFA
will be deemed sufficient by regulators in the longer
term. This report outlines several ways to deliver a
great user experience without sacrificing security.

Key insight

We wanted to make a special call-out to the
progress made in the Government sector.
Organizations that provide services to the
Government sector, or any other federally
regulated sector, should be implementing
MFA for privileged accounts, at minimum.
In the 2023 report, the MFA adoption rate
for government organizations lagged the
private sector by more than 16 percentage
points. This year, MFA adoption in government
organizations increased by 7 points to 55%,
one of the largest jumps in our data. With
U.S. executive orders coming into force [3] and
with the US Cybersecurity and Infrastructure
Security Agency (CISA) repeatedly endorsing
MFA and phishing-resistant authentication,
we are seeing real progress by public service
organizations in the United States.

[2] Some government employees may use Personal Identity Verification (PIV) or
Smart Card as third-party authentication methods and connect to Okta through
enterprise federation. The government MFA adoption rate of 55% doesn’t include
that use case, and may underrepresent the real government MFA adoption rate.
Okta introduced smart card as a native authenticator type in 2023. We recommend
federal customers migrate from X.509 federation to smart card authenticators so
as to take advantage of advanced features such as App-Level Authentication
Policies and Okta Device Access.

[3] https://www.gsa.gov/technology/it-contract-vehicles-and-purchasing-
programs/information-technology-category/it-security/executive-order-14028

17

The Secure Sign-in Trends Report 2024

## Current state: MFA adoption

MFA adoption by
organization size

When we view MFA adoption by organization size,
we see a rough inverse correlation between the
number of employees and the rate of MFA adoption:
The larger the organization, the lower the adoption
rate. Organizations with fewer than 300 employees
tend to have the highest MFA adoption (≥82%), while
those with more than 20,000 employees have the
lowest adoption rate (59%). Despite being the lowest
adoption group, the latter organizations have made
larger than average improvement (5%) on a year-to-
year basis.

Several factors may contribute to this adoption
delta between large and small organizations: Similar
to government and financial institutions, large
enterprises may be slow to adopt modern Identity
frameworks due to the complexity of replacing legacy
infrastructure. Large enterprises are also more likely
to use multiple Identity providers and may use MFA
solutions other than Okta (our report focuses only on
MFA usage using the Okta platform).

Key insight

The lack of a centralized view of Identity and
Access Management (IAM) is problematic,
whether you’re a large or a small company.
Large enterprises tend to be more sensitive to
trust-eroding security events and should be
motivated to pursue broad MFA coverage.

19

The Secure Sign-in Trends Report 2024

## Current state: MFA adoption

MFA adoption
by user type

When we assess MFA adoption by Okta administrators,
we define an Okta administrator as someone who has at
least one administrator role at Okta. This would include
everyone from the IT help desk through to IAM and
security teams. These MFA adoption numbers are very
healthy at 91%, up 1% from last year. Admins also tend to
serve as role models for using phishing-resistant MFA.
FIDO2 WebAuthn adoption among users with admin
permissions grew from 8% to 9% over the past year,
while the use of Okta FastPass among administrative
users grew from 5% to 13%.

In August 2024, as part of the Okta Secure Identity
Commitment, Okta began requiring customers
to configure MFA to access administrative and
management consoles. [4] Before the MFA enforcement
for the WIC Admin Console began we saw high, but
not total adoption. [5] Our goal is to achieve full adoption
by addressing the remaining long-tail of users with
administrative permissions.

To minimize the impact on our customers, this
enforcement action is sequenced according to the
complexity of existing sign-in flows. Some admins log
in directly within Okta WIC, while others use Identity
Provider federation or integrations with privileged access
management software. Okta now prevents the creation
of single factor policies for direct access to the Okta
Admin Console and has enforced MFA for access to the
Console for 62% of Okta’s existing workforce tenants.

We hope that once privileged users experience how
easy it is to sign in with passwordless, phishing-resistant
authenticators, we will see a broader acceleration in MFA
adoption for all users.

Key insight

Okta’s enforcement of MFA for access to
administrative apps provides IT and security
professionals a trigger event to review their
organization’s broader authentication strategy.
We encourage our customers to take this
opportunity to thoroughly review sign-in policies
for all management consoles and other high-risk
or business-critical applications.

Using application-specific authentication policies
can help smooth this rollout by requiring strong
authentication for high-risk or business critical
applications, while allowing employees to use
weaker forms of authentication for less risky
applications. This strategy allows administrators
to improve the security of an organization without
impacting business speed.

21

[4] https://support.okta.com/help/s/blog/a674z000000147HAAQ/mfa-
enforcement-for-the-admin-console?language=en_US

[5] Please note that the percentage of admins using MFA to access the Okta
Admin Console metric is different from the MFA adoption rate for admins metric.
The former metric looks at the access to the Okta Admin Console only, while the
latter looks at the access to any applications. Also, the former metric requires
admins to use MFA every time they access the Admin Console, while the latter
requires at least one MFA authentication in a month.

The Secure Sign-in Trends Report 2024

## Current state: MFA adoption

MFA adoption rate
by authenticator type

Table 1: Authenticator types and properties

The table lists the authenticator types used to study MFA adoption,
usability and security properties, and key authenticator characteristics.

The Okta Identity Cloud is built on the idea of being
platform-agnostic, and allowing customers to use
the technologies that work best for them. Okta
offers a wide selection of first-party and third-party
MFA authenticators for all use cases. Based on their
underlying authentication mechanisms, authenticators
can be categorized into three groups: password
authenticators, traditional MFA authenticators, and
phishing-resistant MFA authenticators.

Traditional MFA authenticators include Email, Hardware
Token, Push, Security Question, Short Message
Service (SMS) and Soft Token. Phishing-resistant
MFA authenticators include Okta FastPass, FIDO2
WebAuthn, and Smart Card. As shown in Table 1, we
include as many vendor offerings as possible for each
authenticator type. However, if the authentication
data couldn't be separated by authenticator types or
involved custom options, we placed it in the "other"
category and excluded it from further study.

| Authenticator type              | Supported authenticators at Okta, used for Authenticator adoption property study | Authenticator names: types, used for usability and security property study | Factor type              | Assurance level |
| :------------------------------ | :------------------------------------------------------------------------------- | :------------------------------------------------------------------------- | :----------------------- | :-------------- |
| Password authenticator          | Password                                                                         | Password                                                                   | Password                 | Medium          |
| Traditional MFA authenticator   | Email                                                                            | A combination of Email code and link (aka magic link)                      | Possession               | Weak            |
|                                 | Hardware Token                                                                   | YubiKey OTP, RSA SecurId, Custom TOTP                                      | Possession               | Weak            |
|                                 | Push                                                                             | Okta Verify Authenticator, Push method, Duo Authenticator                  | Possession               | Weak            |
|                                 | Security Question                                                                | Security questions                                                         | Knowledge                | Weak            |
|                                 | SMS                                                                              | SMS, Duo Authenticator                                                     | Possession               | Weak            |
|                                 | Soft Token                                                                       | Okta Verify OTP, Google Authenticator, RSA SecurId, Custom TOTP, Duo authenticator | Possession               | Weak            |
|                                 | Voice                                                                            | Phone authenticator Voice method, Duo authenticator                        | Possession               | Weak            |
|                                 | Other                                                                            |                                                                            |                          |                 |
| Phishing-resistant MFA authenticator | FastPass                                                                         | Okta Verify authenticator, FastPass method                                 | Possession + Biometric | High            |
|                                 | WebAuthn                                                                         | WebAuthn authenticators (a combination of Mac Touch ID, Android fingerprint, Windows Hello, YubiKey, Google Titan, PassKey), Duo Authenticator | Possession + Biometric | High            |
|                                 | Smart Card                                                                       | Smart Card                                                                 | Possession + Knowledge   | High            |

23

It is no surprise that passwords persist in the
workforce environment. But we also see an increase
in passwordless experience, growing from less than
2% in January 2023 to almost 5% in January 2024.
Push (29%) is the most popular MFA authenticator,
followed by SMS (17%) and Soft token (14%).

Thirdly, we should also expect regulatory compliance
to play a role in further driving the adoption of
phishing-resistant factors. Government agencies
in Australia, for example, must employ phishing-
resistant authentication methods to satisfy Maturity
Levels 2 and 3 of the Essential Eight controls.

Key insight

OIE offers more flexibility in managing login
flows, such as application sign-on policies that
allow administrators to configure individual rules
for accessing applications, and to offer users a
passwordless, phishing-resistant authenticator
in Okta FastPass. We advise Okta customers to
evaluate and implement stronger authenticators
to maximize the benefits to users, not just for
the convenience of administrators. For example,
SMS authenticator is known to have a low
assurance level, is subject to SIM swapping
attacks, and has a higher cost to operate. For
best results, both IT and Security teams should
be involved in the upgrade to rapidly get the
most value and evaluate the best authentication
strategy for the organization.

The adoption rates of traditional MFA authenticators
increased compared to last year, but the changes
are small (1.3% in total). We saw a very small SMS
MFA adoption rate growth of 1.2% over the last three
years, despite the overall MFA adoption rate having
grown 14% during the same period. By contrast,
we see a substantial increase in the adoption of
phishing-resistant authenticators. For example,
the WebAuthn adoption rate increased from 2% of
users in 2023 to 3% of users in 2024, while the Okta
Verify FastPass adoption rate increased from 2% of
users to 6% of users in the same time period.

There are three critical drivers for the growth of
phishing-resistant adoption. The first is the ever-
increasing threat of phishing attacks. For example,
the Okta security team observed that the number of
organizations that were impersonated by phishing
increased by 50% from February 2023 to January
2024 compared to the same period in the previous
year. Similarly, Zscaler saw a 58% increase in
phishing attacks last year using the data from their
network security products. [6]

The second is the availability of phishing-resistant
options. Okta offers support for a broad selection
of phishing-resistant authenticators, such as Okta
FastPass and FIDO2 WebAuthn. Simplifying access
to this technology has a direct impact on adoption.
Okta made FastPass, the passwordless, phishing-
resistant sign-in method built into Okta Verify,
available to all customers as part of the free upgrade
to Okta Identity Engine. We have observed that 7%
of new or migrated OIE tenants who upgraded to
OIE between February 2023 and January 2024 tried
FastPass within their first 90 days.

25

[6] https://www.zscaler.com/blogs/security-research/phishing-attacks-rise-
58-year-ai-threatlabz-2024-phishing-report

The Secure Sign-in Trends Report 2024

## Assessing authenticator usability and security

A data-driven
assessment of
authenticator
usability and
security

While MFA adoption is gaining ground, there are still
hurdles that must be overcome. To help CIOs, CSOs,
and policymakers make informed decisions on which
authenticators to adopt, it helps to understand the
benefits and drawbacks of each.

To this end, we developed a framework to assess
authenticators on both usability and security properties;
assessment categories are captured in Table 2. The
results give us data-driven insights to help security and
IT leaders better protect their organizations and guide
product development.

If you have read our 2023 Secure Sign-In Trends
Report, this section will look very familiar. For the 2024
report, we have updated the metrics, but you won’t
find many significant changes - the time it takes to
type in a password or receive an email code is pretty
consistent. However, we included more users and
events for this year’s study since more organizations
have migrated to OIE. Moreover, we improved our
methodology using Okta IT and Security practitioners’
survey inputs to determine the relative metric weights.
Despite the revised, more practical criteria, we arrive
at the same benefits of using a phishing-resistant
authenticator. Additionally, we added metric data for
smart card authenticators. We believe the insights
from this session are helpful to anyone evaluating
modern authentication methods, such as FastPass or
WebAuthn.

27

The Secure Sign-in Trends Report 2024

## Authenticator usability and security properties

Authenticator
challenge time

A double take on passwords

We included challenge times for a password authenticator under two optional UI configurations:

 • In the usernames and passwords flow, a user is presented with a username and password field on
the same page at sign-in.
 • In the password-only flow, a user enters their username on one page and is prompted to enter a
password on the next page.

The median challenge time for the password authenticator in the password-only scenario is the best-
suited condition to compare with other authenticator challenge times, given that the challenge times for
all other MFA authenticators do not require the user to identify their account prior to the challenge. We
nonetheless present both flows in the chart.

Authenticator challenge time measures the median
amount of time it takes users to successfully
complete an authenticator prompt.

The median challenge times are consistent year-over-
year for the authenticators. Password authentication
continues to show a median challenge time of about
six seconds. We assess that the challenge time
of passwords is biased towards a shorter value via
the assistance of password managers and browser
autofill