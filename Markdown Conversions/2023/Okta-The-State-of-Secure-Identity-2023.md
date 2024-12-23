# 2023 Examining threats against your customer login box—and everything behind it The State of Secure Identity Report

## Table of Contents
- [Foreword: Securing customer authentication](#foreword-securing-customer-authentication)
- [Executive summary](#executive-summary)
- [The login box is a gold mine for bad actors](#the-login-box-is-a-gold-mine-for-bad-actors)
- [Protect and delight customers with CIAM](#protect-and-delight-customers-with-ciam)
- [Introduction to Customer Identity security](#introduction-to-customer-identity-security)
- [Consumers expect secure and convenient experiences](#consumers-expect-secure-and-convenient-experiences)
- [CIAM’s role in security identities and applications](#ciams-role-in-security-identities-and-applications)
- [Adapting secure authentication to millions of peoples’ desire for simplicity](#adapting-secure-authentication-to-millions-of-peoples-desire-for-simplicity)
- [AI has made it easier to deploy identity attacks at scale](#ai-has-made-it-easier-to-deploy-identity-attacks-at-scale)
- [Part 1: Before the login box](#part-1-before-the-login-box)
- [Host-layer defenses are the first line of defense](#host-layer-defenses-are-the-first-line-of-defense)
- [Platform and application layer defenses benefit from network effects](#platform-and-application-layer-defenses-benefit-from-network-effects)
- [Part 2: At the login box](#part-2-at-the-login-box)
- [Sign-up incentives attract bad actors](#sign-up-incentives-attract-bad-actors)
- [Credential reuse aids attackers in account takeovers](#credential-reuse-aids-attackers-in-account-takeovers)
- [Part 3: After the login box](#part-3-after-the-login-box)
- [Attackers value session tokens even more in a passwordless world](#attackers-value-session-tokens-even-more-in-a-passwordless-world)
- [Enhancing customer security and experience with CIAM](#enhancing-customer-security-and-experience-with-ciam)
- [Afterword: Authorization, the next frontier](#afterword-authorization-the-next-frontier)
- [Appendices](#appendices)

01
2023
Examining threats 
against your customer 
login box—and 
everything behind it
The State of Secure 
Identity Report
02
The State of Secure Identity Report 2023
Table of contents
Table of 
contents
03	
Foreword: Securing customer authentication
05	
Executive summary
07	
	
The login box is a gold mine for bad actors
09	
	
Protect and delight customers with CIAM 
13 	
Introduction to Customer Identity security
15		
	
Consumers expect secure and convenient experiences
17		
	
CIAM’s role in security identities and applications
19		
	
Adapting secure authentication to millions of peoples’ desire for simplicity
21		
	
AI has made it easier to deploy identity attacks at scale
23	
Part 1: Before the login box
25	
	
Host-layer defenses are the first line of defense
27	
	
	
Platform and application layer defenses benefit from network effects
29	
Part 2: At the login box
31		
	
Sign-up incentives attract bad actors
39	
	
Credential reuse aids attackers in account takeovers
59	
Part 3: After the login box
61		
	
Attackers value session tokens even more in a passwordless world
65	
Enhancing customer security and experience with CIAM
69	
Afterword: Authorization, the next frontier
71 	
Appendices
04
The State of Secure Identity Report 2023
## Foreword: Securing customer authentication
Rapid innovation and widespread access to information 
have revolutionized the demand for Identity solutions 
within the last decade. Identity is now the primary 
enterprise security entry point for consumer and 
workforce applications. Meanwhile, identity attacks 
have increased in volume and complexity. As an 
industry leader, Okta has a responsibility to champion 
a higher standard of identity security.  The Okta Secure 
Identity Commitment is our long-term commitment to 
lead the industry in the fight against identity-based 
attacks.  We will achieve this by providing market-
leading secure products & services, hardening our 
corporate infrastructure, championing customer 
best practices and elevating our industry to be more 
protected from identity attacks.
In that context, this report aims to elevate industry 
understanding of key customer identity security 
trends, and share best practices.
Securing the login box is one of the most critical 
steps of identity security. Through authentication, an 
essential function of Customer Identity and Access 
Management (CIAM) services, the login box attempts 
to confirm a customer’s digital Identity — the set of 
attributes that define a particular user (or non-human 
entity, like a specific device or system) in the context 
of an application.
But legitimate users aren’t the only ones interested in 
what’s behind the login gateway. There’s money to be 
made for those who can break in, and economic forces 
have led to the emergence of an entire ecosystem of 
technologies, services, and other resources to enable 
such intrusions.
Across industries, attacks against entities large and 
small continue to accelerate. As cybercriminals direct 
more effort and expertise into getting past the login 
box — including by leveraging the same artificial 
intelligence (AI) capabilities that are transforming 
society and business — protecting it requires ever-
more layers of ever-more sophisticated defenses.
Complicating matters is the reality that customer portals 
— whether business-to-consumer (B2C) or business-
to-business (B2B) — generally have to be accessible on 
the public internet. Plus, the authentication experience 
has to be visible enough to create a sufficient level of 
trust for the customer, but seamless enough to not 
impose any unnecessary inconvenience.
For many years, customer authentication generally 
relied upon a knowledge factor — usually a password 
— presumed to be known only to the legitimate 
user and the application provider. But time and 
time again, this presumption has been proven false: 
knowledge can be stolen or learned (e.g., via Open 
Source Intelligence), passwords in particular are a 

problem, and both application providers and the CIAM 
services upon which they rely need to pull customers 
to more secure authentication factors. They also 
ideally need to get customers to enroll in multi-factor 
authentication (MFA).
Up until a few years ago, an argument could be 
reasonably made that it was impossible (or at least 
impractical) to simultaneously satisfy the need 
for secure authentication with the imperative of 
a convenient user experience — that a trade-off 
was required — and that MFA was too unwieldy for 
widespread adoption, especially within B2C contexts.
But with the growing availability of passkeys — and 
synced passkeys in particular — we are now at the 
point where those arguments break down. In fact, we 
believe that the arrival of synced passkeys will be looked 
back on as a major milestone in securing Customer 
Identity. Plus, even setting aside their security benefits, 
passkeys have already proven to deliver a convenient 
and familiar user experience that, in many ways, 
surpasses the usability of other approaches.
And passkeys haven’t arrived a moment too soon. 
Today, digital identities control access to an ever-
growing number of applications and services, 
impacting — and to some degree governing — many 
aspects of modern living. Tomorrow, their impacts will 
be even larger, making authentication, authorization, 
and CIAM in general vital to preserving trust, security, 
and privacy. Consequently, CIAM also plays a central 
role in accessibility, and it’s up to Identity practitioners 
to determine whether that role widens or helps to close 
the digital divide.
In this report, our third annual State of Secure Identity, 
we aim to increase awareness of threats to customer 
Identity and of the defensive measures that should be 
in place to withstand these threats. We’ve switched 
things up a bit this year, and structured the report as a 
three-part journey:
	
- Before the login box, because as much as the 
login box needs to be generally accessible, it really 
shouldn’t be presented to everyone
	
- At the login box, where Identity battles rage 

every day
	
- After the login box, because securing access 
doesn’t stop just because a user made it past the 
gatekeeper
Thank you for joining me — and all of us at Okta — on 
this journey.
Shiven Ramji 
President, Customer Identity Cloud, Okta
Foreword
Securing 
customer 
authentication
06
The State of Secure Identity Report 2023
CIAM is a unique segment of the wider Identity and 
Access Management (IAM) space, as customer-facing 
applications must deliver an experience that’s user 
friendly, secure, and private while being fully exposed 
to an ever-changing threat landscape.
This report shows that signup fraud, credential stuffing, 
and MFA bypass are all everyday threats that must be 
managed by practically every customer login box.
## Executive summary
08
The State of Secure Identity Report 2023
## Executive summary
This report reveals that from January 1, 2023 through 
June 30, 2023:
13.9% of attempted account registrations met the 
Okta Customer Identity Cloud, powered by Auth0, 
criteria of a signup attack:
	
- Of the 10 industries with the most significant 
representation within the Customer Identity Cloud, 
four stood out as experiencing particularly high 
proportions of fraudulent registrations: Financial 
Services (28.8%), Media (28.4%), Manufacturing 
(25.1%), and Software/SaaS/Tech (24.0%)
	
- On the ‘busiest’ day for signup fraud, the 
technology identified nearly 10 million fraudulent 
registration attempts
	
- On April 15, more than 64% of account registration 
attempts were assessed to be fraudulent
24.3% of login attempts overall met the Customer 
Identity Cloud’s criteria of credential stuffing:
	
- Of the 10 industries with the most significant 
representation within the technology, Retail/
eCommerce (51.3%), Media (42.3%), Software/
SaaS/Tech (32.1%), and Financial Services (30.3%) 
all experienced higher-than-average proportions 
of credential stuffing
	
- On the ‘busiest’ day for credential stuffing 
attempts, the technology identified more than 27 
million such events
	
- On January 1, more than 46% of login attempts 
were attributed to credential stuffing
12.7% of MFA attempts met the Customer Identity 
Cloud’s criteria of being malicious (i.e., MFA 
bypass):
	
- Of the 10 industries with the most significant 
representation within the technology, Media 
(12.8%), Financial Services (10.9%), Manufacturing 
(7.8%), and Software/SaaS/Tech (6.4%) 
experienced the highest proportion of MFA bypass 
attempts
	
- On the ‘busiest’ day for MFA bypass attempts, the 
technology identified  more than 750,000 such 
incidents
	
- On June 11, MFA bypass attempts accounted for 
more than 30% of all MFA attempts
An organization’s industry vertical isn’t the only factor 
influencing the threats it faces. For example, small 
businesses and enterprises seem to be targeted at a 
higher rate — with fraudulent registrations, credential 
stuffing attempts, and MFA bypass attempts — than 
mid-market organizations. A reasonable interpretation 
is that cybercriminals consider enterprises as 
comparatively valuable targets and small businesses 
as comparatively easier targets.
And even the region in which an organization is 
headquartered has an effect; companies based in 
Asia-Pacific (APAC) experienced by far the highest 
rates of fraudulent registration, while those based in 

the Americas (AMER) faced significantly more 
credential stuffing. 
[1] Proportion of total registration attempts
[2] Proportion of password authentication attempts
[3] Proportion of total MFA attempts
[4] Please see the Methodology section for an explanation of why all three regions are below the global average
Executive summary
## The login box is a gold mine for bad actors
Fraudulent 
registration 
attempts1
Credential 
stuffing 
attempts2
MFA 
bypass 
attempts3
Rate
Rank
Rate
Rank
Rate
Rank
Overall (technology wide)
13.9%
—
24.3%
—
12.7%
—
10 most-
represented 
industries
Advertising/marketing
1.0%
10
16.7%
6
3.4%
9
Financial services
28.8%
1
30.3%
4
10.9%
2
Food/beverage/hospitality
9.0%
8
11.4%
8
5.5%
5
Healthcare
6.3%
9
16.1%
7
4.6%
7
Manufacturing
25.1%
3
17.7%
5
7.8%
3
Media
28.4%
2
42.3%
2
12.8%
1
Professional services
13.4%
5
7.2%
10
4.5%
8
Retail/eCommerce
9.3%
7
51.3%
1
5.0%
6
Software/SaaS/tech
24.0%
4
32.1%
3
6.4%
4
Travel/transportation
9.7%
6
7.2%
9
2.9%
10
Organization 
size
Enterprise
19.9%
1
39.4%
1
9.5%
2
Mid-market
12.6%
3
20.1%
3
9.0%
3
Small business
19.4%
2
30.9%
2
20.3%
1
Organization 
HQ location
AMER
9.4%
2
28.0%
1
12.0%
14
APAC
27.9%
1
13.3%
3
11.0%
2
EMEA
8.1%
3
20.2%
2
7.6%
3
Table 1: Summary of Identity attack rates as determined by the Customer Identity Cloud technology (January 1, 2023 through June 30, 2023)
10
The State of Secure Identity Report 2023
While Workforce Identity management can 
accommodate comparatively higher friction and can 
often count on a user base that has undergone security 
awareness training, CIAM lacks these factors and 
must instead rely on more subtle security techniques 
to achieve and maintain a strong and resilient posture 
while preserving convenient user experiences.
Because customer expectations are always growing 
and the threat landscape is always evolving, these 
techniques must be continuously tuned to achieve the 
appropriate balance of user experience, security, and 
privacy — a balance that itself varies based upon each 
organization’s risk profile and appetite.
Executive summary
## Protect and delight customers with CIAM
The State of Secure Identity Report 2023
Executive summary
12
Implement layered defenses
Straightforward controls — including rate limiting, 
suspicious IP blocking, and breached password 
detection — are all necessary defensive measures, but 
by themselves are insufficient.
Similarly, effective password policies (e.g., requiring 
strong passwords, having a secure reset process) and 
good session hygiene (e.g., keeping session tokens 
out of URLs, generating new and unpredictable tokens 
after login) are fundamental requirements, but only part 
of the solution.
As cybercriminals invest in bypassing security 
measures, CIAM services and application providers 
must also scale their investments in next-generation 
defenses.
For example, Bot Detection, with Okta AI has proven 
capable of filtering nearly 80% of bots targeting 
authentication systems. Importantly, these defensive 
capabilities were achieved without introducing 
unnecessary user friction; by carefully training 
and continually tuning the AI at the heart of the Bot 
Detection feature, we can ensure that human users 
are rarely presented with a CAPTCHA, preserving 
seamless experiences.
Plus, there’s considerable evidence that this efficacy 

is a very strong deterrent; some of our largest 
customers saw their 90-day average of bot traffic drop 
by nearly 90% after enabling this Attack Protection 
feature — indicating that cybercriminals prefer going 
after easier targets.
Strengthen authentication
We can’t overstate how much potential passkeys have 
to dramatically strengthen customer authentication 
compared to password-based logins. Passwords 

are at the root of many Identity threats, and passkeys 
represent a major step in relegating passwords to a 
much smaller role:
	
- Synced passkeys in particular deliver strong 
authentication in a familiar and convenient manner 
—  making them beautifully suited to mainstream 
consumer demographics, which are especially 
sensitive to friction (in fact, as of October 10, 2023, 
Google offers passkeys as the default option 
across personal Google Accounts)
	
- Device-bound passkeys are a great option for 
B2B markets and other customer applications 
that require the even stronger authentication that 
comes from FIDO-Certified authenticators and 
security keys
MFA in general also has a continuing role in 
strengthening customer authentication. In the past, 
customer-facing organizations were hesitant to 
introduce and encourage — let alone require — MFA 
out of concern that the additional friction would 
impede conversions. However, those objections no 
longer apply (and really haven’t for a few years):
	
- Adaptive MFA allows application providers to 
reserve MFA challenges only for risky logins, where 
riskiness is a function of many threat signals
	
- Step-up authentication allows application 
providers to provide access to low-risk resources 
via a comparatively weaker authentication 
mechanism (e.g., a password), while reserving 
stronger authentication (e.g., MFA) for when a user 
wants to access a more sensitive resource
However — and as we’ve seen — threat actors are 
investing more resources in bypassing relatively 
weaker MFA factors, so it’s essential that application 
providers migrate customers to authenticators based 
on possession or biometric factors.
Build or buy?
Building such a layered CIAM solution in-house is a 
massive undertaking that’s well beyond the capacity 
of all but the most well-resourced of enterprises. 
Nevertheless, such layers and technologies are 
required to deliver convenient and secure customer 
experiences that preserve privacy.
For most organizations, an agile, secure-by-design 
CIAM solution is the most effective and efficient 
approach, as it will allow them to tailor Customer 
Identity and Access Management — and continually 
tune as needed — without drawing in resources better 
applied toward advancing core competencies.
Third-party authentication makes a 
meaningful difference
A recent global survey of application 
development team members underscored the 
value of incorporating third-party authentication 
into SaaS applications.
Based upon 675 responses from professionals 
in 56 countries, the survey found that:
	
- Authentication as a function takes the 
third-most time to build and maintain 
in-house, behind only Data Management 
and Storage, and DevOps Tooling and 
Automation
	
- Third-party authentication reduces 
time to market more than any other 
SaaS component: 88% of organizations 
that use a third-party SaaS platform for 
authentication report reducing time to 
market in the last year
Learn more in How development teams 
purchase SaaS 
14
The State of Secure Identity Report 2023
## Introduction to Customer Identity security
Securing Customer Identity should be a top-tier priority 
for any application or service provider, for the simple 
reason that people other than legitimate users want 
access to whatever’s behind your login box — and 
these malicious actors are willing to invest considerable 
effort to get what they want.
With this, our third annual State of Secure Identity 
Report, we aim to increase awareness of:
	
- Threats to Customer Identity
	
- The techniques available now that can be layered 
to build robust and reliable defenses
To achieve these goals, we’ll explore today’s most 
common and most dangerous attack patterns, 

and the broad trends that are shaping tomorrow’s 
threat landscape.
Where possible, we’ll provide data from Okta Customer 
Identity Cloud, powered by Auth0 — which provides 
CIAM functionality to thousands of organizations large 
and small — to illustrate the prevalence and impact of 
Identity threats.
But before we get into the specifics, it’s worth taking 
a moment to review the unique context of Customer 
Identity, in particular:
	
- The need to deliver convenient experiences that 
are also secure
	
- The vital role of Customer Identity and Access 
Management (CIAM)
	
- The ongoing evolution of authentication 
mechanisms
	
- The double-edged sword of artificial intelligence (AI)
16
The State of Secure Identity Report 2023
For any organization serving customers through a 
digital channel, minimizing the friction inherent within 
each and every interaction is vitally important. In 
practical terms, this means minimizing clicks, designing 
intuitive user interfaces (UIs), reducing latency, and 
delivering a consistent and convenient user experience 
(UX) across the full range of channels (e.g., websites 
and apps).
To protect their services and legitimate customers, 
organizations must also implement security measures 
that can withstand a broad range of Identity-related 
attacks. An idealized Identity implementation provides 
infinite friction for attackers and something near zero 
— because a little bit of friction in the right place at the 
right time can help to build trust — for genuine users.
While such a solution is a worthy objective, the real 
world frequently involves tradeoffs. For example, 
deploying a mechanism to detect and impede 
large-scale, scripted bot attacks may increase an 
application’s overall resilience — but at the expense of 
some number of human users being presented with a 
security challenge.
Once deployed, the mechanism can be fine-
tuned based upon operational insights to strike 
the appropriate balance between security and 
convenience. Practically, this balance will vary from 
application to application, organization to organization, 
and industry to industry, because each combination 
of customer base, threat landscape, and security 
preferences is unique. To complicate matters further, 
the balance may shift over time, as threat actors adjust 
their Tactics, Techniques, and Procedures (TTPs) and 
select new targets, and as customer desires shift.
But organizations that put in the effort and find a 
balance stand to reap significant rewards. For example, 
Okta’s Customer Identity Trends Report 2023, based on 
a global survey of 21,512 consumers from 14 countries, 
revealed that nearly 60% of survey respondents would 
be more likely to spend money when services offered 
a simple, secure, and frictionless login process (Figure 
1) — with the much-coveted younger demographics 
especially favoring such convenient experiences. 
Introduction to Customer Identity security
## Consumers expect secure and convenient experiences
Introduction to Customer Identity security
100%
90%
80%
70%
60%
50%
40%
30%
20%
10%
0%
Share of respondents
18 to 29 years
30 to 39 years
40 to 49 years
50 to 59 years
60 plus
Retail and
hospitality
Financial services
and insurance
Public sector
Healthcare
Transportation
and travel
Media and
entertainment
Figure 1: Consumers are more likely to spend money with a brand online if they know the 
login experience is simple, secure, and frictionless.
The graphs show the sum of “Very likely” and “Somewhat likely” responses.
18
The State of Secure Identity Report 2023
A bot detection mechanism like the one outlined above 
is only a single element within an Identity security stack, 
and Identity security is only one aspect of Customer 
Identity and Access Management.
Modern CIAM solutions empower organizations to 
balance convenience, privacy, and security for every 
type of user who needs access to their applications 
and services. CIAM also allows companies to 
continually evolve the UX, to minimize the demand on 
the engineering team for Identity-related capabilities 
— thereby allowing them to focus on core features 
— and to efficiently and effectively meet regulatory, 
certification, and contractual requirements.
In Identity terms, the three essential features of 
an effective CIAM solution are authentication, 
authorization, and Identity management:
	
- Proper authentication ensures that the users 
logging into accounts are who they say they are.
	
- Effective authorization helps businesses to 
provide a user with the appropriate level of access 
to an application and/or resources.
	
- Comprehensive Identity management allows 
administrators to update user access permissions 
and implement security policies; this feature 
also enables customers to manage — to the 
extent permitted by the use case and required 
by regulations — their own identities, data, and 
preferences.
While the literal definition of CIAM has remained 
consistent, its true meaning — in terms of what use 
cases it enables, using what functional components, 
for what types of organizations — has evolved, 
especially in recent years. Today, CIAM is essential for:
	
- Serving consumers: In the business-to-consumer 
(B2C) world, an effective CIAM implementation 
enables highly personalized promotions and 
recommendations that drive additional revenue 
and create more value for your customers — all 
while ensuring a convenient user experience 
across your digital channels.
	
- Empowering business customers: Countless 
organizations rely on business-to-business (B2B) 
SaaS applications as essential enablers. However, 
different users within each organization need 
different levels of access to different resources, 
and creating a convenient and secure experience 
requires precisely managing Identity and 
access privileges. CIAM provides the answer by 
empowering B2B SaaS customers to self-manage 
Identity.
	
- Enabling constituents, partners, and other 
known third parties: In consumer and SaaS 
applications, customers manage their own 
identities, but there are many scenarios where 
Identity must be managed by the organization 
providing the service. To fulfill use cases where 
customer identities are known to, and provisioned 
by, the service provider, CIAM provides all the tools 
organizations need to manage customer account 
creation, maintenance, and end of life.
Within a Workforce Identity context, administrators can 
impose controls with comparatively less regard for the 
user experience. In the world of Customer Identity, the 
need to minimize (or at least carefully manage) friction 
creates challenges — particularly with respect to 
authentication. 
Introduction to Customer Identity security
## CIAM’s role in securing identity and applications
Introduction to Customer Identity security
20
The State of Secure Identity Report 2023
Current state: MFA adoption
While the Zero Trust paradigm represents a major 
change in the Workforce Identity world, CIAM has 
always operated in a world without trust. In almost 
every pure CIAM use case, neither the application 
provider nor the Identity provider has control over the 
endpoints from which the service is being accessed.
To establish enough trust to enable an interaction or 
transaction — i.e., to grant some level of access — 
Identity flows require each user to present one or more 
authentication factors:
	
- Knowledge: Something that the user knows, such 
as a password or the answer to a security question
	
- Possession: Something that the user has, such as 
a phone or access to an email account
	
- Inherence: Something that the user is, 
corresponding to a biometric attribute like 
a fingerprint, face, or voice profile; in most 
implementations, the device attests that the person 
attempting to authenticate is the same person who 
originally set up this type of authentication
But what started as a simple login box filled in by 
humans has changed dramatically over the years:
	
- Passwords got more complex: As attackers 
became adept at guessing weak passwords and 
taking advantage of widespread password reuse, 
requirements about complexity evolved, leading 
to ever-longer passwords with special characters, 
combinations of upper and lowercase letters, and 
numbers
	
- Password management matured: This forced 
users to grapple with more — and more complex 
— passwords, and drove adoption of password 
managers (whether implemented in a browser or 
in a separate application)
	
- MFA’s importance grew: As phishing became 
a widespread threat and huge password dumps 
appeared online, MFA gained support as an 
effective defense against account takeovers 
(ATOs)
Unfortunately, the friction associated with traditional 
MFA techniques has resulted in low consumer adoption; 
plus, many older MFA techniques are now under threat, 
with attackers finding scalable and economic ways to 
bypass this important barrier.

Introduction to Customer Identity security
## Adapting secure authentication to millions of peoples’ desire for simplicity
As authentication techniques and attacker TTPs 
evolved, CIAM solutions introduced new layers of 
Identity security to defend against a wide array of 
automated cyberattacks that both cost organizations 
money and that threaten the privacy of customers.
Inching ever-closer to the idealized solution, modern 
security measures include approaches like adaptive 
MFA and step-up authentication — both of which 
aim to only create friction when a sufficient level of 
risk exists. Key to deciding exactly when a security 
challenge is needed — that is, to maintain the optimal 
balance between security and convenience — are 
intelligent systems that ingest risk signals and other 
context (e.g., the level of access being requested) to 
assess risk, choose an appropriate authentication 
challenge, and so on.
In fact, artificial intelligence (AI) has long been 
embedded within Identity systems, and AI’s importance 
is undoubtedly going to increase (even looking beyond 
security, AI can be leveraged to craft better customer 
experiences).
However, while AI is many things, it’s also just another 
tool that can be wielded for good or ill. 
22
The State of Secure Identity Report 2023
Introduction to Customer Identity security
Introduction to Customer Identity security
## AI has made it easier to deploy identity attacks at scale
On a basic level, artificial intelligence can be 
understood as a decision made by a computer where 
its “smartness” is indistinguishable from a human-
made decision — no matter how the decision is made.
The original premise can be traced back to 1943, long 
before the invention of the digital stored memory 
computer, when logician Walter Pitts and neuroscientist 
Warren McCulloch tried to create a mathematical 
representation of the neurons in a human brain.
Since the 1960s, AI has evolved into a very large 
collection of algorithms, which can perform various 
tasks. One of those tasks is the detection and 
recognition of patterns, and is usually called machine 
learning (ML). The ML field has advanced quite 
dramatically in the last 15 years due to progress 
in the construction and manipulation of neural 
networks — and with ever-more powerful computers, 

neural networks can be made "deeper" (or larger), 
resulting in the emergence of practical and economic 
deep learning.
But the AI development that has taken the wider world 
by storm is the incredible — and many would say 
shocking — arrival and rapid evolution of generative 
AI, driven mainly by remarkable advances in Large 
Language Models (LLMs).
Suddenly, writing prose and creating complex (and 
lifelike, if that’s the intention) images are no longer the 
sole domain of humans. And what’s more, because 
LLMs are so adept at writing — including programming 
— and so many things are now controlled by software, 
LLMs are behind unexpected breakthroughs and 
advances in a wide range of domains.
In the context of Identity security, advances in AI make 
the threat landscape more dangerous in a few ways. 
For example, AI can:
	
- Make existing low-quality, high-intensity 
Identity attacks more dangerous: Credential 
stuffing, fraudulent registrations, SMS pumping 
schemes, and other attacks may become harder 
to detect, and more effective/destructive
	
- Enable entirely new types of Identity attack: 
Some new attacks will be anticipated by defenders 
or discovered in advance by researchers, but 
others will only become apparent once they’re 
spotted in the wild (i.e., the “unknown unknowns” 
problem)
	
- Overcome some existing security measures: 
AI-based tools have already demonstrated the 
ability to solve CAPTCHAs and to use trick voice 
biometric systems via deepfakes
Plus, the coding and scripting abilities of generative 
AI makes it easier for threat actors of any skill level 
(i.e., with or without coding abilities) to launch attacks, 

in general, potentially drawing more participants 
into the cybercrime ecosystem and improving their 
operational efficiencies.
Enabling scalable and cost-effective 
personalized attacks
But perhaps the most dangerous new Identity threat 
is that AI enables spear phishing at a massive scale. 
Consider this plausible attack pipeline:
1.  A threat actor selects an organization to target
2.  The threat actor uses open-source intelligence 
(OSINT) techniques to compile a list of employees
3.  The threat actor feeds this list into a social search 
API (there are many options available), which then 
returns a list of social media accounts associated 
with each employee
4.  The threat actor programmatically filters the list 
to identify employees with open and active social 
media accounts, then starts examining each to 
identify who the user follows, what posts they like, 
what they post, when they're active, etc.; the threat 
actor can even perform subject-based sentiment 
analysis to build highly personalized psychological 
profiles, and can update these profiles over time
5.  The threat actor follows each employee on 
the available social applications, and begins 
interacting in completely benign ways (e.g., liking 
and resharing posts, adding comments, etc.) to 
establish a rapport
6.  The threat actor monitors current events, news, 
and trends for an opportunity to engage with each 
employee on a personal level
7.  The threat actor crafts an email (or direct message, 
on any medium) and reaches out to each target 
employee
8.  If a target engages, then the conversation can 
continue until enough trust has been established 