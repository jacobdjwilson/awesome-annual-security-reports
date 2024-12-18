July 2021

CYBER SECURITY HUB 

2021 STATE OF 
DEVSECOPS

Sponsored by:

2

Introduction

Today, DevOps teams are embracing new 

approaches of embedding application security 

testing (AST) into their development pipelines to 

truly achieve DevSecOps. Developer and security 

teams agree that a single vulnerability scan late 

in the software development life cycle (SDLC) 

is insufficient, can result in delayed software 

releases, and often becomes unnecessarily 

expensive. As with any type of security testing, 

discovering vulnerabilities late in the pipeline 

means it takes more time and effort to remediate 

them. Hence, it’s highly desirable to shift AST as 

far left as possible by integrating security into the 

tooling developers use. 

However, DevSecOps is still in its early stages, as 

evidenced by our 2021 survey, which indicates that 

the security portion of DevSecOps is maturing in 

pieces. Part of the problem is budget, and part

of it has to do with a talent shortage. Smaller 

companies especially lack the security expertise 

and tools larger companies have.

Some of the key findings from our 2021 

survey are:

Half of respondents plan to add more 

application security staff in the next year.

43% say their biggest frustration is security 

testing done late in the SDLC because it 

delays launches.

Of all the application security types, API 

testing is the most popular among two\-thirds 

of respondents.

Two\-thirds lack a security champion.

2021 State of DevSecOpsMethodology

3

This report is based on a global online survey of application 

APAC and the Americas. Forty\-five percent hold director, 

security professionals that took place during late May and 

VP, or C\-level titles.

June 2021\. Sixty percent are located in EMEA, followed by 

How big is your application security team?

There are always far fewer application security team 

members than developers. Developers outnumber security 

professionals 100 to 1 in large organizations. More than half of 

respondents (53%) said they employ one to five application 

security team members, and generally speaking, the lower 

number is generally associated with small and medium 

businesses (SMBs).

However, typically, as the number of application security 

team members rise, so does the size of the organization. 

The number of companies employing 21 or more such 

professionals outnumbers those that employ 11 to 20\.

17%

7%

23%

1\-5 

6\-10

53%

11\-20

21\+

Do you plan on adding additional staff to your application security team within the next year?

50%

38%

12%

No more additional staff planned

1\-5 more

5\-10 more

Half of respondents plan to add more security staff, with 

the majority (38%) adding just one to five more. A non\-trivial 

factor is the shortage of security talent. 

“There’s always a shortage of experienced people, and that’s 

the challenge,” said Stephen Gates, security evangelist and 

senior solutions specialist at Checkmarx. “That’s a hurdle 

organizations are going to have to deal with even though 

they want to double the size of their staff.”

2021 State of DevSecOpsMethodology

4

72%

75%

0%

46%

44%

42%

30%

Nearly three\-quarters (72%) view vulnerability reduction as 

automation, typically in a CI/CD pipeline that is highly 

the key measure of success. Fewer (46%) are focused on 

automated otherwise.

particular vulnerabilities they’ve identified previously. 

The scary statistic is that 44% measure success based 

don’t want to advertise the fact that they have software 

on security vulnerability identification, not remediation. 

vulnerabilities, and they don’t want people hacking their 

About the same number (42%) are achieving release 

systems to find bugs. On an industry level, companies 

speed and quality by integrating security testing and 

generally are decreasing bug bounties.

Three in 10 have reduced bug bounties because they likely 

What kind of reporting is given to the CISO? 
\*Respondents could select more than one option

Half of respondents are providing the CISO with a PDF report 

of security scan findings, some of which include custom 

charts. The people who are not providing the CISO with any 

report may lack the necessary tools or time to do it, or the 

company may not have a CISO in the first place.

50%

34%

PDF report 

with findings

Custom charts created 

by the AppSec team

32%

No report 

given

4%

Other

2021 State of DevSecOpsHow do you measure a successful application security testing program?\*Respondents could select more than one optionOverall reduction of all types of vulnerabilitiesSpecific reduction of vulnerabilities (such as SQL injection and/or XSS)Number of vulnerabilities identified (but not fixed)Increased velocity of releases with application security testing integrated and automatedDecrease in bug bounty effortsMethodology

5

What is your biggest frustration with application security testing?
\*Respondents could select more than one option

Too late in life cycle \- delays launch

Understanding the vulnerability findings \- 

what was found, how risky, how to fix it?

Too many false positives

Tracking vulnerability status \- verified? 

Scheduled for remediation? Fixed?

Prioritizing vulnerability remediation

Finding who can perform 

the remediation

Other

45%

)

%

(

s
t
n
e
d
n
o
p
s
e
R

0%

43% 43%

36%

36%

29%

25%

1%

There are several frustrations with application security 

An equal number (43%) are frustrated by their inability 

testing, and one of the most prominent is testing too late in 

to interpret the scan findings, how risky a suspected 

the life cycle (43%). A quick vulnerability scan is not enough 

vulnerability may be, and how to quickly fix it. There’s a gap 

to address all application vulnerabilities, and it often results 

between understanding a vulnerability and its remediation.

in interpersonal conflicts between developers and security 

since it requires developers to revisit code after they’ve 

A related issue is tracking the vulnerability status to make 

moved onto another project. From an overhead perspective, 

sure it’s actually being fixed (36%). Teams often lack the 

it’s more time\-consuming and expensive.

tools or tool integration they need to track the status of 

vulnerability remediation in a quick and easy way.

“When people say a vulnerability is being identified too late, 

Also at 36% are false positives, which waste precious time. 

is a clear indication that integration and automation of 

Alternatively, when false positives are too frequent, people 

AST solutions within their development pipelines is less than 

tend to ignore them (which is called “alert fatigue”). Alert 

perfect,” said Gates. “Then, just before deployment, they 

fatigue is not only very real, but also potentially dangerous 

launch a scan and then say, ‘Oh wow, we have lots more 

because some true positives may be ignored.

work to remediate the vulnerabilities we’ve discovered’.”

2021 State of DevSecOps 
Methodology

6

How are you currently (or planning) automating application security testing?

Time to market pressure necessitates automated AST, but it 

CI/CD tooling (Jenkins, 

SCM integration 

also helps ensure code quality. Those with CI/CD pipelines 

TeamCity, CircleCI, etc.)

(Webhooks on 

(36%) are automating or plan to automate security testing 

as part of a larger automation strategy since CI/CD and 

automation go hand in hand. Another 15% are relying on 

SCM integration.

Do not have automation

pull request / pushes)

Nightly / Weekly cronjobs

“Source code management integration is something people 

either don’t know about or they don’t have the correct 

application security testing tools that can integrate directly 

within their SCM tools of choice,” said Gates. “Scan early and 

scan often is the way to work. Within the SCM is the best 

18%

location to launch scans since it’s the often the farthest left 

you can go.”

15%

36%

Automation is a maturity issue that requires AST integration 

within the dev tools in use, which some organizations clearly 

lack (31%). However, modern AST solutions can easily be 

intergrated and fully automated.

31%

Where is the best place developers consume application security results?

Half the respondent base considers a bug tracking tool 

Bug tracking tool

In the pull / merge request

like Jira the best place to consume application security 

In their IDE

PDF report

results because they already have the tool in place, with 

both develops and security already using it. A distant 

second (20%) is in an IDE, because modern IDEs show 

coding errors in real time, though they won’t catch 

everything because they were not designed specifically to 

identify application vulnerabilities.

About the same number (19%) prefer a pull/merge request.

19%

“If you automate the pull request, then you can actually 

get the results right back in the SCM tool you’re working 

on, and what’s nice about that is it’s very fast,” said Gates. 

“Developers have the opportunity to remediate quickly 

when they’re sitting in a branch of code or working on it. It’s 

just expected.”

12%

20%

49%

2021 State of DevSecOpsMethodology

7

What type of security testing are you performing?
\*Respondents could select more than one option

Two\-thirds of survey participants (67%) are doing API 

testing because it’s becoming an increasing threat. In 

fact, Gartner predicts that APIs will become the most 

popular attack vector by 2022\. Another reason API testing 

is popular is because modern applications have a lot of 

dependencies. Today’s applications rely on a number of 

outside functions and data to operate as intended. Those 

70%

dependencies, if they contain security flaws, may infect 

an application. In addition, cloud native development and 

the use of microservices are growing exponentially, so API 

vulnerabilities are of particular concern. 

API

SAST

Container scanning

SCA

DAST

IAST

Fuzzing

67%

44%

36%

31%

21%

14%

11%

)

%

(

s
t
n
e
d
n
o
p
s
e
R

0%

Static application security testing (SAST) is more than 

twice as popular (44%) as dynamic application security 

testing (DAST, at 21%) because DAST doesn’t always fit well 

into modern application development practices, which 

emphasize speed.

When organizations start decomposing applications 

into microservices and using containers—or building new 

applications with containers—they eventually realize they 

need special tooling and updated practices since traditional 

application security tooling and practices won’t work. Each 

container represents an individual attack surface, unlike a 

monolithic application. The 36% using container scanning 

realize this.

Finally, the use of software composition analysis (SCA) tools 

is on the rise because of open source security concerns. 

Today’s applications use more third\-party commercial and 

open source components and libraries than ever before 

because of time to market mandates and an increase in 

application complexity. Without SCA, it can be more difficult 

to pinpoint open source vulnerabilities and license risks.

2021 State of DevSecOps 
 
Methodology

8

Do you use any open source tooling specifically for finding security vulnerabilities?

42%

Yes

58%

No

Despite the increased use of open source code, 58% said 

open source modules, packages, and libraries these teams 

they’re not using open source security testing tools.

are using,” said Gates.

“That’s a concern because of the increase in the amount of 

What improvements in application security testing would you like to see?
\*Respondents could select more than one option

Better integrations

User interface / experience

Faster scans

Less false positives

More application security offerings

More accurate queries out of the box

52%

50%

45%

39%

30%

62%

65%

)

%

(

s
t
n
e
d
n
o
p
s
e
R

0%

Most respondents (62%) chose better integrations as the top 

velocity and product quality. Also causing friction are less\-

improvement they’d like to see because of all the friction a 

than\-optimal user experiences (52%). Faster scans (50%) and 

lack of integration causes. Insufficient integration precludes 

fewer false positives (45%) are also about speed.

visibility across tooling and it prevents teams from achieving 

the level of automation they need to improve release 

2021 State of DevSecOps 
Methodology

9

How do you communicate with developers on bugs found?

Jira tickets

Emails

Group meetings

Slack messages

Other

48%

50%

31%

)

%

(

s
t
n
e
d
n
o
p
s
e
R

0%

13%

6%

2%

Jira tickets are the top means of communicating with 

respondents since everyone uses email but not everyone 

developers (48%) since so many DevOps teams already use it.

uses Jira. While email can accommodate all the information 

a developer will need, unlike Slack, emails are not a real\-

“Integration and automation into Jira systems is probably 

time communication medium, and they can get lost easily 

vastly desired because of the need for speed, which extends 

in a universe of other emails. It can also be difficult to search 

to triage, troubleshooting, and remediation,” said Gates. 

through emails to find out what the status of remediation is.

“There’s a desire to have automation and integration with 

the actual scans to open and close tickets automatically.”

Group meetings have the benefit of getting everyone on the 

same page (13%), but they take time away from other day\-

Email is an antiquated way of communicating information 

to\-day tasks. 

about code issues, but it’s still popular among 31% of 

Do you currently use a Security Champion type of model within your organization?

Another scary statistic is that two\-thirds of respondents (66%) 

lack a security champion, when that’s such an important 

role. The security champion evangelizes security within the 

organization, which helps create a cyber\-aware culture. 

Since they’re security experts and also good communicators, 

they’re a good resource for mentoring developers. The 

security champion is the designated go\-to person 

developers and others can tap when they have a security\-

related question.

34%

66%

Yes

No

2021 State of DevSecOps 
Methodology

10

What do you currently do for security awareness?
\*Respondents could select more than one option

47%

44%

39%

34%

6%

Internal 

wiki center

Instructional

videos

OWASP

Just\-in\-time training solution 

Other

(such as Checkmarx Codebashing)

Wikis are alive and well in a security context. Nearly half 

specific to web application security, and the guidelines tend 

of survey participants (47%) are using a wiki as the primary 

to be quite general.

vehicle for security awareness, with just slightly fewer (44%) 

saying they use instructional videos.

About one\-third have integrated real\-time training, which 

helps accelerate application release speed and quality. Unlike 

Fewer still are those using the Open Web Application Security 

videos, which take time away from coding, real\-time training 

Project (OWASP), an online community providing freely 

teaches developers application security within the context of 

available web application security articles, methodologies, 

writing code. If a developer doesn’t know how to remediate 

documentation, tools, and technology. Then again, OWASP is 

an issue, a five\-minute tutorial will often solve the problem.

What skills will be important for security professionals to have in the future?
\*Respondents could select more than one option

61%

56%

52%

48%

35%

Subject matter 

Soft skills like communication 

Advanced 

AI/ML

expertise

and collaboration

programming

IoT/

blockchain

1%

Other

Subject matter expertise tops the list (61%) of what 

the application side of application security as much as the 

respondents think security professionals will need to have in 

security side of application security and being able to tell a 

the future. Security professionals tend to be driven to upskill 

developer what to do. 

themselves because they want to advance their careers, 

often into the role of a security champion or CISO.

AI and machine learning are also considered important 

knowledge to have (48%), given their growing popularity 

However, to become an effective security champion or CISO, 

throughout enterprises. At first, enterprises raced to implement 

they need to have technical expertise and soft skills (56%), 

AI and ML to reap the benefits, but more realize now that they 

such as communication and collaboration, because the role 

must also manage the potential risks not only with the help of 

interacts with other roles in the company. 

data scientists, but security professionals as well.

Advanced programming skills (52%) does not mean that 

Meanwhile, IoT and blockchain use is emerging, as reflected 

security professionals are morphing into developers (though 

by the 35%.

some may choose to do so). It’s more about understanding 

2021 State of DevSecOpsMethodology

11

Is the speed of an application security testing scan more valuable than the quality of results?

64%

No

36%

Yes

It’s encouraging that 64% of respondents consider the quality 

The result may seem counterintuitive based on some of the 

of application testing more important than speed, because 

other survey responses that demonstrate a desire to remove 

it speaks to the desire to provide higher quality software and 

obstacles to speed. However, given the choice between 

avoid the headaches of a customer or bad actor discovering 

speed and quality, quality prevails because it equates to 

security issues in production.

more secure code.

Conclusion

Application security continues to rise in importance 

As always, individual respondent companies are at different 

because it represents legal, regulatory, and brand issues. 

stages of maturity because speeding delivering and 

End users expect applications to be of high quality, which 

increasing code security simultaneously is a journey. Moving 

includes security. It’s not enough to simply build and deliver 

from DevOps to DevSecOps helps.

applications faster. Speed and quality must go hand in hand. 

2021 State of DevSecOps

2021 State of DevSecOpsAbout Cyber Security Hub 

The Cyber Security Hub is an online news 

through obtaining data and interviewing end 

source for global cyber security professionals 

users and analysts throughout the industry to 

and business leaders who leverage technology 

deliver practical and strategic advice. 

and services to secure the entire perimeter in 

their enterprise. 

Our editorial team surveys and monitors the 

latest trends in cyber security and creates news 

We’re dedicated to providing the latest industry 

articles, market reports, case studies and in\-

news, thought leadership and analysis in the 

depth analysis for a captive audience consisting 

cyber security space. Cyber Security Hub’s expert 

of C\-Level executives, VPs and directors of cyber 

commentary, tools and resources are developed 

security and information technology. 

Cyber Security Hub Team

Dorene Rettas 
Managing Director

Dorene.Rettas@CSHub.com

Joshua Snead
North America Sales Director

Joshua.Snead@iqpc.com

Seth Adler
Editor\-in\-Chief

Seth.Adler@iqpc.co.uk

Tilak Antony
Director of IQPC

Digital Partnerships
Tilak.Antony@iqpc.com 

Imran Shafi
Sales Director

Imran.shafi@iqpc.com

Desiree Santiago
Marketing Manager

Desiree.Santiago@cshub.com 

Social Media Information

Facebook:
CSHubIQPC

Twitter:
CSHubUSA

LinkedIn:
CSHub – Enterprise
Security Professionals

2021 State of DevSecOps

 Visit CSHub.com for more information from cyber 

security leaders for the cyber security community

The world runs on code.
We secure it.

Checkmarx is constantly pushing the boundaries of Application Security 

Testing to make security seamless and simple for the world’s developers and 

security teams. As the AppSec testing leader, we deliver the unparalleled 

accuracy, coverage, visibility, and guidance our customers need to build 

tomorrow’s software securely and at speed.

2021 State of DevSecOps