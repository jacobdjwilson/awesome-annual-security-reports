# Mobile Security Index 2022

## Table of Contents
- [Foreword](#foreword)
- [Introduction](#introduction)
- [Bring your own dangers](#bring-your-own-dangers)
- [Threats and defenses](#threats-and-defenses)
  - [3.1 Users and behaviors](#31-users-and-behaviors)
  - [3.2 Apps](#32-apps)
  - [3.3 Devices and things](#33-devices-and-things)
  - [3.4 Networks and clouds](#34-networks-and-clouds)
- [Appendices](#appendices)

---

## Foreword

### Attacks are up—losses too.
In 2021, the FBI’s Internet Crime Complaint Center (IC3) team received a record 847,376 complaints—a 7% increase from 2020. The estimated potential losses were over $6.9 billion.[^1] 

![Figure 1: Percentage of respondents that admitted their company suffered a compromise which involved a mobile device and led to the loss of data or downtime.]

Close to half of the companies that we surveyed said they had suffered a compromise involving a mobile device in the past 12 months. Companies with a global presence were even more likely to have been affected. More than three in five (61%) had been hit, compared to 43% of organizations with only a local presence.

### Changing working practices are a challenge.
According to a survey by Proofpoint, 64% of people have changed where they work. Changes driven by the pandemic have stuck. Sixty-eight percent of those surveyed have started working from home either full time or some of the time.[^2]

Almost four-fifths (79%) of respondents agreed that recent changes to working practices had adversely affected their organization’s cybersecurity.

### Companies are more reliant on mobile devices.
Companies are increasingly reliant on mobile devices. 58% of respondents have more users using mobile devices than 12 months ago, 59% report mobile users are doing more with their devices, and 53% report mobile devices have access to more sensitive data than a year ago.

### Security spend is rising in response.
Over three-quarters (77%) of respondents said that their security spend had increased in the preceding year.

![Figure 2: Year-over-year change in security spend.]
![Figure 3: Factors that respondents said drove the increase in security spend.]

---

## Introduction

### Mobile is now critical.
When asked how critical mobile devices were to the smooth running of their organization on a ten-point scale, 91% of respondents answered seven or above—and 78% answered eight or higher.

### Everywhere, all the time
There is a downside to mobile flexibility. For many, "any time, anywhere" has evolved into "everywhere, all the time." Working excessive hours can affect mental health. LifeWorks found that the 21% of workers who disagreed with the statement “I am typically able to disconnect from work after usual work hours” had a Mental Health Index score 4.8 points lower than those that were able to switch off.[^7]

### Success brings unwanted attention.
Now that mobile is so critical to business operations, it’s getting more attention from bad actors. Whether the attacker is a well-trained professional or an amateur, mobile devices are an attractive target.

---

## Bring your own dangers

### Bring your own office.
As working from home has become more commonplace, people have invested in building a more comfortable place to work. However, many companies haven’t provided employees with clear guidance on what’s expected.

### Bring your own device (BYOD).
Securing BYOD devices can be considerably more difficult than securing company-owned ones. Rigorous policies and thorough enforcement are required.

### How to secure BYOD devices
Recommendations are structured around the five functions in the NIST Cybersecurity Framework:
- **Identify**: Develop a detailed BYOD policy.
- **Protect**: Implement an MDM solution and educate users on app permissions.
- **Detect**: Consider introducing endpoint detection and response (EDR).
- **Respond**: Ensure staff know what to do if a device is lost or stolen.
- **Recover**: Use mobile threat defense (MTD) combined with unified endpoint management (UEM).

---

## Threats and defenses

### 3.1 Users and behaviors
The human element continues to drive breaches. Over four-fifths (82%) of breaches analyzed for the 2022 DBIR involved the human element.[^17]

#### Passwords
Attackers exploit a range of social and technical vulnerabilities to steal or crack credentials, including guessing, social engineering, credential stuffing, password spraying, brute force, shoulder surfing, and keyloggers.

#### Phishing
In 2021, five out of six organizations experienced a successful email-based phishing attack.[^19] Attackers are increasingly designing phishing sites specifically for mobile devices, taking advantage of smaller screens and user distractions.

#### How to secure against phishing
- Identify "very attacked people" (VAPs).
- Carry out "real world" attack simulations.
- Implement solutions that block inbound email threats.
- Use web isolation solutions to restrict suspicious URLs.

#### How to create an effective incident reporting process
1. **Make it easy**: Ensure the system is accessible even if the user lacks email access.
2. **Define multiple workflows**: Route reports based on type, severity, and location.
3. **Leverage automation**: Use automated alerts to speed up response times.

---

## Appendices

### Terminology used in this report
- **BYOD**: Bring Your Own Device.
- **MDM**: Mobile Device Management.
- **MTD**: Mobile Threat Defense.
- **UEM**: Unified Endpoint Management.
- **VAP**: Very Attacked People.

### Survey methodology
In April 2022, we commissioned an independent market research company to survey more than 600 people responsible for security strategy, policy and management.

### Contributors
This report was produced in collaboration with leaders in mobile device security: Absolute, Check Point, IBM, Ivanti, Jamf, Lookout, Netskope, Proofpoint, and Thales.

---

[^1]: FBI, 2021 Internet Crime Report, 2021
[^2]: Proofpoint, 2022 State of the Phish, 2022
[^7]: LifeWorks, The Mental Health Index by LifeWorks, 2022
[^17]: Verizon, Data Breach Investigations Report, 2022
[^19]: Proofpoint, 2022 State of the Phish, 2022

---

complex project. You
could do it using a Google Form.

4. Create an audit trail.

Obviously, the primary purpose of an
incident reporting process is to enable
employees to report incidents and
action those reports. But the information
gathered as part of this process can
be invaluable to later forensic analysis.
It’s important to record everything that
you can: What was reported, when
and by whom. Consider using existing
tools to record the progress of a report.
Though not specifically designed for
the purpose, applications like Jira and
Slack are easy to use, record a journal
of activity and enable you to set up
automated notifications.

60%

Meeting with manager or
infosec team

52%

Negative mark on
performance review

45%

Disciplinary action, such as a
written warning

31%

Monetary penalty

15%

Termination

Figure 21. Penalties for falling for a phishing
email, real or simulated, reported by
respondents. Data from Proofpoint.36

MSI 2022  Threats and defenses
MSI 2021  Foreword

36
36

3.2 Apps

The number of apps, especially web-based apps, continues to
grow apace. Malware remains a major problem, but even non-
malicious apps, including those downloaded from official stores,
can be a threat.

46%

Nearly half of those that had
suffered a mobile-related
security breach said that app
threats were a contributing
factor. Those in the energy and
utilities sector were most likely
to list this as a factor, 55%.

MSI 2022  Threats and defenses

37

App permissions

Hands up, who has ever read the terms and conditions when making a purchase
or installing an app on a mobile device? We’re guessing that there aren’t many
hands up right now.

As we’ve discussed in previous editions of this report, giving applications access
to the camera, microphone, photos, location data and other data and device
functions can be a significant security risk.

It’s very easy to just click accept, but users should be careful about applications
requesting permissions that they don’t really need. For example, according
to Jamf research, 53% of finance applications request permission to access
location data. Only 62% of navigation apps ask for the same access!

Percentage of apps per category requesting specific iOS permissions

Photos

Camera

Location

Microphone

Calendar

Contacts

Bluetooth

Voice
processing

Health

Local
network

66% 78% 69% 63% 65% 79% 71% 49% 68% 53% 50% 62% 96% 75% 87% 84% 67% 52%

65%

60%

75%

54%

54%

58%

74%

56%

44%

68%

39%

48%

43%

90%

70%

83%

83%

54%

52%

61%

58% 63% 42% 57% 53% 81% 61% 43% 66% 46% 62% 61% 68% 47% 81% 72% 64% 60% 55%

34%

44%

40%

40%

24%

32%

15%

19%

36%

41%

21%

41%

64%

44%

33%

69%

21%

20%

38%

29% 28% 22% 38% 18% 31% 56% 23% 31% 36% 27% 31% 18% 23% 26%

35%

41%

33%

25%

27%

37%

19%

20%

36%

46%

9%

15%

31%

13%

22%

21%

44%

37%

37%

59%

20%

27%

26%

25% 26% 21% 39% 17% 42% 18% 23% 29% 35% 22% 25% 31% 22% 25% 26% 31% 20% 26%

9%

14%

15%

3%

9%

10%

2%

7%

8%

7%

6%

3%

8%

12%

13%

18%

5%

7%

9%

2% 1% 1%

1% 1%

3%

2% 23%

3%

1% 1% 1%

0%

1%

1% 1%

4%

1%

1%

1%

1%

1%

1%

0%

0%

0%

0%

1%

0%

0%

0%

1%

1%

0%

2%

0%

0%

1%

All

Business

Education
Entertainment

Finance
Food and drink

Games

Health and fitness

Lifestyle

Music

Navigation

Figure 22. Permissions requested by Apple iOS apps. Data from Jamf.37

News

Photo and video

Productivity

Sports

Travel

Utilities

Social networking
Shopping

37   Jamf, An Analysis of iOS App Permissions, 2021

MSI 2022  Threats and defenses

38

Malware

The 2022 Verizon Data Breach
Investigations Report found that over
30% of breach cases involved some
form of malware.38 And according to
Jamf, the percentage of organizations
that experienced the installation of
malware on a remote device doubled
in 2021, going from 3% to 6%.38

Over the years, one of the problems
we’ve faced when writing this report is a
lack of mobile-specific stats on threats
and compromises. In fact, that’s why
we started producing this report. Often,
people will talk about the actions that
attackers use, such as phishing, and the
asset that was the eventual target, say a
server, but not the device that provided
the opening for the attack in the
first place.

As we’ve shown, attackers do design
phishing campaigns specifically
targeting mobile devices, and they
build malware specifically for mobile
devices too.

The built-in security features on some
phones and the degree of control
associated with using official app stores,
such as Google Play, do offer some
protection. But attackers manage.

Lorem ipsum
Check Point Research recently tracked
the development of a new form of
malware. “Rogue” is a form of mobile
remote access Trojan (MRAT) that can
gain control over the host device and
exfiltrate data such as photos, location,
contacts and messages; modify the
files on the device; and download other
malicious payloads.

Rogue is particularly adept at digging in
and avoiding removal:

•  It adopts the services of the Firebase
platform to disguise and masquerade
as a legitimate Google service

•  Once it gets all the required

permissions, it hides its icon to make
it harder for the user to get rid of it

•  It registers itself as a device

administrator; if the user tries to
revoke this permission, they are
presented with an “Are you sure to
wipe all the data?” dialog

Malware comes in many forms, but in
recent years ransomware has become
the most common.

70%

Ransomware was present
in almost 70% of malware
breaches analyzed for
the 2022 Data Breach
Investigations Report.39

38   Jamf, Security 360 Annual Trends Report, 2022
39   Verizon, Data Breach Investigations Report, 2022

MSI 2022  Threats and defenses

39

Ransomware

You must have been hiding under a rock for the last few years if you haven’t heard
about ransomware. It’s been behind some of the most high-profile compromises in
the past decade. But just in case you have been busy, here’s a quick definition.

Ransomware is a form of malware that denies a user or
organization access to files on their computers. Files are
encrypted and a ransom demanded for the decryption key.
Ransomware is no longer limited to individual machines and
many attackers target servers or cloud services. Some
variants have added additional functionality—such as data
theft or exposure—to further incentivize victims to pay up.40

75%

Three-quarters of
ransomware attacks start
with email phishing.44

In previous editions of this report, we have discussed some of the variants of
ransomware, including doxware. We won’t go over those again here, but we
saw a new angle during 2021.

Several companies reported employees receiving emails soliciting them to become
accomplices in a ransomware attack. The emails targeted users with access to
company servers and offered a substantial return if the attack was successful.

Think you’re covered? Think again.

According to the U.S. Government Accountability Office (GAO), the percentage of
companies with cyber coverage increased from 26% in 2016 to 47% in 2020.41 But
insurance is no panacea. As payouts have increased,42 insurers have tightened up
policies, reduced coverage and increased premiums.43 Between 20Q1 and 21Q3,
renewal premiums increased more than 2.5-fold. Not only are premiums increasing,
the rate at which they have increased has grown.

Percentage change in
renewal premiums

+28%

25%

20%

15%

10%

5%

0%

’20/Q1

’20/Q3

’21/Q1

’21/Q3

Figure 23. Increase in cyber insurance
renewal premiums.45

40  Proofpoint, Stopping Ransomware Hub, 2022
41   U.S. Government Accountability Office, Cyber Insurance: Insurers and Policyholders Face Challenges in an Evolving Market, 2021
42   Fitch, Sharply Rising Cyber Insurance Claims Signal Further Risk Challenges, 2021
43   ACA Group, Cyber Insurance: Top Five Trends for 2022, 2022
44  Check Point, What is Ransomware?, 2022.
45  The Council, Commercial Property Casualty Market Index: Q3/2021, 2021

MSI 2022  Threats and defenses

40

64%

Nearly two-thirds of
respondents in a Proofpoint
study said that their
organization had paid a
ransom to try and resolve a
ransomware incident.48

To pay or not to pay?

There are several reasons why companies choose to pay the ransom:

Reduce downtime
Downtime is costly, so paying the ransom and avoiding lengthy disruption
can look like an attractive option.

Protect reputation
Some people may think that paying up quickly could help keep the
compromise quiet, even obviate the need to publicly admit “we’ve been
hacked” and damage customer and investor confidence.

Avoid recovery costs
The ransoms stated in some of the stories that hit the headlines can be tens
of millions, but they are usually a lot lower—21% of ransoms paid were under
$10,000.46 If the costs of bringing in the experts, replacing hardware,
rebuilding devices and servers, etc., are higher, doesn’t paying up make
business sense?

Protect privacy
Companies don’t want their dirty linen, or their data, exposed. For some,
the ransom is a more palatable loss.

But there is widespread agreement among experts that paying the ransom is a
bad idea:

•  The attacker won’t send the unlock code at all—this happens quite often

•  The unlock code may not work—according to a Sophos study, only 4%

that pay up get all their data back; the average was 61%47

•  There are technical issues with decrypting files—this has been reported by

many users

•  The attacker may demand a further payment or payments—sometimes
this is linked to not publishing the files, an attack known as doxware

Those are the selfish reasons for not paying. There’s also a social reason.
Paying up incentivizes attackers to carry out more attacks. Unfortunately,
it’s a bit like when we’re faced with a traffic jam; we wish that everybody
else would turn around and give us a clear road ahead.

There might soon be another reason not to pay up; it might be against
the law.

46, 47   Sophos, The State of Ransomware 2022, 2022.
48  Verizon, Data Breach Investigations Report, 2022

MSI 2022  Threats and defenses

41

Paying up may be illegal.

The U.S. government has already communicated that paying up could be contrary to
existing laws intended to block the funding of groups involved in crime or terrorism.

Bills to specifically outlaw the payment of ransoms have been discussed in several
countries, including the U.S. On March 15, 2022, U.S. President Biden signed the
Cyber Incident Reporting for Critical Infrastructure Act (CIRCIA) into law. It places
mandatory reporting obligations in connection with cybersecurity incidents on a
broad range of private and public-sector entities operating in “critical infrastructure”
sectors. Companies covered by the act must report “substantial” cyber incidents to
the Cybersecurity and Infrastructure Security Agency (CISA) within 72 hours. And if
they pay a ransom, they must report doing so within 24 hours. Similar laws are being
considered in several other countries.

“Companies that facilitate ransomware payments to cyber
actors on behalf of victims, including financial institutions,
cyber insurance firms, and companies involved in digital
forensics and incident response, not only encourage future
ransomware payment demands but also may risk violating
OFAC [Office of Foreign Assets Control] regulations.”49

“The FBI does not advocate
paying a ransom, in part
because it does not
guarantee an organization
will regain access to its
data. In some cases,
victims who paid a ransom
were never provided
with decryption keys. In
addition, due to flaws in the
encryption algorithms of
certain malware variants,
victims may not be able to
recover some or all of their
data even with a valid
decryption key.

Paying ransoms
emboldens criminals to
target other organizations
and provides an alluring
and lucrative enterprise to
other criminals. However,
the FBI understands that
when businesses are faced
with an inability to function,
executives will evaluate all
options to protect their
shareholders, employees,
and customers.”

—FBI50

49  U.S. Department of the Treasury, Updated Advisory on Potential Sanctions Risks for Facilitating Ransomware Payments, 2021
50  FBI, 2021 Internet Crime Report, 2021.

MSI 2022  Threats and defenses

42

Mobile ransomware

Ransomware has been a thorn in the side of cybersecurity teams for the past
several years. It’s not just big companies that should be concerned about
ransomware; companies of all sizes in all industries have been attacked.
And mobile devices are a common component of attacks.

The remote environment is primed for ransomware.

As organizations continue to support remote or hybrid work, they no longer have the
visibility and control they once had inside their perimeter. Attackers are exploiting this
weakness and profiting. Here are three reasons they’re able to do so:

•  Most organizations now have employees working from anywhere

•  These employees expect seamless access to all resources from unmanaged and

personal devices on networks outside the traditional perimeter

Hank Schless
Senior Manager, Security Solutions
Lookout

•  This greatly reduces the visibility and control that security teams have and can
make it difficult to understand risks posed by users and the devices they’re
working from

Mobile devices make it easier for attackers to phish credentials.

Attackers are always looking for ways into your infrastructure. Compromising
an employee’s credentials enables them to gain legitimate access and remain
undetected. Their primary tactic for stealing credentials is to phish employees on
mobile devices. Because phones, tablets, etc., are used for both work and personal
tasks, employees can be targeted through multiple apps such as SMS, social media
platforms and third-party messaging apps. The simplified user interfaces of a phone
or tablet hide signs of phishing and make them ripe targets for socially engineered
phishing campaigns.

VPNs enable lateral movement.

Organizations rely on VPNs to give their employees remote access to resources,
but this approach has a number of security shortcomings. First, a VPN may grant
individuals the capability to traverse to any app across your network from a single
point of entry. Second, VPNs don’t evaluate the context under which users or devices
connect. Context is necessary to detect activity that’s indicative of a compromised
account or device.

Ransomware groups now operate like businesses. There is more evidence of
organized groups carrying out scalable campaigns that increase their success rate
and enable them to reinvest in new tools and procedures. Regardless of where or how
we work, these groups continue to take advantage of vulnerable architecture to extort
money from victims. Many organizations have taken steps to protect themselves from
ransomware attacks, but attackers continue to evolve their tactics, and companies
must respond.

MSI 2022  Threats and defenses
MSI 2021  Foreword

43
43

How to
secure apps

Recover

Identify

NIST
Framework

P
r
o

tect

d
n
o
p

Res

Detect

These recommendations are structured
around the five functions in the NIST
Cybersecurity Framework.

To find out more, visit
nist.gov/cyberframework

Identify

Detect

Audit company systems and processes
for vulnerabilities to malware.

Implement an MTD solution to quickly
identify potential threats.

Subscribe to a threat intelligence
service to stay abreast of the latest
malware threats.

Conduct regular network penetration
tests to identify possible vulnerabilities—
and act on the findings.

Protect

Educate users on how to identify and
report unexpected system behavior—
something a user may just see as an
annoyance, like a device constantly
needing charging, could be an indicator
of malware infection.

Monitor devices for unusual behavior—
including excessive data transfer and
out-of-hours use.

Deploy anti-malware functionality to
all devices.

Respond

Add content filtering to all external
gateways to make it more difficult for
attackers to deliver malicious content
to users via their web browser
and email.

Where possible, prevent the use
of removable media such as USB
drives—at the very least, disable
auto-run functions and set up devices
to automatically scan removable media
for malicious content.

Ensure that your backup policies
are effective—backups should not
be connected to the computers and
networks they are backing up; for
example, store them offline.

Verify your backups often—an
emergency is a bad time to find
out that there’s a problem.

Use deny listing on external
gateways to block access to known
malicious websites.

Identify all infected devices and
physically disconnect them from
the network.

Suspend the login credentials of
any accounts that may have been
compromised.

Notify all users of the compromised
app and what action to take—deleting
the app may not always be the best
course of action, as this could destroy
important forensic data.

Recover

Reset all credentials, especially those
with administrator privileges, that may
have been compromised.

Wipe all infected devices and reinstall
from the OS up.

Conduct a postmortem exercise
to determine how the malware
managed to get through and where
controls, processes and technology
fell short, and then distribute an
“after action” report.

MSI 2022  Threats and defenses
MSI 2021  Foreword

44
44

3.3 Devices
and things

With the volume of devices a modern enterprise relies on, keeping
them all up to date can seem like a Sisyphean task. With more and
more devices, the danger of lost or missing devices grows. But
it’s not just the quantity of devices that’s growing, the variety is
growing too. Today there are smartphones, laptops, tablets,
hybrids (like Microsoft Surface), Chromebooks, wearables and
a seemingly endless range of connected devices.

46%

Over a third of those that had
suffered a mobile-related
security breach said that
device-based threats were a
contributing factor. Those in
the healthcare sector were
most likely to list this as a
factor, 47%.

MSI 2022  Threats and defenses

45

Lost or
stolen devices

People leave phones, tablets and laptops in taxis, on trains, at restaurants—the list
goes on and on. Some of these will end up in a lost-and-found box, and others will
find a new owner—or rather a new owner will find them.

One of the reasons so few organizations are worried is because loss/theft is one
of the types of attack that’s easiest to mitigate. Protections like device encryption
and remote wipe are now standard with most types of user devices and MDM.
But that doesn’t mean that companies, or their employees, are using them.
Whole-disk encryption and PIN security codes should be activated as a standard
precaution on all devices. With these simple precautions in place, even if a device
is stolen, the data it holds will be—for all intents and purposes—worthless to
the attacker.

Mobile device
management

MDM is not mobile security. MDM
solutions were never designed
to protect against sophisticated
cyberattacks. The purpose of
these solutions have always been
management—the clue is in the name.
The security capabilities of these
solutions have always been quite
limited. They can be useful in ensuring
applications are kept up to date and
some other policies are being followed.
But devices are prone to threats like
phishing even with MDM in place, as
this data from Lookout shows. This
shows that the difference in encounter
rate is small, and on occasion devices
with MDM even faced more attacks.

51  Lookout, data supplied, June 2022

MSI 2022  Threats and defenses

Encounter rate of phishing attacks on devices with/without MDM

MDM

No MDM

3-month rolling average

3-month rolling average

20%

15%

10%

5%

0%

20Q1

20Q2

20Q3

20Q4

21Q1

21Q2

21Q3

21Q4

22Q1

Figure 24. Incidence of phishing attacks on devices with/without MDM in place.
Data from Lookout.51

46

The case for MTD

Unified endpoint management (UEM) solutions—or their predecessors, mobile
device management (MDM) solutions—were designed to help mobilize businesses
by streamlining processes, managing device life cycles and creating a managed
workspace on smartphones and tablets. Today, UEM solutions have evolved into
consolidated solutions that work with other endpoints beyond mobile devices,
including PCs.

UEM enforces some device-level policies—such as device encryption and remote
wipe—to maintain a basic hygiene and some have a basic jailbreak/root detection
function too. But these basic features don’t provide the protection needed to
withstand even the most basic mobile malware attack. UEMs do not scan for mobile-
related threats like malicious apps, vulnerable operating systems or network-based
attacks, nor do they protect users against phishing and other social engineering
attacks. Even with a UEM solution in place, organizations remain exposed to
credential theft, data leakage or device takeover.

A mobile threat defense (MTD) solution is essential to keep corporate data on
mobile devices secure, protected from all attack vectors.

To find out more, read the Check Point white paper, Mobile Management Solutions
Are Not Security.52

Features

MDM/UEM

MTD

Device life-cycle management

App management and containerization

Remote access

Conditional access

Jailbreak/root detection

Malicious app detection

Download prevention

Anti-phishing (known and unknown sites)

Anti-bot (blocking C&C communications)

Man-in-the-middle attack prevention

URL filtering

Real-time threat intelligence

•

•

•

•

Partial

•

•

•

•

•

•

•

•

•

Pete Nicoletti
Field CISO
Check Point

UEMs do not scan for
mobile-related threats like
malicious apps, vulnerable
operating systems or network-
based attacks, or protect
users against phishing and
other social engineering
attacks. As a result, users and
organizations remain exposed
to credential theft, data leakage
or device takeover.

52  Check Point, Mobile Management Solutions Are Not Security, 2021

MSI 2022  Threats and defenses
MSI 2021  Foreword

47
47

The dangers
of things

One of the challenges of securing IoT projects is the lack of centralized
coordination of projects. In many organizations, IoT projects are led by the lines
of business and don’t even have to follow standard security requirements.

Remember, an IoT device can be an attack vector (a weak point that can be
exploited to mount an attack), a vehicle for attacks (like a part of a botnet used
to carry out a distributed denial-of-service (DDoS) attack) or a target in its
own right.

42%

Lines of business/business
units initiate their own
IoT projects.

59%

IT has oversight of all
IoT projects.

48%

53%

There is central coordination
of all IoT projects.

We have defined IoT security
standards that apply to
all projects.

The nature of IoT devices themselves also presents distinct challenges compared to
securing other mobile devices. These fall into three broad areas:

Variety

Distance

Longevity

The sheer volume and
diversity of IoT devices can
present enormous logistical
obstacles to effective device
security. It doesn’t help that
many IoT products have been
found to have extremely weak
cybersecurity—including security
devices such as smart locks,
doorbells and, ironically,
security cameras.

Many IoT devices are out in the
field. This can make them
vulnerable to physical tampering
or network attack and harder to
update or replace. Isolation can
also make devices vulnerable to
SIM theft, one of the simplest
types of attack to carry out—
often all that’s required is a
screwdriver. All the hacker has to
do is break open the connected
device, such as a smart lamppost,
and remove the SIM. This can
then be put into another device,
giving the user free calls and data
at the organization’s expense.

In the survey for the previous
edition of this report, we found
that over half (54%) said that
some of their IoT devices had an
anticipated lifetime of five years
or more—up from 36% in our
previous report. This would be
very old for a smartphone or
laptop. Combined with the
difficulty of updating devices,
this can make it hard to keep IoT
protected against constantly
evolving threats.

MSI 2022  Threats and defenses

48

How to secure
IoT devices

Recover

Identify

NIST
Framework

P
r
o

tect

d
n
o
p

Res

Detect

These recommendations are structured
around the five functions in the NIST
Cybersecurity Framework.

To find out more, visit
nist.gov/cyberframework

Identify

Thoroughly review the security before
you purchase anything.

Ensure that users developing or
purchasing IoT programs work with
the information security team to factor
in the cost and resources required to
secure devices and applications.

Ask potential vendors to supply details of
their security measures, and review them
for robustness.

Detect

Protect

Harden all devices, including
ensuring they are tamper-resistant
and tamper-evident.

Change all default or vendor-
supplied passwords.

Use network intrusion detection tools
to monitor all traffic, incoming and
outgoing, for unusual activity and put in
place a process to handle any
alerts promptly.

Subscribe to a threat intelligence
service to get early warning of
emerging threats.

Change all default or vendor-supplied
passwords, really.

Analyze logs for signs of suspicious
behavior.

Shut down anything you don’t
need—if you’re not using a port or
protocol, block it.

Keep devices patched—use over-the-
air (OTA) updates to help keep devices
secure, especially those in remote or
difficult-to-access locations.

Bind SIMs to devices, limiting the
potential damage of SIM theft.

Use private, non-routable IP addresses
to make it harder for attackers to
access IoT devices.

Consider using a private cellular
network to keep devices off the
public internet.

Encrypt data in transit and at rest.

Create an IoT security assurance
process that regularly analyzes IoT risk
data in your organization.

Integrate MTD with EDR or security
incident event management (SIEM) to
help simplify monitoring and, should it
be necessary, forensic analysis

Respond

Put controls in place to contain the
spread of infection and prevent the
attacker from gaining any additional
access or access to sensitive data.

Implement network blocks to limit an
attack from infecting more devices
or the attacker from accessing more
critical systems.

Recover

Conduct a postmortem to determine
how the attack managed to get
through and where controls, processes
and technology fell short, and then
distribute an “after action” report.

MSI 2022  Threats and defenses
MSI 2021  Foreword

49
49

3.4 Networks
and clouds

Insecure networks remain a serious threat to mobile device
security. Attackers can intercept traffic through man-in-the-
middle (MitM) attacks or lure employees into using rogue Wi-Fi
hotspots or access points. Cloud-based services are now used
for many mission-critical tasks. They are also one of the reasons
that mobile devices have become more critical to business.
That brings a whole new range of problems.

“ There is a distinct imbalance between protecting a
network and attacking it, and this imbalance continues to
grow as more effective hacking resources become available
at a significantly lower cost. But without continuous
investment and commitment to cyber resilience,
organizations will be more vulnerable to cyberattacks
and thus more likely to endure reputational, financial,
operational and safety impacts.”

—World Economic Forum, 202253

52%

Over half of those that had
suffered a mobile-related
security breach said that
network threats were a
contributing factor. Those
in the financial services
sector were most likely to
list this as a factor, 61%.

53  World Economic Forum, Global Cybersecurity Outlook 2022, 2022.

MSI 2022  Threats and defenses

50

Public Wi-Fi

Another familiar topic. With traveling off the agenda, public Wi-Fi may not have
been on your list of most pressing issues last year, but it remains a critical issue.
Reports suggest that corporate travel is at less than 50% of pre-pandemic norms
and experts suggest that it will take years to recover—if it ever does. But the
dangers of public Wi-Fi aren’t limited to executives jetting around the world,
or even employees traveling by plane, train or automobile.

There’s a lot of disagreement about working models, how they have changed and
how they may change in the future. But it’s safe to say that fewer people are now
following the traditional model of commuting to the office five days a week. For a
lot of people, that means working from home a couple of days a week or more.
Maybe that includes the odd afternoon in a coffee shop for a change of scenery.
Or whether you work from home or not, who hasn’t checked their email when
at the mall or in a restaurant or other public place. With reliable, high-speed mobile
internet now widely available, you might do this on a cellular connection. But
whether for performance or to avoid data caps, people still use public Wi-Fi, with
all its attendant dangers.

Less than a third of organizations (32%) ban the use of public Wi-Fi, and only about
half (52%) of those actually do anything to enforce that policy.

In fact, 43% of respondents working for companies that banned the use of public
Wi-Fi admitted breaking the rule themselves.

Public Wi-Fi policy

Banned

No policy

Allowed

0%

25%

50%

75%

100%

Blocking of public Wi-Fi

Blocked

Not blocked

0%

25%

50%

75%

100%

Figure 25. Public Wi-Fi policy. [n=632]

Ah, you might say, but it’s okay as long
as you use a virtual private network.
VPNs do offer a degree of protection,
but many companies still rely on an
“honor approach.” Even among the
informed audience that made up our
survey respondents, 8% admitted to
not using a VPN when using public
Wi-Fi. It’s quite likely that this is an
underestimate—many people will
forgive themselves the odd slipup. It’s
highly likely that this number is much
higher among employees that don’t
work in cybersecurity.

x2

In 2021, the number of devices
connecting to a risky hotspot
per week doubled from 0.5%
to 1%.54

46%

Nearly half of VPN clients
are misconfigured or
out of date.55

See our discussion of Zero Trust
approaches on page 56.

54  Absolute, The Future of Work, 2022
55  Jamf, Security 360 Annual Trends Report, 2022.

MSI 2022  Threats and defenses

51

Home Wi-Fi

With fewer people working in the office five days a week, it’s inevitable that more
business is being done over home Wi-Fi and home broadband connections.
It’s unsurprising then that nearly four-fifths of businesses allow employees to
use their home networks.

Home Wi-Fi policy

Banned

No policy

Allowed

0%

25%

50%

75%

100%

Figure 26. Use of home Wi-Fi. [n=632]

While likely to be less risky than public Wi-Fi (see our 2019 report), home Wi-Fi is
still a concern. Ask yourself how many employees have:

Changed the default password on their home router?

Shared their router password with dozens of friends and family members—maybe
even neighbors?

Updated their router firmware since receiving it?

Looked at router logs for signs of intrusion?

MSI 2022  Threats and defenses

52

Proofpoint surveyed 3,500 working
adults across Australia, France,
Germany, Japan, Spain, the U.K. and
the U.S. It found that most hadn’t taken
basic security measures to protect
their home Wi-Fi network.56

Of those who hadn’t taken steps to
secure their home Wi-Fi, 62% said that
was because they weren’t concerned
about the security of their home
network. Close to 90% of the rest said
it was because they didn’t know how to.

82%

never updated
router software/
firmware.

80%

had never changed
their router
password.

74%

hadn’t changed
their Wi-Fi
password.

74%

hadn’t changed
their Wi-Fi
network name.

40%

didn’t password-
protect their Wi-Fi.

11%

didn’t do any
of the above.

Figure 27. What measures working adults took to protect their home Wi-Fi network.

56   Proofpoint, 2022 State of the Phish, 2022

MSI 2022  Threats and defenses

53

How to secure
networks

Recover

Identify

NIST
Framework

P
r
o

tect

d
n
o
p

Res

Detect

These recommendations are structured
around the five functions in the NIST
Cybersecurity Framework.

To find out more, visit
nist.gov/cyberframework

Identify

Detect

Remember that mobile devices could
provide an entry point for a wide range
of attacks; consider ways that attackers
could disrupt operations as well as
expose data.

Use network intrusion detection tools
to monitor all traffic, incoming and
outgoing, for unusual activity and put
in place a process to handle any
alerts promptly.

Protect

Re-architect your network into smaller
segments, isolating the hosts and
services that hold sensitive data.

Implement  a “least privilege” access
policy—if people don’t absolutely need
access, they shouldn’t have it, and
access should be revoked when no
longer required.

Secure all wireless access points;
allow only known devices to connect to
corporate Wi-Fi services.

Educate users on the dangers of Wi-Fi,
including rogue access points.

Consider providing users with a
fixed wireless access (FWA) device—
sometimes called mobile broadband—
exclusively for use when working
from home.

Subscribe to a threat intelligence
service to get early warning of
emerging threats.

Analyze logs for signs of suspicious
behavior.

Integrate MTD with EDR or SIEM to
help simplify monitoring and, should it
be necessary, forensic analysis.

Respond

Create an IR plan that covers how
to qualify and categorize incidents,
what should be done and who the
responsible parties are.

Recover

Conduct a postmortem to determine
where controls, processes and
technology fell short and then distribute
an “after action” report.

Confirm that employees chose a
home broadband solution that includes
regular firmware updates to patch any
new vulnerabilities.

Consider updating policies; at the very
least, remind users about your AUP
and their responsibilities.

Consider putting systems like MDM or
endpoint protection in place to block
the use of public Wi-Fi entirely.

Implement MTD to monitor and mitigate
the risk of MitM attack.

Consider using a cloud access security
broker (CASB) or secure web gateway
(SWG) to help secure all connections to
cloud-based systems.

MSI 2022  Threats and defenses
MSI 2021  Foreword

54
54

Zero Trust

4

Zero Trust network access (ZTNA) is an approach
to network security that assumes every device,
application or system that connects to your
network potentially could be compromised.
It involves granting authorized users access only
to the applications they need to perform their
jobs. It also isolates specific applications, devices
and systems to certain parts of the network and
doesn’t make the internal network visible to the
internet, which could otherwise make it easier for
hackers to infiltrate.

Zero Trust network
access

ZTNA can be an effective alternative to the traditional approach to network security,
which typically involves using a VPN to connect workers from remote locations and
implicitly trusting these connections.

A Zero Trust security approach can bolster endpoint, network and remote
work security by minimizing the company’s exposure. With this model, dozens
or potentially hundreds of devices, applications and users would not have
wide-ranging access to the company’s network or sensitive data—they could
only access the systems and information to which they are authorized.

Though ZTNA can strengthen a company’s security policy and make it more
resilient, it’s also important to balance this approach with delivering a user-friendly
digital experience that helps remote employees remain productive. If employees
can’t easily access the applications and systems they need to do their work, they
may not be as productive.

It’s a delicate balance, but you can deliver a frictionless remote work experience
while also helping to keep the organization secure. For example, intelligent,
analytics-driven identity access management solutions can automate the process
of determining when to grant a specific user access to certain applications. AI-
driven threat detection solutions can also help your organization detect anomalies
or suspicious user behavior and network activity and isolate these threats before a
breach occurs. This way, employees don’t have to deal with onerous authentication
requirements; they aren’t unintentionally blocked from accessing the systems they
need to do their jobs and also aren’t given unauthorized access to sensitive data.

As companies embrace remote and hybrid work, a ZTNA model can help combat
security threats while giving employees the flexibility to work from anywhere and
on any device they choose—whether it’s their desktop, tablet or phone. With an
approach focused on verification rather than implicit trust, companies can establish
a strong security perimeter, deliver a better employee experience and remain agile
in the increasingly complex threat environment as they adapt to the future of work.

82%

A large majority of respondents
said that they had adopted or
were actively considering
adopting a Zero Trust
approach to security.

MSI 2022  Zero Trust

56

A continuous
Zero Trust mindset

The White House’s executive order (EO) highlights many specific areas of interest
for not only federal government security, but how we should be thinking about
security and network architecture everywhere.57

As the EO notes: “To keep pace with today’s dynamic and increasingly sophisticated
cyber threat environment, the Federal Government must take decisive steps to
modernize its approach to cybersecurity, including by increasing the Federal
Government’s visibility into threats, while protecting privacy and civil liberties.”

According to the EO, agency heads are required to update existing agency plans,
develop a plan to implement Zero Trust Architecture based on current NIST migration
steps, and report on progress—within 60 days of the order. This is powerful, not
least because it helps bring Zero Trust back down to earth from how over-marketed
the term has become in recent years. It helpfully frames Zero Trust in architecture
terms—something Netskope has also underscored and that we’re seeing as common
to the success of our many customers worldwide.

In a modern architecture, Zero Trust principles should be judiciously applied, adaptively
and continuously. But today, many organizations don’t have much more than isolated
“Zero Trust projects” focused on networks, users, devices or isolating servers. The
main miss on most of these projects is that they are focused on application-level
access and other pieces, but not focused on the data. Architecturally, we must go
beyond access control and isolation to provide continuous Zero Trust: real-time
access and policy controls that adapt on an ongoing basis based on users, devices,
apps, threats and data context.

This data-centric approach is the only effective way to dynamically manage risk
across a mix of third-party applications and a remote-first workforce that needs
always-on access to cloud apps and data to stay productive. As the EO calls out in
Section 10, item K:

“Zero Trust Architecture embeds comprehensive security monitoring; granular
risk-based access controls; and system security automation in a coordinated manner
throughout all aspects of the infrastructure in order to focus on protecting data in
real-time within a dynamic threat environment. This data-centric security model
allows the concept of least-privileged access to be applied for every access decision,
where the answers to the questions of who, what, when, where, and how are critical
for appropriately allowing or denying access to resources…”

Proper application of Zero Trust principles is also a critical step toward Secure
Access Service Edge (SASE) architecture. SASE isn’t specifically mentioned in the
EO, but as the order explains, applying Zero Trust at an architectural level means
“a set of system design principles, and a coordinated cybersecurity and system
management strategy based on an acknowledgment that threats exist both inside
and outside traditional network boundaries.” In other words—and crucial to SASE—
yesterday’s security and network technologies and designs won’t even start to
address the prevalence of cloud-delivered threats or attacker abuse of cloud
apps, or the increasingly acute need for security and networking teams to more
effectively converge and collaborate.

Sanjay Beri
Founder and CEO
Netskope

47%

Nearly half of respondents
that experienced a mobile-
related compromise said that
cloud-based systems/apps
were compromised as
a consequence.

57   The White House, Executive Order on Improving the Nation’s Cybersecurity, 2021

MSI 2022  Zero Trust
MSI 2021  Foreword

57
57

Conclusion

While preparing this report, at the end of each interview, we asked the same
question: Are you optimistic or pessimistic about the future of mobile device
security? Without exception, every one of the experts said that they were optimistic.
When we asked them why, they had a variety of reasons. Some cited the growing
awareness of the issue among business leaders; others talked about the advances
in technology, including the introduction of AI; some talked about improved
regulation and industry standards.

It’s been said that sunlight is the best disinfectant.58 As cybersecurity becomes
more high-profile, it is receiving more attention from consumers, business leaders
and legislators. This increased attention is driving companies to take the issue
more seriously and legislators to improve guidance for organizations. In the past,
many cybersecurity regulations were criticized for being too “outcome-based” and
offering little clear guidance. Our panel of experts said that they see that changing.

But having rules and tools in place is only part of the story. Our experts weren’t
surprised to hear that over half of respondents had said that they’d sacrificed
mobile device security. And when we asked them for a single piece of advice for
our readers, the majority of them said that they wished more companies used
all the tools that they were paying for.

Based on our experts’ advice, we have strived to pack this report with lots
of practical advice. We hope that you find it useful and that it helps you to
educate your employees, inform your leadership and get more out of your
cybersecurity investments.

We too are optimistic about the future of cybersecurity, because people like
you got through a whole 58 pages.

You didn’t cheat and skip to the last page did you?

64%

Nearly two-thirds of
respondents said that public
awareness of cybersecurity
risks will increase in the future.

66%

Nearly two-thirds of
respondents said that they’d
come under pressure to
sacrifice mobile-device
security “to get the job done.”
And 79% of those (52% of all
respondents) had succumbed
to that pressure.

58   Louis Brandeis, Other People’s Money, 1914

MSI 2022  Appendices

58

Appendices

5

In compiling this report, we interviewed a number of leading
security experts among our contributors. Talking with these highly
experienced security professionals was fascinating and really
helped us to shape this report. We are really grateful to them for
their time.

Terminology used
in this report

Organization
descriptions

Throughout this report, when we
refer to companies, businesses or
organizations, we include both public-
and private-sector entities of all sizes.
We use the term “enterprise” to refer
to organizations with 500 or more
employees, and “small and medium-
sized businesses (SMBs)” for those
with fewer.

Security terms

Security terms like “attack” and “breach” are often used interchangeably.
For clarity and precision, we have used the following definitions
throughout this report:

Attack
A general term covering any deliberate action toward a system or
data that is unauthorized. This may be as simple as attempting to
access it without permission.

Compromise
A successful attack that results in a system’s defenses being
rendered ineffective. This could involve data loss, downtime, other
systems being affected or no detrimental effects at all. It could be
malicious or accidental.

Data breach
An incident that results in the confirmed disclosure—not just
potential exposure—of data to an unauthorized party.

Exploit
A definition, often in the form of a script or code, of a method
to successfully leverage one or more vulnerabilities to access a
system without proper authorization.

Incident
This covers any form of security event, malicious or not, successful
or not. This could be anything from a failed authentication attempt
to a successful compromise and data breach. It includes non-
malicious events, such as the loss of a device.

Risk
A measure of the likelihood of a threat, an organization’s
vulnerability to said event and the scale of the potential damage.

Threat
Any danger that could impact the security of systems or privacy of
data. This can apply to a technique, such as phishing, or an actor,
such as an organized criminal group.

Vulnerability
A weakness that could be exploited. It may be known or unknown—
to the manufacturer, developer, owner or the world.

MSI 2022  Appendices

60

Survey
methodology

We contracted an independent research company to survey senior professionals
responsible for the procurement, management and security of mobile devices.

In total, 632 professionals responsible for the buying, managing and security of
these devices responded. The charts below break down the demographics of these
respondents. Our sample included both small companies and large enterprises.

Company size was not a strong indicator for most of our questions. Unless stated
otherwise, all data in this report is from this survey.

Unless stated otherwise, stats quoted in this report are from this survey.

Respondents by country

Respondents by company size

Respondents by company operations

Australia

6%

U.K.

14%

10,000 or more

5,000 — 9,999

5%

10%

Global (operations across
multiple countries across
multiple continents)

17%

11%

2,500 – 4,999

47%

34%

Regional

80%

25%

27%

U.S.

500 – 2,499

50 – 499

24%

Local

Multinational
(operations in at least
one other country)

Data from contributions
Details of the source of data and statistics supplied by our contributors are given in
the next section.

MSI 2022  Appendices

61

Contributors

Absolute
Maintain secure remote access, without sacrificing on experience. Kick off or
continue your journey to SASE with a cloud-first security platform that improves
the remote working experience. NetMotion by Absolute provides optimized
remote access with a Zero Trust security posture alongside context-aware policy
enforcement for all endpoints on any network. It also enables complete visibility
of remote devices and the employee experience.

absolute.com

Check Point
Check Point is a leading provider of cybersecurity solutions to governments and
corporate enterprises globally. Its solutions protect customers from fifth-generation
cyberattacks with a leading catch rate of malware, ransomware and other types
of attacks. Check Point offers multilevel security architecture, “Infinity” Total
Protection with Gen-V advanced threat prevention, which defends enterprises’ cloud-,
network- and mobile device-held information. Check Point provides one of the most
comprehensive and intuitive “one point of control” security management systems.
Check Point protects over 100,000 organizations of all sizes.

checkpoint.com

IBM
IBM Security MaaS360 with Watson transforms how IT is securing smartphones,
tablets, laptops, desktops, wearables and IoT without sacrificing a great user
experience. AI and predictive analytics keep you alerted to potential endpoint threats
and provide remediation to avoid security breaches and disruptions. MaaS360
protects apps, content and data so organizations can rapidly scale their remote
workforce and BYOD initiatives.

The MaaS360 Mobile Metrics feature offers cloud-sourced benchmarking data and
best practices to enhance productivity and improve security. Benchmarking data is
generated by leveraging multiple data values from MaaS360 client implementations
to build aggregated metrics.

ibm.com/security/mobile/maas360

MSI 2022  Appendices

62

Ivanti
Ivanti makes the Everywhere Workplace possible. In the Everywhere Workplace,
employees use myriad devices to access IT applications and data over various
networks to stay productive as they work from anywhere. The Ivanti Neurons
automation platform connects the company’s unified endpoint management, Zero
Trust security and enterprise service management solutions, providing a unified IT
platform that enables devices to self-heal and self-secure and also empowers users
to self-service. Over 40,000 customers, including 96 of the Fortune 100, have
chosen Ivanti to discover, manage, secure and service their IT assets from cloud
to edge, and deliver excellent end-user experiences for employees, wherever and
however they work.

ivanti.com

Jamf
Jamf’s purpose is to simplify work by helping organizations manage and secure
an Apple experience that end users love and organizations trust. Jamf is one of
the only companies in the world that provides complete management and security
solutions for an Apple-first environment that is enterprise secure, consumer simple
and protects personal privacy. Today, more than 62,000 customers rely on Jamf to
manage and secure more than 27 million devices worldwide.

jamf.com

Lookout
Lookout is a leading provider of endpoint and cloud security solutions. Our
mission is to secure and empower our digital future in a privacy-focused world
where mobility and cloud are essential to all we do for work and play. We enable
consumers and employees to protect their data, and to securely stay connected
without violating their privacy and trust. Lookout is trusted by millions of consumers,
the largest enterprises and government agencies, and various partners across
telecommunications and technology.

Powered by one of the largest data sets of mobile code in existence, the Lookout
Security Graph provides visibility into the entire spectrum of mobile risk. The
installed base of Lookout’s personal and enterprise mobile endpoint products is
over 205 million mobile devices worldwide. This acts as a global sensor network
that provides visibility into the threat landscape, including over 170 million apps—
and that’s growing by up to 90,000 apps a day

lookout.com

MSI 2022  Appendices

63

Netskope
Netskope safely and quickly connects users directly to the internet, any application,
and their infrastructure from any device, on or off the network. With CASB, SWG,
and ZTNA built natively in a single platform, the Netskope Security Cloud provides
the most granular context, via patented technology, to enable conditional access
and user awareness while enforcing Zero Trust principles across data protection
and threat prevention everywhere. Netskope’s global security private cloud provides
full compute capabilities at the edge.

Netskope’s Security Cloud protects 25% of Fortune 100 companies, including:

•  Three of the world’s six largest airlines

•  Three of the world’s four largest banks

•  Five of the world’s seven largest healthcare providers

•  Two of the world’s largest telecommunications companies

Netskope is fast everywhere, data-centric and cloud-smart, all while enabling good
digital citizenship and providing a lower total cost of ownership.

netskope.com

Proofpoint
Proofpoint, Inc., is a leading cybersecurity company that protects organizations’
greatest assets and biggest risks: their people. With an integrated suite of cloud-
based solutions, Proofpoint helps companies around the world stop targeted
threats, safeguard their data and make their users more resilient against
cyberattacks. Leading organizations of all sizes, including more than half of the
Fortune 1000, rely on Proofpoint for people-centric security and compliance
solutions that mitigate their most critical risks across email, the cloud, social
media and the web.

proofpoint.com

Thales
Thales is a global high-technology leader investing in digital and “deep tech”
innovations—connectivity, big data, artificial intelligence, cybersecurity and quantum
technology—to build a future we can all trust, which is vital to the development of
our societies. The company provides solutions, services and products that help
its customers—businesses, organizations and states—in the defense, aeronautics,
space, transportation, and digital identity and security markets to fulfill their critical
missions, by placing humans at the heart of the decision-making process.

thalesgroup.com

MSI 2022  Appendices

64

65