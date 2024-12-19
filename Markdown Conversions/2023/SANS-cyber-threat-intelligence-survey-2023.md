# SANS 2023 CTI Survey: Keeping Up with a Changing Threat Landscape

Written by Rebekah Brown and Katie Nickels
July 2023
©2023 SANS™ Institute

## Table of Contents
* [Executive Summary](#executive-summary)
* [Survey Respondents](#survey-respondents)
* [People and Teams](#people-and-teams)
* [Requirements and Prioritization](#requirements-and-prioritization)
* [Sources](#sources)
* [Producing Intelligence](#producing-intelligence)
    * [Production and Consumption](#production-and-consumption)
* [Tools](#tools)
* [Analytic Processes](#analytic-processes)
* [Dissemination and Feedback](#dissemination-and-feedback)
    * [Dissemination Methods](#dissemination-methods)
    * [Impact of CTI](#impact-of-cti)
    * [A Note on RFIs](#a-note-on-rfis)
* [Challenges and Limitations](#challenges-and-limitations)
* [Moving Forward](#moving-forward)
* [Sponsors](#sponsors)

## Executive Summary
Events throughout 2022 highlighted the positive impact of cyber threat intelligence (CTI), 
from informing decisions about major ransomware intrusions to cyber conflict around the 
war in Ukraine. With this year’s survey bringing in the most respondents we’ve ever had, 
the diverse feedback from CTI personnel helps highlight areas where CTI as a discipline has 
matured, as well as opportunities where it still must grow. Key insights from this year’s 
survey include:

*   Current events and geopolitics significantly influence what CTI personnel focus on, 
with most respondents reporting that the war in Ukraine has influenced their team’s 
priorities. CTI personnel frequently rely on external news sources when deciding 
what to prioritize, which can prove both beneficial and challenging.
*   CTI analysts continue to use a range of sources as they consume and produce 
intelligence, with an emphasis on external over internal sources. Although teams 
use multiple sources, indicators of compromise (IOCs) continue to play a key role in 
supporting defensive tools and teams.
*   CTI is an increasingly cross-functional process in many organizations. Examples of 
CTI work frequently cite partnerships between CTI teams and other teams within an 
organization, including vulnerability management teams, security operations teams, 
and incident response teams. Although the importance of these partnerships is 
clear, they aren’t without challenges—inter-team communication and trust are often 
identified as hurdles to overcome.
*   Partnerships between CTI vendors and customers are critical, and CTI vendors play 
a significant role in this discipline. The majority of respondents reported using 
external CTI service providers in some way. We also see both an increase in the 
number of respondents who work for cybersecurity companies and an increase in 
the discussion of specific CTI vendors, products, and tools when describing CTI work. 
This can be a beneficial relationship to have as long as organizations continue to 
leverage critical internal threat-intelligence data and CTI vendors continue to help 
organizations know when information is relevant and actionable for them.

*Image Description: A graphic showing survey demographics. It includes four sections: Top 4 Industries Represented, Organizational Size, Top 4 Roles Represented, and Operations and Headquarters. The Top 4 Industries Represented section shows four gears, each representing 10 respondents, with the labels "Technology", "Government", "Cybersecurity service provider", and "Banking and finance". The Organizational Size section shows five buildings, each representing 25 respondents, with the labels "Small (Up to 1,000)", "Small/Medium (1,001–5,000)", "Medium (5,001–15,000)", "Medium/Large (15,001–50,000)", and "Large (More than 50,000)". The Top 4 Roles Represented section shows four figures, each representing 10 respondents, with the labels "Security operations/ Security analyst", "Security manager or director", "CTI analyst", and "Security administrator". The Operations and Headquarters section shows the number of respondents in operations and headquarters for each of the four industries.*

## Survey Respondents
This year’s survey received feedback from 984 individual respondents in more than 25 
different industries. More than four times as many individuals responded to this year’s 
survey as compared to 2022, allowing us to integrate many more perspectives. See Figure 1.

This year we had several respondents 
from a new industry not previously 
included in our data collection: the water 
industry (including utilities and waste). 
In October 2021, the Cybersecurity and 
Infrastructure Security Agency (CISA) 
released an alert on the ongoing attacks 
against the water sector, highlighting 
the critical importance of water services 
and the active threats that the sector 
faces.<sup>1</sup> Although we have had survey 
respondents in the past who identified 
themselves as water and wastewater 
sector employees, beginning this year 
we are including their responses as one 
of the 18 sectors listed in the survey. CTI 
work is done across many more fields 
than those 18, and each year we have many respondents from industry types not listed 
by default. This year we see a notable increase in the diversity of those fields, including 
agriculture, mining, civil engineering, construction, gaming, health and wellness, and law. 
Figure 2 illustrates some of those various industries represented by the survey respondents.

This demonstrates that CTI continues to be a growing field and that organizations of 
many types can benefit from CTI. Recent attacks show that no one particular industry 
is being targeted; instead, attackers continue to find ways to monetize attacks in nearly 
every vertical. In addition to organizations in these fields benefiting from experienced CTI 
analysts, the CTI field itself will gain from the increased diversity of thought, experience, and 
perspective as analysts work against threats that can impact organizations in unique ways. 
Another notable change observed in this 2023 survey is that the primary industry of 
respondents is cybersecurity service providers, as compared to 2022 when it was banking 
and finance. This notable shift suggests that CTI analysts working for cybersecurity service 
providers represent a substantial portion of the community. Cybersecurity service vendors 
often approach CTI differently than “end-user” organizations such as banks because 
these vendors often have visibility into many organizations while also working to balance 
requirements from those many stakeholders. 
This year’s respondents were heavily skewed toward the United States, with 71% of their 
organizations being primarily headquartered in the United States, up from 58.6% of last 
year’s respondents. Although this is not surprising, it’s important to note this as a limitation 
of the survey, because respondents are heavily influenced by their country of operations.

*Image Description: A pie chart titled "Industries Represented in 2023 Survey". The chart shows the distribution of respondents across various industries, including "Technology", "Government", "Cybersecurity service provider", "Banking and finance", "Healthcare", "Education", "Manufacturing", "Retail", "Energy", "Transportation", "Legal", "Insurance", "Water", "Telecommunications", "Non-profit", "Agriculture", "Mining", "Other".*

<sup>1</sup> “Ongoing Cyber Threats to U.S. Water and Wastewater Systems,” www.cisa.gov/news-events/cybersecurity-advisories/aa21-287a

## People and Teams
This year’s survey respondents came from a variety of team sizes and types. The 
organization size most commonly represented in this year’s survey is 101 to 500 
employees, at 17%, with another 11% representing organizations with fewer than 100 
employees. This highlights the fact that organizations of all sizes utilize CTI to support 
their overall security operations, a far cry from the days when CTI was only thought of as 
useful to the top 1% of companies. 

Fifty-one percent of respondents report that their 
organization has a formal dedicated CTI team, the 
highest number we have seen since 2020. See Figure 3.

Formal dedicated teams often have more bandwidth to 
focus on critical CTI processes that can help streamline 
and optimize the work of CTI analysts, and we see 
reflections of this throughout the survey. Sixteen 
percent of respondents say they have a single dedicated 
person, and 21% say CTI is a shared responsibility 
with staff pulled from other security groups. Analysts 
at smaller organizations and those with a single CTI 
analyst face unique challenges in terms of resources, and small businesses remain at a 
high risk of intrusions because of this. It’s encouraging to see that these organizations still 
recognize CTI as an important function within their security staff, because CTI can help 
small organizations prioritize against the most impactful threats. 

One primary way organizations supplement these limited in-house CTI resources is 
through external CTI service providers. A majority of respondents report using external 
CTI service providers in some way, with 47% using a combination of in-house and service 
provider resources, and 17% exclusively using service providers. Using a combination 
of both in-house and external resources can be a wise choice for many organizations. 
Such an approach allows external providers to cover widespread threats that affect most 
organizations, while in-house personnel focus on applying that CTI to their organization 
and to unique threats their organization faces.

In terms of skill sets and focus areas of those working in the CTI field, the largest group 
of respondents identify themselves as security operations and security analysts, at 
17%, followed by CTI analysts at 15%. This is a significant increase compared to the 2017 
survey, in which only 6% of respondents identified themselves as dedicated CTI analysts, 
indicating substantial growth in this career field.

*Image Description: A line graph titled "Growth of Formal CTI Teams". The graph shows the percentage of organizations with dedicated CTI teams from 2018 to 2023. The percentages are: 2018: 41.5%, 2019: 41.1%, 2020: 49.5%, 2021: 44.4%, 2022: 47.0%, 2023: 50.8%.*

## Requirements and Prioritization
The first phase of the intelligence cycle is planning and direction, which involves crucial 
activities to set up teams for success. A critical part of this phase is defining intelligence 
requirements—the questions or needs an organization has that an intelligence team can 
seek to support. If teams do not define requirements, they risk producing intelligence 
that doesn’t support key decisions and that isn’t used by consumers. Respondents this 
year clearly recognize the value of requirements, because 59% of them report that CTI 
requirements are clearly defined in their organization. 

This represents a positive change from 2022, in which only 
35% of respondents reported they had clearly defined CTI 
requirements. In fact, this year only 3% or respondents 
do not have requirements and have no plans to create 
them, down from 11% in 2022. Although this change is 
likely due, at least in part, to the maturity of respondent 
organizations, it suggests a promising trend: that CTI 
teams are thinking carefully about what they need from 
intelligence. See Figure 4.

When it comes to who contributes to CTI requirements, however, responses show an 
opportunity for growth. Sixty-nine percent of respondents say the CTI team themselves 
contribute to requirements, compared to only 32% of respondents reporting that 
executives contribute. This presents an opportunity for CTI teams to potentially increase 
engagement with executive leadership, a group that has both a need for and a desire for 
CTI. Looking for additional contributions to CTI requirements beyond just the team itself 
presents an opportunity for teams to expand the value and impact of CTI.

Prioritizing requirements and the work the CTI team undertakes is a challenge across 
many teams. This year’s responses reveal that the majority of CTI teams spend a 
significant amount of time responding to open source reporting from others, including 
threat reports from researchers and cybersecurity news stories. Over half of respondents 
note that they spend more than 40% of their time on this set of activities.

When asked how teams determine which CTI tasks to work on and how they prioritize 
threats, one respondent offered a clear explanation: “Whatever is trending.” This response 
indicates that analysts and their leadership increasingly hear about cyber threats from 
social media, blog posts, cybersecurity news, and even mainstream news. Another noted 
that their requirements are often overridden when senior management panics about 
something and the CTI team is told to prioritize that. This trend isn’t surprising given 
the wealth of open source information about cyber threats that constantly inundates 
consumers. However, this also presents an opportunity for CTI teams to try to clarify to 
their consumers that topics trending in the news are not always the most impactful to 
their organization.

*Image Description: A bar chart titled "CTI Requirements". The chart compares the responses from 2022 and 2023 regarding whether CTI requirements are clearly defined. The categories are: "Yes, we have documented intelligence requirements", "No, but we plan to define them", "No, our requirements are ad hoc", and "No, and we have no plans to formalize requirements". The chart shows the percentage of respondents for each category in both 2022 and 2023.*

Many respondents shared more structured approaches to prioritizing their work, 
which fell under several main categories:
*   Examining assets in their organization’s environment and assessing threat 
priority based on the risks to those assets
    *   Example response: We look at known threats in the public/private domain 
and compare them to related software and/or vulnerabilities and prioritize 
these based on the prevalence of the software/system versus the actual 
severity of the vulnerability that may exist within our environment. What 
may also contribute to the order of addressing such items 
is the fact of any potential compensating control that may 
technically reduce the severity level of the vulnerability if 
not able to patch, etc., or haven’t patched yet.
*   Considering threats that others have reported as impacting 
the organization’s industry
    *   Example response: Primarily based on industry threats 
and trends as reported by peers/peer groups and third-
party providers.
*   Prioritizing threats observed in the organization’s network
    *   Example response: Threats from email attachments. We 
saw an increase in these attacks, so we decided to take 
action and block certain attachments.

When it comes to deciding what to focus on, 71% of respondents report that 
geopolitics play a very important or somewhat important role in determining 
requirements. See Figure 5.

A key geopolitical event in 2022 that influenced many teams’ 
requirements was the war in Ukraine, with 84% of respondents 
saying the conflict influenced their requirements in some way. See 
Figure 6.

This trend is understandable given the high-profile nature of the 
war and the anticipation by many intelligence analysts that it could 
lead to significant Russian targeting of US entities, particularly 
critical infrastructure. The effectiveness of the Department of 
Homeland Security (DHS) CISA Shields Up campaign, which aligned 
with respondents’ prioritization related to the conflict, is evident.
Although the conflict may not have resulted in all-out “cyberwar” 
as some analysts anticipated, the focus on defending against 
Russian threats may have resulted in improved defenses that 
thwarted many attacks.<sup>2</sup>

*Image Description: A pie chart titled "Geopolitics’ Influence on Requirements". The chart shows the distribution of responses regarding the importance of geopolitics in developing intelligence requirements. The categories are: "Very important", "Somewhat important", "A little important", "Not at all important", and "Unknown".*

*Image Description: A pie chart titled "Effect of the War in Ukraine". The chart shows the distribution of responses regarding how the war in Ukraine affected intelligence requirements in 2022. The categories are: "Significantly", "Somewhat", "A little", "Not at all", and "Unknown".*

<sup>2</sup> “Defending Ukraine: Early Lessons from the Cyber War,” https://blogs.microsoft.com/on-the-issues/2022/06/22/defending-ukraine-early-lessons-from-the-cyber-war/

## Sources
Just as requirements are key to focusing on the right questions or problem areas 
for an organization, information sources are vital to the quality, accuracy, and 
actionability of CTI. When it comes to sources of information gathered by CTI 
personnel, external sources such as commercial or open source threat feeds, news, 
and social media continue to be more commonly used than internal sources such as 
security event logging and forensics data. Consistent with the pattern that trending 
news is key in prioritizing intelligence 
requirements, 69% of respondents 
report external sources such as 
media reports and news as their 
primary information source. The 
most commonly used internal source 
they report is incident response 
and forensics data, used by 52% of 
respondents. See Figure 7.

This finding presents an opportunity 
for CTI personnel to remind 
themselves of the value of internal 
information, particularly from 
intrusions. This information can 
provide valuable insight, in particular 
because it specifically targeted that 
organization, meaning the threats are 
guaranteed to be relevant. Despite 
the value of internal intrusion 
analysis, there are many obstacles 
to getting this information, including 
that teams may not want to share it 
or may not have the resources to fully 
document findings from an intrusion.

Following external news sources, the 
second most commonly used source 
among respondents is community 
or industry groups, such as information sharing and analysis centers (ISACs) and 
Computer Emergency Readiness Teams (CERTs), with 66% of respondents reporting 
use of these sources. This finding suggests that these formal groups have a key role in 
disseminating information to CTI teams, because this source was more popular than 
other formal and informal groups used by 41% of respondents.

*Image Description: A bar chart titled "Information Sources". The chart shows the percentage of respondents who consider various types of information as part of their intelligence gathering. The categories are: "Threat feeds from CTI-specific vendors", "Threat feeds from general security vendors", "Open source or public CTI feeds", "Community or industry groups such as information sharing and analysis centers (ISACs) and Computer Emergency Readiness Teams (CERTs)", "Other formal and informal groups with a shared interest", "External sources such as media reports and news", "Social media", "Closed or dark web sources", "Incident response and forensics", "Security data gathered from internal IDS, firewall, endpoint, and other security systems", "Security analytics platform other than SIEM", "SIEM platform", "Application logs", "User behavior data", "Network traffic analysis packet and flow", "Vulnerability data", "Honey pot data", "Shared spreadsheets and/or email", and "Other".*

Other top sources include threat feeds, including from CTI vendors (used by 66% of 
respondents), open source (61%), and general security vendors (56%). These threat feeds 
are often made up of IOCs such as hash values, domain names, and IP addresses. 
One of the most common responses to the open-ended question about examples of 
CTI in action involves indicator use cases. Multiple respondents report that they use 
commercial or freely available IOCs to ingest into tools such as security information and 
event management (SIEM) and endpoint detection and response (EDR) to determine 
whether they are present on their network. This finding shows that even with the rise 
of tracking tactics, techniques, and procedures (TTPs), including with MITRE ATT&CK®, 
CTI personnel still find value in indicators as a key source. This is likely in part due 
to the ease of applying indicators in tools. Although indicators can play a role in CTI, 
organizations should consider, as their CTI function matures, how they can produce or 
consume beyond feeds of IOCs.

## Producing Intelligence
After CTI teams have identified appropriate personnel, established requirements, and 
collected information from many sources, they must analyze that information to produce 
intelligence outputs. Thoughtfully leveraged tools and processes help enable analysts to 
be efficient and thorough as they do this. Once intelligence outputs are produced, their 
work isn’t done yet; they still need to disseminate those outputs in an accessible way and 
obtain feedback to refine and improve future products.

### Production and Consumption
It is often said that intelligence is both a process 
and a product, and CTI is no different. CTI is both 
produced by following intelligence processes and is 
also consumed using a different set of processes. 
Some organizations analyze their own data about 
previous data breaches or network intrusions and 
generate intelligence products (or reports) based on 
that information. They may also generate raw data 
such as lists of IOCs that they can use internally 
and also share externally. CTI can also be consumed 
by organizations that take intelligence provided by 
external sources such as threat-intelligence vendors 
or information-sharing groups and apply it to their 
own internal processes. Many organizations use a 
combination of the two types, leveraging their own internal information, as discussed 
earlier, and also incorporating intelligence generated by others into their security 
processes. A few organizations—primarily threat-intelligence providers—only produce 
intelligence that is meant to be used by other organizations without consuming other 
sources of intelligence. See Figure 8.

*Image Description: A set of three bar charts titled "Use of CTI by Year". Each chart compares the percentage of respondents who produce, consume, or both produce and consume different types of threat intelligence across the years 2019, 2022, and 2023. The three types of threat intelligence are: "Published threat intelligence", "Contextual threat alerts", and "Raw threat data". Each chart shows the percentage of respondents who "Produce", "Consume", or "Both" for each year.*

This year’s survey shows that the highest number of respondents consume intelligence 
and that the numbers are rather consistent across the types of information that they 
consume: raw threat data, contextual alerts, and published threat intelligence. Of those 
who produce intelligence, their most common output is raw threat data consumed 
by other organizations, with 15% of respondents producing this output. This indicates 
how the field of threat-intelligence production has grown over the past few years. In 
2019, only 5% of respondents exclusively produced raw threat data, and 3% produced 
published threat intelligence. The doubling (and even tripling) of respondents in this 
space demonstrates the growing market for threat intelligence and the growing ability 
of vendors in this space to produce intelligence for consumption. Interestingly, aside 
from the increase in production, the balance of those consuming and both consuming 
and producing has remained relatively consistent over the past few years with one 
exception: Nearly 10% fewer organizations exclusively consume published intelligence 
reports, whereas the number of organizations producing and the number of organizations 
both producing and consuming intelligence reports have both increased, indicating an 
overall higher level of reporting available. Not only are there more reports by volume, but 
they are being produced by a greater number of organizations, which likely leads to an 
increase in the diversity of reporting perspectives and approaches. 

When we asked respondents to share examples of CTI at work, we can see some of the 
unique ways that organizations both consume and produce intelligence.

**Consume**
*   “We consume threat-intel data from other third parties in order to evaluate [our] 
overall security posture and also used by our threat-intel and incident-response 
teams to act on potential security breaches.”
*   “IoCs gathered from events on peer/similar/same region companies shared through 
a closed group.”
*   “External threat intel is used to support the prioritization of vulnerability 
management and remediation, primarily as an ‘escalator’ in cases where intel aligns 
with vulnerabilities aligns with exposure.”

**Produce**
*   “We produce threat intelligence from our IR practice; we share those findings 
publicly.”
*   “We produce internal intelligence reports from synthesis of external reports, 
identifying specific areas that are usable for our security operations, such as threat 
detection and threat-hunting opportunities.”

## Tools
As teams are producing and consuming CTI, various categories of tools can help them 
be successful and efficient. As they have for several years, spreadsheets reign supreme 
when it comes to tools used to aggregate and analyze CTI information, with 71% of 
respondents using them. This highlights that a simple spreadsheet remains a powerful 
and cost-effective way to help analysts organize information, even with the availability 
of CTI-specific tools. The second-ranked tool (59%) behind spreadsheets was a SIEM or 
other security analytics platform, demonstrating that CTI personnel are making use of 
tools that are likely already in their environment for use by other security operations 
teams. Open source threat-intelligence platforms (TIPs) ranked third, with 48% of 
respondents using these TIPs.

## Analytic Processes
With an increase in production of intelligence, it is important to pay attention to both 
the sources being used, as discussed earlier, and the analytic processes being used. This 
is the second year that we have asked survey respondents to share some information 
about the processes and techniques that they use when conducting analysis. We asked 
respondents about five different methods they commonly use in intelligence analysis and 
asked whether they use those methods 
frequently, occasionally, or never. The 
most commonly used method is intuitive 
or judgment-based analysis, followed very 
closely by threat modeling, and then the 
use of conceptual models such as the 
Diamond Model or Kill Chain. See Figure 9.

In both 2022 and 2023, respondents 
indicated that they use intuitive analysis 
and experience-based judgment most 
heavily, with nearly half of respondents 
using this method frequently. Experience 
and intuition can both be useful to 
analysts as they work to interpret threat 
data and synthesize insights, but because cognitive biases can lead to flawed analysis, it 
is important that analysts do not rely solely on them. The good thing is that most analysts 
do not exclusively rely on experience; they pair that beneficial experience with other 
methods of analysis to counter biases and use their intuition as a starting point rather 
than the entire process. In the past year, we have seen significant jumps in the number of 
people reporting that in addition to experience-based judgments they also frequently use 
conceptual models, structured analytic techniques (SATs), and inductive reasoning/graph-
driven analysis.<sup>3</sup> Most notable is the increase in those who frequently leverage SATs, which 
are methods specifically designed to counteract cognitive bias in analysis. In 2022, only 
19% reported that they frequently use SATs in analysis. In 2023, that number has jumped 
to over 30%!

*Image Description: A bar chart titled "CTI Methodologies". The chart shows the percentage of respondents who frequently or occasionally use various methods in CTI analysis. The categories are: "Intuitive or experience-based judgment", "Threat modeling", "Use of structured analytic techniques, such as key assumptions check, clustering, or Analysis of Competing Hypotheses (ACH)", "Inductive reasoning/graph-driven analysis", "Use of conceptual models such as the Diamond Model, Kill Chain methodology, or target-centric models", and "Other".*

<sup>3</sup> “There Is MOAR To Structured Analytic Techniques Than Just ACH! – SANS CTI Summit 2018,” https://www.youtube.com/watch?v=PtYWVzY2Ves

## Dissemination and Feedback
Once CTI has been produced—whether this production was done by a third-party partner, 
a vendor, or the CTI team itself—it needs to get to the right people or systems at the right 
time to enable them to make the best use of the intelligence. Another critical component 
of the dissemination process is gathering feedback to make sure that the intelligence 
benefited the organization. If it is not helping improve security or helping defenders make 
more insightful decisions, then something about the CTI process needs to be adjusted. 
Organizations should approach dissemination and feedback intentionally as a critical part 
of the intelligence process.

### Dissemination Methods
All the methods we asked about in the survey—emails, integrations with 
threat intelligence platforms, reports, and briefings—are each used by 
over 50% of respondents. This indicates that CTI personnel have to be 
prepared to disseminate information in different formats based on the 
goals and the audience. Several respondents described using both written 
reports and in-person or remote briefings for security-education and 
security-awareness purposes. The same content that organizations can 
use for security-awareness briefings—for example, a change in tactics in 
phishing campaigns—likely also has indicators that they can disseminate 
to security tools via a threat-intelligence platform, doubling the impact of 
the same threat-intelligence content.

### Impact of CTI
As previously mentioned, gathering feedback is one of the best ways to ensure that CTI 
is benefiting an organization. This holds true whether you are an in-house CTI team 
or individual or are part of a CTI team in a cybersecurity organization that provides 
intelligence to multiple partners. This year, 50% of respondents indicate that they measure 
the effectiveness of their CTI programs, and 
87% report that CTI has helped to improve 
security prevention, detection, and response. 
Of those who measure the effectiveness of 
their programs, the most common methods 
of measurement are first automated and then 
manual tracking of actions that they take based 
off of CTI. Many also use the time it takes to 
respond to an alert or incident as a measure 
of impact. Although CTI might not be able to 
prevent all incidents, it can help reduce the time 
it takes to respond to an issue. Interestingly, only 
23% get feedback directly from customers as a 
method of measuring impact. See Figure 10.

*Image Description: A bar chart titled "Measuring CTI Effectiveness". The chart shows the percentage of respondents who use various methods to measure the effectiveness of CTI. The categories are: "Automated tracking of all actions taken based on CTI", "Manual tracking of actions taken based on CTI", "Measure number of reports or written summaries disseminated", "Measure time to respond to alerts generated using CTI", "Measure time to respond to queries using CTI", "Measure number of legitimate alerts generated using CTI", "Measure number of preventions accounted for by using CTI", "Request feedback on performance directly from CTI consumers", and "Other".*

### A Note on RFIs
This year some respondents pointed out that it 
isn’t always the threat-intelligence team pushing 
information out to others. Sometimes other groups 
within an organization reach out to CTI teams with 
requests for information (RFIs). Responding to RFIs 
is a great way not only to provide information to 
the organization, but also for CTI teams to learn 
more about which types of information are helpful 
to others in the organization, which they can then 
use to generate future intelligence requirements. 
In fact, RFIs represent a type of feedback on what 
organizations find valuable.

Although we saw a lower number of respondents who directly solicit feedback, 
when we asked for examples of how they measure CTI impact, we received several 
responses that spoke to the importance of this type of feedback:
*   “We capture key success stories with our customers. How did our 
notification/report result in actions taken to improve security and reduce 
risk for our customers? How did our actionable information result in timely 
actions and decisions?”
*   “[We] meet regularly with consumers to discuss feedback from CT intel and 
collaborate on what is working, what needs improvement, what they would 
like to see.”
*   “Feedback from customers about effectiveness of defensive measures taken 
on the basis of [CTI].”

Gathering feedback, directly or indirectly, provides a great way to understand the 
impact of CTI and identify ways to improve or optimize the support being provided 
to other teams.

## Challenges and Limitations
This year’s survey highlights many ways that the CTI field continues to grow in 
maturity and capabilities, which we see from things such as an increase in the 
number of organizations with formal and 
documented intelligence requirements, the 
number of organizations with dedicated 
CTI teams, and an increase in the analytic 
methods organizations use to generate CTI. 
When it comes to challenges, we also see 
a decrease in challenges reported across 
the board. Although all these indications 
are promising, many organizations still face 
significant challenges when it comes to CTI. 
Survey respondents cite a number of areas 
that currently hold them back, including a 
lack of training, lack of staff, lack of time, and 
lack of automation. See Figure 11.

*Image Description: A bar chart titled "CTI Challenges". The chart shows the percentage of respondents who are inhibited from implementing CTI effectively due to various reasons. The categories are: "Lack of trained staff or lack of skills needed to fully utilize CTI", "Lack of time to implement new processes", "Interoperability issues/ lack of automation", "Lack of funding", "Lack of buy-in from partner teams (SOC, IR team, etc.)", "Lack of management buy-in", "Lack of technical capability to integrate CTI tools into our environment", "Lack of confidence in using the information to make decisions", and "Other".*

Lack of trained staff is a commonly cited challenge in the CTI space. Although we see 
many signs that the CTI field continues to mature, it is still a relatively new field in 
cybersecurity, and the growth of CTI teams can often outpace the training pipeline. In 2022, 
57% of organizations listed lack of trained staff as their number one challenge. This year, 
although staffing still remains the top challenge, that number has dropped down to 44% 
of organizations. Many great resources are available for those looking to get into the CTI 
field or those in other cybersecurity jobs who are interested in learning more about CTI. To 
get started, check out these blogs:
*   Cyber Threat Intelligence Self-Study Plan—Part I<sup>4</sup>
*   Cyber Threat Intelligence Self-Study Plan—Part II<sup>5</sup>
*   CTI Reading List<sup>6</sup>
*   SANS CTI Summit Presentations<sup>7</sup>

Despite the reduction in the number of challenges CTI teams face, lack of automation 
remains a hurdle to many and is the second most prevalent challenge experienced 
by CTI personnel. This area has grown steadily since 2017 and peaked in 2022. We can 
attribute the decrease of more than 10% to the rise in cybersecurity vendors providing 
threat-intelligence support, with many using 
their own platforms and tools as part of 
their processes. An improvement in these 
tools would have a significant impact on 
the overall industry, and many teams who 
struggle to optimize their workflows would 
welcome the change. See Figure 12.

*Image Description: A line graph titled "Lack of Automation". The graph shows the percentage of respondents who cite lack of automation as a challenge from 2017 to 2023. The percentages are: 2017: 25.4%, 2018: 38.5%, 2019: 44.0%, 2020: 47.8%, 2021: 45.1%, 2022: 53.6%, 2023: 42.1%.*

Many of these challenges are ones