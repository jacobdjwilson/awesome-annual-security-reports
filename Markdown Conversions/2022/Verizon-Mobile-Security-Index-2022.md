# MSI Mobile Security Index 2022

## Table of Contents
- [Who should read this report?](#who-should-read-this-report)
- [About this report](#about-this-report)
- [Foreword](#foreword)
- [Introduction](#introduction)
- [Mobile is now critical.](#mobile-is-now-critical)
- [Everywhere, all the time](#everywhere-all-the-time)
- [Success brings unwanted attention.](#success-brings-unwanted-attention)
- [The severity of attacks has grown.](#the-severity-of-attacks-has-grown)
- [Security spend](#security-spend)
- [Bring your own dangers.](#bring-your-own-dangers)
- [Bring your own office.](#bring-your-own-office)
- [Bring your own device (BYOD).](#bring-your-own-device-byod)
- [Bring your own applications.](#bring-your-own-applications)
- [How to secure BYOD devices](#how-to-secure-byod-devices)
- [Training and acceptable use polices](#training-and-acceptable-use-policies)
- [How to work from home, securely](#how-to-work-from-home-securely)
- [Threats and defenses](#threats-and-defenses)
- [Users and behaviors](#users-and-behaviors)
- [Passwords](#passwords)
- [Phishing](#phishing)
- [Inappropriate content](#inappropriate-content)
- [The great exfiltrations](#the-great-exfiltrations)
- [How to secure against phishing](#how-to-secure-against-phishing)
- [How to create an effective incident reporting process](#how-to-create-an-effective-incident-reporting-process)
- [Apps](#apps)
- [App permissions](#app-permissions)
- [Malware](#malware)
- [Ransomware](#ransomware)
- [Mobile ransomware](#mobile-ransomware)
- [How to secure apps](#how-to-secure-apps)
- [Devices and things](#devices-and-things)
- [Lost or stolen devices](#lost-or-stolen-devices)
- [Device management](#device-management)
- [Check Point: The case for UEM](#check-point-the-case-for-uem)
- [The dangers of things](#the-dangers-of-things)
- [How to secure IoT devices](#how-to-secure-iot-devices)
- [Networks and clouds](#networks-and-clouds)
- [Public Wi-Fi](#public-wi-fi)
- [Home Wi-Fi](#home-wi-fi)
- [How to secure networks](#how-to-secure-networks)
- [Zero Trust](#zero-trust)
- [Zero Trust network access](#zero-trust-network-access)
- [A continuous Zero Trust mindset](#a-continuous-zero-trust-mindset)
- [Conclusion](#conclusion)
- [Appendices](#appendices)
- [Terminology used in this report](#terminology-used-in-this-report)
- [Survey methodology](#survey-methodology)
- [Contributors](#contributors)

Who should read this report?
We produced this fifth annual Verizon Mobile Security Index to help security 
professionals, like chief information security officers (CISOs), assess their 
organization’s mobile security environment and calibrate their defenses. While 
the report is packed with detail, there’s also lots of information that would be 
interesting—and extremely relevant—to anybody involved in the specification, 
procurement or management of IT devices and services.

About this report
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

# Foreword
Executive summary

In 2021, the FBI’s Internet Crime Complaint Center (IC3) team received a record 
847,376 complaints—a 7% increase from 2020. The estimated potential losses 
were over $6.9 billion.[^1] Unsurprisingly, ransomware, business email compromise 
(BEC) and the criminal use of cryptocurrency were among the most commonly 
reported types of incident.
In 2021, America experienced an unprecedented increase in cyberattacks and 
malicious cyber activity. Normally, the legal team would never let us say something 
as bold as that; they’d want evidence for such a dramatic statement. But those 
words are verbatim from the opening of the FBI’s 2021 Internet Crime Report.[^1]
And our research found that compromises that were known to involve a mobile 
device followed this trend—in fact, the growth in the number of companies 
affected was higher.

[^1]: FBI, 2021 Internet Crime Report, 2021

Attacks are 
up—losses too.
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
45%

![Figure 1. QAPNW Percentage of respondents that admitted their company suffered a compromise which involved a mobile device and led to the loss of data or downtime. [n=601, 671, 876, 856, 632]]

Figure 1. Percentage of respondents that admitted their company suffered a compromise that 
involved a mobile device and led to the loss of data or downtime. 
[n=601, 671, 876, 856, 632]

Changing working practices are a challenge.
According to a survey by Proofpoint, 64% of people have changed where they 
work. Changes driven by the pandemic have stuck. Sixty-eight percent of those 
surveyed have started working from home either full time or some of the time.[^2]
IT organizations did a stellar job enabling millions of people to work from home 
on short notice. New security approaches and tools mean that employees 
working from home can be just as secure as those working from the office. 
And managing a mix of remote, home, hybrid and office-based employees 
doesn’t need to be any more difficult either.
But companies are still struggling. Almost four-fifths of respondents agreed 
that recent changes to working practices had adversely affected their 
organization’s cybersecurity.

[^2]: Proofpoint, 2022 State of the Phish, 2022

79%
22%
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
posture.[^3]

[^3]: Absolute, The Future of Work, 2022

Almost two in three CISOs across all regions agree that remote working makes 
their organization more vulnerable to cyberattack.

Companies are more reliant on mobile devices. 
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
58%
59%
53%
Many employees now have access to much of the same data—customer lists, 
banking details, employees’ personal data, billing information, etc.—and systems—
messaging, enterprise resource planning (ERP), etc.—via their mobile devices as 
they would sitting at a desktop in the office. This means that the compromise of a 
mobile device can now pose a significant risk to customer data, intellectual property 
and core systems.
13%
Only one in eight respondents 
said they had few (less than 
10% of their workforce) 
people working from home 
or following a hybrid 
working model.

![Figure TTIBF. Year-over-year change in security spend. [n=632]]

Figure 2. Year-over-year change in security spend. [n=632]

![Figure REMOG: Factors that respondents said drove the increase in security spend that they have seen in the preceding 12 months. [n=626]]

Figure 3. Factors that respondents said drove the increase in security spend that they had 
seen in the preceding 12 months. [n=626]

Security spend is rising in response.
Over three-quarters (77%) of respondents said that their security spend 
had increased in the preceding year. More than a fifth said that it had 
increased significantly.

# Introduction
Whereas traditionally technology got a foothold in the enterprise 
and then trickled down to consumers, it was consumers that 
drove the growth of what we then called smartphones. Fifteen 
years ago, around when the first edition of the Verizon Data 
Breach Investigations Report (DBIR) was being written, most 
home computers were large boxes with separate monitors and 
keyboards. These devices were pretty rudimentary compared with 
what we’re used to today, but at the time they were game changing. 
Now you could have a device in your pocket that enables you to 
access the web, send and receive emails, and more. 

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

Mobile is now critical.
When asked how critical, on a ten-point scale, mobile devices were to the smooth 
running of their organization, 91% of respondents in our survey answered seven or 
above—and 78% answered eight or higher. The picture was very similar regardless 
of company operations (local, regional or global) and company size (small, medium 
or enterprise size). The difference was no more than two percentage points up 
or down.

![Figure WRTTQ. Responses to the question “How critical are mobile devices to the smooth running of your organization?” [n=632]]

Figure 4. Responses to the question “How critical are mobile devices to the smooth running of 
your organization?” [n=632]

The vast majority of 
respondents said that flexibility 
in where they work and what 
devices they can use will be 
important to attracting the 
best new talent.

![Figure MLDMA: What proportion of your organization’s staff work from each of these locations most (80% or more) of the time? [n=632]]

Figure 5. What proportion of your 
organization’s staff work from each of these 
locations most (80% or more) of the time? 
[n=632]

Everywhere, all the time
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
passed a law giving workers the right to disconnect.[^4] Since then, Ireland, Italy 
and Spain have enacted similar legislation. The province of Ontario is considering 
enacting a similar law.

[^4]: Légifrance, Partie législative (Articles L1 à L8331-1), 2017

![Figure FCOLS: Reasons why employees feel unable to “disconnect” from work.]

Figure 6. Reasons why employees feel unable to “disconnect” from work.[^5]

[^5]: LifeWorks, The Mental Health Index by LifeWorks, 2022

![Figure 7. Extract from Working for Workers Act, 2021 in the Legislative Assembly of Ontario.]

Figure 7. Extract from Working for 
Workers Act, 2021 in the Legislative 
Assembly of Ontario.[^6]

[^6]: Legislative Assembly of Ontario, Bill 27, Working for Workers Act, 2021, 2021

Working excessive hours can affect mental health. LifeWorks found that the 21% of 
workers who disagreed with the statement “I am typically able to disconnect from 
work after usual work hours” had a Mental Health Index score 4.8 points lower than 
those that were able to switch off.[^7]

[^7]: LifeWorks, The Mental Health Index by LifeWorks, 2022

![Figure JHSNI: Global Mental Health Index score by month, LifeworksLFEWRX]

Figure 8. Global Mental Health Index score by month.[^8]

[^8]: LifeWorks, The Mental Health Index by LifeWorks, 2022

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
What do you do?
- Hover over the button and check the actual URL in the 
status bar
- Expand the message header and check the 
sender’s address
- Close the email and decide to review later
- Flag the email as spam/suspicious
- Click the button

It’s late. You’ve been out for the evening and had a 
couple of beers. You’re in a cab on your way home 
when your phone buzzes in your pocket. You tap on the 
notification and the email opens up.
You’ve just taken a training course about phishing, so 
you’re a bit suspicious. But the email includes some 
personal information, looks professional and has no 
obvious giveaways like bad grammar.
What do you do?
- Close the email and decide to review later
- Flag the email as spam/suspicious
- Click the button

Now that mobile is so critical to business operations, it’s getting more attention 
from bad actors too. From coordinated state-sponsored campaigns to unfocused, 
opportunistic criminal exploits, the volume of attacks is going up. Whether the 
attacker is a well-trained and well-resourced professional or an amateur taking 
advantage of the many commercially available exploits, mobile devices are an 
attractive target.  

Success brings 
unwanted attention.

![Figure FFPLC: Reported incidents and losses, based on FBI data.]

Figure 9. Reported incidents and losses, based on FBI data.[^9]

[^9]: FBI, 2021 Internet Crime Report, 2021

Despite this, we still get respondents saying that mobile devices are of less interest 
to cybercriminals than other IT assets—36% in our latest survey, up from 30% in our 
2021 report.

The severity of attacks has grown.
As mentioned earlier, 45% of respondents said that their organization had been 
subject to a security incident involving a mobile device that led to data loss, 
downtime or other negative outcome.
Of those respondents, 73% described the impact of the attack as major, and over 
two-fifths (42%) said that it had lasting repercussions. That’s up from our previous 
report, where less than half of incidents were described as major, and just 28% 
were said to have had lasting repercussions.

![Figure DPEMS: Prevalence and severity of mobile-related compromises. [n=601, 671, 876, 856, 632].]

Figure 10. Prevalence and severity of mobile-related compromises. [n=601, 671, 876, 856, 632]

However, the 2021 data was a bit of an anomaly—wonder why? This year’s 
severity figures show a return to the level we’ve seen since we started 
producing the Mobile Security Index, just a little higher. Of course, with 
a lot more respondents saying that their company had experienced a 
mobile-related compromise, this means a lot more companies are facing 
major, and lasting, consequences. 

Over three-quarters of 
respondents said that their 
cybersecurity budget had 
increased in the previous 
12 months.
Over two-thirds said that 
spend had increased in the 
previous 12 months and they 
expected it to rise again in the 
next 12 months.
Over three-quarters of 
respondents said that they 
expect their cybersecurity 
budget to increase in the 
coming 12 months.
77%
77%
67%

Security spend
These factors help explain why 
77% of respondents said that their 
cybersecurity budget had increased 
in the previous 12 months—that’s 
up from 65% in the previous edition 
of this report—and close to a third 
(29%) of those said it had increased 
significantly.

And respondents expect their budgets 
to grow again. Over three-quarters 
said that they expected their budget 
to grow in the following 12 months; 
25% said they expected it to increase 
significantly. Just 1% expected their 
budget to decrease.

Of course, growing budgets sounds like good news for CISOs, but what really 
matters is whether that budget is sufficient to meet needs—especially when needs 
are growing as we’ve discussed.
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

![Figure GKZPW: Objectives for cybersecurity spend.]

Figure 11. Objectives for cybersecurity spend. [n=632]

![Figure JHUQM: Respondents estimated breakdown of security spend by NIST category. [n=632]]

Figure 12. Respondents’ estimated 
breakdown of security spend by NIST 
category. [n=226]

According to a report by 
Thales, two-fifths of 
organizations are not confident 
that their current security 
systems could effectively 
secure remote work.[^10]
The vast majority of companies 
said that they have a defined 
budget for mobile security.
67%
40%
85%

[^10]: Thales, 2022 Thales Data Threat Report, 2022

# Bring your own dangers.
Working patterns were changing long before 
we all learned what a coronavirus is. But the 
COVID-19 crisis catalyzed dramatic changes in 
expectations, for both employers and employees. 
These new behaviors have brought new 
challenges and threats with them.

Bring your 
own office.
Challenges to managing 
risk and compliance
How many times have you seen a “look what I just received” post on LinkedIn? 
Somebody has just started a new job and received a new laptop, monitor and bunch 
of logo’d swag—typically including a water bottle and a mousepad. That’s what 
onboarding has looked like for a lot of people over the last couple of years.
As working from home has become more commonplace, people have invested in 
building a more comfortable place to work. There’s been a boom in loft and garage 
conversions, or if you’re really lucky maybe you splashed out on a “shed quarters” 
at the bottom of the garden.
Many of you reading this report will be seasoned remote workers. But recent 
events have created millions of new home and hybrid workers. Despite this, many 
companies haven’t provided employees with clear guidance on what’s expected.

Over half of CISOs across all regions agree that targeted attacks on 
their organizations have increased since adopting mass hybrid working. 
Small organizations seem more affected, with 59% of companies with 
500 or fewer employees saying their workforce has been targeted more 
since they implemented hybrid working. At the other end of the scale, 
only 48% of enterprises (5,000 employees and above) agree.[^11]

[^11]: Proofpoint, 2022 Voice of the CISO, 2022

![Figure 13. Challenges to managing risk and compliance. Data from Absolute.]

Figure 13. Challenges to managing risk 
and compliance. Data from Absolute.[^12]

[^12]: Absolute, The Future of Work, 2022

According to Thales, nearly 
four in five organizations 
are still “somewhat” or 
“very concerned” about the 
security risks and threats 
that a greatly increased 
remote workforce poses.[^13]
79%

[^13]: Thales, 2022 Thales Data Threat Report, 2022

Bring your own 
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

Bring your own 
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

![Figure 14. BYOD policies, current and under consideration. [n=623]]

Figure 14. BYOD policies, current and under 
consideration. [n=623]

How to secure 
BYOD devices
NIST
Framework
R
e
c
o
v
e
r
 
I
d
e
n
t
i
f
y
 
P
r
o
t
e
c
t
D
e
t
e
c
t
R
e
s
p
o
n
d
**Identify**
- Develop a detailed BYOD policy that 
clearly lists responsibilities in plain 
language—this may involve translating it 
into local languages.
**Protect**
- Educate users on the importance of 
managing the permissions granted to 
apps—users often aren’t aware of how 
some permissions can be exploited for 
nefarious purposes.
- Implement an MDM solution to help 
remotely secure, manage and support 
personally owned devices.
- Consider restricting what resources 
devices not controlled by the company 
can access.
- Ensure that users understand the 
importance of keeping the operating 
system (OS) and apps up to date.
- Educate users on the dangers of 
malware and how to reduce the 
risks—malware can obviate protections 
like containerization.
- Consider implementing a Zero Trust 
approach; this can reduce the reliance 
on end users making informed and 
security-conscious decisions—see 
page 56 for more details.
**Detect**
- Consider introducing endpoint 
detection and response (EDR); this 
uses behavioral-based analysis to 
provide threat protection and can 
provide valuable insight. 
- Consider implementing data loss 
prevention (DLP) to detect and block 
the exfiltration of information.
- Give users an authorized—and easy-to-
use—means to share files outside 
the company. 
**Respond**
- Make sure that your team has the 
training—or the third-party support—to 
handle greater device variety.
- Make sure that staff know what to do if 
a device is lost or stolen, or they spot 
something suspicious—this should be 
part of your general security policy, but 
it’s worth reiterating here. 
- Make reporting concerns easy—it 
shouldn’t be something people have to 
look up—and remember, the employee 
might not be able to access company 
systems when reporting an issue.
**Recover**
- Use mobile threat defense (MTD) 
combined with unified endpoint 
management (UEM) to help bring 
devices that are out of compliance back 
into line through self-remediation.
- Develop a clear policy, in consultation 
with your legal team, that covers the 
tricky issues around performing 
digital forensics on an employee-
owned device.  

These recommendations are structured 
around the five functions in the 
NIST Cybersecurity Framework. 
To find out more, 
visit nist.gov/cyberframework

![Work profiles]

Work profiles

Training and acceptable 
use policies
Lack of clarity on expectations
Some behavior is clearly unacceptable, such as accessing adult, extreme or illegal 
content on company devices. This could not only damage your organization’s 
reputation, this type of behavior could put your company at risk. But there are many 
gray areas in defining appropriate use, especially when it comes to mobile devices. 
What if employees want to use their work devices to check personal emails, stream 
music or scroll through social media? Many people think this is a reasonable 
allowance in a flexible, modern workplace.
Part of the problem is that many companies struggle to develop an effective 
acceptable use policy (AUP)—48% didn’t have one at all, an improvement from 57% 
in our last report. Defining what counts as misuse of a work device can be tricky, 
especially if your employees need to access social media and other content to do 
their jobs, but creating clear guidance, including rules for mobile-specific content, 
is crucial for helping prevent misuse.
Plus, with many employees now working from home, the lines are blurred 
even further.

![Figure 15. Personal tasks carried out on work devices, by user and user’s friends/family. Data from Proofpoint.]

Figure 15. Personal tasks carried out on work devices, by user and user’s friends/family. 
Data from Proofpoint.[^14]

[^14]: Proofpoint, 2022 State of the Phish, 2022

Nearly four-fifths (79%) of 
people admitted to using a 
work device for a personal 
task, such as checking 
personal email, shopping 
or streaming.[^15]
Nearly half of respondents 
said their organization didn’t 
have an acceptable use policy 
in place.
79%
48%

[^15]: Proofpoint, 2022 State of the Phish, 2022

It’s not our place to say how companies should manage abuse, but we advocate 
creating a positive security culture. Creating a blame-free environment is likely to 
encourage employees to report suspicious activity and mistakes that they may 
make—enabling the organization to mitigate the damage.

Lack of training
Many companies set high expectations on their employees but don’t give them 
sufficient training to meet those standards. 
Lack of remote working guidance
We’ve seen a massive shift in working practices—even if only temporary for some 
people—yet less than half of companies said that they have given employees 
training on how that affects cybersecurity. 

How to work from 
home, securely
A guide for users
**Reduce risky behavior.**
- Read and understand your company’s 
policies. Ask for further guidance on 
anything you’re unsure about. 
- Try to keep your private and work life 
separate.
- Consider where you keep work devices 
and any sensitive data—are these stored 
safely when not in use?
- Make sure that you’ve set a password 
or PIN—or enabled Touch ID where 
applicable—for access.
- Configure your devices to lock 
automatically after a few minutes 
of inactivity.
- Create a unique strong password 
for each account, including email and 
web applications
- Turn on two-factor authentication 
wherever possible.
- Think about who can see or hear what 
you are saying or typing on your screen.
- Sign up to newsletters from trusted 
organizations to improve your 
cybersecurity skills and knowledge.
**Manage your apps.**
- Be careful what apps you install on your 
devices, especially when those devices 
have access to corporate resources.
- Make sure you understand your 
company’s AUP and any other 
restrictions that may be in place.
- Install updates promptly—it can be a 
bother, but failing to do so could put 
your device, and the company, at risk.
- Be frugal with which permissions you 
give apps. Consult company policies on 
what to limit on which apps.
**Secure your devices.**
- Don’t share devices—you may be 
allowed to perform personal tasks, 
but that doesn’t apply to your friends 
and family.
- As with apps, install OS updates when 
asked to do so.
- If you lose a device, or it gets stolen—
these things happen—report it 
immediately.
**Be smart about 
networks.**
- Change the default password on your 
home router—and any smart home 
devices connected to it.
- Set up separate Wi-Fi networks for 
smart home devices, visitors and 
work use—many wireless access 
points include this functionality in 
the admin console.
- If your company provides a VPN, use it.
- Be wary of public Wi-Fi networks—even 
ones associated with brands you know 
and trust.

# Threats 
and defenses

The human element continues to drive breaches. Over 
four-fifths (82%) of breaches analyzed for the 2022 DBIR 
involved the human element. Whether it is the use of stolen 
credentials, phishing, misuse or simply an error, people 
continue to play a very large role in incidents and 
breaches alike.[^16]

[^16]: Verizon, Data Breach Investigations Report, 2022

3.1 Users 
