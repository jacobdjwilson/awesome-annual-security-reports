# THE STATE OF CLOUD NATIVE SECURITY REPORT 2022

## Table of Contents
[Introduction](#introduction)  
[Executive Summary](#executive-summary)  
&nbsp;&nbsp;&nbsp;&nbsp;[Cloud Expansion and Strategy](#cloud-expansion-and-strategy)  
&nbsp;&nbsp;&nbsp;&nbsp;[Security Posture and Friction](#security-posture-and-friction)  
&nbsp;&nbsp;&nbsp;&nbsp;[Security Drivers](#security-drivers)  
[The Global State of Cloud and Cloud Native Security](#the-global-state-of-cloud-and-cloud-native-security)  
&nbsp;&nbsp;&nbsp;&nbsp;[Cloud Growth Through the Pandemic](#cloud-growth-through-the-pandemic)  
[Security Challenges in Moving to the Cloud](#security-challenges-in-moving-to-the-cloud)  
&nbsp;&nbsp;&nbsp;&nbsp;[Organizational Attributes of High Performance](#organizational-attributes-of-high-performance)  
&nbsp;&nbsp;&nbsp;&nbsp;[Security Posture and Spending](#security-posture-and-spending)  
&nbsp;&nbsp;&nbsp;&nbsp;[How Organizations Achieve Stronger Security Posture](#how-organizations-achieve-stronger-security-posture)  
&nbsp;&nbsp;&nbsp;&nbsp;[The Impact of Open Source Security Tools](#the-impact-of-open-source-security-tools)  
[Identify and Learn from Your Cloud Group](#identify-and-learn-from-your-cloud-group)  
&nbsp;&nbsp;&nbsp;&nbsp;[Which Group Best Describes Your Organization?](#which-group-best-describes-your-organization)  
&nbsp;&nbsp;&nbsp;&nbsp;[The State of Cloud Adoption Groups](#the-state-of-cloud-adoption-groups)  
[Rapid Cloud Expansion Has Polarizing Results](#rapid-cloud-expansion-has-polarizing-results)  
&nbsp;&nbsp;&nbsp;&nbsp;[The Role of Security Vendors, Tools, and Teams](#the-role-of-security-vendors-tools-and-teams)  
&nbsp;&nbsp;&nbsp;&nbsp;[Group Adoption of Best-in-Class Security](#group-adoption-of-best-in-class-security)  
[Final Thoughts](#final-thoughts)  
[Methodology and Demographics](#methodology-and-demographics)  
[About](#about)  
&nbsp;&nbsp;&nbsp;&nbsp;[Palo Alto Networks](#palo-alto-networks)  
&nbsp;&nbsp;&nbsp;&nbsp;[Prisma Cloud](#prisma-cloud)  

## Introduction
In these yearly State of Cloud Native Security Reports, more than 3,000 respondents around 
the world are surveyed about their cloud adoption strategies, budgets, experiences, and plans. 
Their responses shed light on the practices, tools, and technologies used to implement cloud 
workloads and manage security for cloud native architectures. As in the 2020 report, we aim to 
highlight the behaviors and correlated outcomes of organizations who succeeded in their cloud 
initiatives, as well as those who fell short. A clear differentiator appeared in how organizations 
addressed cloud security. This includes differences in how they implemented technologies and 
processes to support both high security posture, defined as the effectiveness of their cloud 
security efforts, and low security friction, defined as the degree to which cloud security is 
limiting their operations. 
Perhaps unsurprisingly, the COVID-19 pandemic influenced both cloud expansion and results 
(see “The Ongoing Impact of COVID-19”). While organizations moved quickly during the 
pandemic to respond to increased cloud demands, many still struggled to automate cloud 
security and mitigate cloud risks. Yet, the move to the cloud continues for companies at all 
stages, from those newly taking advantage of cloud capabilities to the well-established, born-
in-the-cloud organizations. 
The report identified patterns in approaches and outcomes that led to three representative 
groups known as Moderate Adopters, Rapid Expanders, and Established Users. These groups 
emerged based on traits such as cloud footprint, transformation goals, and operational 
strategies. We present these groups along with rigorous data and analysis of their behaviors to 
help readers find their organization’s peer group and identify common challenges and strategies 
that impact outcomes. Regardless of your organization’s cloud maturity level, industry, region, 
or cloud-migration goals, the research outlined in this report provides the essential insights you 
need to plan your cloud adoption path.

## Executive Summary
As the cloud’s unique capabilities continue to evolve, so have the ways in which we employ it 
to drive business forward. As such, this report includes research that pays special attention to 
the latest top-of-mind concerns and narratives in the cloud native security community, including 
automation, DevSecOps, security posture, the use of open source and more. Our goal each year 
in the production of this report remains the same: for you to come away with valuable insights 
that help guide your cloud adoption and security journey in 2022 and beyond. 

### Cloud Expansion and Strategy
*   Organizations rapidly expanded their use of clouds during the pandemic by more than 25% 
overall but struggled with comprehensive security, compliance, and technical complexity.
*   Organizations expanded with less budget, with 39% of organizations spending less than 
$10M on their cloud (up 16% from 2020) and only 26% spending more than $50M (down 
17% from 2020). 
*   While organizations continue to use diverse compute options, platform as a service (PaaS) 
and serverless approaches rose 20%, likely supporting the rapid transition to the cloud, 
while the use of containers and containers as a service (CaaS) saw more moderate growth.

### Security Posture and Friction
*   Organizations with a strong security posture are more than 2X more likely to have low levels 
of security friction—the degree to which organizations believe cloud security supports or limits 
their operations. This highlights the need for a two-pronged approach to cloud security, with 
effective security capabilities that don’t disrupt teams outside of security. 
*   Organizations with best-in-class security operations see the greatest benefits to their 
workforce in terms of productivity and satisfaction. Eighty percent of those with strong 
security posture and 85% of those with low security friction reported increased 
workforce productivity.
*   A majority of organizations (55%) report a weak security posture and believe they need 
to improve their underlying activities—such as gaining multicloud visibility, applying more 
consistent governance across accounts, or streamlining incident response and investigation—
to achieve a stronger posture.
*   Eighty percent of organizations that primarily use open source security tools have weak or 
very weak security posture, compared to 26% of those who primarily leverage their cloud 
services provider and 52% of those who depend on third parties, highlighting that piecing 
together a platform using disparate tools leaves an organization less secure.

### Security Drivers
*   Organizations are consolidating their security approach. Nearly three-quarters use 10 or 
fewer security tools, and we see a 27% increase from the 2020 data in the number of 
organizations using just one to five security vendors, suggesting that they are looking to 
fewer security vendors for more capabilities.
*   Organizations that have implemented a high level of security automation are 2X more likely 
to have low friction and strong posture than their counterparts with low levels of security 
automation.
*   How well organizations adopted and implemented DevSecOps methodologies is the 
primary indicator of best-in-class security. Organizations that tightly integrate DevSecOps 
principles are over 7X more likely to have strong or very strong security posture and are 
9X more likely to have low levels of security friction.

## The Global State of Cloud and Cloud Native Security 
 
In the first section of this report, we review the broad trends in cloud adoption and cloud security 
activities as reported by organizations around the world. (See the [Methodology and Demographics](#methodology-and-demographics) section 
for more detail on who we surveyed.) 

### Cloud Growth Through the Pandemic  
Throughout the pandemic, there were significant expansions of cloud workloads overall, jumping to 
an average of 59% of workloads hosted on the cloud, up from an average of 46% in 2020. In addition, 
69% of organizations host more than half of their workloads in the cloud, up from just 31% of 
respondents in 2020.

*Figure 1: Percent change in cloud workload volumes since 2020. This figure shows a bar chart with two sets of bars. The first set of bars shows the percentage of workloads hosted on the cloud. In 2020, it is 46%, and in 2021, it is 59%. The second set of bars shows the percentage of organizations hosting more than half of their workloads in the cloud. In 2020, it is 31%, and in 2021, it is 69%.*

When examining the reasons why organizations expanded their cloud capabilities, the growth was fueled 
by strategic business drivers—application modernization, maintaining competitiveness, and controlling 
infrastructure overhead. While the pandemic was surely a contributing factor in this year’s report, these 
reasons remain paramount for why organizations choose to utilize the cloud in general. The flexibility 
and agility that the cloud provides to organizations allow them to keep businesses moving forward at an 
ever-increasing pace.

Looking ahead, organizations have not significantly changed their expectations for leveraging the cloud 
since last year. On average, organizations expect to host 68% of their workloads in the cloud within two 
years, which is consistent with last year’s expectation of 65%. Despite a faster shift during the pandemic 
than many organizations expected, this suggests that the upper limit of organizations’ cloud transformation has not significantly grown. 

Cloud composition also evolved this year, as organizations shifted toward private hosting of their 
cloud workloads, with an average of 55% of cloud workloads on private clouds, up seven percentage 
points from 2020. While organizations continue to use diverse compute options, PaaS and serverless 
approaches rose 20 percentage points, while the use of containers and CaaS saw more moderate 
growth. PaaS and serverless strategies, which allow development teams to put applications in the cloud 
without necessarily having to build and scale infrastructure at the same time, likely helped support 
the rapid transition to the cloud seen in the past year. This is a trend we expect to continue and plan to 
closely monitor.

*Figure 2: Share of workloads hosted in public vs. private clouds (left); share of workloads by compute type (right). The left side of the figure shows a bar chart with two sets of bars. The first set of bars shows the percentage of workloads hosted in public clouds. In 2020, it is 52%, and in 2021, it is 45%. The second set of bars shows the percentage of workloads hosted in private clouds. In 2020, it is 48%, and in 2021, it is 55%. The right side of the figure shows a bar chart with five sets of bars. Each set of bars shows the percentage of workloads by compute type. The first set of bars shows the percentage of workloads using VMs. In 2020, it is 30%, and in 2021, it is 24%. The second set of bars shows the percentage of workloads using Containers. In 2020, it is 17%, and in 2021, it is 24%. The third set of bars shows the percentage of workloads using CaaS. In 2020, it is 13%, and in 2021, it is 21%. The fourth set of bars shows the percentage of workloads using PaaS and Serverless. In 2020, it is 22%, and in 2021, it is 42%. The fifth set of bars shows the percentage of workloads using other compute types. In 2020, it is 3%, and in 2021, it is 4%.*

*Figure 3: Reasons for expanding cloud capabilities. This figure shows a bar chart with seven sets of bars. Each set of bars shows the percentage of respondents who cited a particular reason for expanding cloud capabilities. The reasons and percentages are as follows: Application modernization (53%), Maintain competitiveness in market (51%), Reduce infrastructure overhead (42%), Regulatory compliance (40%), Part of wider digital transformation efforts (16%), Enable developer agility (39%), and Born in the cloud/have always been in the cloud (61%).*

Despite the push to move more workloads to the cloud, organizations did so with less budget than the 
previous year. In 2021, 39% of organizations spent less than $10 million on their cloud, an increase of 
16% from 2020, while only 26% spent more than $50 million, a drop of 17% from 2020. This drop in 
cloud spending may be the result of across-the-board budget cuts or reallocation of funds due to the 
pandemic, or it may simply reflect a “normalization” of cloud activities, with budgets falling naturally 
as teams gain confidence and efficiencies with experience. 

*Figure 4: Changes to cloud budgets. This figure shows text and percentages highlighting the changes in cloud budgets. In 2020, 21% of organizations dedicated less than $10M toward their cloud. In 2021, 39% of respondents fall in that category. Organizations with cloud budgets over $50M dropped from 46% to 26%.*

While we see slight differences in cloud adoption approaches by industry, geography, and revenue, the 
data indicates that these variations do not play a significant role in overall results. That said, the figure 
below highlights some of the more notable regional variations.

*Figure 5: Cloud trends by global region. This figure shows a map of the world with text boxes highlighting regional cloud trends. In Brazil, almost half (48%) of respondents expect their companies to have anywhere from 76-100% of their workloads in the cloud in the next two years, showing a movement of embracing the cloud. The UK uses more open source tooling as their primary provider for cloud security than any other country surveyed. Almost half (47%) of USA respondents report a strong or very strong security posture, higher in comparison to other countries. Germany reported the highest percentage of automating security processes (40%). Japan reported the most significant increase of using Serverless architecture (57%) in the next 24 months, over any other architecture.*

## Security Challenges in Moving to the Cloud
As organizations rapidly expanded their use of the cloud over the past year, they reported the same 
top challenges as last year’s respondents: comprehensive security and compliance, along with 
technical complexity.

*Figure 6: Challenges in moving to the cloud. This figure shows a bar chart with three sets of bars. Each set of bars shows the percentage of respondents who cited a particular challenge in moving to the cloud. The challenges and percentages are as follows: Maintaining comprehensive security (2020: 39%, 2021: 50%), Meeting compliance requirements (2020: 42%, 2021: 45%), and Technical complexity (2020: 42%, 2021: 32%).*

While top-line cloud budgets fell, cloud security budgets remained steady. 
We interpret that to mean that while organizations spent less money on the 
cloud overall, they did not let their security budgets waver. This highlights 
that companies understand the value of securing the cloud in order to take 
the most advantage of it.

We saw this year that companies expanded their cloud security teams during 
the pandemic, with 53% of organizations reporting a security team of over 
30 people, up from 41% last year. Companies also consolidated their cloud 
security vendors as they expanded their cloud environments. The data shows 
a 27% increase in the number of organizations using just one to five security 
vendors, while those using six to ten vendors is down 19% since last year.

*Figure 7: Respondents spending more than 20% of cloud budget on security. This figure shows a bar chart with two bars. The first bar shows the percentage of respondents spending more than 20% of their cloud budget on security in 2020, which is 4%. The second bar shows the percentage of respondents spending more than 20% of their cloud budget on security in 2021, which is 15%.*

*Figure 8: Changes to number of security vendors. This figure shows a bar chart with two sets of bars. The first set of bars shows the percentage of organizations using 6-10 security vendors. In 2020, it is 68%, and in 2021, it is 39%. The second set of bars shows the percentage of organizations using 1-5 security vendors. In 2020, it is 41%, and in 2021, it is 20%.*

While companies reduced the number of security vendors they engage, they made minimal year-over-
year changes in the number of security tools they are leveraging. We define cloud security vendors as any 
company that organizations employ to secure their clouds and security tools as the number of capabilities 
and/or features those cybersecurity companies offer. Nearly three-quarters of organizations use 10 or 
fewer security tools, suggesting that they are looking to fewer security vendors to satisfy the need for a 
wide range of capabilities. This consolidation supports observations that organizations who depend on 
disparate tools from multiple vendors can experience blind spots that increase risk and force additional 
efforts to close those gaps. For the 28% of organizations who are still using large numbers of tools—including the 8% using 21 to more than 50 tools—we raise a cautionary flag. 

Of those organizations that used 21 or more security tools, almost all (91%) used six or more vendors to supply them. To manage so many tools simultaneously, these organizations had larger teams 
managing and supporting cloud workload security; nearly half (49%) of them employed more than 50 
employees to manage cloud security. Perhaps not surprisingly, then, higher tool usage is more likely to 
be taken on by companies with higher revenues. Of respondents working at companies with revenues 
of $1 billion, 11% indicated using 21 or more tools, versus only 3% of those working for companies with 
revenues less than $1 billion.

### Organizational Attributes of High Performance
Beyond the varying use of security vendors and tools, we also examined the organizational security 
attributes that underlie successful cloud expansion. The research highlights the key elements of cloud 
native security, drivers for best-in-class security, and the impact of security on wider organizational 
success. 

To reach a conclusion that allowed us to compare otherwise disparate organizations, we studied two 
opposing security attributes:
*   Security posture is how organizations rate the effectiveness of their cloud security efforts. 
*   Security friction is the degree to which organizations believe cloud security supports or limits their 
operations.

To measure cloud security posture, we asked respondents about their agreement with six statements. 
The more strongly a respondent agreed with the statements, the stronger the overall perception of the 
organization’s cloud security posture. We found that a slight majority of organizations (55%) have a 
weak security posture. More specifically, this majority believes their underlying activities—such as 
gaining multicloud visibility, applying more consistent governance across accounts, or streamlining 
incident response and investigation—need to be more effective.

### Security Posture and Spending
Organizations with strong security postures tend to spend more on security. Over two-thirds of those 
with strong or very strong security posture invested 16% or more of their cloud budget on security. For 
those with weak or very weak security posture, under a fifth spent the same percentage of their cloud 
budget on security. The “strong security posture” group also appears to have plans to increase its security spending. Nearly three-quarters (71%) of organizations with strong or very strong security posture 
plan to spend 16% or more of their cloud budget on security over the next 12 months, versus only 46% 
of the weak or very weak security posture group.

*Figure 9: Factors contributing to security posture (left); percentage of organizations with strong or weak security posture (right). The left side of the figure shows a list of six statements about security tools and practices. The statements are: Our security tools provide visibility across all cloud accounts and resources, Our risk and vulnerability prioritization is extremely useful, Our automated runtime protection provides a strong security baseline for workloads, Our security tools provide robust governance policies across all cloud native applications and resources, Our security tools make it easy for us to maintain compliant environments and easily generate audit-ready reports, and Our security tools make it easier to investigate and respond to incidents. The right side of the figure shows a pie chart with four segments. The segments represent the percentage of organizations with very weak, weak, strong, and very strong security posture. The percentages are 6%, 39%, 33%, and 22%, respectively. The figure also highlights that 45% of organizations have a strong cloud security posture and 55% have a weak cloud security posture.*

By combining these two metrics, we see that achieving low 
security friction is essential to driving a stronger security 
posture. Organizations with a strong security posture 
are more than two times more likely to have low levels of 
security friction. This highlights the need to take a two-
pronged approach to cloud security: organizations should 
strive for the most effective security capabilities, but they 
need to ensure those tools and processes do not interfere with 
the flow of business operations.

Beyond operational excellence, we also see additional 
advantages to achieving these best-in-class security 
outcomes. Organizations that enable high security posture and low friction see the greatest benefits to 
their workforce in terms of increased productivity and higher employee satisfaction with over 80% of 
organizations with low levels of security friction reporting increased or significantly increased levels 
of employee satisfaction.

To analyze cloud security friction, we asked respondents whether they agree with two statements about 
business outcomes as a result of cloud adoption and security. The more strongly a respondent agreed with 
the statements, the higher the respondent’s overall perception of their company’s cloud security friction. 
Here we find that just under half (48%) of organizations believe they have low security friction.

*Figure 10: Factors contributing to organizational friction (left); Percentage of organizations with high, medium, or low friction (right). The left side of the figure shows a list of two statements about cloud security and business outcomes. The statements are: Our cloud expansion has not met its expected ROI due to our issues around cloud security and Security processes have caused delays to our project timelines. The right side of the figure shows a pie chart with three segments. The segments represent the percentage of organizations with low, mid, and high security friction. The percentages are 48%, 28%, and 24%, respectively.*

*Figure 11: Percent of “low-friction” organizations with weak or strong posture. This figure shows a pie chart with two segments. The segments represent the percentage of "low-friction" organizations with weak and strong security posture. The percentages are 71% and 29%, respectively.*

*Figure 12: Comparing organization outcomes to overall security posture. This figure shows a bar chart with two sets of bars. The first set of bars shows the percentage of organizations with increased productivity. The second set of bars shows the percentage of organizations with increased satisfaction. The bars are grouped by security posture level: Very Weak, Weak, Strong, and Very Strong. The percentages are as follows: Very Weak (Productivity: 50%, Satisfaction: 50%), Weak (Productivity: 60%, Satisfaction: 60%), Strong (Productivity: 80%, Satisfaction: 80%), and Very Strong (Productivity: 85%, Satisfaction: 85%).*

### How Organizations Achieve Stronger Security Posture
Next, we examine the approaches taken by top-performing organizations to reduce organizational 
friction and improve overall posture. The organizations that achieve this balanced, best-in-class security 
excel in two related disciplines:
*   DevSecOps integration—the degree to which cloud security touchpoints have been integrated into the 
full development lifecycle, from build to runtime.
*   Cloud security automation—the degree to which cloud security has been automated.

We asked respondents to rate the degree of their organization’s DevSecOps integration on a scale of 
“never” to “always” in response to four questions.

*Figure 13: Factors that contribute to DevSecOps integration measurement (left); comparing DevSecOps integration to automation levels (right). The left side of the figure shows a list of four phases of the delivery cycle. The phases are: Requirements and design phase of the delivery cycle, Building phase of the delivery cycle, Testing phase of the delivery cycle, and Deployment phase of the delivery cycle. The right side of the figure shows a bar chart with three bars. Each bar shows the percentage of teams with high DevSecOps integration. The bars are grouped by automation level: Highly Automated Teams (61%), Medium Automated Teams (22%), and Low Automated Teams (16%).*

How well organizations adopted and implemented 
DevSecOps methodologies was the primary indicator 
of best-in-class security. Organizations that tightly 
integrate DevSecOps principles into their development 
lifecycle are over seven times more likely to have strong 
or very strong security posture and are nine times more 
likely to have low levels of security friction.

To measure automation, we asked respondents to 
rate how deeply their organization has automated five 
security practices, on a scale of “completely manual” to 
“completely automated.”

*Figure 14: Outcomes for organization that tightly integrate DevSecOps principles. This figure shows text highlighting the outcomes for organizations that tightly integrate DevSecOps principles. These organizations are over 7X more likely to have strong or very strong security posture and are 9X more likely to have low levels of security friction.*

*Figure 15: Factors that contribute to automation measurement (left); comparing security friction to automation levels (right). The left side of the figure shows a list of five security practices. The practices are: Onboarding of cloud accounts for visibility, Ticket creation for security alerts, Remediation of misconfigurations, Scanning infrastructure as code (IaC) template, and Scanning container images during CI/CD. The right side of the figure shows a bar chart with three bars. Each bar shows the percentage of teams with low security friction. The bars are grouped by automation level: Highly Automated Teams (72%), Medium Automated Teams (38%), and Low Automated Teams (41%).*

We find that organizations that have implemented a high level of security automation are roughly two 
times more likely to have low friction and strong posture than their counterparts with low levels of 
security automation. Specifically, pushing past “average” levels of automation leads to a significant 
increase in security outcomes.

### The Impact of Open Source Security Tools
Organizations took a wide variety of approaches to the providers of their security tools, leveraging 
cloud service providers (CSPs), third parties, and open source security tools. However, the data reveals 
consistent challenges for organizations that rely primarily on open source tools.  
This group tends to have smaller budgets than their counterparts who are leveraging third-party or 
CSP methods, but perhaps counter-intuitively, these teams are larger than those using tools from 
third-party or CSP providers, with 70% of organizations that rely primarily on open source tools 
reporting security teams of 30 or more.

*Figure 16: Automation as a driver of security outcomes. This figure shows a bar chart with two sets of bars. The first set of bars shows the percentage of organizations with low security friction. The second set of bars shows the percentage of organizations with strong or very strong security posture. The bars are grouped by automation level: Low Level of Automation, Mid Level of Automation, and High Level of Automation. The percentages are as follows: Low Level of Automation (Friction: 41%, Posture: 25%), Mid Level of Automation (Friction: 31%, Posture: 38%), and High Level of Automation (Friction: 72%, Posture: 83%).*

*Figure 17: Security provider and team budget (top) and size (bottom). The top part of the figure shows a table with four rows. Each row represents a different type of security provider: CSP Primary Security Provider, Third Party Primary Security Provider, Open Source Primary Security Provider, and Balanced Security Providers. Each row shows the percentage of organizations that spend a certain percentage of their cloud budget on security. The percentages are 1-5%, 6-10%, 11-15%, 16-20%, 21-30%, and 31-50%. The bottom part of the figure shows a table with four rows. Each row represents a different type of security provider: CSP Primary Security Provider, Third Party Primary Security Provider, Open Source Primary Security Provider, and Balanced Security Providers. Each row shows the percentage of organizations that have a certain team size. The team sizes are Under 20, 21-30, 31-50, and 51+.*

Furthermore, of those who are using primarily open source security tools, 80% have weak or very 
weak security posture.

*Figure 18: Security provider and security posture. This figure shows a bar chart with four sets of bars. Each set of bars shows the percentage of organizations with a certain security posture. The bars are grouped by security provider: CSP, Third Party, Open Source, and Balanced. The security posture levels are Very Weak, Weak, Strong, and Very Strong. The percentages are as follows: CSP (Very Weak: 9%, Weak: 15%, Strong: 64%, Very Strong: 12%), Third Party (Very Weak: 6%, Weak: 42%, Strong: 32%, Very Strong: 20%), Open Source (Very Weak: 19%, Weak: 51%, Strong: 29%, Very Strong: 1%), and Balanced (Very Weak: 15%, Weak: 43%, Strong: 40%, Very Strong: 2%).*

In aggregate, the data suggests that open source security tools do not offer an integrated, comprehensive approach that satisfies the full range of capabilities and features organizations are looking 
for. Organizations successfully utilizing open source security tools seem to merely shift budget costs 
to labor in order to support their efforts. Organizations that are looking to adopt open source tools 
should be prepared to trade a highly customized implementation with ongoing investments for internal 
support that would otherwise come from designated solution providers. 

## Identify and Learn from Your Cloud Group
To determine if certain frameworks can drive best-in-class security outside of DevSecOps methodologies 
and automated security, as noted above, we looked for patterns in the paths that organizations took to 
develop their cloud environments and cloud security during the pandemic. This period provided something of a natural experiment, where we were able to compare different approaches and see their impact 
on a significantly condensed timeline. Rather than waiting for several years, this concentrated move to 
the cloud produced rapid results in just months. 

From the data, we discovered three representative groups based on organizational 
behaviors and approaches to cloud security. Note that our findings from these 
groups remain consistent regardless of geography, industry, or revenue. This 
gives us a unique look at cloud success factors—and paths to failure—based on 
how organizations approach their cloud and cloud security initiatives rather than 
who they are.

The first group is the Moderate Adopters, comprising organizations with a lower 
focus on cloud adoption both before and during the pandemic. The second group is 
Rapid Expanders, made up of organizations that had small cloud footprints before 
the pandemic but engaged in rapid, widespread cloud adoption during the pandemic. 
Finally, Established Users are organizations that already had large cloud footprints 
before the pandemic and continued moderate expansion during this time.

We encourage you to explore the traits and experiences of each group to identify which most closely 
matches your organization. You can use the data to benchmark your organization against your peers, 
validate experiences, and explore differences. This analysis also allows you to identify a group that most 
closely matches your future cloud aspirations and explore the decisions and behaviors the group exhibits 
to inform your ongoing strategies for long-term success.

*Figure 19: Characteristics of each cloud adoption group. This figure shows a text box with the characteristics of each cloud adoption group. Moderate Adopters: 39% of total, More likely to have lower revenue, Before pandemic: Small cloud footprint, During pandemic: Steady cloud expansion, Expansion driven by tactical value, Low investment and priority for cloud, Currently: Leveraging serverless architectures, Planning: Average target for total cloud usage (62%). Rapid Expanders: 33% of total, Tend to have higher revenue, Before pandemic: Small cloud footprint, During pandemic: Rapid cloud expansion, Expansion driven by strategic and tactical value, Average investment and priority for cloud, Currently: Leveraging PaaS architectures, Planning: Average target for total cloud usage (62%). Established Users: 28% of total, Mostly large organizations (by revenue), Before pandemic: Large cloud footprint, During pandemic: Steady cloud expansion, Expansion driven by tactical value, High investment and priority for cloud, Currently: Balanced use of compute environments, Planning: High target for total cloud usage (84%).*

### Which Group Best Describes Your Organization?
### The State of Cloud Adoption Groups
As stated earlier, the cloud traits and behaviors of these groups are generally consistent regardless of 
geography, industry, or size of the organization.

*Figure 20: Cloud adoption groups by industry (left); cloud adoption groups by income (right). The left side of the figure shows a table with four rows. Each row represents a different industry: Consumer, Energy, resources, and industrials, Financial services, Life sciences and healthcare, and Technology, media, and telecommunications. Each row shows the percentage of organizations in each cloud adoption group: Moderate Adopter, Rapid Expander, and Established User. The right side of the figure shows a table with six rows. Each row represents a different income bracket: Under $10M, $10M–$100M, $100M–$500M, $500M–$1B, $1B–$5B, and Over $5B. Each row shows the percentage of organizations in each cloud adoption group: Moderate Adopter, Rapid Expander, and Established User.*

*Figure 21: Percent of workloads in the cloud by adoption group. This figure shows a table with four rows. Each row represents a different cloud adoption group: Moderate Adopter, Rapid Expander, and Established User. Each row shows the percentage of workloads in the cloud in 2020, 2021, the current total, and the 2022 target.*

Cloud Spending
Across all groups, cloud spend varied significantly. Only 42% of Moderate Adopters spent more than 
$10M on the cloud, compared to 69% of Rapid Expanders and 70% of Established Users. Established 
Users also have the highest cloud budgets, with 10% spending over $100M, compared to just 2% of 
Moderate Adopters and 1% of Rapid Expanders.

*Figure 22: Total cloud spend by adoption group. This figure shows a table with six rows. Each row represents a different cloud spend bracket: Don’t know/No spend, Under $1M, $1M–10M, $10M–$50M, $50M–$100M, and Over $100M. Each row shows the percentage of organizations in each cloud adoption group: Moderate Adopter, Rapid Expander, and Established User.*

### Approach to Compute Environment
We also see differences in approaches to cloud architectures. Established Users are far more likely to 
use a blend of compute environments, including virtual machines (VMs), containers/CaaS, PaaS, and 
serverless, with 65% of this group using all four equally. Rapid Expanders also show a mostly balanced 
approach (48%), but with twice the use of PaaS compared to Established Users (28% versus 14%). This 
decision to avoid infrastructure management may have enabled some of Rapid Expanders’ fast growth. 
Our analysis is that Moderate Adopters, with smaller cloud footprints and slower growth plans, may not 
be “cloud-first” organizations; rather