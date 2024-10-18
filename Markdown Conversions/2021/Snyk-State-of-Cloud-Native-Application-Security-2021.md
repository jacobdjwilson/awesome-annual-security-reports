State of Cloud Native 
Application Security
How cloud native adoption transforms the way 
organizations defend against security threats99% of companies recognized 
security as important to their 
cloud native strategySuccess in the cloud native era is defined by an organization's 
ability to deliver new versions of software faster and more 
efficiently, which is reinforced by our survey results. Being able 
to deploy code to production faster and more easily manage 
those applications were the primary reasons for moving 
towards containerized infrastructure. However, as companies 
embrace cloud native technologies as part of their digital 
transformation, security is seen as a key factor to building 
successful platforms. While only 36% of respondents stated 
that security was one of the main reasons for moving their 
production applications into containers, 99% of respondents 
recognized security as an important element in their cloud 
native strategy. In addition, over 80% stated security is very 
important to them.Snyk Report: State of Cloud Native Application Security \| 01
What are the main reasons for moving your 
applications into containers?
How important is security to your cloud 
native strategy?
Deployment
velocity
%
68
Ease of
management
%
67
Reduce
costs
%
43
Improved
security
Attracting 
talent
%
11
%
36
Very
important
83%
Somewhat
important
16%
Not 
important
1%
As cloud native adoption increases, 
security needs to be built in as standardOver 78% of production workloads 
are deployed as containers or 
serverless applicationsIn total over 78% of production workloads are deployed as 
containers or serverless applications. Containers continue to 
be the dominant mechanism for cloud native application 
deployment, with nearly 60% of production workloads deployed 
in containers. Penetration of serverless technologies is now 
significant across all company sizes, and makes up more than 
a fifth (mean average) of all production workloads. Usage of 
cloud native technologies is strongacross all company sizes, 
indicating that adoption is becoming mainstream. With over 
50% of respondents workloads also being deployed with some 
form of Infrastructure As Code, use of software\-driven 
infrastructure has increased alongside the container and 
serverless growth trends. Usage of these core technologies is 
one of the key indicators of cloud native transformation in 
general, and so we use these metrics throughout this report as 
indicative of the level of adoption within an organization. 
Snyk Report: State of Cloud Native Application Security \| 02
Containers
Serverless
IaC
58%
21%
51%
While 95% of respondents use 
automation, only 33% fully 
automate their deployment 
pipelineDeployment automation is one of the key tenets of 
cloud native practices, enabling development 
velocity. Our survey showed that over 95% of 
respondents were using some level of automation 
with almost a third having an entirely automated 
deployment pipeline. By comparing the upper and 
lower quartiles of cloud native production usage 
(high levels of adoption vs low levels of adoption), 
we can see that organizations that show high levels 
of cloud native adoption are over twice as likely to 
have an entirely automated deployment process 
than organizations with low cloud native adoption.
Snyk Report: State of Cloud Native Application Security \| 03
1\.7% \- Not 
automated at 
all
42%
Entirely
automated
56%
Partially
automated
76%
Partially
automated
Are your application deployments manual 
or automated?Download Snyks Infrastructure as 
Code Security Insights report for the
trends on how companies are using 
and securing IaC today and common 
roadblocks to its wide spread use
Low adoption
18%
Entirely
automated
6% \- Not 
automated at 
all
High adoption
Download now 
 Misconfiguration and known 
unpatched vulnerabilities were 
responsible for the greatest 
number of security incidents in 
cloud native environmentsIn contrast to where organizations are most concerned, we also asked about 
previous incidents that occured in production. The top two incident types by a 
distance were misconfiguration and known unpatched vulnerabilities, at 45% and 
38% respectively. Over 56% experienced a misconfiguration or known unpatched 
vulnerability incident involving their cloud native applications.
Data leaks by insiders were more than twice as likely to have occurred in 
organizations with high levels of cloud native adoption, reinforcing that adopting 
zero trust principles becomes increasingly important in fully automated cloud 
based environments.
Snyk Report: State of Cloud Native Application Security \| 04
Over half of respondents suffered from a 
misconfiguration or known vulnerabilities 
incidentMalware
Misconfiguration
Known unpatched 
vulnerabilities
Failed audit
Secret leaks
Data leaks 
by insider
Havent 
experienced any 
security 
incidents
Prefer not 
to answer
10%
14%
50%
43%
45%
33%
21%
14%
18%
17%
18%
7%
14%
21%
18%
21%
High adoption
Low adoption
12
Incidents
Nearly 60% have increased 
security concerns since 
adopting cloud nativeAdoption of cloud native technologies will 
undoubtedly change the security posture 
of your overall application. While the core 
security principles remain constant, as 
with all emerging ecosystems the best 
practice is still being defined, driving fresh 
concern as teams navigate through 
unfamiliar landscapes. Our survey shows 
organizations are nearly 4x more likely to 
have increased rather than decreased 
concerns over their security posture since 
adopting cloud native.Snyk Report: State of Cloud Native Application Security \| 05
12
Increased
58%
Decreased
15%
Hasnt
changed
20%
Dont
know
7%
Misconfiguration is the 
area of most concern when 
moving to cloud native 
Cloud native platforms utilizing automated tooling will rely on credentials such as 
secrets and API tokens in order to operate, and necessitates a more decentralized 
approach to managing such access. The need for effective management of these 
kinds of artifacts is a key differentiator from the more centralized pre\-cloud era, 
and a major area of concern for operations teams transforming their 
infrastructure. Our survey showed that misconfigurations were the biggest area of 
increased concern, with over half of respondents stating its a bigger problem for 
them since moving to a cloud native platform. Despite secret leaks and data leaks 
not showing up highly in the actual incidents data, they feature strongly as areas 
of increased worry particularly among high adopters of cloud native technologies.Snyk Report: State of Cloud Native Application Security \| 06
Malware
Known unpatched 
vulnerabilities
Data leaks by 
insider
Secret 
leaks
Insecure 
APIs
Misconfigur
ation
Ownership to 
handlefix
Impact of 
security on 
deployment 
velocity
Ability to 
respond 
quickly to 
risks
34%
23%
45%
44%
38%
17%
45%
35%
50%
53%
52%
57%
16%
18%
22%
30%
20%
29%
High adoption
Low adoption
Areas of concern
12
Deployment automation unlocks scalable security controlsSnyk Report: State of Cloud Native Application Security \| 07
Highly automated pipelines are twice as 
likely to be incorporate security testing 
throughout their development lifecycleWhile building fully automated deployment pipelines can be challenging, once automation and 
processes are in place, they can create a virtuous cycle providing multiple integration points to 
enable further automation This is a key enabler for security testing. Companies with high levels of 
deployment automation were more than twice as likely to have adopted security testing at all 
points throughout the software development lifecycle, when compared to organizations with no 
automation. While companies of all sizes showed a clear preference to test in CI and earlier, 
enterprises were more likely to also be testing during later deployment and production stages. 
Despite testing in local development environments, such as an IDE, being a developer driven task, 
more automated organizations were nearly twice as likely to see their development teams adopt 
security early on in their workflows.
Snyk Report: State of Cloud Native Application Security \| 08
Local development eg 
IDEs and CLI tools
Source Code 
repositories
CI system
Deployment time
Production
When do you do security testing?
When do you do security testing?
Entirely Automated
Not Automated
All
Enterprise
Medium
Small
40%
34
42%
39%
45%
50%
64%
56%
58%
36%
37%
22%
25%
19%
15%
Local development eg 
IDEs and CLI tools
Source Code 
repositories
CI system
Deployment time
Production
24%
16%
28%
32%
8%
40%
34
42%
39%
45%
50%
65%
56%
58%
36%
37%
22%
26%
19%
15%
Local development eg 
IDEs and CLI tools
Source Code 
repositories
CI system
Deployment time
Production
40%
24%
44%
45%
16%
43%
60%
28%
74%
33%
32%
38%
22%
8%
26%
Continuous deployment 
empowers continuous testing
Snyk Report: State of Cloud Native Application Security \| 09
Once the use of security tooling is integrated throughout 
the software development lifecycle, this dramatically 
expands the possibilities for more regular security testing. 
Nearly 70% of respondents with high levels of deployment 
automation were able to test their security daily or more 
frequently. This was 17x more than respondents who had 
no deployment automation, and 60% of those only tested 
their security monthly or less frequently. This was 3x more 
than respondents who had full deployment automation.
Snyk Report: State of Cloud Native Application Security \| 01
Local development eg 
IDEs and CLI tools
Source Code 
repositories
CI system
When do you do security testing?
When do you do security testing?
40%
34
42%
39%
45%
50%
64%
56%
58%
Local development eg 
IDEs and CLI tools
Source Code 
repositories
CI system
40%
24%
43%
44%
16%
42%
60%
28%
73%
Snyk Report: State of Cloud Native Application Security \| 10
Continuously or
daily
Weekly
Monthly or less 
frequently
How often do you do security 
testing?
How often do you do security 
testing?
Entirely Automated
Not Automated
All
Enterprise
Medium
Small
54%
44%
34%
17%
12%
20%
29%
44%
46%
Continuously or 
daily
Weekly
Monthly or less 
frequently
47%
4%
69%
18%
36%
12%
35%
60%
19%
Over 72% of fully automated teams find and fix 
critical vulnerabilities in under 1 weekSnyk Report: State of Cloud Native Application Security \| 11
Testing faster leads to fixing faster. Over 72% of respondents with high levels of 
automation had an average time to fix vulnerabilities of less than one week, with 36% 
having an average of one day or less. Those with full automation were over 4x more 
likely to fix security issues in a day and over twice as likely to fix within a week. 
Automated testing is also a key enabler of visibility \- you cant fix what you cant see. 
This was reinforced by the 28% of organizations with low levels of automation who 
responded that they didnt know how long it takes them to fix issues.1 day or less
1 week
2 weeks
1 month
Longer than 1 month
Don't know
8%
36%
24%
45%
20%
6%
12%
10%
8%
28%
3%
8%
Time fo fix critical 
sec issues
37%
Not automated
Entirely Automated
Not Automated
Companies who automate are twice as likely to implement security testingSnyk Report: State of Cloud Native Application Security \| 12
Automation empowers 
shift left securityAdopting a broad and deep approach to security practices throughout the software development life cycle is key to a 
successful Cloud Native Application Security program. Our survey shows that companies with higher levels of cloud 
native automation have a greater adoption of security testing techniques. They tend to focus more on Static Application 
Security Testing (SAST), scanning for vulnerabilities in application dependencies with Software Composition Analysis 
(SCA), container image testing, and scanning infrastructure as code which are all techniques which fit well into the 
paradigm of automation. Organizations with fully automated deployment pipelines are twice as likely to adopt SAST and 
SCA tooling into their SDLC, and almost 3x as likely to add Dynamic Application Security Testing (DAST), although in 
general, dynamic testing isnt as well adopted when compared with static testing. Policy compliance testing is still an 
emerging field, with only 23% of respondents having adopted it. 
Enterprises are more likely to adopt security practices, yet smaller 
companies with less established security practices are keeping up
Larger companies and enterprises are, of course, more likely to have the resources to run dedicated security teams 
so it shouldnt come as a surprise to see enterprises having the support to adopt formal Cloud Native Application 
Security Practices. While in smaller organizations the security function may be wholly owned by another org, such 
as the engineering teams, our survey shows that they are still able to keep up, particularly in the static testing 
space with over half of small organizations adopting SAST, SCA and container image scanning.Snyk Report: State of Cloud Native Application Security \| 13
Which software development life cycle 
security practices are you following?
Static code 
analysis 
(SAST)
Code scanning for 
package dependency 
vulnerabilities 
(SCA)Dynamic 
Application 
Security 
Testing (DAST)Interactive 
Application 
Security 
Testing (IAST)
Scanning 
infrastructure as 
code (Terraform, 
Kubernetes)
Container 
image scanning
Policy compliance 
tools (Open Policy 
AgentGatekeeper)
10%
0%
20%
30%
40%
50%
60%
70%
Which Software Development Life Cycle 
security practices are you following?
Static code 
analysis 
(SAST)
Code scanning for 
package dependency 
vulnerabilities 
(SCA)Dynamic 
Application 
Security 
Testing (DAST)Interactive 
Application 
Security 
Testing (IAST)
Scanning 
infrastructure as 
code (Terraform, 
Kubernetes)
Container 
image scanning
Policy compliance 
tools (Open Policy 
AgentGatekeeper)
10%
0%
20%
30%
40%
50%
60%
70%
Watch this on\-demand webinar to 
learn tips for implementing security 
automation into modern development 
environments
Watch Now
Entirely Automated
Not Automated
All
Enterprise
Medium
Small
Developers are adding security to their stack of hatsThe move towards the concept of DevSecOps has accelerated in conjunction with 
adoption of cloud native technologies, as security shifts left in the software 
development lifecycle. Developers now have a pivotal role in ensuring that cloud 
native applications and infrastructure are secure since they increasingly contribute 
to the application, the infrastructure code, and workload deployment technologies. 
With this in mind, perception of security ownership provided interesting results in 
our survey set. While less than 10% of respondents in security roles believed 
developers were responsible for the security of their cloud native environment and 
applications, over 36% of developers stated that they were responsible.Traditionally, in a more siloed organization, the ownership of security would have 
sat firmly with the security team. Respondents in security roles are almost 3x 
more likely to attribute security ownership to the IT security team than 
respondents in development teams are. These indicators suggest that this 
ownership is being accepted by the development teams faster than the security 
teams are willing to let go of it. Security teams are still adjusting to the shifting 
responsibilities which transitioning to cloud native brings, and development teams 
are increasingly aware of their growing role in Cloud Native Application Security.
Snyk Report: State of Cloud Native Application Security \| 14
Security isn't just for the 
security teamSnyk Report: State of Cloud Native Application Security \| 15
Who is primarily responsible for the security of 
your cloud native environment and applications?DevOps
DevSecOps
31%
DevOps
DevSecOps
33%
Application 
security team
14%
Application 
security team
23%
IT 
security team
13%
IT 
security team
31%
No\-one 3%
No\-one 2%
Developers
37%
Developers
10%
Developer response
Security response
Developers and security both understand the importance of Cloud Native 
Application Security
The increased awareness of security in development teams was also reinforced by the survey results around security exposure 
concerns. Both developers and security professionals alike shared that switching to cloud native technologies had increased their 
security concerns. Developers were just as likely to be invested in good security outcomes as the security team \- good news for the 
adoption of DevSecOps principles which relies on shared security goals across the organization.Snyk Report: State of Cloud Native Application Security \| 16
Hasnt changed
18%
Hasnt changed
21%
Decreased
13%
Has switching to Cloud Native technologies increased 
or decreased your security exposure concerns?Security response
Developer response
Learn how Twilios Head of Product 
Security scaled through dev\-first 
security and devsecops in a cloud 
native environmentWatch NowIncreased
61%
Decreased
13%
Increased
58%
Decreased
13%
Snyks CNAS report shows clear 
movement in a positive direction.99% of 
respondents recognize that security is 
important to their business strategy.
Thats a world I want to live in


Curious how Snyk can help?
Snyk is a developer\-first platform for building software securely. Learn more about how Snyk can help 
you secure cloud native applications across your IDEs, repos, containers, and pipelines.Learn more