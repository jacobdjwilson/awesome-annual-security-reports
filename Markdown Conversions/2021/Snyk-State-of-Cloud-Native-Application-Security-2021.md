State of Cloud Native Application SecurityHow cloud native adoption transforms the way organizations defend against security threats

99% of companies recognized  security as important to their  cloud native strategy



Success in the cloud native era is defined by an organization's ability to deliver new versions of software faster and more efficiently, which is reinforced by our survey results. Being able to deploy code to production faster and more easily manage those applications were the primary reasons for moving towards containerized infrastructure. However, as companies embrace cloud native technologies as part of their digital transformation, security is seen as a key factor to building successful platforms. While only 36% of respondents stated that security was one of the main reasons for moving their production applications into containers, 99% of respondents recognized security as an important element in their cloud native strategy. In addition, over 80% stated security is very important to them.

Snyk Report: State of Cloud Native Application Security \| 01
What are the main reasons for moving your applications into containers?How important is security to your cloud native strategy?Deployment velocity%68Ease of management%67Reduce costs%43Improved securityAttracting  talent%11%36Very
important83%Somewhat
important16%Not important1%As cloud native adoption increases, security needs to be built in as standard


Over 78% of production workloads  

are deployed as containers or 

serverless applications 







In total over 78% of production workloads are deployed as 

containers or serverless applications. Containers continue to 

be the dominant mechanism for cloud native application 

deployment, with nearly 60% of production workloads deployed 

in containers. Penetration of serverless technologies is now 

significant across all company sizes, and makes up more than 

a fifth (mean average) of all production workloads. Usage of 

cloud native technologies is strong across all company sizes, 

indicating that adoption is becoming mainstream. With over 

50% of respondent’s workloads also being deployed with some 

form of Infrastructure As Code, use of software\-driven 

infrastructure has increased alongside the container and 

serverless growth trends. Usage of these core technologies is 

one of the key indicators of cloud native transformation in 

general, and so we use these metrics throughout this report as 

indicative of the level of adoption within an organization. 


58%

21%

51%

Containers

Serverless

IaC

Snyk Report: State of Cloud Native Application Security \| 02

While 95% of respondents use 

Are your application deployments manual 

automation, only 33% fully 

automate their deployment 

pipeline








Deployment automation is one of the key tenets of 

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


or automated?



1\.7% \- Not 
automated at 
all

56% 
Partially

automated

18%

Entirely

automated

6% \- Not 
automated at 
all

High adoption

42%

Entirely

automated

Low adoption

76% 
Partially

automated

Snyk Report: State of Cloud Native Application Security \| 03

Download Snyk’s Infrastructure as 

Code Security Insights report for the 

trends on how companies are using 

and securing IaC today and common 

roadblocks to it’s wide spread use

Download now 


 Misconfiguration and known unpatched vulnerabilities were responsible for the greatest number of security incidents in cloud native environments

In contrast to where organizations are most concerned, we also asked about previous incidents that occured in production. The top two incident types by a distance were misconfiguration and known unpatched vulnerabilities, at 45% and 38% respectively. Over 56% experienced a misconfiguration or known unpatched vulnerability incident involving their cloud native applications.
Data leaks by insiders were more than twice as likely to have occurred in organizations with high levels of cloud native adoption, reinforcing that adopting zero trust principles becomes increasingly important in fully automated cloud based environments.Snyk Report: State of Cloud Native Application Security \| 04
Over half of respondents suffered from a misconfiguration or known vulnerabilities incident

MalwareMisconfigurationKnown unpatched vulnerabilitiesFailed auditSecret leaksData leaks by insiderHaven’t experienced any security incidents
Prefer not to answer10%14%50%43%45%33%21%14%18%17%18%7%14%21%18%21%High adoptionLow adoption1

2Incidents
1



2

Nearly 60% have increased 

security concerns since 

adopting cloud native




Adoption of cloud native technologies will 

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

adopting cloud native.



Decreased

15%

Hasn’t

changed

20%

Don’t

know

7%

Increased

58%

Snyk Report: State of Cloud Native Application Security \| 05


Misconfiguration is the area of most concern when moving to cloud native 
Cloud native platforms utilizing automated tooling will rely on credentials such as secrets and API tokens in order to operate, and necessitates a more decentralized approach to managing such access. The need for effective management of these kinds of artifacts is a key differentiator from the more centralized pre\-cloud era, and a major area of concern for operations teams transforming their infrastructure. Our survey showed that misconfigurations were the biggest area of increased concern, with over half of respondents stating it’s a bigger problem for them since moving to a cloud native platform. Despite secret leaks and data leaks not showing up highly in the actual incidents data, they feature strongly as areas of increased worry particularly among high adopters of cloud native technologies.

Snyk Report: State of Cloud Native Application Security \| 06
MalwareKnown unpatched vulnerabilitiesData leaks by insiderSecret leaksInsecure APIsMisconfigurationOwnership to handle/fixImpact of security on deployment velocityAbility to respond quickly to risks34%23%45%44%38%17%45%35%50%53%52%57%16%18%22%30%20%29%High adoptionLow adoptionAreas of concern
1

2Highly automated pipelines are twice as 
likely to be incorporate security testing 
throughout their development lifecycle 






Deployment automation unlocks scalable security controls





While building fully automated deployment pipelines can be challenging, once automation and 

processes are in place, they can create a virtuous cycle providing multiple integration points to 

enable further automation This is a key enabler for security testing. Companies with high levels of 

deployment automation were more than twice as likely to have adopted security testing at all 

points throughout the software development lifecycle, when compared to organizations with no 

automation. While companies of all sizes showed a clear preference to test in CI and earlier, 

enterprises were more likely to also be testing during later deployment and production stages. 

Despite testing in local development environments, such as an IDE, being a developer driven task, 

more automated organizations were nearly twice as likely to see their development teams adopt 

security early on in their workflows.


Snyk Report: State of Cloud Native Application Security \| 07


When do you do security testing?

Entirely kutomated

Not kutomated

kll

44%

24%
24%

40%

43%

16%
16%

45%

74%

28%
28%

60%

38%

32%
32%

33%

26%

8%
8%

22%

Local development eg 
Local development eg 
IDE’s and CLI tools
IDE’s and CLI tools

Source Code 
Source Code 
repositories
repositories

CI system
CI system

Deployment time
Deployment time

Production
Production

When do you do security testing?

Enterprise

Medium

Small

40%
40%

34
34

42%
42%

39%
39%

45%
45%

50%
50%

65%
64%

56%
56%

58%
58%

36%
36%

37%
37%

22%
22%

26%
25%

19%
19%

15%
15%

Local development eg 
IDE’s and CLI tools

Source Code 
repositories

CI system

Deployment time

Production

Snyk Report: State of Cloud Native Application Security \| 08


Continuous deployment 

empowers continuous testing


Once the use of security tooling is integrated throughout 

the software development lifecycle, this dramatically 

expands the possibilities for more regular security testing. 

Nearly 70% of respondents with high levels of deployment 

automation were able to test their security daily or more 

frequently. This was 17x more than respondents who had 

no deployment automation, and 60% of those only tested 

their security monthly or less frequently. This was 3x more 

than respondents who had full deployment automation.


Snyk Report: State of Cloud Native Application Security \| 09


How often do you do security 

testing?

When do you do security testing?

69%
40%

4%
24%

47%
43%

12%
44%

36%
16%

18%
42%

19%
60%

28%
60%

35%
73%

Local development eg 
Continuously or 
daily
IDE’s and CLI tools

Weekly
Source Code 
repositories

CI system
Monthly or less 
frequently

How often do you do security 

testing?
When do you do security testing?

Entirely Automated

Not Automated

All

Enterprise

Medium

Small

54%
40%

44%
34

34%
42%

17%
39%

12%
45%

20%
50%

29%
64%

44%
56%

46%
58%

Local development eg 
Continuously or 
daily
IDE’s and CLI tools

Weekly
Source Code 
repositories

CI system
Monthly or less 
frequently

Snyk Report: State of Cloud Native Application Security \| 10

Snyk Report: State of Cloud Native Application Security \| 01


Over 72% of fully automated teams find and fix critical vulnerabilities in under 1 week 


Snyk Report: State of Cloud Native Application Security \| 11
Testing faster leads to fixing faster. Over 72% of respondents with high levels of automation had an average time to fix vulnerabilities of less than one week, with 36% having an average of one day or less. Those with full automation were over 4x more likely to fix security issues in a day and over twice as likely to fix within a week. Automated testing is also a key enabler of visibility \- you can’t fix what you can’t see. This was reinforced by the 28% of organizations with low levels of automation who responded that they didn’t know how long it takes them to fix issues. 

1 day or less1 week2 weeks1 monthLonger than 1 monthDon't know8%36%24%45%20%6%12%10%8%28%3%8%Time fo fix critical sec issues37%Not automatedEntirely AutomatedNot AutomatedAutomation empowers 
shift left security



Companies who automate are twice as likely to implement security testing






Adoptijg a broad ajd deep approach to security practices throughout the software developmejt life cycle is key to a 

successful Cloud Native Applicatioj Security program. Our survey shows that compajies with higher levels of cloud 

jative automatioj have a greater adoptioj of security testijg techjiques. They tejd to focus more oj Static Applicatioj 

Security Testijg (SAST), scajjijg for vuljerabilities ij applicatioj depejdejcies with Software Compositioj Ajalysis 

(SCA), cojtaijer image testijg, ajd scajjijg ijfrastructure as code which are all techjiques which fit well ijto the 

paradigm of automatioj. Orgajizatiojs with fully automated deploymejt pipelijes are twice as likely to adopt SAST ajd 

SCA toolijg ijto their SDLC, ajd almost 3x as likely to add Dyjamic Applicatioj Security Testijg (DAST), although ij 

gejeral, dyjamic testijg isj’t as well adopted whej compared with static testijg. Policy compliajce testijg is still aj 

emergijg field, with ojly 23% of respojdejts havijg adopted it. 


Enterprises are more likely to adopt security practices, yet smaller 

companies with less established security practices are keeping up


Larger compajies ajd ejterprises are, of course, more likely to have the resources to ruj dedicated security teams 

so it shouldj’t come as a surprise to see ejterprises havijg the support to adopt formal Cloud Native Applicatioj 

Security Practices. While ij smaller orgajizatiojs the security fujctioj may be wholly owjed by ajother org, such 

as the ejgijeerijg teams, our survey shows that they are still able to keep up, particularly ij the static testijg 

space with over half of small orgajizatiojs adoptijg SAST, SCA ajd cojtaijer image scajjijg.




Snyk Report: State of Cloud Native Application Security \| 12


70%

60%

50%

40%

30%

20%

10%

0%

70%

60%

50%

40%

30%

20%

10%

0%

Watch this on\-demand webinar to 

learn tips for implementing security 

automation into modern development 

environments


Watch Now


Which software development life cycle 

security practices are you following?

Entirely Automated

Not Automated

All

Static code 

Code scanning for 

Dynamic 

analysis 

(SAST)

package dependency 

Application 

vulnerabilities 

Security 

Interactive 

Application 

Security 

Scanning 

Container 

Policy compliance 

infrastructure as 

image scanning

tools (Open Policy 

code (Terraform, 

Agent/Gatekeeper)

(SCA)



Testing (DAST)



Testing (IAST)

Kubernetes)

Which Software Development Life Cycle 

security practices are you following?

Enterprise

Medium

Small

Static code 

Code scanning for 

Dynamic 

analysis 

(SAST)

package dependency 

Application 

vulnerabilities 

Security 

Interactive 

Application 

Security 

Scanning 

Container 

Policy compliance 

infrastructure as 

image scanning

tools (Open Policy 

code (Terraform, 

Agent/Gatekeeper)

(SCA)



Testing (DAST)



Testing (IAST)

Kubernetes)

Snyk Report: State of Cloud Native Application Security \| 13


Securitj isn't just for the 
securitj team



Developers are adding security to their stack of hats





The move towards the concept of DevSecOps has accelerated in conjunction with 

adoption of cloud native technologies, as security shifts left in the software 

development lifecycle. Developers now have a pivotal role in ensuring that cloud 

native applications and infrastructure are secure since they increasingly contribute 

to the application, the infrastructure code, and workload deployment technologies. 

With this in mind, perception of security ownership provided interesting results in 

our survey set. While less than 10% of respondents in security roles believed 

developers were responsible for the security of their cloud native environment and 

applications, over 36% of developers stated that they were responsible. 



Traditionally, in a more siloed organization, the ownership of security would have 

sat firmly with the security team. Respondents in security roles are almost 3x 

more likely to attribute security ownership to the IT security team than 

respondents in development teams are. These indicators suggest that this 

ownership is being accepted by the development teams faster than the security 

teams are willing to let go of it. Security teams are still adjusting to the shifting 

responsibilities which transitioning to cloud native brings, and development teams 

are increasingly aware of their growing role in Cloud Native Application Security.

Snyk Report: State of Cloud Native Application Security \| 14


Who is primarily responsible for the security of 

your cloud native environment and applications?



Developer response

Security response

Application 

security team

14%

DevOps 
/DevSecOps

31%

DevOps 
/DevSecOps

33%

Developers

37%

No\-one 3%

No\-one 2%

IT 

security team

13%

IT 

security team

31%

Application 

security team

23%

Developers

10%

Snyk Report: State of Cloud Native Application Security \| 15


Developers and security both understand the importance of Cloud Native 

Application Security


The increased awareness of security in development teams was also reinforced by the survey results around security exposure 

concerns. Both developers and security professionals alike shared that switching to cloud native technologies had increased their 

security concerns. Developers were just as likely to be invested in good security outcomes as the security team \- good news for the 

adoption of DevSecOps principles which relies on shared security goals across the organization. 



Has switchijg to Cloud Native techjologies ijcreased 

or decreased your security exposure cojcerjs?





Developer respojse

Security respojse

Ijcreased

61%

Ijcreased

58%

Decreased

13%

Decreased

Decreased

13%
13%

Learn how Twilio’s Head of Product 

Security scaled through dev\-first 

security and devsecops in a cloud 

native environment



Watch Now



Hasj’t chajged

18%

Hasj’t chajged

21%

Snyk Report: State of Cloud Native Application Security \| 16


Snyk’s CNAS report shows clear movement in a positive direction. 99% of respondents recognize that security is important to their business strategy. That’s a world I want to live in
““Curious how Snyk can help?
Snyk is a developer\-first platform for building software securely. Learn more about how Snyk can help you secure cloud native applications across your IDEs, repos, containers, and pipelines.

Learn more