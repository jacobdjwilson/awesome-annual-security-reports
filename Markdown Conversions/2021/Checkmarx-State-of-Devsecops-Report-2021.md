CYBER SECURITY HUB 
2021 STATE OF 
DEVSECOPS
Sponsored by:
July 2021
2021 State of DevSecOps
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
them. Hence, its highly desirable to shift AST as 
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
2021 State of DevSecOps
3
Methodology
This report is based on a global online survey of application 
security professionals that took place during late May and 
June 2021\. Sixty percent are located in EMEA, followed by 
APAC and the Americas. Forty\-five percent hold director, 
VP, or C\-level titles.
How big is your application security team?
1\-5 
6\-10
11\-20
21\+
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
Do you plan on adding additional staff to your application security team within the next year?
Half of respondents plan to add more security staff, with 
the majority (38%) adding just one to five more. A non\-trivial 
factor is the shortage of security talent. 
Theres always a shortage of experienced people, and thats 
the challenge, said Stephen Gates, security evangelist and 
senior solutions specialist at Checkmarx. Thats a hurdle 
organizations are going to have to deal with even though 
they want to double the size of their staff.
No more additional staff planned
53%
23%
17%
7%
50%
38%
1\-5 more
5\-10 more
12%
2021 State of DevSecOps
4
Methodology
How do you measure a successful application security testing program?
\*Respondents could select more than one option
Nearly three\-quarters (72%) view vulnerability reduction as 
the key measure of success. Fewer (46%) are focused on 
particular vulnerabilities theyve identified previously. 
The scary statistic is that 44% measure success based 
on security vulnerability identification, not remediation. 
About the same number (42%) are achieving release 
speed and quality by integrating security testing and 
automation, typically in a CICD pipeline that is highly 
automated otherwise.
Three in 10 have reduced bug bounties because they likely 
dont want to advertise the fact that they have software 
vulnerabilities, and they dont want people hacking their 
systems to find bugs. On an industry level, companies 
generally are decreasing bug bounties.
Half of respondents are providing the CISO with a PDF report 
of security scan findings, some of which include custom 
charts. The people who are not providing the CISO with any 
report may lack the necessary tools or time to do it, or the 
company may not have a CISO in the first place.
Overall reduction of all types of vulnerabilities
Specific reduction of vulnerabilities (such as SQL 
injection andor XSS)
Number of vulnerabilities identified (but not fixed)
Increased velocity of releases with application security 
testing integrated and automated
Decrease in bug bounty efforts
75%
0%
72%
46%
42%
44%
30%
What kind of reporting is given to the CISO? 
\*Respondents could select more than one option
50%
PDF report 
with findings
32%
No report 
given
34%
Custom charts created 
by the AppSec team
4%
Other
2021 State of DevSecOps
5
Methodology
What is your biggest frustration with application security testing?
\*Respondents could select more than one option
There are several frustrations with application security 
testing, and one of the most prominent is testing too late in 
the life cycle (43%). A quick vulnerability scan is not enough 
to address all application vulnerabilities, and it often results 
in interpersonal conflicts between developers and security 
since it requires developers to revisit code after theyve 
moved onto another project. From an overhead perspective, 
its more time\-consuming and expensive.
When people say a vulnerability is being identified too late, 
is a clear indication that integration and automation of 
AST solutions within their development pipelines is less than 
perfect, said Gates. Then, just before deployment, they 
launch a scan and then say, Oh wow, we have lots more 
work to remediate the vulnerabilities weve discovered.
An equal number (43%) are frustrated by their inability 
to interpret the scan findings, how risky a suspected 
vulnerability may be, and how to quickly fix it. Theres a gap 
between understanding a vulnerability and its remediation.
A related issue is tracking the vulnerability status to make 
sure its actually being fixed (36%). Teams often lack the 
tools or tool integration they need to track the status of 
vulnerability remediation in a quick and easy way.
Also at 36% are false positives, which waste precious time. 
Alternatively, when false positives are too frequent, people 
tend to ignore them (which is called alert fatigue). Alert 
fatigue is not only very real, but also potentially dangerous 
because some true positives may be ignored.
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
0%
43%
43%
36%
36%
29%
25%
1%
Respondents (%)
2021 State of DevSecOps
6
Time to market pressure necessitates automated AST, but it 
also helps ensure code quality. Those with CICD pipelines 
(36%) are automating or plan to automate security testing 
as part of a larger automation strategy since CICD and 
automation go hand in hand. Another 15% are relying on 
SCM integration.
Source code management integration is something people 
either dont know about or they dont have the correct 
application security testing tools that can integrate directly 
within their SCM tools of choice, said Gates. Scan early and 
scan often is the way to work. Within the SCM is the best 
location to launch scans since its the often the farthest left 
you can go.
Automation is a maturity issue that requires AST integration 
within the dev tools in use, which some organizations clearly 
lack (31%). However, modern AST solutions can easily be 
intergrated and fully automated.
Methodology
How are you currently (or planning) automating application security testing?
36%
31%
18%
15%
CICD tooling (Jenkins, 
TeamCity, CircleCI, etc.)
Do not have automation
Nightly Weekly cronjobs
SCM integration 
(Webhooks on 
pull request pushes)
Half the respondent base considers a bug tracking tool 
like Jira the best place to consume application security 
results because they already have the tool in place, with 
both develops and security already using it. A distant 
second (20%) is in an IDE, because modern IDEs show 
coding errors in real time, though they wont catch 
everything because they were not designed specifically to 
identify application vulnerabilities.
About the same number (19%) prefer a pullmerge request.
If you automate the pull request, then you can actually 
get the results right back in the SCM tool youre working 
on, and whats nice about that is its very fast, said Gates. 
Developers have the opportunity to remediate quickly 
when theyre sitting in a branch of code or working on it. Its 
just expected.
Where is the best place developers consume application security results?
49%
20%
19%
12%
Bug tracking tool
In their IDE
In the pull merge request
PDF report
2021 State of DevSecOps
7
Two\-thirds of survey participants (67%) are doing API 
testing because its becoming an increasing threat. In 
fact, Gartner predicts that APIs will become the most 
popular attack vector by 2022\. Another reason API testing 
is popular is because modern applications have a lot of 
dependencies. Todays applications rely on a number of 
outside functions and data to operate as intended. Those 
dependencies, if they contain security flaws, may infect 
an application. In addition, cloud native development and 
the use of microservices are growing exponentially, so API 
vulnerabilities are of particular concern. 
Static application security testing (SAST) is more than 
twice as popular (44%) as dynamic application security 
testing (DAST, at 21%) because DAST doesnt always fit well 
into modern application development practices, which 
emphasize speed.When organizations start decomposing applications 
into microservices and using containersor building new 
applications with containersthey eventually realize they 
need special tooling and updated practices since traditional 
application security tooling and practices wont work. Each 
container represents an individual attack surface, unlike a 
monolithic application. The 36% using container scanning 
realize this.
Finally, the use of software composition analysis (SCA) tools 
is on the rise because of open source security concerns. 
Todays applications use more third\-party commercial and 
open source components and libraries than ever before 
because of time to market mandates and an increase in 
application complexity. Without SCA, it can be more difficult 
to pinpoint open source vulnerabilities and license risks.
Methodology
What type of security testing are you performing?
\*Respondents could select more than one option
70%
0%
67%
44%
31%
36%
21%
14%
11%
Respondents (%)
API
SAST
Container scanning
SCA
DAST
IAST
Fuzzing
2021 State of DevSecOps
8
Despite the increased use of open source code, 58% said 
theyre not using open source security testing tools.
Thats a concern because of the increase in the amount of 
open source modules, packages, and libraries these teams 
are using, said Gates.
Methodology
Do you use any open source tooling specifically for finding security vulnerabilities?
Most respondents (62%) chose better integrations as the top 
improvement theyd like to see because of all the friction a 
lack of integration causes. Insufficient integration precludes 
visibility across tooling and it prevents teams from achieving 
the level of automation they need to improve release 
velocity and product quality. Also causing friction are less\-
than\-optimal user experiences (52%). Faster scans (50%) and 
fewer false positives (45%) are also about speed.
What improvements in application security testing would you like to see?
\*Respondents could select more than one option
Better integrations
User interface experience
Faster scans
Less false positives
More application security offerings
More accurate queries out of the box
65%
0%
62%
52%
45%
50%
39%
30%
No
58%
42%
Yes
Respondents (%)
2021 State of DevSecOps
9
Jira tickets are the top means of communicating with 
developers (48%) since so many DevOps teams already use it.
Integration and automation into Jira systems is probably 
vastly desired because of the need for speed, which extends 
to triage, troubleshooting, and remediation, said Gates. 
Theres a desire to have automation and integration with 
the actual scans to open and close tickets automatically.
Email is an antiquated way of communicating information 
about code issues, but its still popular among 31% of 
respondents since everyone uses email but not everyone 
uses Jira. While email can accommodate all the information 
a developer will need, unlike Slack, emails are not a real\-
time communication medium, and they can get lost easily 
in a universe of other emails. It can also be difficult to search 
through emails to find out what the status of remediation is.
Group meetings have the benefit of getting everyone on the 
same page (13%), but they take time away from other day\-
to\-day tasks. 
Another scary statistic is that two\-thirds of respondents (66%) 
lack a security champion, when thats such an important 
role. The security champion evangelizes security within the 
organization, which helps create a cyber\-aware culture. 
Since theyre security experts and also good communicators, 
theyre a good resource for mentoring developers. The 
security champion is the designated go\-to person 
developers and others can tap when they have a security\-
related question.
Do you currently use a Security Champion type of model within your organization?
Methodology
66%
No
34%
Yes
50%
0%
48%
31%
6%
13%
2%
Respondents (%)
Jira tickets
Emails
Group meetings
Slack messages
Other
How do you communicate with developers on bugs found?
2021 State of DevSecOps
10
Wikis are alive and well in a security context. Nearly half 
of survey participants (47%) are using a wiki as the primary 
vehicle for security awareness, with just slightly fewer (44%) 
saying they use instructional videos.
Fewer still are those using the Open Web Application Security 
Project (OWASP), an online community providing freely 
available web application security articles, methodologies, 
documentation, tools, and technology. Then again, OWASP is 
specific to web application security, and the guidelines tend 
to be quite general.
About one\-third have integrated real\-time training, which 
helps accelerate application release speed and quality. Unlike 
videos, which take time away from coding, real\-time training 
teaches developers application security within the context of 
writing code. If a developer doesnt know how to remediate 
an issue, a five\-minute tutorial will often solve the problem.
What do you currently do for security awareness?
\*Respondents could select more than one option
Subject matter expertise tops the list (61%) of what 
respondents think security professionals will need to have in 
the future. Security professionals tend to be driven to upskill 
themselves because they want to advance their careers, 
often into the role of a security champion or CISO.
However, to become an effective security champion or CISO, 
they need to have technical expertise and soft skills (56%), 
such as communication and collaboration, because the role 
interacts with other roles in the company. 
Advanced programming skills (52%) does not mean that 
security professionals are morphing into developers (though 
some may choose to do so). Its more about understanding 
the application side of application security as much as the 
security side of application security and being able to tell a 
developer what to do. 
AI and machine learning are also considered important 
knowledge to have (48%), given their growing popularity 
throughout enterprises. At first, enterprises raced to implement 
AI and ML to reap the benefits, but more realize now that they 
must also manage the potential risks not only with the help of 
data scientists, but security professionals as well.
Meanwhile, IoT and blockchain use is emerging, as reflected 
by the 35%.
What skills will be important for security professionals to have in the future?
\*Respondents could select more than one option
Methodology
61%
Subject matter 
expertise
56%
Soft skills like communication 
and collaboration
52%
Advanced 
programming
48%
AIML
35%
IoT
blockchain
1%
Other
47%
Internal 
wiki center
44%
Instructional
videos
39%
OWASP
34%
Just\-in\-time training solution 
(such as Checkmarx Codebashing)
6%
Other
2021 State of DevSecOps
11
Its encouraging that 64% of respondents consider the quality 
of application testing more important than speed, because 
it speaks to the desire to provide higher quality software and 
avoid the headaches of a customer or bad actor discovering 
security issues in production.
The result may seem counterintuitive based on some of the 
other survey responses that demonstrate a desire to remove 
obstacles to speed. However, given the choice between 
speed and quality, quality prevails because it equates to 
more secure code.
Is the speed of an application security testing scan more valuable than the quality of results?
Application security continues to rise in importance 
because it represents legal, regulatory, and brand issues. 
End users expect applications to be of high quality, which 
includes security. Its not enough to simply build and deliver 
applications faster. Speed and quality must go hand in hand. 
As always, individual respondent companies are at different 
stages of maturity because speeding delivering and 
increasing code security simultaneously is a journey. Moving 
from DevOps to DevSecOps helps.
Methodology
No
64%
36%
Yes
Conclusion
2021 State of DevSecOps
2021 State of DevSecOps
The Cyber Security Hub is an online news 
source for global cyber security professionals 
and business leaders who leverage technology 
and services to secure the entire perimeter in 
their enterprise. 
Were dedicated to providing the latest industry 
news, thought leadership and analysis in the 
cyber security space. Cyber Security Hubs expert 
commentary, tools and resources are developed 
through obtaining data and interviewing end 
users and analysts throughout the industry to 
deliver practical and strategic advice. 
Our editorial team surveys and monitors the 
latest trends in cyber security and creates news 
articles, market reports, case studies and in\-
depth analysis for a captive audience consisting 
of C\-Level executives, VPs and directors of cyber 
security and information technology. 
Cyber Security Hub Team
Facebook:
CSHubIQPC
Twitter:
CSHubUSA
LinkedIn:
CSHub Enterprise
Security Professionals
Dorene Rettas 
Managing Director
Dorene.Rettas@CSHub.com
Tilak Antony
Director of IQPC
Digital Partnerships
Tilak.Antony@iqpc.com 
Seth Adler
Editor\-in\-Chief
Seth.Adler@iqpc.co.uk
Social Media Information
About Cyber Security Hub 
Desiree Santiago
Marketing Manager
Desiree.Santiago@cshub.com
Imran Shafi
Sales Director
Imran.shafi@iqpc.com
Joshua Snead
North America Sales Director
Joshua.Snead@iqpc.com
The world runs on code.
We secure it.
Checkmarx is constantly pushing the boundaries of Application Security 
Testing to make security seamless and simple for the worlds developers and 
security teams. As the AppSec testing leader, we deliver the unparalleled 
accuracy, coverage, visibility, and guidance our customers need to build 
tomorrows software securely and at speed.
2021 State of DevSecOps
 Visit CSHub.com for more information from cyber 
security leaders for the cyber security community