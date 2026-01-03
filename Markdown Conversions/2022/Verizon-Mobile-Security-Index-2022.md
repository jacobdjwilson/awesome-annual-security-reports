MSI

Mobile Security
Index 2022

## Who should read this report?
We produced this fifth annual Verizon Mobile Security Index to help security
professionals, like chief information security officers (CISOs), assess their
organization’s mobile security environment and calibrate their defenses. While
the report is packed with detail, there’s also lots of information that would be
interesting—and extremely relevant—to anybody involved in the specification,
procurement or management of IT devices and services.

## About this report
In April 2022, we commissioned an independent market research company
to survey more than 600 people responsible for security strategy, policy and
management. We also surveyed security practitioners and interviewed nine C-level
experts in the field. And again this year we worked with several leaders in mobile
device security: Absolute, Check Point, IBM, Ivanti, Jamf, Lookout, Netskope,
Proofpoint and Thales. These contributors provided additional information, including
incident and usage data.

We’d like to thank all our contributors for helping us to present a more complete
picture of the threats that affect mobile devices and what is being done to mitigate
them. This report wouldn’t be possible without them.

For more information on our methodology, see page 61.

MSI 2022

2

## Table of
contents

4

Zero Trust

Zero Trust network access

A continuous Zero Trust mindset

Conclusion

5

Appendices

Terminology used in this report

Survey methodology

Contributors

55

56

57

58

59

60

61

62

Foreword

Attacks are up—losses too.

Changing working practices is
a challenge.

Companies are more reliant on mobile
devices.

Security spend is rising in response.

3

4

5

6

7

Threats and defenses

3.1 Users and behaviors

Passwords

Phishing

Inappropriate content

The great exfiltrations

1

Introduction

Mobile is now critical.

Everywhere, all the time

Success brings unwanted attention.

The severity of attacks has grown.

Security spend

2

Bring your own dangers

Bring your own office

Bring your own device (BYOD)

Bring your own applications

How to secure BYOD devices

Training and acceptable use polices

How to work from home, securely

8

9

9

13

13

14

16

17

19

19

19

21

23

How to secure against phishing

How to create an effective
incident reporting process

3.2 Apps

App permissions

Malware

Ransomware

Mobile ransomware

How to secure apps

3.3 Devices and things

Lost or stolen devices

Device management

Check Point: The case for UEM

The dangers of things

How to secure IoT devices

3.4 Networks and clouds

Public Wi-Fi

Home Wi-Fi

24

25

26

28

33

34

35

36

37

38

39

40

43

44

45

46

46

47

48

49

50

51

52

MSI 2022 Table of contents

3

# Foreword

## Attacks are up—losses too.
In 2021, America experienced an unprecedented increase in cyberattacks and
malicious cyber activity. Normally, the legal team would never let us say something
as bold as that; they’d want evidence for such a dramatic statement. But those
words are verbatim from the opening of the FBI’s 2021 Internet Crime Report.1
And our research found that compromises that were known to involve a mobile
device followed this trend—in fact, the growth in the number of companies
affected was higher.

![Figure 1. Percentage of respondents that admitted their company suffered a compromise that involved a mobile device and led to the loss of data or downtime. [n=601, 671, 876, 856, 632]](Figure 1. QAPNW)

In 2021, the FBI’s Internet Crime Complaint Center (IC3) team received a record
847,376 complaints—a 7% increase from 2020. The estimated potential losses
were over $6.9 billion.1 Unsurprisingly, ransomware, business email compromise
(BEC) and the criminal use of cryptocurrency were among the most commonly
reported types of incident.

Close to half of the companies
that we surveyed said they had
suffered a compromise
involving a mobile device in
the past 12 months. Companies
with a global presence were
even more likely to have been
affected. More than three in
five (61%) had been hit,
compared to 43% of
organizations with only a
local presence.

1 FBI, 2021 Internet Crime Report, 2021

MSI 2022 Foreword

4

## Changing working practices are a challenge.
According to a survey by Proofpoint, 64% of people have changed where they
work. Changes driven by the pandemic have stuck. Sixty-eight percent of those
surveyed have started working from home either full time or some of the time.2
IT organizations did a stellar job enabling millions of people to work from home
on short notice. New security approaches and tools mean that employees
working from home can be just as secure as those working from the office.
And managing a mix of remote, home, hybrid and office-based employees
doesn’t need to be any more difficult either.

But companies are still struggling. Almost four-fifths of respondents agreed
that recent changes to working practices had adversely affected their
organization’s cybersecurity.

Almost four-fifths of
respondents agreed that
recent changes to working
practices had adversely
affected their organization’s
cybersecurity.

Over a fifth (22%) of IT leaders
in an Absolute study said that
their primary reason for
wanting employees to work
from the office is to maintain
a better corporate security
posture.3

Almost two in three CISOs across all regions agree that remote working makes
their organization more vulnerable to cyberattack.

2 Proofpoint, 2022 State of the Phish, 2022
3 Absolute, The Future of Work, 2022

MSI 2022 Foreword

5

## Companies are more reliant on mobile devices.
Companies are increasingly reliant on mobile devices. This is partly driven by the
shift toward more hybrid working, but there are several other factors too. For many,
mobile devices are no longer a secondary device.

We have more users
using mobile devices than
12 months ago.

Mobile users are doing
more with the devices than
12 months ago.

Mobile devices have access
to more sensitive data than a
year ago.

Many employees now have access to much of the same data—customer lists,
banking details, employees’ personal data, billing information, etc.—and systems—
messaging, enterprise resource planning (ERP), etc.—via their mobile devices as
they would sitting at a desktop in the office. This means that the compromise of a
mobile device can now pose a significant risk to customer data, intellectual property
and core systems.

Only one in eight respondents
said they had few (less than
10% of their workforce)
people working from home
or following a hybrid
working model.

MSI 2022 Foreword

6

## Security spend is rising in response.
Over three-quarters (77%) of respondents said that their security spend
had increased in the preceding year. More than a fifth said that it had
increased significantly.

![Figure 2. Year-over-year change in security spend. [n=632]](Figure TTIBF)

![Figure 3. Factors that respondents said drove the increase in security spend that they have seen in the preceding 12 months. [n=626]](Figure REMOG)

MSI 2022 Foreword

7

# 1 Introduction

## Mobile is now critical.
It’s worth remembering that one of the early successes in the mobile device field
was BlackBerry, and specifically BlackBerry Enterprise Server. The first thing that
springs to mind when most people think of BlackBerry is the physical keyboard. But
looking back, what’s really interesting about BlackBerry is that security was central
to how it was designed.

However, Blackberry’s dominance, driven by enterprise users, was quickly
overwhelmed by consumer-friendly devices from the likes of Apple. And that’s when
people started having better technology at home than at work. Executives around
the world started putting pressure on IT teams to give them devices for work that
were as user friendly as their personal devices. And it wasn’t just hardware, it was
apps too.

Today, few people even use the phrase “mobile phone”—unless you’re well over 40,
anyway—and laptops have become the norm. And it’s not just the hardware that’s
changed, what we do with it has exploded.

Mobile devices are now critical to how we work. With increased capabilities and
expansive connectivity, we now have access to far more information and tools than
we ever did in the days of desktops and personal digital assistants (PDAs). Partly
driven by the growth in cloud-based applications, a smaller screen no longer means
less powerful.

![Figure 4. Responses to the question “How critical are mobile devices to the smooth
running of your organization?” [n=632]](Figure WRTTQ)

When asked how critical, on a ten-point scale, mobile devices were to the smooth
running of their organization, 91% of respondents in our survey answered seven or
above—and 78% answered eight or higher. The picture was very similar regardless
of company operations (local, regional or global) and company size (small, medium
or enterprise size). The difference was no more than two percentage points up
or down.

![Figure 5. What proportion of your
organization’s staff work from each of these
locations most (80% or more) of the time?
[n=632]](Figure MLDMA)

MSI 2022 Introduction

9

## Everywhere, all the time
Fifteen years ago when we wrote about mobility, we often talked about the new
ability to work from anywhere at any time. Marketers came up with all kinds of
clever phrases, like “Make work an activity, not a location.”

Obviously, the COVID-19 pandemic had a dramatic impact on working practices.
But it didn’t create the trend toward more flexible working, it just accelerated it. On
average, about two-fifths (40%) of employees work from the office most of the time
(80% or more). About the same percentage (41%) work from home or “on the road”
most of the time.

There is a downside. For many people, “any time, anywhere” has evolved into
“everywhere, all the time.” Sometimes, it’s employers putting expectations on
employees to be contactable outside, often way outside, working hours. In some
cases, it’s employees themselves slipping into the habit of checking messages,
and more, at all hours of the day. It’s easy to find ways to justify it to yourself:
“This project is important,” “I’d rather know now than worry about it all night,”
and countless more.

Prior to 2016, employers in France were able to dismiss employees for failing to
respond to out-of-hours messages—and some did. Then the French government
passed a law giving workers the right to disconnect.5 Since then, Ireland, Italy
and Spain have enacted similar legislation. The province of Ontario is considering
enacting a similar law.

![Figure 7. Extract from Working for
Workers Act, 2021 in the Legislative
Assembly of Ontario.5](Figure 7)

![Figure 6. Reasons why employees feel unable to “disconnect” from work.4](Figure FCOLS)

Working excessive hours can affect mental health. LifeWorks found that the 21% of
workers who disagreed with the statement “I am typically able to disconnect from
work after usual work hours” had a Mental Health Index score 4.8 points lower than
those that were able to switch off.7

![Figure 8. Global Mental Health Index score by month.8](Figure JHSNI)

7, 8 LifeWorks, The Mental Health Index by LifeWorks, 2022

MSI 2022 Introduction

11

This is more than an interesting aside; there is a direct connection with
cybersecurity. In previous editions, we’ve discussed why mobile phones can
make it harder to spot an attack like a phishing email. Tired or distracted
employees are also more likely to tap on something that they shouldn’t.

Imagine two scenarios:

It’s mid-morning and you’re sitting at your desk in the
office. An email drops into your inbox. You double-click
it and start reading.

You’ve just taken a training course about phishing, so
you’re a bit suspicious. But the email includes some
personal information, looks professional and has no
obvious giveaways like bad grammar.

It’s late. You’ve been out for the evening and had a
couple of beers. You’re in a cab on your way home
when your phone buzzes in your pocket. You tap on the
notification and the email opens up.

You’ve just taken a training course about phishing, so
you’re a bit suspicious. But the email includes some
personal information, looks professional and has no
obvious giveaways like bad grammar.

What do you do?

• Hover over the button and check the actual URL in the
status bar
• Close the email and decide to review later
• Expand the message header and check the
sender’s address
• Close the email and decide to review later
• Flag the email as spam/suspicious

What do you do?

• Hover over the button and check the actual URL in the
status bar
• Close the email and decide to review later
• Expand the message header and check the
sender’s address
• Close the email and decide to review later
• Flag the email as spam/suspicious

Nearly two-thirds of
cyberattacks attributed
to insiders were assessed to
be due to negligence rather
than malicious intent.9

9 Ponemon, 2020 Ponemon Cost of Insider Threats Global Report, 2020

MSI 2022 Introduction

12

## Success brings
unwanted attention.
Now that mobile is so critical to business operations, it’s getting more attention
from bad actors too. From coordinated state-sponsored campaigns to unfocused,
opportunistic criminal exploits, the volume of attacks is going up. Whether the
attacker is a well-trained and well-resourced professional or an amateur taking
advantage of the many commercially available exploits, mobile devices are an
attractive target.

Growth in incidents and losses

Losses ($B)

Complaints (000s)

8

6

4

2

0

1,000

750

500

250

0

2017

2018

2019

2020

2021

![Figure 9. Reported incidents and losses, based on FBI data.10](Figure FFPLC)

Despite this, we still get respondents saying that mobile devices are of less interest
to cybercriminals than other IT assets—36% in our latest survey, up from 30% in our
2021 report.

## The severity of attacks has grown.
As mentioned earlier, 45% of respondents said that their organization had been
subject to a security incident involving a mobile device that led to data loss,
downtime or other negative outcome.

Of those respondents, 73% described the impact of the attack as major, and over
two-fifths (42%) said that it had lasting repercussions. That’s up from our previous
report, where less than half of incidents were described as major, and just 28%
were said to have had lasting repercussions.

Nearly half of SMBs that had
suffered a mobile-related
compromise said that the
impact was major and that it
had lasting repercussions.

10 FBI, 2021 Internet Crime Report, 2021

MSI 2022 Introduction

13

However, the 2021 data was a bit of an anomaly—wonder why? This year’s
severity figures show a return to the level we’ve seen since we started
producing the Mobile Security Index, just a little higher. Of course, with
a lot more respondents saying that their company had experienced a
mobile-related compromise, this means a lot more companies are facing
major, and lasting, consequences.

![Figure 10. Prevalence and severity of mobile-related compromises. [n=601, 671, 876, 856, 632]](Figure DPEMS)

Nearly three-quarters of
respondents from small and
medium-sized businesses said
that they perceived the risk as
significant or high—compared
to “just” 60% of those from
larger organizations.

## Security spend
These factors help explain why
77% of respondents said that their
cybersecurity budget had increased
in the previous 12 months—that’s
up from 65% in the previous edition
of this report—and close to a third
(29%) of those said it had increased
significantly.

Over three-quarters of
respondents said that their
cybersecurity budget had
increased in the previous
12 months.

And respondents expect their budgets
to grow again. Over three-quarters
said that they expected their budget
to grow in the following 12 months;
25% said they expected it to increase
significantly. Just 1% expected their
budget to decrease.

Over three-quarters of
respondents said that they
expect their cybersecurity
budget to increase in the
coming 12 months.

Over two-thirds said that
spend had increased in the
previous 12 months and they
expected it to rise again in the
next 12 months.

MSI 2022 Introduction

14

Of course, growing budgets sounds like good news for CISOs, but what really
matters is whether that budget is sufficient to meet needs—especially when needs
are growing as we’ve discussed.

Spend by NIST category

Four out of five (80%) of our respondents said that they expected their budget to
be adequate to do the job.

The most common objective for security spend was increasing the security of
existing user activities. That’s not as obvious a statement as it might seem at
first glance. With so many new hybrid workers and the continuous stream of new
applications and capabilities, you might expect that the focus would be on securing
new things, but apparently a lot of companies know that they have much to do to
secure existing activities.

In the past, companies focused their spend on Protect activities, as defined by
the National Institute of Standards and Technology (NIST) Cybersecurity
Framework. But our research found that companies are now spending more
evenly across the five NIST categories. This is a very encouraging sign.

Factors driving increase in security spend

Increasing security of
existing user activities

Integrating management
of phones, tablets and laptops

Enabling new services to
remote workers

Reducing burden on the IT
team (e.g., automating tasks)

Reducing incovenience to users
and increasing productivity

![Figure 12. Respondents’ estimated
breakdown of security spend by NIST
category. [n=632]](Figure JHUQM)

![Figure 11. Objectives for cybersecurity spend. [n=632]](Figure GKZPW)

According to a report by
Thales, two-fifths of
organizations are not confident
that their current security
systems could effectively
secure remote work.11

Over two-thirds of respondents
agreed that companies only
take cybersecurity seriously
enough after they have been
compromised.

The vast majority of companies
said that they have a defined
budget for mobile security.

11 Thales, 2022 Thales Data Threat Report, 2022

MSI 2022 Introduction

15

# 2 Bring your
own dangers.
Working patterns were changing long before
we all learned what a coronavirus is. But the
COVID-19 crisis catalyzed dramatic changes in
expectations, for both employers and employees.
These new behaviors have brought new
challenges and threats with them.

MSI 2022 Bring your own dangers

16

## Bring your
own office.
Biggest challenges to managing risk
and compliance under “work from
anywhere”policy

Right people
and culture

Challenges to managing  risk and compliance

How many times have you seen a “look what I just received” post on LinkedIn?
Somebody has just started a new job and received a new laptop, monitor and bunch
of logo’d swag—typically including a water bottle and a mousepad. That’s what
onboarding has looked like for a lot of people over the last couple of years.

As working from home has become more commonplace, people have invested in
building a more comfortable place to work. There’s been a boom in loft and garage
conversions, or if you’re really lucky maybe you splashed out on a “shed quarters”
at the bottom of the garden.

Over half of CISOs across all regions agree that targeted attacks on
their organizations have increased since adopting mass hybrid working.
Small organizations seem more affected, with 59% of companies with
500 or fewer employees saying their workforce has been targeted more
since they implemented hybrid working. At the other end of the scale,
only 48% of enterprises (5,000 employees and above) agree.12

Many of you reading this report will be seasoned remote workers. But recent
events have created millions of new home and hybrid workers. Despite this, many
companies haven’t provided employees with clear guidance on what’s expected.

![Figure 13. Challenges to managing risk
and compliance. Data from Absolute.13](Figure 13)

According to Thales, nearly
four in five organizations
are still “somewhat” or
“very concerned” about the
security risks and threats
that a greatly increased
remote workforce poses.14

12 Proofpoint, 2022 Voice of the CISO, 2022
13 Absolute, The Future of Work, 2022
14 Thales, 2022 Thales Data Threat Report, 2022

MSI 2022 Bring your own dangers

17

## Bring your own
device (BYOD).
The number of companies that said that they allow employees to use their own
devices dropped since the previous edition of this report. But in that report, over
half of the 70% of companies with a BYOD policy said that they’d adopted it during
lockdown. It seems likely that some will have done so only as a temporary measure
and rescinded it because it didn’t suit their company culture, caused security
problems or proved to be unpopular.

Securing BYOD devices can be considerably more difficult than securing company-
owned ones with a mobile device management (MDM) solution in place. Rigorous
policies and thorough enforcement will be required. See our discussion of Zero
Trust approaches on page 56.

One challenge of securing BYOD devices is getting users to follow company policy
on a device that they see as their property. Employees that receive a stipend may
be more willing to countenance their employer setting rules about how they use
devices and intrusions to their privacy. Over two-thirds (68%) of the respondents to
our survey whose company had a BYOD program said that this included such
a payment.

## Bring your own
applications.
It’s not just devices that people bring into the business. News reports have brought
to light incidents of officials—both in the U.S. and the U.K.—using encrypted
messaging apps like WhatsApp and Telegram to carry out government business.
And it’s not just in the public sector. It’s been reported that major organizations
have let people go for using unauthorized messaging apps. In 2021, one of these,
a major bank, was fined $200 million for insufficient monitoring and record keeping
associated with employees using unapproved messaging apps.

No matter what security measures you put in place, you can’t stop an employee
using an app like this on a personal device to conduct business conversations.
And if they do, it’s a lot harder, even impossible, to spot phishing attacks and
sensitive data being sent outside the company. It could also have serious
compliance implications.

This underlines the importance of making sure that security measures aren’t too
intrusive and that users understand why they are in place. The more draconian and
arbitrary security measures seem, the more likely users are to try and find ways
around them.

Allow employees to access
email on their own phones/
tablets.

A further 31% are considering
doing so.

Allow employees to use
their own phones/tablets to
access corporate systems
and data (BYOD).

A further 41% are considering
doing so.

Allow employees to use their
own laptops for work-related
tasks (bring your own PC, or
BYOPC).

A further 35% are considering
doing so.

![Figure 14. BYOD policies, current and under
consideration. [n=623]](Figure 14)

MSI 2022 Bring your own dangers

18

## How to secure
BYOD devices
These recommendations are structured
around the five functions in the
NIST Cybersecurity Framework.
To find out more,
visit nist.gov/cyberframework

### Identify
Develop a detailed BYOD policy that
clearly lists responsibilities in plain
language—this may involve translating it
into local languages.

### Protect
Educate users on the importance of
managing the permissions granted to
apps—users often aren’t aware of how
some permissions can be exploited for
nefarious purposes.

Consider implementing data loss
prevention (DLP) to detect and block
the exfiltration of information.

Give users an authorized—and easy-to-
use—means to share files outside
the company.

Implement an MDM solution to help
remotely secure, manage and support
personally owned devices.

Educate users on the dangers of
malware and how to reduce the
risks—malware can obviate protections
like containerization.

### Detect
Consider introducing endpoint
detection and response (EDR); this
uses behavioral-based analysis to
provide threat protection and can
provide valuable insight.

Consider implementing a Zero Trust
approach; this can reduce the reliance
on end users making informed and
security-conscious decisions—see
page 56 for more details.

### Respond
Consider restricting what resources
devices not controlled by the company
can access.

Ensure that users understand the
importance of keeping the operating
system (OS) and apps up to date.

Make sure that your team has the
training—or the third-party support—to
handle greater device variety.

Make sure that staff know what to do if
a device is lost or stolen, or they spot
something suspicious—this should be
part of your general security policy, but
it’s worth reiterating here.

Make reporting concerns easy—it
shouldn’t be something people have to
look up—and remember, the employee
might not be able to access company
systems when reporting an issue.

### Recover
Use mobile threat defense (MTD)
combined with unified endpoint
management (UEM) to help bring
devices that are out of compliance back
into line through self-remediation.

Develop a clear policy, in consultation
with your legal team, that covers the
tricky issues around performing
digital forensics on an employee-
owned device.

MSI 2022 Bring your own dangers

19

## Work
profiles

Non-remote workers

Remote workers

Employees that work inside a company-
controlled environment, the perimeter,
like an office, store or plant.

Employees that operate outside the
perimeter, whether on the road or
at home.

Back office

Commuters

Office-bound:
This includes a wide range of workers,
from call center staff to lawyers.
They might be required to work from
the office or choose to do so—not
everybody likes or has the right
conditions to work from home. These
workers typically rely on a local area
network (LAN) or wireless LAN (WLAN)
within the perimeter. They might work
from home a few times a month.

Omniworkers

Home workers:
People based at home or who work
from home a lot. This label can apply to
a wide variety of roles. They typically
use home Wi-Fi, perhaps with a virtual
private network (VPN).

Flexible workers:
Employees that work from home a few
days a week—there are all kinds of
reasons why. They commonly use home
Wi-Fi, perhaps with a VPN.

Front of house
Tethered

Floor workers:
This category includes many roles
in retail, hospitality, manufacturing,
etc. These workers aren’t fixed to a
desk, but their location doesn’t change
much. They are more likely to use a
specialized device. They will rarely
use a network not controlled by
the company.

Corridor warriors:
Employees that are never at their
desks, but their roaming is mainly
limited to one of the company’s
sites. They primarily use the
company’s WLAN.

Nomads

Road warriors:
These are the classic “remote
workers:” sales people, consultants,
CxOs of big companies, etc. They
need to be able to work from multiple
locations and work on the move. They
have complex requirements and use
multiple types of networks. They are
likely to need to use third-party Wi-Fi
and cellular connectivity.

Field workers:
Another well-established category.
It includes roles like service engineers.
People in this group often need to use
custom apps and work on the move—
so cellular connectivity is key. Their
primary device may be a customized
or ruggedized device.

MSI 2022 Bring your own dangers

20

## Training and acceptable
use policies

Nearly four-fifths (79%) of
people admitted to using a
work device for a personal
task, such as checking
personal email, shopping
or streaming.16

Nearly half of respondents
said their organization didn’t
have an acceptable use policy
in place.

### Lack of clarity on expectations
Some behavior is clearly unacceptable, such as accessing adult, extreme or illegal
content on company devices. This could not only damage your organization’s
reputation, this type of behavior could put your company at risk. But there are many
gray areas in defining appropriate use, especially when it comes to mobile devices.
What if employees want to use their work devices to check personal emails, stream
music or scroll through social media? Many people think this is a reasonable
allowance in a flexible, modern workplace.

Personal tasks carried out on work devices

By device “owner”

By friends/family

Personal email

Online shopping

Social media

Gaming

![Figure 15. Personal tasks carried out on work devices, by user and user’s friends/family.
Data from Proofpoint.15](Figure 15)

Part of the problem is that many companies struggle to develop an effective
acceptable use policy (AUP)—48% didn’t have one at all, an improvement from 57%
in our last report. Defining what counts as misuse of a work device can be tricky,
especially if your employees need to access social media and other content to do
their jobs, but creating clear guidance, including rules for mobile-specific content,
is crucial for helping prevent misuse.

Plus, with many employees now working from home, the lines are blurred
even further.

15, 16 Proofpoint, 2022 State of the Phish, 2022

MSI 2022 Bring your own dangers

21

### Lack of training
Many companies set high expectations on their employees but don’t give them
sufficient training to meet those standards.

Don’t give employees security
training on a regular basis.

Don’t give employees security
training when their working
arrangements change (e.g.,
start working from home).

### Lack of remote working guidance
We’ve seen a massive shift in working practices—even if only temporary for some
people—yet less than half of companies said that they have given employees
training on how that affects cybersecurity.

We have guidelines on what are
suitable locations for remote
working (e.g., home is okay,
coffee shop isn’t).

We issue guidance on
maintaining privacy
when working remotely
(e.g., when working in a
shared apartment).

It’s not our place to say how companies should manage abuse, but we advocate
creating a positive security culture. Creating a blame-free environment is likely to
encourage employees to report suspicious activity and mistakes that they may
make—enabling the organization to mitigate the damage.

MSI 2022 Bring your own dangers

22

## How to work from
home, securely
A guide for users

### Reduce risky behavior.
Read and understand your company’s
policies. Ask for further guidance on
anything you’re unsure about.

Try to keep your private and work life
separate.

Consider where you keep work devices
and any sensitive data—are these stored
safely when not in use?

Make sure that you’ve set a password
or PIN—or enabled Touch ID where
applicable—for access.

Configure your devices to lock
automatically after a few minutes
of inactivity.

Create a unique strong password
for each account, including email and
web applications

Turn on two-factor authentication
wherever possible.

Think about who can see or hear what
you are saying or typing on your screen.

Sign up to newsletters from trusted
organizations to improve your
cybersecurity skills and knowledge.

Install updates promptly—it can be a
bother, but failing to do so could put
your device, and the company, at risk.

Be frugal with which permissions you
give apps. Consult company policies on
what to limit on which apps.

### Secure your devices.
Don’t share devices—you may be
allowed to perform personal tasks,
but that doesn