RAN SO MWARE
DE FE NSE
RE PORT

TABLE OF CONTENTS

Introduction

Why We Do This Survey

Key Findings

The Shifting Ransomware Trends

On the Positive Side, We Saw Fewer Organizations Affected...

...But the Impact Remains Immense for Entire Organizations

The Cost Is Climbing, Too

A False Sense of Conﬁdence

Ransomware Is More than a SecOps Problem

Where SecOps and BizOps Collide

Battling Ransomware on Multiple Fronts

Countermeasures Misaligned with New Ransomware Tactics

Future Defense Priorities Show Some Disconnect

All Eyes on Prevention and Automation

Adapting Ransomware Defenses for Stealthier Attacks

Final Thoughts

About SpyCloud

3

4

8

10

10

11

12

13

15

16

17

18

21

23

24

26

27

INTRODUCTION

For the last several years, we’ve watched our workplaces digitally transform, 

making the convenience of working and collaborating from anywhere the rule rather 

than an exception. Many organizations have welcomed this new reality, but they’ve 

struggled to keep their security defenses in step with the fast pace of digital growth 

and an expanding attack surface.

Cybercriminals, however, haven’t had any problem staying current with a digital\- 

ﬁrst, cloud\-ﬁrst environment. As they quickly pivot to next\-generation tactics for 

exﬁltrating data and access, security operations (SecOps) teams are falling farther 

behind – while exposure to cyberattacks like ransomware is at an all\-time high.

Some Background Before You Dig In

After the release of our last Ransomware Defense Report in September 2022, 

ransomware attacks showed some promising signs of slowing down. Criminals 

tested other tactics and government agencies cracked down, with the number of 

attacks leveling off by the end of year. But that glimmer of hope ﬁzzled quickly, 

with attackers picking up the pace so fast in 2023 that we’re headed toward the 

Last year, we found 

that organizations were 

losing ground and felt 

less conﬁdent about 

their defenses than 

before. This year’s 

Ransomware Defense 

Report examines how 

security frontline and 

leadership perceptions, 

practices, and priorities 

second\-most costly year for ransomware in history. 

have changed since 

then, and how SecOps 

teams are doing in

their ﬁght against 

ransomware. 

Even through that ebb\-and\-flow, the sophistication and impact of ransomware 

attacks has grown. At least one new ransomware group with double\-extortion 

abilities surfaced every month last year, while the average cost of a ransomware 

attack escalated to $5\.13 million – surpassing the average cost of a data breach.

And one thing hasn’t changed: ransomware is one of the toughest cybersecurity 

challenges organizations of all sizes and industries continue to face. In SpyCloud’s 

2023 Malware and Readiness Defense Report, security leaders and practitioners 

ranked ransomware as the top threat to their organization’s security. 

3WHAT TO EXPECT INTHIS YEAR’S REPORTWHY WE DO THIS SURVEY

As we note in our findings, ransomware defenses are not keeping pace with cybercriminals. We do this survey to shine 

a light on one of the contributing causes: an emerging threat that could be an early warning sign of a ransomware event – 

information\-stealing malware, or infostealers. 

Criminals are using infostealers to siphon authentication data – including logs with information that enable access to 

enterprise networks and applications – and selling the data to ransomware operators. And through a deep analysis of 

recaptured infostealer logs, we’ve uncovered that the presence of infostealer malware is related to the likelihood that a 

company will experience a ransomware event in the near future.

THE INFOSTEALER\-RANSOMWARE CONNECTION, BROKEN DOWN

SpyCloud researchers conducted a detailed analysis using ransomware event data from ecrime.ch and our own 

database of recaptured records from the criminal underground. Of 2,613 North American and European 

companies victimized by ransomware in 2023, 30% had at least one infostealer infection prior to being attacked.

Our analysis also showed that the presence of speciﬁc infostealer infections – Raccoon, Vidar, and Redline – 

increases the probability that a company will experience a ransomware event.

THE MOST PREVALENT INFOSTEALER FAMILIES ASSOCIATED WITH RANSOMWARE 

VICTIM COMPANIES

Companies with Raccoon, Vidar, and Redline infostealers experienced a ransomware

event within an average of 16 weeks post\-infection.

\*Data reflect a sample of 400 companies known to have experienced a ransomware event in 2023

76%
RACCOON\*

8%
VIDAR\*

8%
REDLINE\*

2%
METASTEALER

2%
LUMMAC2

2%
RHADAMANTHYS

1%
STEALC

1%
AURORA

IN 2023,

OF NORTH AMERICAN AND 

EUROPEAN RANSOMWARE 

VICTIM COMPANIES HAD AN 

INFOSTEALER INFECTION PRIOR 

TO BEING ATTACKED.\*

\*Data reflect a sample of 2,613 companies known to have experienced a ransomware event in 2023\. Data is current as of October 20, 2023\.

5SPYCLOUD RANSOMWARE DEFENSE REPORTMany organizations fail to fully remediate infostealer and other malware infections, focusing primarily on protecting the 

infected device and skipping critical remediation of exposed credentials and active session data, leaving them exposed to 

follow\-on attacks. In addition to presenting survey results in this report, we offer insights about how comprehensive 

Post\-Infection Remediation can help prevent ransomware attacks – and ultimately enable security teams to get ahead 

of attackers.

About the SpyCloud Ransomware Report

Since 2021, SpyCloud has gathered insights from security leaders and practitioners about ransomware’s impact on their 

organizations and their defensive practices. In this third year of the report, we continue to analyze the trends related to 

the evolution of this costly cyber threat.

We surveyed 316 individuals in active cybersecurity roles within organizations in the US, Canada, and the UK with at least 

500 employees. We asked them about:

1

2

3

TOP CONCERNS

about ransomware

for their business,

THE MOST COMMON

defenses their

organizations have in

KEY GAPS

that may be leaving

their organizations

including financial impact

place or on their roadmap

exposed

The report also provides insights into next\-generation strategies that support a more complete remediation cycle. We 

encourage you to look at these trends and learn how best practices are evolving to keep pace with new ransomware 

tactics, techniques, and procedures (TTPs).

6SPYCLOUD RANSOMWARE DEFENSE REPORTSurvey Demographics

SpyCloud solicited responses from individuals whose roles range from cybersecurity analysts to C\-suite security 

executives. The majority of the 316 participants come from leadership levels: 37% are cybersecurity directors, managers, 

or team leads; 29% are CIOs, CISOs, and security executives (Figure 1\).

SURVEY PARTICIPANTS BY ROLE

CIO, CISO, or cybersecurity executive

Cybersecurity director, manager, or team lead

Cybersecurity architect / engineer

Cybersecurity operator / analyst / incident responder

Cybersecurity administrator

Other role in cybersecurity

The cross\-section of surveyed organizations ranges in size from small (500\-999 employees) and midmarket (between 

1,000 and 9,999 employees) to large enterprises (with 10,000 or more employees). The two biggest cohorts represent 

mid\-sized employers: 30% with 1,000\-4,999 workers and 23% with 5,000\-9,999\. The largest enterprises (10,000\+ 

employees) comprise a total of 28% of respondents (Figure 2\).

SURVEY PARTICIPANTS BY SIZE OF ORG

500 \- 999

1,000 \- 4,999

5,000 \- 9,999

10,000 \- 25,000

More than 25,000

1

e
r
u
g

i

F

2

e
r
u
g

i

F

...

7SPYCLOUD RANSOMWARE DEFENSE REPORT19%30%23%12%16%29%37%11%11%4%8% 
 
KEY FINDINGS

1

$

1\. Despite some positive developments, the impact of ransomware

attacks remains high.

The good news? We found a drop in the number of organizations affected by 

ransomware and in the number paying ransom compared to the previous year. This 

likely reflects the temporary slowdown of ransomware activity in the later part of 

2022 before things ramped up again in the ﬁrst half of 2023\. Overall, however, 

impact from ransomware remains high, with 81% of surveyed organizations 

affected at least once in the past 12 months, and 48% of those that were 

impacted paying a ransom. Only 12% of those affected said the cumulative cost 

over 12 months was negligible, and for 39%, the cost was at least $1 million. The 

impact, however, is much broader than ﬁnancial losses. Ransomware also disrupts 

operations, damages organizational reputation, and drains SecOps resources – and 

the implications go on and on. 

$

...

8SPYCLOUD RANSOMWARE DEFENSE REPORTSurvey participants ranked phishing and social engineering as the riskiest entry points

points – but will need to keep pivoting to combat new attack vectors.

for ransomware attacks again this year. With human behavior an ongoing issue,

22\. Security teams are changing how they defend their riskiest entry

security teams are changing their approach – shifting from user awareness and

training to technology\-driven countermeasures to mitigate the inevitable

a necessary shift to make, but more adjustments are required. The majority of 

human\-driven risks.

As teams rely more heavily on tooling, they agree that automated workflows would 

signiﬁcantly improve their ransomware defenses and overall security posture. This is 

respondents ranked data backup and endpoint device protection as primary 

mechanisms for defense, but those countermeasures are insufficient as 

cybercriminals increasingly target unmanaged devices and steal authentication data 

that allows them to impersonate users and gain access to organizations’ networks 

and critical business applications. 

3

3\. Infostealer malware is a precursor for a ransomware event, but

teams aren't worried about it – and they aren’t prioritizing malware

remediation. 

Organizations are optimistic about their ransomware prevention capabilities, with 79% 

of surveyed security professionals expressing general conﬁdence in their ability to 

prevent a full\-blown ransomware incident. But their optimism may be misplaced, since 

only 19% of organizations are prioritizing improved visibility and remediation of 

exposed credentials and malware\-exﬁltrated data. Additionally, respondents ranked 

monitoring for compromised web session cookies and tokens as the third least 

important countermeasure. With infostealer malware infections preceding more nearly 

one\-third of ransomware attacks this year, these findings tell us that many 

organizations’ post\-infection remediation efforts are leaving the door wide open for 

follow\-on attacks. 

9SPYCLOUD RANSOMWARE DEFENSE REPORTTHE SHIFTING RANSOMWARE TRENDS

As we noted, ransomware took a roller\-coaster ride in the past 12 months. Some industry research showed a positive 

trend for 2022, with the number of attacks leveling off or even decreasing, and ransomware revenue dropping 40%. But 

the reprieve was temporary. During the second quarter of 2023, ransomware attacks skyrocketed – and ransomware 

payments approached record levels by June.

SpyCloud’s survey reflects these shifting trends. Although some of our indicators moved in a positive direction, upon 

digging in, we found a bleaker picture than appears on the surface.

On the Positive Side, We Saw Fewer Organizations Affected...

First, the positive news. We found a slight decline in the number of organizations affected at least once by ransomware 

in the past 12 months: 81% in this year’s survey vs. 90% last year. Additionally, we saw a year\-over\-year drop in the 

number of organizations affected at least once or multiple times (Figure 3\). It's important to note that 'affected' doesn't 

necessarily mean a business was impacted by a successful ransomware event; rather, that they were impacted to some 

degree that required business resources.

PAST FREQUENCY OF RANSOMWARE INCIDENTS (Y\-o\-Y)

3

e
r
u
g

i

F

E
R
A
W
M
O
S
N
A
R

Y
B

D
E
T
C
E
F
F
A

S
N
O

I

T
A
Z

I

N
A
G
R
O

F
O

E
G
A
T
N
E
C
R
E
P

60%

50%

40%

30%

20%

10%

0%

2021

2022

2023

None

One time

2 to 5 times

6 to 10 times

More than 10 times

NUMBER OF TIMES AFFECTED BY RANSOMWARE

10SPYCLOUD RANSOMWARE DEFENSE REPORT 
 
 
 
 
 
Contributing to some good news for organizations on the ﬁnancial front is a decline in the number of organizations 

paying a ransom (48% in the past 12 months compared to 65% the previous year) and a slight uptick in the number of 

those that recovered data at least partially if not fully, whether paying or not – 95% in this year’s survey vs. 93% last year 

(Figure 4\).

RESPONSE AND OUTCOME TO RANSOMWARE ATTACK

Paid ransom, fully recovered data

36\.2%

32\.9%

Paid ransom, partially recovered data

12\.2%

23\.7%

Paid ransom, had to recover data another way

Paid ransom, lost our data

Did not pay ransom, recovered data

3\.6%

2\.0%

1\.1%
1\.2%

Did not pay ransom, did not recover data

2\.9%

2\.0%

2022

2023

32\.6%%

49\.8%

4

e
r
u
g

i

F

…But the Impact Remains Immense for Entire Organizations

Despite some positive trends, ransomware remains a huge problem for organizations of any size, given that the majority 

are affected. 

While the prevailing assumption is that larger organizations are in a better position to defend themselves given budgets 

and resources, our data shows that large enterprises with 10,000 or more employees were affected just as much as 

mid\-sized organizations, with more than 72% reporting being affected at least once. Smaller organizations, however, 

weathered the worst impacts, with 90% affected (Figure 5\).

AT LEAST 81% OF ALL ORGANIZATIONS SURVEYED REPORTED 

BEING AFFECTED BY RANSOMWARE AT LEAST ONCE IN THE 

PAST 12 MONTHS

11SPYCLOUD RANSOMWARE DEFENSE REPORT 
5

e
r
u
g

i

F

6

e
r
u
g

i

F

D
E
T
C
E
F
F
A

S
N
O

I

T
A
Z

I

N
A
G
R
O

F
O

E
G
A
T
N
E
C
R
E
P

100%

75%

50%

25%

0

AFFECTED BY RANSOMWARE AT LEAST ONCE
(BY ORGANIZATION SIZE)

500 \- 999 employees

1k \- 4,999 employees

5k \- 9,999 employees

10k \- 25k employees

\> 25k employees

NUMBER OF EMPLOYEES IN THE ORGANIZATION

The Cost Is Climbing, Too

Last year, security researchers found an increase in average ransom demands across many sectors, possibly because 

attackers were trying to make up for the lower payee count. Even when victims choose not to pay, they still see ﬁnancial 

losses that go far beyond the ransom. Fewer than 12% of our surveyed organizations that were hit described their costs 

as negligible. For 39%, the price tag was over $1 million (Figure 6\). 

CUMULATIVE COST OF RANSOMWARE ATTACKS
(FOR THOSE ATTACKED IN THE PAST 12 MONTHS)

Negligible

$10k \- $100k

$100k \- $1M

$1M \- $3M

$3M \- $5M

$5M \- $10M

\> $10M

The harder\-to\-measure costs, from reputational damage to impact on operations and drain on resources, can be just as 

high or higher than the ransom itself. For example, SpyCloud’s data shows that multiple core teams across the 

organization, not just SecOps, are involved in traditional malware incident response. Considering that recovery times 

grew longer last year in many industries, the expense of response alone can quickly add up.

12SPYCLOUD RANSOMWARE DEFENSE REPORT90%85%76%74%72%12%17%32%17%15%5%2% 
 
 
 
 
A False Sense of Confidence

The positive developments we noted perhaps explain why 79% of surveyed security professionals feel fairly or highly 

conﬁdent about their capabilities to prevent a full\-blown ransomware attack in the next 12 months (Figure 7\). After all, 

perceptions are colored by past experiences. 

1%

7

e
r
u
g

i

F

CONFIDENCE ABOUT PREVENTING A
RANSOMWARE ATTACK

Not at all conﬁdent we can prevent ransomware

Somewhat conﬁdent we can prevent ransomware

Fairly conﬁdent we can prevent ransomware

Highly conﬁdent we can prevent ransomware

79% OF RESPONDENTS SAID THAT THEY ARE GENERALLY CONFIDENT IN THEIR ABILITY 

TO PREVENT A RANSOMWARE INCIDENT – BUT THEIR OPTIMISM MAY BE MISPLACED

Measuring conﬁdence based on the past or the current state breeds complacency – which is especially dangerous since 

attackers are constantly innovating. Security practitioners understand this better than security leaders: executives 

expressed much higher general conﬁdence than practitioners in preventing an attack. For example, only 71% of 

responding SecOps practitioners agreed they’re highly or fairly conﬁdent in this ability, compared to 91% of executives 

(Figure 8\).

13SPYCLOUD RANSOMWARE DEFENSE REPORT20%45%34% 
PERCENTAGE OF RESPONDENTS GENERALLY CONFIDENT
IN ABILITY TO PREVENT RANSOMWARE
(BY TITLE)

Executive

Overall

Architect / Engineer

Manager

Other

Security Admin

SecOps

91%

F

i

g
u
r
e

8

79%

77%

75%

72%

71%

71%

Our survey found that the two sectors 

most affected by ransomware at least 

once in the past 12 months were retail 

(93%) and technology (91%) (Figure 9\). 

This isn’t surprising, considering these 

sectors also lead in the amount of 

exposed data available on the criminal 

underground. SpyCloud’s recent 

Another factor that may have contributed to the false sense of optimism in the past 

twelve months was a temporary slowdown in activity, as several ransomware 

syndicates experienced chaos. Governments doubled down on dismantling 

high\-proﬁle groups such as Conti and REvil. But the cybercriminals quickly 

rebounded. REvil, for instance, resurfaced within months with an attack on a 

Fortune 1000 Exposure Report found, 

multibillion\-dollar manufacturing company.

among other things, that:

TECHNOLOGY

Had the lion’s share of compromised 

session cookies (1\.26 billion of the 

1\.54 billion total), and nearly 68,000 

malware\-infected employees.

RETAIL

Had 5\.88 million compromised 

cookies and 11,950 malware\-infected 

employees.

This authentication data, exﬁltrated 

from devices infected by infostealers, 

enables cybercriminals to easily 

impersonate employees and inﬁltrate 

the company.

...

In the meantime, multiple new groups popped up. Among them were Play, which 

uses self\-propagation techniques; and Black Basta, which launched a widespread 

campaign using a banking trojan to steal credentials. In the second quarter of 2023 

alone, at least 14 new ransomware\-as\-a\-service groups emerged. As these 

developments illustrate, the actors are multiplying, tactics are evolving, and the 

speed of criminal innovation is no match for current defenses.

INDUSTRY BREAKDOWN
ORGANIZATIONS AFFECTED AT LEAST ONCE

Retail

Technology

Overall

Manufacturing

Financial Services

Healthcare

Government

93%

91%

F

i

g
u
r
e

9

81%

79%

79%

63%

40%

14SPOTLIGHT ON SECTORS 
 
Stolen cookies/tokens are especially 

insidious because cybercriminals don’t 

even need employee credentials – with 

a still\-valid authentication cookie, they 

can bypass any authentication 

method, from multi\-factor 

authentication (MFA) to passkeys, and 

RANSOMWARE IS MORE THAN A
SECOPS PROBLEM

walk right into corporate systems and 

Although some organizations may not see big, immediate ﬁnancial impact from 

networks without raising any alarms.

ransomware attacks, they recognize that the exposure due to data loss creates just 

We were surprised, however, that our 

survey identiﬁed the healthcare sector 

as the second\-least affected industry. 

Although healthcare\-speciﬁc 

cyberattacks don’t seem to appear as 

frequently in headlines as of late, the 

as much risk, if not more. Participants ranked exposure of proprietary and 

sensitive data as the greatest potential impact of ransomware, followed by 

disruption to business operations and disruption to IT and SecOps (Figure 10\). 

The concern over data exposure maintained its lead from last year, reflecting the 

prevalent double\-extortion trend. With 89% of ransomware attacks incorporating 

FBI’s Internet Complaint Center data 

data exﬁltration, organizations realize that they need to worry about much more 

shows more ransomware attack 

reports were received from healthcare 

organizations in 2022 than any other 

critical infrastructure sector.

than being locked out of their encrypted systems or data.

PERCEIVED GREATEST IMPACTS OF RANSOMWARE
ON A SCALE FROM 1 TO 5

Exposure of sensitive or proprietary data

Disruption to business operations

Disruption to IT / security operations (or service levels

Loss of business\-critical data

Hard cost of recovering and restoring to
normal operations

Legal or compliance ramiﬁcations

Damage to brand reputation

Loss of customer satisfaction

4\.17

4\.11

4\.05

3\.98

3\.96

3\.90

3\.88

3\.83

F

i

g
u
r
e

1
0

Loss of revenue

3\.71

Hard cost of paying the ransom

3\.46

15 
R A N S O M W A R E
A T T A C K

$5\.13

AVERAGE COST ACCORDING TO 2023 IBM COST OF DATA BREACH REPORT

For years, compromised credentials 

(username \+ password combo) were 

considered the highest risk for 

cybercrimes such as account 

Where SecOps and BizOps Collide

As we’ve discussed, ransomware is not just a SecOps problem. It affects 

business operations by hoarding resources across the organization, often 

involving a minimum of seven internal departments, and can quickly result 

in damaged brand reputation or loss of business. IBM’s annual Cost of a 

Data Breach Report shows a painful price tag for an organization due to a 

takeover (ATO). Today, with access as 

ransomware attack: $5\.13 million on average, not including the ransom 

the new currency, session hijacking or 

itself.

next\-generation ATO is emerging as a 

new tactic.

Session hijacking originates from the 

takeover (or “hijack”) of an active 

browser or application session using 

a stolen, still\-valid authentication 

cookie where the criminal appears as 

a veriﬁed clone of a legitimate 

employee. This method goes beyond 

traditional credential exposure and 

expands the data criminals can now 

use to assume the access of an 

authenticated user. 

Criminals leverage these active 

sessions to exﬁltrate data, and 

But the burden to proactively protect business operations does generally 

fall on security teams working in the trenches, and these teams are often 

bringing the proverbial knife to a gunﬁght. Simply put, traditional malware 

remediation processes stop short of complete Post\-Infection Remediation, 

keeping the door open for attackers to come back by leaving that stolen 

data out for the taking and available to use until it’s invalidated.

SpyCloud’s Malware Readiness and Defense Report, released earlier this 

year, found that 92% of security leaders and practitioners are extremely or 

signiﬁcantly concerned about malware\-stolen data leading to future 

attacks. Unfortunately, it also revealed that incident response today often 

lacks the crucial steps to negate the consequences of that exposed data – 

and, as we uncovered in this survey, it’s still much the same.

monitor and mimic user behavior 

To prevent ransomware attacks and protect business operations, SecOps 

patterns. 

...

teams must remediate applications and users compromised by malware 

infections. A machine\-centric process of isolating and reimaging the 

infected device only cuts the connection to the malicious intruder. It doesn’t 

address the stolen credentials, cookies, and other authentication data 

making its way to darknet markets, where it can be leveraged by initial 

access brokers selling guaranteed access to ransomware gangs.

16THE IMPLICATIONS OFEMERGING NEXT\-GENACCOUNT TAKEOVER...

Last year alone, SpyCloud 

researchers recaptured 22 billion 

stolen cookie records, which 

indicates criminals are shifting 

tactics to steal, buy, and trade this 

highly accurate and highly valuable 

data – minimizing their need for 

larger breach datasets that may be 

clouded with old, outdated, and for 

their purposes, somewhat useless 

data.

For ransomware attackers, session 

hijacking is a highly successful 

tactic, yielding much better return on 

investment – and we expect to see it 

become mainstream as a way 

around passwordless technologies 

(like passkeys).

BATTLING RANSOMWARE ON
MULTIPLE FRONTS

Phishing and social engineering, along with unpatched vulnerabilities, once again 

ranked as the riskiest entry points for ransomware (Figure 11\). This was expected, 

since ransomware is often preceded by human behavior that results in a malware 

infection, which can then enable a ransomware attack. Similarly, respondents to our 

malware defense survey identiﬁed phishing and spear\-phishing as the second 

greatest threat to their organization’s security overall, with ransomware as the top 

threat.

PERCEIVED RISK OF ENTRY POINTS FOR RANSOMWARE
(ON A SCALE FROM 1 TO 5\)

Phishing / social engineering

3\.87

Unpatched vulnerabilities

3\.72

Third\-party or partner connections

Unmanaged employee devices

Exposed or weak credentials that
enable ATO

Unmanaged contractor devices

Exposed (weak) APIs

Stolen cookies / tokens that enable
session hijacking

3\.61

3\.57

3\.53

3\.48

3\.46

3\.43

F

i

g
u
r
e

1
1

We were surprised, however, to see stolen cookies/tokens rated as the least risky 

entry point, suggesting that understanding of this new threat is just beginning. This 

entry point is an especially high risk in passwordless environments, which many 

view as the future of authentication. While passkeys are a tremendous 

improvement over passwords, cybercriminals are simply working around 

passwordless authentication with session hijacking attacks. 

17 
...

The bottom line is that each of these entry points is risky, but together they’re a 

force multiplier. This means teams must focus on all of them, including third\-party, 

unmanaged, and undermanaged devices, and weak APIs. The use of unmanaged, 

undermanaged, and third\-party devices, for instance, has exploded in the 

digital\-ﬁrst environment, yet they create blind spots for security teams. Likewise, 

the use of APIs has skyrocketed in recent years, and many organizations don’t pay 

Not all sectors view their riskiest entry 

enough attention to the security implications of vulnerable and improperly designed 

points through the same lens, with 

some placing higher emphasis than 

the average across all industries on 

risks such as stolen cookies and 

unmanaged or undermanaged devices. 

For example:

WEAK APIs are a bigger concern in 

retail, manufacturing, and technology

Manufacturing, Technology, and 

Healthcare view COOKIES as riskier 

APIs and stolen API keys, which are another form of access being exﬁltrated from 

malware\-infected devices. 

Countermeasures Misaligned with New Ransomware Tactics

Year over year, data backup has remained the most important countermeasure for 

organizations (Figure 12\). We highlight this as concerning because it shows that 

defenses are not adjusting to the shift in ransomware tactics. Backup was 

effective years ago when data encryption was the biggest problem, but it doesn’t 

mitigate the risks of modern ransomware – which relies heavily on 

compared to the average

malware\-exﬁltrated authentication data.

Across sectors, retail cybersecurity 

professionals are the most concerned 

about UNMANAGED EMPLOYEE 

DEVICES

MOST IMPORTANT COUNTERMEASURES IN PRACTICE TODAY
(ON A SCALE FROM 1 TO 5\)

Data backup

4\.36

Multi\-factor authentication (MFA)

Endpoint / device protection

Email security (with phishing detection)

User awareness / training

Monitoring for exposed credentials

Patch \& secure conﬁguration management

Threat intelligence services

Network / resource segmentation

Monitoring for compromised web sessions
(stolen cookes / tokens)

4\.26

4\.24

4\.21

4\.18

4\.13

4\.10

4\.08

4\.04

3\.98

F

i

g
u
r
e

1
2

User and entity behavior analytics (UEBA)

3\.87

Deception technology (e.g., virtual honeypots)

3\.80

18SPOTLIGHT ON SECTORS’PERCEIVED RISKYENTRY POINTS 
Organizations are optimistic about their ransomware prevention capabilities, with 79% 

of surveyed security professionals expressing general conﬁdence in their ability to 

prevent a full\-blown ransomware incident. But their optimism may be misplaced, since 

only 19% of organizations are prioritizing improved visibility and remediation of 

exposed credentials and malware\-exﬁltrated data. Additionally, respondents ranked 

monitoring for compromised web session cookies and tokens as the third least 

important countermeasure. With infostealer malware infections preceding more than 

a fifth of ransomware attacks this year, these findings tell us that many 

organizations’ post\-infection remediation efforts are leaving the door wide open for 

follow\-on attacks. 

The importance of MFA grew signiﬁcantly year over year, which may be contributing to organizations’ false sense of 

security. Although organizations should deploy MFA as one of their critical defense layers, they must also take the steps 

to identify malware\-infected employees and invalidate stolen cookies that enable authentication bypass and session 

hijacking. As stated earlier, MFA and passwordless technology such as passkeys are not sufﬁcient ﬁxes because session 

hijacking bypasses any form of authentication.

Since technology and tools are only one part of the defense equation, we also asked the security pros about their 

operational and organizational countermeasures. Most feel that they adhere well to basic hygiene practices such as 

patching and applying least privilege techniques (Figure 13\). While the majority already have strategies like 

ransomware\-speciﬁc incident response in place, plenty of work remains to be done, with a good number of respondents 

noting they are considering or are only in the planning stages of implementing upgrades to their existing strategy. 

STATUS OF RANSOMWARE COUNTERMEASURES

ALREADY IN
GOOD SHAPE

PLAN TO
UPGRADE

Adhere to security hygiene best practices

(e.g., frequent patching, least privileges)

Cyber insurance that includes coverage

for ransomware attacks

Ransomware\-speciﬁc incident response team

3
1

e
r
u
g

i

F

Ransomware\-speciﬁc incident response

training or exercises

Ransomware\-speciﬁc incident response

plan / playbook

60%

48%

48%

45%

42%

21%

27%

32%

30%

33%

PLAN
TO ADD

17%

17%

19%

23%

23%

NO
PLANS

2%

8%

4%

2%

2%

It’s worth noting that there is a signiﬁcant disconnect between the high conﬁdence in operational practices and the high 

number of organizations that were affected by ransomware in this year’s survey. This gap tells us that either the 

combination of technology and processes isn’t working – or organizations are overly optimistic about their controls.

19SPYCLOUD RANSOMWARE DEFENSE REPORT 
THE IMPOSSIBLE HUMAN FACTOR

Organizations recognize that human behavior plays a major role in the ability to defend against 

ransomware, but they’re shifting from user awareness to technology\-based measures. Unfortunately, these 

measures only work if SecOps teams have complete visibility and control across all users, applications, and 

devices connecting to the network and accessing sensitive data – and that’s not the case today. In recent 

findings, we learned that:

36%

54%

28%

OF ORGANIZATIONS

OF ORGANIZATIONS

OF ORGANIZATIONS

allow unmanaged personal

struggle with shadow IT

allow unmanaged third\-

devices to access

due to employee adoption

party devices to access 

business applications and

of applications and systems

business applications and

systems

without IT’s consent

systems

These risky practices illustrate that SecOps teams are struggling to keep up with the evolution of the digital 

workplace and often lack visibility into their sprawling attack surface.

20SPYCLOUD RANSOMWARE DEFENSE REPORTFUTURE DEFENSE PRIORITIES SHOW DISCONNECT

Lack of visibility, the inefﬁciency of manual tasks, and cumbersome or false alerts are recognized problems in 

cybersecurity. Survey participants overwhelmingly agree that better visibility of malware\-exﬁltrated data, along with 

automated remediation workflows, would improve their ability to combat ransomware and improve overall security 

posture (Figure 14\).

1%

1%

4
1

e
r
u
g

i

F

VISIBILITY \& REMEDIATION OF
MALWARE\-EXFILTRATED DATA AS KEY
TO COMBATING MALWARE

Strongly agree

Somewhat agree

Somewhat disagree

Strongly disagree

98% OF RESPONDENTS AGREE THAT BETTER VISIBILITY INTO MALWARE\-EXFILTRATED 

DATA AND AUTOMATED REMEDIATION WORKFLOWS WOULD IMPROVE THEIR OVERALL 

SECURITY POSTURE

This sentiment, however, contradicts respondents’ views on the importance of session cookies, which they ranked in their 

bottom three countermeasures, as noted earlier. It also doesn’t align with reported authentication practices that are in place: 

automated workflows to remediate compromised session cookies/tokens and automated workflows to remediate exposed 

passwords are among the bottom three authentication practices that organizations are currently using (Figure 15\). However, 

it’s clear that this is an area of increasing focus, as automation for remediating those two threats is at the top of priorities for 

the next 12 months.

21SPYCLOUD RANSOMWARE DEFENSE REPORT51%47% 
The harder\-to\-measure costs, from reputational damage to impact on operations and drain on resources, can be just as 

high or higher than the ransom itself. For example, SpyCloud’s data shows that multiple core teams across the 

organization, not just SecOps, are involved in traditional malware incident response. Considering that recovery times 

grew longer last year in many industries, the expense of response alone can quickly add up.

AUTHENTICATION PRACTICES IN USE OR PLANNED FOR
IMPLEMENTATION/UPGRADE

ALREADY IN GOOD SHAPE

Password complexity requirements

Monitoring for exposed employee passwords

Banned password list (e.g., 123password)

Single sign\-on

Password manager solutions

Passwordless authentication solutions(biometrics, passkeys)

Monitoring for exposed contractor, partner, and supplier passwords

Monitoring for stolen partner and supplier session cookies / tokens

Other authentication solutions

Monitoring for stolen employee session cookies/tokens

5
1

e
r
u
g

i

F

Automated workflows to remediate compromised session cookies / tokens

Automated workflows to remediate exposed passwords

Hard tokens for MFA

PLAN TO UPGRADE OR ADD

Password complexity requirements

Monitoring for exposed employee passwords

Banned password list (e.g., 123password)

Single sign\-on

Password manager solutions

Passwordless authentication solutions (biometrics, passkeys)

Monitoring for exposed contractor, partner, and supplier passwords

Monitoring for stolen partner and supplier session cookies / tokens

Other authentication solutions

Monitoring for stolen employee session cookies/tokens

Automated workflows to remediate compromised session cookies / tokens

Automated workflows to remediate exposed passwords

Hard tokens for MFA

64%

59%

57%

54%

53%

48%

46%

41%

40%

39%

37%

35%

34%

35%

39%

39%

38%

43%

46%

48%

53%

58%

59%

60%

63%

55%

However troubling the disconnect, these ﬁndings are consistent with those from SpyCloud’s malware defense survey, in 

which 98% of security professionals also agreed that better visibility into business applications exposed by an infostealer 

infection would increase security posture. This lack of visibility hinders progress in the ﬁght against ransomware, and 

SecOps teams have to ﬁgure out this problem in order to effectively reduce the risk of malware exposure.

22SPYCLOUD RANSOMWARE DEFENSE REPORT 
All Eyes on Prevention and Automation

Proactive prevention is just as important as strengthening defenses and response capabilities, and our respondents 

agreed when asked to pick their top three defense priorities. Improving ransomware prevention capabilities is the top 

priority for organizations in the next 12 months, followed by improving ransomware detection capabilities and 

automating security processes and workflows (Figure 16\). 

6
1

e
r
u
g

i

F

TOP SECURITY PRIORITIES

Improving ransomware prevention capabilities

60%

Improving ransomware detection capabilities

Automating security processes and workflows

44%

41%

Improving ransomware response capabilities

34%

Better ensuring the security of third\-party connections and services

Improving security hygeine practices

Improving visibility and remediation for exposed credentials and
malware\-exﬁltrated data

Increasing the size / stafﬁng of the security operations team

Updating incident response plans and procedures

Increasing utilization of external security services / expertise

30%

25%

19%

18%

15%

14%

Although prevention and detection are in the top three priorities for both security leaders and practitioners, the two sides 

place different importance on automation. Executives identiﬁed automation as their second priority, while admins and 

analysts/incident responders ranked it third, and managers and architects fourth. In contrast, automation is the top 

overall security priority identiﬁed in our Malware Readiness and Defense Report, reflecting a growing industry trend of 

organizations automating processes as much as possible to not only combat the talent gap crisis but also boost SecOps 

efﬁciency.

The average duration of a ransomware attack – the time between initial access into the organization and the 

ransomware deployment – has plummeted more than 94% in the span of just two years. What used to take attackers 

more than two months now takes less than four days. This accelerated timeline illustrates how cybercriminals are 

making headwinds at a dizzying pace, underscoring the need for SecOps teams to automate remediation processes.

23SPYCLOUD RANSOMWARE DEFENSE REPORT 
This authentication data, exﬁltrated 

from devices infected by infostealers, 

enables cybercriminals to easily 

impersonate employees and inﬁltrate 

the company.

ADAPTING RANSOMWARE DEFENSES FOR
STEALTHIER ATTACKS

We found that ransomware prevention is consistently at the top of the priority list for organizations, not only across all 

security roles but also regardless of an organization’s size. So, what does proactive prevention look like in the face of 

evolving threats?

Ransomware is a malware problem at its core, which means that preventing ransomware attacks must start with 

proper and robust malware remediation. Bad actors are exploiting infected systems to exﬁltrate data they can use to aid 

an attack, identify potential entry points to corporate resources, and deliver executable ﬁles. 

Traditional malware response, however, doesn’t address the risk of the stolen data from an infected device. By the time 

malware is detected and the device has been reimaged, the data is already in the hands of criminals. Some infostealers 

can siphon data in mere seconds. Non\-persistent malware can vanish with little or no trace, which means teams don’t 

know it was ever there to begin with. SecOps workflows and processes have to evolve to include a critical addition to 

their next\-gen incident response: Post\-Infection Remediation.

MALWARE RESPONSE MUST INCLUDE POST\-INFECTION REMEDIATION

N
IO
T
C
E
F
N

I

\-
T

S

O

P

P R E \- I NFECTION

PREVENTION

ENTERPRISE

EXPOSURE

REMEDIATION

DETECTION \&

CONTAINMENT

D
E

VICE RES

RE\-IMAGE DEVICE

PONSE

24SPYCLOUD RANSOMWARE DEFENSE REPORTToday’s attack surface includes users and applications, not just devices. And Post\-Infection Remediation is a paradigm 

shift from the current machine\-centric response to a more comprehensive identity\-centric response that takes that 

growing attack surface into greater consideration. While traditional machine\-centric remediation simply clears a device, 

Post\-Infection Remediation takes additional measures to reset stolen credentials and invalidate active web sessions of 

exposed applications. This approach adds the necessary steps to protect an organization from additional entry points for 

a ransomware attack. 

SecOps teams can’t take these extra steps without visibility into the entire attack surface to start with. Incident 

responders need to know what authentication data has been stolen, and which users and corporate applications have 

been exposed, so they can focus efforts (ideally in an automated fashion) in the right areas.

Yet, as our report reveals, visibility is a universal struggle. The proliferation of unmanaged, undermanaged, and 

third\-party devices perpetuates blind spots for security teams. Shadow IT and shadow data exacerbate the problem 

because unsanctioned applications and data stored in them are not traditionally governed by corporate security policies.

The only way for defenders to gain ground and stay a step ahead is by embracing next\-generation malware remediation 

practices – and this is where Post\-Infection Remediation comes in. By adding Post\-Infection Remediation to their 

playbooks, SecOps teams can greatly improve their ransomware prevention outcomes and move faster to close the 

door on attackers, all while minimizing the cross\-team resources that full\-blown incidents consume.

25SPYCLOUD RANSOMWARE DEFENSE REPORT 
For years, compromised credentials

(username \+ password combo) were

considered the highest risk for

cybercrimes such as account

takeover (ATO). Today, with access as

the new currency, session hijacking or

next\-generation ATO is emerging as a

new tactic.

Session hijacking originates from the

takeover (or “hijack”) of an active

browser or application session using

a stolen, still\-valid authentication

cookie where the criminal appears as

a veriﬁed clone of a legitimate

employee. This method goes beyond

traditional credential exposure and

expands the data criminals can now

use to assume the access of an

authenticated user.

Criminals leverage these active

sessions to exﬁltrate data, and

monitor and mimic user behavior

patterns.

FINAL THOUGHTS

Our biggest takeaway from this year’s survey is that SecOps teams have not yet embraced a key piece of the 

ransomware defense puzzle – remediating malware\-exﬁltrated authentication data – which means that many 

organizations may be more vulnerable than they realize. With an infostealer infection as a precursor to nearly one\-third 

of ransomware events in 2023, teams can no longer ignore this rising threat.

While many respondents noted feeling conﬁdent in their ability to avoid a ransomware attack in the next 12 months, their 

current practices and future priorities don’t support that optimistic outlook:

Organizations view phishing and social engineering as the riskiest entry point for ransomware, and have 

shifted their focus from changing behaviors through user awareness and training to technology\-driven 

controls. Yet they lack important visibility into authentication data that has been exfiltrated from 

unmanaged, undermanaged, and third\-party devices, which greatly limits the impact of any new defensive 

mechanisms.

Respondents overwhelmingly agree that better visibility of malware\-exﬁltrated data and automated 

remediation would improve their ransomware defenses and overall security posture. But they view 

monitoring for compromised cookies as one of the least important countermeasures. They’re also least 

likely to have or implement automated workflows for remediating exposed passwords and cookies, compared 

to other authentication practices.

Ransomware prevention is the biggest priority for security leaders and practitioners alike. However, 

without complete malware remediation, any prevention efforts will remain limited.

As workplaces continue to digitally transform and organizations adapt how they do business, human behavior continues 

to add to a sprawling attack surface. And threat actors are paying attention. They’re modifying their TTPs for a landscape 

where access is the new currency and ﬁnding quick ways to circumvent authentication layers, from MFA to passkeys. For 

SecOps teams that want to outmaneuver ransomware attackers, SpyCloud’s enterprise protection solution offers 

automated detection of malware infections across devices and fuels remediation workflows powered by comprehensive 

and actionable data. 

Stolen credentials via malware\-siphoned data give cybercriminals the upper hand – isn’t it high time to use the same 

data against them? By gaining full visibility into malware infections and acting quickly, SecOps teams can truly gain 

conﬁdence in their ability to keep the business safe.

26SPYCLOUD RANSOMWARE DEFENSE REPORTPROTECT YOUR ENTERPRISE FROM
RANSOMWARE WITH SPYCLOUD

THE FIRST LINE OF DEFENSE IS PREVENTION

Act on known points of compromise to shut down targeted attacks like ransomware.

With SpyCloud, you get actionable insights and high\-ﬁdelity alerts that let you

stop a malware infection from becoming a full\-blown ransomware event. 

SPYCLOUD EN TER PR IS E PROTECT ION

ABOUT SPYCLOUD

SpyCloud transforms recaptured darknet data to protect businesses from cyberattacks. Its products 

operationalize Cybercrime Analytics (C2A) to produce actionable insights that allow enterprises to proactively 

prevent ransomware and account takeover, protect their business from consumer fraud losses, and 

investigate cybercrime incidents. Its unique data from breaches, malware\-infected devices, and other 

underground sources also powers many popular dark web monitoring and identity theft protection offerings. 

SpyCloud customers include half of the ten largest global enterprises, mid\-size companies, and government 

agencies around the world. Headquartered in Austin, TX, SpyCloud is home to nearly 200 cybersecurity 

experts whose mission is to make the internet a safer place.

To learn more and see insights on your company’s exposed data, visit spycloud.com.

27SPYCLOUD RANSOMWARE DEFENSE REPORT