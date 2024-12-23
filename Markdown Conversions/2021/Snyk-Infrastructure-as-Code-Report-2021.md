# Infrastructure as Code Security Insights
## Table of Contents
- [Introduction](#introduction)
- [Current IaC Practices](#current-iac-practices)
- [Full automation:](#full-automation)
- [Less than full automation:](#less-than-full-automation)
- [Only post-deployment checks:](#only-post-deployment-checks)
- [Does Speed Equate to Safety?](#does-speed-equate-to-safety)
- [Current IaC Security Practices](#current-iac-security-practices)
- [So what is standing in the way of making a change?](#so-what-is-standing-in-the-way-of-making-a-change)
- [Infrastructure Remediation](#infrastructure-remediation)
- [Who Holds Responsibility for IaC Security?](#who-holds-responsibility-for-iac-security)
- [Snyk Infrastructure as Code: Find and fix configuration security issues the way cloud native experts do.](#snyk-infrastructure-as-code-find-and-fix-configuration-security-issues-the-way-cloud-native-experts-do)
- [Survey Methodology](#survey-methodology)

Cloud native applications are more than just the 
code developers create - today’s applications include 
infrastructure as code (IaC) that dictate how the 
applications are setup on cloud infrastructure and how 
containerized applications will run on Kubernetes. The 
use of IaC allows for faster, repeatable deployments, 
but its usage also increases the burden on developers 
to secure not only their code, but also the infrastructure 
configuration, in addition to code dependencies and 
containers. 
In this survey, Snyk sought to take stock of how IaC is 
being deployed by companies both large and small. 
Feedback from a wide range of roles in these companies 
went into our outlook on the state of IaC, highlighting 
the value of IaC, as well as also roadblocks to its 
widespread use and what we can do to overcome them. 
While our survey shows that many organizations have 
not coalesced on one “right” way to use IaC or who 
should be responsible for writing and maintaining it, we 
did find that respondents who are taking advantage of 
automated security testing for their IaC definitions are 
finding and fixing misconfigurations faster than their 
peers. The high performers in our survey are finding and 
fixing issues in their IaC definitions within a single day; 
whereas the lower performers take more than a week 
to realize there is a security issue and then then up 
to 2 more days to fix it.

## Introduction
Respondents performing automated 
security testing as part of their release 
pipelines were faster to find and fix 
vulnerabilities 
Teams with fully 
automated security 
checks
Teams with no or only 
partially automated 
security checks
Teams that only 
check security 
after deployment
76%
59%
38%
KEY TAKE AWAY
Can you fix an issue in under 1 day?
SEE SNYK IAC IN ACTION
The benefits to speed and reliability when everything is in code 
and automated can be immense. But the benefits do come with 
a cost, namely an increasing burden on developers to secure 
not just their own code but it’s dependencies, containers, and 
now, the infrastructure configuration. To start our research, we 
first explored what companies were taking on the challenge of 
implementing IaC and which tools they’re currently using as they 
develop best practices. 
We found that many companies are only starting out on their IaC 
journey, with 63% just beginning to explore the technology and 
only 7% stating they’ve implemented IaC to the best of current 
industry capabilities. While there are many tools either in use or 
being considered, 71% would prefer to standardize on a common 
toolset / workflow across all IaC configuration types and formats.

## Current IaC Practices
63%
of companies are just 
starting out
7%
of companies are 
implementing the best of 
current industry capabilities
In use today
AWS CloudFormation 
36%
Azure Resource 
Manager
30%
Kubernetes (incl. YAML, 
JSON and Helm)
Considering for the future 
Cloud SDKs (AWS CDK, 
Azure SDKs)
AWS CloudFormation
Kubernetes (incl. YAML, 
JSON and Helm)
25%
Ansible
Azure Resource Manager
17%
Terraform 
Google Could 
Deployment Manager
14%
Docker Compose
Other Kubernetes tools
14%
Google Could 
Deployment Manager
Serverless Framework
14%
14%
26%
24%
22%
18%
18%
16%
The opportunity is still wide open for most organizations to lay a firm foundation and implement the right tools and 
practices before widely adopting IaC.
SNYK RESEARCH REPORT
Infrastructure as Code Security Insights 
3
We looked at how three different clusters of 
respondents to our survey fared when it comes to 
finding and fixing configuration issues that arise 
from using infrastructure as code:
These respondents said they always performed 
automated security testing as part of their release 
pipelines.
It may come as no surprise that the fully automated 
group outperformed both of the other groups at 
both discovering and fixing issues. When it comes to 
finding issues, the high performers were able to dis-
cover issues in less than a day roughly twice as often 
as respondents in the other two groups. And the fully 
automated cluster was able to fix issues quickly, in 
less than half a day, over 60% more often than either 
of the other clusters.
There were differences at the other end of the 
responses, too. The two lower performing clusters 
took 1 week or more to discover IaC issues in over 
half their cases, where the fully automated cluster 
only took that long 30% of the time. Fixing the issues 
is where the cluster that only runs post-deployment 
checks really suffered. They were only able to fix 
these IaC issues in less than a day half as often as the 
fully automated respondents, and in 62% of the cases 
it took longer than a day to implement the fix.

## Full automation:
This cluster includes respondents who have no auto-
mation up to those who have partial automation of 
security checks.

## Less than full automation:
This cluster may use some automation, but they 
only perform checks after infrastructure is deployed, 
either via audit tools, pen testing, or investigating 
security incidents

## Only post-deployment checks:
Can you detect an issue in less than 1 day?
How often do you go 1 week or 
longer before finding an issue?
Can you fix an issue in less than 1 day?
How often does it take you over a 
day to fix an issue?
Fully 
automated
Fully 
automated
Fully 
automated
Fully 
automated
Not 
automated
Not 
automated
Not 
automated
Not 
automated
Checks after 
deployment
Checks after 
deployment
Checks after 
deployment
Checks after 
deployment
34%
30%
76%
25%
14%
54%
59%
41%
18%
60%
38%
62%
4
Currently, modern applications deploy 
automatically on infrastructure created and 
configured via code. As a result, security so often 
takes a back seat to a speedy deployment, meaning 
configuration issues are not uncovered until after 
these applications have been deployed. Even 
Gartner* states, “By 2025, 70% of attacks against 
containers will be from known vulnerabilities 
and misconfigurations that could have been 
remediated.” 
Yet, all this does not necessarily mean speed is 
inherently risky when it comes to IaC. In fact, the 
automated testing and release gates that are in 
place for other forms of code can be used with 
IaC and help make security best practices part of 
the development and release process. The highest 
performers in this survey - those who are both 
finding and fixing configuration issues fastest -
 are already doing exactly that. 

## Does Speed Equate to Safety?
70%
By 2025
of attacks against containers will be from 
known vulnerabilities and misconfigurations 
that could have been remediated.
Gartner, 2020
No CI testing
Sometimes
Usually
Always
40%
7%
27%
24%
Do you include IaC security 
tests in your CI pipeline
*Gartner Magic Quadrant for Application 
Security Testing; April 2020
5
SNYK RESEARCH REPORT
Infrastructure as Code Security Insights 
While the highest performers are finding and fixing security issues as part of their release 
pipelines, this type of automated testing is still nascent when it comes to security testing. 
Of those surveyed, 60% said their current workflow for IaC and configuration code does 
go through continuous integration (CI) testing, but security checks are not always part of 
those tests. Only 32% of respondents include security checks in their pipelines. In fact, most 
security issues are still being discovered after deployment, through pen testing, audits, and 
investigating security incidents. For those who are only using these post-deployment checks, 
it takes a week or more to discover a security issue in half the cases and over a day to fix 
those issues in nearly 2/3 of the cases. All in all, that’s potentially 9 days of running with a 
security vulnerability versus less than one day for the highest performers.

## Current IaC Security Practices
How do you find out about security 
issues in your configurations and IaC?
45%
43%
35%
33%
32%
21%
Audit running 
environments 
after deployment 
Pen testing
Manual code 
scans
From investigating 
incidents
Automated 
testing/CI
Tools from our 
IaC or public 
cloud provider
SNYK RESEARCH REPORT
Infrastructure as Code Security Insights 
6
For those who said their IaC and configuration code goes 
through CI testing, the biggest barrier to integrating security 
checks is a lack of standardized best practices on what to check, 
with each of their separate teams making their own decision 
about what to test. When you couple that with the 41% who 
said their barrier was unclear benchmarks for security, the 
shortest path to improved IaC security can be  paved with 
better tools that offer clearer guidance, while still providing 
teams with the freedom to determine what’s most important 
for their needs. 

## So what is standing in the way of making a change?
62%
41%
22%
22%
16%
11%
41%
said their barrier was 
unclear benchmarks for 
security
Each team 
makes their 
own decisions 
about what to 
test 
Wo do not have 
a clear set of 
benchmarks on 
what to test 
against
We have not 
decided what 
is important for 
us to test
We do not 
have the right 
testing tools
Concerned it 
would slow us 
down too much
There is no clear 
owner to address 
issues that are 
discovered
What is limiting you from always integrating 
security checks into the IaC testing process?
SNYK RESEARCH REPORT
Infrastructure as Code Security Insights 
7
Finding the issue is just one piece of the 
puzzle - once an issue is discovered somebody 
has to fix it. When faced with a choice, 52% 
of respondents claim they usually remediate 
a security issue by directly tweaking the 
infrastructure instead of addressing it by 
modifying the IaC source code. This opens 
up the possibility for a number of issues in 
the long-term because the infrastructure 
and the codified definitions used to create it 
will start to drift; either that or the modified 
infrastructure will be reset to its misconfigured 
state on the next deployment. For those 
that choose this manual remediation 
path, their reasoning is split between a 
lack of standardization, knowledge, and 
communication, along with a desire to speed 
up the fixes as much as possible. 

## Infrastructure Remediation
39%
38%
38%
23%
23%
22%
9%
Lack of standardized 
workflow and 
practices
Concern that  
redeploying from code 
will create new issues 
Faster/easier 
to tweak the 
infrastructure 
Tracing infrastructure 
issues back to code is 
complex/slow
Lack of communication 
between developers 
and operators
Lack of security 
knowledge in the team 
responsible for the code 
No automated tests 
to ensure the IaC 
changes work before 
Why do you directly modify the 
infrastructure instead of fixing 
the code?
How often do you directly 
modify infrastructure, rather 
than fixing the configuration 
in your IaC code?
34%
35%
13%
18%
Most of the time - 
we usually change 
the infrastructure 
directly  instead 
of modifying the 
cource code
Rarely
Never - we always 
fix the code first
52%
remediate a security issue  
by directly tweaking the  
infrastructure instead of  
addressing it by modifying 
the IaC source code
Often
8
SNYK RESEARCH REPORT
Infrastructure as Code Security Insights 
While a lack of standardized workflow and prac-
tices was the leading reason respondents chose to 
remediate a security issue manually, a total of 61% 
of respondents also pointed to speed-related issues. 
Namely that it’s faster and/or easier to tweak the 
infrastructure because tracking issues back to the IaC 
definitions is too complex and/or slow. Again, this 
points to two underlying issues:
First, when security checks are only performed after 
infrastructure has been deployed, it’s too late in the 
process. It separates the security checks from the 
code and it’s likely that pen test reports and audit 
tools don’t provide data that’s directly actionable by 
the owners of the IaC code. 
Second, for teams that are stretched thin, a lack of 
bandwidth could lead to the decision (consciously 
or not) to overlook some security in favor of speed. 
For those teams that are at their limit, the right tools 
can make a world of difference to equip developers 
with what they need to prioritize security. But before 
a tool can be decided on, teams must first determine 
who holds final responsibility for IaC. 
said speed-related issues were 
the reason they remediate a 
security issue manually
61%
SNYK RESEARCH REPORT
Infrastructure as Code Security Insights 
9
One of the barriers to shifting IaC security left 
was that teams struggled to standardize prac-
tices across their organization, leaving each 
team to audit IaC as they see fit. In addition 
to the obvious security issues this presents, it 
speaks to a larger disconnect on responsibility. 
A common theme of this survey is the diffi-
culty to pin down security ownership when 
it comes to IaC - so where does the industry 
currently stand? 
Today it seems there is no consensus on who 
is responsible for the security within IaC. 
Developers and DevOps roles have a slightly 
bigger role than other individual teams and a 
good number say it’s a shared responsibility, 
potentially fitting in to the newer DevSecOps 
models. When asked which team should be 
responsible for IaC security, if it is not a shared 
responsibility, the answers shifted heavily to 
the developers / DevOps groups. 
So what’s stopping these security responsibili-
ties from shifting further left? Mostly, it’s con-
fidence in the broader organization’s ability to 
readily spot and fix issues in the code.

## Who Holds Responsibility for IaC Security?
29%
52%
28%
24%
23%
24%
20%
It is a shared 
responsibility 
Developers/
DevOps
Developers/
DevOps
Infrastructure
Infrastructure
Security
Security
Who is responsible for  
configuration security in IaC 
today?
Who should be 
responsible?
10
SNYK RESEARCH REPORT
Infrastructure as Code Security Insights 
Snyk’s long-standing developer-first approach led to 
the creation of Snyk Infrastructure as Code (Snyk IaC) 
to help solve these problems. This latest tool moves the 
security controls for infrastructure and configurations 
to the beginning of the development lifecycle, so devel-
opers can proactively determine whether their applica-
tion and infrastructure specifications are safe. Designed 
to fit a developer’s workflow, Snyk IaC helps pinpoint 
how to write secure Kubernetes and Terraform config-
urations, and even provides automated fixes as code 
in your choice of source code management systems. 
Together with Snyk Container and Snyk Open Source, 
you can finally embed your security expertise across 
your entire development organization.
To secure your organization and learn more about 
Synk IaC visit snyk.io/product/infrastructure- 
as-code-security/. 

## Snyk Infrastructure as Code: Find and fix configuration security issues the way cloud native experts do.
How confident are you 
in your ability to spot 
configuration issues in IaC?
What would make you more confident in your 
organisation’s ability to spot IaC misconfigurations?
67%
48%
42%
37%
29%
26%
22%
Greatly 
confident
Fairly 
confident
Not 
confident
Somewhat 
confident
4%
22%
25%
49%
A clear and scalable solution to IaC security challenges is to invest in the tools and training needed to drive up 
confidence and help with bandwidth for these teams, allowing them to deploy code quickly and securely. In the 
same report cited above, Gartner also sees the potential for these automated tools and predicts that, by 2025, 
organizations will speed up their remediation of coding vulnerabilities by 30% with code suggestions applied 
from automated solutions, reducing time spent fixing bugs by 50%.
Professional 
training
Automated code 
testing for IaC 
in CI/CD
Audit tools 
specific to 
IaC and 
configuration
Playbooks to 
follow
Tools built-in 
to IDEs
Peer
mentoring
Industry or 
infrastructure 
vendor 
benchmarks
SNYK RESEARCH REPORT
Infrastructure as Code Security Insights 
11
This vendor neutral research was 
independently conducted by Virtual 
Intelligence Briefing (ViB). ViB is an interactive 
on-line community focused on emerging 
through rapid growth stage technologies. ViB’s 
community is comprised of more than 2.2M IT 
practitioners and decision makers who share 
their opinions by engaging in sophisticated 
surveys across multiple IT domains.
The survey methodology incorporated 
extensive quality control mechanisms at 3 
levels: targeting, in-survey behavior, and post-
survey analysis. The Calculated Margin of error 
at a 95% confidence level is 3.9%.
After receiving 543 responses from members of 
our opted-in 2M+ IT community, we screened 
out about 120 respondents who met the role, 
level and company size requirements, but 
who indicated they were not currently using, 
or considering using, the IaC / Configuration 
tools listed in the survey. This extensive 
process led to a survey pool of 481 qualified 
individuals in order to present the most 
accurate look at the current state of IaC. 

## Survey Methodology
Cloud &
Platform
1 - 500 
employees
Developers 
and DecOps
1000 - 2000
Architects
500 - 1000
Infrastructure
5000 - 10,000
10,000 - 
15,000
15,000+
Security & 
Compliance
2000 - 5000
11%
28%
30%
14%
12%
23%
31%
8%
4%
8%
16%
15%
Survey respondents 
by role
Survey respondents by 
company size
SNYK RESEARCH REPORT
Infrastructure as Code Security Insights 
12
SEE SNYK IAC IN ACTION
