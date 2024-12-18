3
2
0
2

UNIT 42 
ATTACK SURFACE 
THREAT REPORT

Lessons in Attack Surface Risk 
Based on Observable Data

S
T
N
E
T
N
O
C

F
O

E
L
B
A
T

01

02

03

04

05

06

07

08

09

10

Executive Summary

Attackers Move at Machine Speed

Top Attack Surface Exposures

Remote Access Exposures Lead to Ransomware

Cloud Dynamism Is Straining Security Controls

Cloud Exposures Dominate Most Organizations’ Security Risks

Industry Attack Surface Breakdown

Conclusion

Recommendations

Methodology

 
 
EXECUTIVE 
SUMMARY

Modern organizations are racing to update their 

To put these sweeping changes into context and 

enterprise network architectures to take advantage 

provide actionable intelligence, Unit 42 analyzed 

of Zero Trust security designs, cloud computing, 

several petabytes of public internet data collected 

software\-as\-a\-service (SaaS) value delivery, and 

by Cortex Xpanse — the Palo Alto Networks attack 

distributed workforces. This has fueled a dramatic 

surface management solution — in 2022 and 2023\. 

increase of infrastructure, known and unknown, 

This report outlines aggregate statistics about how 

which in turn has greatly increased the complexity 

attack surfaces worldwide are changing and drills 

of securing their environments. 

down into particular risks that are most relevant to 

the market.

Exposures on publicly facing assets put them 

at risk of being compromised, and sometimes 

this leads to organizations becoming victims of 

opportunity as opposed to a targeted attack. 

Understanding what you need to protect is a 

precursor to any successful cybersecurity program 

— but companies and government agencies struggle 

to understand what they own and what services 

expose the most risk.

01 NEXT CHAPTER

3

UNIT 42 \| CORTEX01

Executive summary

Key Findings

• Constant change in the cloud creates new risk. Cloud\-based IT infrastructure is 

always in a state of flux. In a given month, an average of 20% of an organization’s 

cloud attack surface will be taken offline and replaced with new or updated 

services. The deployment of these new services is generally responsible for 

nearly half of the organizations’ new high or critical cloud exposures every month.

• Remote access exposures are widespread. Over 85% of organizations analyzed 

had Remote Desktop Protocol (RDP) internet\-accessible for at least 25% of the 

month, leaving them open to ransomware attacks or unauthorized login attempts.

• Cloud is the dominant attack surface. A vast 80% of medium, high, or critical 

exposures belonging to the organizations analyzed were observed on assets 

hosted in the cloud.

NEXT CHAPTER

4

01

Executive summary

Recommendations

Obtain continuous, comprehensive visibility 

Monitor remote access services 

Maintain a complete and up\-to\-date inventory of 

Monitor all remote access points and usage to 

your organization’s assets both on\-premises and 

eliminate the risk of unauthorized logins.

in the cloud to ensure consistent application of 

governance policies.

Manage your attack surface at machine speed 

Attackers are utilizing automation to move at 

Transform your vulnerability mindset 

machine speed. It’s critical that your organization 

A lot of security breaches involve exposures 

is able to move at machine speed as well by 

due to issues such as misconfigured 

leveraging attack surface management tools 

services, misconfigured firewalls, or even 

which provide proactive prioritization and enable 

known vulnerabilities. Legacy vulnerability 

automatic remediation of common exposures.

management processes fail to identify many of 

these issues, much less assist your organization 

in resolving them.

Your security teams face challenges in attack 

surface management, including understanding 

current threats, maintaining a comprehensive asset 

Enable your team to respond quickly to 

inventory to avoid unknown risks, and quickly 

emerging threats 

addressing all risks on those assets. Any exposure 

When critical vulnerabilities arise, quickly 

or vulnerability in an internet\-accessible system 

understand your risk exposure for patch 

gives attackers an opportunity to harm your 

prioritization and mitigation of unpatchable end\-

organization, causing downtime, data loss, financial 

of\-life services.

setbacks, and potential brand reputation damage. 

By actively managing your attack surface, you 

proactively and automatically mitigate risks, staying 

a step ahead.

NEXT CHAPTER

5

ATTACKERS 
MOVE AT 
MACHINE SPEED

Attack surfaces are constantly changing, 

As we will explore in this report, attackers have 

making it difficult for security teams to secure 

been observed exploiting vulnerabilities in the wild 

them. Defenders must remain vigilant as every 

within hours of their public disclosure. According 

configuration change, new cloud instance, and 

to previous research, we found that on average, 

vulnerability disclosure present an opportunity 

an organization takes more than three weeks to 

for attackers. 

investigate and remediate a critical exposure.1 Even 

the largest, most\-sophisticated, and best\-resourced 

Today’s attackers have the ability to scan the 

security teams struggle to remediate critical 

entire IPv4 address space for vulnerable targets 

exposures as quickly as attackers can test and field 

in minutes. 

new capabilities.

02 NEXT CHAPTER

6

UNIT 42 \| CORTEX02 Attackers Move at Machine Speed

Exploit Intelligence Confirms 
the Need for Rapid Response

Unit 42 analyzed 30 Common Vulnerabilities and 

Exposures (CVEs) from May 2022 to May 2023 to 

characterize how quickly adversaries were able to 

begin exploiting them. Researchers selected these 

CVEs based on threat intelligence about exploitation 

activity. Figure 1 shows the selected CVEs. Notably, 

three of the 30 vulnerabilities were exploited within 

hours of the CVE public disclosure. Nineteen of the 30 

vulnerabilities were exploited within 12 weeks of the 

public disclosure, highlighting the risks associated with 

incomplete and inconsistent patching programs.

Figure 1: Time elapsed before the first reported attack against 30 vulnerabilities 
exploited by a known threat actor in the last 12 months

NEXT CHAPTER

7

02 Attackers Move at Machine Speed

Ransomware Threat Actors 
Exploit Critical Vulnerabilities 
Within Hours of Publication

Unit 42 analyzed 15 remote code execution (RCE) 

vulnerabilities actively used by ransomware 

operators (shown in figure 2\). These CVEs were 

selected based on intelligence information about 

the threat actor group and their active exploitation 

within 12 months of publication. Threat actors 

targeted three of these critical RCE vulnerabilities 

within hours of disclosure, and six of the 

vulnerabilities were exploited within eight weeks 

of publication.

Figure 2: Time elapsed before the first reported ransomware attack against 15 RCE 
vulnerabilities by a known threat actor in the last 12 months

NEXT CHAPTER

8

TOP ATTACK 
SURFACE 
EXPOSURES

03 NEXT CHAPTER

There are two broad categories of risks associated 

• Examples include moving laterally across 

with the compromise of an internet\-accessible 

an internal subnet to exfiltrate data from 

asset for an organization:

a critical datastore, compromising virtual 

private network (VPN) infrastructure to 

1\. Risks related to attacker actions taken on a 

access and infect source code repositories 

compromised device that can directly harm 

in supply chain attacks, and using a 

the organization: 

compromised IP security camera to record 

• Examples include exfiltration of 

sensitive documents stored on an 

internet\-accessible corporate laptop, 

ransomware attacks that disrupt 

payments processing, and physical 

damage from a compromised building 

control or industrial control system. 

employees physically entering 

login credentials.

In general, when a device is compromised on 

the attack surface, it can pose both kinds of 

risks to organizations. Unit 42 categorized these 

risks according to the business function of a 

device, which relates strongly to the nature and 

severity of risk its compromise could pose to an 

2\. Risks related to how an attacker can leverage 

organization. The total risk an attack surface poses 

unauthorized access on a compromised attack 

to an organization is thus related to the volume 

surface asset to gain further unauthorized 

of exposed assets vulnerable to compromise, the 

access to other organizational IT resources, 

consequence of those assets being compromised, 

including those not directly accessible over 

and the duration of time those assets are exposed 

the public internet: 

relative to the time it takes attacker groups to find 

and exploit them.

9

UNIT 42 \| CORTEX03 Top Attack Surface Exposures

Web framework takeover exposures, as mentioned 

in figure 3, make up 22% of exposures observed 

across the 250 organizations; attackers actively 

seek out and target websites running vulnerable 

software because they are so prevalent. The most 

common exposure types were insecure versions of 

Apache web servers, insecure versions of PHP, and 

insecure versions of jQuery.

Remote access services account for 20% of 

exposures. These exposures include services 

like RDP, Secure Shell (SSH), or virtual network 

computing (VNC). When compromised, these 

services allow attackers to gain unauthorized 

access to an organization’s network or systems, 

potentially leading to financial losses, reputational 

damage, or other consequences. In addition, RDP 

has been shown to be a leading vector for business 

interruption via ransomware.

Figure 3: Distribution of exposure categories observed across the 250 organizations in the last 12 months

NEXT CHAPTER

10

03

Top Attack Surface Exposures

IT and networking infrastructure exposures 

File sharing exposures account for 12% 

Unit 42 also observed other types of 

comprise 17% of exposures that Unit 42 observed. 

of exposures and pose significant risks to 

exposures, including:

Exposures in this category include application\-

organizations, including data breaches. Examples 

layer protocols like Simple Network Management 

of insecure file sharing include publicly accessible 

• Unpatched, misconfigured, and EoL systems

Protocol (SNMP), NetBIOS, Point\-to\-Point 

file\-sharing services, FTP, and misconfigured cloud 

Tunneling Protocol (PPTP), and internet\-accessible 

storage. Compromise of these systems allows 

• Weak or insecure cryptography

administrative login pages of routers, firewalls, 

attackers not only access to the data stored on 

• IoT, embedded devices, and operational 

VPNs, and other core networking and security 

them but also all future data sent through them.

technologies (OT)

appliances. Compromise of these assets can 

have substantial consequences for organizations, 

Database exposures and vulnerabilities make 

including the compromise of core business 

up 9% of exposures observed across the 250 

functions and applications, and the data 

organizations. Exposing a database with sensitive 

• Unencrypted logins and text protocols

• Development infrastructure

they contain.

information directly to the internet can dramatically 

• Business operations applications

increase the probability that your organization 

experiences a data breach. 

• Medical systems

NEXT CHAPTER

11

REMOTE ACCESS 
EXPOSURES 
LEAD TO 
RANSOMWARE

According to the 2022 Unit 42 Incident Response 

Report, the top suspected means of initial access 

for ransomware cases investigated by Unit 42 are 

software vulnerabilities (48%), followed by brute\-

force credential attacks (20%).2 The heavy use of 

software vulnerabilities matches the opportunistic 

behavior of ransomware actors, who typically 

scan the internet at scale for vulnerabilities and 

weak points. This approach, along with brute\-force 

credential attacks, focused on RDP.

04 NEXT CHAPTER

12

UNIT 42 \| CORTEX04

Remote Access Exposures Lead to Ransomware

Remote access services can 
be essential in today’s hybrid 
work environment, but their 
misconfiguration can pose 
significant risks. 

Figure 4 reveals that RDP is the most prevalent remote 

access service worldwide, accounting for over 40% of 

the exposed remote access services. The prevalence of 

remote access exposures on the overall public internet 

remains even when we focus on enterprise networks: 

85% of organizations analyzed in this report had at 

least one internet\-accessible RDP instance online 

during the month.

60%

40%

20%

0%

NAM

EMEA

JAPAC

RDP Server

RPCBind Server

SSH Server

Open SSH

PPTP Server

Other

Figure 4: Top five most common exposed remote access services by geography in the last 12 monthss

NEXT CHAPTER

13

04

Remote Access Exposures Lead to Ransomware

Unit 42 found that the average national 

Across over 600 incident response cases, the 

government organization had internet\-accessible 

2022 Unit 42 Incident Response Report found that 

RDP exposures for 10 distinct days in a month, 

50% of targeted organizations lacked multifactor 

providing attackers with ample opportunity to gain 

authentication (MFA) on key internet\-facing 

unauthorized access. The average professional 

systems. The prevalence of RDP exposures in each 

services organization had RDP exposed for a 

industry studied in this report, combined with the 

shorter duration but tended to have more distinct 

rarity of compensating controls like MFA, make it 

instances of RDP exposed. 

likely that ransomware attacks will continue for the 

foreseeable future.

Eight of the nine industries that Unit 42 studied 

had internet\-accessible RDP vulnerable to brute\-

force attacks for at least 25% of the month. 

The median financial services and state or local 

government organizations had RDP exposures for 

the entire month. 

\* Note: Medians are calculated across organizations in each industry.

Table 1: The Frequency and Duration of RDP Exposures for the Median Large Organization in Each Industry

NEXT CHAPTER

14

CLOUD 
DYNAMISM 
IS STRAINING 
SECURITY 
CONTROLS

To assess the dynamic nature of modern IT 

environments, Unit 42 studied the composition of 

new and existing services running in different cloud 

providers used by an organization over a period of 

six months.

05 NEXT CHAPTER

15

UNIT 42 \| CORTEX05 Cloud Dynamism Is Straining Security Controls

Cloud\-based IT infrastructure 
is always in a state of flux—
on average over 20% of 
externally accessible cloud 
services change every month 
across the 250 organizations, 
as illustrated in figure 5\. 

Without continuous visibility, it is easy to lose track 

of accidental misconfigurations and the steady 

spread of shadow IT within an organization.

Transportation \& Logistics

 27%

Insurance

Financial Services

High Technology

Federal Government

Healthcare

Professional \& Legal Services

Utilities \& Energy

Manufacturing

Wholesale \& Retail

State \& Local Government

Education

 24%

 24%

 23%

 22%

 21%

 20%

 20%

 19%

 18%

 17%

 15%

0%

10%

20%

30%

Figure 5: Median proportion of new services introduced by a typical company in each industry during a given month

NEXT CHAPTER

16

05 Cloud Dynamism Is Straining Security Controls

Transportation \& Logistics

 85%

Insurance

Financial Services

Wholesale \& Retail

Professional \& Legal Services

State \& Local Government

Federal Government

High Technology

Manufacturing

Healthcare

Utilities \& Energy

Education

 9%

 64%

 60%

 50%

 49%

 46%

 46%

 45%

 38%

 32%

 30%

0%

25%

50%

75%

100%

Figure 6: Median proportion of cloud\-hosted exposures that are high risk observed on a 
typical company’s attack surface in each industry during a given month

Upon discovering that one 
out of every five cloud\-based 
systems in an organization 
changes every month, Unit 42 
investigated the impact 
on the number of new 
security risks introduced 
within an organization. 

Figure 6 shows that, for most organizations, over 

45% of their high\-risk, cloud\-hosted exposures in 

a month were observed on new services that were 

not present on their organization’s attack surface in 

the prior month. Thus, the creation of new, publicly 

accessible cloud services, both intended and 

unauthorized, accounts for nearly half of all high\-

criticality exposures at a given time.

NEXT CHAPTER

17

CLOUD 
EXPOSURES 
DOMINATE MOST 
ORGANIZATIONS’ 
SECURITY RISKS

Cloud deployments offer cost savings and 

operational efficiencies, but organizations must 

also be aware of security risks and take appropriate 

measures to secure their cloud environments.

06 NEXT CHAPTER

18

UNIT 42 \| CORTEX06 Cloud Exposures Dominate Most Organizations’ Security Risks

According to our analysis, 
80% of security exposures were 
observed in cloud environments, 
as shown in figure 7\. 

This higher distribution of exposures in the cloud can 

be attributed to frequent misconfigurations, shared 

responsibilities, shadow IT, inherent connection to the 

internet, and lack of visibility into cloud assets.

Figure 7: Distribution of exposures (Critical, High, Medium) in the cloud versus on\-premises in 2022

NEXT CHAPTER

19

06 Cloud Exposures Dominate Most Organizations’ Security Risks

Cloud

On\-Premises

As seen in figure 8, nearly 
95% of EoL software systems 
exposed on the public 
internet of the organizations 
measured were found in cloud 
environments.

EOL Systems

Development Infrastructure

Weak or Insecure 
Cryptography

Remote Access Services

IT and Security Infrastructure

Unencrypted Logins 
and Text Protocols

Web Framework

Business Operations 
Applications

Insecure File Sharing

Databases

0%

25%

50%

75%

100%

Figure 8: Distribution of different categories of Exposures (Critical, High, 
Medium) in the Cloud vs. On\-Premises in the last 12 months

This suggests that organizations might be slower to 

• 89% of insecure file\-sharingfile sharing 

retire outdated systems that are publicly accessible 

exposures

in cloud environments than on\-premises ones, and 

also that it is comparatively easier for developers 

to create and deploy large volumes of new services 

with substantially outdated software in the cloud. 

Similarly, over 75% of publicly accessible 

software development infrastructure exposures 

were found in the cloud, making them attractive 

targets for attackers. 

Common exposures that are found primarily on\-

premises may inadvertently increase: 

• 67% of unencrypted logins and text 

protocol exposures 

• 93% of internet\-exposed databases 

While these exposures are being found primarily 

on\-premises, organizations should be cognizant of 

these exposures when migrating sensitive data to 

the cloud.

Any of these exposures being accessible over the 

public internet is a cause for concern since they can 

act as a toehold for attackers to gain unauthorized 

access to an organization’s network and access 

sensitive data.

NEXT CHAPTER

20

INDUSTRY 
ATTACK 
SURFACE 
BREAKDOWN

Last year, Palo Alto Networks published the 

2022 Cortex Xpanse Attack Surface Threat Report,4 

which included a study of attack surface exposures 

in different industry verticals. In this year’s report, 

Unit 42 provides an update for each sector, showing 

the frequency of exposures and explaining the 

potential consequence of a successful attack.

07 NEXT CHAPTER

21

UNIT 42 \| CORTEX07 Industry Attack Surface Breakdown

 34%

 31%

 22%

IT Security and 
Networking Infrastructure

Remote Access Services

IOT, Embedded Devices, 
and OT

File Sharing

 7%

Unencrypted Logins 
and Text Protocols

Unpatched, Misconfigured, 
and End of Life systems

 2%

 2%

Databases

 1%

Business Operations 
Applications

 1%

High Technology

Unit 42 observed that high\-tech companies 

security practices. Insecure implementation of SSH 

are unintentionally exposing several login and/

servers is the leading contributor to remote access 

or admin pages of critical IT as well as security 

exposures in this industry.

infrastructure, such as routers, switches, and 

firewalls, as shown in figure 9\. If these assets 

High\-tech companies are generally stronger 

are exploited successfully, attackers would have 

at keeping publicly accessible web servers 

the same ability to control the environment as a 

up to date. This is likely due to a correlation 

member of an IT team. Compounding the risk, 

between having a strong digital presence related 

credential reuse is common on IT and security 

to revenue\-generating operations and their 

infrastructure, which means that attacks can be 

security departments having better inventories of 

heavily automated and don’t require an unpatched 

intentionally public\-facing assets. Unfortunately, 

0%

10%

20%

30%

40%

vulnerability to succeed. 

this does not extend to assets deployed as shadow 

IT or IoT devices with no associated DNS.

Figure 9: Median distribution of top exposures in the high\-tech industry in 2022

Additionally, these companies rely heavily on 

remote access services, which amount to 31% 

of all the exposures for a typical company in this 

industry. This can be a significant attack vector 

due to accidental misconfigurations or inadequate 

NEXT CHAPTER

22

07 Industry Attack Surface Breakdown

National Governments

The top exposures for national governments are related 

to data security and IT infrastructure. As shown in 

figure 10, file sharing and database exposures account 

for over 46% of all the exposures in a typical national 

government organization. Misconfigured critical IT 

systems and internet\-accessible login and/or admin 

pages of routers, firewalls, VPNs, etc., were some of 

the common exposures found under this category. 

Insecure file sharing and databases are one of the most 

significant attack surface risks in national governments, 

above the rates for other organizations.

 28%

 23%

 23%

IT Security and 
Networking Infrastructure

File Sharing

Databases

Remote Access Services

 14%

Unencrypted Logins 
and Text Protocols

 6%

IOT, Embedded Devices, 
and OT

 4%

Development Infrastructure

 1%

Business Operations 
Applications

 1%

0%

10%

20%

30%

Figure 10: Median distribution of top exposures in national governments in 2022

NEXT CHAPTER

23

07 Industry Attack Surface Breakdown

Professional and 
Legal Services

Unencrypted FTP servers are ubiquitous in 

professional and legal services organizations, as 

shown in figure 11, opening several avenues for 

File Sharing

 50%

IT Security and Networking 
Infrastructure

 17%

data compromise. Additionally, the improper use of 

Remote Access Services

 11%

cloud\-based data storage and analysis systems for 

business information processing, visualization, and 

analytics leads to accidental exposures that provide 

Unencrypted Logins 
and Text Protocols

opportunities for attackers to steal critical information.

Databases

 7%

 7%

The higher rates of file\-sharing exposures for this 

sector are especially concerning. As part of business 

operations, these organizations must send and receive 

large volumes of files from clients, necessitating a large 

number of file\-transfer services to run their business. 

However, the sensitive nature of the files exchanged, 

combined with the number of exposed systems, 

makes targeting these systems especially valuable 

to attackers.

IOT, Embedded Devices, 
and OT

 5%

Business Operations 
Applications

 1%

Development Infrastructure

 1%

Web Framework 
Takeover

 1%

0%

20%

40%

60%

Figure 11: Median distribution of top exposures in the professional services industry in 2022

NEXT CHAPTER

24

07 Industry Attack Surface Breakdown

Healthcare

As healthcare companies undergo digital 

transformations, it is essential that they keep sensitive 

data, like protected health information (PHI), secure. 

The high rate of publicly exposed development 

environments, which are often misconfigured and 

vulnerable, gives attackers an opportunity to establish 

a foothold in the organization’s network. This access 

can lead to data breaches, unauthorized access, or 

even medical device failures, as shown in figure 12\.

Development Infrastructure

IT Security and Networking 
Infrastructure

 18%

 56%

Remote Access Services

 7%

Business Operations 
Applications

 6%

Unencrypted Logins 
and Text Protocols

 4%

IOT, Embedded Devices, 
and OT

Weak or Insecure 
Cryptography

 3%

 3%

File Sharing

 2%

Databases

 1%

0%

20%

40%

60%

Figure 12: Median distribution of top exposures in the healthcare industry in 2022

NEXT CHAPTER

25

07 Industry Attack Surface Breakdown

Utilities and Energy

Internet\-accessible IT infrastructure control panels 

account for nearly one out of two exposures in the 

utilities and energy sector, as shown in figure 13\. 

RDP servers make up 11% of the exposures and are 

the leading cause of remote access exposures in 

this sector. 

Particularly concerning is the elevated risk of IT 

networking systems that would allow attackers more 

direct access to the core, internal networks of these 

organizations. Even if the attackers are unable to 

cross to OT networks from IT networks, business 

interruptions on IT networks can still result in overall 

power and energy service disruption to the individuals 

and businesses that these organizations serve.

IT Security and 
Networking Infrastructure

 47%

Remote Access Services

 15%

File Sharing

IOT, Embedded Devices, 
and OT

 13%

 13%

Databases

 8%

Unencrypted Logins 
and Text Protocols

 3%

Business Operations 
Applications

 1%

0%

10%

20%

30%

40%

50%

Figure 13: Median distribution of top exposures in the utilities and energy industry in 2022

NEXT CHAPTER

26

07 Industry Attack Surface Breakdown

Manufacturing

IT Security and 
Networking Infrastructure

 48%

The most prevalent risks observed on the attack 

surface of manufacturing companies were IT, security, 

and networking infrastructure. By compromising 

core networks, attackers could cause significant 

operational disruptions, leading to production 

downtime, loss of revenue, andreputational damage 

with long\-lasting effects.

File Sharing

 19%

Remote Access Services

 12%

IOT, Embedded Devices, 
and OT

 8%

Unencrypted Logins 
and Text Protocols

 6%

Business Operations 
Applications

 3%

Databases

 3%

Other

 1%

0%

10%

20%

30%

40%

50%

Figure 14: Median distribution of top exposures in the manufacturing industry in 2022

NEXT CHAPTER

27

07 Industry Attack Surface Breakdown

Education

Educational institutions were most likely to 

expose IT, security, and networking infrastructure, 

followed by file\-sharing services and remote 

access services. Unit 42 also observed business 

operations applications and IoT at a higher rate 

than other sectors. Risky exposures like these can 

lead to a serious data breach, such as: 

• The theft of sensitive personal, academic, 

and financial information.

• The disruption of essential 

educational services.

• Financial losses from investigation, restoration, 

and potential fines due to breaches.

IT Security and 
Networking Infrastructure

 31%

File Sharing

 26%

Remote Access Services

 14%

Business Operations 
Applications

IOT, Embedded Devices, 
and OT

 11%

 10%

Unencrypted Logins 
and Text Protocols

 4%

Databases

 3%

Web Framework 
Takeover

 1%

0%

10%

20%

30%

40%

Figure 15: Median distribution of top exposures in the education industry in 2022

NEXT CHAPTER

28

07 Industry Attack Surface Breakdown

US State and 
Local Governments

In a Palo Alto Networks–sponsored survey of IT 

leaders from US state and local governments, nearly 

one\-third of respondents did not know whether 

remote work had impacted their organization.5 Unit 

42 found that remote access services are responsible 

for 24% of remote access risks in state and local 

governments, as shown in figure 16\. Many state and 

local governments also exposed IT, networking, and 

security infrastructure and file\-sharing services. 

State and local governments should secure their 

networks due to the critical importance of the data 

and services they handle. These systems frequently 

house sensitive information, such as citizens’ personal 

data, infrastructure details, and financial records. If 

compromised, this can result in breaches of privacy, 

identity theft, and significant financial and reputation 

damage. Further consequences could include the 

disruption of critical public services, ranging from 

emergency response to utility provisioning.

IT Security and 
Networking Infrastructure

 45%

Remote Access Services

 24%

File Sharing

 12%

IOT, Embedded Devices, 
and OT

Business Operations 
Applications

 6%

 6%

Unencrypted Logins 
and Text Protocols

 5%

Databases

 2%

0%

10%

20%

30%

40%

50%

Figure 16: Median distribution of top exposures in state and local government in 2022

NEXT CHAPTER

29

07 Industry Attack Surface Breakdown

Transportation and Logistics

Compromise of remote access services, 

which make up 13% of all the exposures in 

this industry, as shown in figure 17, can lead to 

disruptions in transportation networks, delays 

in delivery schedules, and potential theft or 

manipulation of sensitive data. Database exposures 

are responsible for one out of every four critical 

issues in a logistics company.

These exposures can result in unauthorized 

access to sensitive information, including shipping 

manifests, customer contacts, and operational data 

that can lead to potential theft or manipulation of 

sensitive cargo data. Additionally, this industry also 

relies on outdated and unencrypted FTP servers 

(7% of all exposures are legacy FTP servers) to 

share data, which provides attackers with several 

opportunities for data theft.

IT Security and 
Networking Infrastructure

Databases

File Sharing

 34%

 27%

 22%

Remote Access Services

 13%

IOT, Embedded Devices, 
and OT

Unencrypted Logins 
and Text Protocols

 2%

 2%

0%

10%

20%

30%

40%

Figure 17: Median distribution of top exposures in the transport and logistics industry in 2022

NEXT CHAPTER

30

07 Industry Attack Surface Breakdown

Finance

Financial institutions most frequently expose 

file\-sharing services, followed by IT, security, 

networking infrastructure, and remote access 

services. Financial institutions must prioritize 

network security due to the sensitive nature of the 

data they handle and the potential consequences 

of a breach. These institutions are custodians of 

vast amounts of personal and financial data, and 

any compromise can lead to substantial monetary 

loss, identity theft, fraud, and a loss of customer 

trust that can be irreparable. 

Moreover, as financial systems interconnect 

globally, a security breach can have systemic 

implications, potentially destabilizing the financial 

ecosystem. Hence, robust cybersecurity measures 

are paramount in protecting the integrity and 

confidentiality of data, ensuring the continuity of 

services, maintaining customer trust, and upholding 

the overall stability of the financial system.

File Sharing

IT Security and 
Networking Infrastructure

 38%

 28%

Remote Access Services

 16%

Unencrypted Logins 
and Text Protocols

 7%

Databases

 3%

IOT, Embedded Devices, 
and OT

Web Framework 
Takeover

 2%

 2%

Other

 2%

Business Operations 
Applications

 1%

Development Infrastructure

 1%

0%

10%

20%

30%

40%

Figure 18: Median distribution of top exposures in the finance industry in 2022

NEXT CHAPTER

31

07 Industry Attack Surface Breakdown

Wholesale and Retail

Wholesale and retail organizations had a remarkably 

high proportion of remote access services, which are 

likely exposed to help organizations efficiently manage 

the IT at a large number of distinct physical locations. 

Misconfigured remote access services carry substantial 

risk since they give attackers an opportunity to gain 

unauthorized access to the organization’s network. 

Securing network infrastructure is of paramount 

importance for retail businesses due to the sensitive 

nature of the data they handle and the potential impact 

on their operations. Retailers collect and store vast 

amounts of customer data, including personal and 

financial information. 

A security breach can lead to significant data loss, 

fraud, and a breach of customer trust that can damage 

the brand’s reputation. Additionally, retailers rely 

heavily on IT systems for inventory management, sales 

processing, and other critical operations. A disruption 

due to a cyberattack can lead to substantial financial 

losses and operational inefficiencies.

Remote Access Services

 78%

IT Security and 
Networking Infrastructure

 9%

 File Sharing

 4%

IOT, Embedded Devices, 
and OT

 3%

Unencrypted Logins 
and Text Protocols

 2%

Web Framework 
Takeover

 1%

Business Operations 
Applications

 1%

Databases

 1%

Development Infrastructure

 1%

0%

20%

40%

60%

80%

Figure 19: Median distribution of top exposures in the wholesale and retail industry in 2022

NEXT CHAPTER

32

CONCLUSION

Organizations across all industries face significant 

By implementing the recommendations outlined 

challenges and risks due to growing attack 

in the report, organizations can actively manage 

surfaces. Modern threat actors are experts at 

their attack surfaces and keep their organization 

exploiting the path of least resistance to gain 

safe. The following section provides detailed 

access to victims’ environments. 

recommendations to help organizations strengthen 

their cybersecurity posture and actively manage 

To manage and secure their attack surfaces, 

their dynamic attack surfaces.

organizations must adopt a proactive and holistic 

approach. This involves continuous visibility and 

prioritizing remediation to maintain control over 

their internet\-facing infrastructure. 

08 NEXT CHAPTER

33

UNIT 42 \| CORTEXRecommendations

Attackers are using automation and opportunity 

at scale, and defenders must do the same to be 

convergent with the threats they face. Here are our 

recommendations:

Gain continuous visibility over all assets 

Secure remote access services 

Ensure that your organization has a comprehensive, real\-time 

Implement strong authentication methods, such as MFA, and 

understanding of all internet\-accessible assets, including cloud\-

monitor remote access services for signs of unauthorized access 

based systems and services, to effectively manage your attack 

or brute\-force attacks. Our Prisma Access solutions can help 

surface. This is important to maintain even as that attack surface 

enable Zero Trust Network Access and provide other SASE 

changes every day. Cortex Xpanse helps your organization actively 

capabilities your organization needs.

discover, learn about, and respond to risks in all connected systems 

and exposed services.

Prioritize remediation 

Address cloud misconfigurations 

Regularly review and update cloud configurations to ensure they align 

with best practices and address any potential security risks. Prisma 

Focus on addressing the most critical vulnerabilities and exposures, 

Cloud helps security and DevOps teams collaborate and drive secure 

such as those with a high Common Vulnerability Scoring System 

cloud\-native application development and deployment. This is a great 

(CVSS) score, which accounts for severity, and an Exploit Prediction 

way for security and DevOps teams to build a working relationship 

Scoring System (EPSS) score, which accounts for likelihood, to 

that’s good for everyone.

reduce the likelihood of successful cyberattacks.

Get the help you need 

Stay informed about new vulnerabilities, exploits, and threat 

If attack surface management is new to your organization, or you’d 

actors. Continuously assess your organization’s attack surface for 

like help with improving your program, a Unit 42 Attack Surface 

potential risks. Follow the Unit 42 blog for our insights, and if you’d 

Assessment can jump\-start your journey.

like a consulting relationship, consider a services retainer for threat 

landscape briefings and incident response services.

Monitor for emerging threats 

09 NEXT CHAPTER

34

UNIT 42 \| CORTEXMETHODOLOGY

10

Unit 42 and Cortex Xpanse collected petabytes 

The datasets used for this were from March 31, 

of information on internet\-accessible exposures 

2022, to March 31, 2023\. 

across 250 organizations in 2022 and 2023\. While 

Unit 42 used the data to analyze issues associated 

The research team only accounted for exposures 

with these exposures, the research team used 

where the product or vendor or the Common 

the last six months of 2022 to study the nature of 

Platform Enumeration (CPE) could be inferred, 

the change of cloud services and the associated 

and the data points were consistent across the 

risks they create in a typical organization across 

fingerprinting source and the vulnerabilities data 

industries because six months yielded sufficient 

source. To identify the steady median for analysis, 

data for computation.

the research team used a rolling 10\-day median, 

which eliminated any outlier bias in our VPN device 

For each industry category, the research team 

observations. 

included data from at least five large organizations 

in that industry. Cortex Xpanse was used to 

For delineation between cloud and on\-premises 

classify a system as on\-premises or cloud, 

assets, on\-premises assets of an organization are 

depending on a variety of factors. To do this work 

publicly accessible systems and services owned 

with speed, precision, and scale, the research 

by an organization with statically assigned IP 

team leveraged a machine learning model for 

addresses, and cloud assets are publicly accessible 

the accurate attribution of assets to different 

systems and services leased by an organization in 

organizations. The model was supervised by a 

dynamic IP space, not including multitenant, SaaS\-

team of attack surface analysts that support 

delivered services.

Cortex Xpanse.

To map the timeline of the attack, the research 

team combined our data with third\-party data for 

the “time elapsed before attack” analysis. 

35

UNIT 42 \| CORTEXAbout Palo Alto Networks

About Cortex Xpanse

About the Unit 42 Attack Surface Assessment

About Unit 42

Palo Alto Networks is the world’s cybersecurity 

Cortex® Xpanse™ is an active attack surface 

The Unit 42 Attack Surface Assessment helps 

Palo Alto Networks Unit 42™ brings together 

leader. We innovate to outpace cyberthreats 

management solution that helps your organization 

you identify and manage exposure, mitigate risk, 

world\-renowned threat researchers, elite incident 

so organizations can embrace technology 

actively discover, learn about, and respond to 

and bolster your security posture now and in the 

responders, and expert security consultants to 

with confidence. We provide next\-generation 

unknown risks in all connected systems and 

future. This assessment provides an expert view 

create an intelligence\-driven, response\-ready 

cybersecurity to thousands of customers globally, 

internet\-accessible services. 

of your internet\-connected assets with prioritized 

organization that’s passionate about helping 

across all sectors. 

recommendations to improve your defenses so you 

you proactively manage cyber risk. Together, 

Cortex Xpanse protects the U.S. Department 

can remediate issues before they can be exploited. 

our team serves as your trusted advisor to help 

Our best\-in\-class cybersecurity platforms and 

of Defense, all six branches of the U.S. military, 

assess and test your security controls against real\-

services are backed by industry\-leading threat 

several federal agencies, and several large 

With our security expertise and Cortex Xpanse 

world threats, transform your security strategy 

intelligence and strengthened by state\-of\-the\-art 

enterprises like Accenture, AT\&T, American 

data, you will find previously unknown assets, 

with a threat\-informed approach, and respond to 

automation. Whether deploying our products to 

Express, AIG, Pfizer, and over 200 others.

including shadow IT infrastructure, to identify 

incidents in record time so that you get back to 

enable the Zero Trust Enterprise, responding to 

vulnerabilities and security gaps. You get 

business faster. 

a security incident, or partnering to deliver better 

For more information, visit 

recommendations tailored to your specific 

security outcomes through a world\-class partner 

www.paloaltonetworks.com/cortex/cortex\-xpanse

business and security concerns. 

Visit paloaltonetworks.com/unit42

ecosystem, we’re committed to helping ensure 

each day is safer than the one before. It’s what 

makes us the cybersecurity partner of choice. 

For more information, visit 

www.paloaltonetworks.com

Identifying and remediating issues in your attack 

surface can reduce insurance premiums and show 

measurable progress to regulators, board members, 

and other stakeholders. If your organization needs 

help with starting or advancing your attack surface 

management program, the Unit 42 Attack Surface 

Assessment can help.6

3000 Tannery Way

Santa Clara, CA 95054

Main 

Sales 

\+1\.408\.753\.4000

\+1\.866\.320\.4788

Support 

\+1\.866\.898\.9087

References:

 1\. 2021 Cortex Xpanse Attack Surface Threat Report, Palo Alto Networks, May 10, 2021\. 2\. 2022 Unit 42 Incident Response Report, Palo Alto Networks, July 26, 2022\. 3\. Ibid.
4\. 2022 Cortex Xpanse Attack Surface Threat Report, Palo Alto Networks, July 19, 2022\. 5\. Smart Investments for Getting Ahead of Ransomware, Center for Digital Government, February 2022\. 
6\. “Unit 42 Attack Surface Assessment” datasheet, Palo Alto Networks, January 31, 2023\. 

© 2023 Palo Alto Networks, Inc. Palo Alto Networks is a registered trademark of Palo Alto Networks. A list of our trademarks can be found at www.paloaltonetworks.com/company/trademarks.html. 
All other marks mentioned herein may be trademarks of their respective companies. 2023 Unit 42 Ransomware and Extortion Report 03/2023\. 

36